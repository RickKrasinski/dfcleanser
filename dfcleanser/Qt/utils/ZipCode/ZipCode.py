"""
# zipcode
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:29:22 2017

@author: Rick
"""

import sys
this = sys.modules[__name__]


import inspect
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QStackedWidget

from PyQt5.QtCore import Qt
from PyQt5 import uic


import dfcleanser.common.cfg as cfg 

DEBUG_ZIPCODE                   =   True


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -           general Data Inspection Housekeeping                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

import logging
logger = logging.getLogger(__name__)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

# Set the exception hook to our wrapping function
sys.excepthook = except_hook

# Enables PyQt event loop in IPython
from dfcleanser.sw_utilities.dfc_qt_model import fix_ipython
fix_ipython()


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                 Data Import subfunctions                      -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#



DISPLAY_ZIPCODES                        =   "ZipCodes"

DISPLAY_ZIPCODE_ATTRIBUTES              =   "ZipCode attributes"
DISPLAY_ZIPCODE_ATTRIBUTES_DATA         =   "ZipCode attributes data"

DISPLAY_ZIPCODE_BY_LOCATION             =   "ZipCode by location"
DISPLAY_CITY_ZIPCODES                   =   "City Zipcodes"
DISPLAY_CITY_ZIPCODES_DATA              =   "City Zipcodes data"

DISPLAY_STATE_COUNTIES                  =   "State Counties"
DISPLAY_STATE_COUNTIES_DATA             =   "State Counties data"

DISPLAY_COUNTY_CITIES                   =   "County Cities"
DISPLAY_COUNTY_CITIES_DATA              =   "County Cities data"

DISPLAY_STATE_CITIES                    =   "State Cities"
DISPLAY_STATE_CITIES_DATA               =   "State Cities data"




"""

DISPLAY_DFC_HISTORIES                   =   "System display dfs histories"
DISPLAY_ADD_USER_DF                     =   "System display dfs add user df"

DISPLAY_INFO                            =   "System display info"
DISPLAY_ABOUT                           =   "System display about"
DISPLAY_EULA                            =   "System display eula"



EXPORT_EXCEL_FILE_TYPE_HISTORIES        =   "DataExport excel filetypes Exported"
EXPORT_JSON_FILE_TYPE_HISTORIES         =   "DataExport json filetypes Exported"
EXPORT_HTML_FILE_TYPE_HISTORIES         =   "DataExport html filetypes Exported"
EXPORT_SQLTABLE_FILE_TYPE_HISTORIES     =   "DataExport sqltable filetypes Exported"
EXPORT_CUSTOM_FILE_TYPE_HISTORIES       =   "DataExport custom filetypes Exported"
"""


