"""
# zipcode
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

from dfcleanser.Qt.utils.Geocode.GeocodeModel import DEBUG_GEOCODE

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



DISPLAY_GEOCODE                         =   "Geocode"

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

DISPLAY_SPLIT_COLUMN                    =   "Geocode display split column"
DISPLAY_JOIN_COLUMNS                    =   "Geocode display join columns"

DISPLAY_GEOCODE_ADDRESS_DISTANCE_RESULTS         =   "Geocode display address distance results"
DISPLAY_GEOCODE_LAT_LNG_DISTANCE_RESULTS         =   "Geocode display latlng distance results"

DISPLAY_GEOCODE_CENTER_POINT_RESULTS             =   "Geocode display center point results"
DISPLAY_GEOCODE_DF_CENTER_POINT_RESULTS          =   "Geocode display df center point results"
DISPLAY_GEOCODE_LIST_POINT_RESULTS               =   "Geocode display closest results"



DEFAULT_ROW_HEIGHT                      =   20


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                       System main GUI                         -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

from PyQt5.QtWidgets import *

# -----------------------------------------------------------------#
# -    Subclass of QMainWindow to disp[lay the columns uniques    -#
# -----------------------------------------------------------------#
class GeocodeGui(QtWidgets.QMainWindow):

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

        self.GeocodeWidgets_stack_dict     =   {}

        # enable custom window hint
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)

        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)


        # general housekeeping
        self.caller_stack   = inspect.currentframe().f_back
        self.stacked_widget = QStackedWidget(None)

        self.init_gui()

        self.form.GeocodeLayout.addLayout(self.stackedLayout)
        self.form.GeocodeLayout.addStretch()


    def update(self):   
        self.update()

    
    # -----------------------------------------------------------------#
    # -                     Initialize the gui                        -#
    # -----------------------------------------------------------------#
        
    def init_gui(self):

        if(DEBUG_GEOCODE) :
            print("initgui")
        
        # set up the ui form from a qtdesigner ui
        cfgdir  = cfg.DataframeCleanserCfgData.get_dfc_qt_dir_name()
        ui_name = cfgdir +"\\utils\Geocode\GeocodeUI.ui"
        Form, Window = uic.loadUiType(ui_name)
        self.form = Form()
        self.form.setupUi(self)

        from PyQt5.QtWidgets import QStackedLayout
        self.stackedLayout = QStackedLayout()

        # -----------------------------------------------------#
        #     common window attribute settings     #
        # -----------------------------------------------------#
        
        # set common window attributes
        self.setWindowTitle("dfcleanser - Geocode")
        
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
        icon_name   =   dfcdir +"\GeocodeChapterIcon.png"
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
        self.init_geocode_form()

        if(DEBUG_GEOCODE) :
            print("initgui end")
           

    # -----------------------------------------------------------------#
    # -                 Initialize chapter buttons                    -#
    # -----------------------------------------------------------------#
    def init_geocode_buttons(self):

        if(DEBUG_GEOCODE) :
            print("[SystemGui][init_geocode_buttons]  ")

        from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QLabel

        self.selectgeoocoderbutton            =   QPushButton()   
        self.geocodequerybutton               =   QPushButton()    
        self.geocodereversebutton             =   QPushButton()   
        self.geocodebulkbutton                =   QPushButton()   
        self.geocodeutilitiesbutton           =   QPushButton()   
        self.geocodehelpbutton                =   QPushButton()

        button_bar_button_list     =   [self.selectgeoocoderbutton, self.geocodequerybutton, self.geocodereversebutton, 
                                        self.geocodebulkbutton, self.geocodeutilitiesbutton, self.geocodehelpbutton]
        button_bar_text_list       =   ["Select Geocoder","Query\nGeocoding","Reverse\nGeocoding","Bulk Geocoding","Geocode Utilities", "Help"]
        button_bar_size_list       =   [167,100]
        button_bar_tool_tip_list   =   ["select geocoder","geocoding query","geocodin reverse","bulk copy","geocode utilities","geocode help"]
        button_bar_stylesheet      =   "background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; "
        button_bar_connect_list    =   [self.select_geocoder, self.geocode_query,self.geocode_reverse,
                                        self.geocode_bulk,self.geocode_utilities_display, self.geocode_help]

        from dfcleanser.sw_utilities.dfc_qt_model import build_button_bar
        self.transform_button_bar           =   QHBoxLayout()
        build_button_bar(self.transform_button_bar,button_bar_button_list,button_bar_text_list,button_bar_size_list,button_bar_tool_tip_list,button_bar_stylesheet,button_bar_connect_list)

        cmdbarLayout    =   QVBoxLayout()
        cmdbarLayout.addLayout(self.transform_button_bar)
        cmdbarLayout.addStretch()
        
        from dfcleanser.sw_utilities.dfc_qt_model import clearLayout
        clearLayout(self.form.GeocodeCmdbarLayout)
        self.form.GeocodeCmdbarLayout.addLayout(cmdbarLayout)


    # -----------------------------------------------------------------#
    # -            Initialize the chapter splah image                 -#
    # -----------------------------------------------------------------#
    def init_geocode_splash_screen(self):

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][init_geocode_splash_screen]  ")

        from dfcleanser.sw_utilities.dfc_qt_model import build_chapter_splash_screen
        from dfcleanser.common.cfg import SWGeocodeUtility_ID
        build_chapter_splash_screen(SWGeocodeUtility_ID, self.form.Geocodesplash)

        if(DEBUG_GEOCODE) :
            print("[end init_geocode_splash_screen]  ")

    # -----------------------------------------------------------------#
    # -             Initialize the dfs select form                    -#
    # -----------------------------------------------------------------#
    def init_geocode(self):

        if(DEBUG_GEOCODE) :
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

        geocode_index  =   self.GeocodeWidgets_stack_dict.get(DISPLAY_GEOCODE)

        if(geocode_index is None) :
            current_index   =  len(self.GeocodeWidgets_stack_dict)
            self.GeocodeWidgets_stack_dict.update({DISPLAY_GEOCODE: current_index})
            self.stackedLayout.addWidget(self.geocodemain)
        else :
            current_index   =   geocode_index

        self.stackedLayout.setCurrentIndex(current_index)

        self.resize(1070,350)

    # -----------------------------------------------------------------#
    # -                 Initialize the gui form                       -#
    # -----------------------------------------------------------------#
    def init_geocode_form(self):

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][init_geocode_form]  ")

        self.init_geocode_buttons()
        self.init_geocode_splash_screen()
        self.init_geocode()

        self.resize(1070,350)

    # -----------------------------------------------------------------#
    # -                 Main Gui Geocode Methods                      -#
    # -----------------------------------------------------------------#

    def select_geocoder(self):

        self.form.selectgeoocoderbutton.toggle()

        if(DEBUG_GEOCODE) :
            print("\n[GeocodeGui][select_geocoder]  ")

        self.display_select_geocoder()

    def geocode_query(self):

        self.form.geocodequerybutton.toggle()

        if(DEBUG_GEOCODE) :
            print("\n[GeocodeGui][geocode_query]  ")

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import QUERY
        self.display_interactive_geocoding(QUERY)
    
    def geocode_reverse(self):

        self.form.geocodereversebutton.toggle()

        if(DEBUG_GEOCODE) :
            print("\n[GeocodeGui][geocode_reverse]  ")

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import REVERSE
        self.display_interactive_geocoding(REVERSE)

    def geocode_bulk(self):

        self.form.geocodebulkbutton.toggle()

        if(DEBUG_GEOCODE) :
            print("\n[GeocodeGui][geocode_bulk]  ")

        from dfcleanser.common.common_utils import run_jscript
        jscript     =   "add_dfcleanser_chapter(" + str(cfg.DC_GEOCODE_BULK_ID) + ");"
        run_jscript(jscript,"fail to add bulk geocode chapter : ")

    def geocode_utilities_display(self):

        self.form.geocodeutilitiesbutton.toggle()

        if(DEBUG_GEOCODE) :
            print("\n[GeocodeGui][geocode_utilities]  ")

        self.display_geocoding_utilities()

    def geocode_help(self):

        #self.form.geocodehelpbutton.toggle()

        if(DEBUG_GEOCODE) :
            print("\n[GeocodeGui][geocode_help]  ")

        from dfcleanser.common.common_utils import display_url
        display_url("https://rickkrasinski.github.io/dfcleanser/help/dfcleanser-geocoding.html")



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


        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_current_geocoder_id
        geocoderid  =   get_current_geocoder_id()

        if(DEBUG_GEOCODE) :
            print("\n[GeocodeGui][display_interactive_geocoding]  type : geocodeid : ",geocoding_type,geocoderid)

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import (QUERY, REVERSE)
        from dfcleanser.Qt.utils.Geocode.GeocodeModel import (ArcGISId,BingId,GoogleId,OpenMapQuestId, NominatimId, get_geocoder_title)

        if(geocoding_type == QUERY) :
    
            if(geocoderid == ArcGISId) :
                index_id     =   DISPLAY_ARCGIS_QUERY_GEOCODING
                height       =   800
            elif(geocoderid == BingId) :
                index_id     =   DISPLAY_BING_QUERY_GEOCODING
                height       =   900
            elif(geocoderid == GoogleId) :
                index_id     =   DISPLAY_GOOGLE_QUERY_GEOCODING
                height       =   950
            elif(geocoderid == OpenMapQuestId) :
                index_id     =   DISPLAY_MAPQUEST_QUERY_GEOCODING
                height       =   800
            elif(geocoderid == NominatimId) :
                index_id     =   DISPLAY_NOMINATUM_QUERY_GEOCODING
                height       =   850

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

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import get_current_geocoder_id
        geocoderid  =   get_current_geocoder_id()

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_data]  type : geocodid : ",geocoding_type,geocoderid)
            print("[GeocodeGui][display_geocoding_data]  results : ",results)            

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
    # -            Display Geocoding Distance Results                 -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_geocoding_distance_data(self,geocoding_type,units,results):

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_distance_data]  type : ",geocoding_type,units)
            print("[GeocodeGui][display_geocoding_distance_data]  results : \n   ",results)            

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import ADDRESS

        if(geocoding_type == ADDRESS) :
            geocoding_index  =   self.GeocodeWidgets_stack_dict.get(DISPLAY_GEOCODE_ADDRESS_DISTANCE_RESULTS)
        else :
            geocoding_index  =   self.GeocodeWidgets_stack_dict.get(DISPLAY_GEOCODE_LAT_LNG_DISTANCE_RESULTS)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_distance_data]  index : ",geocoding_index)
        
        if(geocoding_index is None) :

            try :

                from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import Geoocoder_Distance_Results_Widget
                parms   =   [self,geocoding_type,units,results]

                if(geocoding_type == ADDRESS) :
                    self.geocode_address_distance_results       =   Geoocoder_Distance_Results_Widget(parms)
                else :
                     self.geocode_latlng_distance_results       =   Geoocoder_Distance_Results_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_geocoding_distance_data] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.GeocodeWidgets_stack_dict)
                if(geocoding_type == ADDRESS) :
                    self.GeocodeWidgets_stack_dict.update({DISPLAY_GEOCODE_ADDRESS_DISTANCE_RESULTS : current_index})
                else :
                    self.GeocodeWidgets_stack_dict.update({DISPLAY_GEOCODE_LAT_LNG_DISTANCE_RESULTS : current_index})
                
                if(geocoding_type == ADDRESS) : 
                    self.stackedLayout.addWidget(self.geocode_address_distance_results)
                else :
                    self.stackedLayout.addWidget(self.geocode_latlng_distance_results)

        else :

            if(DEBUG_GEOCODE) :
                print("[GeocodeGui][display_geocoding_distance_data] reload_data:  ",geocoding_index)

            if(geocoding_type == ADDRESS) :
                self.geocode_address_distance_results.reload_data(self,geocoding_type,units,results)
            else :
                self.geocode_latlng_distance_results.reload_data(self,geocoding_type,units,results)

            current_index   =   geocoding_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_distance_data] end : stack \n  ",self.GeocodeWidgets_stack_dict)

        self.resize(1070,600)


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -           Display Geocoding Center Point Results              -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def display_geocoding_center_point_data(self,center_point_type,geopoints,center_point):

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import USER_LOCATION
        if(center_point_type == USER_LOCATION) : 

            self.geopoints  =   geopoints
            self.dftitle    =   None
            self.colname    =   None 

        else :

            self.geopoints  =   None
            self.dftitle    =   geopoints[0]
            self.colname    =   geopoints[1] 


        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_center_point_data]  type : ",center_point_type)
            if(center_point_type == USER_LOCATION) :
                print("[GeocodeGui][display_geocoding_center_point_data] geopoints :   \n",geopoints)
            else :
                print("[GeocodeGui][display_geocoding_center_point_data] dftitle :  colname : ",self.dftitle,self.colname)


            print("[GeocodeGui][display_geocoding_center_point_data]  center_point :   ",center_point)            

        if(center_point_type == USER_LOCATION) :
            geocoding_index  =   self.GeocodeWidgets_stack_dict.get(DISPLAY_GEOCODE_CENTER_POINT_RESULTS)
        else :
            geocoding_index  =   self.GeocodeWidgets_stack_dict.get(DISPLAY_GEOCODE_DF_CENTER_POINT_RESULTS)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_center_point_data]  index : ",geocoding_index)
        
        if(geocoding_index is None) :

            try :

                from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import Geoocoder_Center_Point_Results_Widget
                parms   =   [self,center_point_type,geopoints,center_point]

                if(center_point_type == USER_LOCATION) :
                    self.geocode_center_point_results           =   Geoocoder_Center_Point_Results_Widget(parms)
                else :
                     self.geocode_df_center_point_results       =   Geoocoder_Center_Point_Results_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_geocoding_center_point_data] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.GeocodeWidgets_stack_dict)
                if(center_point_type == USER_LOCATION) :
                    self.GeocodeWidgets_stack_dict.update({DISPLAY_GEOCODE_CENTER_POINT_RESULTS : current_index})
                else :
                    self.GeocodeWidgets_stack_dict.update({DISPLAY_GEOCODE_DF_CENTER_POINT_RESULTS : current_index})
                
                if(center_point_type == USER_LOCATION) : 
                    self.stackedLayout.addWidget(self.geocode_center_point_results)
                else :
                    self.stackedLayout.addWidget(self.geocode_df_center_point_results)

        else :

            if(DEBUG_GEOCODE) :
                print("[GeocodeGui][display_geocoding_center_point_data] reload_data:  ",geocoding_index)

            if(center_point_type == USER_LOCATION) :
                self.geocode_center_point_results.reload_data(self,center_point_type,geopoints,center_point)
            else :
                self.geocode_df_center_point_results.reload_data(self,center_point_type,geopoints,center_point)

            current_index   =   geocoding_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_center_point_data] end : stack \n  ",self.GeocodeWidgets_stack_dict)

        if(center_point_type == USER_LOCATION) :
            self.resize(1070,600)
        else :
            self.resize(1070,480)


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

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import USER_LOCATION
        if(ptsource == USER_LOCATION) :
            geocoding_index  =   self.GeocodeWidgets_stack_dict.get(DISPLAY_CENTER_POINT)
        else :
            geocoding_index  =   self.GeocodeWidgets_stack_dict.get(DISPLAY_DF_CENTER_POINT)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_center_point]  index : ",geocoding_index)
        
        if(geocoding_index is None) :

            try :

                if(ptsource == USER_LOCATION) :

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

                if(ptsource == USER_LOCATION) :

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

        if(ptsource == USER_LOCATION) :
            self.resize(1070,750)
        else :
            self.resize(1070,600)

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

        from dfcleanser.Qt.utils.Geocode.GeocodeModel import USER_LOCATION, DF_CENTER_POINT_LOCATION, CENTER_POINT_LIST_LOCATION 
        if(fixedpt_type == USER_LOCATION) :
            geocoding_index  =   self.GeocodeWidgets_stack_dict.get(DISPLAY_DF_DISTANCE_FROM_LOCATION)
        if(fixedpt_type == DF_CENTER_POINT_LOCATION) :
            geocoding_index  =   self.GeocodeWidgets_stack_dict.get(DISPLAY_DF_DISTANCE_FROM_CENTER_PT)
        else :
            geocoding_index  =   self.GeocodeWidgets_stack_dict.get(DISPLAY_GEOCODE_LIST_POINT_RESULTS)

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
                
                elif(fixedpt_type == DISPLAY_DF_DISTANCE_FROM_CENTER_PT) :

                    from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import Geocode_Distance_From_Center_Point_Widget
                    parms   =   [self]
                    self.geocode_distance_center_pt_utility      =   Geocode_Distance_From_Center_Point_Widget(parms)

                else :

                    from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import Geocode_Distance_From_Closest_Point_Widget
                    parms   =   [self]
                    self.geocode_distance_closest_pt_utility      =   Geocode_Distance_From_Closest_Point_Widget(parms)

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

                elif(fixedpt_type == DISPLAY_DF_DISTANCE_FROM_CENTER_PT) :

                    current_index   =  len(self.GeocodeWidgets_stack_dict)
                    self.GeocodeWidgets_stack_dict.update({DISPLAY_DF_DISTANCE_FROM_CENTER_PT : current_index})
                    self.stackedLayout.addWidget(self.geocode_distance_center_pt_utility)

                else :

                    current_index   =  len(self.GeocodeWidgets_stack_dict)
                    self.GeocodeWidgets_stack_dict.update({DISPLAY_GEOCODE_LIST_POINT_RESULTS : current_index})
                    self.stackedLayout.addWidget(self.geocode_distance_closest_pt_utility)

        else :

            if(DEBUG_GEOCODE) :
                print("[GeocodeGui][display_geocoding_distance_from_fixed_location] reload_data:  ",geocoding_index)

            current_index   =   geocoding_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_distance_from_fixed_location] end : stack \n  ",self.GeocodeWidgets_stack_dict)

        if(fixedpt_type == USER_LOCATION) :
            self.resize(1070,850)
        elif(fixedpt_type == CENTER_POINT_LIST_LOCATION) :
            self.resize(1070,950)
        else :
            self.resize(1070,1050)


    # -----------------------------------------------------------------#
    # -                Display Geocoding Split Utility                -#
    # -----------------------------------------------------------------#

    def display_geocoding_split(self):

        if(DEBUG_GEOCODE) :
            print("\n[GeocodeGui][display_geocoding_split]")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        geocoding_index  =   self.GeocodeWidgets_stack_dict.get(DISPLAY_SPLIT_COLUMN)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_split]  index : ",geocoding_index)
        
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

                from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import Geocode_Split_Column_Widget
                parms   =   [self]
                self.geocode_split_column      =   Geocode_Split_Column_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_geocoding_split] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.GeocodeWidgets_stack_dict)
                self.GeocodeWidgets_stack_dict.update({DISPLAY_SPLIT_COLUMN : current_index})
                self.stackedLayout.addWidget(self.geocode_split_column)

        else :

            if(DEBUG_GEOCODE) :
                print("[GeocodeGui][display_geocoding_split] reload_data:  ",geocoding_index)

            current_index   =   geocoding_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_split] end : stack \n  ",self.GeocodeWidgets_stack_dict)

        self.resize(1070,700)

    # -----------------------------------------------------------------#
    # -                Display Geocoding Join Utility                 -#
    # -----------------------------------------------------------------#

    def display_geocoding_join(self):

        if(DEBUG_GEOCODE) :
            print("\n[GeocodeGui][display_geocoding_join]")

        from dfcleanser.common.common_utils import opStatus
        opstat      =   opStatus()

        geocoding_index  =   self.GeocodeWidgets_stack_dict.get(DISPLAY_JOIN_COLUMNS)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_join]  index : ",geocoding_index)
        
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

                from dfcleanser.Qt.utils.Geocode.GeocodeWidgets import Geocode_Join_Columns_Widget
                parms   =   [self]
                self.geocode_join_column      =   Geocode_Join_Columns_Widget(parms)

            except Exception as e:

                opstat.set_status(False)
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[display_geocoding_join] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            if(opstat.get_status()) :

                current_index   =  len(self.GeocodeWidgets_stack_dict)
                self.GeocodeWidgets_stack_dict.update({DISPLAY_JOIN_COLUMNS : current_index})
                self.stackedLayout.addWidget(self.geocode_join_column)

        else :

            if(DEBUG_GEOCODE) :
                print("[GeocodeGui][display_geocoding_join] reload_data:  ",geocoding_index)

            current_index   =   geocoding_index

        self.stackedLayout.setCurrentIndex(current_index)

        if(DEBUG_GEOCODE) :
            print("[GeocodeGui][display_geocoding_join] end : stack \n  ",self.GeocodeWidgets_stack_dict)

        self.resize(1070,750)




# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                Global access to Geocode Chapter               -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def clearGeocode()  :

    from dfcleanser.common.common_utils import clear_screen
    
    clear_screen()

    from dfcleanser.common.cfg import dfc_qt_chapters, GEOCODE_QT_CHAPTER_ID
    num_instances   =   dfc_qt_chapters.get_qt_chapters_count(GEOCODE_QT_CHAPTER_ID)

    if(num_instances > 0) :
        instances       =   dfc_qt_chapters.get_qt_chapters(GEOCODE_QT_CHAPTER_ID)
        for i in range(len(instances)) :
            instances[i].get_main_window().init_geocode_form()

    clear_screen()

def closeGeocodeInstances()  :
    
    from dfcleanser.common.cfg import dfc_qt_chapters, GEOCODE_QT_CHAPTER_ID
    num_instances   =   dfc_qt_chapters.get_qt_chapters_count(GEOCODE_QT_CHAPTER_ID)

    if(num_instances > 0) :
        instances       =   dfc_qt_chapters.get_qt_chapters(GEOCODE_QT_CHAPTER_ID)
        for i in range(len(instances)) :
            instances[i].get_main_window().close()

    from dfcleanser.common.common_utils import clear_screen
    
    clear_screen()
    logger.info(" Geocode Utility Instances closed")

def showGeocode()  :

    from dfcleanser.common.common_utils import displayHTML,clear_screen
    from dfcleanser.common.cfg import dfc_qt_chapters, GEOCODE_QT_CHAPTER_ID, GEOCODE_TITLE
    
    clear_screen()
    
    gecode_gui = GeocodeGui()
    gecode_gui.show()

    dfc_qt_chapters.add_qt_chapter(GEOCODE_QT_CHAPTER_ID,gecode_gui,"showGeocode")

    total_instances     =   dfc_qt_chapters.get_qt_chapters_count(GEOCODE_QT_CHAPTER_ID)
    logger.info(str(total_instances) + " Geocode Utility Instances Loaded")


def closeGeocodeChapter()  :

    closeGeocodeInstances()

    from dfcleanser.common.cfg import run_javascript
    run_javascript("delete_dfc_cell('DCGeocodeUtility')","unable to delete Geocode : ")    

