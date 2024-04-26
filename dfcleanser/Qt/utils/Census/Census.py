"""
# census
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:29:22 2017

@author: Rick
"""

from email.headerregistry import Address
import sys
this = sys.modules[__name__]


import inspect
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QStackedWidget

from PyQt5.QtCore import Qt
from PyQt5 import uic


import dfcleanser.common.cfg as cfg 

DEBUG_CENSUS                  =   True


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



DISPLAY_CENSUS                          =   "Census"

DISPLAY_SELECT_BING_GEOCODER            =   "Geocode select bing geocoder"
DISPLAY_SELECT_GOOGLE_GEOCODER          =   "Geocode select google geocoder"
DISPLAY_SELECT_ARCGIS_GEOCODER          =   "Geocode select arcgis geocoder"
DISPLAY_SELECT_NOMINATUM_GEOCODER       =   "Geocode select monimatum geocoder"
DISPLAY_SELECT_MAPQUEST_GEOCODER        =   "Geocode select mapquest geocoder"

DISPLAY_BING_QUERY_GEOCODING            =   "Geocode display bing geocoding"
DISPLAY_BING_REVERSE_GEOCODING          =   "Geocode display bing reverse geocoding"
DISPLAY_GOOGLE_QUERY_GEOCODING          =   "Geocode display google geocoding"
DISPLAY_GOOGLE_REVERSE_GEOCODING        =   "Geocode display google reverse geocoding"
DISPLAY_ARCGIS_QUERY_GEOCODING          =   "Geocode display garcgis geocoding"
DISPLAY_ARCGIS_REVERSE_GEOCODING        =   "Geocode display arcgis reverse geocoding"
DISPLAY_NOMINATUM_QUERY_GEOCODING       =   "Geocode display nominatum geocoding"
DISPLAY_NOMINATUM_REVERSE_GEOCODING     =   "Geocode display nominatum reverse geocoding"
DISPLAY_MAPQUEST_QUERY_GEOCODING        =   "Geocode display mapquest geocoding"
DISPLAY_MAPQUEST_REVERSE_GEOCODING      =   "Geocode display mapquest reverse geocoding"

DISPLAY_GEOCODE_QUERY_RESULTS           =   "Geocode display query results"
DISPLAY_GEOCODE_REVERSE_RESULTS         =   "Geocode display reverse results"

DISPLAY_GEOCODE_UTILITIES               =   "Geocode display utilities"
DISPLAY_ADDRESS_DISTANCE                =   "Geocode display address distancess"
DISPLAY_LATLNG_DISTANCE                 =   "Geocode display latlng distancess"
DISPLAY_DATAFRAME_DISTANCE              =   "Geocode display dataframe distances"

DISPLAY_CENTER_POINT                    =   "Geocode display center point"
DISPLAY_DF_CENTER_POINT                 =   "Geocode display df center point"

DISPLAY_DF_DISTANCE_FROM_LOCATION       =   "Geocode display df distance from location"
DISPLAY_DF_DISTANCE_FROM_CENTER_PT      =   "Geocode display df distance center point"

