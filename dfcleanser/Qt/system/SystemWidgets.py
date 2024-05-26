"""
# DataInspection
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
from dfcleanser.common.cfg import (print_to_string, add_debug_to_log, DC_SYSTEM_ID, DC_DATA_IMPORT_ID, DC_DATA_INSPECTION_ID, 
                                   DC_DATA_CLEANSING_ID, DC_DATA_TRANSFORM_ID, DC_DATA_EXPORT_ID, DBUtils_ID, SWUtilities_ID, 
                                   DC_CENSUS_ID, DC_ZIPCODE_UTILITY_ID, DC_GEOCODE_UTILITY_ID)


from dfcleanser.Qt.system.SystemModel import is_debug_on, save_debug_flags
from dfcleanser.common.cfg import System_ID

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
# -           System Tableviews and Models                    -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -             Table view and Model for Active dfs               -#
# -----------------------------------------------------------------#

class SystemActivedfsModel(QtCore.QAbstractTableModel):
    def __init__(self, dfsdata, colheaders):

        super(SystemActivedfsModel, self).__init__()
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

            try :
                retval  =  self._data[index.row()][index.column()] 
            except :
                retval  =  "Error"

            return retval
        
        if role == Qt.TextAlignmentRole: 
            #odd = (column % 2) 
            if(column == 0) :
                return(Qt.AlignLeft)
            elif(column == 1) :
                return(Qt.AlignCenter)
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

# -----------------------------------------------------------------#
# -                 Table view active dfs table                   -#
# -----------------------------------------------------------------#
class SystemActivedfsTable(QtWidgets.QTableView):

    def __init__(self,  **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemActivedfsTable] : init"))

        self.init_tableview()

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemActivedfsTable] : end"))

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self):
        
        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemActivedfsTable] : reload_data"))

        active_dfs_data     =   self.load_active_dfs_data()
        self.model.reload_data(active_dfs_data)
    
    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemActivedfsTable][init_tableview]"))

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        activedfsdata     =   self.load_active_dfs_data()
        
        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
           add_debug_to_log("SystemWidgets",print_to_string("[SystemActivedfsTable][init_tableview] :headers",self.column_headers))

        if(self.model is None) :
            self.model = SystemActivedfsModel(activedfsdata,self.column_headers)
            self.setModel(self.model)

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
           add_debug_to_log("SystemWidgets",print_to_string("[SystemActivedfsTable][init_tableview] : model loaded"))

        self.num_rows   =   len(activedfsdata)
        
        if(self.num_rows < 15) :
            new_height  =   40 + ((self.num_rows + 1) * DEFAULT_ROW_HEIGHT)
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
        nrows = len(activedfsdata)
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
    def load_active_dfs_data(self):

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemActivedfsTable][load_active_dfs_data]"))

        data    =   []

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list, get_dfc_dataframe_df, get_dfc_dataframe_notes
        
        active_dfs      =   get_dfc_dataframes_titles_list()

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemActivedfsTable][load_active_dfs_data] active_dfs : ",active_dfs))

        if(not (active_dfs is None)) :

            for i in range(len(active_dfs)) :
                
                data_row    =   []

                data_row.append(str(""))
                data_row.append(active_dfs[i])
                
                df  =   get_dfc_dataframe_df(active_dfs[i])
                
                data_row.append(str(len(df)))
                data_row.append(str(len(df.columns)))
                data_row.append(get_dfc_dataframe_notes(active_dfs[i]))

                data.append(data_row)

            if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
                add_debug_to_log("SystemWidgets",print_to_string("[SystemActivedfsTable] : data"))
                for j in range(len(data)) :
                    add_debug_to_log("SystemWidgets",print_to_string("  [",j,"] : ",data[j]))

        else :

            data_row    =   []

            data_row.append(str(""))
            data_row.append("")
            data_row.append("")
            data_row.append("")
            data_row.append("No Active dfs defined")

            data.append(data_row)


        self.column_headers     =   ["DRP","df Title","Num Rows","Num Cols","Notes"]
        self.column_widths      =   [30,160,80,80,610]

        return(data)

# -----------------------------------------------------------------#
# -               Table view active dfs table end                 -#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                    System dfc dfs Widget                      -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
class System_dfc_dfs_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_dfc_dfs_Widget]"))

        super().__init__()

        self.parent     =   dfparms[0]

        self.init_form()

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_Info_Widget] end"))

    def reload_data(self) :

        self.acive_dfs_data.reload_data()

    def init_form(self):  

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_dfc_dfs_Widget][init_form]"))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.SystemdfcdfsLayout     =   QVBoxLayout()

        from PyQt5.QtWidgets import QLabel
        acive_dfs_title_label   =   QLabel()
        acive_dfs_title_label.setText("\n\nCurrent Active dfCleanser dataframes")
        acive_dfs_title_label.setAlignment(Qt.AlignCenter)
        acive_dfs_title_label.resize(480,50)
        acive_dfs_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.SystemdfcdfsLayout.addWidget(acive_dfs_title_label)

        self.acive_dfs_data         =   SystemActivedfsTable()
        self.acive_dfs_data.doubleClicked.connect(self.select_df_to_drop)

        self.SystemdfcdfsLayout.addWidget(self.acive_dfs_data)
        
        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_dfc_dfs_Widget][init_form] : active dfs loaded"))
        
        from PyQt5.QtWidgets import QLabel
        blank_title_label   =   QLabel()
        blank_title_label.setText("\n\n")
        blank_title_label.setAlignment(Qt.AlignCenter)
        blank_title_label.resize(480,50)
        blank_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.SystemdfcdfsLayout.addWidget(blank_title_label)

        # buttons for inspect rows
        from PyQt5.QtWidgets import QPushButton
        drop_button         =   QPushButton()     
        drop_button.setText("Drop\nSelected\ndfc df(s)")
        drop_button.setFixedSize(200,70)
        drop_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        drop_button.clicked.connect(self.drop_dfs_callback) 
        
        adddf_button        =   QPushButton()     
        adddf_button.setText("Add User\ndf to dfc")
        adddf_button.setFixedSize(200,70)
        adddf_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        adddf_button.clicked.connect(self.add_user_df_callback) 
        
        dfshist_button        =   QPushButton()     
        dfshist_button.setText("Display\ndfs Histories")
        dfshist_button.setFixedSize(200,70)
        dfshist_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        dfshist_button.clicked.connect(self.display_df_histories_callback) 

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_dfc_dfs_Widget][init_form] : buttons built"))

        from PyQt5.QtWidgets import QHBoxLayout
        dfcdfsbutonsLayout  =   QHBoxLayout()
        dfcdfsbutonsLayout.addWidget(drop_button)
        dfcdfsbutonsLayout.addWidget(adddf_button)
        dfcdfsbutonsLayout.addWidget(dfshist_button)
        dfcdfsbutonsLayout.setAlignment(Qt.AlignHCenter)
        self.SystemdfcdfsLayout.addLayout(dfcdfsbutonsLayout)

        self.SystemdfcdfsLayout.addStretch()
        self.setLayout(self.SystemdfcdfsLayout)

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_dfc_dfs_Widget][init_form] end"))


    # -----------------------------------------------------------------#
    # -                System dfc dfs Widget methods                  -#
    # -----------------------------------------------------------------#

    def select_df_to_drop(self) :

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_dfc_dfs_Widget][select_df_to_drop]"))

        for idx in self.acive_dfs_data.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_dfc_dfs_Widget][select_df_to_drop] ",row_number,column_number))

        model   =   self.acive_dfs_data.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][column_number]

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :    
            add_debug_to_log("SystemWidgets",print_to_string("[System_dfc_dfs_Widget][select_df_to_drop] : cell value [",cell,"]",type(cell),len(cell)))

        if(column_number == 0) :
            if(len(cell) == 0) :
                tdata[row_number][column_number] = "X" 
            else :
                tdata[row_number][column_number] = ""      

            model.reload_data(tdata)

    def drop_dfs_callback(self) :

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_dfc_dfs_Widget][drop_dfs_callback]"))

        model   =   self.acive_dfs_data.model
        tdata   =   model.get_data()

        delete_list     =   []

        for i in range(len(tdata)) :
            check_value     =   tdata[i][0]
            if(not (len(check_value) == 0)) :
                delete_list.append(tdata[i][1])

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_dfc_dfs_Widget][drop_dfs_callback] delete_list",delete_list))
        
        if(len(delete_list) > 0) :

            from PyQt5.QtWidgets import QMessageBox
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Verify Drop Active df")
            dlg.setText("Do you want to drop reference to selected dfs?")
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setStyleSheet("QLabel{min-width: 300px;}");
            button = dlg.exec()

            if(button == QMessageBox.Yes) :

                from dfcleanser.common.cfg import drop_dfc_dataframe

                for i in range(len(delete_list)) :
                    drop_dfc_dataframe(delete_list[i])

                from PyQt5.QtWidgets import QMessageBox
                dlga = QMessageBox(self)
                dlga.setWindowTitle("Drop Active dfs Status")
                dlga.setText("Selected dfs dropped from dfcleanser.")
                dlga.setStandardButtons(QMessageBox.Ok)
                dlga.setStyleSheet("QLabel{min-width: 300px;}");
                button = dlga.exec()

        else :

            from PyQt5.QtWidgets import QMessageBox
            dlgc = QMessageBox(self)
            dlgc.setWindowTitle("Drop Active dfs Status")
            dlgc.setText("No active dfs selected to drop.")
            dlgc.setStandardButtons(QMessageBox.Ok)
            dlgc.setStyleSheet("QLabel{min-width: 300px;}");
            button = dlgc.exec()


    def add_user_df_callback(self) :

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_dfc_dfs_Widget][add_user_df_callback]"))

        self.parent.display_add_user_df_to_dfc()

    def display_df_histories_callback(self) :

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_dfc_dfs_Widget][display_df_histories_callback]"))

        self.parent.display_dfcleanser_dfs_histories()



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                   System dfc dfs Widget end                   -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -             System dfc dfs histories Widget                   -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
class System_dfc_dfs_histories_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_dfc_dfs_histories_Widget]"))

        super().__init__()

        self.parent     =   dfparms[0]

        self.init_form()

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_dfc_dfs_histories_Widget] end"))

    def init_form(self):  

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_dfc_dfs_histories_Widget][init_form]"))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.SystemdfcdfshistoryLayout     =   QVBoxLayout()

        from PyQt5.QtWidgets import QLabel
        history_title_label   =   QLabel()
        history_title_label.setText("\n\ndfCleanser dataframes History\n")
        history_title_label.setAlignment(Qt.AlignCenter)
        history_title_label.resize(480,50)
        history_title_label.setStyleSheet("font-size: 18px; font-weight: bold; font-family: Arial; ")
        self.SystemdfcdfshistoryLayout.addWidget(history_title_label)

        from dfcleanser.Qt.data_import.DataImportWidgets import Data_Import_Histories_Widget
        callback_parms  =   [None,None]
        self.dfs_dfs_histories         =   Data_Import_Histories_Widget(callback_parms)
        self.SystemdfcdfshistoryLayout.addWidget(self.dfs_dfs_histories)
        
        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_dfc_dfs_histories_Widget][init_form] : histories loaded"))
        
        note_text   =   "The above tables define a history of all dfs that were imported or exported.\nTo get details on imports or exports go to Data Import or Data Export Chapters.\n"
        from PyQt5.QtWidgets import QLabel
        note_label   =   QLabel()
        note_label.setText(note_text)
        note_label.setAlignment(Qt.AlignCenter)
        note_label.resize(480,50)
        note_label.setStyleSheet("font-size: 14px; font-weight: normal; font-family: Arial; ")
        self.SystemdfcdfshistoryLayout.addWidget(note_label)
        
        from PyQt5.QtWidgets import QHBoxLayout
        dfcdfsbutonsLayout  =   QHBoxLayout()
        dfcdfsbutonsLayout.setAlignment(Qt.AlignHCenter)
        self.SystemdfcdfshistoryLayout.addLayout(dfcdfsbutonsLayout)

        self.SystemdfcdfshistoryLayout.addStretch()
        self.setLayout(self.SystemdfcdfshistoryLayout)

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_dfc_dfs_histories_Widget][init_form] end"))

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -             System dfc dfs histories Widget                   -#
# -----------------------------------------------------------------#

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -             System add user df to dfc Widget                  -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
class System_add_user_df_to_dfc_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_add_user_df_to_dfc_Widget]"))

        super().__init__()

        self.parent     =   dfparms[0]

        self.init_form()

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_add_user_df_to_dfc_Widget] end"))

    def init_form(self):  

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_add_user_df_to_dfc_Widget][init_form]"))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.SystemuserfdtodfcLayout     =   QVBoxLayout()

        from PyQt5.QtWidgets import QLabel
        user_df_title_label   =   QLabel()
        user_df_title_label.setText("\n\nAdding User dfs to dfcleanser\n")
        user_df_title_label.setAlignment(Qt.AlignCenter)
        user_df_title_label.resize(480,50)
        user_df_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.SystemuserfdtodfcLayout.addWidget(user_df_title_label)

        
        user_df_note1_text  =   "In order to use the dfcleanser chapter functions on a df the df must be made visible to dfcleanser.\n"
        user_df_note2_text  =   "A df can be viible to dfcleanser by importing it using dfcleanser or calling a dfc method to add the user defined df.\n"

        from PyQt5.QtWidgets import QLabel
        overview_title_label   =   QLabel()
        overview_title_label.setText("\n" + user_df_note1_text + user_df_note2_text + "\n")
        overview_title_label.setAlignment(Qt.AlignLeft)
        overview_title_label.resize(480,50)
        overview_title_label.setStyleSheet("font-size: 14px; font-weight: normal; font-family: Arial; ")
        self.SystemuserfdtodfcLayout.addWidget(overview_title_label)

        note_text   =   "Adding a user defined df to dfcleanser consists of a simple method call with 4 parameters\n"
        from PyQt5.QtWidgets import QLabel
        note_label   =   QLabel()
        note_label.setText(note_text)
        note_label.setAlignment(Qt.AlignLeft)
        note_label.resize(480,50)
        note_label.setStyleSheet("font-size: 14px; font-weight: normal; font-family: Arial; ")
        self.SystemuserfdtodfcLayout.addWidget(note_label)


        step0_text   =   "\ndfcleanser Method :"
        from PyQt5.QtWidgets import QLabel
        note0_label   =   QLabel()
        note0_label.setText(step0_text)
        note0_label.setAlignment(Qt.AlignLeft)
        note0_label.resize(480,50)
        note0_label.setStyleSheet("font-size: 14px; font-weight: bold; font-family: Arial; ")
        self.SystemuserfdtodfcLayout.addWidget(note0_label)

        step1_text   =   "\n    from dfcleanser.common.cfg import add_df_to_dfc"
        step2_text   =   "\n    add_df_to_dfc(df_title, user_df, df_source, df_notes)\n"
        from PyQt5.QtWidgets import QLabel
        note1_label   =   QLabel()
        note1_label.setText( step1_text + step2_text)
        note1_label.setAlignment(Qt.AlignLeft)
        note1_label.resize(480,50)
        note1_label.setStyleSheet("font-size: 14px; font-weight: normal; font-family: Arial; ")
        self.SystemuserfdtodfcLayout.addWidget(note1_label)
        
        stepa_text   =   "\nadd_df_to_dfc Parameters :"
        from PyQt5.QtWidgets import QLabel
        notea_label   =   QLabel()
        notea_label.setText(stepa_text)
        notea_label.setAlignment(Qt.AlignLeft)
        notea_label.resize(480,50)
        notea_label.setStyleSheet("font-size: 14px; font-weight: bold; font-family: Arial; ")
        self.SystemuserfdtodfcLayout.addWidget(notea_label)

        step3_text   =   "\n df_title : descriptive title used to identify a df"
        step4_text   =   "\n user_df : user defined dataframe"
        step5_text   =   "\n df_source : the python code used to build the df. (commentary)"
        step6_text   =   "\n df_notes : descriptive notes to fully identify the dataframe (commentary)\n\n"

        from PyQt5.QtWidgets import QLabel
        note2_label   =   QLabel()
        note2_label.setText(step3_text + step4_text + step5_text + step6_text) 
        note2_label.setAlignment(Qt.AlignLeft)
        note2_label.resize(480,50)
        note2_label.setStyleSheet("font-size: 14px; font-weight: normal; font-family: Arial; ")
        self.SystemuserfdtodfcLayout.addWidget(note2_label)
        
        from PyQt5.QtWidgets import QHBoxLayout
        dfcdfsbutonsLayout  =   QHBoxLayout()
        dfcdfsbutonsLayout.setAlignment(Qt.AlignHCenter)
        self.SystemuserfdtodfcLayout.addLayout(dfcdfsbutonsLayout)

        self.SystemuserfdtodfcLayout.addStretch()
        self.setLayout(self.SystemuserfdtodfcLayout)

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_add_user_df_to_dfc_Widget][init_form] end"))


    def dfc_dfs_add_user_df_return_callback(self) :

         if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_dfc_dfs_histories_Widget][dfc_dfs_add_user_df_return_callback]"))

            self.parent.display_dfcleanser_dfs()

    def dfc_dfs_add_user_df_help_callback(self) :

         if(is_debug_on(System_ID,"DEBUG_SYSTEM_DFS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_dfc_dfs_histories_Widget][dfc_dfs_add_user_df_help_callback)]"))


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -             System dfc dfs histories Widget                   -#
# -----------------------------------------------------------------#





# -----------------------------------------------------------------#
# -             Table view and Model for Python info              -#
# -----------------------------------------------------------------#

class SystemPythonInfoModel(QtCore.QAbstractTableModel):
    def __init__(self, pythondata, colheaders):

        super(SystemPythonInfoModel,self).__init__()
        self._data          =   pythondata
        self.column_names   =   colheaders

    def reload_data(self,pythondata) :
        self._data = pythondata

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
            #odd = (column % 2) 
            #if(column == 0) :
            return(Qt.AlignLeft)
            #elif(column == 1) :
            #    return(Qt.AlignLeft)
            #else :
            #    return(Qt.AlignLeft)

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

# -----------------------------------------------------------------#
# -                 Table view system infotable                   -#
# -----------------------------------------------------------------#
class SystemPythonInfoTable(QtWidgets.QTableView):

    def __init__(self,  **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemPythonInfoTable] : init"))

        self.init_tableview()

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemPythonInfoTable] : end"))

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self):
        
        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemPythonInfoTable] : reload_data"))

        python_data     =   self.load_python_info_data()
        self.model.reload_data(python_data)
    
    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO_DETAILS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemPythonInfoTable][init_tableview]"))

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        pythondata     =   self.load_python_info_data()
        
        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO_DETAILS")) :
           add_debug_to_log("SystemWidgets",print_to_string("[SystemPythonInfoTable][init_tableview] :headers",self.column_headers))

        if(self.model is None) :
            self.model = SystemPythonInfoModel(pythondata,self.column_headers)
            self.setModel(self.model)

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO_DETAILS")) :
           add_debug_to_log("SystemWidgets",print_to_string("[SystemPythonInfoTable][init_tableview] : model loaded"))

        self.num_rows   =   len(pythondata)
        
        if(self.num_rows < 15) :
            new_height  =   (40 + (self.num_rows * DEFAULT_ROW_HEIGHT))
        else :
            new_height  =   (40 + (15 * DEFAULT_ROW_HEIGHT))

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
        nrows = len(pythondata)
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
    def load_python_info_data(self):

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO_DETAILS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemPythonInfoTable][load_python_info_data]"))

        data    =   []

        infotitles     =   ["Version","API","Info"]
        infovalues     =   [str(get_python_version()),str(sys.api_version),str(sys.version_info)]
            
        for i in range(len(infotitles)) :
                
            data_row    =   []

            data_row.append(infotitles[i])
            data_row.append(infovalues[i])

            data.append(data_row)

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO_DETAILS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemPythonInfoTable] : data"))
            for j in range(len(data)) :
                add_debug_to_log("SystemWidgets",print_to_string("  [",j,"] : ",data[j]))

        self.column_headers     =   ["Stat Name","Stat Value"]
        self.column_widths      =   [250,720]

        return(data)

# -----------------------------------------------------------------#
# -               Table view active dfs table end                 -#
# -----------------------------------------------------------------#

"""
#----------------------------------------------------------
#   get formatted representation of python version
#----------------------------------------------------------
"""    
def get_python_version() :
    
    import sys
    sysver = sys.version
    
    try :
        cindex = sysver.index("(")
        vermaj = sysver[0:(cindex-1)]
    except :
        vermaj =  sysver
        
    vermaj.strip()
    
    return(vermaj)


# -----------------------------------------------------------------#
# -            Table view and Model for Notebook info             -#
# -----------------------------------------------------------------#

class dfcleanserInfoModel(QtCore.QAbstractTableModel):
    def __init__(self, notebookdata, colheaders):

        super(dfcleanserInfoModel,self).__init__()
        self._data          =   notebookdata
        self.column_names   =   colheaders

    def reload_data(self,notebookdata) :
        self._data = notebookdata

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
            #odd = (column % 2) 
            #if(column == 0) :
            return(Qt.AlignLeft)
            #elif(column == 1) :
            #    return(Qt.AlignLeft)
            #else :
            #    return(Qt.AlignLeft)

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

# -----------------------------------------------------------------#
# -                 Table view system infotable                   -#
# -----------------------------------------------------------------#
class dfcleanserInfoTable(QtWidgets.QTableView):

    def __init__(self,  **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemNotebookInfoTable] : init"))

        self.init_tableview()

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemNotebookInfoTable] : end"))

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self):
        
        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemNotebookInfoTable] : reload_data"))

        notebook_data     =   self.load_notebook_info_data()
        self.model.reload_data(notebook_data)
    
    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO_DETAILS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemNotebookInfoTable][init_tableview]"))

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        dfcleanserInfoTabledata     =   self.load_dfcleanser_info_data()
        
        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO_DETAILS")) :
           add_debug_to_log("SystemWidgets",print_to_string("[dfcleanserInfoTable][init_tableview] :headers",self.column_headers))

        if(self.model is None) :
            self.model = dfcleanserInfoModel(dfcleanserInfoTabledata,self.column_headers)
            self.setModel(self.model)

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO_DETAILS")) :
           add_debug_to_log("SystemWidgets",print_to_string("[dfcleanserInfoTable][init_tableview] : model loaded"))

        self.num_rows   =   len(dfcleanserInfoTabledata)
        
        if(self.num_rows < 15) :
            new_height  =   (40 + self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   (40 + 15 * DEFAULT_ROW_HEIGHT)

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
        nrows = len(dfcleanserInfoTabledata)
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
    def load_dfcleanser_info_data(self):

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO_DETAILS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfcleanserInfoTable][load_dfcleanser_info_data]"))

        data    =   []

        infotitles     =   ["dfcleanser path"]
        infovalues     =   [str(cfg.get_dfcleanser_location())]
            
        for i in range(len(infotitles)) :
                
            data_row    =   []

            data_row.append(infotitles[i])
            data_row.append(infovalues[i])

            data.append(data_row)

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO_DETAILS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfcleanserInfoTable] : data"))
            for j in range(len(data)) :
                add_debug_to_log("SystemWidgets",print_to_string("  [",j,"] : ",data[j]))

        self.column_headers     =   ["Stat Name","Stat Value"]
        self.column_widths      =   [250,720]

        return(data)

# -----------------------------------------------------------------#
# -             Table view notebook info table end                -#
# -----------------------------------------------------------------#



# -----------------------------------------------------------------#
# -            Table view and Model for Notebook info             -#
# -----------------------------------------------------------------#

class SystemNotebookInfoModel(QtCore.QAbstractTableModel):
    def __init__(self, notebookdata, colheaders):

        super(SystemNotebookInfoModel,self).__init__()
        self._data          =   notebookdata
        self.column_names   =   colheaders

    def reload_data(self,notebookdata) :
        self._data = notebookdata

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
            #odd = (column % 2) 
            #if(column == 0) :
            return(Qt.AlignLeft)
            #elif(column == 1) :
            #    return(Qt.AlignLeft)
            #else :
            #    return(Qt.AlignLeft)

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

# -----------------------------------------------------------------#
# -                 Table view system infotable                   -#
# -----------------------------------------------------------------#
class SystemNotebookInfoTable(QtWidgets.QTableView):

    def __init__(self,  **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemNotebookInfoTable] : init"))

        self.init_tableview()

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemNotebookInfoTable] : end"))

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self):
        
        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemNotebookInfoTable] : reload_data"))

        notebook_data     =   self.load_notebook_info_data()
        self.model.reload_data(notebook_data)
    
    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO_DETAILS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemNotebookInfoTable][init_tableview]"))

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        notebookdata     =   self.load_notebook_info_data()
        
        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO_DETAILS")) :
           add_debug_to_log("SystemWidgets",print_to_string("[SystemNotebookInfoTable][init_tableview] :headers",self.column_headers))

        if(self.model is None) :
            self.model = SystemNotebookInfoModel(notebookdata,self.column_headers)
            self.setModel(self.model)

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO_DETAILS")) :
           add_debug_to_log("SystemWidgets",print_to_string("[SystemNotebookInfoTable][init_tableview] : model loaded"))

        self.num_rows   =   len(notebookdata)
        
        if(self.num_rows < 15) :
            new_height  =   (40 + self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   (40 + 15 * DEFAULT_ROW_HEIGHT)

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
        nrows = len(notebookdata)
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
    def load_notebook_info_data(self):

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO_DETAILS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemNotebookInfoTable][load_notebook_info_data]"))

        data    =   []

        infotitles     =   ["Notebook Path","Notebook Name"]
        infovalues     =   [str(cfg.get_notebookPath()),str(cfg.get_notebookName())]
            
        for i in range(len(infotitles)) :
                
            data_row    =   []

            data_row.append(infotitles[i])
            data_row.append(infovalues[i])

            data.append(data_row)

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO_DETAILS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemNotebookInfoTable] : data"))
            for j in range(len(data)) :
                add_debug_to_log("SystemWidgets",print_to_string("  [",j,"] : ",data[j]))

        self.column_headers     =   ["Stat Name","Stat Value"]
        self.column_widths      =   [250,720]

        return(data)

# -----------------------------------------------------------------#
# -             Table view notebook info table end                -#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -            Table view and Model for package info              -#
# -----------------------------------------------------------------#

class SystemPackageInfoModel(QtCore.QAbstractTableModel):
    def __init__(self, notebookdata, colheaders):

        super(SystemPackageInfoModel,self).__init__()
        self._data          =   notebookdata
        self.column_names   =   colheaders

    def reload_data(self,notebookdata) :
        self._data = notebookdata

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
            #odd = (column % 2) 
            if(column == 0) :
                return(Qt.AlignLeft)
            elif(column == 1) :
                return(Qt.AlignCenter)
            else :
                return(Qt.AlignCenter)

        if role==Qt.BackgroundColorRole:
            if(column == 0):
                bgcolor = QtGui.QBrush(QColor(240, 234, 193))
            elif(column == 3) :
                cell_value  =  self._data[index.row()][index.column()] 
                if(cell_value == "OK") :
                    bgcolor = QtGui.QBrush(QColor(153, 255, 153))
                elif(cell_value == "Error") :
                    bgcolor = QtGui.QBrush(QColor(255, 102, 102))
                else :
                    bgcolor = QtGui.QBrush(QColor(255, 255, 204))
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

# -----------------------------------------------------------------#
# -                 Table view system infotable                   -#
# -----------------------------------------------------------------#
class SystemPackageInfoTable(QtWidgets.QTableView):

    def __init__(self,  **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemPackageInfoTable] : init"))

        self.init_tableview()

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemPackageInfoTable] : end"))

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self):
        
        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemPackageInfoTable] : reload_data"))

        package_data     =   self.load_package_info_data()
        self.model.reload_data(package_data)
    
    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO_DETAILS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemPackageInfoTable][init_tableview]"))

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        packagedata     =   self.load_package_info_data()
        
        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO_DETAILS")) :
           add_debug_to_log("SystemWidgets",print_to_string("[SystemPackageInfoTable][init_tableview] :headers",self.column_headers))

        if(self.model is None) :
            self.model = SystemPackageInfoModel(packagedata,self.column_headers)
            self.setModel(self.model)

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO_DETAILS")) :
           add_debug_to_log("SystemWidgets",print_to_string("[SystemPackageInfoTable][init_tableview] : model loaded"))

        self.num_rows   =   len(packagedata)
        
        if(self.num_rows < 10) :
            new_height  =   (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   (10 * DEFAULT_ROW_HEIGHT)

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
        nrows = len(packagedata)
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
    def load_package_info_data(self):

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO_DETAILS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemPackageInfoTable][load_package_info_data]"))

        data    =   []

        GREEN       =   0
        YELLOW      =   1
        RED         =   2

        testedModules               =   ["Python","IPython","ipywidgets","ipykernel","notebook",
                                         "pandas","scikit-learn","matplotlib","seaborn","pillow","numpy","scipy",
                                         "json","sqlalchemy","pymysql","mysql-connector-python",
                                         "pyodbc","pymssql","sqlite3","psycopg2","cx-oracle","lxml","openpyxl",
                                         "geopy","googlemaps","arcgis","xlrd","folium","kaleido",
                                         "juypter_core","jupyter_client","jupyter_server","traitlets",
                                         "PyQt5","PyQt5-Qt5","PyQt5-sip"]
    
        testedmoduleVersions        =   ["3.10.11","8.13.2","8.0.6","6.23.1","6.5.4",
                                         "1.5.3","1.2.1","3.7.1","0.13.0","9.0.0","1.24.3","1.10.1",
                                         "2.0.9","1.4.39","1.0.2","8.0.31",
                                         "4.0.35","2.2.5","3.42.0","2.9.3","8.3.0","4.9.3","3.1.2",
                                         "2.3.0","2.5.1","2.0.0","2.0.1","0.14.0","0.2.1",
                                         "5.3.0","8.2.0","2.5.0","5.9.0",
                                         "5.15.9","5.15.2","12.12.1"]

        installedmoduleVersions     =   []


        package_list    =   get_env_package_list()

        python_version = str(get_python_version())
        hash_index  =  python_version.find("|")
        installedmoduleVersions.append(python_version[:(hash_index - 1)])

        import IPython
        installedmoduleVersions.append(str(IPython.__version__))


        try :
            import ipywidgets
            installedmoduleVersions.append(str(ipywidgets.__version__))
        except :
            installedmoduleVersions.append(str("-1"))
        
        try :
            import ipykernel
            installedmoduleVersions.append(str(ipykernel.__version__))
        except :
            installedmoduleVersions.append(str("-1"))

        try :
            import notebook
            installedmoduleVersions.append(str(notebook.__version__))
        except :
            installedmoduleVersions.append(str("-1"))
    
        try :
            import pandas
            installedmoduleVersions.append(str(pandas.__version__))
        except :
            installedmoduleVersions.append(str("-1"))

        try :
            import sklearn
            installedmoduleVersions.append(str(sklearn.__version__))
        except :
            installedmoduleVersions.append(str("-1"))

        try :
            import matplotlib
            installedmoduleVersions.append(str(matplotlib.__version__))
        except Exception as e :
            package_version     =  get_env_package_version(package_list,"matplotlib") 
            installedmoduleVersions.append(str(package_version))
         
        try :
            import seaborn
            installedmoduleVersions.append(str(seaborn.__version__))
        except Exception as e :
            installedmoduleVersions.append(str("-1"))
   
        try :
            import PIL
            installedmoduleVersions.append(str(PIL.__version__))
        except Exception as e :
            installedmoduleVersions.append(str("-1"))

        try :
            import numpy
            installedmoduleVersions.append(str(numpy.__version__))
        except :
            installedmoduleVersions.append(str("-1"))
    
        try :
            import scipy
            installedmoduleVersions.append(str(scipy.__version__))
        except :
            installedmoduleVersions.append(str("-1"))
    
        try :
            import json
            installedmoduleVersions.append(str(json.__version__))
        except :
            installedmoduleVersions.append(str("-1"))

        try :
            import sqlalchemy
            installedmoduleVersions.append(str(sqlalchemy.__version__))
        except :
            installedmoduleVersions.append(str("-1"))
    
        try :
            import pymysql
            installedmoduleVersions.append(str(pymysql.__version__))
        except :
            installedmoduleVersions.append(str("-1"))

        try :
            import mysql.connector    
            installedmoduleVersions.append(str(mysql.connector.__version__))
        except :
            installedmoduleVersions.append(str("-1"))
        
        try :
            import pyodbc    
            installedmoduleVersions.append(str(pyodbc.connector.__version__))
        except Exception as e:
            package_version     =  get_env_package_version(package_list,"pyodbc") 
            installedmoduleVersions.append(str(package_version))
 
        try :
            import pymssql    
            installedmoduleVersions.append(str(pymssql.__version__))
        except :
            installedmoduleVersions.append(str("-1"))
        
        try :
            import sqlite3    
            installedmoduleVersions.append(str(sqlite3.sqlite_version))
        except Exception as e:
            installedmoduleVersions.append(str("unknown"))
   
        try :
            import psycopg2
    
            pgversion =  str(psycopg2.__version__)
            found = pgversion.find("(")
            if(found > 0)  :
                installedmoduleVersions.append(pgversion[0:found-1])
            else :
                installedmoduleVersions.append(pgversion)
        except :
            installedmoduleVersions.append(str("-1"))

        try :
            import cx_Oracle    
            installedmoduleVersions.append(str(cx_Oracle.__version__))
        except :
            installedmoduleVersions.append(str("-1"))
        
        try :
            import lxml    
            installedmoduleVersions.append(str(lxml.__version__))
        except :
            installedmoduleVersions.append(str("-1"))
        
        try :
            import openpyxl    
            installedmoduleVersions.append(str(openpyxl.__version__))
        except :
            installedmoduleVersions.append(str("-1"))
    
        try :
            import geopy    
            installedmoduleVersions.append(str(geopy.__version__))
        except :
            installedmoduleVersions.append(str("-1"))

        try :
            import googlemaps    
            installedmoduleVersions.append(str(googlemaps.__version__))
        except :
            installedmoduleVersions.append(str("-1"))
    
        try :
            import arcgis    
            installedmoduleVersions.append(str(arcgis.__version__))
        except :
            installedmoduleVersions.append(str("-1"))
    
        try :
            import xlrd    
            installedmoduleVersions.append(str(xlrd.__version__))
        except :
            installedmoduleVersions.append(str("-1"))
    
        try :
            import folium    
            installedmoduleVersions.append(str(folium.__version__))
        except :
            installedmoduleVersions.append(str("-1"))
    
        try :
            import kaleido    
            installedmoduleVersions.append(str(kaleido.__version__))
        except :
            installedmoduleVersions.append(str("-1"))
    
        try :
            import jupyter_core    
            installedmoduleVersions.append(str(jupyter_core.__version__))
        except :
            installedmoduleVersions.append(str("-1"))
    
        try :
            import jupyter_client    
            installedmoduleVersions.append(str(jupyter_client.__version__))
        except :
            installedmoduleVersions.append(str("-1"))
    
        try :
            import jupyter_server    
            installedmoduleVersions.append(str(jupyter_server.__version__))
        except :
            installedmoduleVersions.append(str("-1"))
        
        try :
            import traitlets    
            installedmoduleVersions.append(str(traitlets.__version__))
        except :
            installedmoduleVersions.append(str("-1"))


        try :
            from PyQt5.Qt import PYQT_VERSION_STR   
            installedmoduleVersions.append(PYQT_VERSION_STR)
        except :
            installedmoduleVersions.append(str("-1"))
    
        try :
            from PyQt5.QtCore import QT_VERSION_STR    
            installedmoduleVersions.append(QT_VERSION_STR)
        except :
            installedmoduleVersions.append(str("-1"))

        installedmoduleVersions.append(str("unknown"))

        colorList = [] 
    
        for i in range(len(testedModules)) :

            if(installedmoduleVersions[i] == "not installed") :
                colorRow = YELLOW
            elif(installedmoduleVersions[i] == "unknown") :
                colorRow = YELLOW
            elif(testedmoduleVersions[i] > installedmoduleVersions[i]) :
                colorRow = RED
            elif(testedmoduleVersions[i] < installedmoduleVersions[i]) :
                colorRow = YELLOW
            else :
                colorRow = GREEN
            
            colorList.append(colorRow)

        for i in range(len(testedModules)) :
                
            data_row    =   []

            data_row.append(testedModules[i])
            data_row.append(testedmoduleVersions[i])
            data_row.append(installedmoduleVersions[i])

            if(colorList[i] == RED)      :      data_row.append("Error")
            elif(colorList[i] == YELLOW) :      data_row.append("Warning")
            else :                              data_row.append("OK")

            data.append(data_row)

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO_DETAILS")) :
            add_debug_to_log("SystemWidgets",print_to_string("[SystemPackageInfoTable] : data"))
            for j in range(len(data)) :
                add_debug_to_log("SystemWidgets",print_to_string("  [",j,"] : ",data[j]))

        self.column_headers     =   ["Package Name","Tested With Version","Installed Version","Status"]
        self.column_widths      =   [300,220,220,220]

        return(data)

# -----------------------------------------------------------------#
# -             Table view package info table end                 -#
# -----------------------------------------------------------------#



"""
#--------------------------------------------------------------------------
#   get environment packages list
#--------------------------------------------------------------------------
"""    
def get_env_package_list() :
    
    import pkg_resources
    sysver = sys.version
    
    try :
        installed_packages = pkg_resources.working_set
        installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
            for i in installed_packages])
    except :
        return(["no packages found"])
        
    return(installed_packages_list)



"""
#--------------------------------------------------------------------------
#   get environment package version
#--------------------------------------------------------------------------
"""    
def get_env_package_version(package_list,package) :
    
    for i in range (len(package_list)) :

        if(package_list[i].find(package+"==") > -1) :

            version_index = package_list[i].find("==")
            if(version_index > -1) :
                return(package_list[i][version_index+2:])
            else :
                return("unknown")
    
    return("unknown")




# -----------------------------------------------------------------#
# -                     System Info Widget                        -#
# -----------------------------------------------------------------#
class System_Info_Widget(QtWidgets.QWidget):

    def __init__(self):  

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_Info_Widget]"))

        super().__init__()

        self.init_form()

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_Info_Widget] end"))

    def init_form(self):  

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_Info_Widget][init_form]"))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.SystemInfoLayout     =   QVBoxLayout()

        from PyQt5.QtWidgets import QLabel
        python_info_title_label   =   QLabel()
        python_info_title_label.setText("\n\nInstalled Python Info")
        python_info_title_label.setAlignment(Qt.AlignCenter)
        python_info_title_label.resize(480,50)
        python_info_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.SystemInfoLayout.addWidget(python_info_title_label)

        self.python_info_data         =   SystemPythonInfoTable()
        self.SystemInfoLayout.addWidget(self.python_info_data)

        from PyQt5.QtWidgets import QLabel
        dfcleanser_info_title_label   =   QLabel()
        dfcleanser_info_title_label.setText("\ndfcleanser Info")
        dfcleanser_info_title_label.setAlignment(Qt.AlignCenter)
        dfcleanser_info_title_label.resize(480,50)
        dfcleanser_info_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.SystemInfoLayout.addWidget(dfcleanser_info_title_label)

        self.dfcleanser_info_data         =   dfcleanserInfoTable()
        self.SystemInfoLayout.addWidget(self.dfcleanser_info_data)

        from PyQt5.QtWidgets import QLabel
        notebook_info_title_label   =   QLabel()
        notebook_info_title_label.setText("\nNotebook Info")
        notebook_info_title_label.setAlignment(Qt.AlignCenter)
        notebook_info_title_label.resize(480,50)
        notebook_info_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.SystemInfoLayout.addWidget(notebook_info_title_label)

        self.notebook_info_data         =   SystemNotebookInfoTable()
        self.SystemInfoLayout.addWidget(self.notebook_info_data)

        from PyQt5.QtWidgets import QLabel
        package_info_title_label   =   QLabel()
        package_info_title_label.setText("\nPackage Info")
        package_info_title_label.setAlignment(Qt.AlignCenter)
        package_info_title_label.resize(480,50)
        package_info_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.SystemInfoLayout.addWidget(package_info_title_label)

        self.package_info_data         =   SystemPackageInfoTable()
        self.SystemInfoLayout.addWidget(self.package_info_data)
        self.SystemInfoLayout.addStretch()

        self.setLayout(self.SystemInfoLayout)

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_Info_Widget][init_form] end"))


# -----------------------------------------------------------------#
# -                    System Info Widget end                     -#
# -----------------------------------------------------------------#



# -----------------------------------------------------------------#
# -                    System About Widget                        -#
# -----------------------------------------------------------------#
class System_About_Widget(QtWidgets.QWidget):

    def __init__(self,  **kwargs):  

        super().__init__()

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_About_Widget]"))

        self.init_form()

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_About_Widget] end"))

    def init_form(self):  

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_About_Widget][init_form]"))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.SystemAboutLayout     =   QVBoxLayout()

        from PyQt5.QtWidgets import QLabel
        author_title_label   =   QLabel()
        author_title_label.setText("\n\nAuthor : Rick Krasinski\n")
        author_title_label.setAlignment(Qt.AlignCenter)
        author_title_label.resize(480,50)
        author_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.SystemAboutLayout.addWidget(author_title_label)

        from PyQt5.QtWidgets import QLabel
        email_title_label   =   QLabel()
        email_title_label.setText("email : rickmkrasinski@gmail.com\n")
        email_title_label.setAlignment(Qt.AlignCenter)
        email_title_label.resize(480,50)
        email_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.SystemAboutLayout.addWidget(email_title_label)

        from PyQt5.QtWidgets import QLabel
        version_title_label   =   QLabel()
        version_title_label.setText("Dataframe Cleanser Version : v1.0.0\n")
        version_title_label.setAlignment(Qt.AlignCenter)
        version_title_label.resize(480,50)
        version_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.SystemAboutLayout.addWidget(version_title_label)
        self.SystemAboutLayout.addStretch()

        self.setLayout(self.SystemAboutLayout)

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_About_Widget][init_form] end"))


# -----------------------------------------------------------------#
# -                    System Info Widget end                     -#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                      System Files Widgets                     -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

# -----------------------------------------------------------------#
# -           Table view and Model for dfcleanser files           -#
# -----------------------------------------------------------------#

class dfcleansercfgfilesModel(QtCore.QAbstractTableModel):
    def __init__(self, cfgfiledata, colheaders):

        super(dfcleansercfgfilesModel,self).__init__()
        self._data          =   cfgfiledata
        self.column_names   =   colheaders

    def reload_data(self,filedata) :
        self._data = filedata

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
            #odd = (column % 2) 
            #if(column == 0) :
            return(Qt.AlignLeft)
            #elif(column == 1) :
            #    return(Qt.AlignLeft)
            #else :
            #    return(Qt.AlignLeft)

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

# -----------------------------------------------------------------#
# -                 Table view system infotable                   -#
# -----------------------------------------------------------------#
class dfcleansercfgfilesTable(QtWidgets.QTableView):

    def __init__(self,  **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfcleansercfgfilesTable] : init"))

        self.init_tableview()

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES") ) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfcleansercfgfilesTable] : end"))

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self):
        
        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfcleansercfgfilesTable] : reload_data"))

        cfgfiles_data     =   self.load_cfgfiles_info_data()
        self.model.reload_data(cfgfiles_data)
    
    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfcleansercfgfilesTable][init_tableview]"))

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        dfcleansercfgfilesTabledata     =   self.load_dfcleanser_cfgfiles_data()
        
        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
           add_debug_to_log("SystemWidgets",print_to_string("[dfcleansercfgfilesTable][init_tableview] :headers",self.column_headers))

        if(self.model is None) :
            self.model = dfcleanserInfoModel(dfcleansercfgfilesTabledata,self.column_headers)
            self.setModel(self.model)

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES") ) :
           add_debug_to_log("SystemWidgets",print_to_string("[dfcleansercfgfilesTable][init_tableview] : model loaded"))

        self.num_rows   =   len(dfcleansercfgfilesTabledata)
        
        if(self.num_rows < 15) :
            new_height  =   (40 + self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   (40 + 15 * DEFAULT_ROW_HEIGHT)

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
        nrows = len(dfcleansercfgfilesTabledata)
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
    def load_dfcleanser_cfgfiles_data(self):

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfcleanserInfoTable][load_dfcleanser_cfgfiles_data]"))

        data    =   []

        infotitles     =   ["dfcleanserCommon_config",
                            "dfcleanserCommon_import_history",
                            "dfcleanserCommon_export_history"]
        
        infovalues     =   [str(cfg.get_dfcleanser_location()+"files"),
                            str(cfg.get_dfcleanser_location()+"files"),
                            str(cfg.get_dfcleanser_location()+"files")]
            
        for i in range(len(infotitles)) :
                
            data_row    =   []

            data_row.append(infotitles[i])
            data_row.append(infovalues[i])

            data.append(data_row)

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfcleansercfgfiles] : data"))
            for j in range(len(data)) :
                add_debug_to_log("SystemWidgets",print_to_string("  [",j,"] : ",data[j]))

        self.column_headers     =   ["File","Location"]
        self.column_widths      =   [250,720]

        return(data)

# -----------------------------------------------------------------#
# -        Table view dfcleanser cfg files table end              -#
# -----------------------------------------------------------------#

# -----------------------------------------------------------------#
# -             Table view and Model for notebook files           -#
# -----------------------------------------------------------------#

class notebookcfgfilesModel(QtCore.QAbstractTableModel):
    def __init__(self, cfgfiledata, colheaders):

        super(notebookcfgfilesModel,self).__init__()
        self._data          =   cfgfiledata
        self.column_names   =   colheaders

    def reload_data(self,filedata) :
        self._data = filedata

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
            #odd = (column % 2) 
            #if(column == 0) :
            return(Qt.AlignLeft)
            #elif(column == 1) :
            #    return(Qt.AlignLeft)
            #else :
            #    return(Qt.AlignLeft)

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

# -----------------------------------------------------------------#
# -                 Table view system infotable                   -#
# -----------------------------------------------------------------#
class notebookcfgfilesTable(QtWidgets.QTableView):

    def __init__(self,  **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[notebookcfgfilesTable] : init"))

        self.init_tableview()

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[notebookcfgfilesTable] : end"))

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self):
        
        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[notebookcfgfilesTable] : reload_data"))

        cfgfiles_data     =   self.load_cfgfiles_info_data()
        self.model.reload_data(cfgfiles_data)
    
    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[notebookcfgfilesTable][init_tableview]"))

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        notebookcfgfilesTabledata     =   self.load_dfcleanser_cfgfiles_data()
        
        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
           add_debug_to_log("SystemWidgets",print_to_string("[notebookcfgfilesTable][init_tableview] :headers",self.column_headers))

        if(self.model is None) :
            self.model = dfcleanserInfoModel(notebookcfgfilesTabledata,self.column_headers)
            self.setModel(self.model)

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
           add_debug_to_log("SystemWidgets",print_to_string("[notebookcfgfilesTable][init_tableview] : model loaded"))

        self.num_rows   =   len(notebookcfgfilesTabledata)
        
        if(self.num_rows < 15) :
            new_height  =   (40 + self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   (40 + 15 * DEFAULT_ROW_HEIGHT)

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
        nrows = len(notebookcfgfilesTabledata)
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
    def load_dfcleanser_cfgfiles_data(self):

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[notebookcfgfilesTable][load_dfcleanser_cfgfiles_data]"))

        data    =   []

        infotitles     =   [str(cfg.get_notebookName()) + "_config",
                            str(cfg.get_notebookName()) + "_errorlog"]
        
        infovalues     =   [str(cfg.get_notebookPath()) + "\\" + str(cfg.get_notebookName()) + "_files",
                            str(cfg.get_notebookPath()) + "\\" + str(cfg.get_notebookName()) + "_files"]
            
        for i in range(len(infotitles)) :
                
            data_row    =   []

            data_row.append(infotitles[i])
            data_row.append(infovalues[i])

            data.append(data_row)

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfcleansercfgfiles] : data"))
            for j in range(len(data)) :
                add_debug_to_log("SystemWidgets",print_to_string("  [",j,"] : ",data[j]))

        self.column_headers     =   ["File","Location"]
        self.column_widths      =   [275,700]

        return(data)



# -----------------------------------------------------------------#
# -                     System files Widget                       -#
# -----------------------------------------------------------------#
class cfg_files_Widget(QtWidgets.QWidget):

    def __init__(self,parms):  


        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[cfg_files_Widget]"))

        super().__init__()

        self.parent     =   parms[0]


        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[cfg_files_Widget]"))

        self.init_form()

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[cfg_files_Widget] end"))

    def init_form(self):  

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[cfg_files_Widget][init_form]"))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.dfccfgLayout     =   QVBoxLayout()

        from PyQt5.QtWidgets import QLabel
        dfc_cfg_title_label   =   QLabel()
        dfc_cfg_title_label.setText("\n\ndfcleanser Configuration Files")
        dfc_cfg_title_label.setAlignment(Qt.AlignCenter)
        dfc_cfg_title_label.resize(480,50)
        dfc_cfg_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.dfccfgLayout.addWidget(dfc_cfg_title_label)

        self.dfc_cfg_files_data         =   dfcleansercfgfilesTable()
        self.dfc_cfg_files_data.doubleClicked.connect(self.select_dfc_cfg_file)
        self.dfccfgLayout.addWidget(self.dfc_cfg_files_data)

        from PyQt5.QtWidgets import QLabel
        notebook_cfg_title_label   =   QLabel()
        notebook_cfg_title_label.setText("\n\nnotebook Configuration Files")
        notebook_cfg_title_label.setAlignment(Qt.AlignCenter)
        notebook_cfg_title_label.resize(480,50)
        notebook_cfg_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.dfccfgLayout.addWidget(notebook_cfg_title_label)

        self.notebook_cfg_files_data         =   notebookcfgfilesTable()
        self.notebook_cfg_files_data.doubleClicked.connect(self.select_notebook_cfg_file)

        self.dfccfgLayout.addWidget(self.notebook_cfg_files_data)


        from PyQt5.QtWidgets import QLabel
        self.dspacer_label   =   QLabel()
        self.dspacer_label.setText("\n\n\n\n\n\n")
        self.dspacer_label.setAlignment(Qt.AlignCenter)
        self.dspacer_label.resize(480,50)
        self.dspacer_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")

        from PyQt5.QtWidgets import QPushButton        
        self.debug_button       =   QPushButton("Debug")
        self.debug_button.setFixedSize(200,70)
        self.debug_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        
        self.debug_button.clicked.connect(self.display_debug_log)

        self.dfccfgLayout.addWidget(self.dspacer_label)

        from PyQt5.QtWidgets import QHBoxLayout
        dfcdfsbutonsLayout  =   QHBoxLayout()
        dfcdfsbutonsLayout.addWidget(self.debug_button)
        dfcdfsbutonsLayout.setAlignment(Qt.AlignHCenter)

        self.dfccfgLayout.addLayout(dfcdfsbutonsLayout)
        self.dfccfgLayout.addStretch()

        self.setLayout(self.dfccfgLayout)

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[cfg_files_Widget][init_form] end"))


    def select_dfc_cfg_file(self) :

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[cfg_files_Widget][select_dfc_cfg_file]"))

        for idx in self.dfc_cfg_files_data.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[cfg_files_Widget][select_dfc_cfg_file] ",row_number,column_number))

        model   =   self.dfc_cfg_files_data.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][column_number]

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :    
            add_debug_to_log("SystemWidgets",print_to_string("[cfg_files_Widget][select_dfc_cfg_file] : cell value [",cell,"]",type(cell),len(cell)))

        self.parent.display_dfcleanser_file(cell)

    def select_notebook_cfg_file(self) :

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[cfg_files_Widget][select_notebook_cfg_file]"))

        for idx in self.notebook_cfg_files_data.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[cfg_files_Widget][select_notebook_cfg_file] ",row_number,column_number))

        model   =   self.notebook_cfg_files_data.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][column_number]

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :    
            add_debug_to_log("SystemWidgets",print_to_string("[cfg_files_Widget][select_notebook_cfg_file] : cell value [",cell,"]",type(cell),len(cell)))

        self.parent.display_dfcleanser_file(cell)

    def display_debug_log(self) :

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[display_debug_log]"))

        self.parent.display_dfcleanser_debug(self.parent,0)

# -----------------------------------------------------------------#
# -                     System files Widget                       -#
# -----------------------------------------------------------------#
class dfc_file_Widget(QtWidgets.QWidget):

    def __init__(self,parms):  

        from dfcleanser.common.cfg import dfc_debug_log
        debug_file  =   dfc_debug_log.get_debuglog_file_name()
        
        self.file_name      =   parms[1]
        
        self.allow_debug    =   True

        if(debug_file == self.file_name) :
            self.allow_debug    =   False


        if((is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug)) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfc_file_Widget]"))

        super().__init__()

        self.parent     =   parms[0]

        if((is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug)) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfc_file_Widget]"))

        self.init_form()

        if( (is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug)) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfc_file_Widget] end"))

    def reload_data(self,file_name) :

        if( (is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug) ) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfc_file_Widget][reload_data] file_name",file_name))

        self.file_name  =   file_name
        self.dfc_cfg_title_label.setText("\n\n" + self.file_name + "\n")
        file_text   =   self.get_dfc_file(self.file_name)
        self.dfc_file_content.setText(file_text)

    def init_form(self):  

        if( (is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug) ) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfc_file_Widget][init_form]"))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout

        self.dfcfileLayout     =   QVBoxLayout()

        from PyQt5.QtWidgets import QLabel
        self.dfc_cfg_title_label   =   QLabel()
        self.dfc_cfg_title_label.setText("\n\n" + self.file_name + "\n")
        self.dfc_cfg_title_label.setAlignment(Qt.AlignCenter)
        self.dfc_cfg_title_label.resize(720,50)

        if(len(self.file_name) > 50) :
            self.dfc_cfg_title_label.setStyleSheet("font-size: 12px; font-weight: bold; font-family: Arial; ")  
        else :  
            self.dfc_cfg_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.dfcfileLayout.addWidget(self.dfc_cfg_title_label)

        from PyQt5.QtWidgets import QTextEdit
        self.dfc_file_content    =   QTextEdit()
        self.dfc_file_content.setReadOnly(True)
        self.dfc_file_content.setStyleSheet("font-size: 12px; font-weight: normal; font-family: Tahoma; ")

        file_text   =   self.get_dfc_file(self.file_name)
        self.dfc_file_content.setText(file_text)
        
        from dfcleanser.common.cfg import dfc_debug_log
        debug_file_name     =   dfc_debug_log.get_debuglog_file_name()
        if(debug_file_name == self.file_name) :

            self.dfc_file_content.setFixedHeight(500)

        if( (is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug) ) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfc_file_Widget] file_text\n",file_text))

        from PyQt5.QtWidgets import QLabel
        self.spacer_label   =   QLabel()
        self.spacer_label.setText("")
        self.spacer_label.setAlignment(Qt.AlignCenter)
        self.spacer_label.resize(480,50)
        self.spacer_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        
        from PyQt5.QtWidgets import QPushButton

        if(not (debug_file_name == self.file_name)) :

            self.backup_button       =   QPushButton("Backup File")
            self.backup_button.setFixedSize(200,70)
            self.backup_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")

            self.restore_button      =   QPushButton("Restore File")
            self.restore_button.setFixedSize(200,70)
            self.restore_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")

            self.return_button      =   QPushButton("Return")
            self.return_button.setFixedSize(200,70)
            self.return_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")

        else :

            self.backupd_button       =   QPushButton("Backup Debug\n File")
            self.backupd_button.setFixedSize(200,70)
            self.backupd_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")

            self.clear_button      =   QPushButton("Clear Debug\nFile")
            self.clear_button.setFixedSize(200,70)
            self.clear_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")

            self.returnd_button      =   QPushButton("Return")
            self.returnd_button.setFixedSize(200,70)
            self.returnd_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")

        from PyQt5.QtWidgets import QHBoxLayout
        dfcdfsbutonsLayout  =   QHBoxLayout()

        if(not (debug_file_name == self.file_name)) :

            dfcdfsbutonsLayout.addWidget(self.backup_button)
            dfcdfsbutonsLayout.addWidget(self.restore_button)
            dfcdfsbutonsLayout.addWidget(self.return_button)

        else :

            dfcdfsbutonsLayout.addWidget(self.backupd_button)
            dfcdfsbutonsLayout.addWidget(self.clear_button)
            dfcdfsbutonsLayout.addWidget(self.returnd_button)

        dfcdfsbutonsLayout.setAlignment(Qt.AlignHCenter)

        self.dfcfileLayout.addWidget(self.dfc_file_content)
        self.dfcfileLayout.addWidget(self.spacer_label)
        self.dfcfileLayout.addLayout(dfcdfsbutonsLayout)
        self.dfcfileLayout.addStretch()

        self.setLayout(self.dfcfileLayout)

        if(not (debug_file_name == self.file_name)) :

            self.backup_button.clicked.connect(self.backup_file)
            self.restore_button.clicked.connect(self.restore_file)
            self.return_button.clicked.connect(self.return_file)

        else :

            self.backupd_button.clicked.connect(self.backup_debug_file)
            self.clear_button.clicked.connect(self.clear_file)
            self.returnd_button.clicked.connect(self.return_file)

        if( (is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug) ) :
            add_debug_to_log("SystemWidgets",print_to_string("[cfg_files_Widget][init_form] end"))


    def backup_file(self):

        if( (is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug) ) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfc_file_Widget][backup_file]"))

        file_parms      =   self.get_file_dir_and_name(self.file_name)
        cfg_file_dir    =   file_parms[0]
        cfg_file_name   =   file_parms[1]

        if( (is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug) ) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfc_file_Widget][backup_file] \n",cfg_file_dir,"\n",cfg_file_name))

        from dfcleanser.common.common_utils import does_dir_exist, make_dir, copy_a_file, opStatus, does_file_exist
        if(not (does_dir_exist(cfg_file_dir + "Backup"))) :
                make_dir(cfg_file_dir + "Backup")

        opstat = opStatus()

        from_file   =   cfg_file_name
        to_file     =   cfg_file_dir + "Backup" + "\\" + self.file_name + ".json" 

        if( (is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug) ) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfc_file_Widget][backup_file][copy_a_file] \n",from_file,"\n",to_file))

        copy_a_file(from_file,to_file,opstat)
        
        if( (is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug) ) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfc_file_Widget][backup_file][does_file_exist] ",does_file_exist(to_file)))

        if(opstat.get_status()):

            title       =   "dfcleanser system files"       
            status_msg  =   "[backup_file] file backed up successfully"
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg)

        else :

            title       =   "dfcleanser exception"
            status_msg  =   "[backup_file] file not backed up successfully "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,opstat.get_exception())


    def restore_file(self):

        if( (is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug) ) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfc_file_Widget][restore_file]"))

        file_parms      =   self.get_file_dir_and_name(self.file_name)
        cfg_file_dir    =   file_parms[0]
        cfg_file_name   =   file_parms[1]

        if( (is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug) ) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfc_file_Widget][restore_file] \n",cfg_file_dir,"\n",cfg_file_name))

        from dfcleanser.common.common_utils import does_dir_exist, make_dir, copy_a_file, opStatus, does_file_exist
        if(not (does_dir_exist(cfg_file_dir + "Backup"))) :

            title       =   "dfcleanser system files"       
            status_msg  =   "[restore_file] no backup file to restore from : no dir"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

        else :

            if(not (does_file_exist(cfg_file_dir + "Backup" + "\\" + self.file_name))) :

                title       =   "dfcleanser system files"       
                status_msg  =   "[restore_file] no backup file to restore from : no file"
                from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                display_error_msg(title,status_msg)

            else :

                opstat = opStatus()

                to_file     =   cfg_file_name
                from_file   =   cfg_file_dir + "Backup" + "\\" + self.file_name + ".json" 
                copy_a_file(from_file,to_file,opstat)

                if(opstat.get_status()):

                    title       =   "dfcleanser system files"       
                    status_msg  =   "[restore_file] file restored  successfully"
                    from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
                    display_status_msg(title,status_msg)

                else :

                    title       =   "dfcleanser exception"
                    status_msg  =   "[restore_file] file not restored successfully "
                    from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                    display_exception(title,status_msg,opstat.get_exception())

    def clear_file(self):

        if( (is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug) ) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfc_file_Widget][clear_file]"))

        from dfcleanser.common.cfg import clear_debug_log
        clear_debug_log()

        from dfcleanser.common.cfg import dfc_debug_log
        debug_file_name     =   dfc_debug_log.get_debuglog_file_name()

        self.parent.display_dfcleanser_file(debug_file_name)

    def backup_debug_file(self):

        if( (is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug) ) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfc_file_Widget][backup_file]"))

        file_parms      =   self.get_file_dir_and_name(self.file_name)
        cfg_file_dir    =   file_parms[0]
        cfg_file_name   =   file_parms[1]

        if( (is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug) ) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfc_file_Widget][backup_file] \n",cfg_file_dir,"\n",cfg_file_name))

        from dfcleanser.common.common_utils import does_dir_exist, make_dir, copy_a_file, opStatus, does_file_exist
        if(not (does_dir_exist(cfg_file_dir + "Backup"))) :
                make_dir(cfg_file_dir + "Backup")

        opstat = opStatus()

        from_file   =   cfg_file_name
        to_file     =   cfg_file_dir + "Backup" + "\\" + self.file_name + ".json" 

        if( (is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug) ) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfc_file_Widget][backup_file][copy_a_file] \n",from_file,"\n",to_file))

        copy_a_file(from_file,to_file,opstat)
        
        if( (is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug) ) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfc_file_Widget][backup_file][does_file_exist] ",does_file_exist(to_file)))

        if(opstat.get_status()):

            title       =   "dfcleanser system files"       
            status_msg  =   "[backup_file] file backed up successfully"
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg)

        else :

            title       =   "dfcleanser exception"
            status_msg  =   "[backup_file] file not backed up successfully "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,opstat.get_exception())

    def return_file(self):

        if( (is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug) ) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfc_file_Widget][return_file]"))

        self.parent.display_dfcleanser_sys_files()

    def get_file_dir_and_name(self,file_name) :

        if( (is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug) ) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfc_file_Widget][get_dfc_file]",file_name))

        if( (file_name == "dfcleanserCommon_config") or 
            (file_name == "dfcleanserCommon_import_history") or 
            (file_name == "dfcleanserCommon_export_history") ) :

            file_dir        =   str(cfg.get_dfcleanser_location()) + "files" + "\\"
            file_to_read    =   file_dir + file_name + ".json"  

        else :

            file_dir        =   str(cfg.get_notebookPath()) + "\\"
            file_to_read    =   file_dir + str(cfg.get_notebookName()) + "_files" + "\\" + file_name + ".json"

        return([file_dir,file_to_read])

    def get_dfc_file(self,file_name):

        if( (is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug) ) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfc_file_Widget][get_dfc_file]",file_name))

        if( (file_name == "dfcleanserCommon_config") or 
            (file_name == "dfcleanserCommon_import_history") or 
            (file_name == "dfcleanserCommon_export_history") ) :
            file_to_read    =   str(cfg.get_dfcleanser_location()) + "files" + "\\" + file_name + ".json"  

        else :

            from dfcleanser.common.cfg import dfc_debug_log
            debug_log_file  =   dfc_debug_log.get_debuglog_file_name()

            if(debug_log_file == file_name) :
                file_to_read    =   debug_log_file
            else :
                file_to_read    =   str(cfg.get_notebookPath()) + "\\" + str(cfg.get_notebookName()) + "_files" + "\\" + file_name + ".json"

        if( (is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug) ) :
            add_debug_to_log("SystemWidgets",print_to_string("[dfc_file_Widget][get_dfc_file]",file_to_read))

        import json

        try :

            file_text   =   ""

            with open(file_to_read,'r') as  system_file :
                            
                file_data = json.load(system_file)
                system_file.close()

                if( (is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) and (self.allow_debug) ) :
                    add_debug_to_log("SystemWidgets",print_to_string("[dfc_file_Widget]  - file_data  ",type(file_data),len(file_data)))

                if(type(file_data) == list) :
                    
                    for i in range(len(file_data)) :
                        file_text   =   file_text + str(file_data[i]) + "\n"

                elif(type(file_data) == dict) :
                    dict_keys   =   list(file_data.keys())

                    for i in range(len(dict_keys)) :
                        file_text   =   file_text + "{ " + str(dict_keys[i]) + " : " + str(file_data.get(dict_keys[i])) + " }" + "\n"

                else :
                    file_text   =   str(file_data)
                        
        except :
                        
            from dfcleanser.common.cfg import add_error_to_log, SEVERE_ERROR
            add_error_to_log("[get_dfc_file Error - for json decode error] "  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)

        return(file_text)
    
        import json

        if( (DEBUG_IMPORT_HISTORY_DETAILS) and (self.allow_debug) ) :
            add_debug_to_log("SystemWidgets",print_to_string("[load_history_file] : self.history_file_loaded  ",self.history_file_loaded ))

        history_data             =   []
        
        history_dir_name         =   self.get_history_dir_name(self.history_type)
        history_file_name        =   self.get_history_file_name(self.history_type)
        history_full_file_name   =   self.get_history_full_file_name(self.history_type)
        
        if( (DEBUG_IMPORT_HISTORY_DETAILS) and (self.allow_debug) ) :
            add_debug_to_log("SystemWidgets",print_to_string("load_history_file",history_dir_name,"\n",history_file_name,"\n",history_full_file_name))
        
        if(not (history_dir_name is None)) :
            
            from dfcleanser.common.common_utils import does_dir_exist, make_dir
            if(not (does_dir_exist(history_dir_name))) :
                make_dir(history_dir_name)
            
            from dfcleanser.common.common_utils import does_file_exist
            if( (DEBUG_IMPORT_HISTORY_DETAILS) and (self.allow_debug) ) :
                add_debug_to_log("SystemWidgets",print_to_string("[load_history_file] : does_file_exist ",does_file_exist(history_full_file_name)))
            
            if(not (does_file_exist(history_full_file_name))) :
                
                if( (DEBUG_IMPORT_HISTORY_DETAILS) and (self.allow_debug) ) :
                    add_debug_to_log("SystemWidgets",print_to_string("load_history_file - file not found\n",history_full_file_name))
                    add_debug_to_log("SystemWidgets",print_to_string("load_history_file - file not found : history type",self.history_type))
 
                self.history_file_loaded    =   False    
                self.notebook_history       =   {}
                
                if(DEBUG_IMPORT_HISTORY_DETAILS) :
                    add_debug_to_log("SystemWidgets",print_to_string("load_history_file - file not found : history length ",len(self.notebook_history)))
                    self.dump_history()
            
            # import history file does exist
            else :
                
                if( (DEBUG_IMPORT_HISTORY_DETAILS) and (self.allow_debug) ) :
                    add_debug_to_log("SystemWidgets",print_to_string("[load_history_file]  - file found\n  ",history_full_file_name))
                
                try :

                    with open(history_full_file_name,'r') as  history_file :
                            
                        history_data = json.load(history_file)
                        history_file.close()

                    if( (DEBUG_IMPORT_HISTORY_DETAILS) and (self.allow_debug) ) :
                        add_debug_to_log("SystemWidgets",print_to_string("[load_history_file]  - history_data  ",type(history_data),len(history_data)))
                    
                    self._parse_history_file_to_dict(history_data)
                    self.history_file_loaded = True
                        
                except :
                        
                    from dfcleanser.common.cfg import add_error_to_log, SEVERE_ERROR
                    add_error_to_log("[Load history file Error - for json decode error] "  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)
                    
        if( (DEBUG_IMPORT_HISTORY_DETAILS) and (self.allow_debug) ) :
            add_debug_to_log("SystemWidgets",print_to_string("[load_history_file] - complete : ",self.history_file_loaded))



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                     Debug files Widget                        -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#



class System_Debug_Widget(QtWidgets.QWidget):

    def __init__(self,parms):  

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_Debug_Widget]"))

        super().__init__()

        self.parent     =   parms[0]
        self.chapterid  =   parms[1]

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_Debug_Widget]"))

        self.init_form()

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_Debug_Widget] end"))

    def init_form(self):  

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_Debug_Widget][init_form]"))

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout, QWidget

        self.systemLayout       =   QVBoxLayout()
        #from dfcleanser.Qt.system.SystemModel import get_chapter_parms, build_chapter_debug_flags
        from dfcleanser.common.debug_utils import get_chapter_parms, build_chapter_debug_flags

        chparms                 =   get_chapter_parms(DC_SYSTEM_ID)
        self.systemLayout       =   build_chapter_debug_flags(DC_SYSTEM_ID,chparms)

        self.importLayout       =   QVBoxLayout()
        #from dfcleanser.Qt.system.SystemModel import get_chapter_parms, build_chapter_debug_flags
        from dfcleanser.common.debug_utils import get_chapter_parms, build_chapter_debug_flags
        chparms                 =   get_chapter_parms(DC_DATA_IMPORT_ID)
        self.importLayout       =   build_chapter_debug_flags(DC_DATA_IMPORT_ID,chparms)

        self.col1Layout         =   QVBoxLayout()
        self.col1Layout.addLayout(self.systemLayout)
        self.col1Layout.addLayout(self.importLayout)
        self.col1Layout.addStretch()

        self.inspectLayout       =   QVBoxLayout()
        #from dfcleanser.Qt.system.SystemModel import get_chapter_parms, build_chapter_debug_flags
        from dfcleanser.common.debug_utils import get_chapter_parms, build_chapter_debug_flags
        chparms                  =   get_chapter_parms(DC_DATA_INSPECTION_ID)
        self.inspectLayout       =   build_chapter_debug_flags(DC_DATA_INSPECTION_ID,chparms)
        
        self.cleanseLayout       =   QVBoxLayout()
        #from dfcleanser.Qt.system.SystemModel import get_chapter_parms, build_chapter_debug_flags
        from dfcleanser.common.debug_utils import get_chapter_parms, build_chapter_debug_flags
        chparms                  =   get_chapter_parms(DC_DATA_CLEANSING_ID)
        self.cleanseLayout       =   build_chapter_debug_flags(DC_DATA_CLEANSING_ID,chparms)

        self.col2Layout         =   QVBoxLayout()
        self.col2Layout.addLayout(self.inspectLayout)
        self.col2Layout.addLayout(self.cleanseLayout)
        self.col2Layout.addStretch()

        self.transformLayout       =   QVBoxLayout()
        #from dfcleanser.Qt.system.SystemModel import get_chapter_parms, build_chapter_debug_flags
        from dfcleanser.common.debug_utils import get_chapter_parms, build_chapter_debug_flags
        chparms                  =   get_chapter_parms(DC_DATA_TRANSFORM_ID)
        self.transformLayout       =   build_chapter_debug_flags(DC_DATA_TRANSFORM_ID,chparms)
        
        self.exportLayout       =   QVBoxLayout()
        #from dfcleanser.Qt.system.SystemModel import get_chapter_parms, build_chapter_debug_flags
        from dfcleanser.common.debug_utils import get_chapter_parms, build_chapter_debug_flags
        chparms                  =   get_chapter_parms(DC_DATA_EXPORT_ID)
        self.exportLayout       =   build_chapter_debug_flags(DC_DATA_EXPORT_ID,chparms)

        self.col3Layout         =   QVBoxLayout()
        self.col3Layout.addLayout(self.transformLayout)
        self.col3Layout.addLayout(self.exportLayout)
        self.col3Layout.addStretch()

        self.dbutilsLayout       =   QVBoxLayout()
        #from dfcleanser.Qt.system.SystemModel import get_chapter_parms, build_chapter_debug_flags
        from dfcleanser.common.debug_utils import get_chapter_parms, build_chapter_debug_flags
        chparms                  =   get_chapter_parms(DBUtils_ID)
        self.dbutilsLayout       =   build_chapter_debug_flags(DBUtils_ID,chparms)
        
        self.swutilsLayout       =   QVBoxLayout()
        #from dfcleanser.Qt.system.SystemModel import get_chapter_parms, build_chapter_debug_flags
        from dfcleanser.common.debug_utils import get_chapter_parms, build_chapter_debug_flags
        chparms                  =   get_chapter_parms(SWUtilities_ID)
        self.swutilsLayout       =   build_chapter_debug_flags(SWUtilities_ID,chparms)

        self.censusLayout        =   QVBoxLayout()
        #from dfcleanser.Qt.system.SystemModel import get_chapter_parms, build_chapter_debug_flags
        from dfcleanser.common.debug_utils import get_chapter_parms, build_chapter_debug_flags
        chparms                  =   get_chapter_parms(DC_CENSUS_ID)
        self.censusLayout        =   build_chapter_debug_flags(DC_CENSUS_ID,chparms)

        self.zipcodeLayout       =   QVBoxLayout()
        #from dfcleanser.Qt.system.SystemModel import get_chapter_parms, build_chapter_debug_flags
        from dfcleanser.common.debug_utils import get_chapter_parms, build_chapter_debug_flags
        chparms                  =   get_chapter_parms(DC_ZIPCODE_UTILITY_ID)
        self.zipcodeLayout       =   build_chapter_debug_flags(DC_ZIPCODE_UTILITY_ID,chparms)

        self.col4Layout         =   QVBoxLayout()
        self.col4Layout.addLayout(self.dbutilsLayout)
        self.col4Layout.addLayout(self.swutilsLayout)
        self.col4Layout.addLayout(self.censusLayout)
        self.col4Layout.addLayout(self.zipcodeLayout)
        self.col4Layout.addStretch()

        self.geocodeLayout       =   QVBoxLayout()
        #from dfcleanser.Qt.system.SystemModel import get_chapter_parms, build_chapter_debug_flags
        from dfcleanser.common.debug_utils import get_chapter_parms, build_chapter_debug_flags
        chparms                  =   get_chapter_parms(DC_GEOCODE_UTILITY_ID)
        self.geocodeLayout       =   build_chapter_debug_flags(DC_GEOCODE_UTILITY_ID,chparms)

        self.col5Layout         =   QVBoxLayout()
        self.col5Layout.addLayout(self.geocodeLayout)
        self.col5Layout.addStretch()

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QHBoxLayout, QWidget
        self.debugLayout       =   QHBoxLayout()
        self.debugLayout.addLayout(self.col1Layout) 
        self.debugLayout.addLayout(self.col2Layout)
        self.debugLayout.addLayout(self.col3Layout)
        self.debugLayout.addLayout(self.col4Layout)
        self.debugLayout.addLayout(self.col5Layout)

        # buttons for inspect rows
        from PyQt5.QtWidgets import QPushButton
        Clear_button         =   QPushButton()     
        Clear_button.setText("Clear\nDebug\nFlags")
        Clear_button.setFixedSize(200,70)
        Clear_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        Clear_button.clicked.connect(self.clear_flags_callback) 
        
        Save_button        =   QPushButton()     
        Save_button.setText("Save\nDebug\nFlags")
        Save_button.setFixedSize(200,70)
        Save_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        Save_button.clicked.connect(self.save_flags_callback) 
        
        Display_button        =   QPushButton()     
        Display_button.setText("Display\nDebug Log")
        Display_button.setFixedSize(200,70)
        Display_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        Display_button.clicked.connect(self.display_debug_log_callback) 
        
        Return_button        =   QPushButton()     
        Return_button.setText("Return")
        Return_button.setFixedSize(200,70)
        Return_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        Return_button.clicked.connect(self.debug_return_callback) 

        from PyQt5.QtWidgets import QHBoxLayout
        self.dfcdfsbutonsLayout  =   QHBoxLayout()
        self.dfcdfsbutonsLayout.addWidget(Clear_button)
        self.dfcdfsbutonsLayout.addWidget(Save_button)
        self.dfcdfsbutonsLayout.addWidget(Display_button)
        self.dfcdfsbutonsLayout.addWidget(Return_button)
        self.dfcdfsbutonsLayout.setAlignment(Qt.AlignHCenter)

        self.finalLayout         =   QVBoxLayout()
        self.finalLayout.addLayout(self.debugLayout)
        self.finalLayout.addLayout(self.dfcdfsbutonsLayout)
        self.finalLayout.addStretch()

        self.setLayout(self.finalLayout)

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_Debug_Widget][init_form] end"))


    def clear_flags_callback(self) :

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_Debug_Widget][clear_flags_callback]"))


    def save_flags_callback(self) :

        print("save_flags_callback")

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_Debug_Widget][save_flags_callback]"))

        save_debug_flags()

        print("save_flags_callback : file saved")

    def display_debug_log_callback(self) :

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[display_debug_log_callback]"))

        from dfcleanser.common.cfg import dfc_debug_log
        debug_file  =   dfc_debug_log.get_debuglog_file_name()

        self.parent.display_dfcleanser_file(debug_file)

    def debug_return_callback(self) :

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_FILES")) :
            add_debug_to_log("SystemWidgets",print_to_string("[debug_return_callback]"))

        self.parent.display_dfcleanser_sys_files()

# -----------------------------------------------------------------#
# -                    System About Widget                        -#
# -----------------------------------------------------------------#
class System_EULA_Widget(QtWidgets.QWidget):

    def __init__(self,  **kwargs):  

        super().__init__()

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_EULA_Widget]"))

        self.init_form()

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_EULA_Widget] end"))

    def init_form(self):  

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_EULA_Widget][init_form]"))

        from dfcleanser.Qt.system.SystemControl import isEULA_read

        if(isEULA_read()) : 
            eula_file_name  =   cfg.get_common_files_path()+"\EULARead.html" 
        else :
            eula_file_name  =   cfg.get_common_files_path()+"\EULA.html"


        from dfcleanser.common.common_utils import  displayHTML
        displayHTML(eula_file_name)


        from PyQt5.QtWidgets import QLabel
        version_title_label   =   QLabel()
        version_title_label.setText("\nDataframe Cleanser Version : v1.0.0\n")
        version_title_label.setAlignment(Qt.AlignCenter)
        version_title_label.resize(480,50)
        version_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.SystemAboutLayout.addWidget(version_title_label)
        self.SystemAboutLayout.addStretch()

        self.setLayout(self.SystemAboutLayout)

        if(is_debug_on(System_ID,"DEBUG_SYSTEM_INFO")) :
            add_debug_to_log("SystemWidgets",print_to_string("[System_About_Widget][init_form] end"))


# -----------------------------------------------------------------#
# -                    System Info Widget end                     -#
# -----------------------------------------------------------------#










