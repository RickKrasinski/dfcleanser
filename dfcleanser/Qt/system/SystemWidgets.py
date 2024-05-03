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

DEBUG_SYSTEM_DFS            =   False
DEBUG_SYSTEM_INFO           =   False
DEBUG_SYSTEM_FILES          =   False


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

        if(DEBUG_SYSTEM_DFS) :
            print("\n[SystemActivedfsTable] : init")

        self.init_tableview()

        if(DEBUG_SYSTEM_DFS) :
            print("[SystemActivedfsTable] : end")

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self):
        
        if(DEBUG_SYSTEM_DFS) :
            print("  [SystemActivedfsTable] : reload_data")

        active_dfs_data     =   self.load_active_dfs_data()
        self.model.reload_data(active_dfs_data)
    
    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(DEBUG_SYSTEM_DFS) :
            print("  [SystemActivedfsTable][init_tableview]")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        activedfsdata     =   self.load_active_dfs_data()
        
        if(DEBUG_SYSTEM_DFS) :
           print("  [SystemActivedfsTable][init_tableview] :headers",self.column_headers)

        if(self.model is None) :
            self.model = SystemActivedfsModel(activedfsdata,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_SYSTEM_DFS) :
           print("  [SystemActivedfsTable][init_tableview] : model loaded")

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

        if(DEBUG_SYSTEM_DFS) :
            print("  [SystemActivedfsTable][load_active_dfs_data]")

        data    =   []

        from dfcleanser.common.cfg import get_dfc_dataframes_titles_list, get_dfc_dataframe_df, get_dfc_dataframe_notes
        
        active_dfs      =   get_dfc_dataframes_titles_list()

        if(DEBUG_SYSTEM_DFS) :
            print("  [SystemActivedfsTable][load_active_dfs_data] active_dfs : ",active_dfs)

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

            if(DEBUG_SYSTEM_DFS) :
                print("  [SystemActivedfsTable] : data")
                for j in range(len(data)) :
                    print("  [",j,"] : ",data[j])

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

        if(DEBUG_SYSTEM_DFS) :
            print("[System_dfc_dfs_Widget]")

        super().__init__()

        self.parent     =   dfparms[0]

        self.init_form()

        if(DEBUG_SYSTEM_DFS) :
            print("[System_Info_Widget] end")

    def reload_data(self) :

        self.acive_dfs_data.reload_data()

    def init_form(self):  

        if(DEBUG_SYSTEM_DFS) :
            print("[System_dfc_dfs_Widget][init_form]")

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
        
        if(DEBUG_SYSTEM_DFS) :
            print("[System_dfc_dfs_Widget][init_form] : active dfs loaded")
        
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

        if(DEBUG_SYSTEM_DFS) :
            print("[System_dfc_dfs_Widget][init_form] : buttons built")

        from PyQt5.QtWidgets import QHBoxLayout
        dfcdfsbutonsLayout  =   QHBoxLayout()
        dfcdfsbutonsLayout.addWidget(drop_button)
        dfcdfsbutonsLayout.addWidget(adddf_button)
        dfcdfsbutonsLayout.addWidget(dfshist_button)
        dfcdfsbutonsLayout.setAlignment(Qt.AlignHCenter)
        self.SystemdfcdfsLayout.addLayout(dfcdfsbutonsLayout)

        self.SystemdfcdfsLayout.addStretch()
        self.setLayout(self.SystemdfcdfsLayout)

        if(DEBUG_SYSTEM_DFS) :
            print("[System_dfc_dfs_Widget][init_form] end")


    # -----------------------------------------------------------------#
    # -                System dfc dfs Widget methods                  -#
    # -----------------------------------------------------------------#

    def select_df_to_drop(self) :

        if(DEBUG_SYSTEM_DFS) :
            print("[System_dfc_dfs_Widget][select_df_to_drop]")

        for idx in self.acive_dfs_data.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_SYSTEM_DFS) :
            print("[System_dfc_dfs_Widget][select_df_to_drop] ",row_number,column_number)

        model   =   self.acive_dfs_data.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][column_number]

        if(DEBUG_SYSTEM_DFS) :    
            print("[System_dfc_dfs_Widget][select_df_to_drop] : cell value [",cell,"]",type(cell),len(cell))

        if(column_number == 0) :
            if(len(cell) == 0) :
                tdata[row_number][column_number] = "X" 
            else :
                tdata[row_number][column_number] = ""      

            model.reload_data(tdata)

    def drop_dfs_callback(self) :

        if(DEBUG_SYSTEM_DFS) :
            print("[System_dfc_dfs_Widget][drop_dfs_callback]")

        model   =   self.acive_dfs_data.model
        tdata   =   model.get_data()

        delete_list     =   []

        for i in range(len(tdata)) :
            check_value     =   tdata[i][0]
            if(not (len(check_value) == 0)) :
                delete_list.append(tdata[i][1])

        if(DEBUG_SYSTEM_DFS) :
            print("[System_dfc_dfs_Widget][drop_dfs_callback] delete_list",delete_list)
        
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

        if(DEBUG_SYSTEM_DFS) :
            print("[System_dfc_dfs_Widget][add_user_df_callback]")

        self.parent.display_add_user_df_to_dfc()

    def display_df_histories_callback(self) :

        if(DEBUG_SYSTEM_INFO) :
            print("[System_dfc_dfs_Widget][display_df_histories_callback]")

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

        if(DEBUG_SYSTEM_DFS) :
            print("[System_dfc_dfs_histories_Widget]")

        super().__init__()

        self.parent     =   dfparms[0]

        self.init_form()

        if(DEBUG_SYSTEM_DFS) :
            print("[System_dfc_dfs_histories_Widget] end")

    def init_form(self):  

        if(DEBUG_SYSTEM_DFS) :
            print("[System_dfc_dfs_histories_Widget][init_form]")

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
        
        if(DEBUG_SYSTEM_DFS) :
            print("[System_dfc_dfs_histories_Widget][init_form] : histories loaded")
        
        note_text   =   "The above tables define a history of all dfs that were imported or exported.\nTo get details on imports or exports go to Data Import or Data Export Chapters.\n"
        from PyQt5.QtWidgets import QLabel
        note_label   =   QLabel()
        note_label.setText(note_text)
        note_label.setAlignment(Qt.AlignCenter)
        note_label.resize(480,50)
        note_label.setStyleSheet("font-size: 14px; font-weight: normal; font-family: Arial; ")
        self.SystemdfcdfshistoryLayout.addWidget(note_label)
        
        """
        # buttons for inspect rows
        from PyQt5.QtWidgets import QPushButton

        return_button        =   QPushButton()     
        return_button.setText("Return")
        return_button.setFixedSize(200,70)
        return_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        return_button.clicked.connect(self.dfc_dfs_histories_return_callback) 

        help_button        =   QPushButton()     
        help_button.setText("Help")
        help_button.setFixedSize(200,70)
        help_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        help_button.clicked.connect(self.dfc_dfs_histories_help_callback) 
        
        if(DEBUG_SYSTEM_DFS) :
            print("[System_dfc_dfs_histories_Widget][init_form] : buttons built")
        """

        from PyQt5.QtWidgets import QHBoxLayout
        dfcdfsbutonsLayout  =   QHBoxLayout()
        #dfcdfsbutonsLayout.addWidget(return_button)
        #dfcdfsbutonsLayout.addWidget(help_button)
        dfcdfsbutonsLayout.setAlignment(Qt.AlignHCenter)
        self.SystemdfcdfshistoryLayout.addLayout(dfcdfsbutonsLayout)

        self.SystemdfcdfshistoryLayout.addStretch()
        self.setLayout(self.SystemdfcdfshistoryLayout)

        if(DEBUG_SYSTEM_DFS) :
            print("[System_dfc_dfs_histories_Widget][init_form] end")

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

        if(DEBUG_SYSTEM_DFS) :
            print("[System_add_user_df_to_dfc_Widget]")

        super().__init__()

        self.parent     =   dfparms[0]

        self.init_form()

        if(DEBUG_SYSTEM_DFS) :
            print("[System_add_user_df_to_dfc_Widget] end")

    def init_form(self):  

        if(DEBUG_SYSTEM_DFS) :
            print("[System_add_user_df_to_dfc_Widget][init_form]")

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
        #dfcdfsbutonsLayout.addWidget(return_button)
        #dfcdfsbutonsLayout.addWidget(help_button)
        dfcdfsbutonsLayout.setAlignment(Qt.AlignHCenter)
        self.SystemuserfdtodfcLayout.addLayout(dfcdfsbutonsLayout)

        self.SystemuserfdtodfcLayout.addStretch()
        self.setLayout(self.SystemuserfdtodfcLayout)

        if(DEBUG_SYSTEM_DFS) :
            print("[System_add_user_df_to_dfc_Widget][init_form] end")


    def dfc_dfs_add_user_df_return_callback(self) :

         if(DEBUG_SYSTEM_DFS) :
            print("[System_dfc_dfs_histories_Widget][dfc_dfs_add_user_df_return_callback]")

            self.parent.display_dfcleanser_dfs()

    def dfc_dfs_add_user_df_help_callback(self) :

         if(DEBUG_SYSTEM_DFS) :
            print("[System_dfc_dfs_histories_Widget][dfc_dfs_add_user_df_help_callback)]")


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
            #print("data model Qt.DisplayRole",row,column)
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

        if(DEBUG_SYSTEM_INFO) :
            print("\n[SystemPythonInfoTable] : init")

        self.init_tableview()

        if(DEBUG_SYSTEM_INFO) :
            print("[SystemPythonInfoTable] : end")

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self):
        
        if(DEBUG_SYSTEM_INFO) :
            print("  [SystemPythonInfoTable] : reload_data")

        python_data     =   self.load_python_info_data()
        self.model.reload_data(python_data)
    
    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(DEBUG_SYSTEM_INFO) :
            print("  [SystemPythonInfoTable][init_tableview]")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        pythondata     =   self.load_python_info_data()
        
        if(DEBUG_SYSTEM_INFO) :
           print("  [SystemPythonInfoTable][init_tableview] :headers",self.column_headers)

        if(self.model is None) :
            self.model = SystemPythonInfoModel(pythondata,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_SYSTEM_INFO) :
           print("  [SystemPythonInfoTable][init_tableview] : model loaded")

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

        if(DEBUG_SYSTEM_INFO) :
            print("  [SystemPythonInfoTable][load_python_info_data]")

        data    =   []

        infotitles     =   ["Version","API","Info"]
        infovalues     =   [str(get_python_version()),str(sys.api_version),str(sys.version_info)]
            
        for i in range(len(infotitles)) :
                
            data_row    =   []

            data_row.append(infotitles[i])
            data_row.append(infovalues[i])

            data.append(data_row)

        if(DEBUG_SYSTEM_INFO) :
            print("  [SystemPythonInfoTable] : data")
            for j in range(len(data)) :
                print("  [",j,"] : ",data[j])

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
            #print("data model Qt.DisplayRole",row,column)
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

        if(DEBUG_SYSTEM_INFO) :
            print("\n[SystemNotebookInfoTable] : init")

        self.init_tableview()

        if(DEBUG_SYSTEM_INFO) :
            print("[SystemNotebookInfoTable] : end")

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self):
        
        if(DEBUG_SYSTEM_INFO) :
            print("  [SystemNotebookInfoTable] : reload_data")

        notebook_data     =   self.load_notebook_info_data()
        self.model.reload_data(notebook_data)
    
    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(DEBUG_SYSTEM_INFO) :
            print("  [SystemNotebookInfoTable][init_tableview]")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        dfcleanserInfoTabledata     =   self.load_dfcleanser_info_data()
        
        if(DEBUG_SYSTEM_INFO) :
           print("  [dfcleanserInfoTable][init_tableview] :headers",self.column_headers)

        if(self.model is None) :
            self.model = dfcleanserInfoModel(dfcleanserInfoTabledata,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_SYSTEM_INFO) :
           print("  [dfcleanserInfoTable][init_tableview] : model loaded")

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

        if(DEBUG_SYSTEM_INFO) :
            print("  [dfcleanserInfoTable][load_dfcleanser_info_data]")

        data    =   []

        infotitles     =   ["dfcleanser path"]
        infovalues     =   [str(cfg.get_dfcleanser_location())]
            
        for i in range(len(infotitles)) :
                
            data_row    =   []

            data_row.append(infotitles[i])
            data_row.append(infovalues[i])

            data.append(data_row)

        if(DEBUG_SYSTEM_INFO) :
            print("  [dfcleanserInfoTable] : data")
            for j in range(len(data)) :
                print("  [",j,"] : ",data[j])

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
            #print("data model Qt.DisplayRole",row,column)
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

        if(DEBUG_SYSTEM_INFO) :
            print("\n[SystemNotebookInfoTable] : init")

        self.init_tableview()

        if(DEBUG_SYSTEM_INFO) :
            print("[SystemNotebookInfoTable] : end")

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self):
        
        if(DEBUG_SYSTEM_INFO) :
            print("  [SystemNotebookInfoTable] : reload_data")

        notebook_data     =   self.load_notebook_info_data()
        self.model.reload_data(notebook_data)
    
    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(DEBUG_SYSTEM_INFO) :
            print("  [SystemNotebookInfoTable][init_tableview]")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        notebookdata     =   self.load_notebook_info_data()
        
        if(DEBUG_SYSTEM_INFO) :
           print("  [SystemNotebookInfoTable][init_tableview] :headers",self.column_headers)

        if(self.model is None) :
            self.model = SystemNotebookInfoModel(notebookdata,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_SYSTEM_INFO) :
           print("  [SystemNotebookInfoTable][init_tableview] : model loaded")

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

        if(DEBUG_SYSTEM_INFO) :
            print("  [SystemNotebookInfoTable][load_notebook_info_data]")

        data    =   []

        infotitles     =   ["Notebook Path","Notebook Name"]
        infovalues     =   [str(cfg.get_notebookPath()),str(cfg.get_notebookName())]
            
        for i in range(len(infotitles)) :
                
            data_row    =   []

            data_row.append(infotitles[i])
            data_row.append(infovalues[i])

            data.append(data_row)

        if(DEBUG_SYSTEM_INFO) :
            print("  [SystemNotebookInfoTable] : data")
            for j in range(len(data)) :
                print("  [",j,"] : ",data[j])

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

        if(DEBUG_SYSTEM_INFO) :
            print("\n[SystemPackageInfoTable] : init")

        self.init_tableview()

        if(DEBUG_SYSTEM_INFO) :
            print("[SystemPackageInfoTable] : end")

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self):
        
        if(DEBUG_SYSTEM_INFO) :
            print("  [SystemPackageInfoTable] : reload_data")

        package_data     =   self.load_package_info_data()
        self.model.reload_data(package_data)
    
    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(DEBUG_SYSTEM_INFO) :
            print("  [SystemPackageInfoTable][init_tableview]")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        packagedata     =   self.load_package_info_data()
        
        if(DEBUG_SYSTEM_INFO) :
           print("  [SystemPackageInfoTable][init_tableview] :headers",self.column_headers)

        if(self.model is None) :
            self.model = SystemPackageInfoModel(packagedata,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_SYSTEM_INFO) :
           print("  [SystemPackageInfoTable][init_tableview] : model loaded")

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

        if(DEBUG_SYSTEM_INFO) :
            print("  [SystemPackageInfoTable][load_package_info_data]")

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

        if(DEBUG_SYSTEM_INFO) :
            print("  [SystemPackageInfoTable] : data")
            for j in range(len(data)) :
                print("  [",j,"] : ",data[j])

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

        if(DEBUG_SYSTEM_INFO) :
            print("[System_Info_Widget]")


        super().__init__()

        if(DEBUG_SYSTEM_INFO) :
            print("[System_Info_Widget]")

        self.init_form()

        if(DEBUG_SYSTEM_INFO) :
            print("[System_Info_Widget] end")

    def init_form(self):  

        if(DEBUG_SYSTEM_INFO) :
            print("[System_Info_Widget][init_form]")

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

        if(DEBUG_SYSTEM_INFO) :
            print("[System_Info_Widget][init_form] end")


