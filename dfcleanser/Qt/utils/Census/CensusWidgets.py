"""
# CensusWidgets
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
from dfcleanser.common.cfg import SWCensusUtility_ID


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
# -                    Census Datasets Objects                    -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class Census_datasetsModel(QtCore.QAbstractTableModel):
    def __init__(self, censusdata, colheaders):

        super(Census_datasetsModel, self).__init__()
        self._data          =   censusdata
        self.column_names   =   colheaders

    def reload_data(self,censusdata) :
        self._data = censusdata

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
            else :
                return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:
            if(column == 0):
                bgcolor = QtGui.QBrush(QColor(240, 234, 193))
            else:
                bgcolor = QtGui.QBrush(QtCore.Qt.white)
            return (bgcolor)  

        #if role == Qt.SizeHintRole:
        #    return QSize(0, 60)                     
                
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


class Census_datasets_Table(QtWidgets.QTableView):

    def __init__(self, parent, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.parent             =   parent

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[Census_datasets_Table] : init"))

        self.doubleClicked.connect(self.select_census_dataset) 

        self.init_tableview()

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[Census_datasets_Table] : end"))

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self):
        
        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[Census_datasets_Table][reload_data] "))

        tbldata    =   self.load_census_datasets_data()
        self.model.reload_data(tbldata)


    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[Census_datasets_Table][init_tableview]"))

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        census_data     =   self.load_census_datasets_data()

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
           add_debug_to_log("Census",print_to_string("[Census_datasets_Table][init_tableview] :headers",self.column_headers))

        if(self.model is None) :
            self.model = Census_datasetsModel(census_data,self.column_headers)
            self.setModel(self.model)

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
           add_debug_to_log("Census",print_to_string("[Census_datasets_Table][init_tableview] : model loaded"))

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
        nrows           =   len(census_data)
        total_height    =   0

        for row in range(nrows):
            if(row==0):
                self.setRowHeight(row, 40) 
                total_height    =   total_height + 40
            elif(row==1):
                self.setRowHeight(row, 70)
                total_height    =   total_height + 70
            elif(row==2):
                self.setRowHeight(row, 110)
                total_height    =   total_height + 110
            elif(row==3):
                self.setRowHeight(row, 40)
                total_height    =   total_height + 40

            elif(row==5):
                self.setRowHeight(row, 100)
                total_height    =   total_height + 100
            
            elif(row==6):
                self.setRowHeight(row, 40)
                total_height    =   total_height + 40
            
            elif(row==7):
                self.setRowHeight(row, 20)
                total_height    =   total_height + 20
            
            elif(row==8):
                self.setRowHeight(row, 100)
                total_height    =   total_height + 100

            else:   
                self.setRowHeight(row, 60) 
                total_height    =   total_height + 60

        if(total_height > 600) :
            total_height    =   600

        self.setMinimumHeight(total_height)
        self.setMaximumHeight(total_height)
        
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(self.column_widths)) :
           self.setColumnWidth(i, self.column_widths[i])     
        
        self.setWordWrap(True)


    # -----------------------------------------------------------------#
    # -                     load the table data                       -#
    # -----------------------------------------------------------------#
    def load_census_datasets_data(self):

        datasetTitles       =   ["Economic","Education","Employment","Health Insurance","Housing",
                                 "Immigration","Internet","Population","Social","Transportation"]
        
        datasetNotes        =   ["Income[race, children, family type]\nEarnings[work type, source, family type, race, sex, worker, education, industry, occupation, employment status]",
                                "Level[age, sex, race, poverty level, earnings]\nEnrollment[school, age, race]\nCollege Major[age, sex]\nGraduate Enrollment[sex, age, school type]",
                                "Employment Status[age, race, poverty level, disability, education]\nFamily Type[children, marital status, work status]\nOccupation[sex, work status]\nIndustry[sex, work status]\nWeeks Worked[sex]\nHours Worked[sex]\nEmployer Type[sex]",
                                "Insurance Coverage[age, sex, race, family type, citizenship, disability, education, employment, income, poverty]\nInsurance Type[age, poverty level, sex]",
                                "Housing Units[race, occupant, age, education, occupancy duration, income, monthly costs, number of occupants, family type, children, number of units, year built, number of rooms, number of bedrooms, with plumbing, with kitchen, vehicles,with telephone, heating type]",
                                "Place Of Birth[native, foreign, region, country, citizenship]\nMarital Status[residency]\nIncome[residency, foreign]\nEducation[residency, nativity ]\nPoverty Level[nativity]\nRace[residency]\nNativity[race, age, sex]",
                                "Devices[]\nInternet Connection Type[income, age, race, education, labor force]",
                                "Population[sex, age, race, citizenship, households]",
                                "Marital Status[sex, age, race, employment]\nLanguage[age, citizenship]\nPoverty Level[sex, age, race, education, employment, family type]\nFood Stamps[family type, marital status, children, poverty level]\nFertility[age, marital status, race, education, poverty level]\nVeterans[sex, era, age, race, income, education, employment, poverty level]\nDisability[sex, race, age]",
                                "Transport Type[age, sex, race, nativity, earnings, poverty level, industry, work type]\nCommute Time[]\nVehicles[]"]
    
        data    =   []


        for i in range(len(datasetTitles)) :
                
            data_row    =   []

            data_row.append(datasetTitles[i])
            data_row.append(datasetNotes[i])

            data.append(data_row)

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[Census_datasets_Table] : data"))
            for j in range(len(data)) :
                add_debug_to_log("Census",print_to_string("  [",j,"] : ",data[j]))

        self.column_headers     =   ["Dataset Name","Dataset Description"]
        self.column_widths      =   [150,750]

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[Census_datasets_Table] end"))

        return(data)
    
    
    def select_census_dataset(self) :

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[Census_datasets_Table][select_census_dataset]"))
   
        row_number      =   None
        column_number   =   None

        for idx in self.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[Census_datasets_Table][select_census_dataset] ",row_number,column_number))

        model   =   self.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][0]

        self.dataset =  cell
            
        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :    
            add_debug_to_log("Census",print_to_string("[Census_datasets_Table][select_census_dataset] : self.dataset [",self.dataset,"]"))

        self.parent.display_census_dataset_columns(self.dataset)

class Census_datasets_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[Census_datasets_Widget]"))

        super().__init__()

        self.parent     =   dfparms[0]

        self.init_form()

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[Census_datasets_Widget] end"))

    def reload_data(self,parent) :

        self.parent     =   parent

    def init_form(self):  

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[Census_datasets_Widget][init_form]"))

        from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QTableWidget

        self.title_label    =   QLabel()
        self.title_label.setText("Census Datasets")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.resize(600,50)
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold; font-family: Arial; ")

        self.dataset_table   =   QWidget()
        self.dataset_table   =   Census_datasets_Table(self.parent)

        self.final_layout   =   QVBoxLayout()
        self.final_layout.addWidget(self.title_label)
        self.final_layout.addWidget(self.dataset_table)
        self.final_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.final_layout)

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[Census_datasets_Widget][init_form] end"))


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                Census Dataset Columns Objects                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class Census_dataset_columnsModel(QtCore.QAbstractTableModel):
    def __init__(self, censusdata, colheaders):

        super(Census_dataset_columnsModel, self).__init__()
        self._data          =   censusdata
        self.column_names   =   colheaders

    def reload_data(self,censusdata) :
        self._data = censusdata

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
            else :
                return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:
            if(column == 0):
                bgcolor = QtGui.QBrush(QColor(240, 234, 193))
            else:
                bgcolor = QtGui.QBrush(QtCore.Qt.white)
            return (bgcolor)  

        #if role == Qt.SizeHintRole:
        #    return QSize(0, 60)                     
                
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


class Census_dataset_columns_Table(QtWidgets.QTableView):

    def __init__(self, parent, dataset, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.parent             =   parent
        self.dataset            =   dataset

        self.num_columns        =   0

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[Census_dataset_columns_Table] : init"))

        self.init_tableview()

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[Census_dataset_columns_Table] : end"))

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self):
        
        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[Census_dataset_columns_Table][reload_data] "))

        tbldata    =   self.load_census_dataset_columns_data(self.dataset)
        self.model.reload_data(tbldata)


    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[Census_dataset_columns_Table][init_tableview]"))

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        census_data     =   self.load_census_dataset_columns_data(self.dataset)

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
           add_debug_to_log("Census",print_to_string("[Census_dataset_columns_Table][init_tableview] :headers",self.column_headers))

        if(self.model is None) :
            self.model = Census_dataset_columnsModel(census_data,self.column_headers)
            self.setModel(self.model)

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
           add_debug_to_log("Census",print_to_string("[Census_dataset_columns_Table][init_tableview] : model loaded"))

        #----------------------------------------------#
        # init the table view header and cell sizes    #
        #----------------------------------------------#
        
        # set default tableview font
        tablefont   =  QFont("Times",9) 
        tablefont.setBold(False)
        self.setFont(tablefont)

        # set table view header
        header = self.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignHCenter)
        header.setFixedHeight(26)

        # set the row heights
        nrows           =   len(census_data)
        total_height    =   0

        for row in range(nrows):
            self.setRowHeight(row, 20) 

        total_height    =   550

        self.setMinimumHeight(total_height)
        self.setMaximumHeight(total_height)
        
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(self.column_widths)) :
           self.setColumnWidth(i, self.column_widths[i])     
        
        self.setWordWrap(True)


    def get_column_names_list(self,dataset) :

        
        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[load_census_dataset_columns_data] dataset ",dataset))

        # set up the ui form from a qtdesigner ui
        cfgdir              =   cfg.DataframeCleanserCfgData.get_dfc_qt_dir_name()
        census_dir_name     =   cfgdir + "\\utils\Census\datasets\\"

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[load_census_dataset_columns_data] census_dir_name ",census_dir_name))

        column_file_name    =   census_dir_name + dataset + "_columns.json"
        
        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[load_census_dataset_columns_data] column_file_name ",column_file_name))
        
        import json
        dataset_columns     =   []

        with open(column_file_name,'r') as  in_file :
                            
                dataset_columns = json.load(in_file)
                in_file.close()

        return(dataset_columns)



    # -----------------------------------------------------------------#
    # -                     load the table data                       -#
    # -----------------------------------------------------------------#
    def load_census_dataset_columns_data(self,dataset):

        column_names        =   self.get_column_names_list(dataset)
        self.num_columns    =   len(column_names)

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[load_census_dataset_columns_data] column_names ",type(column_names),len(column_names)))

        data    =   []

        for i in range(len(column_names)) :
                
            data_row    =   []

            data_row.append(i)
            data_row.append(column_names[i])

            data.append(data_row)

        self.column_headers     =   ["Column Number","Column Description"]
        self.column_widths      =   [100,850]

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[Census_dataset_columns_Table] end"))

        return(data)
    
class Census_dataset_columns_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[Census_dataset_columns_Widget]"))

        super().__init__()

        self.parent     =   dfparms[0]
        self.dataset    =   dfparms[1]

        self.init_form()

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[Census_dataset_columns_Widget] end"))

    def reload_data(self,parent) :

        self.parent     =   parent

    def init_form(self):  

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[Census_dataset_columns_Widget][init_form]"))

        from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QHBoxLayout


        self.dataset_table   =   QWidget()
        self.dataset_table   =   Census_dataset_columns_Table(self.parent,self.dataset)

        self.title_label    =   QLabel()
        self.title_label.setText("\n" + self.dataset + " Dataset Columns : " + str(self.dataset_table.num_columns) + " Columns \n")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.resize(600,50)
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold; font-family: Arial; ")

        self.spacer    =   QLabel()
        self.spacer.setText("")
        self.spacer.setAlignment(Qt.AlignCenter)
        self.spacer.resize(600,50)
        self.spacer.setStyleSheet("font-size: 18px; font-weight: bold; font-family: Arial; ")


        # buttons for inspect rows
        from PyQt5.QtWidgets import QPushButton
        download_button         =   QPushButton()     
        download_button.setText("Download Dataset")
        download_button.setFixedSize(200,30)
        download_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        download_button.clicked.connect(self.download_dataset) 

        self.buttons_bar   =   QHBoxLayout()
        self.buttons_bar.addWidget(download_button)

        self.final_layout   =   QVBoxLayout()
        self.final_layout.addWidget(self.title_label)
        self.final_layout.addWidget(self.dataset_table)
        self.final_layout.addWidget(self.spacer)
        self.final_layout.addLayout(self.buttons_bar)
        self.final_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.final_layout)

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[Census_dataset_columns_Widget][init_form] end"))


    def download_dataset(self) :

        if(is_debug_on(SWCensusUtility_ID,"DEBUG_CENSUS")) :
            add_debug_to_log("Census",print_to_string("[Census_dataset_columns_Widget][download_dataset]"))
        

        from dfcleanser.common.common_utils import display_url
        datasets_url    =   "https://github.com/RickKrasinski/dfc_census_zips"
        display_url(datasets_url)