DEFAULT_ROW_HEIGHT                      =   20


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                       Census main GUI                         -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -    Subclass of QMainWindow to disp[lay the columns uniques    -#
# -----------------------------------------------------------------#
class CensusGui(QtWidgets.QMainWindow):

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

        self.CensusWidgets_stack_dict     =   {}

        # general housekeeping
        self.caller_stack   = inspect.currentframe().f_back
        self.stacked_widget = QStackedWidget(None)

        self.init_gui()

        self.form.dfcCensusMainLayout.addLayout(self.stackedLayout)
        self.form.dfcCensusMainLayout.addStretch()


    def update(self):   
        self.update()

    
    # -----------------------------------------------------------------#
    # -                     Initialize the gui                        -#
    # -----------------------------------------------------------------#
        
    def init_gui(self):

        if(DEBUG_CENSUS) :
            print("initgui")
        
        # set up the ui form from a qtdesigner ui
        cfgdir  = cfg.DataframeCleanserCfgData.get_dfc_qt_dir_name()
        ui_name = cfgdir +"\\utils\Census\CensusUI.ui"
        Form, Window = uic.loadUiType(ui_name)
        self.form = Form()
        self.form.setupUi(self)

        from PyQt5.QtWidgets import QStackedLayout
        self.stackedLayout = QStackedLayout()

        # -----------------------------------------------------#
        #     common window attribute settings     #
        # -----------------------------------------------------#
        
        # set common window attributes
        self.setWindowTitle("dfcleanser - Census")
        
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
        self.init_census_form()

        if(DEBUG_CENSUS) :
            print("initgui end")
           

    # -----------------------------------------------------------------#
    # -                 Initialize chapter buttons                    -#
    # -----------------------------------------------------------------#
    def init_census_buttons(self):

        if(DEBUG_CENSUS) :
            print("[CensusGui][init_census_buttons]  ")

        from dfcleanser.sw_utilities.dfc_qt_model import init_dfc_buttons, set_dfc_buttons_style

        buttons     =   [self.form.CensusDownloadDatasetsbutton, self.form.CensusSetupDatasetsbutton, self.form.CensusLoadToMemorybutton, 
                         self.form.CensusJoinToDfsbutton, self.form.CensusExportbutton,self.form.CensusLoadToDBbutton,self.form.CensusHelpbutton] 
        
        callbacks   =   [self.census_download_datasets,self.census_setup_datasets,self.census_load_to_memory,self.census_join_to_df,
                        self.census_export,self.census_load_to_db,self.census_help]
    
        # init buttons for usage
        System_Button_Style    =   "background-color:#0c4ca7; color:white; font : Arial; font-weight : bold; font-size : 13px;"
        init_dfc_buttons(buttons,System_Button_Style)

        # set button styles
        #set_dfc_buttons_style(buttons,Import_Button_Style)
        
        # adding action to a button
        for i in range(len(buttons)) :
            buttons[i].clicked.connect(callbacks[i])




        """

        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QLabel

        self.CensusDownloadDatasetsbutton            =   QPushButton()   
        self.CensusSetupDatasetsbutton               =   QPushButton()    
        self.CensusLoadToMemorybutton               =   QPushButton()   
        self.CensusJoinToDfsbutton                  =   QPushButton()   
        self.CensusExportbutton                     =   QPushButton()   
        self.CensusLoadToDBbutton                   =   QPushButton() 
        self.CensusHelpbutton                       =   QPushButton()  

        button_bar_button_list     =   [self.CensusDownloadDatasetsbutton, self.CensusSetupDatasetsbutton, self.CensusLoadToMemorybutton, self.CensusJoinToDfsbutton, 
                                        self.CensusExportbutton,self.CensusLoadToDBbutton,self.CensusHelpbutton]
        button_bar_text_list       =   ["Download\nCensus\nDatasets","Setup\nCensus\nDatasets","Load Census\nDatasets\nTo Memory","Census\nColumns To\nUser dfs",
                                        "Export\nCensus\nDatasetses","Load Census\nDatasets\nTo db(s)","Help"]
        button_bar_size_list       =   [149,80]
        button_bar_tool_tip_list   =   ["download datasets","setup datasets","load datasets","columns to df","export datasets","Load To DB","help"]
        button_bar_stylesheet      =   "background-color:#0c4ca7; color:white; font-size: 12px; font-weight: bold; font-family: Tahoma; "
        button_bar_connect_list    =   [self.census_download_datasets,self.census_setup_datasets,self.census_load_to_memory,self.census_join_to_df,
                                        self.census_export,self.census_load_to_db,self.census_help]


        from dfcleanser.sw_utilities.dfc_qt_model import build_button_bar
        self.census_button_bar           =   QHBoxLayout()
        build_button_bar(self.census_button_bar,button_bar_button_list,button_bar_text_list,
                         button_bar_size_list,button_bar_tool_tip_list,button_bar_stylesheet,button_bar_connect_list)
        
        print(self.census_button_bar)

        cmdbarLayout    =   QVBoxLayout()
        cmdbarLayout.addLayout(self.census_button_bar)
        cmdbarLayout.addStretch()
        
        #from dfcleanser.sw_utilities.dfc_qt_model import clearLayout
        #clearLayout(self.form.GeocodeCmdbarLayout)
        #self.form.GeocodeCmdbarLayout.addLayout(cmdbarLayout)
        """

    # -----------------------------------------------------------------#
    # -            Initialize the chapter splah image                 -#
    # -----------------------------------------------------------------#
    def init_census_splash_screen(self):

        if(DEBUG_CENSUS) :
            print("[GCensusGui][init_census_splash_screen]  ")

        from dfcleanser.sw_utilities.dfc_qt_model import build_chapter_splash_screen
        from dfcleanser.common.cfg import SWCensusUtility_ID
        build_chapter_splash_screen(SWCensusUtility_ID, self.form.Censussplash)

        if(DEBUG_CENSUS) :
            print("[end init_census_splash_screen]  ")

    # -----------------------------------------------------------------#
    # -             Initialize the dfs select form                    -#
    # -----------------------------------------------------------------#
    def init_census(self):

        if(DEBUG_CENSUS) :
            print("[GeocodeGui][init_geocode]  ")

        from PyQt5.QtWidgets import QLabel
        self.blank_label   =   QLabel()
        self.blank_label.setText("")
        self.blank_label.setAlignment(Qt.AlignLeft)
        self.blank_label.resize(600,50)
        self.blank_label.setStyleSheet("font-size: 12px; font-weight: bold; font-family: Arial; ")

        from PyQt5.QtWidgets import QVBoxLayout
        self.geocodeLayout     =   QVBoxLayout()
        self.geocodeLayout.addWidget(self.blank_label)
        self.geocodeLayout.addStretch()
        self.geocodeLayout.setAlignment(QtCore.Qt.AlignCenter) 

        from PyQt5.QtWidgets import QWidget  
        self.geocodemain    =   QWidget()
        self.geocodemain.setLayout(self.geocodeLayout)

        geocode_index  =   self.CensusWidgets_stack_dict.get(DISPLAY_CENSUS)

        if(geocode_index is None) :
            current_index   =  len(self.CensusWidgets_stack_dict)
            self.CensusWidgets_stack_dict.update({DISPLAY_CENSUS: current_index})
            self.stackedLayout.addWidget(self.geocodemain)
        else :
            current_index   =   geocode_index

        self.stackedLayout.setCurrentIndex(current_index)

        self.resize(1070,350)

    # -----------------------------------------------------------------#
    # -                 Initialize the gui form                       -#
    # -----------------------------------------------------------------#
    def init_census_form(self):

        if(DEBUG_CENSUS) :
            print("[CensusGui][init_geocode_form]  ")

        self.init_census_buttons()
        self.init_census_splash_screen()
        self.init_census()

        self.resize(1070,350)

    # -----------------------------------------------------------------#
    # -                 Main Gui Census Methods                       -#
    # -----------------------------------------------------------------#

    def census_download_datasets(self) :

         if(DEBUG_CENSUS) :
            print("[CensusGui][census_download_datasets]  ")
       
    def census_setup_datasets(self) :

         if(DEBUG_CENSUS) :
            print("[CensusGui][census_download_datasets]  ")

    def census_load_to_memory(self) :

         if(DEBUG_CENSUS) :
            print("[CensusGui][census_load_to_memory]  ")

    def census_join_to_df(self) :

         if(DEBUG_CENSUS) :
            print("[CensusGui][census_join_to_df]  ")

    def census_export(self) :

         if(DEBUG_CENSUS) :
            print("[CensusGui][census_export]  ")

    def census_load_to_db(self) :

         if(DEBUG_CENSUS) :
            print("[CensusGui][load_to_db]  ")

    def census_help(self) :

         if(DEBUG_CENSUS) :
            print("[CensusGui][help]  ")



    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                 Display Select Geocoder                       -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_select_geocoder(self,bulkflag=False,geocoderid=None):

        if(DEBUG_GEOCODE) :
            print("\n[GeocodeGui][display_geocode_select_geocoder]  ",bulkflag,geocoderid)

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        if(geocoderid is None) :
            from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_current_geocoder_id
            geocoderid  =   get_current_geocoder_id()

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocode_select_geocoder]  ",geocoderid)

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import (ArcGISId, BingId, GoogleId, OpenMapQuestId, NominatimId)
        if(geocoderid == BingId) :
           index_id     =   DISPLAY_SELECT_BING_GEOCODER
           height       =   750
        elif(geocoderid == GoogleId) :
           index_id     =   DISPLAY_SELECT_GOOGLE_GEOCODER
           height       =   950
        elif(geocoderid == ArcGISId) :
           index_id     =   DISPLAY_SELECT_ARCGIS_GEOCODER
           height       =   750
        elif(geocoderid == OpenMapQuestId) :
           index_id     =   DISPLAY_SELECT_MAPQUEST_GEOCODER
           height       =   850
        elif(geocoderid == NominatimId) :
           index_id     =   DISPLAY_SELECT_NOMINATUM_GEOCODER
           height       =   800

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocode_select_geocoder]  ",geocoderid,index_id,height)

        select_geocoder_index  =   self.GeocodeWidgets_stack_dict.get(index_id)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_select_geocoder]  index : ",select_geocoder_index)
        
        if(select_geocoder_index is None) :

            try :

                from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import Geoocoder_Connector_Widget
                parms   =   [self,bulkflag,geocoderid]

                if(geocoderid == BingId)                : self.Bing_Geocode_select_geocoder   =   Geoocoder_Connector_Widget(parms)
                elif(geocoderid == GoogleId)            : self.Google_Geocode_select_geocoder   =   Geoocoder_Connector_Widget(parms)
                elif(geocoderid == ArcGISId)            : self.ArcGis_Geocode_select_geocoder   =   Geoocoder_Connector_Widget(parms)
                elif(geocoderid == OpenMapQuestId)      : self.OpenMapQuest_Geocode_select_geocoder   =   Geoocoder_Connector_Widget(parms)
                elif(geocoderid == NominatimId)         : self.Nominatim_Geocode_select_geocoder   =   Geoocoder_Connector_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_select_geocoder] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.GeocodeWidgets_stack_dict)
                self.GeocodeWidgets_stack_dict.update({index_id  : current_index})

                if(geocoderid == BingId)                : self.stackedLayout.addWidget(self.Bing_Geocode_select_geocoder)
                elif(geocoderid == GoogleId)            : self.stackedLayout.addWidget(self.Google_Geocode_select_geocoder)
                elif(geocoderid == ArcGISId)            : self.stackedLayout.addWidget(self.ArcGis_Geocode_select_geocoder)
                elif(geocoderid == OpenMapQuestId)      : self.stackedLayout.addWidget(self.OpenMapQuest_Geocode_select_geocoder)
                elif(geocoderid == NominatimId)         : self.stackedLayout.addWidget(self.Nominatim_Geocode_select_geocoder)

        else :

            if(DEBUG_GEOCODE) :
                print("[GeocodeGui][display_select_geocoder] reload_data:  ",select_geocoder_index)

            if(geocoderid == BingId)                : self.Bing_Geocode_select_geocoder.reload_data(self,bulkflag,geocoderid)
            elif(geocoderid == GoogleId)            : self.Google_Geocode_select_geocoder.reload_data(self,bulkflag,geocoderid)
            elif(geocoderid == ArcGISId)            : self.ArcGis_Geocode_select_geocoder.reload_data(self,bulkflag,geocoderid)
            elif(geocoderid == OpenMapQuestId)      : self.OpenMapQuest_Geocode_select_geocoder.reload_data(self,bulkflag,geocoderid)
            elif(geocoderid == NominatimId)         : self.Nominatim_Geocode_select_geocoder.reload_data(self,bulkflag,geocoderid)

            current_index   =   select_geocoder_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_select_geocoder] end : stack \n  ",self.GeocodeWidgets_stack_dict)

        self.resize(1070,height)


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -              Display Interactive Geocoding                    -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_interactive_geocoding(self,geocoding_type):

        if(DEBUG_GEOCODE) :
            print("\n[GeocodeGui][display_interactive_geocoding]  ",geocoding_type)

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_current_geocoder_id
        geocoderid  =   get_current_geocoder_id()

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_interactive_geocoding]  ",geocoderid)

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import (QUERY, REVERSE)
        from dfcleanser.Qt.utils.Geocode.GeocodeModel import (ArcGISId,BingId,GoogleId,OpenMapQuestId, NominatimId, get_geocoder_title)

        if(geocoding_type == QUERY) :
    
            if(geocoderid == ArcGISId) :

                index_id     =   DISPLAY_ARCGIS_QUERY_GEOCODING
                height       =   800
            
            elif(geocoderid == BingId) :

                index_id     =   DISPLAY_BING_QUERY_GEOCODING
                height       =   1050

            elif(geocoderid == GoogleId) :

                index_id     =   DISPLAY_GOOGLE_QUERY_GEOCODING
                height       =   1050

            elif(geocoderid == OpenMapQuestId) :

                index_id     =   DISPLAY_MAPQUEST_QUERY_GEOCODING
                height       =   800

            elif(geocoderid == NominatimId) :

                index_id     =   DISPLAY_NOMINATUM_QUERY_GEOCODING
                height       =   1050

        else :

            if(geocoderid == ArcGISId) :

                index_id     =   DISPLAY_ARCGIS_REVERSE_GEOCODING
                height       =   900
            
            elif(geocoderid == BingId) :

                index_id     =   DISPLAY_BING_REVERSE_GEOCODING
                height       =   900

            elif(geocoderid == GoogleId) :

                index_id     =   DISPLAY_GOOGLE_REVERSE_GEOCODING
                height       =   850

            elif(geocoderid == OpenMapQuestId) :

                index_id     =   DISPLAY_MAPQUEST_REVERSE_GEOCODING
                height       =   900

            elif(geocoderid == NominatimId) :

                index_id     =   DISPLAY_NOMINATUM_REVERSE_GEOCODING
                height       =   900

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_interactive_geocoding]  ",index_id,height)

        geocoding_index  =   self.GeocodeWidgets_stack_dict.get(index_id)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_interactive_geocoding]  index : ",geocoding_index)
        
        if(geocoding_index is None) :

            try :

                from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import Geoocoder_Geocoding_Widget
                parms   =   [self,geocoding_type,geocoderid]

                if(geocoding_type == QUERY) :
           
                    if(geocoderid == ArcGISId)          :   self.arcgis_query       =   Geoocoder_Geocoding_Widget(parms)
                    elif(geocoderid == BingId)          :   self.bing_query         =   Geoocoder_Geocoding_Widget(parms)
                    elif(geocoderid == GoogleId)        :   self.google_query       =   Geoocoder_Geocoding_Widget(parms)
                    elif(geocoderid == OpenMapQuestId)  :   self.openmapquest_query =   Geoocoder_Geocoding_Widget(parms)
                    elif(geocoderid == NominatimId)     :   self.nominatum_query    =   Geoocoder_Geocoding_Widget(parms)

                else :
           
                    if(geocoderid == ArcGISId)          :   self.arcgis_reverse       =   Geoocoder_Geocoding_Widget(parms)
                    elif(geocoderid == BingId)          :   self.bing_reverse         =   Geoocoder_Geocoding_Widget(parms)
                    elif(geocoderid == GoogleId)        :   self.google_reverse       =   Geoocoder_Geocoding_Widget(parms)
                    elif(geocoderid == OpenMapQuestId)  :   self.openmapquest_reverse =   Geoocoder_Geocoding_Widget(parms)
                    elif(geocoderid == NominatimId)     :   self.nominatum_reverse    =   Geoocoder_Geocoding_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_interactive_geocoding] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.GeocodeWidgets_stack_dict)
                self.GeocodeWidgets_stack_dict.update({index_id  : current_index})
                
                if(geocoding_type == QUERY) :
           
                    if(geocoderid == ArcGISId)          :   self.stackedLayout.addWidget(self.arcgis_query)
                    elif(geocoderid == BingId)          :   self.stackedLayout.addWidget(self.bing_query)
                    elif(geocoderid == GoogleId)        :   self.stackedLayout.addWidget(self.google_query)
                    elif(geocoderid == OpenMapQuestId)  :   self.stackedLayout.addWidget(self.openmapquest_query)
                    elif(geocoderid == NominatimId)     :   self.stackedLayout.addWidget(self.nominatum_query)

                else :
           
                    if(geocoderid == ArcGISId)          :   self.stackedLayout.addWidget(self.arcgis_reverse)
                    elif(geocoderid == BingId)          :   self.stackedLayout.addWidget(self.bing_reverse)
                    elif(geocoderid == GoogleId)        :   self.stackedLayout.addWidget(self.google_reverse)
                    elif(geocoderid == OpenMapQuestId)  :   self.stackedLayout.addWidget(self.openmapquest_reverse)
                    elif(geocoderid == NominatimId)     :   self.stackedLayout.addWidget(self.nominatum_reverse)

        else :

            if(DEBUG_GEOCODE) :
                print("[GeocodeGui][display_interactive_geocoding] reload_data:  ",geocoding_index)

            if(geocoding_type == QUERY) :
           
                if(geocoderid == ArcGISId)          :   self.arcgis_query.reload_data(self,geocoding_type,geocoderid)
                elif(geocoderid == BingId)          :   self.bing_query.reload_data(self,geocoding_type,geocoderid)
                elif(geocoderid == GoogleId)        :   self.google_query.reload_data(self,geocoding_type,geocoderid)
                elif(geocoderid == OpenMapQuestId)  :   self.openmapquest_query.reload_data(self,geocoding_type,geocoderid)
                elif(geocoderid == NominatimId)     :   self.nominatum_query.reload_data(geocoding_type,geocoderid)

            else :
           
                if(geocoderid == ArcGISId)          :   self.arcgis_reverse.reload_data(self,geocoding_type,geocoderid)
                elif(geocoderid == BingId)          :   self.bing_reverse.reload_data(self,geocoding_type,geocoderid)
                elif(geocoderid == GoogleId)        :   self.google_reverse.reload_data(self,geocoding_type,geocoderid)
                elif(geocoderid == OpenMapQuestId)  :   self.openmapquest_reverse.reload_dataself,(geocoding_type,geocoderid)
                elif(geocoderid == NominatimId)     :   self.nominatum_reverse.reload_data(geocoding_type,geocoderid)

            current_index   =   geocoding_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_interactive_geocoding] end : stack \n  ",self.GeocodeWidgets_stack_dict)

        self.resize(1070,height)


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                  Display Geocoding Data                       -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_geocoding_data(self,geocoding_type,results):

        if(DEBUG_GEOCODE) :
            print("\n[GeocodeGui][display_geocoding_data]  ",geocoding_type,"\n  ",results)

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_current_geocoder_id
        geocoderid  =   get_current_geocoder_id()

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_data]  ",geocoderid)

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import (QUERY)

        if(geocoding_type == QUERY) :
            geocoding_index  =   self.GeocodeWidgets_stack_dict.get(DISPLAY_GEOCODE_QUERY_RESULTS)
        else :
            geocoding_index  =   self.GeocodeWidgets_stack_dict.get(DISPLAY_GEOCODE_REVERSE_RESULTS)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_data]  index : ",geocoding_index)
        
        if(geocoding_index is None) :

            try :

                from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import Geoocoder_Geocoding_Results_Widget
                parms   =   [self,geocoding_type,results]

                if(geocoding_type == QUERY) :
                    self.geocode_query_results      =   Geoocoder_Geocoding_Results_Widget(parms)
                else :
                     self.geocode_reverse_results   =   Geoocoder_Geocoding_Results_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_geocoding_results] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.GeocodeWidgets_stack_dict)
                if(geocoding_type == QUERY) :
                    self.GeocodeWidgets_stack_dict.update({DISPLAY_GEOCODE_QUERY_RESULTS : current_index})
                else :
                    self.GeocodeWidgets_stack_dict.update({DISPLAY_GEOCODE_REVERSE_RESULTS : current_index})
                
                if(geocoding_type == QUERY) : 
                    self.stackedLayout.addWidget(self.geocode_query_results)
                else :
                    self.stackedLayout.addWidget(self.geocode_reverse_results)

        else :

            if(DEBUG_GEOCODE) :
                print("[GeocodeGui][display_geocoding_data] reload_data:  ",geocoding_index)

            if(geocoding_type == QUERY) :
                self.geocode_query_results.reload_data(self,geocoding_type,results)
            else :
                self.geocode_reverse_results.reload_data(self,geocoding_type,results)

            current_index   =   geocoding_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_data] end : stack \n  ",self.GeocodeWidgets_stack_dict)

        self.resize(1070,800)



    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                  Display Geocoding Utilities                  -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_geocoding_utilities(self):

        if(DEBUG_GEOCODE) :
            print("\n[GeocodeGui][display_geocoding_utilities]  ")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_current_geocoder_id
        geocoderid  =   get_current_geocoder_id()

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_utilities]  ",geocoderid)

        geocoding_index  =   self.GeocodeWidgets_stack_dict.get(DISPLAY_GEOCODE_UTILITIES )

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_utilities]  index : ",geocoding_index)
        
        if(geocoding_index is None) :

            try :

                from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import Geocode_Utilities_Widget

                parms   =   [self]
                self.geocode_utilities      =   Geocode_Utilities_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_geocoding_utilities] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.GeocodeWidgets_stack_dict)
                self.GeocodeWidgets_stack_dict.update({DISPLAY_GEOCODE_UTILITIES : current_index})
                self.stackedLayout.addWidget(self.geocode_utilities)

        else :

            if(DEBUG_GEOCODE) :
                print("[GeocodeGui][display_geocoding_utilities] reload_data:  ",geocoding_index)

            self.geocode_utilities.init_command_bar()
            current_index   =   geocoding_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_utilities] end : stack \n  ",self.GeocodeWidgets_stack_dict)

        self.resize(1070,350)


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                  Display Geocoding Utilities                  -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_geocoding_distance_utility(self,gintype):

        if(DEBUG_GEOCODE) :
            print("\n[GeocodeGui][display_geocoding_distance_utility]",gintype)

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_current_geocoder_id
        geocoderid  =   get_current_geocoder_id()

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_distance_utility]  ",geocoderid)

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import ADDRESS, LAT_LNG
        if(gintype == ADDRESS) :
            geocoding_index  =   self.GeocodeWidgets_stack_dict.get(DISPLAY_ADDRESS_DISTANCE)
        elif(gintype == LAT_LNG) :
            geocoding_index  =   self.GeocodeWidgets_stack_dict.get(DISPLAY_LATLNG_DISTANCE)
        else :
            geocoding_index  =   self.GeocodeWidgets_stack_dict.get(DISPLAY_DATAFRAME_DISTANCE)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_distance_utility]  index : ",geocoding_index)
        
        if(geocoding_index is None) :

            try :

                if(gintype == ADDRESS) :

                    from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import Geocode_Address_Distance_Utility_Widget
                    parms   =   [self]
                    self.geocode_address_distance_utility      =   Geocode_Address_Distance_Utility_Widget(parms)

                if(gintype == LAT_LNG) :

                    from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import Geocode_LatLng_Distance_Utility_Widget
                    parms   =   [self]
                    self.geocode_latlng_distance_utility      =   Geocode_LatLng_Distance_Utility_Widget(parms)

                else :

                    from dfcleanser.common.cfg import get_dfc_dataframes_titles_list, get_dfc_dataframe_df
                    dataframes      =   get_dfc_dataframes_titles_list()

                    if(dataframes is None) :

                        title       =   "dfcleanser error"       
                        status_msg  =   "No dfc dataframe defined"
                        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                        display_error_msg(title,status_msg)

                        return(None)


                    from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import Geocode_df_Distance_Utility_Widget
                    parms   =   [self]
                    self.geocode_df_distance_utility      =   Geocode_df_Distance_Utility_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_geocoding_distance_utility] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                if(gintype == ADDRESS) :

                    current_index   =  len(self.GeocodeWidgets_stack_dict)
                    self.GeocodeWidgets_stack_dict.update({DISPLAY_ADDRESS_DISTANCE : current_index})
                    self.stackedLayout.addWidget(self.geocode_address_distance_utility)

                elif(gintype == LAT_LNG) :

                    current_index   =  len(self.GeocodeWidgets_stack_dict)
                    self.GeocodeWidgets_stack_dict.update({DISPLAY_LATLNG_DISTANCE : current_index})
                    self.stackedLayout.addWidget(self.geocode_latlng_distance_utility)
                
                else :

                    current_index   =  len(self.GeocodeWidgets_stack_dict)
                    self.GeocodeWidgets_stack_dict.update({DISPLAY_DATAFRAME_DISTANCE : current_index})
                    self.stackedLayout.addWidget(self.geocode_df_distance_utility)

        else :

            if(DEBUG_GEOCODE) :
                print("[GeocodeGui][display_geocoding_distance_utility] reload_data:  ",geocoding_index)
            
            #if(gintype == ADDRESS) :
            #    self.geocode_address_distance_utility.reload_data(self)
            #else :
            #    self.geocode_latlng_distance_utility.reload_data(self)

            current_index   =   geocoding_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_distance_utility] end : stack \n  ",self.GeocodeWidgets_stack_dict)

        self.resize(1070,900)


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                  Display Geocoding Utilities                  -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_geocoding_center_point(self,ptsource):

        if(DEBUG_GEOCODE) :
            print("\n[GeocodeGui][display_geocoding_center_point]",ptsource)

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import DATAFRAME, LAT_LNG
        if(ptsource == LAT_LNG) :
            geocoding_index  =   self.GeocodeWidgets_stack_dict.get(DISPLAY_CENTER_POINT)
        else :
            geocoding_index  =   self.GeocodeWidgets_stack_dict.get(DISPLAY_DF_CENTER_POINT)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_center_point]  index : ",geocoding_index)
        
        if(geocoding_index is None) :

            try :

                if(ptsource == LAT_LNG) :

                    from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import Geocode_Center_Point_Widget
                    parms   =   [self]
                    self.geocode_center_pt_utility      =   Geocode_Center_Point_Widget(parms)

                else :

                    from dfcleanser.common.cfg import get_dfc_dataframes_titles_list, get_dfc_dataframe_df
                    dataframes      =   get_dfc_dataframes_titles_list()

                    if(dataframes is None) :

                        title       =   "dfcleanser error"       
                        status_msg  =   "No dfc dataframe defined"
                        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                        display_error_msg(title,status_msg)

                        return(None)

                    from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import Geocode_df_Center_Point_Widget
                    parms   =   [self]
                    self.geocode_df_center_pt_utility      =   Geocode_df_Center_Point_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_geocoding_center_point] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                if(ptsource == LAT_LNG) :

                    current_index   =  len(self.GeocodeWidgets_stack_dict)
                    self.GeocodeWidgets_stack_dict.update({DISPLAY_CENTER_POINT : current_index})
                    self.stackedLayout.addWidget(self.geocode_center_pt_utility)

                else :

                    current_index   =  len(self.GeocodeWidgets_stack_dict)
                    self.GeocodeWidgets_stack_dict.update({DISPLAY_DF_CENTER_POINT : current_index})
                    self.stackedLayout.addWidget(self.geocode_df_center_pt_utility)

        else :

            if(DEBUG_GEOCODE) :
                print("[GeocodeGui][display_geocoding_center_point] reload_data:  ",geocoding_index)

            current_index   =   geocoding_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_center_point] end : stack \n  ",self.GeocodeWidgets_stack_dict)

        if(ptsource == LAT_LNG) :
            self.resize(1070,750)
        else :
            self.resize(1070,850)

    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                  Display Geocoding Utilities                  -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_geocoding_distance_from_fixed_location(self,fixedpt_type):

        if(DEBUG_GEOCODE) :
            print("\n[GeocodeGui][display_geocoding_distance_from_fixed_location]",fixedpt_type)

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import USER_LOCATION
        if(fixedpt_type == USER_LOCATION) :
            geocoding_index  =   self.GeocodeWidgets_stack_dict.get(DISPLAY_DF_DISTANCE_FROM_LOCATION)
        else :
            geocoding_index  =   self.GeocodeWidgets_stack_dict.get(DISPLAY_DF_DISTANCE_FROM_CENTER_PT)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_distance_from_fixed_location]  index : ",geocoding_index)
        
        if(geocoding_index is None) :

            try :

                from dfcleanser.common.cfg import get_dfc_dataframes_titles_list, get_dfc_dataframe_df
                dataframes      =   get_dfc_dataframes_titles_list()

                if(dataframes is None) :

                    title       =   "dfcleanser error"       
                    status_msg  =   "No dfc dataframe defined"
                    from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                    display_error_msg(title,status_msg)

                    return(None)


                if(fixedpt_type == USER_LOCATION) :

                    from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import Geocode_Distance_From_User_Loaction_Widget
                    parms   =   [self]
                    self.geocode_distance_user_pt_utility      =   Geocode_Distance_From_User_Loaction_Widget(parms)

                else :

                    from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import Geocode_Distance_From_Center_Point_Widget
                    parms   =   [self]
                    self.geocode_distance_center_pt_utility      =   Geocode_Distance_From_Center_Point_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_geocoding_distance_from_fixed_location] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                if(fixedpt_type == USER_LOCATION) :

                    current_index   =  len(self.GeocodeWidgets_stack_dict)
                    self.GeocodeWidgets_stack_dict.update({DISPLAY_DF_DISTANCE_FROM_LOCATION : current_index})
                    self.stackedLayout.addWidget(self.geocode_distance_user_pt_utility)

                else :

                    current_index   =  len(self.GeocodeWidgets_stack_dict)
                    self.GeocodeWidgets_stack_dict.update({DISPLAY_DF_DISTANCE_FROM_CENTER_PT : current_index})
                    self.stackedLayout.addWidget(self.geocode_distance_center_pt_utility )

        else :

            if(DEBUG_GEOCODE) :
                print("[GeocodeGui][display_geocoding_distance_from_fixed_location] reload_data:  ",geocoding_index)

            current_index   =   geocoding_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_distance_from_fixed_location] end : stack \n  ",self.GeocodeWidgets_stack_dict)

        if(fixedpt_type == USER_LOCATION) :
            self.resize(1070,950)
        else :
            self.resize(1070,950)



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                Global access to Geocode Chapter               -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def clearCensus()  :

    from dfcleanser.common.common_utils import displayHTML,clear_screen
    from dfcleanser.common.cfg import CENSUS_TITLE
    
    clear_screen()
    displayHTML(CENSUS_TITLE)