# -----------------------------------------------------------------#
# -                    System Info Widget end                     -#
# -----------------------------------------------------------------#



# -----------------------------------------------------------------#
# -                    System About Widget                        -#
# -----------------------------------------------------------------#
class System_About_Widget(QtWidgets.QWidget):

    def __init__(self,  **kwargs):  

        super().__init__()

        if(DEBUG_SYSTEM_INFO) :
            print("[System_About_Widget]")

        self.init_form()

        if(DEBUG_SYSTEM_INFO) :
            print("[System_About_Widget] end")

    def init_form(self):  

        if(DEBUG_SYSTEM_INFO) :
            print("[System_About_Widget][init_form]")

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

        if(DEBUG_SYSTEM_INFO) :
            print("[System_About_Widget][init_form] end")


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
            #print("data model Qt.DisplayRole",row,column)
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

        if(DEBUG_SYSTEM_FILES) :
            print("\n[dfcleansercfgfilesTable] : init")

        self.init_tableview()

        if(DEBUG_SYSTEM_FILES ) :
            print("[dfcleansercfgfilesTable] : end")

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self):
        
        if(DEBUG_SYSTEM_FILES) :
            print("  [dfcleansercfgfilesTable] : reload_data")

        cfgfiles_data     =   self.load_cfgfiles_info_data()
        self.model.reload_data(cfgfiles_data)
    
    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(DEBUG_SYSTEM_FILES) :
            print("  [dfcleansercfgfilesTable][init_tableview]")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        dfcleansercfgfilesTabledata     =   self.load_dfcleanser_cfgfiles_data()
        
        if(DEBUG_SYSTEM_FILES) :
           print("  [dfcleansercfgfilesTable][init_tableview] :headers",self.column_headers)

        if(self.model is None) :
            self.model = dfcleanserInfoModel(dfcleansercfgfilesTabledata,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_SYSTEM_FILES ) :
           print("  [dfcleansercfgfilesTable][init_tableview] : model loaded")

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

        if(DEBUG_SYSTEM_FILES) :
            print("  [dfcleanserInfoTable][load_dfcleanser_cfgfiles_data]")

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

        if(DEBUG_SYSTEM_FILES) :
            print("  [dfcleansercfgfiles] : data")
            for j in range(len(data)) :
                print("  [",j,"] : ",data[j])

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
            #print("data model Qt.DisplayRole",row,column)
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

        if(DEBUG_SYSTEM_FILES) :
            print("\n[notebookcfgfilesTable] : init")

        self.init_tableview()

        if(DEBUG_SYSTEM_FILES) :
            print("[notebookcfgfilesTable] : end")

    # -----------------------------------------------------------------#
    # -                    reload the table data                      -#
    # -----------------------------------------------------------------#
    def reload_data(self):
        
        if(DEBUG_SYSTEM_FILES) :
            print("  [notebookcfgfilesTable] : reload_data")

        cfgfiles_data     =   self.load_cfgfiles_info_data()
        self.model.reload_data(cfgfiles_data)
    
    # -----------------------------------------------------------------#
    # -                     init the tableview                        -#
    # -----------------------------------------------------------------#
    def init_tableview(self):

        if(DEBUG_SYSTEM_FILES) :
            print("  [notebookcfgfilesTable][init_tableview]")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        notebookcfgfilesTabledata     =   self.load_dfcleanser_cfgfiles_data()
        
        if(DEBUG_SYSTEM_FILES) :
           print("  [notebookcfgfilesTable][init_tableview] :headers",self.column_headers)

        if(self.model is None) :
            self.model = dfcleanserInfoModel(notebookcfgfilesTabledata,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_SYSTEM_FILES) :
           print("  [notebookcfgfilesTable][init_tableview] : model loaded")

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

        if(DEBUG_SYSTEM_FILES) :
            print("  [notebookcfgfilesTable][load_dfcleanser_cfgfiles_data]")

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

        if(DEBUG_SYSTEM_FILES) :
            print("  [dfcleansercfgfiles] : data")
            for j in range(len(data)) :
                print("  [",j,"] : ",data[j])

        self.column_headers     =   ["File","Location"]
        self.column_widths      =   [275,700]

        return(data)



