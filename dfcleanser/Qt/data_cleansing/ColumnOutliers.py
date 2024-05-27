"""
# ColumnOutliers
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
from PyQt5.QtWidgets import QStackedWidget

from PyQt5.QtCore import Qt
from PyQt5 import uic

from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont


import dfcleanser.common.cfg as cfg 

from dfcleanser.Qt.system.SystemModel import is_debug_on
from dfcleanser.common.cfg import DataCleansing_ID

import logging
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -           dcommon dfcleanser qt header styles                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


common_qt_header_background_color   =   "#428bca"
common_qt_header_font_size          =   "12px"
common_qt_header_font_weight        =   "bold"
common_qt_header_font_style         =   "normal"
common_qt_header_font_family        =   "Tahoma"

common_qt_header_style_element      =   "background-color: " + common_qt_header_background_color + "; " + "font-size: " + common_qt_header_font_size + "; " +"font-weight: " + common_qt_header_font_weight + "; " + "font-style: " + common_qt_header_font_style + "; " + "font-family: " + common_qt_header_font_family + ";  " + "margin-left: 0px; "

def fix_ipython():
    from IPython import get_ipython
    ipython = get_ipython()
    if ipython is not None:
        ipython.magic("gui qt5")

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

# Set the exception hook to our wrapping function
sys.excepthook = except_hook

# Enables PyQt event loop in IPython
fix_ipython()

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -           dfcleanser column uniques qt objects                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

DEFAULT_COLUMN_WIDTHS                   =   [100,140,140,420]
        
DIALOG_GEOMETRY                         =   [0,0,900,550]

OUTLIERS_TABLEVIEW_LABEL_GEOMETRY       =   [40,30,802,30]
OUTLIERS_TABLEVIEW_GEOMETRY             =   [40,60,802,425]

OUTLIERS_STATS_LABEL_GEOMETRY           =   [330,490,220,40]


DEFAULT_TABLEVIEW_HEIGHT                =   OUTLIERS_TABLEVIEW_GEOMETRY[3]
DEFAULT_NUM_ROWS                        =   20
DEFAULT_ROW_HEIGHT                      =   20

FIXED_HEADER_HEIGHT                     =   26


# -----------------------------------------------------------------#
# -     Table Model for unique values table view      -#
# -----------------------------------------------------------------#
class OutliersTableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):

        super(OutliersTableModel, self).__init__()
        self._data = data

    def reload_data(self,data) :
        self._data = data

        self.layoutAboutToBeChanged.emit()
        self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0)))
        self.layoutChanged.emit()
 
    def get_data(self) :
        return(self._data)
    
    def save_bgcolors(self,bgcolors) :
        self.outliers_bgcolors  =   bgcolors

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
            #if(column == 3) :
            return(Qt.AlignLeft)
            #else :
            #    return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:
            # get colors from data set
            return(self.outliers_bgcolors[row])

                
    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            odd = (section % 2) 
            if(section == 0) :
                return('Std Devs')
            elif(section == 1) :
                return('Count')
            elif(section == 2) :
                return('% Total')
            else :
                return("Values Range")
        return super().headerData(section, orientation, role)


# -----------------------------------------------------------------#
# -    Subclass of QMainWindow to disp[lay the columns uniques    -#
# -----------------------------------------------------------------#
class OutliersGui(QtWidgets.QMainWindow):

    #def __init__(self):
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

        self.df                 =   None
        self.dftitle            =   dfparms[0]
        self.colname            =   dfparms[1]
        self.mean               =   dfparms[2]
        self.std                =   dfparms[3]
        self.outliers_data      =   dfparms[4]

        self.rows_to_display    =   0

        self.form               =   None
        self.model              =   None

        self.caller_stack   = inspect.currentframe().f_back
        self.stacked_widget = QStackedWidget(None)

        # enable custom window hint
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)

        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)


        self.init_gui()

    def update(self):   
        self.update()

    # dump the cirrent form geometry
    def dump_geometry(self) :

        # dump the form geometries
        
        add_debug_to_log("dump_geometry",print_to_string("OutliersTablelabel : ",self.form.OutliersTablelabel.geometry()))
        add_debug_to_log("dump_geometry",print_to_string("OutliersTableView : ",self.form.OutliersTableView.geometry()))
        add_debug_to_log("dump_geometry",print_to_string("OutliersStatslabel : ",self.form.StdDevDef.geometry()))

    
    # -----------------------------------------------------------------#
    # -                     Initialize the gui                        -#
    # -----------------------------------------------------------------#
        
    def init_gui(self):
        
        # set up the ui form from a qtdesigner ui
        cfgdir  = cfg.DataframeCleanserCfgData.get_dfc_qt_dir_name()
        ui_name = cfgdir +"\data_cleansing\ColumnOutliersUI.ui"
        Form, Window = uic.loadUiType(ui_name)
        self.form = Form()
        self.form.setupUi(self)
        
        # -----------------------------------------------------#
        #     common window attribute settings     #
        # -----------------------------------------------------#
        
        # set common window attributes
        self.setWindowTitle("dfcleanser Column Outliers")
        
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
        iconi_name  =   dfcdir +"\dfcicon.png"
        self.app.setWindowIcon(QtGui.QIcon(iconi_name))

        # Hide the question mark on dialogs
        self.app.setAttribute(Qt.AA_DisableWindowContextHelpButton) 
        
        # set overall app style
        self.app.setStyle('Fusion')      

        # -----------------------------------------------------#
        #            common window widgets             #
        # -----------------------------------------------------#

        # Status bar
        self.setStatusBar(QtWidgets.QStatusBar())
        
        # init the gui form
        self.init_outliers_form()


    # -----------------------------------------------------------------#
    # -                 Initialize the form widgets                   -#
    # -----------------------------------------------------------------#
    def adjust_table_view(self):

        OutliersTableView = self.form.OutliersTableView

        dead_space  =   0

        num_data_rows   =   0
        for i in range(len(self.outliers_data)) :
            if(not (self.outliers_data[i] == 0)) :
                num_data_rows   =   num_data_rows + 1

        new_height  =   ((num_data_rows) * DEFAULT_ROW_HEIGHT) + FIXED_HEADER_HEIGHT + 2
            
        OutliersTableView.setMinimumHeight(new_height)
        OutliersTableView.setMaximumHeight(new_height)

        dead_space  =   DEFAULT_TABLEVIEW_HEIGHT - new_height
            
        return(dead_space)


    # -----------------------------------------------------------------#
    # -                 Initialize the form widgets                   -#
    # -----------------------------------------------------------------#
    def adjust_form_widgets(self,dead_space):

        if(dead_space > 0) :

            new_geometry        =   OUTLIERS_STATS_LABEL_GEOMETRY.copy()
            new_geometry[1]     =   (new_geometry[1] - dead_space)
            self.form.StdDevDef.move(new_geometry[0],new_geometry[1])

            dialog_height       =   DIALOG_GEOMETRY[3] - dead_space

            self.resize(DIALOG_GEOMETRY[2],dialog_height)
            
        if(DEBUG_COUTLIERS) :
            self.dump_geometry()


    # -----------------------------------------------------------------#
    # -                 Initialize the gui form                       -#
    # -----------------------------------------------------------------#
    def init_outliers_form(self):

        if(is_debug_on(DataCleansing_ID,"DEBUG_CLEANSING_DETAILS")) : :
            self.dump_geometry()

        # init the tableview title
        self.form.OutliersTablelabel.setText("  df '" + self.dftitle + "' : Column '" + self.colname + "'" + " Simple Outliers")
        self.form.OutliersTablelabel.setStyleSheet("background-color:#3399ff; color: white; font-size: 16px; font-weight: bold; font-style: normal; font-family: Arial;  margin-left: 0px; ") 
        
        stddev   =   0
        # init the tableview footer
        self.form.StdDevDef.setText("Standard Deviation = " + "{0:.2f}".format(self.std))
        self.form.StdDevDef.setStyleSheet("font-size: 12px; font-weight: bold; font-style: normal; font-family: Arial;  margin-left: 0px; ") 

        #----------------------------#
        # init the tableview widget  #
        #----------------------------#
        
        # grab the tableview form
        OutliersTableView = self.form.OutliersTableView

        [bgcolors,data]     =   self.load_model_data(self.outliers_data)
        num_data_rows       =   len(data)

        if(DEBUG_COUTLIERS) :
            add_debug_to_log("init_outliers_form",print_to_string(" num_data_rows : ",num_data_rows))

        # adjust the height of the tableview
        dead_space  =   self.adjust_table_view()

        #----------------------------------------------#
        # adjust form widgets based on tableview size  #
        #----------------------------------------------#

        self.adjust_form_widgets(dead_space)

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        if(self.model is None) :
            self.model = OutliersTableModel(data)
            OutliersTableView.setModel(self.model)
            self.model.save_bgcolors(bgcolors)

        #----------------------------------------------#
        # init the table view header and cell sizes    #
        #----------------------------------------------#
        
        # set default tableview font
        tablefont   =  QFont("Times",10) 
        tablefont.setBold(False)
        OutliersTableView.setFont(tablefont)

        # set table view header
        header = OutliersTableView.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignHCenter)
        header.setFixedHeight(26)

        # set the row heights
        nrows = num_data_rows
        for row in range(nrows):
            OutliersTableView.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        # set table view columns
        OutliersTableView.verticalHeader().setVisible(False)
        for i in range(len(DEFAULT_COLUMN_WIDTHS)) :
           OutliersTableView.setColumnWidth(i, DEFAULT_COLUMN_WIDTHS[i])     
        
        OutliersTableView.setWordWrap(True)


    # -----------------------------------------------------------------#
    # -                 Initialize the form widgets                   -#
    # -----------------------------------------------------------------#
    def format_outliers_data(self,colname,outliers_data) :

        add_debug_to_log("format_outliers_data",print_to_string("format_outliers_data",outliers_data))


    # -----------------------------------------------------------------#
    # -                 Load data into the model                      -#
    # -----------------------------------------------------------------#
    def load_model_data(self,outliers_data):

        data    =   []

        outliers_stds       =   []
        outliers_count      =   []
        outliers_percent    =   []
        outliers_range      =   []
        outliers_color      =   []

        from dfcleanser.common.cfg import get_dfc_dataframe_df 
        df          =   get_dfc_dataframe_df(self.dftitle)
        self.df     =   df

        green_bgcolor   =   QtGui.QBrush(QColor(173, 236, 196))
        yellow_bgcolor  =   QtGui.QBrush(QColor(250, 246, 190))
        red_bgcolor     =   QtGui.QBrush(QColor(241, 196, 183))
       
        minv        =   df[self.colname].min()
        maxv        =   df[self.colname].max()

        total_counts        =   0
        for i in range(len(outliers_data)) :
            total_counts    =   total_counts + outliers_data[i]

        for i in range(len(outliers_data)) :

            if(not (outliers_data[i] == 0) ) :
            
                outliers_stds.append(i)
                outliers_count.append(outliers_data[i])
                outliers_percent.append(float("{0:.2f}".format(100 * (outliers_data[i] / total_counts))))

                if(i == 0) :
                    
                    outliers_range.append("{0:.2f}".format(self.mean - ((i+1)*self.std)) + " - " + "{0:.2f}".format(self.mean + ((i+1)*self.std)))
                    outliers_color.append(green_bgcolor)
                    
                else :
                    
                    lowermin = self.mean - ((i+1)*self.std)
                    lowermax = self.mean - ((i)*self.std)
                    if(lowermin < minv) : lowermin = minv
                    if(lowermax < minv) : lowermax = minv
                    
                    uppermin = self.mean + ((i)*self.std)
                    uppermax = self.mean + ((i+1)*self.std)
                    if(uppermin > maxv) : uppermin = maxv
                    if(uppermax > maxv) : uppermax = maxv
                    
                    rangestr    =   ""
                    rangestr1   =   ""
                    
                    if(lowermax > minv) :
                        rangestr = "{0:.2f}".format(lowermin) + " - " + "{0:.2f}".format(lowermax)
                    if(uppermin < maxv) :
                        rangestr1 = rangestr1 + "{0:.2f}".format(uppermin) + " - " + "{0:.2f}".format(uppermax)
                    
                    if( (len(rangestr) > 0) and (len(rangestr1) > 0) ) :
                        rangestr = rangestr + "  and  " + rangestr1
                    else :
                        rangestr = rangestr + rangestr1
                    
                    outliers_range.append(rangestr)
                    
                    if(i > 2) :
                        outliers_color.append(red_bgcolor)
                    else :
                        outliers_color.append(yellow_bgcolor)

        if(DEBUG_COUTLIERS) :
            add_debug_to_log("format_outliers_data",print_to_string(outliers_stds,outliers_count,outliers_percent,outliers_range,outliers_color))

        data_row            =   []
        num_data_rows       =   0

        # fill in the data rows
        for i in range(len(outliers_count)) :
            
            data_row            =   []
            
            data_row.append(outliers_stds[i])
            data_row.append(outliers_count[i])
            data_row.append(outliers_percent[i])
            data_row.append(outliers_range[i])

            data.append(data_row)
 
            num_data_rows   =   num_data_rows + 1

        if(DEBUG_COUTLIERS) :
            add_debug_to_log("format_outliers_data",print_to_string(num_data_rows,"\n",data))

        return([outliers_color,data])


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -           dfcleanser column outliers qt objects                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

      
# -----------------------------------------------------------------#
# -                Global access to display uniques               -#
# -----------------------------------------------------------------#
def showOutliers(dftitle,colname)  :

    if(DEBUG_COUTLIERS) :
        add_debug_to_log("showUniques",print_to_string(dftitle,colname))

    logger.info("Opening dfc Outliers GUI")

    #from dfcleanser.common.cfg import get_dfc_dataframe_df
    df = cfg.get_dfc_dataframe_df(dftitle)

    if(not (df is None)) :

        # check if valid column
        from dfcleanser.common.common_utils import is_column_in_df 
        if (is_column_in_df(df,colname)) :

            dfParms     =   []
            dfParms.append(dftitle)
            dfParms.append(colname)
            dfParms.append(df[colname].mean())
            dfParms.append(df[colname].std())

            outliers_data   =   get_simple_col_outliers(df,colname)
            dfParms.append(outliers_data)

            outliers_gui = OutliersGui(dfParms)
            outliers_gui.show()

            from dfcleanser.common.cfg import dfc_qt_chapters, OUTLIERS_QT_CHAPTER_ID
            dfc_qt_chapters.add_qt_chapter(outliers_gui,OUTLIERS_QT_CHAPTER_ID,(dftitle + "_" + colname))


            return outliers_gui  
         
        else :
        
            return(None)
    
    else :
    
        return(None)

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -           dfcleanser column outliers qt objects                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

def get_simple_col_outliers(df,colname) :
    """
    * -------------------------------------------------------------------------- 
    * function : get a simplelist of outliers based on stddev from means
    * 
    * parms :
    *   df       -   dataframe
    *   colname  -   column name
    *
    * returns : 
    *  outliers
    * --------------------------------------------------------
    """

    outliers        =   []
    outlierscount   =   []
    
    numstddevs      =   15
    
    for i in range(numstddevs) :
        outliers.append([])
        outlierscount.append(0)
    
    mean    =   df[colname].mean()
    std     =   df[colname].std()
    
    counts  =   df[colname].value_counts().to_dict()
    uniques =   list(counts.keys())
    
    from dfcleanser.common.common_utils import is_numeric_col
    if(is_numeric_col(df,colname)) :
        uniques.sort()

    for i in range(len(uniques)) :
        import pandas as pd
        if( not pd.isnull(uniques[i])) :
            difference = abs(mean - uniques[i])
        
            import math
            outindex = math.floor(difference / std)
            outlierscount[outindex] = outlierscount[outindex] + counts.get(uniques[i])
    
    return(outlierscount)        