DEFAULT_ROW_HEIGHT                  =   20


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                       System main GUI                         -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -    Subclass of QMainWindow to disp[lay the columns uniques    -#
# -----------------------------------------------------------------#
class ZipCodeGui(QtWidgets.QMainWindow):

    #def __init__(self):
    def __init__(self, **kwargs):  

        # Enables PyQt event loop in IPython
        fix_ipython()  

        # create the app for uniques
        from PyQt5.QtCore import QCoreApplication

        self.app = QCoreApplication.instance()
        if(self.app is None) :
            self.app = QtWidgets.QApplication(sys.argv) 

        # release resources on close
        self.app.setQuitOnLastWindowClosed(True)  

        super().__init__()

        self.mainLayout         =   None
        self.selectdfsLayout    =   None

        self.dftitle            =   None
        self.df                 =   None

        self.form               =   None
        self.stackedLayout      =   None


        self.ZipCodeWidgets_stack_dict     =   {}

        # enable custom window hint
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)

        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)

        # general housekeeping
        self.caller_stack   = inspect.currentframe().f_back
        self.stacked_widget = QStackedWidget(None)

        self.init_gui()

        self.form.ZipCodeLayout.addLayout(self.stackedLayout)
        self.form.ZipCodeLayout.addStretch()


    def update(self):   
        self.update()

    
    # -----------------------------------------------------------------#
    # -                     Initialize the gui                        -#
    # -----------------------------------------------------------------#
        
    def init_gui(self):

        if(DEBUG_ZIPCODE) :
            print("initgui")
        
        # set up the ui form from a qtdesigner ui
        cfgdir  = cfg.DataframeCleanserCfgData.get_dfc_qt_dir_name()
        ui_name = cfgdir +"\\utils\ZipCode\ZipCodeUI.ui"
        Form, Window = uic.loadUiType(ui_name)
        self.form = Form()
        self.form.setupUi(self)

        from PyQt5.QtWidgets import QStackedLayout
        self.stackedLayout = QStackedLayout()

        # -----------------------------------------------------#
        #     common window attribute settings     #
        # -----------------------------------------------------#
        
        # set common window attributes
        self.setWindowTitle("dfcleanser - Zip Codes")
        
        # Center window on screen
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2),
                         int((screen.height() - size.height()) / 2), )
        
        # don't Accept drops
        self.setAcceptDrops(False)

        # don't allopw code viewing
        self.code_history_viewer = None 

        # -----------------------------------------------------#
        #       common app attribute settings         #
        # -----------------------------------------------------#
        # Set the app icon
        dfcdir      =   cfg.DataframeCleanserCfgData.get_dfc_cfg_dir_name()  
        icon_name   =   dfcdir +"\dfcicon.png"
        self.app.setWindowIcon(QtGui.QIcon(icon_name))

        # Hide the question mark on dialogs
        self.app.setAttribute(Qt.AA_DisableWindowContextHelpButton) 
        
        # set overall app style
        self.app.setStyle('Fusion')      

        # -----------------------------------------------------#
        #            common window widgets             #
        # -----------------------------------------------------#

        # Status bar
        self.setStatusBar(QtWidgets.QStatusBar())
        self.statusBar().setStyleSheet("background-color: #ccffff; font-size: 12px; font-weight: normal; font-family: Arial; margin-left: 0px;")
        
        # init the gui form
        self.init_zipcode_form()

        if(DEBUG_ZIPCODE) :
            print("initgui")
           

    # -----------------------------------------------------------------#
    # -                 Initialize chapter buttons                    -#
    # -----------------------------------------------------------------#
    def init_zipcode_buttons(self):

        if(DEBUG_ZIPCODE) :
            print("[SystemGui][init_zipcode_buttons]  ")

        from dfcleanser.sw_utilities.dfc_qt_model import init_dfc_buttons, set_dfc_buttons_style
        buttons     =   [self.form.ZipCodeAttributesbutton, self.form.ZipCodeListsbutton, self.form.ZipCodeHelpbutton] 
        callbacks   =   [self.get_zipcode_attributes, self.get_zipcode_by_location, self.get_help_zipcode]
    
        # init buttons for usage
        ZipCode_Button_Style    =   "background-color:#0c4ca7; color:white; font : Arial; font-weight : bold; font-size : 13px;"
        init_dfc_buttons(buttons,ZipCode_Button_Style)

        # set button styles
        #set_dfc_buttons_style(buttons,Import_Button_Style)
        
        # adding action to a button
        for i in range(len(buttons)) :
            buttons[i].clicked.connect(callbacks[i])


    # -----------------------------------------------------------------#
    # -            Initialize the chapter splah image                 -#
    # -----------------------------------------------------------------#
    def init_zipcode_splash_screen(self):

        if(DEBUG_ZIPCODE) :
            print("[SystemGui][init_data_inspect_splash_screen]  ")

        from dfcleanser.sw_utilities.dfc_qt_model import build_chapter_splash_screen
        from dfcleanser.common.cfg import SWZipcodeUtility_ID
        build_chapter_splash_screen(SWZipcodeUtility_ID, self.form.ZipCodesplash)

        if(DEBUG_ZIPCODE) :
            print("[end init_zipcode_splash_screen]  ")

    # -----------------------------------------------------------------#
    # -             Initialize the dfs select form                    -#
    # -----------------------------------------------------------------#
    def init_zipcodes(self):

        if(DEBUG_ZIPCODE) :
            print("[init_zipcodes]  ")

        from PyQt5.QtWidgets import QLabel
        self.blank_label   =   QLabel()
        self.blank_label.setText("")
        self.blank_label.setAlignment(Qt.AlignLeft)
        self.blank_label.resize(600,50)
        self.blank_label.setStyleSheet("font-size: 12px; font-weight: bold; font-family: Arial; ")

        from PyQt5.QtWidgets import QVBoxLayout
        self.zipcodeLayout     =   QVBoxLayout()
        self.zipcodeLayout.addWidget(self.blank_label)
        self.zipcodeLayout.addStretch()
        self.zipcodeLayout.setAlignment(QtCore.Qt.AlignCenter) 

        from PyQt5.QtWidgets import QWidget  
        self.zipcodemain    =   QWidget()
        self.zipcodemain.setLayout(self.zipcodeLayout)

        zipcode_index  =   self.ZipCodeWidgets_stack_dict.get(DISPLAY_ZIPCODES)

        if(zipcode_index is None) :
            current_index   =  len(self.ZipCodeWidgets_stack_dict)
            self.ZipCodeWidgets_stack_dict.update({DISPLAY_ZIPCODES: current_index})
            self.stackedLayout.addWidget(self.zipcodemain)
        else :
            current_index   =   zipcode_index

        self.stackedLayout.setCurrentIndex(current_index)

        self.resize(1070,250)

    # -----------------------------------------------------------------#
    # -                 Initialize the gui form                       -#
    # -----------------------------------------------------------------#
    def init_zipcode_form(self):

        if(DEBUG_ZIPCODE) :
            print("[ZipCodeGui][init_zipcode_form]  ")

        self.init_zipcode_buttons()
        self.init_zipcode_splash_screen()
        self.init_zipcodes()

        self.resize(1070,250)

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -               Main Gui Data Import Methods                    -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -                      zipcode attributes                       -#
    # -----------------------------------------------------------------#
    def get_zipcode_attributes(self) :

        self.form.ZipCodeAttributesbutton.toggle()

        if(DEBUG_ZIPCODE) :
            print("[ZipCodeGui][get_zipcode_attributes]")

        self.display_zipcode_attributes()

    # -----------------------------------------------------------------#
    # -                      zipcode by location                      -#
    # -----------------------------------------------------------------#
    def get_zipcode_by_location(self) :

        self.form.ZipCodeListsbutton.toggle()

        if(DEBUG_ZIPCODE) :
            print("[ZipCodeGui][get_zipcode_lists]")

        self.display_zipcode_by_locations()
 
    # -----------------------------------------------------------------#
    # -                      Zip code help                          -#
    # -----------------------------------------------------------------#
    def get_help_zipcode(self) :

        self.form.ZipCodeHelpbutton.toggle()

        if(DEBUG_ZIPCODE) :
            print("[ZipCodeGui][get_help_zipcode]")

        from dfcleanser.common.common_utils import display_url
        display_url("https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-geocoding.html")


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                  display zipcode attributes                   -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_zipcode_attributes(self):

        if(DEBUG_ZIPCODE) :
            print("\n[ZipCodeGui][display_zipcode_attribute]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        zipcode_attrs_index  =   self.ZipCodeWidgets_stack_dict.get(DISPLAY_ZIPCODE_ATTRIBUTES )
        
        if(zipcode_attrs_index is None) :

            try :

                from dfcleanser.Qt.utils.ZipCode.ZipCodeWidgets import ZipCode_attributes_Widget
                self.ZipCode_attrs   =   ZipCode_attributes_Widget([self])

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_zipcode_attributes] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.ZipCodeWidgets_stack_dict)
                self.ZipCodeWidgets_stack_dict.update({DISPLAY_ZIPCODE_ATTRIBUTES  : current_index})
                self.stackedLayout.addWidget(self.ZipCode_attrs)

        else :

            self.ZipCode_attrs.reload_data(self)
            current_index   =   zipcode_attrs_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_ZIPCODE) :
            print("[ZipCodeGui][display_zipcode_attribute] end : stack \n  ",self.ZipCodeWidgets_stack_dict)

        self.resize(1070,450)


    def display_zipcode_attributes_data(self,zipcode):

        if(DEBUG_ZIPCODE) :
            print("\n[ZipCodeGui][display_zipcode_attributes_data]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        zipcode_attrs_index  =   self.ZipCodeWidgets_stack_dict.get(DISPLAY_ZIPCODE_ATTRIBUTES_DATA)

        if(DEBUG_ZIPCODE) :
            print("[ZipCodeGui][display_zipcode_attributes_data]  index : ",zipcode_attrs_index)

        
        if(zipcode_attrs_index is None) :

            try :

                from dfcleanser.Qt.utils.ZipCode.ZipCodeWidgets import ZipCode_attributes_with_data_Widget
                parms   =   [self,zipcode]
                self.ZipCode_attrs_with_data   =   ZipCode_attributes_with_data_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_zipcode_attributes_data] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.ZipCodeWidgets_stack_dict)
                self.ZipCodeWidgets_stack_dict.update({DISPLAY_ZIPCODE_ATTRIBUTES_DATA  : current_index})
                self.stackedLayout.addWidget(self.ZipCode_attrs_with_data)

        else :

            if(DEBUG_ZIPCODE) :
                print("[ZipCodeGui][display_zipcode_attributes_data] reload_data:  ",zipcode_attrs_index,zipcode)

            self.ZipCode_attrs_with_data.reload_data(self,zipcode)
            current_index   =   zipcode_attrs_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_ZIPCODE) :
            print("[ZipCodeGui][display_zipcode_attributes_data] end : stack \n  ",self.ZipCodeWidgets_stack_dict)

        self.resize(1070,750)


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -               display zipcode attributes end                  -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                  display zipcodes by location                 -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_zipcode_by_locations(self):

        if(DEBUG_ZIPCODE) :
            print("\n[ZipCodeGui][display_zipcode_by_locations]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        zipcode_location_index  =   self.ZipCodeWidgets_stack_dict.get(DISPLAY_ZIPCODE_BY_LOCATION)
        
        if(zipcode_location_index is None) :

            try :

                from dfcleanser.Qt.utils.ZipCode.ZipCodeWidgets import ZipCode_locations_Widget
                self.ZipCode_location   =   ZipCode_locations_Widget([self])

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_zipcode_by_locations] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.ZipCodeWidgets_stack_dict)
                self.ZipCodeWidgets_stack_dict.update({DISPLAY_ZIPCODE_BY_LOCATION  : current_index})
                self.stackedLayout.addWidget(self.ZipCode_location)

        else :

            self.ZipCode_location.reload_data(self)
            current_index   =   zipcode_location_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_ZIPCODE) :
            print("[ZipCodeGui][display_zipcode_by_locations] end : stack \n  ",self.ZipCodeWidgets_stack_dict)

        self.resize(1070,350)


    # -----------------------------------------------------------------#
    # -                    display zipcodes by city                   -#
    # -----------------------------------------------------------------#

    def display_city_zipcodes(self):

        if(DEBUG_ZIPCODE) :
            print("\n[ZipCodeGui][display_city_zipcodes]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        city_zipcodes_index  =   self.ZipCodeWidgets_stack_dict.get(DISPLAY_CITY_ZIPCODES )
        
        if(city_zipcodes_index is None) :

            try :

                from dfcleanser.Qt.utils.ZipCode.ZipCodeWidgets import ZipCode_Cities_Widget
                self.city_zipcodes   =   ZipCode_Cities_Widget([self])

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_city_zipcodes] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.ZipCodeWidgets_stack_dict)
                self.ZipCodeWidgets_stack_dict.update({DISPLAY_CITY_ZIPCODES  : current_index})
                self.stackedLayout.addWidget(self.city_zipcodes)

        else :

            self.city_zipcodes.reload_data(self)
            current_index   =   city_zipcodes_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_ZIPCODE) :
            print("[ZipCodeGui][display_city_zipcodes] end : stack \n  ",self.ZipCodeWidgets_stack_dict)

        self.resize(1070,600)


    def display_city_zipcodes_data(self,city,state):

        if(DEBUG_ZIPCODE) :
            print("\n[ZipCodeGui][display_city_zipcodes_data]  ",city,state)

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        city_zips_index  =   self.ZipCodeWidgets_stack_dict.get(DISPLAY_CITY_ZIPCODES_DATA)

        if(DEBUG_ZIPCODE) :
            print("[ZipCodeGui][display_city_zipcodes_data]  index : ",city_zips_index)

        
        if(city_zips_index is None) :

            try :

                from dfcleanser.Qt.utils.ZipCode.ZipCodeWidgets import ZipCode_Cities_with_data_Widget
                parms   =   [self,city,state]
                self.city_zips_data   =   ZipCode_Cities_with_data_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_city_zipcodes_data] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.ZipCodeWidgets_stack_dict)
                self.ZipCodeWidgets_stack_dict.update({DISPLAY_CITY_ZIPCODES_DATA  : current_index})
                self.stackedLayout.addWidget(self.city_zips_data)

        else :

            if(DEBUG_ZIPCODE) :
                print("[ZipCodeGui][display_city_zipcodes_data] reload_data:  ",city,state)

            self.city_zips_data.reload_data(self,city,state)
            current_index   =   city_zips_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_ZIPCODE) :
            print("[ZipCodeGui][display_city_zipcodes_data] end : stack \n  ",self.ZipCodeWidgets_stack_dict)

        self.resize(1070,850)

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                display zipcodes by location end               -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                   display counties by state                   -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_state_counties(self):

        if(DEBUG_ZIPCODE) :
            print("\n[ZipCodeGui][display_state_counties]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        state_counties_index  =   self.ZipCodeWidgets_stack_dict.get(DISPLAY_STATE_COUNTIES)
        
        if(state_counties_index is None) :

            try :

                from dfcleanser.Qt.utils.ZipCode.ZipCodeWidgets import State_Counties_Widget
                self.state_counties   =   State_Counties_Widget([self])

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_state_counties] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.ZipCodeWidgets_stack_dict)
                self.ZipCodeWidgets_stack_dict.update({DISPLAY_STATE_COUNTIES  : current_index})
                self.stackedLayout.addWidget(self.state_counties)

        else :

            self.state_counties.reload_data(self)
            current_index   =   state_counties_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_ZIPCODE) :
            print("[ZipCodeGui][display_state_counties] end : stack \n  ",self.ZipCodeWidgets_stack_dict)

        self.resize(1070,450)


    def display_state_counties_data(self,state):

        if(DEBUG_ZIPCODE) :
            print("\n[ZipCodeGui][display_state_counties_data]  ",state)

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        state_counties_index  =   self.ZipCodeWidgets_stack_dict.get(DISPLAY_STATE_COUNTIES_DATA)

        if(DEBUG_ZIPCODE) :
            print("[ZipCodeGui][display_state_counties_data]  index : ",state_counties_index)

        
        if(state_counties_index is None) :

            try :

                from dfcleanser.Qt.utils.ZipCode.ZipCodeWidgets import State_Counties_with_data_Widget
                parms   =   [self,state]
                self.state_counties_data   =   State_Counties_with_data_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_state_counties_data] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.ZipCodeWidgets_stack_dict)
                self.ZipCodeWidgets_stack_dict.update({DISPLAY_STATE_COUNTIES_DATA : current_index})
                self.stackedLayout.addWidget(self.state_counties_data)

        else :

            if(DEBUG_ZIPCODE) :
                print("[ZipCodeGui][display_city_zipcodes_data] reload_data:  ",state)

            self.state_counties_data.reload_data(self,state)
            current_index   =   state_counties_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_ZIPCODE) :
            print("[ZipCodeGui][display_city_zipcodes_data] end : stack \n  ",self.ZipCodeWidgets_stack_dict)

        self.resize(1070,800)

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                  display counties by state end                -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#



    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                   display cities by county                    -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_county_cities(self):

        if(DEBUG_ZIPCODE) :
            print("\n[ZipCodeGui][display_county_cities]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        county_cities_index  =   self.ZipCodeWidgets_stack_dict.get(DISPLAY_COUNTY_CITIES)
        
        if(county_cities_index is None) :

            try :

                from dfcleanser.Qt.utils.ZipCode.ZipCodeWidgets import County_Cities_Widget
                self.county_cities   =   County_Cities_Widget([self])

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_county_cities] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.ZipCodeWidgets_stack_dict)
                self.ZipCodeWidgets_stack_dict.update({DISPLAY_COUNTY_CITIES  : current_index})
                self.stackedLayout.addWidget(self.county_cities)

        else :

            self.county_cities.reload_data(self)
            current_index   =   county_cities_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_ZIPCODE) :
            print("[ZipCodeGui][display_county_cities] end : stack \n  ",self.ZipCodeWidgets_stack_dict)

        self.resize(1070,500)


    def display_county_cities_data(self,state,county):

        if(DEBUG_ZIPCODE) :
            print("\n[ZipCodeGui][display_county_cities_data]  ",state,county)

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        county_cities_data_index  =   self.ZipCodeWidgets_stack_dict.get(DISPLAY_COUNTY_CITIES_DATA)

        if(DEBUG_ZIPCODE) :
            print("[ZipCodeGui][display_state_counties_data]  index : ",county_cities_data_index)

        
        if(county_cities_data_index is None) :

            try :

                from dfcleanser.Qt.utils.ZipCode.ZipCodeWidgets import County_Cities_with_data_Widget
                parms   =   [self,state,county]
                self.county_cities_data   =   County_Cities_with_data_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_county_cities_data] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.ZipCodeWidgets_stack_dict)
                self.ZipCodeWidgets_stack_dict.update({DISPLAY_COUNTY_CITIES_DATA : current_index})
                self.stackedLayout.addWidget(self.county_cities_data)

        else :

            if(DEBUG_ZIPCODE) :
                print("[ZipCodeGui][display_county_cities_data] reload_data:  ",state,county)

            self.county_cities_data.reload_data(self,state,county)
            current_index   =   county_cities_data_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_ZIPCODE) :
            print("[ZipCodeGui][display_county_cities_data] end : stack \n  ",self.ZipCodeWidgets_stack_dict)

        self.resize(1070,800)

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                  display cities by county end                 -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                   display cities by state                    -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_state_cities(self):

        if(DEBUG_ZIPCODE) :
            print("\n[ZipCodeGui][display_state_cities]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        state_cities_index  =   self.ZipCodeWidgets_stack_dict.get(DISPLAY_STATE_CITIES)
        
        if(state_cities_index is None) :

            try :

                from dfcleanser.Qt.utils.ZipCode.ZipCodeWidgets import State_Cities_Widget
                self.state_cities   =   State_Cities_Widget([self])

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_state_cities] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.ZipCodeWidgets_stack_dict)
                self.ZipCodeWidgets_stack_dict.update({DISPLAY_STATE_CITIES  : current_index})
                self.stackedLayout.addWidget(self.state_cities)

        else :

            self.state_cities.reload_data(self)
            current_index   =   state_cities_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_ZIPCODE) :
            print("[ZipCodeGui][display_state_cities] end : stack \n  ",self.ZipCodeWidgets_stack_dict)

        self.resize(1070,500)


    def display_state_cities_data(self,state):

        if(DEBUG_ZIPCODE) :
            print("\n[ZipCodeGui][display_state_cities_data]  ",state)

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        state_cities_data_index  =   self.ZipCodeWidgets_stack_dict.get(DISPLAY_STATE_CITIES_DATA)

        if(DEBUG_ZIPCODE) :
            print("[ZipCodeGui][display_state_cities_data]  index : ",state_cities_data_index)

        
        if(state_cities_data_index is None) :

            try :

                from dfcleanser.Qt.utils.ZipCode.ZipCodeWidgets import State_Cities_with_data_Widget
                parms   =   [self,state]
                self.state_cities_data   =   State_Cities_with_data_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_state_cities_data] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.ZipCodeWidgets_stack_dict)
                self.ZipCodeWidgets_stack_dict.update({DISPLAY_STATE_CITIES_DATA : current_index})
                self.stackedLayout.addWidget(self.state_cities_data)

        else :

            if(DEBUG_ZIPCODE) :
                print("[ZipCodeGui][display_state_cities_data] reload_data:  ",state)

            self.state_cities_data.reload_data(self,state)
            current_index   =   state_cities_data_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_ZIPCODE) :
            print("[ZipCodeGui][display_state_cities_data] end : stack \n  ",self.ZipCodeWidgets_stack_dict)

        self.resize(1070,1000)

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                  display cities by county end                 -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#




# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                Global access to System Chapter                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def clearZipCode()  :

    from dfcleanser.common.common_utils import clear_screen
    
    clear_screen()

    from dfcleanser.common.cfg import dfc_qt_chapters, ZIPCODE_QT_CHAPTER_ID
    num_instances   =   dfc_qt_chapters.get_qt_chapters_count(ZIPCODE_QT_CHAPTER_ID)

    if(num_instances > 0) :
        instances       =   dfc_qt_chapters.get_qt_chapters(ZIPCODE_QT_CHAPTER_ID)
        for i in range(len(instances)) :
            instances[i].get_main_window().init_zipcode_form()

    clear_screen()
 

def closeZipCodeInstances()  :
    
    from dfcleanser.common.cfg import dfc_qt_chapters, ZIPCODE_QT_CHAPTER_ID
    num_instances   =   dfc_qt_chapters.get_qt_chapters_count(ZIPCODE_QT_CHAPTER_ID)

    if(num_instances > 0) :
        instances       =   dfc_qt_chapters.get_qt_chapters(ZIPCODE_QT_CHAPTER_ID)
        for i in range(len(instances)) :
            instances[i].get_main_window().close()

    from dfcleanser.common.common_utils import clear_screen
    #from dfcleanser.common.cfg import ZIPCODE_TITLE
    
    clear_screen()
    #displayHTML(ZIPCODE_TITLE)
    logger.info(" ZipCode Utility Instances closed")

def showZipCode()  :

    from dfcleanser.common.common_utils import displayHTML,clear_screen
    from dfcleanser.common.cfg import dfc_qt_chapters, ZIPCODE_QT_CHAPTER_ID, ZIPCODE_TITLE
    
    clear_screen()
    #displayHTML(ZIPCODE_TITLE)

    #logger.info("Opening ZipCode GUI")

    zipcode_gui = ZipCodeGui()
    zipcode_gui.show()
    
    dfc_qt_chapters.add_qt_chapter(ZIPCODE_QT_CHAPTER_ID,zipcode_gui,"showZipCode")

    total_instances     =   dfc_qt_chapters.get_qt_chapters_count(ZIPCODE_QT_CHAPTER_ID)
    logger.info(str(total_instances) + " Zipcode Utility Instances Loaded")

    #return zipcode_gui  

def closeZipCodeChapter()  :

    closeZipCodeInstances()

    from dfcleanser.common.cfg import run_javascript
    run_javascript("delete_dfc_cell('DCZipcodeUtility')","unable to delete ZipCode : ")    