def closeCensusInstances()  :
    
    from dfcleanser.common.cfg import dfc_qt_chapters, CENSUS_QT_CHAPTER_ID
    num_instances   =   dfc_qt_chapters.get_qt_chapters_count(CENSUS_QT_CHAPTER_ID)

    if(num_instances > 0) :
        instances       =   dfc_qt_chapters.get_qt_chapters(CENSUS_QT_CHAPTER_ID)
        for i in range(len(instances)) :
            instances[i].get_main_window().close()

    from dfcleanser.common.common_utils import displayHTML,clear_screen
    from dfcleanser.common.cfg import CENSUS_TITLE
    
    clear_screen()
    displayHTML(CENSUS_TITLE)


def showCensus()  :

    from dfcleanser.common.common_utils import displayHTML,clear_screen
    from dfcleanser.common.cfg import dfc_qt_chapters, CENSUS_QT_CHAPTER_ID, CENSUS_TITLE
    
    clear_screen()
    displayHTML(CENSUS_TITLE)

    logger.info("Opening Geocode GUI")

    gecode_gui = CensusGui()
    gecode_gui.show()

    dfc_qt_chapters.add_qt_chapter(CENSUS_QT_CHAPTER_ID,CensusGui,"showCensus")

    total_instances     =   dfc_qt_chapters.get_qt_chapters_count(CENSUS_QT_CHAPTER_ID)
    logger.info(str(total_instances) + " Census                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Utility Instances Loaded")

    return gecode_gui  

def closeGCensusChapter()  :

    closeCensusInstances()

    from dfcleanser.common.cfg import run_javascript
    run_javascript("delete_dfc_cell('DCCensusUtility')","unable to delete Geocode : ")    