# -----------------------------------------------------------------#
# -                     System files Widget                       -#
# -----------------------------------------------------------------#
class cfg_files_Widget(QtWidgets.QWidget):

    def __init__(self,parms):  

        if(DEBUG_SYSTEM_FILES) :
            print("[cfg_files_Widget]")
        

        super().__init__()

        self.parent     =   parms[0]


        if(DEBUG_SYSTEM_FILES) :
            print("[cfg_files_Widget]")

        self.init_form()

        if(DEBUG_SYSTEM_FILES) :
            print("[cfg_files_Widget] end")

    def init_form(self):  

        if(DEBUG_SYSTEM_FILES) :
            print("[cfg_files_Widget][init_form]")

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

        self.dfccfgLayout.addStretch()

        self.setLayout(self.dfccfgLayout)

        if(DEBUG_SYSTEM_FILES) :
            print("[cfg_files_Widget][init_form] end")


    def select_dfc_cfg_file(self) :

        if(DEBUG_SYSTEM_FILES) :
            print("[cfg_files_Widget][select_dfc_cfg_file]")

        for idx in self.dfc_cfg_files_data.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_SYSTEM_FILES) :
            print("[cfg_files_Widget][select_dfc_cfg_file] ",row_number,column_number)

        model   =   self.dfc_cfg_files_data.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][column_number]

        if(DEBUG_SYSTEM_FILES) :    
            print("[cfg_files_Widget][select_dfc_cfg_file] : cell value [",cell,"]",type(cell),len(cell))

        self.parent.display_dfcleanser_file(cell)

    def select_notebook_cfg_file(self) :

        if(DEBUG_SYSTEM_FILES) :
            print("[cfg_files_Widget][select_notebook_cfg_file]")

        for idx in self.notebook_cfg_files_data.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_SYSTEM_FILES) :
            print("[cfg_files_Widget][select_notebook_cfg_file] ",row_number,column_number)

        model   =   self.notebook_cfg_files_data.model
        tdata   =   model.get_data()
        cell    =   tdata[row_number][column_number]

        if(DEBUG_SYSTEM_FILES) :    
            print("[cfg_files_Widget][select_notebook_cfg_file] : cell value [",cell,"]",type(cell),len(cell))

        self.parent.display_dfcleanser_file(cell)


