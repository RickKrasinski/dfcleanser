"""
# ZipCodeWidgets
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

DEBUG_ZIPCODE               =   True
DEBUG_ZIPCODE_DETAILS       =   False

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -             general Data Import Housekeeping                  -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

import logging
logger = logging.getLogger(__name__)

DEFAULT_ROW_HEIGHT                  =   20



"""
#--------------------------------------------------------------------------
#    zipcode attributes input form
#--------------------------------------------------------------------------
"""
zipcode_atributes_input_title             =   "Zipcode Attributes"
zipcode_atributes_input_id                =   "zipcodeattrs"
zipcode_atributes_input_idList            =   ["zipcodeid",
                                               None,None,None]

zipcode_atributes_input_labelList         =   ["zip_code",
                                               "Get</br>Zipcode</br>Attributes",
                                               "Return","Help"]

zipcode_atributes_input_typeList          =   ["text","button","button","button"]

zipcode_atributes_input_placeholderList   =   ["Enter 5 didgit zipcode",
                                              None,None,None]

zipcode_atributes_input_reqList           =   [0]


"""
#--------------------------------------------------------------------------
#    zipcode cities input form
#--------------------------------------------------------------------------
"""
zipcode_cities_input_title             =   "Zipcode Cities"
zipcode_cities_input_id                =   "zipcodecities"
zipcode_cities_input_idList            =   ["cityname",
                                            "cityselect",
                                            "stateid",
                                             None,None,None,None]

zipcode_cities_input_labelList         =   ["city",
                                            "city list",
                                            "state",
                                            "Find</br>Closest</br>Cities",
                                            "Get</br>Zipcodes</br>For City",
                                            "Return","Help"]

zipcode_cities_input_typeList          =   ["text","select","select","button","button","button","button"]

zipcode_cities_input_placeholderList   =   ["enter city",
                                            "select city",
                                            "select state",
                                           None,None,None,None]

zipcode_cities_input_reqList           =   [0,1,2]


"""
#--------------------------------------------------------------------------
#    state counties input form
#--------------------------------------------------------------------------
"""
state_counties_input_title             =   "State Counties"
state_counties_input_id                =   "statecounties"
state_counties_input_idList            =   ["stateid",
                                             None,None,None]

state_counties_input_labelList         =   ["state",
                                            "Get</br>State</br>Counties",
                                            "Return","Help"]

state_counties_input_typeList          =   ["select","button","button","button"]

state_counties_input_placeholderList   =   ["select state",
                                            None,None,None]

state_counties_input_reqList           =   [0]


"""
#--------------------------------------------------------------------------
#    county cities input form
#--------------------------------------------------------------------------
"""
county_cities_input_title             =   "County Cities"
county_cities_input_id                =   "countycities"
county_cities_input_idList            =   ["stateid",
                                           "countyid",
                                           None,None,None]

county_cities_input_labelList         =   ["state",
                                           "county",
                                           "Get</br>County</br>Cities",
                                           "Return","Help"]

county_cities_input_typeList          =   ["select","select","button","button","button"]

county_cities_input_placeholderList   =   ["select state",
                                           "select county",
                                           None,None,None]


county_cities_input_reqList           =   [0,1]


"""
#--------------------------------------------------------------------------
#    state cities input form
#--------------------------------------------------------------------------
"""
state_cities_input_title             =   "State Counties"
state_cities_input_id                =   "statecities"
state_cities_input_idList            =   ["stateid",
                                          None,None,None]

state_cities_input_labelList         =   ["state",
                                          "Get</br>State</br>Cities",
                                          "Return","Help"]

state_cities_input_typeList          =   ["select","button","button","button"]

state_cities_input_placeholderList   =   ["select state",None,None,None]

state_cities_input_reqList           =   [0]


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                  ZipCode attributes Objects                   -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class ZipCode_attributesModel(QtCore.QAbstractTableModel):
    def __init__(self, dfsdata, colheaders):

        super(ZipCode_attributesModel, self).__init__()
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


class ZipCode_attributes_Table(QtWidgets.QTableView):

    def __init__(self,  tblparms, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.zipcode_to_get     =   tblparms[0]

        if(DEBUG_ZIPCODE) :
            print("\n  [ZipCode_attributes_Table] : init",self.zipcode_to_get)

        self.init_tableview()

        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_attributes_Table] : end")

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self, zipcode):
        
        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_attributes_Table][reload_data] zipcode : ",zipcode)

        self.zipcode_to_get     =   zipcode
        tbldata    =   self.load_zipcode_attr_data()
        self.model.reload_data(tbldata)


    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_attributes_Table][init_tableview]")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        zipcodeattr_data     =   self.load_zipcode_attr_data()
        
        if(DEBUG_ZIPCODE) :
           print("  [ZipCode_attributes_Table][init_tableview] :headers",self.column_headers)

        if(self.model is None) :
            self.model = ZipCode_attributesModel(zipcodeattr_data,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_ZIPCODE) :
           print("  [ZipCode_attributes_Table][init_tableview] : model loaded")

        self.num_rows   =   len(zipcodeattr_data)
        
        if(self.num_rows < 25) :
            new_height  =   40 + (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   40 + (15 * DEFAULT_ROW_HEIGHT)

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
        nrows = len(zipcodeattr_data)
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
    def load_zipcode_attr_data(self):

        attrTitles      =   ["Current Status","Zipcode Type","Primary City(s)","Acceptable City(s)","Not Acceptable City(s)",
                             "County","State","[Latitude, Longitude]","Area Codes"]
    
        from dfcleanser.Qt.utils.ZipCode.ZipCodeModel import get_zipcode_attributes
        attrValuesDict      =   get_zipcode_attributes(self.zipcode_to_get)

        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_attributes_Table][load_zipcode_attr_data]")

        data    =   []

        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_attributes_Table][load_zipcode_attr_data] attrValuesDict : \n",attrValuesDict)

        for i in range(len(attrTitles)) :
                
            data_row    =   []

            data_row.append(attrTitles[i])
            attrValue   =   str(attrValuesDict.get(attrTitles[i]))
            data_row.append(attrValue)

            data.append(data_row)

        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_attributes_Table] : data")
            for j in range(len(data)) :
                print("  [",j,"] : ",data[j])

        self.column_headers     =   ["Attribute Name","Attribute Value"]
        self.column_widths      =   [150,430]

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_attributes_Table]")

        return(data)
    
# -----------------------------------------------------------------#
# -             get zipcode attribute input form                  -#
# -----------------------------------------------------------------#
def get_zipcode_attribute_form(get_attrs_callback,return_callback,help_callback) :

    form_parms      =   [zipcode_atributes_input_id,zipcode_atributes_input_idList,zipcode_atributes_input_labelList,zipcode_atributes_input_typeList,zipcode_atributes_input_placeholderList,zipcode_atributes_input_reqList]
    comboMethods    =   None
    comboList       =   None
    file_methods    =   None
    button_methods  =   [get_attrs_callback,return_callback,help_callback]
    cfg_parms       =   None
    form_title      =   "\nGet Zipcode Attributes\n"
    form_width      =   600

    form_parms.append(comboList)
    form_parms.append(comboMethods)            
    form_parms.append(file_methods)
    form_parms.append(button_methods)            
    form_parms.append(cfg_parms)            
    form_parms.append(form_title)
    form_parms.append(form_width)        

    from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
    zipcode_attrs_form    =   dfcleanser_input_form_Widget(form_parms)

    return(zipcode_attrs_form)


class ZipCode_attributes_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_attributes_Widget]")

        super().__init__()

        self.parent     =   dfparms[0]

        self.init_form()

        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_attributes_Widget] end")

    def reload_data(self,parent) :

        self.parent     =   parent

    def init_form(self):  

        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_attributes_Widget][init_form]")

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.zipcodeattrsLayout     =   QVBoxLayout()

        self.zipcode_attrs_form    =   get_zipcode_attribute_form(self.get_zipcode_attrs,self.return_from_get_attrs,self.help_for_get_attrs)

        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        zipcode_container = QWidget()
        zipcode_container.setFixedWidth(600)       

        self.zipcodeLayout     =   QVBoxLayout(zipcode_container)
        self.zipcodeLayout.addWidget(self.zipcode_attrs_form)
        self.zipcodeLayout.addStretch()

        self.final_widget   =   QWidget()
        self.final_widget.setLayout(self.zipcodeLayout)
        self.final_widget.setFixedWidth(600)

        self.final_layout   =   QVBoxLayout()
        self.final_layout.addWidget(self.final_widget)
        self.final_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.final_layout)

        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_attributes_Widget][init_form] end")

    
    def get_zipcode_attrs(self) :
 
        zipcode     =   self.zipcode_attrs_form.get_form_input_value_by_index(0)

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_attributes_Widget][get_zipcode_attrs]",zipcode)

        self.parent.display_zipcode_attributes_data(zipcode)

    def return_from_get_attrs(self) :

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_attributes_Widget][return_from_get_attrs]")

        self.parent.init_zipcodes()

    def help_for_get_attrs(self) :

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_attributes_Widget][help_for_get_attrs]")


class ZipCode_attributes_with_data_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_attributes_with_data_Widget]")

        super().__init__()

        self.parent     =   dfparms[0]
        self.zipcode    =   dfparms[1]

        self.init_form()

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_attributes_with_data_Widget] end")

    def reload_data(self,parent,zipcode) :

        self.parent     =   parent
        self.zipcode    =   zipcode
        
        if(DEBUG_ZIPCODE) :
            print("[ZipCode_attributes_with_data_Widget][reload_d] zipcode : ",self.zipcode)

        self.zipcode_attrs_data_table.reload_data(self.zipcode)

    def init_form(self):  

        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_attributes_with_data_Widget][init_form]")

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.zipcodeattrsdataLayout     =   QVBoxLayout()

        self.zipcode_attrs_data_form    =   get_zipcode_attribute_form(self.get_zipcode_data_attrs,self.return_from_get_data_attrs,self.help_for_get_data_attrs)

        tblparms   =   [self.zipcode]       
        self.zipcode_attrs_data_table   =   ZipCode_attributes_Table(tblparms)

        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        zipcodedata_container = QWidget(self)
        zipcodedata_container.setFixedWidth(600)       

        self.zipcodedataLayout     =   QVBoxLayout(zipcodedata_container)
        self.zipcodedataLayout.addWidget(self.zipcode_attrs_data_form)
        self.zipcodedataLayout.addWidget(self.zipcode_attrs_data_table)
        self.zipcodedataLayout.addStretch()
        self.zipcodedataLayout.setAlignment(QtCore.Qt.AlignCenter)

        self.finaldata_widget   =   QWidget()
        self.finaldata_widget.setLayout(self.zipcodedataLayout)
        self.finaldata_widget.setFixedWidth(600)

        self.finaldata_layout   =   QVBoxLayout()
        self.finaldata_layout.addWidget(self.finaldata_widget)
        self.finaldata_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.finaldata_layout)

        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_attributes_with_data_Widget][init_form] end")
    
    def get_zipcode_data_attrs(self) :
 
        zipcode     =   self.zipcode_attrs_data_form.get_form_input_value_by_index(0)

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_attributes_Widget][get_zipcode_data_attrs]",zipcode)

        self.parent.display_zipcode_attributes_data(zipcode)

    def return_from_get_data_attrs(self) :

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_attributes_Widget][return_from_get_data_attrs]")

        self.parent.init_zipcodes()

    def help_for_get_data_attrs(self) :

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_attributes_Widget][help_for_get_data_attrs]")


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                 ZipCode attributes Objects end                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                   ZipCode locations Objects                   -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class ZipCode_locations_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_locations_Widget]")

        super().__init__()

        self.parent     =   dfparms[0]

        self.init_form()

        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_locations_Widget] end")

    def reload_data(self,parent) :

        self.parent     =   parent

    def init_form(self):  

        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_locations_Widget][init_form]")

        # build the overall dtypes layout

        from PyQt5.QtWidgets import QPushButton
       
        zipcity_button        =   QPushButton()     
        zipcity_button.setText("Get\nZipcodes\nFor City")
        zipcity_button.setFixedSize(178,70)
        zipcity_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        zipcity_button.clicked.connect(self.get_zipcodes_for_city) 

        statecnty_button        =   QPushButton()     
        statecnty_button.setText("Get\nCounties\nFor State")
        statecnty_button.setFixedSize(178,70)
        statecnty_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        statecnty_button.clicked.connect(self.get_counties_for_state) 

        cntycities_button        =   QPushButton()     
        cntycities_button.setText("Get\nCities\nFor County")
        cntycities_button.setFixedSize(178,70)
        cntycities_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        cntycities_button.clicked.connect(self.get_cities_for_county) 

        statecities_button        =   QPushButton()     
        statecities_button.setText("Get\nCities\nFor State")
        statecities_button.setFixedSize(178,70)
        statecities_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        statecities_button.clicked.connect(self.get_cities_for_state) 

        return_button        =   QPushButton()     
        return_button.setText("Retuen")
        return_button.setFixedSize(178,70)
        return_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        return_button.clicked.connect(self.return_from_get_location) 
        
        help_button        =   QPushButton()     
        help_button.setText("Help")
        help_button.setFixedSize(178,70)
        help_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        help_button.clicked.connect(self.help_for_get_location) 


        from PyQt5.QtWidgets import QHBoxLayout
        ccbutonsLayout  =   QHBoxLayout()
        ccbutonsLayout.addWidget(zipcity_button)
        ccbutonsLayout.addWidget(statecnty_button)
        ccbutonsLayout.addWidget(cntycities_button)
        ccbutonsLayout.addWidget(statecities_button)
        ccbutonsLayout.addWidget(return_button)
        ccbutonsLayout.addWidget(help_button)
        ccbutonsLayout.setAlignment(Qt.AlignHCenter)

        from PyQt5.QtWidgets import QVBoxLayout
        locationsLayout  =   QVBoxLayout()
        locationsLayout.addLayout(ccbutonsLayout)
        locationsLayout.addStretch()

        self.setLayout(locationsLayout)

    
    def get_zipcodes_for_city(self) :
 
        if(DEBUG_ZIPCODE) :
            print("[ZipCode_locations_Widget][get_zipcodes_for_city]")

        self.parent.display_city_zipcodes()

    def get_counties_for_state(self) :
 
        if(DEBUG_ZIPCODE) :
            print("[ZipCode_locations_Widget][get_counties_for_state]")

        self.parent.display_state_counties()

 
    def get_cities_for_county(self) :
 
        if(DEBUG_ZIPCODE) :
            print("[ZipCode_locations_Widget][get_cities_for_county]")

        self.parent.display_county_cities()

    def get_cities_for_state(self) :
 
        if(DEBUG_ZIPCODE) :
            print("[ZipCode_locations_Widget][get_cities_for_state]")

        self.parent.display_state_cities()

    def return_from_get_location(self) :

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_locations_Widget][return_from_get_attrs]")

        self.parent.init_zipcodes()

    def help_for_get_location(self) :

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_locations_Widget][help_for_get_location")


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                  ZipCode locations Objects end                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                  ZipCodes for Cities Objects                  -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class ZipCode_Cities_Model(QtCore.QAbstractTableModel):
    def __init__(self, dfsdata, colheaders):

        super(ZipCode_Cities_Model, self).__init__()
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
            else :
                return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:

            if( self._data[row][1] == "Zipcodes") :
                bgcolor = QtGui.QBrush(QColor(240, 234, 193))
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


class ZipCode_Cities_Table(QtWidgets.QTableView):

    def __init__(self,  tblparms, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.city           =   tblparms[0]
        self.state          =   tblparms[1]

        if(DEBUG_ZIPCODE) :
            print("\n  [ZipCode_Cities_Table] : init",self.city, self.state)

        self.init_tableview()

        if(DEBUG_ZIPCODE) :
            print("  ZipCode_Cities_Table] : end")

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self, city, state):
        
        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_Cities_Table][reload_data] zipcode : ",city,state)

        self.city           =   city
        self.state          =   state

        tbldata    =   self.load_zipcode_cities_data()
        self.model.reload_data(tbldata)

        num_rows   =   len(tbldata)
        
        if(num_rows < 8) :
            new_height  =   40 + (num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   40 + (8 * DEFAULT_ROW_HEIGHT)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)


    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_Cities_Table][init_tableview]")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        zipcodecities_data     =   self.load_zipcode_cities_data()
        
        if(DEBUG_ZIPCODE) :
           print("  [ZipCode_attributes_Table][init_tableview] :headers",self.column_headers)

        if(self.model is None) :
            self.model = ZipCode_Cities_Model(zipcodecities_data,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_ZIPCODE) :
           print("  [ZipCode_Cities_Table][init_tableview] : model loaded")

        self.num_rows   =   len(zipcodecities_data)
        
        if(self.num_rows < 10) :
            new_height  =   40 + (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   40 + (10 * DEFAULT_ROW_HEIGHT)

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
        nrows = len(zipcodecities_data)
        for row in range(nrows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(self.column_widths)) :
           self.setColumnWidth(i, self.column_widths[i])     
        
        self.setWordWrap(True)

    def load_zipcode_cities_type_data(self,zipcodelist) :

        data    =   []

        if( not (zipcodelist is None)) :

            for i in range(len(zipcodelist)) :

                if( (i % 15) == 0) :
                
                    if(i>0) : 
                        data_row.append(str(zipcodelist[i]))
                        data.append(data_row)

                    data_row    =   []

                else :

                    data_row.append(str(zipcodelist[i]))

            if(len(data_row)> 0) :
                num_to_fill     =   15 - len(data_row)

                for j in range(num_to_fill) :
                    data_row.append("")

                data.append(data_row)

        #else :

        #    data.append(["","","","","","","","","","","","","","",""])

        return(data)

    # -----------------------------------------------------------------#
    # -                     load the table data                       -#
    # -----------------------------------------------------------------#
    def load_zipcode_cities_data(self):

        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_Cities_Table][load_zipcode_cities_data]",self.state, self.city)

        table_state     = self.state[0:2]  

        from dfcleanser.Qt.utils.ZipCode.ZipCodeModel import (CITY_ZIPS_PRIMARY_LIST, CITY_ZIPS_SECONDARY_LIST, CITY_ZIPS_POBOX_LIST, CITY_ZIPS_UNIQUES_LIST, 
                                                              CITY_ZIPS_UNACCEPTABLE_LIST, CITY_ZIPS_DECOMMISSIONED_LIST, get_zipcodes_for_city)
        
        zip_data        =   []

        primary_header  =   ["Primary","Zipcodes","","","","","","","","","","","","",""]
        zipcode_list    =   get_zipcodes_for_city(table_state, self.city, CITY_ZIPS_PRIMARY_LIST)
        list_data       =   self.load_zipcode_cities_type_data(zipcode_list)
        if(len(list_data)>0) :
            zip_data.append(primary_header) 
            for i in range(len(list_data)) :
                zip_data.append(list_data[i])

        secondary_header  =   ["Secondry","Zipcodes","","","","","","","","","","","","",""]
        zipcode_list    =   get_zipcodes_for_city(table_state, self.city, CITY_ZIPS_SECONDARY_LIST)
        list_data       =   self.load_zipcode_cities_type_data(zipcode_list)
        if(len(list_data)>0) :
            zip_data.append(secondary_header)
            for i in range(len(list_data)) :
                zip_data.append(list_data[i])

        pobox_header  =   ["P.O. Box","Zipcodes","","","","","","","","","","","","",""]
        zipcode_list    =   get_zipcodes_for_city(table_state, self.city, CITY_ZIPS_POBOX_LIST)
        list_data       =   self.load_zipcode_cities_type_data(zipcode_list)
        if(len(list_data)>0) :
            zip_data.append(pobox_header)
            for i in range(len(list_data)) :
                zip_data.append(list_data[i])
        
        unique_header  =   ["Uniques","Zipcodes","","","","","","","","","","","","",""]
        zipcode_list    =   get_zipcodes_for_city(table_state, self.city, CITY_ZIPS_UNIQUES_LIST)
        list_data       =   self.load_zipcode_cities_type_data(zipcode_list)
        if(len(list_data)>0) :
            zip_data.append(unique_header)
            for i in range(len(list_data)) :
                zip_data.append(list_data[i])

        decom_header  =   ["Decomm","Zipcodes","","","","","","","","","","","","",""]
        zipcode_list    =   get_zipcodes_for_city(table_state, self.city, CITY_ZIPS_DECOMMISSIONED_LIST)
        list_data       =   self.load_zipcode_cities_type_data(zipcode_list)
        if(len(list_data)>0) :
            zip_data.append(decom_header)
            for i in range(len(list_data)) :
                zip_data.append(list_data[i])

        dead_header     =   ["Dead","Zipcodes","","","","","","","","","","","","",""]
        zipcode_list    =   get_zipcodes_for_city(table_state, self.city, CITY_ZIPS_UNACCEPTABLE_LIST)
        list_data       =   self.load_zipcode_cities_type_data(zipcode_list)
        if(len(list_data)>0) :
            zip_data.append(dead_header)
            for i in range(len(list_data)) :
                zip_data.append(list_data[i])


        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_Cities_Table][load_zipcode_cities_data]",zipcode_list)

        self.column_headers     =   ["","","","","","","","","","","","","","",""]
        self.column_widths      =   [64,64,64,64,64,64,64,64,64,64,64,64,64,64,64]

        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_Cities_Table] end load")

        return(zip_data)

def get_zipcode_cities_form(find_cities_callback,get_attrs_callback,return_callback,help_callback,update_city,update_city_list) :

    if(DEBUG_ZIPCODE) :
        print("    [ZipCode_Cities_Table][get_zipcode_cities_form]")

    form_parms      =   [zipcode_cities_input_id,zipcode_cities_input_idList,zipcode_cities_input_labelList,zipcode_cities_input_typeList,zipcode_cities_input_placeholderList,zipcode_cities_input_reqList]
    comboMethods    =   [update_city,update_city_list]
    comboList       =   None
    file_methods    =   None
    button_methods  =   [find_cities_callback,get_attrs_callback,return_callback,help_callback]
    cfg_parms       =   None
    form_title      =   "Get City Zipcodes\n"
    form_width      =   600

    selectDicts     =   []

    from dfcleanser.sw_utilities.DFCDataStores import get_Dict
    states_dict  =   get_Dict("US_States_and_Territories")
    
    if(DEBUG_ZIPCODE_DETAILS) :
        print("    [ZipCode_Cities_Table][get_zipcode_cities_form] states_dict : \n",states_dict)
    
    state_keys  =   list(states_dict.keys())
    state_keys.sort()

    if(DEBUG_ZIPCODE_DETAILS) :
        print("    [ZipCode_Cities_Table][get_zipcode_cities_form] state_keys : \n",state_keys)
    
    states_list     =   []
    
    for i in range(len(state_keys)) :
        states_list.append(str(state_keys[i]) + " : " + str(states_dict.get(state_keys[i])))

    if(DEBUG_ZIPCODE_DETAILS) :
        print("    [ZipCode_Cities_Table][get_zipcode_cities_form] states_list \n",states_list)

    state_sel    =   {"default":states_list[0],"list":states_list}

    if(DEBUG_ZIPCODE) :
        print("    [ZipCode_Cities_Table][get_zipcode_cities_form] state_sel built : ")


    from dfcleanser.Qt.utils.ZipCode.ZipCodeModel import (us_zipcodes, ANY_LOCATION_TYPE)
    state_parm      =   states_list[0][0:2] 
    cities_list     =   us_zipcodes.get_cities_for_state(state_parm, ANY_LOCATION_TYPE)
    city_sel        =   {"default":cities_list[0],"list":cities_list}
    
    if(DEBUG_ZIPCODE) :
        print("    [ZipCode_Cities_Table][get_zipcode_cities_form] city_sel built : ")

    selectDicts.append(city_sel)
    selectDicts.append(state_sel)  

    form_parms.append(selectDicts)
    form_parms.append(comboMethods)            
    form_parms.append(file_methods)
    form_parms.append(button_methods)            
    form_parms.append(cfg_parms)            
    form_parms.append(form_title)
    form_parms.append(form_width)   

    if(DEBUG_ZIPCODE) :
        print("    [ZipCode_Cities_Table][get_zipcode_cities_form] parms built : ")


    from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
    zipcode_cities_form    =   dfcleanser_input_form_Widget(form_parms)

    if(DEBUG_ZIPCODE) :
        print("    [ZipCode_Cities_Table][get_zipcode_cities_form] zipcode_cities_form built")

    return(zipcode_cities_form)


class ZipCode_Cities_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_Cities_Widget]")

        super().__init__()

        self.parent     =   dfparms[0]

        self.init_form()

        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_Cities_Widget] end")

    def reload_data(self,parent) :

        self.parent     =   parent

    def init_form(self):  

        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_Cities_Widgett][init_form]")

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.zipcodeattrsLayout     =   QVBoxLayout()

        self.zipcode_cities_form    =   get_zipcode_cities_form(self.find_closest_city,self.get_zipcode_cities,self.return_from_get_cities,self.help_for_get_cities,self.select_city,self.get_new_city_list)

        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        zipcode_container = QWidget()
        zipcode_container.setFixedWidth(600)       

        self.zipcodeLayout     =   QVBoxLayout(zipcode_container)
        self.zipcodeLayout.addWidget(self.zipcode_cities_form)
        self.zipcodeLayout.addStretch()

        self.final_widget   =   QWidget()
        self.final_widget.setLayout(self.zipcodeLayout)
        self.final_widget.setFixedWidth(600)

        self.final_layout   =   QVBoxLayout()
        self.final_layout.addWidget(self.final_widget)
        self.final_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.final_layout)

        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_Cities_Widget][init_form] end")

    def find_closest_city(self) :

        city       =   self.zipcode_cities_form.get_form_input_value_by_index(0)
        state      =   self.zipcode_cities_form.get_form_input_value_by_index(2)

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_Cities_Widget][find_closest_city]",city,state)

        from dfcleanser.Qt.utils.ZipCode.ZipCodeModel import (us_zipcodes, ANY_LOCATION_TYPE)
        state_parm      =   state[0:2]
        cities_list     =   us_zipcodes.get_cities_for_state(state_parm, ANY_LOCATION_TYPE)

        char_to_match   =   city[0]
        char_to_match   =   char_to_match.upper()

        combo_index     =   0

        for i in range(len(cities_list)) :

            list_char   =   cities_list[i][0]

            if( (list_char == char_to_match) or (list_char > char_to_match)) :
                combo_index     =   i
                break

        self.zipcode_cities_form.set_form_combobox_index(1, combo_index)


    def select_city(self) :

        city       =   self.zipcode_cities_form.get_form_input_value_by_index(1)
        
        if(DEBUG_ZIPCODE) :
            print("[ZipCode_Cities_Widget][select_city]",city)

        self.zipcode_cities_form.set_form_input_value_by_index(0,city)
       

    def get_new_city_list(self) :

        state       =   self.zipcode_cities_form.get_form_input_value_by_index(2)
        state_parm  =   state[0:2]

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_Cities_Widget][get_new_city_list]",state)

        from dfcleanser.Qt.utils.ZipCode.ZipCodeModel import (us_zipcodes, ANY_LOCATION_TYPE)
        cities_list     =   us_zipcodes.get_cities_for_state(state_parm, ANY_LOCATION_TYPE)

        self.zipcode_cities_form.reset_form_combobox_by_index(1, cities_list)


    def get_zipcode_cities(self) :
 
        city     =   self.zipcode_cities_form.get_form_input_value_by_index(0)
        state    =   self.zipcode_cities_form.get_form_input_value_by_index(2)


        if(DEBUG_ZIPCODE) :
            print("[ZipCode_Cities_Widget][get_zipcode_cities]",city,state)

        self.parent.display_city_zipcodes_data(city,state)

    def return_from_get_cities(self) :

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_Cities_Widget][return_from_get_cities]")

        self.parent.init_zipcodes()

    def help_for_get_cities(self) :

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_Cities_Widget][help_for_get_cities]")


class ZipCode_Cities_with_data_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_Cities_with_data_Widget]")

        super().__init__()

        self.parent     =   dfparms[0]
        self.city       =   dfparms[1]
        self.state      =   dfparms[2]
 
        self.init_form()

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_Cities_with_data_Widget] end")

    def reload_data(self,parent,city,state) :

        self.parent     =   parent
        self.city       =   city
        self.state      =   state

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_Cities_with_data_Widget][reload_data] ",self.city,self.state)

        self.zipcode_cities_data_table.reload_data(self.city,self.state)
        
        display_state   =   self.state[5:]
        self.zipcode_cities_datanote_label.setText("\nZipcodes for " + self.city + " " + display_state + "\n")

    def init_form(self):  

        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_Cities_with_data_Widget][init_form]")

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        #self.zipcodeattrsdataLayout     =   QVBoxLayout()

        self.zipcode_cities_data_form    =   get_zipcode_cities_form(self.find_nearest_city,self.get_zipcode_data_cities,self.return_from_get_data_cities,self.help_for_get_data_cities,self.select_new_city,self.reset_city_list)

        tblparms   =   [self.city,self.state]       
        self.zipcode_cities_data_table   =   ZipCode_Cities_Table(tblparms)

        display_state   =   self.state[0:5]
        from PyQt5.QtWidgets import QLabel
        self.zipcode_cities_datanote_label   =   QLabel()
        self.zipcode_cities_datanote_label.setText("\nZipcodes for " + self.city + " " + display_state + "\n")
        self.zipcode_cities_datanote_label.setAlignment(Qt.AlignLeft)
        self.zipcode_cities_datanote_label.resize(600,50)
        self.zipcode_cities_datanote_label.setStyleSheet("font-size: 14px; font-weight: bold; font-family: Arial; ")

        from PyQt5.QtWidgets import QVBoxLayout, QWidget
        self.cityzipcodesLayout     =   QVBoxLayout()
        self.cityzipcodesLayout.addWidget(self.zipcode_cities_data_form)
        self.cityzipcodesLayout.addWidget(self.zipcode_cities_datanote_label)
        self.cityzipcodesLayout.addWidget(self.zipcode_cities_data_table)
        self.cityzipcodesLayout.addStretch()
        self.cityzipcodesLayout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.cityzipcodesLayout)

        """
        cityzipcodes_container = QWidget(self)
        cityzipcodes_container.setFixedWidth(600)       

        self.cityzipcodesLayout     =   QVBoxLayout(cityzipcodes_container)
        self.cityzipcodesLayout.addWidget(self.zipcode_cities_data_form)
        self.cityzipcodesLayout.addStretch()
        self.cityzipcodesLayout.setAlignment(QtCore.Qt.AlignCenter)

        self.finaldata_widget   =   QWidget()
        self.finaldata_widget.setLayout(self.cityzipcodesLayout)
        self.finaldata_widget.setFixedWidth(600)

        self.finaldata_layout   =   QVBoxLayout()
        self.finaldata_layout.addWidget(self.finaldata_widget)
        self.finaldata_layout.addWidget(self.zipcode_cities_datanote_label)
        self.finaldata_layout.addWidget(self.zipcode_cities_data_table)
        self.finaldata_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.finaldata_layout)
        """
        if(DEBUG_ZIPCODE) :
            print("  [ZipCode_Cities_with_data_Widget][init_form] end")

    def find_nearest_city(self) :

        city       =   self.zipcode_cities_data_form.get_form_input_value_by_index(0)
        state      =   self.zipcode_cities_data_form.get_form_input_value_by_index(2)
        
        if(DEBUG_ZIPCODE) :
            print("[ZipCode_Cities_Widget][find_nearest_city]",city)

        from dfcleanser.Qt.utils.ZipCode.ZipCodeModel import (us_zipcodes, ANY_LOCATION_TYPE)
        state           =   self.zipcode_cities_form.get_form_input_value_by_index(2)
        state_parm      =   state[0:2]
        cities_list     =   us_zipcodes.get_cities_for_state(state_parm, ANY_LOCATION_TYPE)

        char_to_match   =   city[0]
        char_to_match   =   char_to_match.upper()

        combo_index     =   0

        for i in range(len(cities_list)) :

            list_char   =   cities_list[i][0]

            if( (list_char == char_to_match) or (list_char > char_to_match)) :
                combo_index     =   i
                break

        self.zipcode_cities_data_form.set_form_combobox_index(1, combo_index)
    
    def select_new_city(self) :

        city       =   self.zipcode_cities_data_form.get_form_input_value_by_index(1)
        
        if(DEBUG_ZIPCODE) :
            print("[ZipCode_Cities_Widget][select_city]",city)

        self.zipcode_cities_data_form.set_form_input_value_by_index(0,city)

    def reset_city_list(self) :

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_Cities_with_data_Widget][reset_city_list]")

        state           =   self.zipcode_cities_data_form.get_form_input_value_by_index(2)
        search_state    =   state[0:2]

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_Cities_with_data_Widget][reset_city_list]",state)

        from dfcleanser.Qt.utils.ZipCode.ZipCodeModel import (us_zipcodes, ANY_LOCATION_TYPE)
        cities_list     =   us_zipcodes.get_cities_for_state(search_state, ANY_LOCATION_TYPE)

        self.zipcode_cities_data_form.reset_form_combobox_by_index(1, cities_list)
    
    def get_zipcode_data_cities(self) :
 
        city     =   self.zipcode_cities_data_form.get_form_input_value_by_index(0)
        state    =   self.zipcode_cities_data_form.get_form_input_value_by_index(2)

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_Cities_with_data_Widget][get_zipcode_data_cities]",city,state)

        self.parent.display_city_zipcodes_data(city,state)

    def return_from_get_data_cities(self) :

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_Cities_with_data_Widget][return_from_get_data_attrs]")

        self.parent.init_zipcodes()

    def help_for_get_data_cities(self) :

        if(DEBUG_ZIPCODE) :
            print("[ZipCode_Cities_with_data_Widget][help_for_get_data_attrs]")


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                 ZipCodes for Cities Objects end               -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                     State Counties Objects                    -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class State_Counties_Model(QtCore.QAbstractTableModel):
    def __init__(self, dfsdata, colheaders):

        super(State_Counties_Model, self).__init__()
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
            else :
                return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:
            if(column == 0):
                bgcolor = QtGui.QBrush(QtCore.Qt.white)#QtGui.QBrush(QColor(240, 234, 193))
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


class State_Counties_Table(QtWidgets.QTableView):

    def __init__(self,  tblparms, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.state          =   tblparms[0]

        if(DEBUG_ZIPCODE) :
            print("\n  [State_Counties_Table] : init",self.state)

        self.init_tableview()

        if(DEBUG_ZIPCODE) :
            print("  [State_Counties_Table] : end")

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self, state):
        
        if(DEBUG_ZIPCODE) :
            print("  [State_Counties_Table][reload_data] zipcode : ",state)

        self.state          =   state
 
        tbldata    =   self.load_state_counties_data()
        self.model.reload_data(tbldata)

        num_rows   =   len(tbldata)
        
        if(num_rows < 10) :
            new_height  =   40 + (num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   40 + (10 * DEFAULT_ROW_HEIGHT)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)


    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(DEBUG_ZIPCODE) :
            print("  [State_Counties_Table][init_tableview]")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        statecounties_data     =   self.load_state_counties_data()
        
        if(DEBUG_ZIPCODE) :
           print("  [State_Counties_Table][init_tableview] :headers",self.column_headers)

        if(self.model is None) :
            self.model = State_Counties_Model(statecounties_data,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_ZIPCODE) :
           print("  [State_Counties_Table][init_tableview] : model loaded")

        self.num_rows   =   len(statecounties_data)
        
        if(self.num_rows < 10) :
            new_height  =   40 + (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   40 + (10 * DEFAULT_ROW_HEIGHT)

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
        nrows = len(statecounties_data)
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
    def load_state_counties_data(self):

        if(DEBUG_ZIPCODE) :
            print("  [State_Counties_Table][load_state_counties_data]",self.state)

        table_state     = self.state[0:2]  

        from dfcleanser.Qt.utils.ZipCode.ZipCodeModel import (us_zipcodes)
        counties_list   =   us_zipcodes.get_state_counties_list(table_state)

        if(DEBUG_ZIPCODE) :
            print("  [State_Counties_Table][load_zipcode_cities_data]",counties_list)

        data    =   []

        if( not (counties_list is None)) :

            for i in range(len(counties_list)) :

                if( (i % 9) == 0) :
                
                    if(i>0) : 
                        data_row.append(str(counties_list[i]))
                        data.append(data_row)

                    data_row    =   []

                else :

                    data_row.append(str(counties_list[i]))

            if(len(data_row)> 0) :
                num_to_fill     =   9 - len(data_row)

                for j in range(num_to_fill) :
                    data_row.append("")

                data.append(data_row)

        else :

            data.append(["","","","","","","","",""])

        if(DEBUG_ZIPCODE) :
            print("  [State_Counties_Table] : data")
            for j in range(len(data)) :
                print("  [",j,"] : ",data[j])

        self.column_headers     =   ["","","","","","","","",""]
        self.column_widths      =   [108,108,108,108,108,108,108,108,108]

        if(DEBUG_ZIPCODE) :
            print("[State_Counties_Table]")

        return(data)

def get_state_counties_form(get_attrs_callback,return_callback,help_callback) :

    if(DEBUG_ZIPCODE) :
        print("    [State_Counties_Table][get_state_counties_form]")

    form_parms      =   [state_counties_input_id,state_counties_input_idList,state_counties_input_labelList,state_counties_input_typeList,state_counties_input_placeholderList,state_counties_input_reqList]
    comboMethods    =   [None]
    comboList       =   None
    file_methods    =   None
    button_methods  =   [get_attrs_callback,return_callback,help_callback]
    cfg_parms       =   None
    form_title      =   "Get State Counties\n"
    form_width      =   600

    selectDicts     =   []

    from dfcleanser.sw_utilities.DFCDataStores import get_Dict
    states_dict  =   get_Dict("US_States_and_Territories")
    
    if(DEBUG_ZIPCODE_DETAILS) :
        print("    [State_Counties_Table][get_state_counties_form] states_dict : \n",states_dict)
    
    state_keys  =   list(states_dict.keys())
    state_keys.sort()

    if(DEBUG_ZIPCODE_DETAILS) :
        print("    [State_Counties_Table][get_state_counties_form] state_keys : \n",state_keys)
    
    states_list     =   []
    
    for i in range(len(state_keys)) :
        states_list.append(str(state_keys[i]) + " : " + str(states_dict.get(state_keys[i])))

    if(DEBUG_ZIPCODE_DETAILS) :
        print("    [State_Counties_Table][get_state_counties_form] states_list \n",states_list)


    state_sel    =   {"default":states_list[0],"list":states_list}
    selectDicts.append(state_sel)  

    form_parms.append(selectDicts)
    form_parms.append(comboMethods)            
    form_parms.append(file_methods)
    form_parms.append(button_methods)            
    form_parms.append(cfg_parms)            
    form_parms.append(form_title)
    form_parms.append(form_width)    

    from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
    state_counties_form    =   dfcleanser_input_form_Widget(form_parms)

    if(DEBUG_ZIPCODE) :
        print("    [State_Counties_Table][get_state_counties_form] state_counties_form built")

    return(state_counties_form)


class State_Counties_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_ZIPCODE) :
            print("  [State_Counties_Widget]")

        super().__init__()

        self.parent     =   dfparms[0]

        self.init_form()

        if(DEBUG_ZIPCODE) :
            print("  [State_Counties_Widget] end")

    def reload_data(self,parent) :

        self.parent     =   parent

    def init_form(self):  

        if(DEBUG_ZIPCODE) :
            print("  [State_Counties_Widget][init_form]")

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.state_counties_form    =   get_state_counties_form(self.get_state_counties,self.return_from_get_counties,self.help_for_get_counties)

        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        zipcode_container = QWidget()
        zipcode_container.setFixedWidth(600)       

        self.statecountiesLayout     =   QVBoxLayout(zipcode_container)
        self.statecountiesLayout.addWidget(self.state_counties_form)
        self.statecountiesLayout.addStretch()

        self.final_widget   =   QWidget()
        self.final_widget.setLayout(self.statecountiesLayout)
        self.final_widget.setFixedWidth(600)

        self.final_layout   =   QVBoxLayout()
        self.final_layout.addWidget(self.final_widget)
        self.final_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.final_layout)

        if(DEBUG_ZIPCODE) :
            print("  [State_Counties_Widget][init_form] end")

    
    def get_state_counties(self) :
 
        state    =   self.state_counties_form.get_form_input_value_by_index(0)

        if(DEBUG_ZIPCODE) :
            print("[State_Counties__Widget][get_state_counties]",state)

        self.parent.display_state_counties_data(state)

    def return_from_get_counties(self) :

        if(DEBUG_ZIPCODE) :
            print("[State_Counties_data_Widget][return_from_get_counties]")

        self.parent.init_zipcodes()

    def help_for_get_counties(self) :

        if(DEBUG_ZIPCODE) :
            print("[State_Counties_with_data_Widget][help_for_get_counties]")


class State_Counties_with_data_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_ZIPCODE) :
            print("[State_Counties_with_data_Widget]")

        super().__init__()

        self.parent     =   dfparms[0]
        self.state      =   dfparms[1]
 
        self.init_form()

        if(DEBUG_ZIPCODE) :
            print("[State_Counties_with_data_Widget] end")

    def reload_data(self,parent,state) :

        self.parent     =   parent
        self.state      =   state
 
        if(DEBUG_ZIPCODE) :
            print("[State_Counties_with_data_Widget][reload_data] ",self.state)

        self.state_counties_data_table.reload_data(self.state)

        display_state   =   self.state[5:]
        self.counties_note_label.setText("\n" + display_state + " Counties\n")


    def init_form(self):  

        if(DEBUG_ZIPCODE) :
            print("  [State_Counties_with_data_Widget][init_form]")

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.state_counties_data_form    =   get_state_counties_form(self.get_state_counties_data,self.return_from_get_state_counties_data,self.help_for_get_state_counties_data)

        tblparms   =   [self.state]       
        self.state_counties_data_table   =   State_Counties_Table(tblparms)

        display_state  =   self.state[5:]
        from PyQt5.QtWidgets import QLabel
        self.counties_note_label   =   QLabel()
        self.counties_note_label.setText("\n" + display_state + " Counties\n")
        self.counties_note_label.setAlignment(Qt.AlignLeft)
        self.counties_note_label.resize(480,50)
        self.counties_note_label.setStyleSheet("font-size: 14px; font-weight: bold; font-family: Arial; ")

        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        #statecounties_container = QWidget(self)
        #statecounties_container.setFixedWidth(600)       

        self.statecountiesLayout     =   QVBoxLayout()
        self.statecountiesLayout.addWidget(self.state_counties_data_form)
        self.statecountiesLayout.addWidget(self.counties_note_label)
        self.statecountiesLayout.addWidget(self.state_counties_data_table)
        self.statecountiesLayout.addStretch()
        self.statecountiesLayout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.statecountiesLayout)

        """"
        self.statecountiesLayout.addWidget(self.state_counties_data_form)
        self.statecountiesLayout.addStretch()
        self.statecountiesLayout.setAlignment(QtCore.Qt.AlignCenter)

        self.finaldata_widget   =   QWidget()
        self.finaldata_widget.setLayout(self.statecountiesLayout)
        self.finaldata_widget.setFixedWidth(600)

        self.finaldata_layout   =   QVBoxLayout()
        self.finaldata_layout.addWidget(self.finaldata_widget)
        self.finaldata_layout.addWidget(self.counties_note_label)
        self.finaldata_layout.addWidget(self.state_counties_data_table)
        self.finaldata_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.finaldata_layout)

        """

        if(DEBUG_ZIPCODE) :
            print("  [State_Counties_with_data_Widget][init_form] end")

    
    def get_state_counties_data(self) :
 
        state    =   self.state_counties_data_form.get_form_input_value_by_index(0)
 
        if(DEBUG_ZIPCODE) :
            print("[State_Counties_with_data_Widget][get_zipcode_data_cities]",state)

        self.parent.display_state_counties_data(state)

    def return_from_get_state_counties_data(self) :

        if(DEBUG_ZIPCODE) :
            print("[State_Counties_with_data_Widget][return_from_get_state_counties_data]")

        self.parent.init_zipcodes()

    def help_for_get_state_counties_data(self) :

        if(DEBUG_ZIPCODE) :
            print("[State_Counties_with_data_Widget][elp_for_get_state_counties_data]")


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                    State Counties Objects end                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                    County Cities Objects end                  -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class County_Cities_Model(QtCore.QAbstractTableModel):
    def __init__(self, dfsdata, colheaders):

        super(County_Cities_Model, self).__init__()
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
            else :
                return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:
            if(column == 0):
                bgcolor = QtGui.QBrush(QtCore.Qt.white)#QtGui.QBrush(QColor(240, 234, 193))
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


class County_Cities_Table(QtWidgets.QTableView):

    def __init__(self,  tblparms, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.state          =   tblparms[0]
        self.county         =   tblparms[1]

        if(DEBUG_ZIPCODE) :
            print("\n  [County_Cities_Table] : init",self.state)

        self.init_tableview()

        if(DEBUG_ZIPCODE) :
            print("  [County_Cities_Table] : end")

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self, state,county):
        
        if(DEBUG_ZIPCODE) :
            print("  [County_Cities_Table][reload_data] zipcode : ",state)

        self.state          =   state
        self.county         =   county
 
        tbldata    =   self.load_county_cities_data()
        self.model.reload_data(tbldata)

        num_rows   =   len(tbldata)
        
        if(num_rows < 10) :
            new_height  =   40 + (num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   40 + (10 * DEFAULT_ROW_HEIGHT)

        print("new_height",new_height)
        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)


    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(DEBUG_ZIPCODE) :
            print("  [County_Cities_Table][init_tableview]")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        countycities_data     =   self.load_county_cities_data()
        
        if(DEBUG_ZIPCODE) :
           print("  [County_Cities_Table][init_tableview] :headers",self.column_headers)

        if(self.model is None) :
            self.model = County_Cities_Model(countycities_data,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_ZIPCODE) :
           print("  [County_Cities_Table][init_tableview] : model loaded")

        self.num_rows   =   len(countycities_data)
        
        if(self.num_rows < 10) :
            new_height  =   40 + ((self.num_rows) * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   40 + ((10) * DEFAULT_ROW_HEIGHT)

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
        nrows = len(countycities_data)
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
    def load_county_cities_data(self):

        if(DEBUG_ZIPCODE) :
            print("  [County_Cities_Table][load_county_cities_data]",self.state,self.county)

        table_state     = self.state[0:2]  

        from dfcleanser.Qt.utils.ZipCode.ZipCodeModel import (us_zipcodes, ANY_LOCATION_TYPE)
        cities_list     =   us_zipcodes.get_cities_for_county(table_state, self.county, ANY_LOCATION_TYPE)

        if(DEBUG_ZIPCODE) :
            print("  [County_Cities_Table][load_county_cities_data][cities_list]",cities_list)

        data                =   []
        data_row            =   []

        if( (not (cities_list is None)) and (len(cities_list) > 0)) :

            for i in range(len(cities_list)) :

                if( (i % 9) == 0) :
                
                    if(i>0) : 
                        
                        data.append(data_row)
                        data_row    =   []
                        data_row.append(str(cities_list[i]))

                    else :
                        data_row.append(str(cities_list[i]))

                else :

                    data_row.append(str(cities_list[i]))

            if(len(data_row) > 0) :
                num_to_fill     =   9 - len(data_row)

                for j in range(num_to_fill) :
                    data_row.append("")

                data.append(data_row)

        else :

            data.append(["","","","","","","","",""])

        if(DEBUG_ZIPCODE) :
            print("  [County_Cities_Table] : data")
            for j in range(len(data)) :
                print("  [",j,"] : ",data[j])

        self.column_headers     =   ["","","","","","","","",""]
        self.column_widths      =   [108,108,108,108,108,108,108,108,108]

        if(DEBUG_ZIPCODE) :
            print("[County_Cities_Table][end]")

        return(data)

def get_county_cities_form(get_attrs_callback,return_callback,help_callback,update_callback) :

    if(DEBUG_ZIPCODE) :
        print("    [County_Cities_Widget][get_county_cities_form]")

    form_parms      =   [county_cities_input_id,county_cities_input_idList,county_cities_input_labelList,county_cities_input_typeList,county_cities_input_placeholderList,county_cities_input_reqList]
    comboMethods    =   [update_callback,None]
    comboList       =   [None,None]
    file_methods    =   None
    button_methods  =   [get_attrs_callback,return_callback,help_callback]
    cfg_parms       =   None
    form_title      =   "Get County Cities\n"
    form_width      =   600

    selectDicts     =   []

    from dfcleanser.sw_utilities.DFCDataStores import get_Dict
    states_dict  =   get_Dict("US_States_and_Territories")
    
    if(DEBUG_ZIPCODE_DETAILS) :
        print("    [County_Cities_Widget][get_state_counties_form] states_dict : \n",states_dict)
    
    state_keys  =   list(states_dict.keys())
    state_keys.sort()

    if(DEBUG_ZIPCODE_DETAILS) :
        print("    [County_Cities_Widget][get_state_counties_form] state_keys : \n",state_keys)
    
    states_list     =   []
    
    for i in range(len(state_keys)) :
        states_list.append(str(state_keys[i]) + " : " + str(states_dict.get(state_keys[i])))

    if(DEBUG_ZIPCODE_DETAILS) :
        print("    [County_Cities_Widget][get_county_cities_form] states_list \n",states_list)


    state_sel    =   {"default":states_list[0],"list":states_list}
    selectDicts.append(state_sel)  
        
    from dfcleanser.Qt.utils.ZipCode.ZipCodeModel import (us_zipcodes)
    counties_list   =   us_zipcodes.get_state_counties_list("NY")
    counties_sel    =   {"default":counties_list[0],"list":counties_list}
    selectDicts.append(counties_sel)  
 
    form_parms.append(selectDicts)
    form_parms.append(comboMethods)            
    form_parms.append(file_methods)
    form_parms.append(button_methods)            
    form_parms.append(cfg_parms)            
    form_parms.append(form_title)
    form_parms.append(form_width)    

    from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
    county_cities_form    =   dfcleanser_input_form_Widget(form_parms)

    if(DEBUG_ZIPCODE) :
        print("    [County_Cities_Widget][get_county_cities_form] zipcode_cities_form built")

    return(county_cities_form)


class County_Cities_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_ZIPCODE) :
            print("  [County_Cities_Widget]")

        super().__init__()

        self.parent     =   dfparms[0]

        self.init_form()

        if(DEBUG_ZIPCODE) :
            print("  [County_Cities_Widget] end")

    def reload_data(self,parent) :

        self.parent     =   parent

    def init_form(self):  

        if(DEBUG_ZIPCODE) :
            print("  [County_Cities_Widget][init_form]")

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        #self.statecountiesLayout     =   QVBoxLayout()

        self.county_cities_data_form    =   get_county_cities_form(self.get_county_cities,self.return_from_get_county_cities,self.help_for_get_county_cities,self.select_state)

        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        zipcode_container = QWidget()
        zipcode_container.setFixedWidth(600)       

        self.statecountiesLayout     =   QVBoxLayout(zipcode_container)
        self.statecountiesLayout.addWidget(self.county_cities_data_form)
        self.statecountiesLayout.addStretch()

        self.final_widget   =   QWidget()
        self.final_widget.setLayout(self.statecountiesLayout)
        self.final_widget.setFixedWidth(600)

        self.final_layout   =   QVBoxLayout()
        self.final_layout.addWidget(self.final_widget)
        self.final_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.final_layout)

        if(DEBUG_ZIPCODE) :
            print("  [County_Cities_Widget][init_form] end")

    def select_state(self) :

        if(DEBUG_ZIPCODE) :
            print("[County_Cities_Widget][select_state]")

        state           =   self.county_cities_data_form.get_form_input_value_by_index(0)
        table_state     =   state[0:2]

        from dfcleanser.Qt.utils.ZipCode.ZipCodeModel import (us_zipcodes)
        counties_list   =   us_zipcodes.get_state_counties_list(table_state)

        self.county_cities_data_form.reset_form_combobox_by_index(1, counties_list)
 
    
    def get_county_cities(self) :
 
        state    =   self.county_cities_data_form.get_form_input_value_by_index(0)
        county   =   self.county_cities_data_form.get_form_input_value_by_index(1)

        if(DEBUG_ZIPCODE) :
            print("[County_Cities_Widget][get_county_citie]",state,county)

        self.parent.display_county_cities_data(state,county)

    def return_from_get_county_cities(self) :

        if(DEBUG_ZIPCODE) :
            print("[County_Cities_Widget][return_from_get_county_cities]")

        self.parent.init_zipcodes()

    def help_for_get_county_cities(self) :

        if(DEBUG_ZIPCODE) :
            print("[County_Cities_Widget][help_for_get_county_cities]")


class County_Cities_with_data_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_ZIPCODE) :
            print("[County_Cities_with_data_Widget]")

        super().__init__()

        self.parent     =   dfparms[0]
        self.state      =   dfparms[1]
        self.county     =   dfparms[2]
 
        self.init_form()

        if(DEBUG_ZIPCODE) :
            print("[County_Cities_with_data_Widget] end")

    def reload_data(self,parent,state,county) :

        self.parent     =   parent
        self.state      =   state
        self.county     =   county  

        if(DEBUG_ZIPCODE) :
            print("[County_Cities_with_data_Widget][reload_data] ",self.state)

        self.county_cities_data_table.reload_data(self.state,self.county)
        text    =   "\n" + self.county + " : " + self.state[5:] + " Cities\n"
        self.county_cities_note_label.setText(text)


    def init_form(self):  

        if(DEBUG_ZIPCODE) :
            print("[County_Cities_with_data_Widget][init_form]")

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.county_cities_data_form    =   get_county_cities_form(self.get_county_cities_data,self.return_from_get_county_cities_data,self.help_for_get_county_cities_data,self.change_state)

        tblparms   =   [self.state,self.county]       
        self.county_cities_data_table   =   County_Cities_Table(tblparms)

        from PyQt5.QtWidgets import QLabel
        self.county_cities_note_label   =   QLabel()
        text    =   "\n" + self.county + " : " + self.state[5:] + " Cities\n"
        self.county_cities_note_label.setText(text)
        self.county_cities_note_label.setAlignment(Qt.AlignLeft)
        self.county_cities_note_label.resize(480,50)
        self.county_cities_note_label.setStyleSheet("font-size: 14px; font-weight: bold; font-family: Arial; ")

        from PyQt5.QtWidgets import QVBoxLayout, QWidget
        self.countycitiesLayout     =   QVBoxLayout()
        self.countycitiesLayout.addWidget(self.county_cities_data_form)
        self.countycitiesLayout.addWidget(self.county_cities_note_label)
        self.countycitiesLayout.addWidget(self.county_cities_data_table)
        self.countycitiesLayout.addStretch()
        self.countycitiesLayout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.countycitiesLayout)


        """
        countycities_container = QWidget(self)
        countycities_container.setFixedWidth(600)       

        self.countycitiesLayout     =   QVBoxLayout(countycities_container)
        self.countycitiesLayout.addWidget(self.county_cities_data_form)
        self.countycitiesLayout.addStretch()
        self.countycitiesLayout.setAlignment(QtCore.Qt.AlignCenter)

        self.finaldata_widget   =   QWidget()
        self.finaldata_widget.setLayout(self.countycitiesLayout)
        self.finaldata_widget.setFixedWidth(600)

        self.finaldata_layout   =   QVBoxLayout()
        self.finaldata_layout.addWidget(self.finaldata_widget)
        self.finaldata_layout.addWidget(self.county_cities_note_label)
        self.finaldata_layout.addWidget(self.county_cities_data_table)
        self.finaldata_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.finaldata_layout)
        """

        if(DEBUG_ZIPCODE) :
            print("[County_Cities_with_data_Widget][init_form] end")


    def change_state(self) :

        state           =   self.county_cities_data_form.get_form_input_value_by_index(0)
        table_state     =   state[0:2]

        from dfcleanser.Qt.utils.ZipCode.ZipCodeModel import (us_zipcodes)
        counties_list   =   us_zipcodes.get_state_counties_list(table_state)

        self.county_cities_data_form.reset_form_combobox_by_index(1, counties_list)
 

    def get_county_cities_data(self) :
 
        state    =   self.county_cities_data_form.get_form_input_value_by_index(0)
        state    =   state[0:2]
        county   =   self.county_cities_data_form.get_form_input_value_by_index(1)
 
        if(DEBUG_ZIPCODE) :
            print("[County_Cities_with_data_Widget][get_county_cities_data]",state,county)

        self.parent.display_county_cities_data(state,county)

    def return_from_get_county_cities_data(self) :

        if(DEBUG_ZIPCODE) :
            print("[County_Cities_with_data_Widget][return_from_get_county_cities_data]")

        self.parent.init_zipcodes()

    def help_for_get_county_cities_data(self) :

        if(DEBUG_ZIPCODE) :
            print("[County_Cities_with_data_Widget][elp_for_get_county_cities_data]")




# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                   County Cities Objects end                   -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                       State Cities Objects                    -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class State_Cities_Model(QtCore.QAbstractTableModel):
    def __init__(self, dfsdata, colheaders):

        super(State_Cities_Model, self).__init__()
        self._data          =   dfsdata
        self.column_names   =   colheaders

    def reload_data(self,dfsdata,headers) :

        if(DEBUG_ZIPCODE) :
            print("  [SState_Cities_Model][reload_data] state : ",headers)

        self._data          =   dfsdata
        self.column_names   =   headers

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
            else :
                return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:

            if( (len(self._data[row][column]) == 1) or (len(self._data[row][column]) == 0)):
                if((len(self._data[row][0]) == 1)) : 
                    bgcolor = QtGui.QBrush(QColor(240, 234, 193))
                else :
                    bgcolor = QtGui.QBrush(QtCore.Qt.white)
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


class State_Cities_Table(QtWidgets.QTableView):

    def __init__(self,  tblparms, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.state          =   tblparms[0]

        if(DEBUG_ZIPCODE) :
            print("\n  [State_Cities_Table] : init",self.state)

        self.init_tableview()

        if(DEBUG_ZIPCODE) :
            print("  [State_Cities_Table] : end")

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self, state):

        if(DEBUG_ZIPCODE) :
            print("  [State_Cities_Table][reload_data] state : ",state)

        self.state          =   state
 
        tbldata    =   self.load_state_cities_data()

        if(DEBUG_ZIPCODE) :
            print("  [State_Cities_Table][reload_data] self.column_headers) : ",self.column_headers)

        self.model.reload_data(tbldata,self.column_headers)

        num_rows   =   len(tbldata)
        
        if(num_rows < 20) :
            new_height  =   40 + (num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   40 + (20 * DEFAULT_ROW_HEIGHT)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)


    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(DEBUG_ZIPCODE) :
            print("  [State_Cities_Table][init_tableview]")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        statecities_data     =   self.load_state_cities_data()
        
        if(DEBUG_ZIPCODE) :
           print("  [State_Cities_Table][init_tableview] : headers",self.column_headers)

        if(self.model is None) :
            self.model = State_Cities_Model(statecities_data,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_ZIPCODE) :
           print("  [State_Cities_Table][init_tableview] : model loaded")

        self.num_rows   =   len(statecities_data)
        
        if(self.num_rows < 20) :
            new_height  =   40 + ((self.num_rows) * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   40 + ((20) * DEFAULT_ROW_HEIGHT)

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
        header.setDefaultAlignment(Qt.AlignLeft)
        header.setStyleSheet("font-size: 14px; font-weight: bold; font-family: Arial; ")

 
        header.setFixedHeight(26)

        # set the row heights
        nrows = len(statecities_data)
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
    def load_state_cities_data(self):

        if(DEBUG_ZIPCODE) :
            print("  [State_Cities_Table][load_state_cities_data]",self.state)

        table_state     =   self.state[0:2] 
        display_state   =   self.state[5:] 

        from dfcleanser.Qt.utils.ZipCode.ZipCodeModel import (us_zipcodes, ANY_LOCATION_TYPE)
        cities_list     =   us_zipcodes.get_cities_for_state(table_state, ANY_LOCATION_TYPE)

        if(DEBUG_ZIPCODE_DETAILS) :
            print("  [State_Cities_Table][load_state_cities_data][cities_list]",cities_list)

        data                =   []
        data_row            =   []

        current_letter      =   ""

        if( (not (cities_list is None)) and (len(cities_list) > 0)) :

            for i in range(len(cities_list)) :

                
                first_letter    =   cities_list[i][0]
                if(not (first_letter == current_letter)) :

                    current_letter  =   first_letter

                    if(len(data_row) > 0) :
                        num_to_fill     =   9 - len(data_row)

                        for j in range(num_to_fill) :
                            data_row.append("")

                        data.append(data_row)

                    data_row    =   [current_letter,"","","","","","","",""]
                    data.append(data_row)
                    data_row    =   []
                    data_row.append(cities_list[i])

                else :

                    if( (len(data_row) % 9) == 0) :
                
                        data.append(data_row)
                        data_row    =   []
                        data_row.append(str(cities_list[i]))

                    else :
                        data_row.append(str(cities_list[i]))

            if(len(data_row) > 0) :
                num_to_fill     =   9 - len(data_row)

                for j in range(num_to_fill) :
                    data_row.append("")

                data.append(data_row)

        else :

            data.append(["","","","","","","","",""])

        if(DEBUG_ZIPCODE_DETAILS) :
            print("  [State_Cities_Table] : data")
            for j in range(len(data)) :
                print("  [",j,"] : ",data[j])

        self.column_headers     =   [display_state,"Cities","","","","","","",""]
        self.column_widths      =   [108,108,108,108,108,108,108,108,108]

        if(DEBUG_ZIPCODE) :
            print("  [State_Cities_Table][load_state_cities_data]",self.column_headers)

        return(data)

def get_state_cities_form(get_attrs_callback,return_callback,help_callback) :

    if(DEBUG_ZIPCODE) :
        print("  [State_Cities_Widget][get_state_cities_form]")

    form_parms      =   [state_cities_input_id,state_cities_input_idList,state_cities_input_labelList,state_cities_input_typeList,state_cities_input_placeholderList,state_cities_input_reqList]
    comboMethods    =   [None]
    comboList       =   [None]
    file_methods    =   None
    button_methods  =   [get_attrs_callback,return_callback,help_callback]
    cfg_parms       =   None
    form_title      =   "Get State Cities\n"
    form_width      =   600

    selectDicts     =   []

    from dfcleanser.sw_utilities.DFCDataStores import get_Dict
    states_dict  =   get_Dict("US_States_and_Territories")
    
    if(DEBUG_ZIPCODE_DETAILS) :
        print("  [State_Cities_Widget][get_state_cities_form] states_dict : \n",states_dict)
    
    state_keys  =   list(states_dict.keys())
    state_keys.sort()

    if(DEBUG_ZIPCODE_DETAILS) :
        print("  [State_Cities_Widget][get_state_cities_form] state_keys : \n",state_keys)
    
    states_list     =   []
    
    for i in range(len(state_keys)) :
        states_list.append(str(state_keys[i]) + " : " + str(states_dict.get(state_keys[i])))

    if(DEBUG_ZIPCODE_DETAILS) :
        print("  [State_Cities_Widget][get_state_cities_form] states_list \n",states_list)


    state_sel    =   {"default":states_list[0],"list":states_list}
    selectDicts.append(state_sel)  
        
 
    form_parms.append(selectDicts)
    form_parms.append(comboMethods)            
    form_parms.append(file_methods)
    form_parms.append(button_methods)            
    form_parms.append(cfg_parms)            
    form_parms.append(form_title)
    form_parms.append(form_width)    

    from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
    state_cities_form    =   dfcleanser_input_form_Widget(form_parms)

    if(DEBUG_ZIPCODE) :
        print("  [State_Cities_Widget][get_state_cities_form] state_cities_form built")

    return(state_cities_form)


class State_Cities_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_ZIPCODE) :
            print("  [State_Cities_Widget]")

        super().__init__()

        self.parent     =   dfparms[0]

        self.init_form()

        if(DEBUG_ZIPCODE) :
            print("  [State_Cities_Widget] end")

    def reload_data(self,parent) :

        self.parent     =   parent

    def init_form(self):  

        if(DEBUG_ZIPCODE) :
            print("  [State_Cities_Widget][init_form]")

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        #self.statecountiesLayout     =   QVBoxLayout()

        self.state_cities_data_form    =   get_state_cities_form(self.get_state_cities,self.return_from_get_state_cities,self.help_for_get_state_cities)

        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        zipcode_container = QWidget()
        zipcode_container.setFixedWidth(600)       

        self.statecountiesLayout     =   QVBoxLayout(zipcode_container)
        self.statecountiesLayout.addWidget(self.state_cities_data_form)
        self.statecountiesLayout.addStretch()

        self.final_widget   =   QWidget()
        self.final_widget.setLayout(self.statecountiesLayout)
        self.final_widget.setFixedWidth(600)

        self.final_layout   =   QVBoxLayout()
        self.final_layout.addWidget(self.final_widget)
        self.final_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.final_layout)

        if(DEBUG_ZIPCODE) :
            print("  [State_Cities_Widget][init_form] end")

    
    def get_state_cities(self) :
 
        state    =   self.state_cities_data_form.get_form_input_value_by_index(0)
 
        if(DEBUG_ZIPCODE) :
            print("[State_Cities_Widget][get_state_citie]",state)

        self.parent.display_state_cities_data(state)

    def return_from_get_state_cities(self) :

        if(DEBUG_ZIPCODE) :
            print("[State_Cities_Widget][return_from_get_state_cities]")

        self.parent.init_zipcodes()

    def help_for_get_state_cities(self) :

        if(DEBUG_ZIPCODE) :
            print("[State_Cities_Widget][help_for_get_state_cities]")


class State_Cities_with_data_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(DEBUG_ZIPCODE) :
            print("[State_Cities_with_data_Widget]")

        super().__init__()

        self.parent     =   dfparms[0]
        self.state      =   dfparms[1]
 
        self.init_form()

        if(DEBUG_ZIPCODE) :
            print("[State_Cities_with_data_Widget] end")

    def reload_data(self,parent,state) :

        self.parent     =   parent
        self.state      =   state

        if(DEBUG_ZIPCODE) :
            print("[State_Cities_with_data_Widget][reload_data] ",self.state)

        self.state_cities_data_table.reload_data(self.state)

    def init_form(self):  

        if(DEBUG_ZIPCODE) :
            print("[State_Cities_with_data_Widget][init_form]")

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.state_cities_data_form    =   get_state_cities_form(self.get_state_cities_data,self.return_from_get_state_cities_data,self.help_for_get_state_cities_data)

        tblparms   =   [self.state]       
        self.state_cities_data_table   =   State_Cities_Table(tblparms)

        if(DEBUG_ZIPCODE) :
            print("  [State_Cities_wth_date_Widget][init_form] state_cities_table built")


        from PyQt5.QtWidgets import QLabel
        note_label   =   QLabel()
        note_label.setText("\nState Cities\n")
        note_label.setAlignment(Qt.AlignLeft)
        note_label.resize(480,50)
        note_label.setStyleSheet("font-size: 14px; font-weight: bold; font-family: Arial; ")

        from PyQt5.QtWidgets import QVBoxLayout, QWidget
        self.statecitiesLayout     =   QVBoxLayout()
        self.statecitiesLayout.addWidget(self.state_cities_data_form)
        self.statecitiesLayout.addWidget(note_label)
        self.statecitiesLayout.addWidget(self.state_cities_data_table)
        self.statecitiesLayout.addStretch()
        self.statecitiesLayout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.statecitiesLayout)

        """
        countycities_container = QWidget(self)
        countycities_container.setFixedWidth(600)       

        self.countycitiesLayout     =   QVBoxLayout(countycities_container)
        self.countycitiesLayout.addWidget(self.state_cities_data_form)
        self.countycitiesLayout.addStretch()
        self.countycitiesLayout.setAlignment(QtCore.Qt.AlignCenter)

        self.finaldata_widget   =   QWidget()
        self.finaldata_widget.setLayout(self.countycitiesLayout)
        self.finaldata_widget.setFixedWidth(600)

        self.finaldata_layout   =   QVBoxLayout()
        self.finaldata_layout.addWidget(self.finaldata_widget)
        #self.finaldata_layout.addWidget(note_label)
        self.finaldata_layout.addWidget(self.state_cities_data_table)
        self.finaldata_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.finaldata_layout)
        """
        
        if(DEBUG_ZIPCODE) :
            print("[tate_Cities_with_data_Widget][init_form] end")


    def get_state_cities_data(self) :
 
        state    =   self.state_cities_data_form.get_form_input_value_by_index(0)
        #state    =   state[0:2]
 
        if(DEBUG_ZIPCODE) :
            print("\n[State_Cities_with_data_Widget][get_state_cities_data]",state)

        self.parent.display_state_cities_data(state)

    def return_from_get_state_cities_data(self) :

        if(DEBUG_ZIPCODE) :
            print("[State_Cities_with_data_Widget][return_from_get_state_cities_data]")

        self.parent.init_zipcodes()

    def help_for_get_state_cities_data(self) :

        if(DEBUG_ZIPCODE) :
            print("[State_Cities_with_data_Widget][help_for_get_state_cities_data]")




# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                   County Cities Objects end                   -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#










# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                ZipCode attributes Objects end                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#













