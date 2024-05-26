"""
# DataTransformColumnsWidgets
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
from dfcleanser.common.cfg import DataTransform_ID


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
# -                  Transfoprm Columns Widget                    -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class DataTransform_transform_columns_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_transform_columns_Widget][init] "))

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_transform_columns_Widget] dftitle ; ",self.dftitle))

        self.init_form()

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_transform_columns_Widget] end"))

    def reload_banner(self) :
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_transform_columns_Widget][reload_data] "))

        self.init_command_bar()

    def init_form(self):  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_transform_columns_Widget][init_form]"))

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

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_transform_columns_Widget][init_form] end"))


    def init_command_bar(self):  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_transform_columns_Widget][init_command_bar]"))

        from dfcleanser.sw_utilities.dfc_qt_model import build_button_bar
        
        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton

        self.rename_button          =   QPushButton()   
        self.drop_button            =   QPushButton()    
        self.reorder_button         =   QPushButton()   
        self.save_button            =   QPushButton()    
        self.copy_button            =   QPushButton()   
        self.apply_fn_button        =   QPushButton()   
        self.map_button             =   QPushButton()    
        self.dummies_button         =   QPushButton()   
        self.make_cat_button        =   QPushButton()    
        self.datatype_button        =   QPushButton()   
        self.help_button            =   QPushButton()
        self.return_button          =   QPushButton()   

        button_bar1_button_list     =   [self.rename_button,self.drop_button,self.reorder_button,self.save_button,self.copy_button,self.apply_fn_button,
                                        self.map_button,self.dummies_button,self.make_cat_button,self.datatype_button,self.help_button,self.return_button ] 
        button_bar1_text_list       =   ["Rename\nColumns","Drop\nColumns","Reorder\nColumns","Save\nColumns","Copy\nColumns","Apply\nfn To\n Column",
                                         "Map\nColumns","Dummies\nFor\nColumn","Make\nColumn\nCategorical","Change\nColumn\nDatatype","Help","Return"]
        button_bar1_size_list       =   [88,70]
        button_bar1_tool_tip_list   =   ["Rename Columns","Drop Columns","Reorder Columns","Save Columns","Copy Columns","Apply fn To Column",
                                         "Map Columns","Dummies For Column","Make Column Categorical","Column Datatype","Help","Return"]
        button_bar1_stylesheet      =   "background-color:#0c4ca7; color:white; font-size: 11px; font-weight: bold; font-family: Tahoma; "
        button_bar1_connect_list    =   [self.rename_column,self.drop_column,self.reorder_column,self.save_column,self.copy_column,self.apply_fn_to_column,
                                         self.map_column,self.dummies_for_column,self.make_cat_column,self.datatype_column,self.help_column,self.return_from_cleanse_column]

        self.button_bar_1           =   QHBoxLayout()
        build_button_bar(self.button_bar_1,button_bar1_button_list,button_bar1_text_list,button_bar1_size_list,button_bar1_tool_tip_list,button_bar1_stylesheet,button_bar1_connect_list,)

        cmdbarLayout    =   QVBoxLayout()
        cmdbarLayout.addLayout(self.button_bar_1)
        cmdbarLayout.addStretch()
        
        from dfcleanser.sw_utilities.dfc_qt_model import clearLayout
        clearLayout(self.parent.form.DataTransformCmdbarLayout)
        self.parent.form.DataTransformCmdbarLayout.addLayout(cmdbarLayout)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_transform_columns_Widget][init_command_bar] end"))


    # -----------------------------------------------------------------#
    # -              Transfoprm Columns Widget methods                -#
    # -----------------------------------------------------------------#

    def rename_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_transform_columns_Widget][rename_column]"))

        self.parent.display_rename_column_form()
   
    def drop_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_transform_columns_Widget][drop_column]"))

        self.parent.display_drop_column()
    
    def reorder_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_transform_columns_Widget][reorder_column]"))

        self.parent.display_reorder_column()

    def save_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_transform_columns_Widget][save_column]"))

        self.parent.display_save_columns()        
 
    def copy_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_transform_columns_Widget][copy_column]"))
        
        self.parent.display_copy_column()        

    def apply_fn_to_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_transform_columns_Widget][apply_fn_to_column]"))

        self.parent.display_apply_fn_column()

    def map_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_transform_columns_Widget][map_column]"))
        
        self.parent.display_map_column()

    def dummies_for_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_transform_columns_Widget][dummies_for_column]"))

        self.parent.display_dummies_column()

    def make_cat_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_transform_columns_Widget][make_cat_column]"))

        self.parent.display_category_column()

    def datatype_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_transform_columns_Widget][datatype_column]"))

        self.parent.display_change_column_datatype(None)
    
    def help_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_transform_columns_Widget][return_from_cleanse_column]"))

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_COLS_ID
        display_url(TRANSFORM_COLS_ID)


    def return_from_cleanse_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_transform_columns_Widget][return_from_cleanse_column]"))

        self.parent.init_stacked_index()


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                Transform Rename Column Widgets                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#



# -----------------------------------------------------------------#
# -              Transform Rename Column Form Widget              -#
# -----------------------------------------------------------------#

class DataTransform_rename_column_form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_rename_columns_Widget][init] dftitle : ",self.dftitle))

        self.init_form()

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_rename_column_form_Widget] end"))

    def reload_data(self,parent,dftitle) :
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_rename_columns_Widget][reload_data] "))

        self.parent         =   parent
        self.dftitle        =   dftitle

    def init_form(self):  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_rename_column_form_Widget][init_form]"))

        from PyQt5.QtWidgets import QVBoxLayout

        self.DataTransformRenameLayout     =   QVBoxLayout()

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms              =    [self.dftitle,15,self.select_column_to_rename]
        self.colsStats     =    DataInspectionColumnsStatsTable(parms)

        if(self.colsStats.num_rows < 15) :
            new_height  =   45 + (self.colsStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (15 * DEFAULT_ROW_HEIGHT)

        self.colsStats.setMinimumHeight(new_height)
        self.colsStats.setMaximumHeight(new_height)

        import dfcleanser.Qt.data_transform.DataTransformColumnsModel as DTCM

        form_parms      =   [DTCM.rename_column_input_id,DTCM.rename_column_input_idList,DTCM.rename_column_input_labelList,DTCM.rename_column_input_typeList,DTCM.rename_column_input_placeholderList,DTCM.rename_column_input_reqList]
        comboMethods    =   None
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.rename_column_name,self.universal_column_names,self.return_from_rename_column]
        cfg_parms       =   None
        form_title      =   "\n\nRename Column Name\n"
        form_width      =   550

        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.rename_form     =   dfcleanser_input_form_Widget(form_parms)

        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.DataTransformRenameFormLayout     =   QVBoxLayout()
        self.DataTransformRenameFormLayout.addWidget(self.colsStats)
        self.DataTransformRenameFormLayout.addWidget(self.rename_form)
        self.DataTransformRenameFormLayout.addStretch()

        self.setLayout(self.DataTransformRenameFormLayout)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_rename_column_form_Widget][init_form] end"))

    def select_column_to_rename(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_rename_columns_Widget][select_column_to_rename]"))

        row_number      =   None
        column_number   =   None

        for idx in self.colsStats.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_rename_columns_Widget][select_column_to_rename] ",row_number,column_number))

        model   =   self.colsStats.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :    
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_rename_columns_Widget][select_column_to_rename] : colname [",cell,"]"))

        self.rename_form.set_form_input_value_by_index(0,cell)

    def rename_column_name(self) :

        old_name    =   self.rename_form.get_form_input_value_by_index(0)
        new_name    =   self.rename_form.get_form_input_value_by_index(1)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_rename_column_form_Widget][rename_column_name] : old name : new_name ",old_name,new_name))

        from dfcleanser.Qt.data_transform.DataTransformColumnsControl import process_rename_column
        process_rename_column(self.dftitle,old_name,new_name)
        
        self.colsStats.reload_data()

    def universal_column_names(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_rename_column_form_Widget][universal_column_names] : "))

        self.parent.display_universal_rename_column_form() 

    def return_from_rename_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_rename_column_form_Widget][return_from_rename_column] "))

        self.parent.display_transform_columns()

# -----------------------------------------------------------------#
# -              Transform Rename Column Form Widget              -#
# -----------------------------------------------------------------#

class DataTransform_universal_column_form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_universal_column_form_Widget][init] dftitle : ",self.dftitle))

        self.init_form()

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_universal_column_form_Widget] end"))

    def reload_data(self,parent,dftitle) :
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            padd_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_universal_column_form_Widget][reload_data] "))

        self.parent         =   parent
        self.dftitle        =   dftitle

    def init_form(self):  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_universal_column_form_Widget][init_form]"))

        from PyQt5.QtWidgets import QVBoxLayout

        self.DataTransformRenameLayout     =   QVBoxLayout()

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms              =    [self.dftitle,15,self.select_column_to_rename]
        self.colsStats     =    DataInspectionColumnsStatsTable(parms)

        if(self.colsStats.num_rows < 15) :
            new_height  =   45 + (self.colsStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (15 * DEFAULT_ROW_HEIGHT)

        self.colsStats.setMinimumHeight(new_height)
        self.colsStats.setMaximumHeight(new_height)

        import dfcleanser.Qt.data_transform.DataTransformColumnsModel as DTCM

        form_parms      =   [DTCM.universal_column_input_id,DTCM.universal_column_input_idList,DTCM.universal_column_input_labelList,
                             DTCM.universal_column_input_typeList,DTCM.universal_column_input_placeholderList,DTCM.universal_column_input_reqList]
        comboMethods    =   None
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.check_universal_names,self.make_universal_names,self.return_from_universal_column]
        cfg_parms       =   None
        form_title      =   "Universal Column Names\n"
        form_width      =   550

        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.universal_form     =   dfcleanser_input_form_Widget(form_parms)

        self.rename_form.set_form_input_value_by_index(0,"_")
        
        from PyQt5.QtWidgets import QTextEdit
        self.dfc_file_content    =   QTextEdit()
        self.dfc_file_content.setReadOnly(True)
        self.dfc_file_content.setStyleSheet("font-size: 12px; font-weight: normal; font-family: Tahoma; ")

        warning_text   =   "Some data stores such as sql servers(PostGres) can not handle a leading or trailing blank in a column name.\n"
        warning_text1  =   "Some data stores using xml can not handle embedded blanks in a column name.\n"
        warning_text2  =   "The safest universal column name shouk not have either. Special chars such as #,%,@ .. should be removed as well.\n"
        final_warning   =   warning_text + warning_text1 + warning_text2

        self.dfc_file_content.setText(final_warning)

        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.DataTransformRenameFormLayout     =   QVBoxLayout()
        self.DataTransformRenameFormLayout.addWidget(self.colsStats)
        self.DataTransformRenameFormLayout.addWidget(self.universal_form)
        self.DataTransformRenameFormLayout.addWidget(self.dfc_file_content)
        self.DataTransformRenameFormLayout.addStretch()

        self.setLayout(self.DataTransformRenameFormLayout)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_universal_column_form_Widget][init_form] end"))

    def select_column_to_rename(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_universal_column_form_Widget][select_column_to_rename]"))

        row_number      =   None
        column_number   =   None

        for idx in self.colsStats.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_universal_column_form_Widget][select_column_to_rename] ",row_number,column_number))

        model   =   self.colsStats.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :    
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_universal_column_form_Widget][select_column_to_rename] : colname [",cell,"]"))

        self.rename_form.set_form_input_value_by_index(0,cell)

    def check_universal_names(self) :

        old_name    =   self.rename_form.get_form_input_value_by_index(0)
        new_name    =   self.rename_form.get_form_input_value_by_index(1)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_universal_column_form_Widget][check_universal_names] : old name : new_name ",old_name,new_name))

        from dfcleanser.Qt.data_transform.DataTransformColumnsControl import process_rename_column
        process_rename_column(self.dftitle,old_name,new_name)
        
        self.colsStats.reload_data()

    def make_universal_names(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_universal_column_form_Widget][make_universal_names] : "))

        #self.parent.display_universal_column_names() 

    def return_from_universal_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_universal_column_form_Widget][return_from_universal_column] "))

        self.parent.display_transform_columns()

      

# -----------------------------------------------------------------#
# -             Transform Rename Column Form Widget               -#
# -----------------------------------------------------------------#

class DataTransform_drop_column_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_drop_column_Widget][init] "))

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]   

        self.init_form()

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_drop_column_Widget] end"))

    def reload_data(self,parent,dftitle) :
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_drop_column_Widget][reload_data] "))

        self.parent         =   parent
        self.dftitle        =   dftitle


    def init_form(self):  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_drop_column_Widget][init_form]"))

        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.DataTransformDropLayout     =   QVBoxLayout()

        from PyQt5.QtWidgets import QLabel
        drop_column_title_label   =   QLabel()
        drop_column_title_label.setText("\n\nColumn To Drop\n")
        drop_column_title_label.setAlignment(Qt.AlignCenter)
        drop_column_title_label.resize(480,50)
        drop_column_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.DataTransformDropLayout.addWidget(drop_column_title_label)


        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms              =    [self.dftitle,15,self.select_column_to_drop]
        self.colsStats     =    DataInspectionColumnsStatsTable(parms)

        if(self.colsStats.num_rows < 10) :
            new_height  =   45 + (self.colsStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (10 * DEFAULT_ROW_HEIGHT)

        self.colsStats.setMinimumHeight(new_height)
        self.colsStats.setMaximumHeight(new_height)

        self.DataTransformDropLayout.addWidget(self.colsStats)
        self.DataTransformDropLayout.addStretch()


        self.setLayout(self.DataTransformDropLayout)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_drop_columns_Widget][init_form] end"))


    # -----------------------------------------------------------------#
    # -              Transfoprm Columns Widget methods                -#
    # -----------------------------------------------------------------#

    def select_column_to_drop(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_drop_columns_Widget][select_column_to_drop]"))
   
        row_number      =   None
        column_number   =   None

        for idx in self.colsStats.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_drop_columns_Widget][select_column_to_drop] ",row_number,column_number))

        model   =   self.colsStats.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :    
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_drop_columns_Widget][select_column_to_drop] : colname [",cell,"]"))

        from dfcleanser.Qt.data_transform.DataTransformColumnsControl import process_drop_column
        process_drop_column(self.dftitle,cell)

        self.colsStats.reload_data()



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                  Transform add Column Widgets                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -                Transform add Column Form Widget               -#
# -----------------------------------------------------------------#

class DataTransform_add_column_form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   None  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_columns_Widget][init] "))

        self.init_form()

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_form_Widget] end"))

    def reload_data(self,parent,dftitle,colname) :
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_rename_columns_Widget][reload_data] "))

        self.parent         =   parent
        self.dftitle        =   dftitle
        #self.colname        =   colname

    def init_form(self):  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_form_Widget][init_form]"))

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms              =    [self.dftitle,15,self.select_column_to_use]
        self.colsStats     =    DataInspectionColumnsStatsTable(parms)

        if(self.colsStats.num_rows < 15) :
            new_height  =   45 + (self.colsStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (15 * DEFAULT_ROW_HEIGHT)

        self.colsStats.setMinimumHeight(new_height)
        self.colsStats.setMaximumHeight(new_height)

        from PyQt5.QtWidgets import QLabel
        note_label   =   QLabel()
        note_label.setText("\nDouble click on column to be used as source of new column\n")
        note_label.setAlignment(Qt.AlignCenter)
        note_label.resize(480,50)
        note_label.setStyleSheet("font-size: 12px; font-weight: bold; font-family: Arial; ")

        import dfcleanser.Qt.data_transform.DataTransformColumnsModel as DTCM

        form_parms      =   [DTCM.add_column_input_id,DTCM.add_column_input_idList,DTCM.add_column_input_labelList,DTCM.add_column_input_typeList,DTCM.add_column_input_placeholderList,DTCM.add_column_input_reqList]
        comboMethods    =   None
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.get_column_values_from_fns, self.get_column_values_from_code, self.return_from_add_column,self.help_for_add_column]
        cfg_parms       =   None
        form_title      =   "\n\nAdd New Column\n"
        form_width      =   1000

        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.add_form     =   dfcleanser_input_form_Widget(form_parms)

        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.DataTransformAddFormLayout     =   QVBoxLayout()
        self.DataTransformAddFormLayout.addWidget(self.colsStats)
        self.DataTransformAddFormLayout.addWidget(note_label)
        self.DataTransformAddFormLayout.addWidget(self.add_form)
        self.DataTransformAddFormLayout.addStretch()

        self.setLayout(self.DataTransformAddFormLayout)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_form_Widget][init_form] end"))

    def select_column_to_use(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_drop_columns_Widget][select_column_to_use]"))
   
        row_number      =   None
        column_number   =   None

        for idx in self.colsStats.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_drop_columns_Widget][select_column_to_drop] ",row_number,column_number))

        model   =   self.colsStats.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :    
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_drop_columns_Widget][select_column_to_drop] : colname [",cell,"]"))

        self.colname    =   cell

        current_columns     =   self.add_form.get_form_input_value_by_index(0)

        #new_column_list     =   self.add_form.get_form_input_value_by_index(0)

        if(len(current_columns) == 0) :
            new_column_list     =   "[" + self.colname + "]"
        else :
            new_column_list     =   current_columns[:(len(current_columns)-1)] + ", " + self.colname + "]"

        self.add_form.set_form_input_value_by_index(0,new_column_list)    

    def get_column_values_from_fns(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_form_Widget][get_column_values_from_fns] ")

        self.new_colname    =   self.add_form.get_form_input_value_by_index(1)

        if( len(self.new_colname) == 0) :

            title       =   "dfcleanser error"       
            status_msg  =   "[get_column_values_from_code] no newcolname "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

        else :

            self.parent.display_add_colum_from_fns(self.new_colname)

    def get_column_values_from_code(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_form_Widget][get_column_values_from_code] "))

        self.new_colname    =   self.add_form.get_form_input_value_by_index(1)

        if( len(self.new_colname) == 0) :

            title       =   "dfcleanser error"       
            status_msg  =   "[get_column_values_from_code] no newcolname "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)


        else :
            self.parent.display_add_colum_from_user_code(self.new_colname) 

    def return_from_add_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_rename_column_form_Widget][return_from_add_column] "))

        self.parent.display_add_column()

    def help_for_add_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_rename_column_form_Widget][help_for_add_column] "))

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_COLS_ADD_FILE_ID
        display_url(TRANSFORM_COLS_ADD_FILE_ID)
  
# -----------------------------------------------------------------#
# -                Transform add Column Form Widget               -#
# -----------------------------------------------------------------#

class DataTransform_add_column_from_fns_form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.new_colname    =   dfparms[2]  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_fns_form_Widget][init] "))

        self.init_form()

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_form_Widget] end"))

    def reload_data(self,parent,dftitle,new_colname) :
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_fns_form_Widget][reload_data] "))

        self.parent         =   parent
        self.dftitle        =   dftitle
        self.new_colname    =   new_colname

    def init_form(self):  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_fns_form_Widget][init_form]"))

        import dfcleanser.Qt.data_transform.DataTransformColumnsModel as DTCM

        form_parms      =   [DTCM.add_column_dfc_fn_input_id,DTCM.add_column_dfc_fn_input_idList,DTCM.add_column_dfc_fn_input_labelList,DTCM.add_column_dfc_fn_input_typeList,DTCM.add_column_dfc_fn_input_placeholderList,DTCM.add_column_dfc_fn_input_reqList]
        comboMethods    =   [self.select_add_dfc_fn]
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.add_column_from_fns, self.return_from_add_column_from_fns, self.help_for_add_column_from_fns]
        cfg_parms       =   None
        form_title      =   "\n\nAdd New Column from dfc fns\n"
        form_width      =   600

        selectDicts     =   []
        
        fns     =   []
        from dfcleanser.sw_utilities.GenericFunctionsModel import genfns, genfns_with_parms
        for i in range(len(genfns)) :
            fns.append(genfns[i])
        
        for i in range(len(genfns_with_parms)) :
            fns.append(genfns_with_parms[i])
            
        dfc_fn  =   fns[0]    
        
        lambdas         =   {"default":dfc_fn,"list":fns}
        selectDicts.append(lambdas)


        form_parms.append(selectDicts)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.add_form     =   dfcleanser_input_form_Widget(form_parms)

        self.add_form.set_form_input_value_by_index(0,self.new_colname)

        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.DataTransformAddFormLayout     =   QVBoxLayout()
        self.DataTransformAddFormLayout.addWidget(self.add_form)
        self.DataTransformAddFormLayout.addStretch()

        self.setLayout(self.DataTransformAddFormLayout)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_fns_form_Widget][init_form] end"))

    def select_add_dfc_fn(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_fns_form_Widget][select_add_dfc_fn] "))

        self.dfc_fn     =   self.add_form.get_form_input_value_by_index(1) 
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_dfc_fn_form_Widget][select_dfc_fn] : self.dfc_fn ",self.dfc_fn))

        from dfcleanser.sw_utilities.GenericFunctionsModel import genfns, genfns_with_parms
        if(self.dfc_fn in genfns)   :
            parms_dict   =   "{}"   
        else :

            open_paren      =     self.dfc_fn.find("(") 
            close_paren     =     self.dfc_fn.find(")") 

            parms_list      =   self.dfc_fn[(open_paren+1):(close_paren)]

            parms           =   []

            if("," in parms_list) :
                parms   =   parms_list.split(",")
            else :
                parms.append(parms_list)

            parms_dict  =   "{ "
            for i in range(len(parms)) :
                parms_dict  =   parms_dict + "'" + parms[i] + "' : " + str(parms[i]) + "Value "
                if(len(parms) == 1) :
                   parms_dict  =   parms_dict + "}"  
                else :
                    if(i == (len(parms) -1)) :
                        parms_dict  =   parms_dict + "}"
                    else :
                        parms_dict  =   parms_dict + ", "       

        self.add_form.set_form_input_value_by_index(2,parms_dict)

    def add_column_from_fns(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_fns_form_Widget][add_column_from_fns] "))

        self.new_colname    =   self.add_form.get_form_input_value_by_index(0)
        self.dfc_fn         =   self.add_form.get_form_input_value_by_index(1)
        self.fn_parms       =   self.add_form.get_form_input_value_by_index(2)

        from dfcleanser.data_transform.DataTransformColumnsControl import process_apply_dfc_fn_to_column
        process_apply_dfc_fn_to_column(self.dftitle,self.colname,self.dfc_fn,self.fn_parms,add_column_name=self.new_colnamee)

       
    def return_from_add_column_from_fns(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_fns_form_Widget][return_from_add_column_from_fns] "))

        self.parent.display_add_column()

    def help_for_add_column_from_fns(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_fns_form_Widget][help_for_add_column_from_fns] "))

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_COLS_ADD_FILE_ID
        display_url(TRANSFORM_COLS_ADD_FILE_ID)
  

# -----------------------------------------------------------------#
# -           Transform add Column Form User CodeWidget           -#
# -----------------------------------------------------------------#

class DataTransform_add_column_from_user_code_form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_user_code_form_Widget][init] "))

        self.init_form()

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_user_code_form_Widget] end"))

    def reload_data(self,parent,dftitle,new_colname) :
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_user_code_form_Widget][reload_data] "))

        self.parent         =   parent
        self.dftitle        =   dftitle
        self.new_colname    =   new_colname

        code_preamble   =   "from dfcleanser.common.cfg import get_dfc_dataframe_df\n"
        code_preamble   =   code_preamble + "df  =   get_dfc_dataframe_df('" + self.dftitle + "')\n"
        code_preamble   =   code_preamble + "colname  =  '" + self.colname + "'\n\n"
        code_preamble   =   code_preamble + "*           user defined function              *\n"
        code_preamble   =   code_preamble + "* USER DEFINED COLUMN VALUES = user_defined_column_values*\n\n\n\n\n"
        code_preamble   =   code_preamble + "from dfcleanser.common.cfg import set_columns\n"
        code_preamble   =   code_preamble + "set_columns(USER DEFINED COLUMN VALUES)\n"
       
        self.add_form.set_form_input_value_by_index(0,code_preamble)


    def init_form(self):  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_user_code_form_Widget][init_form]"))

        import dfcleanser.Qt.data_transform.DataTransformColumnsModel as DTCM

        form_parms      =   [DTCM.add_column_user_fn_input_id,DTCM.add_column_user_fn_input_idList,DTCM.add_column_user_fn_input_labelList,DTCM.add_column_user_fn_input_typeList,DTCM.add_column_user_fn_input_placeholderList,DTCM.add_column_user_fn_input_reqList]
        comboMethods    =   None
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.add_column_from_user_code, self.return_from_add_column_from_user_code, self.help_for_add_column_from_user_code]
        cfg_parms       =   None
        form_title      =   "\n\nAdd New Column from User Code\n"
        form_width      =   600


        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.add_form     =   dfcleanser_input_form_Widget(form_parms)

        code_preamble   =   "from dfcleanser.common.cfg import get_dfc_dataframe_df\n"
        code_preamble   =   code_preamble + "df  =   get_dfc_dataframe_df('" + self.dftitle + "')\n"
        code_preamble   =   code_preamble + "colname  =  '" + self.colname + "'\n\n"
        code_preamble   =   code_preamble + "*           user defined function              *\n"
        code_preamble   =   code_preamble + "* USER DEFINED COLUMN VALUES = user_defined_column_values*\n\n\n\n\n"
        code_preamble   =   code_preamble + "from dfcleanser.common.cfg import set_columns\n"
        code_preamble   =   code_preamble + "set_columns(USER DEFINED COLUMN VALUES)\n"
       
        self.add_form.set_form_input_value_by_index(0,self.new_colname)
        self.add_form.set_form_input_value_by_index(1,code_preamble)

        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.DataTransformAddFormLayout     =   QVBoxLayout()
        self.DataTransformAddFormLayout.addWidget(self.add_form)
        self.DataTransformAddFormLayout.addStretch()

        self.setLayout(self.DataTransformAddFormLayout)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_user_code_form_Widget][init_form] end"))

    def add_column_from_user_code(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_user_code_form_Widget][add_column_from_user_code] "))

        new_colname     =   self.add_form.get_form_input_value_by_index(0)      
        user_code       =   self.add_form.get_form_input_value_by_index(1)

        from dfcleanser.Qt.data_transform.DataTransformCoukmnsControl import process_apply_user_fn_to_column
        process_apply_user_fn_to_column(self.dftitle,self.colname,user_code,new_colname=new_colname)

    def return_from_add_column_from_user_code(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_user_code_form_Widget][return_from_add_column_from_user_code] "))

        self.parent.display_add_column()

    def help_for_add_column_from_user_code(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_user_code_fns_form_Widget][help_for_add_column_from_user_code] "))

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_COLS_ADD_USER_ID
        display_url(TRANSFORM_COLS_ADD_USER_ID)

# -----------------------------------------------------------------#
# -            Transform add Column Form Merge Widget             -#
# -----------------------------------------------------------------#

class DataTransform_add_column_from_merge_form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        #self.colname        =   dfparms[2]  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_merge_form_Widget][init] "))

        self.init_form()

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_merge_form_Widget] end"))

    def reload_data(self,parent,dftitle,colname) :
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_merge_form_Widget][reload_data] "))

        self.parent         =   parent
        self.dftitle        =   dftitle
        self.colname        =   colname

    def init_form(self):  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_merge_form_Widget][init_form]"))

        import dfcleanser.Qt.data_transform.DataTransformColumnsModel as DTCM

        form_parms      =   [DTCM.add_column_merge_input_id,DTCM.add_column_merge_input_idList,DTCM.add_column_merge_input_labelList,DTCM.add_column_merge_input_typeList,DTCM.add_column_merge_input_placeholderList,DTCM.add_column_merge_input_reqList]
        comboMethods    =   [self.add_col_merge_change_df, self.add_col_merge_change_col, None, None, None, None, None, self.add_col_merge_change_copy]
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.add_column_from_merge, self.clear_from_add_column_from_merge]
        cfg_parms       =   None
        form_title      =   "\n\nAdd New Column from df Merge\n"
        form_width      =   450

        selectDicts     =   []
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df     =   get_dfc_dataframe_df(self.dftitle)
            
        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        dfs         =   get_dfc_dataframes_titles_list()
        
        valid_dfs   =   []
        for i in range(len(dfs)) :
            if(not (dfs[i] == self.dftitle)) :
                valid_dfs.append(dfs[i])    
                
        if( (len(valid_dfs) < 1) ) :
            
            title       =   "dfcleanser exception : [DataTransform_add_column_from_merge_form_Widget]"        
            status_msg  =   "No df to merge with"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            self.parent.display_add_column()

            return(None)
        
        else :
    
            dfsdict     =   {"default":valid_dfs[0],"list":valid_dfs}
            selectDicts.append(dfsdict)
                
            merge_df        =   cfg.get_dfc_dataframe_df(valid_dfs[0])
            merge_cols      =   merge_df.columns.tolist()
            mergecolsdict   =   {"default":merge_cols[0],"list":merge_cols}   
            selectDicts.append(mergecolsdict)

            from dfcleanser.Qt.data_transform.DataTransformColumnsModel import how_select_default, how_select_default   
            howdict      =   {"default":how_select_default,"list":how_select_default}
            selectDicts.append(howdict)
                

            form_parms.append(selectDicts)
            form_parms.append(comboMethods)            
            form_parms.append(file_methods)
            form_parms.append(button_methods)            
            form_parms.append(cfg_parms)            
            form_parms.append(form_title)
            form_parms.append(form_width)        

            from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget, SMALL
            self.add_form     =   dfcleanser_input_form_Widget(form_parms)
        
            form_parmsA      =   [DTCM.add_column_mergeA_input_id,DTCM.add_column_mergeA_input_idList,DTCM.add_column_mergeA_input_labelList,DTCM.add_column_mergeA_input_typeList,DTCM.add_column_mergeA_input_placeholderList,DTCM.add_column_mergeA_input_reqList]
            comboMethodsA    =   [None, None, None, None, self.add_col_merge_change_copy]
            comboListA       =   None
            file_methodsA    =   None
            button_methodsA  =   [self.return_from_add_column_from_merge, self.help_for_add_column_from_merge]
            cfg_parmsA       =   None
            form_titleA      =   ""
            form_widthA      =   450

            selectDictsA     =   []

            leftdict     =   {"default":"False","list":["True","False"]}
            selectDictsA.append(leftdict)
                
            rightdict    =   {"default":"False","list":["True","False"]}
            selectDictsA.append(rightdict)
                
            sortdict     =   {"default":"False","list":["True","False"]}
            selectDictsA.append(sortdict)

            from dfcleanser.Qt.data_transform.DataTransformColumnsModel import validate_select_default, validate_select_list   
            validatedict =   {"default":validate_select_default,"list":validate_select_list}
            selectDictsA.append(validatedict)
                
            copydict     =   {"default":"False","list":["True","False"]}
            selectDictsA.append(copydict)

            form_parmsA.append(selectDictsA)
            form_parmsA.append(comboMethodsA)            
            form_parmsA.append(file_methodsA)
            form_parmsA.append(button_methodsA)            
            form_parmsA.append(cfg_parmsA)            
            form_parmsA.append(form_titleA)
            form_parmsA.append(form_widthA)        

            self.add_formA     =   dfcleanser_input_form_Widget(form_parmsA)


            from PyQt5.QtWidgets import QHBoxLayout, QWidget

            self.DataTransformAddFormsLayout     =   QHBoxLayout()
            self.DataTransformAddFormsLayout.addWidget(self.add_form)
            self.DataTransformAddFormsLayout.addWidget(self.add_formA)
            self.DataTransformAddFormsLayout.setAlignment(Qt.AlignHCenter)

            from PyQt5.QtWidgets import QVBoxLayout, QWidget

            self.DataTransformAddFormLayout     =   QVBoxLayout()
            self.DataTransformAddFormLayout.addLayout(self.DataTransformAddFormsLayout)
            self.DataTransformAddFormLayout.addStretch()

            self.setLayout(self.DataTransformAddFormLayout)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_merge_form_Widget][init_form] end"))

    def add_col_merge_change_df(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_merge_form_Widget][add_col_df_change_df] "))

    def add_col_merge_change_col(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_merge_form_Widget][add_col_df_change_col] "))

    def add_col_merge_change_copy(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_merge_form_Widget][add_col_change_copy] "))

    def add_column_from_merge(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_merge_form_Widget][add_column_from_merge] "))

    def clear_from_add_column_from_merge(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_merge_form_Widget][clear_from_add_column_from_merge] "))
       
    def return_from_add_column_from_merge(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_merge_form_Widget][return_from_add_column_from_merge] "))

        self.parent.display_add_column()

    def help_for_add_column_from_merge(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_merge_form_Widget][help_for_add_column_from_merge] "))

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_COLS_ADD_DF_ID
        display_url(TRANSFORM_COLS_ADD_DF_ID)

# -----------------------------------------------------------------#
# -            Transform add Column Form Join Widget             -#
# -----------------------------------------------------------------#

class DataTransform_add_column_from_join_form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        #self.colname        =   dfparms[2]  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_join_form_Widget][init] "))

        self.init_form()

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_join_form_Widget] end"))

    def reload_data(self,parent,dftitle,colname) :
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_join_form_Widget][reload_data] "))

        self.parent         =   parent
        self.dftitle        =   dftitle
        self.colname        =   colname

    def init_form(self):  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_join_form_Widget][init_form]"))

        import dfcleanser.Qt.data_transform.DataTransformColumnsModel as DTCM

        form_parms      =   [DTCM.add_column_join_input_id,DTCM.add_column_join_input_idList,DTCM.add_column_join_input_labelList,DTCM.add_column_join_input_typeList,DTCM.add_column_join_input_placeholderList,DTCM.add_column_join_input_reqList]
        comboMethods    =   [self.add_col_df_change_df, self.add_col_df_change_col,None,None,self.add_col_change_copy]
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.add_column_from_join, self.clear_from_add_column_from_join, self.return_from_add_column_from_join, self.help_for_add_column_from_join]
        cfg_parms       =   None
        form_title      =   "\n\nAdd New Column from df Join\n"
        form_width      =   600

        selectDicts     =   []
        
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df     =   get_dfc_dataframe_df(self.dftitle)
            
        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
        dfs         =   get_dfc_dataframes_titles_list()
        
        valid_dfs   =   []
        for i in range(len(dfs)) :
            if(not (dfs[i] == self.dftitle)) :
                valid_dfs.append(dfs[i])    
                
        if( (len(valid_dfs) < 1) ) :
            
            title       =   "dfcleanser exception : [DataTransform_add_column_from_merge_form_Widget]"        
            status_msg  =   "No df to join with"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            self.parent.display_add_column()

            return(None)
        
        else :
    
            dfsdict      =   {"default":valid_dfs[0],"list":valid_dfs}
            selectDicts.append(dfsdict)
                        
            merge_df        =   cfg.get_dfc_dataframe_df(valid_dfs[0])
            merge_cols      =   merge_df.columns.tolist()
            mergecolsdict   =   {"default":merge_cols[0],"list":merge_cols}   
            selectDicts.append(mergecolsdict)
            
            from dfcleanser.Qt.data_transform.DataTransformColumnsModel import join_how_select_default, join_how_select_list   
            howdict      =   {"default":join_how_select_default,"list":join_how_select_list}
            selectDicts.append(howdict)
                
            sortdict     =   {"default":"False","list":["True","False"]}
            selectDicts.append(sortdict)
                
            copydict     =   {"default":"False","list":["True","False"]}
            selectDicts.append(copydict)

            form_parms.append(selectDicts)
            form_parms.append(comboMethods)            
            form_parms.append(file_methods)
            form_parms.append(button_methods)            
            form_parms.append(cfg_parms)            
            form_parms.append(form_title)
            form_parms.append(form_width)        

            from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
            self.add_form     =   dfcleanser_input_form_Widget(form_parms)

            from PyQt5.QtWidgets import QVBoxLayout, QWidget

            self.DataTransformAddFormLayout     =   QVBoxLayout()
            self.DataTransformAddFormLayout.addWidget(self.add_form)
            self.DataTransformAddFormLayout.addStretch()

            self.setLayout(self.DataTransformAddFormLayout)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_join_form_Widget][init_form] end"))

    def add_col_df_change_df(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_join_form_Widget][add_col_df_change_df] "))

    def add_col_df_change_col(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_join_form_Widget][add_col_df_change_col] "))

    def add_col_change_copy(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_join_form_Widget][add_col_df_add_col_change_copy] "))

    def add_column_from_join(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_join_form_Widget][add_column_from_join] "))

    def clear_from_add_column_from_join(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_join_form_Widget][clear_from_add_column_from_join] ")
       
    def return_from_add_column_from_join(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_from_join_form_Widget][return_from_add_column_from_join] "))

        self.parent.display_add_column()

    def help_for_add_column_from_join(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_add_column_join_form_Widget][help_for_add_column_from_join] "))

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_COLS_ADD_DF_ID
        display_url(TRANSFORM_COLS_ADD_DF_ID)


# -----------------------------------------------------------------#
# -             Transform reorder Column Form Widget              -#
# -----------------------------------------------------------------#

class DataTransform_reorder_column_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_reorder_column_Widget][init] dftitle : ",self.dftitle))

        self.init_form()

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_reorder_column_Widget] end"))

    def reload_data(self,parent,dftitle) :
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_reorder_column_Widget][reload_data] "))
        
        self.parent         =   parent
        self.dftitle        =   dftitle

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_reorder_column_Widget][reload_data]",self.cols_to_reorder_List.count()))

    def init_form(self):  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_reorder_column_Widget][init_form]"))

        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.DataTransformReorderLayout     =   QVBoxLayout()

        from PyQt5.QtWidgets import QLabel
        reorder_column_title_label   =   QLabel()
        reorder_column_title_label.setText("\n\nReorder Columns\n")
        reorder_column_title_label.setAlignment(Qt.AlignCenter)
        reorder_column_title_label.resize(480,50)
        reorder_column_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.DataTransformReorderLayout.addWidget(reorder_column_title_label)

        from PyQt5.QtWidgets import  QListWidget, QListWidgetItem, QAbstractItemView
        self.cols_to_reorder_List     =   QListWidget()
        self.cols_to_reorder_List.setStyleSheet("font-size: 11px; font-weight: normal; font-family: Tahoma; ")
        self.cols_to_reorder_List.setDragDropMode(QAbstractItemView.InternalMove)

        self.load_columns_order()

        self.DataTransformReorderLayout.addWidget(self.cols_to_reorder_List)

        from PyQt5.QtWidgets import QLabel
        reorder_column_note_label   =   QLabel()
        reorder_column_note_label.setText("\nDrag and Drop Column Names to choose order.\n")
        reorder_column_note_label.setAlignment(Qt.AlignCenter)
        reorder_column_note_label.resize(480,50)
        reorder_column_note_label.setStyleSheet("font-size: 12px; font-weight: normal; font-family: Arial; ")
        self.DataTransformReorderLayout.addWidget(reorder_column_note_label)


        from PyQt5.QtWidgets import QHBoxLayout, QPushButton
        cmdbuttonsLayout  =   QHBoxLayout()
         
        reorder_button        =   QPushButton()     
        reorder_button.setText("Reorder\nColumns")
        reorder_button.setFixedSize(200,70)
        reorder_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        reorder_button.clicked.connect(self.reorder_columns) 

        return_button        =   QPushButton()     
        return_button.setText("Return")
        return_button.setFixedSize(200,70)
        return_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        return_button.clicked.connect(self.return_from_reorder_column) 
        
        help_button        =   QPushButton()     
        help_button.setText("Help")
        help_button.setFixedSize(200,70)
        help_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        help_button.clicked.connect(self.help_for_reorder_column) 

         
        cmdbuttonsLayout.addWidget(reorder_button)
        cmdbuttonsLayout.addWidget(return_button)
        cmdbuttonsLayout.addWidget(help_button)
        cmdbuttonsLayout.setAlignment(Qt.AlignHCenter)

        self.DataTransformReorderLayout.addLayout(cmdbuttonsLayout)
        self.DataTransformReorderLayout.addStretch()

        self.setLayout(self.DataTransformReorderLayout)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_reorder_column_Widget][init_form] end"))

    def load_columns_order(self) :

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        self.df     =   get_dfc_dataframe_df(self.dftitle)

        columns     =   self.df.columns.tolist()
        
        from PyQt5.QtWidgets import  QListWidgetItem
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_reorder_column_Widget][load_columns_order]",self.cols_to_reorder_List.count()))

        for i in range(len(columns)) :
            QListWidgetItem(columns[i],self.cols_to_reorder_List)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_reorder_column_Widget][load_columns_order]",self.cols_to_reorder_List.count()))
            
    def reorder_columns(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_reorder_column_Widget][reorder_columns]")

        total_cols  =   self.cols_to_reorder_List.count()

        new_cols    =   []
        for i in range(total_cols) :
            new_cols.append(self.cols_to_reorder_List.item(i).text())

        from dfcleanser.Qt.data_transform.DataTransformColumnsControl import process_reorder_columns
        process_reorder_columns(self.dftitle,new_cols)

        self.reload_data(self.parent,self.dftitle)

    def return_from_reorder_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_reorder_column_Widget][return_from_reorder_column]"))

        self.parent.display_transform_columns()

    def help_for_reorder_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_reorder_column_Widget][help_for_reorder_column]"))

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_COLS_REORDER_ID
        display_url(TRANSFORM_COLS_REORDER_ID)



# -----------------------------------------------------------------#
# -             Transform dummies Column Form Widget              -#
# -----------------------------------------------------------------#

class DataTransform_save_column_form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        #self.colname        =   dfparms[2]  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_save_column_form_Widget][init] "))

        self.init_form()

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_save_column_form_Widget] end"))

    def reload_data(self,parent,dftitle,colname) :
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_save_column_form_Widget][reload_data] "))

        self.parent         =   parent
        self.dftitle        =   dftitle
        self.colname        =   colname

    def init_form(self):  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_save_column_form_Widget][init_form]"))

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms              =    [self.dftitle,15,self.select_column_to_save]
        self.colsStats     =    DataInspectionColumnsStatsTable(parms)

        if(self.colsStats.num_rows < 10) :
            new_height  =   45 + (self.colsStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (10 * DEFAULT_ROW_HEIGHT)

        self.colsStats.setMinimumHeight(new_height)
        self.colsStats.setMaximumHeight(new_height)

        import dfcleanser.Qt.data_transform.DataTransformColumnsModel as DTCM

        form_parms      =   [DTCM.save_column_input_id,DTCM.save_column_input_idList,DTCM.save_column_input_labelList,DTCM.save_column_input_typeList,DTCM.save_column_input_placeholderList,DTCM.save_column_input_reqList]
        comboMethods    =   [None]
        comboList       =   None
        file_methods    =   [self.browse_to_fle_path]
        button_methods  =   [self.save_column, self.return_from_save_column, self.help_for_save_column]
        cfg_parms       =   None
        form_title      =   "\nSave Column\n"
        form_width      =   600

        selectDicts     =   []
        
        ftypes          =   {"default" : "json","list" : ["json","csv","excel"]}
        selectDicts.append(ftypes)
            
        form_parms.append(selectDicts)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.save_form     =   dfcleanser_input_form_Widget(form_parms)

        #self.save_form.set_form_input_value_by_index(1,DTCM.map_column_sample)

        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.DataTransformSaveFormLayout     =   QVBoxLayout()
        self.DataTransformSaveFormLayout.addWidget(self.colsStats)
        self.DataTransformSaveFormLayout.addWidget(self.save_form)
        self.DataTransformSaveFormLayout.addStretch()

        self.setLayout(self.DataTransformSaveFormLayout)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_save_column_form_Widget][init_form] end"))

    
    def browse_to_fle_path(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_save_column_form_Widget][browse_to_fle_path] "))


        from PyQt5.QtWidgets import QFileDialog
        fname = QFileDialog.getOpenFileName(self, 'Select file','c:\\',"csv files (*.csv)")
        self.save_form.set_form_input_value_by_index(2,fname[0])   

    def select_column_to_save(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_save_column_form_Widget][select_column_to_save]"))

        row_number      =   None
        column_number   =   None

        for idx in self.colsStats.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())

        model   =   self.colsStats.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :    
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_save_column_form_Widget][select_column_to_save] : colname [",cell,"]"))

        current_save_list   =   self.save_form.get_form_input_value_by_index(0)

        if(len(current_save_list) == 0) :

            new_save_list   =   "['" + cell + "']"
            self.save_form.set_form_input_value_by_index(0,new_save_list)

        else :

            end_bracket     =   current_save_list.find("]")

            if(end_bracket > -1):
                new_save_list   =   current_save_list[0:(end_bracket -1)]
                new_save_list   =   new_save_list + ", '" + cell + "']"
 
        self.save_form.set_form_input_value_by_index(0,new_save_list)

    def save_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_save_column_form_Widget][save_column] "))

        cols_to_save    =   self.save_form.get_form_input_value_by_index(0)
        file_name       =   self.save_form.get_form_input_value_by_index(1)
        file_type       =   self.save_form.get_form_input_value_by_index(2)

        from dfcleanser.Qt.data_transform.DataTransformColumnsControl import process_save_column
        process_save_column(self.dftitle,cols_to_save,file_name,file_type)        

    def return_from_save_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_save_column_form_Widget][return_from_save_column] "))

        self.parent.display_transform_columns()

    def help_for_save_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_save_column_form_Widget][help_for_save_column] "))

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_COLS_SAVE_ID
        display_url(TRANSFORM_COLS_SAVE_ID)


# -----------------------------------------------------------------#
# -               Transform copy Column Form Widget               -#
# -----------------------------------------------------------------#

class DataTransform_copy_column_form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        #self.colname        =   dfparms[2]  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_copy_column_form_Widget][init] "))

        self.init_form()

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_copy_column_form_Widget] end"))

    def reload_data(self,parent,dftitle,colname) :
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_copy_column_form_Widget][reload_data] "))

        self.parent         =   parent
        self.dftitle        =   dftitle
        self.colname        =   colname

    def init_form(self):  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_copy_column_form_Widget][init_form]"))

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms              =    [self.dftitle,15,self.select_column_to_copy]
        self.colsStats     =    DataInspectionColumnsStatsTable(parms)

        if(self.colsStats.num_rows < 10) :
            new_height  =   45 + (self.colsStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (10 * DEFAULT_ROW_HEIGHT)

        self.colsStats.setMinimumHeight(new_height)
        self.colsStats.setMaximumHeight(new_height)

        import dfcleanser.Qt.data_transform.DataTransformColumnsModel as DTCM

        form_parms      =   [DTCM.copy_column_input_id,DTCM.copy_column_input_idList,DTCM.copy_column_input_labelList,DTCM.copy_column_input_typeList,DTCM.copy_column_input_placeholderList,DTCM.copy_column_input_reqList]
        comboMethods    =   None
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.copy_column, self.return_from_copy_column, self.help_for_copy_column]
        cfg_parms       =   None
        form_title      =   "\nCopy Column\n"
        form_width      =   600

        selectDicts     =   []
        
        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.copy_form     =   dfcleanser_input_form_Widget(form_parms)

        #self.save_form.set_form_input_value_by_index(1,DTCM.map_column_sample)

        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.DataTransformCopyFormLayout     =   QVBoxLayout()
        self.DataTransformCopyFormLayout.addWidget(self.colsStats)
        self.DataTransformCopyFormLayout.addWidget(self.copy_form)
        self.DataTransformCopyFormLayout.addStretch()

        self.setLayout(self.DataTransformCopyFormLayout)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_copy_column_form_Widget][init_form] end"))

    def select_column_to_copy(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_copy_column_form_Widget][select_column_to_copy]"))

        row_number      =   None
        column_number   =   None

        for idx in self.colsStats.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_copy_column_form_Widget][select_column_to_copy] ",row_number,column_number))

        model   =   self.colsStats.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :    
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_copy_column_form_Widget][select_column_to_copy] : colname [",cell,"]"))

        self.copy_form.set_form_input_value_by_index(0,cell)
 
    def copy_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_copy_column_form_Widget][copy_column] "))

        existing_col    =   self.copy_form.get_form_input_value_by_index(0)
        new_col         =   self.copy_form.get_form_input_value_by_index(1)

        from dfcleanser.Qt.data_transform.DataTransformColumnsControl import process_copy_column        
        process_copy_column(self.dftitle,existing_col,new_col)


    def return_from_copy_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_copy_column_form_Widget][return_from_copy_column] "))

        self.parent.display_transform_columns()

    def help_for_copy_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_copy_column_form_Widget][help_for_copy_column] "))

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_COLS_COPY_ID
        display_url(TRANSFORM_COLS_COPY_ID)


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -        Transform apply fn Column Form Widget Variants         -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

# -----------------------------------------------------------------#
# -       Transform apply fn Column select fns Form Widget        -#
# -----------------------------------------------------------------#

class DataTransform_apply_fn_select_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   None 

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_fn_select_Widget][init] "))

        self.init_form()

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
           add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_fn_select_Widget] end"))

    def reload_data(self,parent,dftitle,colname) :
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_fn_select_Widget][reload_data] "))

        self.parent         =   parent
        self.dftitle        =   dftitle
        self.colname        =   colname

    def init_form(self):  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_fn_select_Widget][init_form]"))

        from PyQt5.QtWidgets import QVBoxLayout
        self.DataTrnasformapplyfnLayout     =   QVBoxLayout()

        from PyQt5.QtWidgets import QLabel
        applyfn_title_label   =   QLabel()
        applyfn_title_label.setText("\n\nSelect Column To Apply fn To\n")
        applyfn_title_label.setAlignment(Qt.AlignCenter)
        applyfn_title_label.resize(480,50)
        applyfn_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.DataTrnasformapplyfnLayout.addWidget(applyfn_title_label)


        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms              =    [self.dftitle,15,self.select_column_to_apply_fn_to]
        self.colsStats     =    DataInspectionColumnsStatsTable(parms)

        if(self.colsStats.num_rows < 10) :
            new_height  =   45 + (self.colsStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (10 * DEFAULT_ROW_HEIGHT)

        self.colsStats.setMinimumHeight(new_height)
        self.colsStats.setMaximumHeight(new_height)

        import dfcleanser.Qt.data_transform.DataTransformColumnsModel as DTCM

        form_parms      =   [DTCM.apply_column_fn_input_id,DTCM.apply_column_fn_input_idList,DTCM.apply_column_fn_input_labelList,
                            DTCM.apply_column_fn_input_typeList,DTCM.apply_column_fn_input_placeholderList,DTCM.apply_column_fn_input_reqList]
        comboMethods    =   None
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.display_dfc_fn_form, self.display_user_fn_form, self.return_from_apply_fn_column, self.help_for_apply_fn_column]
        cfg_parms       =   None
        form_title      =   "\nApply fn to Column\n"
        form_width      =   600

        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.apply_fn_form     =   dfcleanser_input_form_Widget(form_parms)
        
        self.DataTrnasformapplyfnLayout.addWidget(self.colsStats)
        self.DataTrnasformapplyfnLayout.addWidget(self.apply_fn_form)
        self.DataTrnasformapplyfnLayout.addStretch()

        self.setLayout(self.DataTrnasformapplyfnLayout)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_fn_select_Widget][init_form] end"))

    def select_column_to_apply_fn_to(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataCleansing_cleanse_columns_Widget][select_column_to_apply_fn_to"))

        row_number      =   None
        column_number   =   None

        for idx in self.colsStats.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_fn_select_Widget][select_column_to_cleanse] ",row_number,column_number))

        model   =   self.colsStats.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :    
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_fn_select_Widget][select_column_to_cleanse] : colname [",cell,"]"))

        self.colname    =   cell

        self.apply_fn_form.set_form_input_value_by_index(0,cell)

    def display_dfc_fn_form(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_fn_select_Widget][display_dfc_fn_form] "))

        if(not (self.colname is None)) :
        
            self.parent.display_apply_dfc_fn_column(self.colname)
        
        else :

            title       =   "dfcleanser error"       
            status_msg  =   "[display_dfc_fn_form] no column selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

    
    def display_user_fn_form(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_fn_select_Widget][display_user_fn_form] "))
        
        if(not (self.colname is None)) :
        
            self.parent.display_apply_user_fn_column(self.colname)
        
        else :

            title       =   "dfcleanser error"       
            status_msg  =   "[display_dfc_fn_form] no column selected "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

    def return_from_apply_fn_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_fn_select_Widget][return_from_apply_fn_column] "))

        self.parent.display_transform_columns()

    def help_for_apply_fn_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_fn_select_Widget][help_for_apply_fn_column] "))

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_COLS_APPLY_FN_ID
        display_url(TRANSFORM_COLS_APPLY_FN_ID)



# -----------------------------------------------------------------#
# -           Transform apply dfc fn Column Form Widget           -#
# -----------------------------------------------------------------#

class DataTransform_apply_dfc_fn_form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2] 

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_dfc_fn_form_Widget][init] : colname ",self.colname))

        self.init_form()

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_dfc_fn_form_Widget] end"))

    def reload_data(self,parent,dftitle,colname) :
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_dfc_fn_form_Widget][reload_data] "))

        self.parent         =   parent
        self.dftitle        =   dftitle
        self.colname        =   colname

    def init_form(self):  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_dfc_fn_form_Widget][init_form]"))

        import dfcleanser.Qt.data_transform.DataTransformColumnsModel as DTCM

        form_parms      =   [DTCM.apply_column_dfc_fn_input_id,DTCM.apply_column_dfc_fn_input_idList,DTCM.apply_column_dfc_fn_input_labelList,DTCM.apply_column_dfc_fn_input_typeList,DTCM.apply_column_dfc_fn_input_placeholderList,DTCM.apply_column_dfc_fn_input_reqList]
        comboMethods    =   [self.select_dfc_fn]
        comboList       =   [None]
        file_methods    =   None
        button_methods  =   [self.apply_fn_to_column, self.return_from_apply_dfc_fn_column, self.help_for_apply_dfc_fn_column]
        cfg_parms       =   None
        form_title      =   "\nApply dfc fn To Column '" + self.colname + "'\n"
        form_width      =   600

        selectDicts     =   []
        
        fns     =   []
        from dfcleanser.sw_utilities.GenericFunctionsModel import genfns, genfns_with_parms
        for i in range(len(genfns)) :
            fns.append(genfns[i])
        
        for i in range(len(genfns_with_parms)) :
            fns.append(genfns_with_parms[i])
            
        dfc_fn  =   fns[0]    
        
        lambdas         =   {"default":dfc_fn,"list":fns}
        selectDicts.append(lambdas)

        form_parms.append(selectDicts)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget , LARGE_TEXTEDIT
        self.apply_dfc_fn_form     =   dfcleanser_input_form_Widget(form_parms,size=LARGE_TEXTEDIT)

        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.DataTransformApplyFnFormLayout     =   QVBoxLayout()
        self.DataTransformApplyFnFormLayout.addWidget(self.apply_dfc_fn_form)
        self.DataTransformApplyFnFormLayout.addStretch()

        self.setLayout(self.DataTransformApplyFnFormLayout)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_dfc_fn_form_Widget][init_form] end"))


    def select_dfc_fn(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_dfc_fn_form_Widget][select_dfc_fn] "))

        self.dfc_fn     =   self.apply_dfc_fn_form.get_form_input_value_by_index(0) 
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_dfc_fn_form_Widget][select_dfc_fn] : self.dfc_fn ",self.dfc_fn))

        from dfcleanser.sw_utilities.GenericFunctionsModel import genfns, genfns_with_parms
        if(self.dfc_fn in genfns)   :
            parms_dict   =   "{}"   
        else :

            open_paren      =     self.dfc_fn.find("(") 
            close_paren     =     self.dfc_fn.find(")") 

            parms_list      =   self.dfc_fn[(open_paren+1):(close_paren)]

            parms           =   []

            if("," in parms_list) :
                parms   =   parms_list.split(",")
            else :
                parms.append(parms_list)

            parms_dict  =   "{ "
            for i in range(len(parms)) :
                parms_dict  =   parms_dict + "'" + parms[i] + "' : " + str(parms[i]) + "Value "
                if(len(parms) == 1) :
                   parms_dict  =   parms_dict + "}"  
                else :
                    if(i == (len(parms) -1)) :
                        parms_dict  =   parms_dict + "}"
                    else :
                        parms_dict  =   parms_dict + ", "       

        self.apply_dfc_fn_form.set_form_input_value_by_index(1,parms_dict)


    def apply_fn_to_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("DataTransform_apply_dfc_fn_form_Widget][apply_fn_to_column] "))

        self.dfc_fn     =   self.apply_dfc_fn_form.get_form_input_value_by_index(0)
        self.fn_parms   =   self.apply_dfc_fn_form.get_form_input_value_by_index(1)

        from dfcleanser.data_transform.DataTransformColumnsControl import process_apply_dfc_fn_to_column
        process_apply_dfc_fn_to_column(self.dftitle,self.colname,self.dfc_fn,self.fn_parms,add_column_name=None)
        

    def return_from_apply_dfc_fn_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_dfc_fn_form_Widget][return_from_apply_fn_column] "))

        self.parent.display_transform_columns()

    def help_for_apply_dfc_fn_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_dfc_fn_form_Widget][help_for_apply_fn_column] "))

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_COLS_APPLY_USER_FN_ID
        display_url(TRANSFORM_COLS_APPLY_USER_FN_ID)


# -----------------------------------------------------------------#
# -           Transform apply user fn Column Form Widget           -#
# -----------------------------------------------------------------#

class DataTransform_apply_user_fn_form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2] 

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_user_fn_form_Widget][init] : colname ",self.colname))

        self.init_form()

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_user_fn_form_Widget] end"))

    def reload_data(self,parent,dftitle,colname) :
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_user_fn_form_Widget][reload_data] "))

        self.parent         =   parent
        self.dftitle        =   dftitle
        self.colname        =   colname

    def get_code_text(self) :

        code_preamble   =   "from dfcleanser.common.cfg import get_dfc_dataframe_df\n"
        code_preamble   =   code_preamble + "df  =   get_dfc_dataframe_df('" + self.dftitle + "')\n"
        code_preamble   =   code_preamble + "colname  =  '" + self.colname + "'\n\n"
        code_preamble   =   code_preamble + "try : \n\n"
        code_preamble   =   code_preamble + "*           user defined mapping              *\n\n\n\n\n\n\n\n"
        code_preamble   =   code_preamble + "except Exception as e:\n"
        code_preamble   =   code_preamble + "   title       =   'dfcleanser exception'\n"
        code_preamble   =   code_preamble + "   status_msg  =   '[map_column_error] error'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       \n"
        code_preamble   =   code_preamble + "   from dfcleanser.sw_utilities.dfc_qt_model import display_exception\n"
        code_preamble   =   code_preamble + "   display_exception(title,status_msg,e)\n"

        return(code_preamble)

    def init_form(self):  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_user_fn_form_Widget][init_form]"))

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms              =    [self.dftitle,15,self.select_column_to_fn]
        self.colsStats     =    DataInspectionColumnsStatsTable(parms)

        if(self.colsStats.num_rows < 6) :                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            new_height  =   45 + (self.colsStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (6 * DEFAULT_ROW_HEIGHT)

        self.colsStats.setMinimumHeight(new_height)
        self.colsStats.setMaximumHeight(new_height)

        import dfcleanser.Qt.data_transform.DataTransformColumnsModel as DTCM

        form_parms      =   [DTCM.apply_user_fn_input_id,DTCM.apply_user_fn_input_idList,DTCM.apply_user_fn_input_labelList,DTCM.apply_user_fn_input_typeList,DTCM.apply_user_fn_input_placeholderList,DTCM.apply_user_fn_input_reqList]
        comboMethods    =   None
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.apply_user_fn_to_column, self.return_from_apply_user_fn_column, self.help_for_apply_user_fn_column]
        cfg_parms       =   None
        form_title      =   "Apply user fn To Column '" + self.colname + "'\n"
        form_width      =   600
 
        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.apply_user_fn_form     =   dfcleanser_input_form_Widget(form_parms)

        self.apply_user_fn_form.set_form_input_value_by_index(0,self.get_code_text())

        from PyQt5.QtWidgets import QVBoxLayout

        self.DataTransformApplyFnFormLayout     =   QVBoxLayout()
        self.DataTransformApplyFnFormLayout.addWidget(self.colsStats)        
        self.DataTransformApplyFnFormLayout.addWidget(self.apply_user_fn_form)
        self.DataTransformApplyFnFormLayout.addStretch()

        self.setLayout(self.DataTransformApplyFnFormLayout)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_user_fn_form_Widget][init_form] end"))
    
    def select_column_to_fn(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_map_column_form_Widget][select_column_to_map]"))

        row_number      =   None
        column_number   =   None

        for idx in self.colsStats.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_map_column_form_Widget][select_column_to_map] ",row_number,column_number))

        model   =   self.colsStats.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :    
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_map_column_form_Widget][select_column_to_map] : colname [",cell,"]"))

        self.map_form.set_form_input_value_by_index(0,cell)
        self.colname    =   cell

    def apply_user_fn_to_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("DataTransform_apply_user_fn_form_Widget][apply_user_fn_to_column] "))

        user_code   =   self.apply_user_fn_form.get_form_input_value_by_index(0)

        from dfcleanser.common.common_utils import opStatus
        opstat  =   opStatus()

        from dfcleanser.Qt.data_transform.DataTransformCoukmnsControl import process_apply_user_fn_to_column
        opstat  =   process_apply_user_fn_to_column(user_code)    
        
        if(opstat.get_status())  :
              
            title       =   "dfcleanser status : [apply_fn_column]"        
            status_msg  =   "column fn applied successfully"
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg)

            self.colsStats.reload_data()

    def return_from_apply_user_fn_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_user_fn_form_Widget][return_from_apply_user_fn_column] "))

        self.parent.display_transform_columns()

    def help_for_apply_user_fn_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_apply_user_fn_form_Widget][help_for_apply_user_fn_column] "))

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_COLS_APPLY_USER_FN_ID
        display_url(TRANSFORM_COLS_APPLY_USER_FN_ID)




# -----------------------------------------------------------------#
# -               Transform map Column Form Widget                -#
# -----------------------------------------------------------------#

class DataTransform_map_column_form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.column_to_map  =   "Undefined"
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_map_column_form_Widget][init] "))

        self.init_form()

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_map_column_form_Widget] end"))

    def reload_data(self,parent,dftitle) :
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_map_column_form_Widget][reload_data] "))

        self.parent             =   parent
        self.dftitle            =   dftitle

        self.map_form.set_form_input_value_by_index(1,self.get_code_text())
        self.colsStats.reload_data()

    def get_code_text(self) :

        code_preamble   =   "from dfcleanser.common.cfg import get_dfc_dataframe_df\n"
        code_preamble   =   code_preamble + "df  =   get_dfc_dataframe_df('" + self.dftitle + "')\n"
        code_preamble   =   code_preamble + "colname  =  '" + self.column_to_map + "'\n\n"
        code_preamble   =   code_preamble + "try : \n\n"
        code_preamble   =   code_preamble + "*           user defined mapping              *\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        code_preamble   =   code_preamble + "except Exception as e:\n"
        code_preamble   =   code_preamble + "   title       =   'dfcleanser exception'\n"
        code_preamble   =   code_preamble + "   status_msg  =   '[map_column_error] error'\n"
        code_preamble   =   code_preamble + "   from dfcleanser.sw_utilities.dfc_qt_model import display_exception\n"
        code_preamble   =   code_preamble + "   display_exception(title,status_msg,e)\n"

        return(code_preamble)

    def init_form(self):  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_map_column_form_Widget][init_form]"))

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms              =    [self.dftitle,15,self.select_column_to_map]
        self.colsStats     =    DataInspectionColumnsStatsTable(parms)

        if(self.colsStats.num_rows < 6) :
            new_height  =   45 + (self.colsStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (6 * DEFAULT_ROW_HEIGHT)

        self.colsStats.setMinimumHeight(new_height)
        self.colsStats.setMaximumHeight(new_height)

        import dfcleanser.Qt.data_transform.DataTransformColumnsModel as DTCM

        form_parms      =   [DTCM.transform_map_input_id,DTCM.transform_map_input_idList,DTCM.transform_map_input_labelList,DTCM.transform_map_input_typeList,DTCM.transform_map_input_placeholderList,DTCM.transform_map_input_reqList]
        comboMethods    =   [None]
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.map_column, self.return_from_map_column, self.help_for_map_column]
        cfg_parms       =   None
        form_title      =   "Map Column"
        form_width      =   600

        form_parms.append(comboList)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.map_form     =   dfcleanser_input_form_Widget(form_parms)
        
        self.map_form.set_form_input_value_by_index(1,self.get_code_text())


        # TBD add note for save as dict, list, function

        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.DataTransformMapFormLayout     =   QVBoxLayout()
        self.DataTransformMapFormLayout.addWidget(self.colsStats)
        self.DataTransformMapFormLayout.addWidget(self.map_form)
        self.DataTransformMapFormLayout.addStretch()

        self.setLayout(self.DataTransformMapFormLayout)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_map_column_form_Widget][init_form] end"))
    
    def select_column_to_map(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_map_column_form_Widget][select_column_to_map]"))

        row_number      =   None
        column_number   =   None

        for idx in self.colsStats.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_map_column_form_Widget][select_column_to_map] ",row_number,column_number))

        model   =   self.colsStats.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :    
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_map_column_form_Widget][select_column_to_map] : colname [",cell,"]"))

        self.map_form.set_form_input_value_by_index(0,cell)
        self.colname    =   cell



    def map_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_map_column_form_Widget][map_column] "))

        map_function    =  self.map_form.get_form_input_value_by_index(1) 

        from dfcleanser.common.common_utils import opStatus
        opstat = opStatus()

        from dfcleanser.Qt.data_transform.DataTransformColumnsControl import process_transform_column_map
        opstat  =    process_transform_column_map(map_function)   

        if(opstat.get_status()) :

            title       =   "dfcleanser status : [process_map_column]"        
            status_msg  =   "column mapped successfully"
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg)

            self.colsStats.reload_data()

    def return_from_map_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_map_column_form_Widget][return_from_map_column] "))

        self.parent.display_transform_columns()

    def help_for_map_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_map_column_form_Widget][help_for_map_column] "))

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_COLS_MAP_ID
        display_url(TRANSFORM_COLS_MAP_ID)



# -----------------------------------------------------------------#
# -             Transform dummies Column Form Widget              -#
# -----------------------------------------------------------------#

class DataTransform_dummies_column_form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        #self.colname        =   dfparms[2]  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_dummies_column_form_Widget][init] "))

        self.init_form()

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_dummies_column_form_Widget] end"))

    def reload_data(self,parent,dftitle,colname) :
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_dummies_column_form_Widget][reload_data] "))

        self.parent         =   parent
        self.dftitle        =   dftitle
        self.colname        =   colname

        self.colsStats.reload_data()

    def init_form(self):  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_dummies_column_form_Widget][init_form]"))

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms              =    [self.dftitle,15,self.select_column_to_dummy]
        self.colsStats     =    DataInspectionColumnsStatsTable(parms)

        if(self.colsStats.num_rows < 10) :
            new_height  =   45 + (self.colsStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (10 * DEFAULT_ROW_HEIGHT)

        self.colsStats.setMinimumHeight(new_height)
        self.colsStats.setMaximumHeight(new_height)
        

        import dfcleanser.Qt.data_transform.DataTransformColumnsModel as DTCM

        form_parms      =   [DTCM.transform_dummy_input_id,DTCM.transform_dummy_input_idList,DTCM.transform_dummy_input_labelList,DTCM.transform_dummy_input_typeList,DTCM.transform_dummy_input_placeholderList,DTCM.transform_dummy_input_reqList]
        comboMethods    =   [None]
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.make_dummies_for_column, self.return_from_dummies_column, self.help_for_dummies_column]
        cfg_parms       =   None
        form_title      =   "\nDummies For Column\n"
        form_width      =   600

        selectDicts     =   []
        
        remdict     =   {"default":"False","list":["True","False"]}
        selectDicts.append(remdict)
                
        form_parms.append(selectDicts)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.dummies_form     =   dfcleanser_input_form_Widget(form_parms)

        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.DataTransformDummiesFormLayout     =   QVBoxLayout()
        self.DataTransformDummiesFormLayout.addWidget(self.colsStats)
        self.DataTransformDummiesFormLayout.addWidget(self.dummies_form)
        self.DataTransformDummiesFormLayout.addStretch()

        self.setLayout(self.DataTransformDummiesFormLayout)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_dummies_column_form_Widget][init_form] end"))

    def select_column_to_dummy(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_dummies_column_form_Widget][select_column_to_dummy]"))

        row_number      =   None
        column_number   =   None

        for idx in self.colsStats.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_dummies_column_form_Widget][select_column_to_dummy] ",row_number,column_number))

        model   =   self.colsStats.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :    
            padd_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_dummies_column_form_Widget][select_column_to_dummy] : colname [",cell,"]"))

        self.dummies_form.set_form_input_value_by_index(0,cell)

    def make_dummies_for_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_dummies_column_form_Widget][make_dummies_for_column] "))

        dummy_col   =   self.dummies_form.get_form_input_value_by_index(0)
        remove_col  =   self.dummies_form.get_form_input_value_by_index(1)
        if(remove_col == "False") :
            remove_col  = False
        else :
            remove_col  =   True

        from dfcleanser.Qt.data_transform.DataTransformColumnsControl import make_col_categorical_from_dummies
        make_col_categorical_from_dummies(self.dftitle,dummy_col,remove_col)

        self.colsStats.reload_data()

    def return_from_dummies_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_dummies_column_form_Widget][return_from_dummies_column] "))

        self.parent.display_transform_columns()

    def help_for_dummies_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_dummies_column_form_Widget][help_for_dummies_column] "))

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_COLS_DUMMY_ID
        display_url(TRANSFORM_COLS_DUMMY_ID)

# -----------------------------------------------------------------#
# -               Transform Category Column Form Widget           -#
# -----------------------------------------------------------------#

# -----------------------------------------------------------------#
# -             Table view and Model for column uniques           -#
# -----------------------------------------------------------------#
class ColumnUniquesModel(QtCore.QAbstractTableModel):
    def __init__(self, coldata, colheaders):

        super(ColumnUniquesModel,self).__init__()
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

class ColumnUniquesTable(QtWidgets.QTableView):

    def __init__(self,  colparms, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.dftitle            =   colparms[0]
        self.colname            =   colparms[1]
        self.callback           =   colparms[2]

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[ColumnUniquesTable] : init"))

        self.init_tableview()

        self.doubleClicked.connect(self.callback) 

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[ColumnUniquesTable] : end"))

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self,dftitle,colname):
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[ColumnUniquesTable][reload_data] : dftile : colname : ",dftitle,colname))

        self.dftitle    =   dftitle
        self.colname    =   colname

        statsdata       =   self.load_columns_info_data()
        self.model.reload_data(statsdata)

        self.num_rows   =   len(statsdata)
        
        if(self.num_rows < 30) :
            new_height  =   (35 + (self.num_rows * DEFAULT_ROW_HEIGHT))
        else :
            new_height  =   (35 + (30 * DEFAULT_ROW_HEIGHT))

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)
    
    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[ColumnUniquesTable][init_tableview]"))

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        statsdata     =   self.load_columns_info_data()
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN_DETAILS")) :
           add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[ColumnUniquesTable][init_tableview] :headers",self.column_headers))

        if(self.model is None) :
            self.model = ColumnUniquesModel(statsdata,self.column_headers)
            self.setModel(self.model)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
           add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[ColumnUniquesTable][init_tableview] : model loaded"))

        self.num_rows   =   len(statsdata)
        
        if(self.num_rows < 25) :
            new_height  =   (35 + (self.num_rows * DEFAULT_ROW_HEIGHT))
        else :
            new_height  =   (35 + (25 * DEFAULT_ROW_HEIGHT))

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

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[ColumnUniquesTable][load_columns_info_data]"))

        data    =   []

        if(not (self.colname is None) ) :

            from dfcleanser.common.cfg import get_dfc_dataframe_df 
            df          =   get_dfc_dataframe_df(self.dftitle)
            uniques     =   df[self.colname].unique().tolist()
            
            from dfcleanser.common.common_utils import is_numeric_col
            if(is_numeric_col(df,self.colname)) :
                uniques.sort()

            for i in range(len(uniques)) :
                
                data_row    =   []
                data_row.append(str(uniques[i]))
                data.append(data_row)

            if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN_DETAILS")) :
                add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[ColumnUniquesTable] : data"))
                for j in range(len(data)) :
                    add_debug_to_log("DataTransformColumnsWidgets",print_to_string("  [",j,"] : ",data[j]))

        else :

            data_row    =   [""]
            data.append(data_row)

        self.column_headers     =   ["Unique Value"]
        self.column_widths      =   [330]

        return(data)

# -----------------------------------------------------------------#
# -             Table view and Model for column uniques           -#
# -----------------------------------------------------------------#

class DataTransform_category_column_form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   None 

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_category_column_form_Widget][init] "))

        self.init_form()

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_category_column_form_Widget] end"))

    def reload_data(self,parent,dftitle) :
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_category_column_form_Widget][reload_data] "))

        self.parent         =   parent
        self.dftitle        =   dftitle
        
        parms               =    [self.dftitle,self.colname,self.select_unique_value]
        self.uniques.reload_data(self.dftitle,self.colname)


    def init_form(self):  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_category_column_form_Widget][init_form]"))

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms              =    [self.dftitle,15,self.select_category_column]
        self.colsStats     =    DataInspectionColumnsStatsTable(parms)

        if(self.colsStats.num_rows < 10) :
            new_height  =   45 + (self.colsStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (10 * DEFAULT_ROW_HEIGHT)

        self.colsStats.setMinimumHeight(new_height)
        self.colsStats.setMaximumHeight(new_height)

        parms               =    [self.dftitle,self.colname,self.select_unique_value]
        self.uniques        =    ColumnUniquesTable(parms)

        if(self.uniques.num_rows < 30) :
            new_height  =   45 + (self.uniques.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (30 * DEFAULT_ROW_HEIGHT)

        self.uniques.setMinimumHeight(new_height)
        self.uniques.setMaximumHeight(new_height)

        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

        self.uniquesLayout     =   QVBoxLayout()
        self.uniquesLayout.addWidget(self.uniques)
        self.uniquesLayout.addStretch()

        import dfcleanser.Qt.data_transform.DataTransformColumnsModel as DTCM

        form_parms      =   [DTCM.transform_category_input_id,DTCM.transform_category_input_idList,DTCM.transform_category_input_labelList,DTCM.transform_category_input_typeList,DTCM.transform_category_input_placeholderList,DTCM.transform_category_input_reqList]
        comboMethods    =   [None,self.select_unique_value]
        comboList       =   None
        file_methods    =   None
        button_methods  =   [self.make_category_column, self.return_from_category_column, self.help_for_category_column]
        cfg_parms       =   None
        form_title      =   "\nMake Column Categorical\n"
        form_width      =   600

        selectDicts     =   []
        
        orderflag   =   {"default":"False","list":["True","False"]}
        selectDicts.append(orderflag)        
        
        useallflag  =   {"default":"use all uniques","list":["use all uniques","define include list from 'uniques_values'","define exclude list from 'uniques_values' to subtract from all"]}
        selectDicts.append(useallflag)  

        form_parms.append(selectDicts)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.category_form     =   dfcleanser_input_form_Widget(form_parms)

        self.category_form.set_form_input_value_by_index(0,self.colname)

        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

        self.DataTransformCategoryFormLayout     =   QHBoxLayout()
        self.DataTransformCategoryFormLayout.addWidget(self.uniques)
        self.DataTransformCategoryFormLayout.addWidget(self.category_form)
        #self.DataTransformCategoryFormLayout.addStretch()

        self.DataTransformCategoryLayout     =   QVBoxLayout()
        self.DataTransformCategoryLayout.addWidget(self.colsStats)
        self.DataTransformCategoryLayout.addLayout(self.DataTransformCategoryFormLayout)

        self.setLayout(self.DataTransformCategoryLayout)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_category_column_form_Widget][init_form] end"))

    def select_unique_value(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_category_column_form_Widget][select_unique_value] "))

        unique_option   =   self.category_form.get_form_input_value_by_index(2)

        if(not (unique_option == "use all uniques")) :

            row_number      =   None
            column_number   =   None

            for idx in self.uniques.selectionModel().selectedIndexes():
                row_number = int(idx.row())
                column_number = int(idx.column())

            if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
                add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_category_column_form_Widget][select_unique_value] ",row_number,column_number))

            model   =   self.uniques.model
            tdata   =   model.get_data()
            cell    =   tdata[row_number][0]

            if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :    
                add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_category_column_form_Widget][select_unique_value] : colname [",cell,"]"))

            uniques_list   =   self.category_form.get_form_input_value_by_index(3)
            
            if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :    
                add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_category_column_form_Widget][uniques_list] ",uniques_list))

            if( (uniques_list is None) or (len(uniques_list) == 0) ) :
                new_uniques_list    =   "[" + str(cell) + "]"
            else :
                new_uniques_list    =   uniques_list[:len(uniques_list)-1] + "," + str(cell) + "]"

            self.category_form.set_form_input_value_by_index(3,new_uniques_list)    


    def select_category_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_category_column_form_Widget][select_category_column] "))
        
        row_number      =   None
        column_number   =   None

        for idx in self.colsStats.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_change_datatype_form_Widget][select_category_column] ",row_number,column_number))

        model   =   self.colsStats.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        self.colname    =   cell
        self.category_form.set_form_input_value_by_index(0,self.colname)

        self.reload_data(self.parent,self.dftitle,self.colname)

    def make_category_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_category_column_form_Widget][make_category_column] "))

        colname         =   self.category_form.get_form_input_value_by_index(0) 
        order_flag      =   self.category_form.get_form_input_value_by_index(1) 
        uniques_option  =   self.category_form.get_form_input_value_by_index(2)
        uniques_list    =   self.category_form.get_form_input_value_by_index(3)

        from dfcleanser.Qt.data_transform.DataTransformColumnsControl import process_category_convert_transform
        process_category_convert_transform(self.dftitle,colname,order_flag,uniques_option,uniques_list) 

        self.parent.display_transform_columns()

    def return_from_category_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_category_column_form_Widget][return_from_copy_column] "))

        self.parent.display_transform_columns()

    def help_for_category_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_category_column_form_Widget][help_for_copy_column] "))

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_COLS_CAT_ID
        display_url(TRANSFORM_COLS_CAT_ID)




# -----------------------------------------------------------------#
# -           Transform change column datatype Form Widget        -#
# -----------------------------------------------------------------#

class DataTransform_change_datatype_form_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        super().__init__()

        self.parent         =   dfparms[0]
        self.dftitle        =   dfparms[1]
        self.colname        =   dfparms[2]

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_change_datatype_form_Widget][init] : colname ",self.colname))

        self.init_form()

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_change_datatype_form_Widget] end"))

    def reload_data(self,parent,dftitle,colname) :
        
        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_change_datatype_form_Widget][reload_data] ",dftitle,colname))

        self.parent         =   parent
        self.dftitle        =   dftitle
        self.colname        =   colname

        self.colsStats.reload_data()
        self.change_datatype_form.set_form_input_value_by_index(0,self.colname)

        if(self.colname is None) :
            self.form_title      =   "\n\nChange Column Datatype\n"
        else :
            self.form_title      =   "\n\nChange Column '" + self.colname + "' Datatype\n"

    def init_form(self):  

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_change_datatype_form_Widget][init_form]"))

        from dfcleanser.Qt.data_inspection.DataInspectionColumnsWidgets import DataInspectionColumnsStatsTable
        parms              =    [self.dftitle,15,self.select_column_to_change_datatype]
        self.colsStats     =    DataInspectionColumnsStatsTable(parms)

        if(self.colsStats.num_rows < 10) :
            new_height  =   45 + (self.colsStats.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   45 + (10 * DEFAULT_ROW_HEIGHT)

        self.colsStats.setMinimumHeight(new_height)
        self.colsStats.setMaximumHeight(new_height)

        from dfcleanser.common.cfg import get_dfc_dataframe_df 
        df                  =   get_dfc_dataframe_df(self.dftitle)
        if(self.colname is None) :
            self.total_nans     =   0
        else :    
            self.total_nans     =   df[self.colname].isnull().sum()

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_change_datatype_form_Widget][after colstats]"))

        import dfcleanser.Qt.data_transform.DataTransformColumnsModel as DTCM

        if(self.total_nans == 0) :

            form_parms      =   [DTCM.dt_data_type_input_id,DTCM.dt_data_type_input_idList,DTCM.dt_data_type_input_labelList,DTCM.dt_data_type_input_typeList,
                                 DTCM.dt_data_type_input_placeholderList,DTCM.dt_data_type_input_reqList]
            comboMethods    =   [None]
            comboList       =   None
            file_methods    =   None
            button_methods  =   [self.change_datatype_column, self.return_from_change_datatype_column, self.help_for_change_datatype_column]
            cfg_parms       =   None
            if(self.colname is None) :
                self.form_title      =   "\n\nChange Column Datatype\n"
            else :
                self.form_title      =   "\n\nChange Column '" + self.colname + "' Datatype\n"
            form_width      =   600

            selectDicts     =   []

            from dfcleanser.common.common_utils import get_datatypes_list, get_dtype_str_for_datatype 
            datatypes_list  =   get_datatypes_list()
            if(self.colname is None) :
                dtypes          =   {"default":datatypes_list[0],"list":get_datatypes_list(False)}
            else :
                dtypes          =   {"default":datatypes_list[0],"list":get_datatypes_list(False)}
            selectDicts.append(dtypes)
        
            if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
                add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_change_datatype_form_Widget][after selectDicts]"))

        else :

            form_parms      =   [DTCM.dt_nans_data_type_input_id,DTCM.dt_nans_data_type_input_idList,DTCM.dt_nans_data_type_input_labelList,DTCM.dt_nans_data_type_input_typeList,
                                 DTCM.dt_nans_data_type_input_placeholderList,DTCM.dt_nans_data_type_input_reqList]
            comboMethods    =   [None,None]
            comboList       =   None
            file_methods    =   None
            button_methods  =   [self.change_datatype_column, self.return_from_change_datatype_column, self.help_for_change_datatype_column]
            cfg_parms       =   None
            if(self.colname is None) :
                self.form_title      =   "\n\nChange Column Datatype\n"
            else :
                self.form_title      =   "\n\nChange Column '" + self.colname + "' Datatype\n"
            form_width      =   600

            selectDicts     =   []
            
            from dfcleanser.common.common_utils import get_datatypes_list, get_dtype_str_for_datatype 
            datatypes_list  =   get_datatypes_list()
            if(self.colname is None) :
                dtypes          =   {"default":datatypes_list[0],"list":get_datatypes_list(False)}
            else :
                dtypes          =   {"default":datatypes_list[0],"list":get_datatypes_list(False)}
            selectDicts.append(dtypes)
        
            if(self.colname is None) :
                methodopts     =   {"default":"None","list": ["None","backfill","bfill","pad","ffill","mean"]}
            else :

                from dfcleanser.common.common_utils import is_numeric_col
                if(is_numeric_col(df,self.colname)) :
                    methodopts     =   {"default":"None","list": ["None","backfill","bfill","pad","ffill","mean"]}
                else :
                    methodopts     =   {"default":"None","list": ["None","backfill","bfill","pad","ffill"]}
            
            selectDicts.append(methodopts)
 
        form_parms.append(selectDicts)
        form_parms.append(comboMethods)            
        form_parms.append(file_methods)
        form_parms.append(button_methods)            
        form_parms.append(cfg_parms)            
        form_parms.append(self.form_title)
        form_parms.append(form_width)        

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.change_datatype_form     =   dfcleanser_input_form_Widget(form_parms)

        self.change_datatype_form.set_form_input_value_by_index(0,self.colname)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            padd_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_change_datatype_form_Widget][after colstats]"))

        from PyQt5.QtWidgets import QVBoxLayout

        self.DataTransformchange_datatypeLayout     =   QVBoxLayout()
        self.DataTransformchange_datatypeLayout.addWidget(self.colsStats)
        self.DataTransformchange_datatypeLayout.addWidget(self.change_datatype_form)
        self.DataTransformchange_datatypeLayout.addStretch()

        self.setLayout(self.DataTransformchange_datatypeLayout)

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_change_datatype_form_Widget][init_form] end"))


    def select_column_to_change_datatype(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_change_datatype_form_Widget][select_column_to_change_datatype]"))

        row_number      =   None
        column_number   =   None

        for idx in self.colsStats.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_change_datatype_form_Widget][select_column_to_change_datatype] ",row_number,column_number))

        model   =   self.colsStats.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :    
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_change_datatype_form_Widget][select_column_to_change_datatype] : colname [",cell,"]"))

        self.parent.display_change_column_datatype(cell)


    def change_datatype_column(self) :

        from dfcleanser.common.common_utils import opStatus
        opstat  =   opStatus()


        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_change_datatype_form_Widget][change_datatype_column] "))

        if(self.total_nans > 0) :

            column_to_change    =   self.change_datatype_form.get_form_input_value_by_index(0)
            datatype_to_change  =   self.change_datatype_form.get_form_input_value_by_index(1)
            fillna_value        =   self.change_datatype_form.get_form_input_value_by_index(2)
            fillna_method       =   self.change_datatype_form.get_form_input_value_by_index(3)
            fillna_thresholld   =   self.change_datatype_form.get_form_input_value_by_index(4)

            from dfcleanser.Qt.data_transform.DataTransformColumnsControl import process_change_column_datatype
            opstat  =   process_change_column_datatype(self.dftitle,column_to_change,datatype_to_change,fillna_value,fillna_method,fillna_thresholld)

        else :

            column_to_change    =   self.change_datatype_form.get_form_input_value_by_index(0)
            datatype_to_change  =   self.change_datatype_form.get_form_input_value_by_index(1)
            fillna_value        =   None
            fillna_method       =   None
            fillna_thresholld   =   None

            from dfcleanser.Qt.data_transform.DataTransformColumnsControl import process_change_column_datatype
            opstat  =   process_change_column_datatype(self.dftitle,column_to_change,datatype_to_change,fillna_value,fillna_method,fillna_thresholld)

        if(opstat.get_status()) :

            title       =   "dfcleanser status : [change_datatype]"        
            status_msg  =   "column datatype changed successfully"
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg)

            from dfcleanser.common.cfg import df_Column_Changed_signal
            df_Column_Changed_signal.issue_notice(self.dftitle)

        #self.parent.display_transform_columns()


    def return_from_change_datatype_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_change_datatype_form_Widget][return_from_change_datatype_column] "))

        self.parent.display_transform_columns()

    def help_for_change_datatype_column(self) :

        if(is_debug_on(DataTransform_ID,"DEBUG_TRANSFORM_COLUMN")) :
            add_debug_to_log("DataTransformColumnsWidgets",print_to_string("[DataTransform_change_datatype_form_Widget][help_for_change_datatype_column] "))

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import TRANSFORM_COLS_DTYPE_ID
        display_url(TRANSFORM_COLS_DTYPE_ID)



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                 Transfoprm Columns Widget end                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#




