# -----------------------------------------------------------------#
# -                     System files Widget                       -#
# -----------------------------------------------------------------#
class dfc_file_Widget(QtWidgets.QWidget):

    def __init__(self,parms):  

        if(DEBUG_SYSTEM_FILES) :
            print("[dfc_file_Widget]")

        super().__init__()

        self.parent     =   parms[0]
        self.file_name  =   parms[1]

        if(DEBUG_SYSTEM_FILES) :
            print("[dfc_file_Widget]")

        self.init_form()

        if(DEBUG_SYSTEM_FILES) :
            print("[dfc_file_Widget] end")

    def reload_data(self,file_name) :

        if(DEBUG_SYSTEM_FILES) :
            print("[dfc_file_Widget][reload_data] file_name",file_name)

        self.file_name  =   file_name
        self.dfc_cfg_title_label.setText("\n\n" + self.file_name + "\n")
        file_text   =   self.get_dfc_file(self.file_name)
        self.dfc_file_content.setText(file_text)

    def init_form(self):  

        if(DEBUG_SYSTEM_FILES) :
            print("[dfc_file_Widget][init_form]")

        # build the overall dtypes layout
        from PyQt5.QtWidgets import QVBoxLayout

        self.dfcfileLayout     =   QVBoxLayout()

        from PyQt5.QtWidgets import QLabel
        self.dfc_cfg_title_label   =   QLabel()
        self.dfc_cfg_title_label.setText("\n\n" + self.file_name + "\n")
        self.dfc_cfg_title_label.setAlignment(Qt.AlignCenter)
        self.dfc_cfg_title_label.resize(480,50)
        self.dfc_cfg_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        self.dfcfileLayout.addWidget(self.dfc_cfg_title_label)

        from PyQt5.QtWidgets import QTextEdit, QPushButton
        self.dfc_file_content    =   QTextEdit()
        self.dfc_file_content.setReadOnly(True)
        self.dfc_file_content.setStyleSheet("font-size: 12px; font-weight: normal; font-family: Tahoma; ")

        file_text   =   self.get_dfc_file(self.file_name)
        self.dfc_file_content.setText(file_text)

        if(DEBUG_SYSTEM_FILES) :
            print("[dfc_file_Widget] file_text\n",file_text)

        from PyQt5.QtWidgets import QLabel
        self.spacer_label   =   QLabel()
        self.spacer_label.setText("")
        self.spacer_label.setAlignment(Qt.AlignCenter)
        self.spacer_label.resize(480,50)
        self.spacer_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
        

        self.backup_button       =   QPushButton("Backup File")
        self.backup_button.setFixedSize(200,70)
        self.backup_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")

        self.restore_button      =   QPushButton("Restore File")
        self.restore_button.setFixedSize(200,70)
        self.restore_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; ")
        
        from PyQt5.QtWidgets import QHBoxLayout
        dfcdfsbutonsLayout  =   QHBoxLayout()
        dfcdfsbutonsLayout.addWidget(self.backup_button)
        dfcdfsbutonsLayout.addWidget(self.restore_button)

        dfcdfsbutonsLayout.setAlignment(Qt.AlignHCenter)

        self.dfcfileLayout.addWidget(self.dfc_file_content)
        self.dfcfileLayout.addWidget(self.spacer_label)
        self.dfcfileLayout.addLayout(dfcdfsbutonsLayout)
        self.dfcfileLayout.addStretch()

        self.setLayout(self.dfcfileLayout)

        self.backup_button.clicked.connect(self.backup_file)
        self.restore_button.clicked.connect(self.restore_file)

        if(DEBUG_SYSTEM_FILES) :
            print("[cfg_files_Widget][init_form] end")


    def backup_file(self):

        if(DEBUG_SYSTEM_FILES) :
            print("[dfc_file_Widget][backup_file]")

        file_parms      =   self.get_file_dir_and_name(self.file_name)
        cfg_file_dir    =   file_parms[0]
        cfg_file_name   =   file_parms[1]

        if(DEBUG_SYSTEM_FILES) :
            print("[dfc_file_Widget][backup_file] \n",cfg_file_dir,"\n",cfg_file_name)

        from dfcleanser.common.common_utils import does_dir_exist, make_dir, copy_a_file, opStatus, does_file_exist
        if(not (does_dir_exist(cfg_file_dir + "Backup"))) :
                make_dir(cfg_file_dir + "Backup")

        opstat = opStatus()

        from_file   =   cfg_file_name
        to_file     =   cfg_file_dir + "Backup" + "\\" + self.file_name + ".json" 

        if(DEBUG_SYSTEM_FILES) :
            print("[dfc_file_Widget][backup_file][copy_a_file] \n",from_file,"\n",to_file)

        copy_a_file(from_file,to_file,opstat)
        
        if(DEBUG_SYSTEM_FILES) :
            print("[dfc_file_Widget][backup_file][does_file_exist] ",does_file_exist(to_file))

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

        if(DEBUG_SYSTEM_FILES) :
            print("[dfc_file_Widget][restore_file]")

        file_parms      =   self.get_file_dir_and_name(self.file_name)
        cfg_file_dir    =   file_parms[0]
        cfg_file_name   =   file_parms[1]

        if(DEBUG_SYSTEM_FILES) :
            print("[dfc_file_Widget][restore_file] \n",cfg_file_dir,"\n",cfg_file_name)

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



    def get_file_dir_and_name(self,file_name) :

        if(DEBUG_SYSTEM_FILES) :
            print("[dfc_file_Widget][get_dfc_file]",file_name)

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

        if(DEBUG_SYSTEM_FILES) :
            print("[dfc_file_Widget][get_dfc_file]",file_name)

        if( (file_name == "dfcleanserCommon_config") or 
            (file_name == "dfcleanserCommon_import_history") or 
            (file_name == "dfcleanserCommon_export_history") ) :
            file_to_read    =   str(cfg.get_dfcleanser_location()) + "files" + "\\" + file_name + ".json"  

        else :

            file_to_read    =   str(cfg.get_notebookPath()) + "\\" + str(cfg.get_notebookName()) + "_files" + "\\" + file_name + ".json"

        if(DEBUG_SYSTEM_FILES) :
            print("[dfc_file_Widget][get_dfc_file]",file_to_read)

        import json

        try :

            file_text   =   ""

            with open(file_to_read,'r') as  system_file :
                            
                file_data = json.load(system_file)
                system_file.close()

                if(DEBUG_SYSTEM_FILES) :
                    print("[dfc_file_Widget]  - file_data  ",type(file_data),len(file_data))

                if(type(file_data) == list) :
                    
                    for i in range(len(file_data)) :
                        file_text   =   file_text + str(file_data[i]) + "\n"

                elif(type(file_data) == dict) :
                    dict_keys   =   list(file_data.keys())

                    for i in range(len(dict_keys)) :
                        file_text   =   file_text + "{ " + str(dict_keys[i]) + " : " + str(file_data.get(dict_keys[i])) + " }" + "\n"

                else :
                    file_text   =   str(file_data)

                    
                #self._parse_history_file_to_dict(history_data)
                        
        except :
                        
            from dfcleanser.common.cfg import add_error_to_log, SEVERE_ERROR
            add_error_to_log("[get_dfc_file Error - for json decode error] "  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)
            print("","[get_dfc_file file Error - for json decode error] "  + str(sys.exc_info()[0].__name__))



        return(file_text)
    
        import json

        if(DEBUG_IMPORT_HISTORY_DETAILS) :
            print("\n[load_history_file] : self.history_file_loaded  ",self.history_file_loaded )

        history_data             =   []
        
        history_dir_name         =   self.get_history_dir_name(self.history_type)
        history_file_name        =   self.get_history_file_name(self.history_type)
        history_full_file_name   =   self.get_history_full_file_name(self.history_type)
        
        if(DEBUG_IMPORT_HISTORY_DETAILS) :
            print("load_history_file",history_dir_name,"\n",history_file_name,"\n",history_full_file_name)
        
        if(not (history_dir_name is None)) :
            
            from dfcleanser.common.common_utils import does_dir_exist, make_dir
            if(not (does_dir_exist(history_dir_name))) :
                make_dir(history_dir_name)
            
            from dfcleanser.common.common_utils import does_file_exist
            if(DEBUG_IMPORT_HISTORY_DETAILS) :
                print("[load_history_file] : does_file_exist ",does_file_exist(history_full_file_name))
            
            if(not (does_file_exist(history_full_file_name))) :
                
                if(DEBUG_IMPORT_HISTORY_DETAILS) :
                    print("load_history_file - file not found\n",history_full_file_name)
                    print("load_history_file - file not found : history type",self.history_type)
 
                self.history_file_loaded    =   False    
                self.notebook_history       =   {}
                
                if(DEBUG_IMPORT_HISTORY_DETAILS) :
                    print("load_history_file - file not found : history length ",len(self.notebook_history))
                    self.dump_history()
            
            # import history file does exist
            else :
                
                if(DEBUG_IMPORT_HISTORY_DETAILS) :
                    print("[load_history_file]  - file found\n  ",history_full_file_name)
                
                try :

                    with open(history_full_file_name,'r') as  history_file :
                            
                        history_data = json.load(history_file)
                        history_file.close()

                    if(DEBUG_IMPORT_HISTORY_DETAILS) :
                        print("[load_history_file]  - history_data  ",type(history_data),len(history_data))
                    
                    self._parse_history_file_to_dict(history_data)
                    self.history_file_loaded = True
                        
                except :
                        
                    from dfcleanser.common.cfg import add_error_to_log, SEVERE_ERROR
                    add_error_to_log("[Load history file Error - for json decode error] "  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)
                    print("","[Load history file Error - for json decode error] "  + str(sys.exc_info()[0].__name__))
                    
        if(DEBUG_IMPORT_HISTORY_DETAILS) :
            print("[load_history_file] - complete : ",self.history_file_loaded)




















# -----------------------------------------------------------------#
# -                    System About Widget                        -#
# -----------------------------------------------------------------#
class System_EULA_Widget(QtWidgets.QWidget):

    def __init__(self,  **kwargs):  

        super().__init__()

        if(DEBUG_SYSTEM_INFO) :
            print("[System_EULA_Widget]")

        self.init_form()

        if(DEBUG_SYSTEM_INFO) :
            print("[System_EULA_Widget] end")

    def init_form(self):  

        if(DEBUG_SYSTEM_INFO) :
            print("[System_EULA_Widget][init_form]")

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

        if(DEBUG_SYSTEM_INFO) :
            print("[System_About_Widget][init_form] end")


# -----------------------------------------------------------------#
# -                    System Info Widget end                     -#
# -----------------------------------------------------------------#










