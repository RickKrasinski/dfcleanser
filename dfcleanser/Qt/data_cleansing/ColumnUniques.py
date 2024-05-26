"""
# ColumnUniques
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

from PyQt5.QtCore import QSize, Qt
#from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import uic

#from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont


import dfcleanser.common.cfg as cfg 

from dfcleanser.Qt.system.SystemModel import is_debug_on
from dfcleanser.common.cfg import DataCleansing_ID



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


import logging
logger = logging.getLogger(__name__)


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

DEFAULT_COLUMN_WIDTHS               =   [100,80,100,80,100,80,100,80,100,80,100,80,100,80]
        
DIALOG_GEOMETRY                     =   [0,0,1371,879]

UNIQUES_TABLEVIEW_LABEL_GEOMETRY    =   [40,30,1278,30]
UNIQUES_TABLEVIEW_GEOMETRY          =   [40,60,1278,426]

UNIQUES_STATS_LABEL_GEOMETRY        =   [490,500,420,30]
MORE_UNIQUES_BUTTON_GEOMETRY        =   [620,560,150,40]

MIN_VALUE_LABEL_GEOMETRY            =   [490,630,100,20]
MIN_VALUE_INPUT_GEOMETRY            =   [490,660,420,30]
MAX_VALUE_LABEL_GEOMETRY            =   [490,710,100,20]
MAX_VALUE_INPUT_GEOMETRY            =   [490,740,420,30]

RANK_BY_COUNTS_BUTTON_GEOMETRY      =   [540,790,150,40]
FIND_UNIQUES_BUTTON_GEOMETRY        =   [720,790,150,40]

DEFAULT_TABLEVIEW_HEIGHT            =   UNIQUES_TABLEVIEW_GEOMETRY[3]
DEFAULT_NUM_ROWS                    =   20
DEFAULT_ROW_HEIGHT                  =   20

MAX_ROWS_TO_DISPLAY                 =   3000

# -----------------------------------------------------------------#
# -     Table Model for unique values table view      -#
# -----------------------------------------------------------------#
class UniquesTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):

        super(UniquesTableModel, self).__init__()
        self._data = data

    def reload_data(self,data) :
        self._data = data

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
            odd = (column % 2) 
            if(odd) :
                return(Qt.AlignRight)
            else :
                return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:
            odd = (column % 2) 
            if(odd):
                bgcolor = QtGui.QBrush(QtCore.Qt.white)
            else:
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
            odd = (section % 2) 
            if(odd) :
                return('Count')
            else :
                return("Value")
        return super().headerData(section, orientation, role)


# -----------------------------------------------------------------#
# -    Subclass of QMainWindow to disp[lay the columns uniques    -#
# -----------------------------------------------------------------#
class UniquesGui(QtWidgets.QMainWindow):

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
        self.unique_data        =   dfparms[2]
        
        self.drop_flag          =   dfparms[3]

        if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            add_debug_to_log("UniquesGui",print_to_string("self.drop_flag : ",self.drop_flag,type(self.drop_flag)))

        if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            add_debug_to_log("UniquesGui",print_to_string(" self.dftitle : ",self.dftitle))
            add_debug_to_log("UniquesGui",print_to_string(" self.colname : ",self.colname))
            add_debug_to_log("UniquesGui",print_to_string(" self.drop_flag : ",self.drop_flag))


        self.rows_to_display    =   0
        self.num_columns        =   0
        self.form               =   None
        self.model              =   None

        self.caller_stack   = inspect.currentframe().f_back
        self.stacked_widget = QStackedWidget(None)

        # enable custom window hint
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)

        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)


        cfg.set_config_value(cfg.CURRENT_UNIQUES_ORDER_FLAG,cfg.NO_UNIQUES_RANKING)
        cfg.set_config_value(cfg.CURRENT_UNIQUES_LAST_ROW_DISPLAYED,0)

        self.init_gui()

    def update(self):   
        self.update()

    # dump the cirrent form geometry
    def dump_geometry(self) :

        # dump the form geometries
        
        add_debug_to_log("dump_geometry",print_to_string(" : ",self.form.UniquesTablelabel.geometry()))
        add_debug_to_log("dump_geometry",print_to_string(" : ",self.form.columnUniquestableView.geometry()))

        add_debug_to_log("dump_geometry",print_to_string("self : ",self.form.UniqueStatslabel.geometry()))
        add_debug_to_log("dump_geometry",print_to_string("MoreUniquesbutton : ",self.form.MoreUniquesbutton.geometry()))

        add_debug_to_log("dump_geometry",print_to_string("min_value_label : ",self.form.min_value_label.geometry()))
        add_debug_to_log("dump_geometry",print_to_string("min_value_input : ",self.form.min_value_input.geometry()))
        add_debug_to_log("dump_geometry",print_to_string("max_value_label : ",self.form.max_value_label.geometry()))
        add_debug_to_log("dump_geometry",print_to_string("max_value_input : ",self.form.max_value_input.geometry()))

        add_debug_to_log("dump_geometry",print_to_string("RankCountsbutton : ",self.form.RankCountsbutton.geometry()))
        add_debug_to_log("dump_geometry",print_to_string("FindUniquesbutton : ",self.form.FindUniquesbutton.geometry()))

    
    # -----------------------------------------------------------------#
    # -                     Initialize the gui                        -#
    # -----------------------------------------------------------------#
        
    def init_gui(self):
        
        # set up the ui form from a qtdesigner ui
        cfgdir  = cfg.DataframeCleanserCfgData.get_dfc_qt_dir_name()
        ui_name = cfgdir +"\data_cleansing\ColumnUniquesUI.ui"
        Form, Window = uic.loadUiType(ui_name)
        self.form = Form()
        self.form.setupUi(self)
        
        # -----------------------------------------------------#
        #     common window attribute settings     #
        # -----------------------------------------------------#
        
        # set common window attributes
        self.setWindowTitle("dfcleanser Uniques")
        
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
        icon_name  =   dfcdir +"\dfcicon.png"
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
        
        # init the gui form
        self.init_uniques_form()


    # -----------------------------------------------------------------#
    # -                 Initialize the form widgets                   -#
    # -----------------------------------------------------------------#
    def adjust_table_view(self,num_data_rows):

        UniquesTableView = self.form.columnUniquestableView

        dead_space  =   0

        # check numm rows to resize the table view
        if(num_data_rows < DEFAULT_NUM_ROWS) :

            new_height  =   DEFAULT_TABLEVIEW_HEIGHT - ((DEFAULT_NUM_ROWS - num_data_rows) * DEFAULT_ROW_HEIGHT)

            UniquesTableView.setMinimumHeight(new_height)
            UniquesTableView.setMaximumHeight(new_height)

            dead_space  =   UNIQUES_TABLEVIEW_GEOMETRY[3] - new_height

            if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
               add_debug_to_log("adjust_table_view",print_to_string(" : new_height : ",new_height))
               add_debug_to_log("adjust_table_view",print_to_string(" : tableview dead_space : ",dead_space))
            
        if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            add_debug_to_log("adjust_table_view",print_to_string(" : dead_space : ",dead_space))

        return(dead_space)


    # -----------------------------------------------------------------#
    # -                 Initialize the form widgets                   -#
    # -----------------------------------------------------------------#
    def adjust_form_widgets(self,dead_space):

        if(dead_space > 0) :

            new_geometry        =   UNIQUES_STATS_LABEL_GEOMETRY.copy()
            new_geometry[1]     =   (new_geometry[1] - dead_space)
            self.form.UniqueStatslabel.move(new_geometry[0],new_geometry[1])

        if(self.rows_to_display < MAX_ROWS_TO_DISPLAY):

            self.form.MoreUniquesbutton.setEnabled(False)
            self.form.MoreUniquesbutton.hide()
            dead_space  =   dead_space + 70
        
        from dfcleanser.common.common_utils import is_string_col, is_object_col

        if( (is_string_col(self.df,self.colname)) or (is_object_col(self.df,self.colname)) or (self.drop_flag)) :

            if(self.drop_flag) :
                self.form.RankCountsbutton.setText("Drop Rows")
                self.form.min_value_label.setText("drop value") 
            else :   
                self.form.min_value_label.setText("substring")

            if(dead_space > 0) :

                new_geometry        =   MIN_VALUE_LABEL_GEOMETRY.copy()
                new_geometry[1]     =   (new_geometry[1] - dead_space)
                self.form.min_value_label.move(new_geometry[0],new_geometry[1])
            
                new_geometry        =   MIN_VALUE_INPUT_GEOMETRY.copy()
                new_geometry[1]     =   (new_geometry[1] - dead_space)
                self.form.min_value_input.move(new_geometry[0],new_geometry[1])

                dead_space  =   dead_space + 70
                self.form.max_value_label.hide()
                self.form.max_value_input.hide()
            
            else :

                dead_space  =   dead_space + 70
                self.form.max_value_label.hide()
                self.form.max_value_input.hide()

        else :

            if(dead_space > 0) :

                new_geometry        =   MIN_VALUE_LABEL_GEOMETRY.copy()
                new_geometry[1]     =   (new_geometry[1] - dead_space)
                self.form.min_value_label.move(new_geometry[0],new_geometry[1])

                new_geometry        =   MIN_VALUE_INPUT_GEOMETRY.copy()
                new_geometry[1]     =   (new_geometry[1] - dead_space)
                self.form.min_value_input.move(new_geometry[0],new_geometry[1])

                new_geometry        =   MAX_VALUE_LABEL_GEOMETRY.copy()
                new_geometry[1]     =   (new_geometry[1] - dead_space)
                self.form.max_value_label.move(new_geometry[0],new_geometry[1])

                new_geometry        =   MAX_VALUE_INPUT_GEOMETRY.copy()
                new_geometry[1]     =   (new_geometry[1] - dead_space)
                self.form.max_value_input.move(new_geometry[0],new_geometry[1])
            
        if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            add_debug_to_log("adjust_table_view",print_to_string("  : dead_space : ",dead_space))

        if(dead_space > 0) :

            new_geometry        =   RANK_BY_COUNTS_BUTTON_GEOMETRY.copy()
            new_geometry[1]     =   (new_geometry[1] - dead_space)
            self.form.RankCountsbutton.move(new_geometry[0],new_geometry[1])

            new_geometry        =   FIND_UNIQUES_BUTTON_GEOMETRY.copy()
            new_geometry[1]     =   (new_geometry[1] - dead_space)
            self.form.FindUniquesbutton.move(new_geometry[0],new_geometry[1])

            dialog_height       =   DIALOG_GEOMETRY[3] - dead_space

            self.resize(DIALOG_GEOMETRY[2],dialog_height)
            
            if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
                add_debug_to_log("adjust_table_view",print_to_string(" resize : ",DIALOG_GEOMETRY[2],dialog_height))

        if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            if(dead_space > 0) :
                add_debug_to_log("adjust_table_view",print_to_string(" after adjustments",dead_space))
                self.dump_geometry()


    def set_tableview_footer(self,start,last,nuniques):

        # init the tableview footer
        if(self.rows_to_display > MAX_ROWS_TO_DISPLAY) :
            self.form.UniqueStatslabel.setText("Uniques Values " + str(start) + " to " + str(last) + " Displayed : Total Uniques : " + str(nuniques))
        else :
            self.form.UniqueStatslabel.setText("Total " + str(num_uniques) + " Unique Values Displayed ")
        self.form.UniqueStatslabel.setStyleSheet("font-size: 12px; font-weight: bold; font-style: normal; font-family: Arial;  margin-left: 0px; ") 


    # -----------------------------------------------------------------#
    # -                 Initialize the gui form                       -#
    # -----------------------------------------------------------------#
    def init_uniques_form(self):
        
        if(self.df is None) :
            from dfcleanser.common.cfg import get_dfc_dataframe_df 
            df          =   get_dfc_dataframe_df(self.dftitle)
            self.df     =   df
        else :
            df  =   self.df
        
        # format the unique data dependent on type and value length
        [column_widths,rows_to_display]     =   self.format_unique_data(df,self.colname,self.unique_data)
        self.column_widths                  =   column_widths
        self.num_columns                    =   len(self.column_widths)
        self.rows_to_display                =   rows_to_display
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            add_debug_to_log("init_uniques_form",print_to_string(" rows_to_display : num_columns : ",rows_to_display,self.num_columns,"\n  column widths : ",column_widths))
        
        num_uniques     =   len(self.unique_data[0])

        # init the tableview title
        self.form.UniquesTablelabel.setText("  df '" + self.dftitle + "' : Column '" + self.colname + "'" + str(num_uniques) + " Unique Values")
        self.form.UniquesTablelabel.setStyleSheet("background-color:#3399ff; color: white; font-size: 16px; font-weight: bold; font-style: normal; font-family: Arial;  margin-left: 0px; ") 
        


        #----------------------------#
        # init the tableview widget  #
        #----------------------------#
        
        # grab the tableview form
        UniquesTableView = self.form.columnUniquestableView

        if(self.rows_to_display > MAX_ROWS_TO_DISPLAY) :

            start_val   =   cfg.get_config_value(cfg.CURRENT_UNIQUES_LAST_ROW_DISPLAYED)
            last_val    =   int(start_val + (MAX_ROWS_TO_DISPLAY * (self.num_columns / 2))) 

            if(last_val > len(self.unique_data[0])) :
                last_val    =   len(self.unique_data[0])

            if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
                add_debug_to_log("init_uniques_form",print_to_string(" start_val : last_val : ",start_val,last_val))

            self.set_tableview_footer(start_val,last_val,len(self.unique_data[0]))

            cdata_values    =   self.unique_data[0][start_val : last_val]
            cdata_counts    =   {}
            for i in range(len(cdata_values)) :
                cdata_counts.update({cdata_values[i] : self.unique_data[1].get(cdata_values[i])})  

            cdata   =   [cdata_values,cdata_counts] 

            data    =   self.load_model_data(cdata,self.num_columns) 

        else :

            data    =   self.load_model_data(self.unique_data,self.num_columns)

        num_data_rows   =   len(data)

        last_unique_displayed   =   int(num_data_rows * (len(self.column_widths) / 2))
        cfg.set_config_value(cfg.CURRENT_UNIQUES_LAST_ROW_DISPLAYED,last_unique_displayed)
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            add_debug_to_log("init_uniques_form",print_to_string(" num_data_rows : last_unique_displayed ",num_data_rows,last_unique_displayed))

        # adjust the height of the tableview
        dead_space  =   self.adjust_table_view(num_data_rows)

        #--------------------------#
        # init the buttons attrs   #
        #--------------------------#
          
        self.form.MoreUniquesbutton.setCheckable(True)
        self.form.RankCountsbutton.setCheckable(True)
        self.form.FindUniquesbutton.setCheckable(True)
        self.form.MoreUniquesbutton.setChecked(False)
        self.form.RankCountsbutton.setChecked(False)
        self.form.FindUniquesbutton.setChecked(False)
        self.form.MoreUniquesbutton.setEnabled(True)
        self.form.RankCountsbutton.setEnabled(True)
        self.form.FindUniquesbutton.setEnabled(True)

        # set button attributes
        self.form.RankCountsbutton.setStyleSheet("background-color:lightgray")                                        
        self.form.FindUniquesbutton.setStyleSheet("background-color:lightgray")                                         
        self.form.MoreUniquesbutton.setStyleSheet("background-color:lightgray") 

        # adding action to a button
        if(self.drop_flag) :
            self.form.RankCountsbutton.clicked.connect(self.dropvalues)
        else :
            self.form.RankCountsbutton.clicked.connect(self.rankcounts)
        self.form.FindUniquesbutton.clicked.connect(self.finduniques)  
        self.form.MoreUniquesbutton.clicked.connect(self.moreuniques)  


        #----------------------------------------------#
        # adjust form widgets based on tableview size  #
        #----------------------------------------------#

        self.adjust_form_widgets(dead_space)

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        if(self.model is None) :
            self.model = UniquesTableModel(data)
            UniquesTableView.setModel(self.model)

        #----------------------------------------------#
        # init the table view header and cell sizes    #
        #----------------------------------------------#
        
        # set default tableview font
        tablefont   =  QFont("Times",10) 
        tablefont.setBold(False)
        UniquesTableView.setFont(tablefont)

        # set table view header
        header = UniquesTableView.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignHCenter)
        header.setFixedHeight(26)

        # set the row heights
        nrows = num_data_rows#len(data)
        for row in range(nrows):
            UniquesTableView.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        # set table view columns
        UniquesTableView.verticalHeader().setVisible(False)
        for i in range(len(self.column_widths)) :
           UniquesTableView.setColumnWidth(i, self.column_widths[i])     
        
        UniquesTableView.setWordWrap(True)


    # -----------------------------------------------------------------#
    # -                 Initialize the form widgets                   -#
    # -----------------------------------------------------------------#
    def format_unique_data(self,df,colname,unique_data):

        num_uniques             =   len(unique_data[0])

        #----------------------------------------------#
        # adjust the num columns and columns           #
        # based on the unique data types and values    #
        #----------------------------------------------#
        from dfcleanser.common.common_utils import is_numeric_col, is_string_col, is_object_col, is_categorical_col, is_datetime64_col, is_timedelta64_col, is_timedelta_col, is_datetime_col, is_date_col, is_time_col, is_Timestamp_col, is_Timedelta_col

        if( (is_numeric_col(df,colname)) or (is_timedelta64_col(df,self.colname)) or (is_timedelta_col(df,self.colname)) or (is_Timedelta_col(df,self.colname)) ):

            max_value   =   max(unique_data[0])
            val_counts  =   list(unique_data[1].values())
            max_count   =   max(val_counts)

            column_widths   =  DEFAULT_COLUMN_WIDTHS 

        elif( (is_string_col(df,colname)) or (is_object_col(df,colname)) or(self.drop_flag)) :

            max_len     =   -1
            for i in range(num_uniques) :

                try :
                    current_len     =   len(unique_data[0][i]) 
                except :
                    current_len     =   -1

                if(current_len > max_len) :
                    max_len     =   current_len
                    max_value   =   unique_data[0][i]

            val_counts          =   list(unique_data[1].values())
            max_count           =   max(val_counts)
            max_value_length    =   max_len

            if(max_value_length > 50) :
                if(max_value_length > 70) :
                    column_widths   =  [1160,80]
                else :
                    column_widths   =  [540,80,540,80]

            elif(max_value_length <= 12) :
                column_widths   =  DEFAULT_COLUMN_WIDTHS

            elif(max_value_length <= 30)  :
                column_widths   =  [126,80,126,80,126,80,126,80,126,80,126,80] 

            else :
                column_widths   =  [170,80,170,80,170,80,170,80,170,80]    

        elif(is_categorical_col(df,colname)) :

            max_value   =   max(unique_data[0])
            val_counts  =   list(unique_data[1].values())
            max_count   =   max(val_counts)

            column_widths   =  DEFAULT_COLUMN_WIDTHS 

        elif( (is_datetime64_col(df,colname)) or (is_datetime_col(df,colname)) or (is_date_col(df,colname)) or 
              (is_time_col(df,colname)) or (is_Timestamp_col(df,colname)) )  :

            new_data_vals   =   []
            new_counts_dict =   {}

            max_len         =   -1
            for i in range(num_uniques) :

                try :
                    current_datetime    =   str(unique_data[0][i]) 
                    current_length      =   len(current_datetime) 

                    new_data_vals.append(current_datetime)
                    current_value   =  unique_data[0][i] 
                    new_counts_dict.update({current_datetime : unique_data[1].get(current_value)})

                except :
                    current_length      =   -1

                if(current_length> max_len) :
                    max_len     =   current_length
                    max_value   =   current_datetime

            val_counts  =   list(unique_data[1].values())
            max_count   =   max(val_counts)

            # store away the data conveted to strings
            self.unique_data[0]     =   new_data_vals
            self.unique_data[1]     =   new_counts_dict

            column_widths   =  [170,80,170,80,170,80,170,80,170,85] 

        else :

            column_widths   =   DEFAULT_COLUMN_WIDTHS

        rows_to_display     =   num_uniques / (len(column_widths) / 2)

        if( (round(rows_to_display,0)) < rows_to_display) :
            rows_to_display     =   int(rows_to_display) + 1
        else :
            rows_to_display     =   int(rows_to_display)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            add_debug_to_log("format_unique_data",print_to_string(" : num_uniques : rows_to_display ",num_uniques,rows_to_display,"\n   column_widths : ",column_widths))

        return[column_widths,rows_to_display]


    # -----------------------------------------------------------------#
    # -                 Load data into the model                      -#
    # -----------------------------------------------------------------#
    def load_model_data(self,unique_data,num_cols):

        data    =   []

        data_vals           =   unique_data[0]
        data_counts_dict    =   unique_data[1]

        vals_per_row        =   num_cols

        data_row            =   []
        num_data_rows       =   0

        num_uniques         =   len(data_vals)

        if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            add_debug_to_log("load_model_data",print_to_string(" : num_uniques : vals_per_row ",num_uniques,vals_per_row))

        # fill in the data rows
        for i in range(num_uniques) :

            data_row.append(data_vals[i])
            data_row.append(data_counts_dict.get(data_vals[i]))
 
            if(len(data_row) == vals_per_row) :
                data.append(data_row)
                data_row    =   []
                num_data_rows   =   num_data_rows + 1

        # fill in any partial rows
        if( not (len(data_row) == 0)) :
            for i in range((vals_per_row - len(data_row))) :
                data_row.append(" ")

            data.append(data_row)
            num_data_rows   =   num_data_rows + 1

        if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            add_debug_to_log("load_model_data",print_to_string(" : num_data_rows : ",num_data_rows,"\n    ",data[0],"\n    ",data[num_data_rows-1]))

        return(data)


    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -                Table vierw action methods                     -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -                rank uniques by counts                         -#
    # -----------------------------------------------------------------#
    def rankcounts(self):

        current_ranking     =   cfg.get_config_value(cfg.CURRENT_UNIQUES_ORDER_FLAG)

        if(current_ranking == cfg.NO_UNIQUES_RANKING) :
            cfg.set_config_value(cfg.CURRENT_UNIQUES_ORDER_FLAG,cfg.LOW_TO_HIGH_UNIQUES_RANKING)
        elif(current_ranking == cfg.LOW_TO_HIGH_UNIQUES_RANKING) :
            cfg.set_config_value(cfg.CURRENT_UNIQUES_ORDER_FLAG,cfg.HIGH_TO_LOW_UNIQUES_RANKING) 
        else :
            cfg.set_config_value(cfg.CURRENT_UNIQUES_ORDER_FLAG,cfg.LOW_TO_HIGH_UNIQUES_RANKING)        
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            add_debug_to_log("rankcounts",print_to_string(" : current_ranking : ",current_ranking))

        self.form.RankCountsbutton.toggle()

        from dfcleanser.common.cfg import get_dfc_dataframe_df 
        df  =   get_dfc_dataframe_df(self.dftitle)
        
        from dfcleanser.common.common_utils import get_df_unique_counts_column_data
        uniques_data        =   get_df_unique_counts_column_data(df, self.colname)
        self.unique_data    =   uniques_data

        if(current_ranking == cfg.LOW_TO_HIGH_UNIQUES_RANKING):
            self.statusBar().showMessage("Uniques Counts Displayed in Descending Order ")
        else:
            self.statusBar().showMessage("Uniques Counts Displayed in Ascending Order ")

        data    =   self.load_model_data(uniques_data,len(self.column_widths))
        self.model.reload_data(data)
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            add_debug_to_log("rankcounts",print_to_string(" : model data : ",len(data)))
    

    # -----------------------------------------------------------------#
    # -                     drop rows by value                        -#
    # -----------------------------------------------------------------#
    def dropvalues(self):

        return()
        current_ranking     =   cfg.get_config_value(cfg.CURRENT_UNIQUES_ORDER_FLAG)

        if(current_ranking == cfg.NO_UNIQUES_RANKING) :
            cfg.set_config_value(cfg.CURRENT_UNIQUES_ORDER_FLAG,cfg.LOW_TO_HIGH_UNIQUES_RANKING)
        elif(current_ranking == cfg.LOW_TO_HIGH_UNIQUES_RANKING) :
            cfg.set_config_value(cfg.CURRENT_UNIQUES_ORDER_FLAG,cfg.HIGH_TO_LOW_UNIQUES_RANKING) 
        else :
            cfg.set_config_value(cfg.CURRENT_UNIQUES_ORDER_FLAG,cfg.LOW_TO_HIGH_UNIQUES_RANKING)        
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            add_debug_to_log("rankcounts",print_to_string(" : current_ranking : ",current_ranking))

        self.form.RankCountsbutton.toggle()

        from dfcleanser.common.cfg import get_dfc_dataframe_df 
        df  =   get_dfc_dataframe_df(self.dftitle)
        
        from dfcleanser.common.common_utils import get_df_unique_counts_column_data
        uniques_data        =   get_df_unique_counts_column_data(df, self.colname)
        self.unique_data    =   uniques_data

        if(current_ranking == cfg.LOW_TO_HIGH_UNIQUES_RANKING):
            self.statusBar().showMessage("Uniques Counts Displayed in Descending Order ")
        else:
            self.statusBar().showMessage("Uniques Counts Displayed in Ascending Order ")

        data    =   self.load_model_data(uniques_data,len(self.column_widths))
        self.model.reload_data(data)
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            add_debug_to_log("rankcounts",print_to_string(" model data : ",len(data)))
    
    # -----------------------------------------------------------------#
    # -                find unique values in df                       -#
    # -----------------------------------------------------------------#
    def finduniques(self):

        if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            add_debug_to_log("finduniques",print_to_string(" : ",self.dftitle,self.colname) )

        from dfcleanser.common.cfg import get_dfc_dataframe_df 
        df          =   get_dfc_dataframe_df(self.dftitle)
        df_found    =   None

        self.form.FindUniquesbutton.toggle()

        from dfcleanser.common.common_utils import is_numeric_col
        if(is_numeric_col(df, self.colname)):

            min_parm    =  self.form.min_value_input.toPlainText() 
            max_parm    =  self.form.max_value_input.toPlainText() 

            if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
                add_debug_to_log("finduniques",print_to_string(" : ",min_parm,max_parm)) 

            if(len(min_parm) == 0):
                find_min = df[self.colname].min()
            else:

                try :
                    find_min    =   float(min_parm)
                except :
                    find_min    =   None

            if(len(max_parm) == 0):
                find_max = df[self.colname].max()
            else:

                try :
                    find_max    =   float(max_parm)
                except :
                    find_max    =   None
        
            if(not ((find_min is None) and (find_max is None))):

                criteria = (df[self.colname] >= find_min) & (df[self.colname] <= find_max)
                df_found = df[criteria]

            else :

                if(find_min is None) :
                    self.statusBar().showMessage("Invalid min_value")
                else :
                    self.statusBar().showMessage("Invalid max_Value")

        else:

            find_substr   =  self.form.min_value_input.toPlainText()

            if(len(find_substr) == 0):
                substr = None
            else:
                substr = find_substr

            if(not (substr is None)):

                criteria = df[self.colname].str.contains(substr, False)
                df_found = df[criteria]

            else :

                self.statusBar().showMessage("Invalid substring find value")

        if(not(df_found is None)) :

            from dfcleanser.common.common_utils import get_df_unique_column_data
            uniques_data        =   get_df_unique_column_data(df_found, self.colname)
            self.unique_data    =   uniques_data

            if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
                add_debug_to_log("finduniques",print_to_string(" : uniques_data : ",uniques_data))

            data        =   self.load_model_data(uniques_data,len(self.column_widths))
            dead_space  =   self.adjust_table_view(len(data))
            self.adjust_form_widgets(dead_space)
            self.model.reload_data(data)

            self.statusBar().showMessage("Requested Unique Values Displayed")

        else :

            # subset of found values is valid
	    if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            	add_debug_to_log("finduniques",print_to_string(" : ",print_to_string("no values found matching parms")))


    # -----------------------------------------------------------------#
    # -                   display more uniques                        -#
    # -----------------------------------------------------------------#
    def moreuniques(self):

        if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            add_debug_to_log("moreuniques",print_to_string(" :",self.dftitle,self.colname)) 

        self.form.MoreUniquesbutton.toggle()

        from dfcleanser.common.cfg import get_dfc_dataframe_df 
        df          =   get_dfc_dataframe_df(self.dftitle)
        startrow    =   cfg.get_config_value(cfg.CURRENT_UNIQUES_LAST_ROW_DISPLAYED) + 1
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            add_debug_to_log("finduniques",print_to_string(" : startrow",startrow)) 

        display_type  =   cfg.get_config_value(cfg.CURRENT_UNIQUES_ORDER_FLAG)

        if((display_type) == cfg.NO_UNIQUES_RANKING) :
        
            from dfcleanser.common.common_utils import get_df_unique_column_data
            uniques_data    =   get_df_unique_column_data(df, self.colname)

        else :

            from dfcleanser.common.common_utils import get_df_unique_counts_column_data
            uniques_data    =   get_df_unique_counts_column_data(df, self.colname)
        
        if(startrow >= len(uniques_data[0])) :
            cfg.set_config_value(cfg.CURRENT_UNIQUES_LAST_ROW_DISPLAYED,0)
            startrow    =   cfg.get_config_value(cfg.CURRENT_UNIQUES_LAST_ROW_DISPLAYED)
        
        if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            add_debug_to_log("finduniques",print_to_string(" startrow : uniques_data ",startrow,len(uniques_data[0]),uniques_data[0][startrow],uniques_data[0][startrow+1])) 

        uniques_vals            =   uniques_data[0]
        uniques_counts_dict     =   uniques_data[1]

        more_uniques_vals           =   []
        more_uniques_counts_dict    =   {}

        max_more_vals   =   int(MAX_ROWS_TO_DISPLAY * ((len(self.column_widths)) / 2))

        if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            add_debug_to_log("finduniques",print_to_string(" : max_more_vals ",max_more_vals))

        lastrow     =   startrow

        for i in range(max_more_vals) :
            if((i + startrow) < len(uniques_vals)) :
                more_uniques_vals.append(uniques_vals[i + startrow])
                more_uniques_counts_dict.update({uniques_vals[i + startrow] :uniques_counts_dict.get(uniques_vals[i + startrow])})
            else :
                lastrow  =   len(uniques_vals) - 1
                break

        if(lastrow == startrow) :
            lastrow     =  (startrow + max_more_vals) - 1 

        more_uniques_data   =   [more_uniques_vals,more_uniques_counts_dict,]

        if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            add_debug_to_log("finduniques",print_to_string(" more_uniques_data ",len(more_uniques_data),more_uniques_data[0][0])) 

        data        =   self.load_model_data(more_uniques_data,len(self.column_widths))
        dead_space  =   self.adjust_table_view(len(data))
        self.adjust_form_widgets(dead_space)
        self.model.reload_data(data)

        cfg.set_config_value(cfg.CURRENT_UNIQUES_LAST_ROW_DISPLAYED,lastrow)
        self.set_tableview_footer(startrow,lastrow,len(self.unique_data[0]))


        if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
            add_debug_to_log("finduniques",print_to_string(" : lastrow ",cfg.get_config_value(cfg.CURRENT_UNIQUES_LAST_ROW_DISPLAYED))) 

      
# -----------------------------------------------------------------#
# -                Global access to display uniques               -#
# -----------------------------------------------------------------#
def showUniques(dftitle,colname,DropFlag=False)  :

    if(is_debug_on(DataCleansing_ID,"DEBUG_CUNIQUES")) :
        add_debug_to_log("showUniques",print_to_string(" : ",dftitle,colname))

    logger.info("Opening dfc Uniques GUI")

    #from dfcleanser.common.cfg import get_dfc_dataframe_df
    df = cfg.get_dfc_dataframe_df(dftitle)

    if(not (df is None)) :

        # check if valid column
        from dfcleanser.common.common_utils import is_column_in_df 
        if (is_column_in_df(df,colname)) :

            dfParms     =   []
            dfParms.append(dftitle)
            dfParms.append(colname)
        
            from dfcleanser.common.common_utils import get_df_unique_column_data
            uniques_data    =   get_df_unique_column_data(df, colname)
            dfParms.append(uniques_data)
            dfParms.append(DropFlag)

            uniques_gui = UniquesGui(dfParms)
            uniques_gui.show()

            from dfcleanser.common.cfg import dfc_qt_chapters, UNIQUES_QT_CHAPTER_ID
            dfc_qt_chapters.add_qt_chapter(uniques_gui,UNIQUES_QT_CHAPTER_ID,(dftitle + "_" + colname))


            return uniques_gui  
         
        else :
        
            return(None)
    
    else :
    
        return(None)

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -           dfcleanser column uniques qt objects                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#









