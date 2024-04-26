"""
# InspectRows
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:29:22 2017

@author: Rick
"""

#from cgi import parse_multipart
from email.headerregistry import Address
import sys
this = sys.modules[__name__]


import inspect
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStackedWidget

from PyQt5.QtCore import Qt
from PyQt5 import uic

from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont


import dfcleanser.common.cfg as cfg 

DEBUG_INSPECT_ROWS              =   False
DEBUG_INSPECT_ROWS_DETAILS      =   False

DEFAULT_ROW_HEIGHT  =   30

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -           dcommon dfcleanser qt header styles                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

def fix_ipython():
    from IPython import get_ipython
    ipython = get_ipython()
    if ipython is not None:
        ipython.magic("gui qt5")


import logging
logger = logging.getLogger(__name__)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

# Set the exception hook to our wrapping function
sys.excepthook = except_hook

# Enables PyQt event loop in IPython
fix_ipython()


# -----------------------------------------------------------------#
# -    Subclass of QMainWindow to disp[lay the columns uniques    -#
# -----------------------------------------------------------------#
class InspectRowsGui(QtWidgets.QMainWindow):

    def __init__(self, dfparms, **kwargs):  

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

        self.df                 =   None
        self.start_row          =   0

        self.form               =   None
        self.stackedLayout      =   None

        if(DEBUG_INSPECT_ROWS) :
            print("[InspectRowsGui]  dfparms ",dfparms)

        if(not(dfparms is None)) :
            self.dftitle            =   dfparms[0]

            from dfcleanser.common.cfg import get_dfc_dataframe_df 
            df          =   get_dfc_dataframe_df(self.dftitle)

            if(not (df is None)) :
                self.df     =   df
            else :
                self.df     =   None

                title       =   "dfcleanser error"       
                status_msg  =   "No dfc dataframe defined"
                from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                display_error_msg(title,status_msg)

                return(None)

        self.data_inspection_widgets_stack_dict     =   {}

        # enable custom window hint
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)

        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)

 
        # general housekeeping
        self.caller_stack   = inspect.currentframe().f_back
        self.stacked_widget = QStackedWidget(None)

        self.init_gui()

        self.form.dfRowsLayout.addLayout(self.stackedLayout)
        self.form.dfRowsLayout.addStretch()

        self.resize(1000,1200)

    def update(self):   
        self.update()

    
    # -----------------------------------------------------------------#
    # -                     Initialize the gui                        -#
    # -----------------------------------------------------------------#
        
    def init_gui(self):

        # set up the ui form from a qtdesigner ui
        cfgdir  = cfg.DataframeCleanserCfgData.get_dfc_qt_dir_name()
        ui_name = cfgdir +"\data_inspection\InspectRowsUI.ui"
        Form, Window = uic.loadUiType(ui_name)
        self.form = Form()
        self.form.setupUi(self)

        from PyQt5.QtWidgets import QStackedLayout
        self.stackedLayout = QStackedLayout()
       
        # -----------------------------------------------------#
        #     common window attribute settings     #
        # -----------------------------------------------------#
        
        # set common window attributes
        self.setWindowTitle("dfcleanser - df Browser")
        
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
        self.init_data_inspect_df_rows_form()
           

    # -----------------------------------------------------------------#
    # -                 Initialize chapter buttons                    -#
    # -----------------------------------------------------------------#
    def init_data_inspect_df_rows_buttons(self):

        if(DEBUG_INSPECT_ROWS) :
            print("  [InspectRowsGui][init_data_inspect_df_rows_buttons]  ")

        from dfcleanser.sw_utilities.dfc_qt_model import init_dfc_buttons, set_dfc_buttons_style

        buttons     =   [self.form.dfRowsBrowsedfbutton,self.form.dfRowsScrollDownbutton, self.form.dfRowsScrollUpbutton, self.form.dfRowsTopbutton, 
                         self.form.dfRowsFindNextbutton, self.form.dfRowsHelpbutton]
        
        # init buttons for usage
        Inspect_Button_Style    =   "background-color:#0c4ca7; color:white; font : Arial; font-weight : bold; font-size : 13px;"
        init_dfc_buttons(buttons,Inspect_Button_Style)

        # set button styles
        #set_dfc_buttons_style(buttons,Inspect_Button_Style)
        
        # adding action to a button
        self.form.dfRowsBrowsedfbutton.clicked.connect(self.Browsedf)
        self.form.dfRowsScrollDownbutton.clicked.connect(self.ScrolldfDown)
        self.form.dfRowsScrollUpbutton.clicked.connect(self.ScrolldfUp)  
        self.form.dfRowsTopbutton.clicked.connect(self.ScrolldfTop)  
        self.form.dfRowsFindNextbutton.clicked.connect(self.FindNextValue)
        self.form.dfRowsHelpbutton.clicked.connect(self.dfRowsHelp)  

    # -----------------------------------------------------------------#
    # -            Initialize the chapter splah image                 -#
    # -----------------------------------------------------------------#
    def init_data_inspect_df_rows_splash_screen(self):

        if(DEBUG_INSPECT_ROWS) :
            print("  [InspectRowsGui][init_data_inspect_df_rows_splash_screen]  ")

        from dfcleanser.sw_utilities.dfc_qt_model import build_chapter_splash_screen
        from dfcleanser.common.cfg import dfBrowserUtility_ID
        build_chapter_splash_screen(dfBrowserUtility_ID, self.form.dfRowsSplashScreen)

        if(DEBUG_INSPECT_ROWS) :
            print("  [InspectRowsGui][init_data_inspect_df_rows_splash_screen]  end")


    # -----------------------------------------------------------------#
    # -             Initialize the dfs select form                    -#
    # -----------------------------------------------------------------#
    def init_inspect_df_rows_form(self):#, DataInspectionLayout):

        if(DEBUG_INSPECT_ROWS) :
            print("  [InspectRowsGui][init_dfs_to_inspect_df_row]  ")

        from dfcleanser.sw_utilities.dfc_qt_model import build_select_dfs_layout
        dfc_dfs_objects     =   build_select_dfs_layout("* dataframes_to_inspect")

        dfc_dfs_combo_box   =   dfc_dfs_objects[0]
        dfc_dfs_layout      =   dfc_dfs_objects[1]

        self.df_select      =   dfc_dfs_combo_box
        
        if(self.dftitle is None) :
            self.df_select.setCurrentIndex(0)
        else :
            index = dfc_dfs_combo_box.findText(self.dftitle)
            self.df_select.setCurrentIndex(index)

        self.dftitle    =   self.df_select.currentText()
        from dfcleanser.common.cfg import get_dfc_dataframe_df 
        df          =   get_dfc_dataframe_df(self.dftitle)

        if(not (df is None)) :
            self.df     =   df
        else :
            self.df     =   None

        self.df_select.currentIndexChanged.connect(self.change_df)

        self.dfc_dfs_layout =   dfc_dfs_layout
        self.dfc_dfs_layout.addStretch()

        if(DEBUG_INSPECT_ROWS_DETAILS) :
            print("  [InspectRowsGui][init_dfs_to_inspect_df_rows]  ",dfc_dfs_objects)

        if(not(self.df is None)) :

            from PyQt5.QtWidgets import QLabel
            self.title_label   =   QLabel()

            title_text  =   ("\ndf : " + str(self.dftitle) + "    Total Rows : " + str(len(self.df)) + "    Total Columns : " + str(len(self.df.columns.tolist())) + "\n")
            self.title_label.setText(title_text)
            self.title_label.setAlignment(Qt.AlignLeft)
            self.title_label.resize(600,50)
            self.title_label.setStyleSheet("font-size: 14px; font-weight: bold; font-family: Arial; ")
 
            parms           =   [self.df,self.start_row]
            self.df_rows    =   DataInspectiondfRowsTable(parms)

        from PyQt5.QtWidgets import QVBoxLayout

        dfrowsLayout     =   QVBoxLayout()
        dfrowsLayout.addLayout(self.dfc_dfs_layout)

        if(not(self.df is None)) :
            dfrowsLayout.addWidget(self.title_label)
            dfrowsLayout.addWidget(self.df_rows)
           
        dfrowsLayout.addStretch()
        
        from PyQt5.QtWidgets import QWidget
        self.dfrows_input     =   QWidget()
        self.dfrows_input.setLayout(dfrowsLayout)

        DFS_SELECT      =   "Inspect df rows"

        from dfcleanser.Qt.data_inspection.DataInspectionModel import dfc_df_browsers
        df_browsers     =   dfc_df_browsers.get_df_browsers()

        if(self.dftitle in df_browsers) :

            current_index   =   dfc_df_browsers.get_df_browser(self.dftitle)

            if(current_index is None) :

                dfc_df_browsers.pop_df_browser(self.dftitle) 

                current_index   =  len(self.data_inspection_widgets_stack_dict)
                new_index       =  DFS_SELECT + str(len(df_browsers) + 1)
                self.data_inspection_widgets_stack_dict.update({(new_index): current_index})
                self.stackedLayout.addWidget(self.dfrows_input)
                dfc_df_browsers.add_df_browser(self.dftitle,current_index)

        else :

            current_index   =  len(self.data_inspection_widgets_stack_dict)
            new_index       =  DFS_SELECT + str(len(df_browsers) + 1)
            self.data_inspection_widgets_stack_dict.update({(new_index): current_index})
            self.stackedLayout.addWidget(self.dfrows_input)
            dfc_df_browsers.add_df_browser(self.dftitle,current_index)

        self.stackedLayout.setCurrentIndex(current_index)
 
        if(DEBUG_INSPECT_ROWS) :
            print("  [InspectRowsGui][init_dfs_to_inspect_df_rows] end",self.data_inspection_widgets_stack_dict)


    # -----------------------------------------------------------------#
    # -                 Initialize the gui form                       -#
    # -----------------------------------------------------------------#
    def init_data_inspect_df_rows_form(self):
        
        if(DEBUG_INSPECT_ROWS) :
            print("[InspectRowsGui][init_data_inspect_df_rows_form]  ")

        self.init_data_inspect_df_rows_buttons()
        self.init_data_inspect_df_rows_splash_screen()
        self.init_inspect_df_rows_form()

        self.setFixedSize(1200,950)

        if(DEBUG_INSPECT_ROWS) :
            print("[InspectRowsGui][init_data_inspect_df_rows_form]  end")

        
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -              Data Inspection action methods                   -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#

    def change_df(self) :

        if(DEBUG_INSPECT_ROWS) :
            print("[InspectRowsGui][change_df]  ")

        self.dftitle    =   self.df_select.currentText()
        from dfcleanser.common.cfg import get_dfc_dataframe_df 
        self.df          =   get_dfc_dataframe_df(self.dftitle)


    def ScrolldfDown(self) :

        self.form.dfRowsScrollDownbutton.toggle()

        if(DEBUG_INSPECT_ROWS) :
            print("[InspectRowsGui][ScrolldfDown]  ")

        self.start_row  =   self.start_row + 200
        if(self.start_row <= len(self.df)) :
            self.df_rows.reload_data(self.df,self.start_row)
    
    def Browsedf(self) :

        self.form.dfRowsBrowsedfbutton.toggle()

        if(DEBUG_INSPECT_ROWS) :
            print("[InspectRowsGui][Browsedf]  ",self.dftitle)

        title_text  =   ("\ndf : " + str(self.dftitle) + "    Total Rows : " + str(len(self.df)) + "    Total Columns : " + str(len(self.df.columns.tolist())) + "\n")
        self.title_label.setText(title_text)

        self.start_row  =   self.start_row - 200
        if(self.start_row < 0) : self.start_row  =   0
        if(self.start_row <= len(self.df)) :
            self.df_rows.reload_data(self.df,self.start_row)
   
    def ScrolldfUp(self) :

        self.form.dfRowsScrollUpbutton.toggle()

        if(DEBUG_INSPECT_ROWS) :
            print("[InspectRowsGui][ScrolldfUp]  ")

        self.start_row  =   self.start_row - 200
        if(self.start_row < 0) : slf.start_row  =   0
        if(self.start_row <= len(self.df)) :
            self.df_rows.reload_data(self.df,self.start_row)

    def ScrolldfTop(self) :
        
        self.form.dfRowsTopbutton.toggle()

        if(DEBUG_INSPECT_ROWS) :
            print("[InspectRowsGui][ScrolldfTop]  ")

        self.start_row  =   0
        self.df_rows.reload_data(self.df,self.start_row)

    def FindNextValue(self) :
        
        self.form.dfRowsFindNextbutton.toggle()

        if(DEBUG_INSPECT_ROWS) :
            print("[InspectRowsGui][FindNextValue]")

        row_number      =   None
        column_number   =   None

        for idx in self.df_rows.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_INSPECT_ROWS) :
            print("  [InspectRowsGui][select_column_to_cleanse] ",row_number," ",column_number)


        if(column_number is None) :

            title       =   "dfcleanser error"       
            status_msg  =   "No column selected to find next value in"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

        else :

            valueToFind, done1 = QtWidgets.QInputDialog.getText(self, 'Find df Column Value', 'Enter the next value to find :')

            if(done1) :

                if(DEBUG_INSPECT_ROWS) :
                    print("  [InspectRowsGui][select_column_to_cleanse] ",valueToFind)

    def FilterdfRows(self) :
        
        self.form.FilterdfRowsbutton.toggle()

        if(DEBUG_INSPECT_ROWS) :
            print("[InspectRowsGui][FilterdfRows]")

    def dfRowsHelp(self) :
        
        self.form.dfRowsHelpbutton.toggle()

        if(DEBUG_INSPECT_ROWS) :
            print("[InspectRowsGui][dfRowsHelp]")



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -               DataInspection df Rows Objects                  -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -                   Table Model for df rows                     -#
# -----------------------------------------------------------------#

green_color     =   QColor(173, 236, 196)
yellow_color    =   QColor(250, 246, 190)
red_color       =   QColor(241, 196, 183) 

class DataInspectiondfRowsModel(QtCore.QAbstractTableModel):
    def __init__(self, statsdata, col_headers):

        super(DataInspectiondfRowsModel, self).__init__()

        self._data = statsdata
        self.col_headers = col_headers

        #print("[DataInspectiondfRowsModel] : self.col_headers \n   ",self.col_headers)

    def reload_data(self,statsdata) :
        self._data = statsdata

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
            if(column == 0) :
                return(Qt.AlignLeft)
            else :
                return(Qt.AlignCenter)

        if role==Qt.BackgroundColorRole:
            if(column == 0) :
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
# -               Subclass of QMainWindow to df rows              -#
# -----------------------------------------------------------------#
class DataInspectiondfRowsTable(QtWidgets.QTableView):

    def __init__(self, dfparms, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.df                 =   dfparms[0]
        self.start_row          =   dfparms[1]

        self.column_headers     =   []
        self.column_widths      =   []

        if(DEBUG_INSPECT_ROWS) :
            print("    [DataInspectiondfRowsTable] : init : start_row : ",self.start_row)

        self.init_tableview()

        if(DEBUG_INSPECT_ROWS) :
            print("    [DataInspectiondfRowsTable] : done")

    
    def reload_data(self,df,start_row) :

        if(DEBUG_INSPECT_ROWS) :
            print("    [DataInspectiondfRowsTable][reload_data] : start_row : ",start_row)

        self.df                 =   df
        self.start_row          =   start_row

        reload_data     =   self.load_df_rows_data()
        self.model.reload_data(reload_data)        


    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(DEBUG_INSPECT_ROWS) :
            print("    [DataInspectiondfRowsTable][reload_data] : init_tableview")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        dfdata     =   self.load_df_rows_data()

        if(self.model is None) :
            self.model = DataInspectiondfRowsModel(dfdata, self.column_headers)
            self.setModel(self.model)

        if(DEBUG_INSPECT_ROWS) :
           print("    [DataInspectiondfRowsTable] : model loaded",len(dfdata))

        self.num_rows   =   len(dfdata)

        num_rows_limit  =   20

        self.setMinimumHeight(600)

        if(DEBUG_INSPECT_ROWS) :
           print("    [DataInspectiondfRowsTable] : num rows",self.num_rows)


        #----------------------------------------------#
        # init the table view header and cell sizes    #
        #----------------------------------------------#
        
        # set default tableview font
        tablefont   =  QFont("Times",8) 
        tablefont.setBold(False)
        self.setFont(tablefont)

        # set table view header
        header = self.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignHCenter)
        header.setFixedHeight(40)
        header.setStyleSheet("background-color:#0c4ca7; color:white; font : Arial; font-weight : bold; font-size : 10px;")

        # set the row heights
        nrows = len(dfdata)
        for row in range(nrows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(self.column_widths)) :
           self.setColumnWidth(i, self.column_widths[i])     
        
        self.setWordWrap(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)


    # -----------------------------------------------------------------#
    # -                 Initialize the table data                     -#
    # -----------------------------------------------------------------#
    def load_df_rows_data(self):

        if(DEBUG_INSPECT_ROWS) :
            print("    [DataInspectiondfRowsTable] : load_df_rows_data ")

        df_cols         =   self.df.columns.tolist()
        
        if(DEBUG_INSPECT_ROWS) :
            print("    [DataInspectiondfRowsTable] : df_cols ",df_cols)

        header_names    =   ["Row\nId"]
        header_widths   =   [20]

        for i in range(len(df_cols)):

            from dfcleanser.common.common_utils import is_numeric_col
            if(is_numeric_col(self.df,[df_cols[i]])) :
                header_widths.append(45)
            else :
                header_widths.append(70)

            current_header  =   df_cols[i]
            first_blank     =   current_header.find(" ")
            if(first_blank > -1) :
                new_col_name    =   current_header[:(first_blank)] + "\n" + current_header[(first_blank+1):]
                header_names.append(new_col_name)
            else :
                header_names.append(df_cols[i])

        data    =   []

        rows_displayed  =   len(self.df)
        if(rows_displayed > 200) :
            rows_displayed   =   200

        for i in range(rows_displayed) :

            cindex  =  self.start_row + i 

            data_row =  [str(cindex)]

            for j in range(len(df_cols)) :
                from dfcleanser.common.common_utils import is_numeric_col
                if(1):#is_numeric_col(self.df,[df_cols[j]])) :
                    data_row.append(str(self.df.iloc[cindex,j]))
                else :
                    data_row.append(self.df.iloc[cindex,j])

            data.append(data_row)


        self.column_headers     =   header_names
        self.column_widths      =   header_widths

        if(len(self.column_widths) < 15) :

            cwidth  =   1100 / (len(self.column_widths)-1)
            import math
            cwidth  =   int(math.floor(cwidth))
            new_column_widths   =   []
            new_column_widths.append(20)
            for k in range((len(self.column_widths)-1)) :
                 new_column_widths.append(cwidth)   

            self.column_widths  =   new_column_widths

        self.num_rows           =   len(data)

        if(DEBUG_INSPECT_ROWS_DETAILS) :
            print("    [DataInspectiondfRowsTable] : header_names\n   ",self.column_headers)
            print("    [DataInspectiondfRowsTable] : self.column_widths\n   ",self.column_widths)

        if(DEBUG_INSPECT_ROWS) :
            print("    [DataInspectiondfRowsTable] : load_df_rows_data : end")

        return(data)




# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                   Global access to df Browser                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def clearDfBrowser()  :

    from dfcleanser.common.common_utils import displayHTML,clear_screen
    from dfcleanser.common.cfg import DF_BROWSER_TITLE
    
    clear_screen()
    displayHTML(DF_BROWSER_TITLE)


def closeDfBrowserInstances()  :
    
    from dfcleanser.common.cfg import dfc_qt_chapters, DF_BROWSER_QT_CHAPTER_ID
    num_instances   =   dfc_qt_chapters.get_qt_chapters_count(DF_BROWSER_QT_CHAPTER_ID)

    if(num_instances > 0) :
        instances       =   dfc_qt_chapters.get_qt_chapters(DF_BROWSER_QT_CHAPTER_ID)
        for i in range(len(instances)) :
            instances[i].get_main_window().close()

    from dfcleanser.common.common_utils import displayHTML,clear_screen
    from dfcleanser.common.cfg import DF_BROWSER_TITLE
    
    clear_screen()
    displayHTML(DF_BROWSER_TITLE)


def showDfBrowser(df_title)  :

    from dfcleanser.common.common_utils import displayHTML,clear_screen
    from dfcleanser.common.cfg import dfc_qt_chapters, DF_BROWSER_QT_CHAPTER_ID, DF_BROWSER_TITLE
    
    clear_screen()
 
    logger.info("Opening DfBrowser GUI")

    dfbrowser_gui = InspectRowsGui([df_title])
    dfbrowser_gui.show()

    dfc_qt_chapters.add_qt_chapter(DF_BROWSER_QT_CHAPTER_ID,dfbrowser_gui,"showDfBrowser")

    total_instances     =   dfc_qt_chapters.get_qt_chapters_count(DF_BROWSER_QT_CHAPTER_ID)
    logger.info(str(total_instances) + " df Browser Instances Loaded")

    return dfbrowser_gui  

def closeDfBrowserChapter()  :

    closeDfBrowserInstances()

    from dfcleanser.common.cfg import run_javascript
    run_javascript("delete_dfc_cell('DCDfBrowser')","unable to delete df browser : ")    










