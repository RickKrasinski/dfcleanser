"""
# DBUtilsTableViews
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

DEBUG_DBUTILS                           =   True
DEBUG_DBUTILS_DBCONNECTORS              =   False
DEBUG_DBUTILS_TEST_CONNECTOR            =   True
DEBUG_DBUTILS_DBCONNECTOR_FORM          =   True
DEBUG_DBUTILS_DBCON_FORM_DETAILS        =   False

DEBUG_DBUTILS_SQL_FORM                  =   False
DEBUG_DBUTILS_SQL_FORM_DETAILS          =   False
DEBUG_DBUTILS_SQL_FORM_COL_NAMES        =   False
DEBUG_DBUTILS_SQL_FORM_TABLE_NAMES      =   False
DEBUG_DBUTILS_IMPORT                    =   False

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
# -               DBConnectors Table and Model                    -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

# -----------------------------------------------------------------#
# -                 Table Model for DBConnectors                  -#
# -----------------------------------------------------------------#

class DBUtilsDBConnectorsModel(QtCore.QAbstractTableModel):
    def __init__(self, dfsdata, colheaders):

        super(DBUtilsDBConnectorsModel, self).__init__()
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
                return(Qt.AlignCenter)
            elif(column == 1) :
                return(Qt.AlignCenter)
            else :
                return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:
            if(column == 0):
                if(self._data[row][column] == "X") :
                    bgcolor = QtGui.QBrush(QColor(102, 255, 102))  
                else :  
                    bgcolor = QtGui.QBrush(QtCore.Qt.white)
            elif(column == 1) :  
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
    
    def get_value(self,rowid,colid) :
        return(self._data[rowid][colid])

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:

            if(section <= len(self.column_names)) :
                return(self.column_names[section])
            else :
                return("  ")

        return super().headerData(section, orientation, role)


# -----------------------------------------------------------------#
# -                     Table for DBConnectors                    -#
# -----------------------------------------------------------------#
class DBUtilsDBConnectorsTable(QtWidgets.QTableView):

    def __init__(self, dbconparms, **kwargs):  

        super().__init__()

        self.db_connector_keys              =   []
        self.current_selected_dbconnector   =   None

        self.parent         =   dbconparms[0]
        self.import_type    =   dbconparms[1] 
        self.model          =   None

        if(DEBUG_DBUTILS_DBCONNECTORS) :
            print("[DBUtilsDBConnectorsTable] : init")

        self.init_tableview()

        self.doubleClicked.connect(self.select_db_connector)

        if(DEBUG_DBUTILS_DBCONNECTORS) :
            print("[DBUtilsDBConnectorsTable] : init_tableview done")


    def reload_data(self) :

        tdata   =   self.load_dbconnectors_data()
        self.model.reload_data(tdata)
        self.dbconnectorsdata   =   tdata
        self.size_table()


    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(DEBUG_DBUTILS_DBCONNECTORS) :
            print("[DBUtilsDBConnectorsTable] : init_tableview")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        self.dbconnectorsdata     =   self.load_dbconnectors_data()
        
        if(DEBUG_DBUTILS_DBCONNECTORS) :
           print("[DBUtilsDBConnectorsTable][init_tableview] :\n",self.column_headers)

        if(self.model is None) :
            self.model = DBUtilsDBConnectorsModel(self.dbconnectorsdata,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_DBUTILS_DBCONNECTORS) :
           print("[DBUtilsDBConnectorsTable][init_tableview] : num rows ",len(self.dbconnectorsdata))

        self.size_table()

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
        for row in range(self.num_rows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(self.column_widths)) :
           self.setColumnWidth(i, self.column_widths[i])     
        
        self.setWordWrap(True)


    # -----------------------------------------------------------------#
    # -                 Initialize the table data                     -#
    # -----------------------------------------------------------------#
    def load_dbconnectors_data(self) :

        if(DEBUG_DBUTILS) :
           print("     [DBUtilsDBConnectorsTable][load_dbconnectors_data] : ")

        from dfcleanser.sw_utilities.db_utils import dfc_dbconnectors_table, get_db_id_title
        dbconnectors_list   =   dfc_dbconnectors_table.get_dbconnectors_entries_list()
        data                =   []
        
        if(DEBUG_DBUTILS_DBCONNECTORS) :
           print("    [DBUtilsDBConnectorsTable][load_dbconnectors_data] : dbconnectors_list ",dbconnectors_list)

        for i in range(len(dbconnectors_list)) :

            data_row    =   []

            self.db_connector_keys.append(dbconnectors_list[i][0])

            if(self.current_selected_dbconnector is None) :
                data_row.append(str(" "))
            else :
                if(i == self.current_selected_dbconnector) :
                    data_row.append(str("X")) 
                else :                    
                    data_row.append(str(" "))

            data_row.append(get_db_id_title(int(dbconnectors_list[i][1])))
            data_row.append(str(dbconnectors_list[i][2])) 
            data_row.append(str(dbconnectors_list[i][3])) 
            data_row.append(str(dbconnectors_list[i][4])) 
            data_row.append(str(dbconnectors_list[i][5]))
            data_row.append(str(dbconnectors_list[i][6]))

            data.append(data_row)

        if(DEBUG_DBUTILS_DBCONNECTORS) :
            print("  [DBUtilsDBConnectorsTable][load_dbconnectors_data]  self.db_connector_keys \n",self.db_connector_keys)
            for i in range(len(data)) :
                print("data[",i,"] : ",data[i])

        self.column_headers     =   ["SEL","SQL Server Type","Library","Server Name","Database","User","Password"]
        self.column_widths      =   [20,150,165,170,160,150,150]

        return(data)
    
    # -----------------------------------------------------------------#
    # -                    Size the table data                        -#
    # -----------------------------------------------------------------#
    def size_table(self) :
        
        self.num_rows   =   len(self.dbconnectorsdata)
        
        if(self.num_rows < 25) :
            new_height  =   25 + (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   25 + (25 * DEFAULT_ROW_HEIGHT)
        
        if(DEBUG_DBUTILS_DBCONNECTORS) :
           print("[DBUtilsDBConnectorsTable][init_tableview] : new_height ",new_height)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)



    # -----------------------------------------------------------------#
    # -            DBUtilsDBConnectorsTable methods                   -#
    # -----------------------------------------------------------------#

    def select_db_connector(self) :

        if(DEBUG_DBUTILS_DBCONNECTOR_FORM) :
            print("    [DBUtilsDBConnectorsTable][select_db_connector]")

        self.parent.statusBar().clearMessage()

        for idx in self.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())

        if(DEBUG_DBUTILS_DBCONNECTOR_FORM) :
            print("    [DBUtilsDBConnectorsTable][select_db_connector]",row_number,column_number)

        tdata   =   self.model.get_data()
        cell    =   tdata[row_number][column_number]

        if(DEBUG_DBUTILS_DBCONNECTOR_FORM) :    
            print("    [DBUtilsDBConnectorsTable][select_db_connector] cell : [",cell,"]")

        if(column_number == 0) :

            if( not(self.current_selected_dbconnector is None)) :

                if(DEBUG_DBUTILS_DBCONNECTOR_FORM) :    
                    print("    [DBUtilsDBConnectorsTable][select_db_connector] [self.current_selected_dbconnector]",self.current_selected_dbconnector)

                tdata[self.current_selected_dbconnector][0]     =   " "

            tdata[row_number][0]     =   "X"
            self.current_selected_dbconnector   =   row_number

            self.selected_dbcon_key  =   self.db_connector_keys[row_number]

            self.model.reload_data(tdata)
        
        if(DEBUG_DBUTILS_DBCONNECTOR_FORM) :    
            print("    [DBUtilsDBConnectorsTable][select_db_connector] self.current_selected_dbconnector : ",self.current_selected_dbconnector)
        
        from dfcleanser.sw_utilities.db_utils import dfc_dbconnectors_table
        dfc_dbconnectors_table.set_current_dbconnector_key(self.import_type,self.selected_dbcon_key) 

        if(DEBUG_DBUTILS_DBCONNECTOR_FORM) :    
            print("    [DBUtilsDBConnectorsTable][select_db_connector] self.current_selected_dbconnector : ",self.current_selected_dbconnector)
            print("    [DBUtilsDBConnectorsTable][select_db_connector] dfc_dbconnectors_table.get_current_dbconnector : ",dfc_dbconnectors_table.get_current_dbconnector(0))




    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#
    # -             DBConnectors Table and Model end                  -#
    # -----------------------------------------------------------------#
    # -----------------------------------------------------------------#





# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                      DBConnector Widgets                      -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -            QT Widget to display dbconnectors table            -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
class DBUtilsDBConnectorsTableWidget(QtWidgets.QWidget) :

    def __init__(self,  dbconparms, **kwargs):  

        super().__init__()

        if(DEBUG_DBUTILS) :
            print("  [DBUtilsDBConnectorsTableWidget] : init")
        
        self.parent         =   dbconparms[0]
        self.import_type    =   dbconparms[1] 
        self.import_action  =   dbconparms[2]

        if(DEBUG_DBUTILS) :
            print("\n[DBUtilsDBConnectorsTableWidget] : init",dbconparms)

        self.init_content()
        
        if(DEBUG_DBUTILS) :
            print("  [DBUtilsDBConnectorsTableWidget] : end ")


    def reload_data(self) :
        
        if(DEBUG_DBUTILS) :
            print("  [DBUtilsDBConnectorsTableWidget][reload_data]: ")

        self.connectorsTable.reload_data()

    def init_content(self) :

        if(DEBUG_DBUTILS_DBCONNECTORS) :
            print("[DBUtilsDBConnectorsTableWidget] : init_content")

        from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
        from PyQt5.QtWidgets import QLabel, QPushButton

        connectors_title_label    =   QLabel()
        connectors_title_label.setText("\n\ndfcleanser DBConnectors for SQL\n")
        connectors_title_label.setAlignment(Qt.AlignCenter)
        connectors_title_label.resize(960,70)
        connectors_title_label.setStyleSheet("font-size: 16px; font-weight: bold; font-family: Arial; ")
 
        self.connectorsTable         =   DBUtilsDBConnectorsTable([self.parent,self.import_type])

        if(DEBUG_DBUTILS_DBCONNECTORS) :
            print("[DBUtilsDBConnectorsTableWidget][init_content] : table built \n  ",type(self.connectorsTable))

        new_height  =   45 + (self.connectorsTable.num_rows * DEFAULT_ROW_HEIGHT)

        self.connectorsTable.setMinimumHeight(new_height)
        self.connectorsTable.setMaximumHeight(new_height)
        
        if(DEBUG_DBUTILS_DBCONNECTORS) :
            print("[DBUtilsDBConnectorsTableWidget] : table built")

        button_style    =   "background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; "

        # buttons for dbconnectors
        from PyQt5.QtWidgets import QPushButton
        connectors_button         =   QPushButton()     
        connectors_button.setText("Test\nCurrent\nDB Connector")
        connectors_button.setFixedSize(170,90)
        connectors_button.setStyleSheet(button_style)
        connectors_button.clicked.connect(self.test_db_connector) 

        connectors_button1         =   QPushButton()     
        connectors_button1.setText("Create\nNew\nDB Connector")
        connectors_button1.setFixedSize(170,90)
        connectors_button1.setStyleSheet(button_style)
        connectors_button1.clicked.connect(self.create_db_connector) 

        connectors_button2         =   QPushButton()     
        connectors_button2.setText("Delete\nSelected\nDB Connector")
        connectors_button2.setFixedSize(170,90)
        connectors_button2.setStyleSheet(button_style)
        connectors_button2.clicked.connect(self.delete_db_connector) 

        connectors_button3         =   QPushButton()     
        connectors_button3.setText("Edit\nSelected\nDB Connector")
        connectors_button3.setFixedSize(170,90)
        connectors_button3.setStyleSheet(button_style)
        connectors_button3.clicked.connect(self.edit_db_connector) 

        connectors_button4         =   QPushButton() 

        from dfcleanser.sw_utilities.db_utils import IMPORT_FLAG 

        if(self.import_type == IMPORT_FLAG) :  
            connectors_button4.setText("Import Table\nWith Selected\nDB Connector")
        else :
            connectors_button4.setText("Export Table\nWith Selected\nDB Connector") 

        connectors_button4.setFixedSize(170,90)
        connectors_button4.setStyleSheet(button_style)
        connectors_button4.clicked.connect(self.import_action) 

        connectors_button5         =   QPushButton()     
        connectors_button5.setText("Return")
        connectors_button5.setFixedSize(170,90)
        connectors_button5.setStyleSheet(button_style)
        connectors_button5.clicked.connect(self.return_from_db_connector) 
        
        if(DEBUG_DBUTILS_DBCONNECTORS) :
            print("[DBUtilsDBConnectorsTableWidget] : buttons built")

        from PyQt5.QtWidgets import QHBoxLayout
        connectorsbutonsLayout  =   QHBoxLayout()
        connectorsbutonsLayout.addWidget(connectors_button)
        connectorsbutonsLayout.addWidget(connectors_button1)
        connectorsbutonsLayout.addWidget(connectors_button2)
        connectorsbutonsLayout.addWidget(connectors_button3)
        connectorsbutonsLayout.addWidget(connectors_button4)
        connectorsbutonsLayout.addWidget(connectors_button5)

        connectorsbutonsLayout.setAlignment(Qt.AlignHCenter)

        from PyQt5.QtWidgets import QVBoxLayout
        self.connectorsWidgetLayout     =   QVBoxLayout()
        self.connectorsWidgetLayout.addWidget(connectors_title_label)
        self.connectorsWidgetLayout.addWidget(self.connectorsTable)
        self.connectorsWidgetLayout.addLayout(connectorsbutonsLayout)
        self.connectorsWidgetLayout.addStretch()

        self.setLayout(self.connectorsWidgetLayout)

        if(DEBUG_DBUTILS_DBCONNECTORS) :
            print("[DBUtilsDBConnectorsTableWidget] : end init_content")

    # -----------------------------------------------------------------#
    # -                  dbconnectors table  methods                  -#
    # -----------------------------------------------------------------#


    # -----------------------------------------------------------------#
    # -                 Test the Current DBConnector                  -#
    # -----------------------------------------------------------------#
    def test_db_connector(self) :

        from dfcleanser.sw_utilities.db_utils import dfc_dbconnectors_table
        current_selected_connector  =   dfc_dbconnectors_table.get_current_dbconnector(self.import_type)
        
        self.parent.statusBar().clearMessage()

        if(DEBUG_DBUTILS_DBCONNECTORS) :    
            print("[DBUtilsDBConnectorsTableWidget][test_db_connector] : current_selected_connector ",current_selected_connector)

        if(not (current_selected_connector is None)) :

            from dfcleanser.sw_utilities.db_utils import get_db_id_from_dbid_title

            SQL_Server_Type             =   current_selected_connector.get_db_id()
            db_library                  =   current_selected_connector.get_db_library()
            Server_Name                 =   current_selected_connector.get_server()
            Database                    =   current_selected_connector.get_database()
            User                        =   current_selected_connector.get_user()
            Password                    =   current_selected_connector.get_password()

            dbconnectParms          =   [SQL_Server_Type,db_library,Server_Name,Database,User,Password]

            status_msg              =   common_test_db_connector(dbconnectParms)

            from PyQt5.QtWidgets import QMessageBox
            dlg = QMessageBox()
            dlg.setTextFormat(Qt.RichText)
            dlg.setWindowTitle("Db Connector Test Status")
            text_msg    =   status_msg.replace(":","<br>")
            dlg.setText(text_msg)
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setStyleSheet("QLabel{min-width: 350px;}")
            button = dlg.exec()

            self.parent.statusBar().showMessage(status_msg)

        else :

            self.parent.statusBar().showMessage("no current db connector selected to test")
           

        if(DEBUG_DBUTILS_DBCONNECTORS) :    
            print("[DBUtilsDBConnectorsTableWidget][test_db_connector] : end ")
    
    # -----------------------------------------------------------------#
    # -                    Create a new DBConnector                   -#
    # -----------------------------------------------------------------#
    def create_db_connector(self) :

        self.parent.statusBar().clearMessage() 

        if(DEBUG_DBUTILS_DBCONNECTORS) :    
            print("[DBUtilsDBConnectorsTableWidget][create_db_connector] start ")

        from dfcleanser.sw_utilities.db_utils import get_db_id_title, MySql, pymysql_library
        SQL_Server_Type             =   get_db_id_title(MySql)
        db_library                  =   pymysql_library
        Server_Name                 =   ""
        Database                    =   ""
        User                        =   ""
        Password                    =   ""

        dbcon_form_parms    =   [True,self.import_type,[SQL_Server_Type,db_library,Server_Name,Database,User,Password],self.connectorsTable]
        self.parent.display_dbconnector_form(dbcon_form_parms)

        if(DEBUG_DBUTILS_DBCONNECTORS) :
            print("[DBUtilsDBConnectorsTableWidget][create_db_connector] end ")
    
    # -----------------------------------------------------------------#
    # -                      Delete a DBConnector                     -#
    # -----------------------------------------------------------------#
    def delete_db_connector(self) :

        
        self.parent.statusBar().clearMessage() 

        if(DEBUG_DBUTILS) :    
            print("[DBUtilsDBConnectorsTableWidget][delete_db_connector] : ")

        from PyQt5.QtWidgets import QMessageBox
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Verify dbconnector to delete")
        dlg.setText("Do you want to delete dbconnector")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setStyleSheet("QLabel{min-width: 300px;}");
        button = dlg.exec()

        if button == QMessageBox.Yes:

            from dfcleanser.sw_utilities.db_utils import dfc_dbconnectors_table
            current_selected_connector_key  =   dfc_dbconnectors_table.get_current_dbconnector_key(self.import_type)
            dfc_dbconnectors_table.delete_dbconnector(current_selected_connector_key)

            self.parent.statusBar().showMessage("Selected dbconnector deleted")

            self.connectorsTable.reload_data()           
        
        else :

            self.parent.statusBar().showMessage("No dbconnector deleted")

        if(DEBUG_DBUTILS_DBCONNECTORS) :    
            print("[DBUtilsDBConnectorsTableWidget][delete_db_connector] : delete end ")

    
    # -----------------------------------------------------------------#
    # -                       Edit a DBConnector                      -#
    # -----------------------------------------------------------------#
    def edit_db_connector(self) :

        from dfcleanser.sw_utilities.db_utils import dfc_dbconnectors_table
        current_selected_connector  =   dfc_dbconnectors_table.get_current_dbconnector(self.import_type)
        
        self.parent.statusBar().clearMessage()

        if(DEBUG_DBUTILS) :    
            print("\n[DBUtilsDBConnectorsTableWidget][edit_db_connector] current_selected_connector : \n  ",current_selected_connector)

        if(not (current_selected_connector is None)) :

            SQL_Server_Type             =   current_selected_connector.get_db_id()
            db_library                  =   current_selected_connector.get_db_library()
            Server_Name                 =   current_selected_connector.get_server()
            Database                    =   current_selected_connector.get_database()
            User                        =   current_selected_connector.get_user()
            Password                    =   current_selected_connector.get_password()

            dbcon_form_parms    =   [False,self.import_type,[SQL_Server_Type,db_library,Server_Name,Database,User,Password],self.connectorsTable]

            self.parent.display_dbconnector_form(dbcon_form_parms)

        else :

           self.parent.statusBar().showMessage("no current db connector selected to edit")


        if(DEBUG_DBUTILS_DBCONNECTORS) :
            print("[DBUtilsDBConnectorsTableWidget][edit_db_connector] end ")

 
    # -----------------------------------------------------------------#
    # -                Return from DBConnector Table                  -#
    # -----------------------------------------------------------------#
    def return_from_db_connector(self) :

        if(DEBUG_DBUTILS) :
            print("[DBUtilsDBConnectorsTableWidget][return_from_db_connector] ")

        from dfcleanser.sw_utilities.db_utils import IMPORT_FLAG 
        if(self.import_type == IMPORT_FLAG) :  
            self.parent.display_import_histories()
        else :
           self.parent.display_export_histories() 

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -          QT Widget to display dbconnectors table end          -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -              QT Widget to build dbconnector form              -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
class DBUtils_DBConnectorFormWidget(QtWidgets.QWidget) :


    def __init__(self,  dbcparms, **kwargs):  

        super().__init__()

        self.parent              =   dbcparms[0]
        self.import_type         =   dbcparms[1]
        self.dbconnectorParms    =   dbcparms[2]
        self.forCreate           =   dbcparms[3]
        self.dbconTable          =   dbcparms[4]

        if(DEBUG_DBUTILS) :
            print("\n  [DBUtils_DBConnectorFormWidget][init] : self.forCreate : ",self.forCreate,"\n    dbconparms\n     ",self.dbconnectorParms)
            print("\n  [DBUtils_DBConnectorFormWidget][init] : self.dbconTable : ",type(self.dbconTable))
        
        self.init_content()

    def load_form_values(self,reload_parms) :

        if(DEBUG_DBUTILS_DBCONNECTOR_FORM) :
            print("[DBUtils_DBConnectorFormWidget][load_form_values] \n  ",reload_parms)

        build_parms         =   build_dbcon_form_data(reload_parms)
        formParms           =   build_parms[0]
        dblibrary_types     =   build_parms[1]
        cfg_parms           =   build_parms[2]
 
        for i in range(len(cfg_parms)) :
            self.dbconnector_form.set_form_input_value_by_index(i,cfg_parms[i])

    def init_content(self) :

        if(DEBUG_DBUTILS_DBCONNECTOR_FORM) :
            print("[DBUtils_DBConnectorFormWidget][init_content]")

        build_parms         =   build_dbcon_form_data(self.dbconnectorParms)

        formParms           =   build_parms[0]
        dblibrary_types     =   build_parms[1]
        cfg_parms           =   build_parms[2]
        
        if(DEBUG_DBUTILS_DBCONNECTOR_FORM) :
            print("  [DBUtils_DBConnectorFormWidget][init_content] : formParms \n  ",formParms)
            print("  [DBUtils_DBConnectorFormWidget][init_content] : dblibrary_types \n  ",dblibrary_types)
            print("  [DBUtils_DBConnectorFormWidget][init_content] : cfg_parms \n  ",cfg_parms)

        import dfcleanser.sw_utilities.db_utils as qdbu

        if(self.forCreate) :
            form_title      =   "\n\nCreate DBConnector\n"
        else :
            form_title      =   "\n\nEdit DBConnector\n"
        
        form_width          =   900

        if(cfg_parms[0] == qdbu.get_db_id_title(qdbu.Custom)) :

            cfg_parms           =   [cfg_parms[1]]
            comboMethods        =   []
            importcomboList     =   []

        else :

            comboMethods        =   [self.select_servertype,self.select_dblibrary]
            selectDicts         =   []
            sqlserver_types     =   {"default":cfg_parms[0],"list":["MySql","MS SQL Server","SQLite3","Postgresql","Oracle","Custom"]}

            selectDicts.append(sqlserver_types)
            selectDicts.append(dblibrary_types)
        
            importcomboList     =   selectDicts
            
        file_methods    =   []
        button_methods  =   [self.test_db_connector_form,self.save_db_connector_form,self.return_from_db_connector_form,self.help_for_db_connector_form]

        formParms.append(importcomboList)
        formParms.append(comboMethods)            
        formParms.append(file_methods)
        formParms.append(button_methods)            
        formParms.append(cfg_parms)            
        formParms.append(form_title)
        formParms.append(form_width) 

        if(DEBUG_DBUTILS_DBCONNECTOR_FORM) :
            print("    [DBUtils_DBConnectorFormWidget][init_content] formParms :")
            for i in range(len(formParms)) :
                print("       formParms[",i,"]  ",formParms[i])

        from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget
        self.dbconnector_form     =   dfcleanser_input_form_Widget(formParms)
        
        if(DEBUG_DBUTILS_DBCONNECTOR_FORM) :
             print("  [DBUtils_DBConnectorFormWidget][form built]")

        from PyQt5.QtWidgets import QVBoxLayout
        self.dbconnector_formWidgetLayout     =   QVBoxLayout()
        self.dbconnector_formWidgetLayout.addWidget(self.dbconnector_form)
        self.dbconnector_formWidgetLayout.addStretch()

        self.setLayout(self.dbconnector_formWidgetLayout)

        if(DEBUG_DBUTILS) :
             print("  [DBUtils_DBConnectorFormWidget][init_content] end")



    # -----------------------------------------------------------------#
    # -                  dbconnectors form  methods                   -#
    # -----------------------------------------------------------------#
   
    # -----------------------------------------------------------------#
    # -                     Select a SQLServerType                    -#
    # -----------------------------------------------------------------#
    def select_servertype(self) :

        if(DEBUG_DBUTILS_DBCON_FORM_DETAILS ) :
            print("  [DBUtils_DBConnectorFormWidget][select_servertype] : start ")

        self.parent.statusBar().clearMessage()

        sqlserver_type  =   self.dbconnector_form.get_form_input_value_by_index(0)

        import dfcleanser.sw_utilities.db_utils as qdbu

        sqlserver_type_id   =   qdbu.get_db_id_from_dbid_title(sqlserver_type)

        if(DEBUG_DBUTILS_DBCON_FORM_DETAILS ) :
            print("  [DBUtils_DBConnectorFormWidget][select_servertype]",sqlserver_type,sqlserver_type_id)

        if(sqlserver_type_id == qdbu.MySql) : 
            dblibs   =   [qdbu.pymysql_library,qdbu.mysql_connector_library]
        elif(sqlserver_type_id == qdbu.MS_SQL_Server) : 
            dblibs   =   [qdbu.pyodbc_library,dbu.pymssql_library]
        elif(sqlserver_type_id== qdbu.SQLite) : 
            dblibs   =   [qdbu.sqlite3_library]
        elif(sqlserver_type_id== qdbu.Postgresql) : 
            dblibs   =   [qdbu.psycopg2_library]
        elif(sqlserver_type_id== qdbu.Oracle) : 
            dblibs   =   [qdbu.cx_oracle_library]
        elif(sqlserver_type_id== qdbu.Custom) : 
            dblibs   =   [sqlserver_type]
        
        if(DEBUG_DBUTILS_DBCON_FORM_DETAILS ) :
            print("  [DBUtils_DBConnectorFormWidget][select_servertype] dblibs : ",dblibs)

        self.dbconnector_form.reset_form_combobox_by_index(1,dblibs)

        if(DEBUG_DBUTILS_DBCON_FORM_DETAILS ) :
            print("  [DBUtils_DBConnectorFormWidget][select_servertype] : end ")

    # -----------------------------------------------------------------#
    # -                     Select a SQLServerType                    -#
    # -----------------------------------------------------------------#
    def select_dblibrary(self) :

        if(DEBUG_DBUTILS_DBCON_FORM_DETAILS ) :
            print("[DBUtils_DBConnectorFormWidget][select_dblibrary]")

    # -----------------------------------------------------------------#
    # -                     Select a SQLServerType                    -#
    # -----------------------------------------------------------------#
    def get_dbconnectparms_from_form(self) :

        if(DEBUG_DBUTILS_DBCON_FORM_DETAILS ) :
            print("[DBUtils_DBConnectorFormWidget][get_dbconnectparms_from_form]")

        from dfcleanser.sw_utilities.db_utils import dfc_dbconnectors_table

        current_selected_connector      =   dfc_dbconnectors_table.get_current_dbconnector(self.import_type)
        
        if(DEBUG_DBUTILS_DBCON_FORM_DETAILS ) :
            print("[DBUtils_DBConnectorFormWidget][get_dbconnectparms_from_form] current_selected_connector \n  ",current_selected_connector)


        if(not (current_selected_connector is None)) :
            import dfcleanser.sw_utilities.db_utils as qdbu
            current_selected_server_type    =   qdbu.get_db_id_title(current_selected_connector.get_db_id())
        else :
            current_selected_server_type    =   None

        if(DEBUG_DBUTILS_DBCON_FORM_DETAILS ) :    
            print("[DBUtilsDBConnectorsTableWidget][get_dbconnectparms_from_form] : current_selected_connector ",current_selected_connector)
            print("[DBUtilsDBConnectorsTableWidget][get_dbconnectparms_from_form] : current_selected_server_type ",current_selected_server_type)

        import dfcleanser.sw_utilities.db_utils as qdbu

        if(current_selected_server_type == "Custom") :
           
            connect_string      =   self.dbconnector_form.get_form_input_value_by_index(0) 
            dbconnectParms      =   [qdbu.Custom,connect_string,"","","",""]

        else :

            SQL_Server_Type         =   self.dbconnector_form.get_form_input_value_by_index(0)
            SQL_Server_Type_Id      =   qdbu.get_db_id_from_dbid_title(SQL_Server_Type)
            db_library              =   self.dbconnector_form.get_form_input_value_by_index(1)
            Server_Name             =   self.dbconnector_form.get_form_input_value_by_index(2)
            
            if(SQL_Server_Type_Id == qdbu.Oracle) :

                User                    =   self.dbconnector_form.get_form_input_value_by_index(3)
                Password                =   self.dbconnector_form.get_form_input_value_by_index(4)
                dbconnectParms          =   [SQL_Server_Type_Id,db_library,Server_Name,"",User,Password]

            else :

                Database                =   self.dbconnector_form.get_form_input_value_by_index(3)
                User                    =   self.dbconnector_form.get_form_input_value_by_index(4)
                Password                =   self.dbconnector_form.get_form_input_value_by_index(5)
                dbconnectParms          =   [SQL_Server_Type_Id,db_library,Server_Name,Database,User,Password]
        
        if(DEBUG_DBUTILS_DBCON_FORM_DETAILS ) :    
            print("[DBUtilsDBConnectorsTableWidget][get_dbconnectparms_from_form] : dbconnectParms\n",dbconnectParms)

        return(dbconnectParms)


    def get_dbconnectparms_from_conparms(self,cparms) :
         
        import dfcleanser.sw_utilities.db_utils as qdbu

        if(cparms[0] == qdbu.MySql) :
            new_dbcon_parms     =   qdbu.DataframeCleanserDBConnectorParms(cparms[0],cparms[1],cparms[2],cparms[3],cparms[4],cparms[5])
        elif(cparms[0] == qdbu.MS_SQL_Server) :
            new_dbcon_parms     =   qdbu.DataframeCleanserDBConnectorParms(cparms[0],cparms[1],cparms[2],cparms[3],cparms[4],cparms[5])
        elif(cparms[0] == qdbu.SQLite) :
            new_dbcon_parms     =   qdbu.DataframeCleanserDBConnectorParms(cparms[0],cparms[1],cparms[2],"","","")
        elif(cparms[0] == qdbu.Postgresql) :
            new_dbcon_parms     =   qdbu.DataframeCleanserDBConnectorParms(cparms[0],cparms[1],cparms[2],cparms[3],cparms[4],cparms[5])
        elif(cparms[0] == qdbu.Oracle) :
            new_dbcon_parms     =   qdbu.DataframeCleanserDBConnectorParms(cparms[0],cparms[1],cparms[2],"",cparms[3],cparms[4])
        elif(cparms[0] == qdbu.Custom ) :
            new_dbcon_parms     =   qdbu.DataframeCleanserDBConnectorParms(cparms[0],cparms[1],"","","","")

        return(new_dbcon_parms)
   
    
    # -----------------------------------------------------------------#
    # -                     Test the DBConnector                      -#
    # -----------------------------------------------------------------#
    def test_db_connector_form(self) :
        
        if(DEBUG_DBUTILS) :    
            print("[DBUtilsDBConnectorsTableWidget][test_db_connector_form] ")

        self.parent.statusBar().clearMessage()

        dbconnectParms  =  self.get_dbconnectparms_from_form() 

        if(DEBUG_DBUTILS_TEST_CONNECTOR) :    
            print("[DBUtilsDBConnectorsTableWidget][test_db_connector_form] : dbconnectParms\n",dbconnectParms)
        
        status_msg  =   common_test_db_connector(dbconnectParms)

        from PyQt5.QtWidgets import QMessageBox
        dlg = QMessageBox()
        dlg.setTextFormat(Qt.RichText)
        dlg.setWindowTitle("Db Connector Test Status")
        text_msg    =   status_msg.replace(":","<br>")
        dlg.setText(text_msg)
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setStyleSheet("QLabel{min-width: 350px;}")
        button = dlg.exec()

        self.parent.statusBar().showMessage(status_msg)

        if(DEBUG_DBUTILS) :
            print("[DBUtils_DBConnectorFormWidget][test_db_connector] end")
    
    # -----------------------------------------------------------------#
    # -                     Save the DBConnector                      -#
    # -----------------------------------------------------------------#
    def save_db_connector_form(self) :

        if(DEBUG_DBUTILS) :
            print("\n[DBUtils_DBConnectorFormWidget][save_db_connector_form] self.forCreate ",self.forCreate)

        dbconnectParms  =   self.get_dbconnectparms_from_form() 

        if(DEBUG_DBUTILS_DBCON_FORM_DETAILS) :
            print("[DBUtils_DBConnectorFormWidget][save_db_connector_form] dbconnectParms \n  ",dbconnectParms)

        status_msg      =   common_test_db_connector(dbconnectParms)
        
        if(DEBUG_DBUTILS_DBCON_FORM_DETAILS) :
            print("[DBUtils_DBConnectorFormWidget][save_db_connector_form] status_msg : \n",status_msg)

        continue_save   =   True

        if(status_msg.find("failled to connect") > -1) :

            from PyQt5.QtWidgets import QMessageBox
            dlg = QMessageBox()
            dlg.setTextFormat(Qt.RichText)
            dlg.setWindowTitle("Db Connector Failure")
            text_msg    =   "db connector failed to connect.<br>Save dbconnector anyway?"
            dlg.setText(text_msg)
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setStyleSheet("QLabel{min-width: 350px;}")
            button = dlg.exec()

            if(button == QMessageBox.No) :
                continue_save   =   False

        if(continue_save) :

            if(DEBUG_DBUTILS_DBCON_FORM_DETAILS) :
                print("[DBUtils_DBConnectorFormWidget][save_db_connector_form] continue_save : ",continue_save)

            import dfcleanser.sw_utilities.db_utils as qdbu  

            try :

                if(self.forCreate) :

                    if(DEBUG_DBUTILS_DBCON_FORM_DETAILS) :
                        print("[DBUtils_DBConnectorFormWidget][save_db_connector_form] before add : dbconnectParms : \n",dbconnectParms)
 
                    qdbu.dfc_dbconnectors_table.add_dbconnector(dbconnectParms) 

                else :

                    if(DEBUG_DBUTILS_DBCON_FORM_DETAILS) :
                        print("[DBUtils_DBConnectorFormWidget][save_db_connector_form] before edit : dbconnectParms : \n",dbconnectParms)

                    dbconn_key  =   qdbu.dfc_dbconnectors_table.get_current_dbconnector_key(self.import_type)
                    dbconn      =   self.get_dbconnectparms_from_conparms(dbconnectParms)

                    if(DEBUG_DBUTILS_DBCON_FORM_DETAILS) :
                        print("[DBUtils_DBConnectorFormWidget][save_db_connector_form] dbconn_key : \n",dbconn_key)
                        print("[DBUtils_DBConnectorFormWidget][save_db_connector_form] dbconn: \n",dbconn)

                    qdbu.dfc_dbconnectors_table.update_dbconnector(dbconn_key,dbconn)

                from PyQt5.QtWidgets import QMessageBox
                dlg = QMessageBox()
                dlg.setTextFormat(Qt.RichText)
                dlg.setWindowTitle("Db Connector Saved successfully")
                text_msg    =   "Db Connector Saved successfully"
                dlg.setText(text_msg)
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setStyleSheet("QLabel{min-width: 350px;}")
                button = dlg.exec()

                if(DEBUG_DBUTILS) :
                    print("\n[DBUtils_DBConnectorFormWidget][save_db_connector_form] end ")

                self.dbconTable.reload_data()

                self.return_from_db_connector_form()

            except Exception as e:
            
                title       =   "dfcleanser exception"       
                status_msg  =   "[save_db_connector_form] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)
                
                if(DEBUG_DBUTILS) :
                    print("\n[DBUtils_DBConnectorFormWidget][save_db_connector_form] end ")

                self.return_from_db_connector_form()
    
    # -----------------------------------------------------------------#
    # -               Return from DBConnector form                    -#
    # -----------------------------------------------------------------#
    def return_from_db_connector_form(self) :

        if(DEBUG_DBUTILS_DBCON_FORM_DETAILS) :
            print("[DBUtils_DBConnectorFormWidget][return_from_db_connector_form]")

        con_parms   =   [self.import_type,self.forCreate]
        self.parent.statusBar().clearMessage()

        from dfcleanser.sw_utilities.db_utils import IMPORT_FLAG
        if(self.import_type == IMPORT_FLAG) :
            self.parent.display_dbconnector_table(con_parms)
        else :
            self.parent.display_export_dbconnector_table(con_parms)

    # -----------------------------------------------------------------#
    # -                 Help for DBConnector form                     -#
    # -----------------------------------------------------------------#
    def help_for_db_connector_form(self) :

        if(DEBUG_DBUTILS) :
            print("[DBUtils_DBConnectorFormWidget][help_for_db_connector_form]")

        self.parent.statusBar().clearMessage()
       
        from dfcleanser.common.common_utils import display_url
        import dfcleanser.sw_utilities.db_utils as qdbu

        if(self.servertype == qdbu.MySql) :
            if(self.dblibrary == qdbu.pymysql_library) :
                native_url  =   qdbu.PYMYSQL_CONNECTOR_URL
                sqla_url    =   qdbu.PYMYSQL_CONNECTOR_SQLA_URL
            else :
                native_url  =   qdbu.MYSQL_CONNECTOR_URL
                sqla_url    =   qdbu.MYSQL_CONNECTOR_SQLA_URL
        
        elif(self.servertype == qdbu.MS_SQL_Server) :
            if(self.dblibrary == qdbu.pyodbc_library) :
                native_url  =   qdbu.PYODBC_CONNECTOR_URL
                sqla_url    =   qdbu.PYODBC_CONNECTOR_SQLA_URL
            else :
                native_url  =   qdbu.PYMSSQL_CONNECTOR_URL
                sqla_url    =   qdbu.PYMSSQL_CONNECTOR_SQLA_URL

        elif(self.servertype == qdbu.SQLite) :
            native_url  =   qdbu.SQLITE_CONNECTOR_URL
            sqla_url    =   qdbu.SQLITE_CONNECTOR_SQLA_URL

        elif(self.servertype == qdbu.Postgresql) :
            native_url  =   qdbu.POSTGRESQL_CONNECTOR_URL
            sqla_url    =   qdbu.POSTGRESQL_CONNECTOR_SQLA_URL
        
        elif(self.servertype == qdbu.Oracle) :
            native_url  =   qdbu.ORACLE_CONNECTOR_URL
            sqla_url    =   qdbu.ORACLE_CONNECTOR_SQLA_URL
        
        else :
            native_url  =   None
            sqla_url    =   qdbu.CUSTOM_CONNECTOR_URL

        if(not (native_url is None)) :
            display_url(native_url)
        if(not (sqla_url is None)) :
            display_url(sqla_url)

# -----------------------------------------------------------------#
# -              QT Widget to build dbconnector end               -#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                   QT Widgets to import sql                    -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                     Table Names Objects                      -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

# -----------------------------------------------------------------#
# -                      Table Names Model                        -#
# -----------------------------------------------------------------#

class DBUtilsTableNamesModel(QtCore.QAbstractTableModel):

    def __init__(self, tparms):

        super(DBUtilsTableNamesModel, self).__init__()


        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
            print("  [DBUtilsTableNamesModel : init : ",tparms)

        self._data          =   tparms[0]
        self.table_names    =   tparms[1]


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
            return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:
            bgcolor = QtGui.QBrush(QColor(240, 234, 193))
            return (bgcolor)               
                
    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])
    
    def get_value(self,rowid,colid) :
        return(self._data[rowid][colid])

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:

            if(section <= len(self.table_names)) :
                return(self.table_names[section])
            else :
                return("  ")

        return super().headerData(section, orientation, role)


# -----------------------------------------------------------------#
# -                     Table for Column Nammes                   -#
# -----------------------------------------------------------------#
class DBUtilsTableNamesTable(QtWidgets.QTableView):

    def __init__(self, dbparms, **kwargs):  

        super().__init__()

        self.parent             =   dbparms[0]
        self.dbcondict          =   dbparms[1]
        self.filetype           =   dbparms[2]

        self.model              =   None
        self.table_headers      =   []

        if(DEBUG_DBUTILS) :
            print("\n  [DBUtilsTablenNamesTable][init]",self.filetype,"\n  dbcondict : \n    ",self.dbcondict)

        self.init_tableview()

        self.doubleClicked.connect(self.select_table_name)

        if(DEBUG_DBUTILS) :
            print("    [DBUtilsTablenNamesTable] : init_tableview done")


    def reload_table_names_data(self) :
        
        if(DEBUG_DBUTILS) :
            print("    [DBUtilsTablenNamesTable][reload_column_names_data]")

        import dfcleanser.sw_utilities.db_utils as qdbu
        dbconDict           =   qdbu.get_current_dbcondict(0)
        self.dbcondict      =   dbconDict         
        
        tdata   =   self.load_columns_data()

        if(DEBUG_DBUTILS) :
            print("    [DBUtilsTablenNamesTable][reload_table_names_data] : tdata",tdata)

        self.model.reload_data(tdata)
        self.size_table(tdata)
        
        if(DEBUG_DBUTILS) :
            print("    [DBUtilsTablenNamesTable][reload_column_names_data] : end")

    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(DEBUG_DBUTILS_SQL_FORM_TABLE_NAMES) :
            print("  [DBUtilsTablenNamesTable] : init_tableview")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        self.dbtablesdata     =   self.load_tables_data()
        
        if(DEBUG_DBUTILS_SQL_FORM_TABLE_NAMES) :
           print("  [DBUtilsTablenNamesTable][init_tableview] :\n  ",self.dbtablesdata,self.model)

        if(self.model is None) :
            
            cparms  =   [self.dbtablesdata, self.table_headers] 

            if(DEBUG_DBUTILS_SQL_FORM_TABLE_NAMES) :
                print("  [DBUtilsTablenNamesTable][init_tableview] cparms:\n  ",cparms)

            self.model =    DBUtilsTableNamesModel(cparms)
            self.setModel(self.model)

        if(DEBUG_DBUTILS_SQL_FORM_TABLE_NAMES) :
           print("  [DBUtilsTablenNamesTable][init_tableview] : num rows ",len(self.dbtablesdata))

        self.size_table(self.dbtablesdata)

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
        for row in range(self.num_rows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(self.table_widths)) :
           self.setColumnWidth(i, self.table_widths[i])     
        
        self.setWordWrap(True)


    # -----------------------------------------------------------------#
    # -                 Initialize the table data                     -#
    # -----------------------------------------------------------------#
    def load_tables_data(self) :

        if(DEBUG_DBUTILS) :
           print("    [DBUtilsTablenNamesTable][load_tables_data] :")

        from dfcleanser.common.common_utils import opStatus
        opstat = opStatus()

        from dfcleanser.sw_utilities.db_utils import  get_table_names 
        tableparms     =   []
        tableslist     =   get_table_names(self.dbcondict, opstat)

        data    =   []

        for i in range(len(tableslist)) :

            data_row    =   []
            data_row.append(tableslist[i])
            data.append(data_row)

        if(DEBUG_DBUTILS_SQL_FORM_TABLE_NAMES) :
            print("  [DBUtilsTableNamesTable][load_tables_data] ")
            for i in range(len(data)) :
                print("  data[",i,"] : ",data[i])

        self.table_headers     =   ["Table Names"]
        self.table_widths      =   [280]

        return(data)

    # -----------------------------------------------------------------#
    # -            DBUtilsDBColumnNamesTable methods                  -#
    # -----------------------------------------------------------------#

    def select_table_name(self) :

        if(DEBUG_DBUTILS) :
            print("  [DBUtilsTableNamesTable][select_table_name]")

        for idx in self.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_DBUTILS_SQL_FORM_TABLE_NAMES) :
            print("  [DBUtilsTableNamesTable][select_table_name]",row_number,column_number)

        tdata   =   self.model.get_data()
        cell    =   tdata[row_number][column_number]

        if(DEBUG_DBUTILS_SQL_FORM_TABLE_NAMES) :    
            print("  [DBUtilsTableNamesTable][select_table_name] cell : [",cell,"]")

        self.parent.set_table_name(cell)

    #def set_table_name(self,tablename) :

    #    if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
    #        print("  [DBUtilsColumnNamesTable][set_table_name]",tablename)

    #    new_col_names   =   [tablename]
    #    self.model.change_col_names(new_col_names)
    
    def size_table(self,tabledata) :

        if(DEBUG_DBUTILS_SQL_FORM_TABLE_NAMES) :
            print("  [DBUtilsTableNamesTable][size_table]")

        self.num_rows   =   len(tabledata)
        
        if(DEBUG_DBUTILS_SQL_FORM_TABLE_NAMES) :    
            print("  [DBUtilsTableNamesTable] self.num_rows",self.num_rows)
            print("  [DBUtilsTableNamesTable] tabledata \n    ",tabledata)
         
        if(self.num_rows < 10) :
            new_height  =   30 + (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   30 + (10 * DEFAULT_ROW_HEIGHT)
        
        if(DEBUG_DBUTILS_SQL_FORM_TABLE_NAMES) :
           print("  [DBUtilsTableNamesTable][init_tableview] : new_height ",new_height)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)



# -----------------------------------------------------------------#
# -                     Widget for Column Nammes                  -#
# -----------------------------------------------------------------#

TABLE_NAMES_TITLE_HEIGHT       =   100
TABLE_NAMES_TITLE_STYLE        =   "font-size: 14px; font-weight: bold; font-family: Arial;" 

TABLE_NAMES_NOTES_HEIGHT       =   250
TABLE_NAMES_NOTES_STYLE        =   "font-size: 12px; font-weight: bold; font-family: Arial;" 

class DBUtils_TableNamesWidget(QtWidgets.QWidget) :

    def __init__(self,  dbparms, **kwargs):  

        super().__init__()

        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
            print("  [DBUtils_TableNamesWidget][init] : init")

        self.parent         =   dbparms[0]
        self.dbcondict      =   dbparms[1]
        self.filetype       =   dbparms[2]

        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
            print("  [DBUtils_TableNamesWidget][init] : self.dbcondict : \n    ",self.dbcondict)
            print("  [DBUtils_TableNamesWidget][init] : self.filetype : ",self.filetype)

        self.init_content()

        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
            print("  [DBUtils_TableNamesWidget][init] : end")


    def init_content(self) :

        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
            print("[DBUtils_TableNamesWidget][init_content]")

        table_title             =   "\n\nTable Names\n"
        self.table_width        =   280

        table_note       =   "<br><br>Click on the table name to set the table_name field.<br><br>" 
        
        from PyQt5.QtWidgets import QVBoxLayout, QLabel

        self.title_label    =   QLabel()
        self.title_label.setText(table_title)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.resize(COLUMN_NAMES_TITLE_HEIGHT,self.table_width)
        self.title_label.setStyleSheet(COLUMN_NAMES_TITLE_STYLE)

        table_names_parms          =   [self.parent,self.dbcondict,self.filetype]
        self.table_names_table     =   DBUtilsTableNamesTable(table_names_parms)

        self.note_label    =   QLabel()
        self.note_label.setText(table_note)
        self.note_label.setAlignment(Qt.AlignLeft)
        self.note_label.resize(COLUMN_NAMES_NOTES_HEIGHT,self.table_width)
        self.note_label.setStyleSheet(COLUMN_NAMES_NOTES_STYLE)

        self.dbcon_header    =   QLabel()
        self.dbcon_header.setText("Current Dbconnector\n")
        self.dbcon_header.setAlignment(Qt.AlignLeft)
        self.dbcon_header.resize(COLUMN_NAMES_NOTES_HEIGHT,self.table_width)
        self.dbcon_header.setStyleSheet(COLUMN_NAMES_TITLE_STYLE)

        self.set_dbcon_parms(False)        

        self.table_namesWidgetLayout     =   QVBoxLayout()
        self.table_namesWidgetLayout.addWidget(self.title_label)
        self.table_namesWidgetLayout.addWidget(self.table_names_table)
        self.table_namesWidgetLayout.addWidget(self.note_label)
        self.table_namesWidgetLayout.addWidget(self.dbcon_header)
        self.table_namesWidgetLayout.addWidget(self.server_type)
        self.table_namesWidgetLayout.addWidget(self.dblibrary)
        self.table_namesWidgetLayout.addWidget(self.dbc_hostname)
        self.table_namesWidgetLayout.addWidget(self.dbc_database)

        self.table_namesWidgetLayout.addStretch()

        self.setLayout(self.table_namesWidgetLayout)

        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
            print("[DBUtils_TableNamesWidget][init_content] end")


    def reload_tables(self,filetype) :

        if(DEBUG_DBUTILS) :
            print("\n  [DBUtils_TableNamesWidget][reload_tables] : ",filetype)

        import dfcleanser.sw_utilities.db_utils as qdbu
        dbconDict           =   qdbu.get_current_dbcondict(0)
        self.dbcondict      =   dbconDict         

        table_title      =   "\n\nTable Names\n"
        self.title_label.setText(table_title) 

        self.table_names_table.reload_table_names_data()

        self.set_dbcon_parms(True)
        
        if(DEBUG_DBUTILS) :
            print("  [DBUtils_ColumnNamesWidget][reload_columns] : end \n")


    def set_dbcon_parms(self,Reset_Names) :

        if(Reset_Names) :
            import dfcleanser.sw_utilities.db_utils as qdbu
            dbconDict           =   qdbu.get_current_dbcondict(0)
            self.dbcondict      =   dbconDict         

        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
            print("  [DBUtils_TableNamesWidget][set_dbcon_parms] : ",Reset_Names,"\n  ",self.dbcondict)  

        import dfcleanser.sw_utilities.db_utils as qdbu

        server_type         =   self.dbcondict.get('servertype')
        server_type_id      =   int(server_type)

        self.SQL_Database_Type   =   qdbu.get_db_id_title(server_type_id)
        self.SQL_dblibrary           =   self.dbcondict.get("dblibrary")

        if(server_type_id == qdbu.MySql) :

            self.hostname            =   self.dbcondict.get("hostname")
            self.database            =   self.dbcondict.get("database")

        elif(server_type_id == qdbu.MS_SQL_Server) :
            
            self.hostname            =   self.dbcondict.get("msserver")
            self.database            =   self.dbcondict.get("msdatabase")

        elif(server_type_id == qdbu.SQLite) :
 
            self.hostname            =   ""
            self.database            =   self.dbcondict.get("db_file")
           
        elif(server_type_id == qdbu.Postgresql) :
            
            self.hostname            =   self.dbcondict.get("pghost")
            self.database            =   self.dbcondict.get("pgdbname")

        elif(server_type_id == qdbu.Oracle) :
            
            self.hostname            =   self.dbcondict.get("tdshost")
            self.database            =   ""

        elif(server_type_id == qdbu.Custom) :
            
            self.dblibrary           =   self.dbcondict.get("customdbconnectorstring")
            self.hostname            =   ""
            self.database            =   ""
        
        from PyQt5.QtWidgets import QLabel

        if(not (Reset_Names)) :

            self.server_type    =   QLabel()
            self.server_type.setText("Server Type    : " + self.SQL_Database_Type)
            self.server_type.setAlignment(Qt.AlignLeft)
            self.server_type.resize(COLUMN_NAMES_NOTES_HEIGHT,self.table_width)
            self.server_type.setStyleSheet(COLUMN_NAMES_NOTES_STYLE)

            self.dblibrary    =   QLabel()
            self.dblibrary.setText("dblibrary        : " + self.SQL_dblibrary)
            self.dblibrary.setAlignment(Qt.AlignLeft)
            self.dblibrary.resize(COLUMN_NAMES_NOTES_HEIGHT,self.table_width)
            self.dblibrary.setStyleSheet(COLUMN_NAMES_NOTES_STYLE)

            self.dbc_hostname    =   QLabel()
            self.dbc_hostname.setText("hostname       : " + self.hostname)
            self.dbc_hostname.setAlignment(Qt.AlignLeft)
            self.dbc_hostname.resize(COLUMN_NAMES_NOTES_HEIGHT,self.table_width)
            self.dbc_hostname.setStyleSheet(COLUMN_NAMES_NOTES_STYLE)

            self.dbc_database    =   QLabel()
            self.dbc_database.setText("database        : " + self.database)
            self.dbc_database.setAlignment(Qt.AlignLeft)
            self.dbc_database.resize(COLUMN_NAMES_NOTES_HEIGHT,self.table_width)
            self.dbc_database.setStyleSheet(COLUMN_NAMES_NOTES_STYLE)

        else :

            self.server_type.setText("Server Type    : " + self.SQL_Database_Type)            
            self.dblibrary.setText("dblibrary        : " + self.SQL_dblibrary)
            self.dbc_hostname.setText("hostname       : " + self.hostname)
            self.dbc_database.setText("database        : " + self.database)



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                  Table Names Objects end                      -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                     Column Names Objects                      -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

# -----------------------------------------------------------------#
# -                      Column Names Model                       -#
# -----------------------------------------------------------------#

class DBUtilsColumnNamesModel(QtCore.QAbstractTableModel):

    def __init__(self, cparms):

        super(DBUtilsColumnNamesModel, self).__init__()


        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
            print("  [DBUtilsColumnNamesModel : init : ",cparms)

        self._data          =   cparms[0]
        self.column_names   =   cparms[1]


    def reload_data(self,dfsdata) :
        self._data = dfsdata

        self.layoutAboutToBeChanged.emit()
        self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0)))
        self.layoutChanged.emit()
    
    def change_col_names(self,column_names) :
        self.column_names   =   column_names

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
            return(Qt.AlignLeft)

        if role==Qt.BackgroundColorRole:
            bgcolor = QtGui.QBrush(QColor(240, 234, 193))
            return (bgcolor)               
                
    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])
    
    def get_value(self,rowid,colid) :
        return(self._data[rowid][colid])

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:

            if(section <= len(self.column_names)) :
                return(self.column_names[section])
            else :
                return("  ")

        return super().headerData(section, orientation, role)


# -----------------------------------------------------------------#
# -                     Table for Column Nammes                   -#
# -----------------------------------------------------------------#
class DBUtilsColumnNamesTable(QtWidgets.QTableView):

    def __init__(self, dbparms, **kwargs):  

        super().__init__()

        self.parent             =   dbparms[0]
        self.table              =   dbparms[1]
        self.dbcondict          =   dbparms[2]
        self.filetype           =   dbparms[3]

        self.model              =   None
        self.column_headers     =   []

        if(DEBUG_DBUTILS) :
            print("\n  [DBUtilsColumnNamesTable][init]",self.table,self.filetype,"\n  dbcondict : \n    ",self.dbcondict)

        self.init_tableview()

        self.doubleClicked.connect(self.select_column_name)

        if(DEBUG_DBUTILS) :
            print("    [DBUtilsColumnNamesTable] : init_tableview done")


    def reload_column_names_data(self) :
        
        if(DEBUG_DBUTILS) :
            print("    [DBUtilsColumnNamesTable][reload_column_names_data]")

        import dfcleanser.sw_utilities.db_utils as qdbu
        dbconDict           =   qdbu.get_current_dbcondict(0)
        self.dbcondict      =   dbconDict         
        
        if(DEBUG_DBUTILS) :
            print("    [DBUtilsColumnNamesTable][reload_column_names_data] : table ",self.table)

        tdata   =   self.load_columns_data()

        if(DEBUG_DBUTILS) :
            print("    [DBUtilsColumnNamesTable][reload_column_names_data] : tdata",tdata)

        self.model.reload_data(tdata)
        self.size_table(tdata)
        
        if(DEBUG_DBUTILS) :
            print("    [DBUtilsColumnNamesTable][reload_column_names_data] : end")

    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
            print("  [DBUtilsColumnNamesTable] : init_tableview")

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        self.dbcolumnsdata     =   self.load_columns_data()
        
        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
           print("  [DBUtilsColumnNamesTable][init_tableview] :\n  ",self.dbcolumnsdata,self.model)

        if(self.model is None) :
            
            cparms  =   [self.dbcolumnsdata, self.column_headers] 

            if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
                print("  [DBUtilsColumnNamesTable][init_tableview] cparms:\n  ",cparms)

            self.model =    DBUtilsColumnNamesModel(cparms)
            self.setModel(self.model)

        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
           print("  [DBUtilsColumnNamesTable][init_tableview] : num rows ",len(self.dbcolumnsdata))

        self.size_table(self.dbcolumnsdata)

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
        for row in range(self.num_rows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(self.column_widths)) :
           self.setColumnWidth(i, self.column_widths[i])     
        
        self.setWordWrap(True)


    # -----------------------------------------------------------------#
    # -                 Initialize the table data                     -#
    # -----------------------------------------------------------------#
    def load_columns_data(self) :

        if(DEBUG_DBUTILS) :
           print("    [DBUtilsColumnNamesTable][load_columns_data] : table : ",self.table)

        from dfcleanser.common.common_utils import opStatus
        opstat = opStatus()

        from dfcleanser.sw_utilities.db_utils import  get_column_names 
        columnparms     =   []
        columnslist     =   get_column_names(self.table, self.dbcondict, opstat)

        data    =   []

        for i in range(len(columnslist)) :

            data_row    =   []
            data_row.append(columnslist[i])
            data.append(data_row)

        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
            print("  [DBUtilsColumnNamesTable][load_columns_data] ")
            for i in range(len(data)) :
                print("  data[",i,"] : ",data[i])

        from dfcleanser.Qt.data_import.DataImportModel import SQLTABLE_IMPORT
        if(self.filetype==SQLTABLE_IMPORT) :
            self.column_headers     =   ["'columns' Columns"]
        else :
            self.column_headers     =   ["'index_col' Columns"]

        self.column_widths      =   [280]

        return(data)

    # -----------------------------------------------------------------#
    # -            DBUtilsDBColumnNamesTable methods                  -#
    # -----------------------------------------------------------------#

    def select_column_name(self) :

        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
            print("  [DBUtilsColumnNamesTable][select_column_name]")

        for idx in self.selectionModel().selectedIndexes():
            row_number = int(idx.row())
            column_number = int(idx.column())
                
        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
            print("  [DBUtilsColumnNamesTable][select_column_name]",row_number,column_number)

        tdata   =   self.model.get_data()
        cell    =   tdata[row_number][column_number]

        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :    
            print("  [DBUtilsColumnNamesTable][select_column_name] cell : [",cell,"]")

        self.parent.add_column_name(cell)

    def set_table_name(self,tablename) :

        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
            print("  [DBUtilsColumnNamesTable][set_table_name]",tablename)

        new_col_names   =   [tablename]
        self.model.change_col_names(new_col_names)
    
    def size_table(self,tabledata) :

        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
            print("  [DBUtilsColumnNamesTable][size_table]")

        self.num_rows   =   len(tabledata)
        
        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :    
            print("  [DBUtilsColumnNamesTable] self.num_rows",self.num_rows)
            print("  [DBUtilsColumnNamesTable] tabledata \n    ",tabledata)
         
        if(self.num_rows < 10) :
            new_height  =   30 + (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   30 + (10 * DEFAULT_ROW_HEIGHT)
        
        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
           print("  [DBUtilsColumnNamesTable][init_tableview] : new_height ",new_height)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)



# -----------------------------------------------------------------#
# -                     Widget for Column Nammes                  -#
# -----------------------------------------------------------------#

COLUMN_NAMES_TITLE_HEIGHT       =   100
COLUMN_NAMES_TITLE_STYLE        =   "font-size: 14px; font-weight: bold; font-family: Arial;" 

COLUMN_NAMES_NOTES_HEIGHT       =   250
COLUMN_NAMES_NOTES_STYLE        =   "font-size: 12px; font-weight: bold; font-family: Arial;" 

class DBUtils_ColumnNamesWidget(QtWidgets.QWidget) :

    def __init__(self,  dbparms, **kwargs):  

        super().__init__()

        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
            print("  [DBUtils_ColumnNamesWidget][init] : init")

        self.parent         =   dbparms[0]
        self.table          =   dbparms[1]
        self.dbcondict      =   dbparms[2]
        self.filetype       =   dbparms[3]

        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
            print("  [DBUtils_ColumnNamesWidget][init] : self.table : ",self.table)
            print("  [DBUtils_ColumnNamesWidget][init] : self.dbcondict : \n    ",self.dbcondict)
            print("  [DBUtils_ColumnNamesWidget][init] : self.filetype : ",self.filetype)

        self.init_content()

        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
            print("  [DBUtils_ColumnNamesWidget][init] : end")


    def init_content(self) :

        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
            print("[DBUtils_ColumnNamesWidget][init_content]")

        table_title             =   "\n\nTable '" + self.table + "' Column Names\n"
        self.table_width        =   280

        from dfcleanser.Qt.data_import.DataImportModel import SQLTABLE_IMPORT
        if(self.filetype==SQLTABLE_IMPORT) :

            table_note       =   ("<br><br>Click on Set 'columns' Columns to select<br> columns for the 'columns' field.<br><br>" +
                                  "Click on Set 'index_col' Columns to select<br> columns for the 'index_col' field.<br><br>" + 
                                  "Click on Set 'parse_dates' Columns to select<br> columns for the 'parse_dates' field.<br><br>")
        
        else :

            table_note       =   ("<br><br>Click on Set 'index_col' Columns to select<br> columns for the 'index_col' field.<br><br>" + 
                                  "Click on Set 'parse_dates' Columns to select<br> columns for the 'parse_dates' field.<br><br>")

        from PyQt5.QtWidgets import QVBoxLayout, QLabel

        self.title_label    =   QLabel()
        self.title_label.setText(table_title)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.resize(COLUMN_NAMES_TITLE_HEIGHT,self.table_width)
        self.title_label.setStyleSheet(COLUMN_NAMES_TITLE_STYLE)

        column_names_parms          =   [self.parent,self.table,self.dbcondict,self.filetype]
        self.column_names_table     =   DBUtilsColumnNamesTable(column_names_parms)

        self.note_label    =   QLabel()
        self.note_label.setText(table_note)
        self.note_label.setAlignment(Qt.AlignLeft)
        self.note_label.resize(COLUMN_NAMES_NOTES_HEIGHT,self.table_width)
        self.note_label.setStyleSheet(COLUMN_NAMES_NOTES_STYLE)

        self.dbcon_header    =   QLabel()
        self.dbcon_header.setText("Current Dbconnector\n")
        self.dbcon_header.setAlignment(Qt.AlignLeft)
        self.dbcon_header.resize(COLUMN_NAMES_NOTES_HEIGHT,self.table_width)
        self.dbcon_header.setStyleSheet(COLUMN_NAMES_TITLE_STYLE)

        self.set_dbcon_parms(False)        

        self.column_namesWidgetLayout     =   QVBoxLayout()
        self.column_namesWidgetLayout.addWidget(self.title_label)
        self.column_namesWidgetLayout.addWidget(self.column_names_table)
        self.column_namesWidgetLayout.addWidget(self.note_label)
        self.column_namesWidgetLayout.addWidget(self.dbcon_header)
        self.column_namesWidgetLayout.addWidget(self.server_type)
        self.column_namesWidgetLayout.addWidget(self.dblibrary)
        self.column_namesWidgetLayout.addWidget(self.dbc_hostname)
        self.column_namesWidgetLayout.addWidget(self.dbc_database)

        self.column_namesWidgetLayout.addStretch()

        self.setLayout(self.column_namesWidgetLayout)

        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
            print("[DBUtils_ColumnNamesWidget][init_content] end")


    def reload_columns(self,table_name,filetype) :

        if(DEBUG_DBUTILS) :
            print("\n  [DBUtils_ColumnNamesWidget][reload_columns] : ",table_name,filetype)

        import dfcleanser.sw_utilities.db_utils as qdbu
        dbconDict           =   qdbu.get_current_dbcondict(0)
        self.dbcondict      =   dbconDict         

        self.table       =   table_name
        table_title      =   "\n\nTable '" + self.table + "' Column Names\n"
        self.title_label.setText(table_title) 

        #self.title_label
        self.column_names_table.table   =  table_name      
        self.column_names_table.reload_column_names_data()

        self.set_dbcon_parms(True)
        
        if(DEBUG_DBUTILS) :
            print("  [DBUtils_ColumnNamesWidget][reload_columns] : end \n")


    def set_dbcon_parms(self,Reset_Names) :

        if(Reset_Names) :
            import dfcleanser.sw_utilities.db_utils as qdbu
            dbconDict           =   qdbu.get_current_dbcondict(0)
            self.dbcondict      =   dbconDict         

        if(DEBUG_DBUTILS_SQL_FORM_COL_NAMES) :
            print("  [DBUtils_ColumnNamesWidget][set_dbcon_parms] : ",Reset_Names,"\n  ",self.dbcondict)  

        import dfcleanser.sw_utilities.db_utils as qdbu

        server_type         =   self.dbcondict.get('servertype')
        server_type_id      =   int(server_type)

        self.SQL_Database_Type   =   qdbu.get_db_id_title(server_type_id)
        self.SQL_dblibrary           =   self.dbcondict.get("dblibrary")

        if(server_type_id == qdbu.MySql) :

            self.hostname            =   self.dbcondict.get("hostname")
            self.database            =   self.dbcondict.get("database")

        elif(server_type_id == qdbu.MS_SQL_Server) :
            
            self.hostname            =   self.dbcondict.get("msserver")
            self.database            =   self.dbcondict.get("msdatabase")

        elif(server_type_id == qdbu.SQLite) :
 
            self.hostname            =   ""
            self.database            =   self.dbcondict.get("db_file")
           
        elif(server_type_id == qdbu.Postgresql) :
            
            self.hostname            =   self.dbcondict.get("pghost")
            self.database            =   self.dbcondict.get("pgdbname")

        elif(server_type_id == qdbu.Oracle) :
            
            self.hostname            =   self.dbcondict.get("tdshost")
            self.database            =   ""

        elif(server_type_id == qdbu.Custom) :
            
            self.dblibrary           =   self.dbcondict.get("customdbconnectorstring")
            self.hostname            =   ""
            self.database            =   ""
        
        from PyQt5.QtWidgets import QLabel

        if(not (Reset_Names)) :

            self.server_type    =   QLabel()
            self.server_type.setText("Server Type    : " + self.SQL_Database_Type)
            self.server_type.setAlignment(Qt.AlignLeft)
            self.server_type.resize(COLUMN_NAMES_NOTES_HEIGHT,self.table_width)
            self.server_type.setStyleSheet(COLUMN_NAMES_NOTES_STYLE)

            self.dblibrary    =   QLabel()
            self.dblibrary.setText("dblibrary        : " + self.SQL_dblibrary)
            self.dblibrary.setAlignment(Qt.AlignLeft)
            self.dblibrary.resize(COLUMN_NAMES_NOTES_HEIGHT,self.table_width)
            self.dblibrary.setStyleSheet(COLUMN_NAMES_NOTES_STYLE)

            self.dbc_hostname    =   QLabel()
            self.dbc_hostname.setText("hostname       : " + self.hostname)
            self.dbc_hostname.setAlignment(Qt.AlignLeft)
            self.dbc_hostname.resize(COLUMN_NAMES_NOTES_HEIGHT,self.table_width)
            self.dbc_hostname.setStyleSheet(COLUMN_NAMES_NOTES_STYLE)

            self.dbc_database    =   QLabel()
            self.dbc_database.setText("database        : " + self.database)
            self.dbc_database.setAlignment(Qt.AlignLeft)
            self.dbc_database.resize(COLUMN_NAMES_NOTES_HEIGHT,self.table_width)
            self.dbc_database.setStyleSheet(COLUMN_NAMES_NOTES_STYLE)

        else :

            self.server_type.setText("Server Type    : " + self.SQL_Database_Type)            
            self.dblibrary.setText("dblibrary        : " + self.SQL_dblibrary)
            self.dbc_hostname.setText("hostname       : " + self.hostname)
            self.dbc_database.setText("database        : " + self.database)



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                  Column Names Objects end                     -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#











# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                 SQL Import Form Widgets                       -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

COLUMN_NAMES_TITLE_HEIGHT       =   120
COLUMN_NAMES_TITLE_STYLE        =   "font-size: 16px; font-weight: bold; font-family: Arial;" 

COLUMN_NAMES_NOTES_HEIGHT       =   300
COLUMN_NAMES_NOTES_STYLE        =   "font-size: 13px; font-weight: bold; font-family: Arial;" 

ADD_TO_COLUMNS          =   0
ADD_TO_INDEX            =   1
ADD_TO_PARSE_DATES      =   2


class DBUtils_SQLImportFormWidget(QtWidgets.QWidget) :

    def __init__(self,  sqlimpparms, **kwargs):  

        super().__init__()

        self.parent             =   sqlimpparms[0]
        self.build_filetype     =   sqlimpparms[1]
        self.tablenames         =   sqlimpparms[2]
        self.cfg_parms          =   sqlimpparms[3]

        from dfcleanser.Qt.data_import.DataImportModel import SQLTABLE_IMPORT
        if(self.build_filetype==SQLTABLE_IMPORT) :
            self.add_flag           =   ADD_TO_COLUMNS
        else :
            self.add_flag           =   ADD_TO_INDEX

        if(DEBUG_DBUTILS) :
            print("  [DBUtils_SQLImportFormWidget][init] : build_filetypes : len(tablenames) : ",self.build_filetype,len(self.tablenames))
            print("  [DBUtils_SQLImportFormWidget][init] : self.cfg_parms  : \n    ",self.cfg_parms )
        
        if(DEBUG_DBUTILS_SQL_FORM_TABLE_NAMES) :
            print("  [DBUtils_SQLImportFormWidget][init] :tablenames : ",self.tablenames)    
        
        self.init_content()
        
        if(DEBUG_DBUTILS) :
            print("  [DBUtils_SQLImportFormWidget] done : ")

    def init_content(self) :

        if(DEBUG_DBUTILS_SQL_FORM) :
            print("  [DBUtils_SQLImportFormWidget][init_content]")

        selectDicts     =   []
        
        import dfcleanser.Qt.data_import.DataImportModel as DIM

        from dfcleanser.common.common_utils import opStatus
        opstat  =   opStatus()

        try :

            if(not (self.build_filetype==DIM.SQLQUERY_IMPORT)) :

                import_df_titles    =   DIM.get_dftitles_list(DIM.IMPORT_HISTORY,self.build_filetype)
                                
                if(DEBUG_DBUTILS) :
                    print("  [DBUtils_SQLImportFormWidget][init_content] : import_df_titles \n    ",import_df_titles)
        
                if(not (import_df_titles) is None) :
                    last_df_title   =   DIM.get_last_dftitle(DIM.SQLTABLE_IMPORT,import_df_titles)
                else :
                    last_df_title   =    None    

                if(import_df_titles is None) :
                    df_titles           =   {"default":"","list":[""]}
                else :
                    df_titles           =   {"default":str(last_df_title),"list":import_df_titles}

                selectDicts.append(df_titles)
            
                if(DEBUG_DBUTILS) :
                    print("  [DBUtils_SQLImportFormWidget][init_content] : df_titles \n    ",df_titles)

            if(self.tablenames is None) :
                table_names     =   {"default":"","list":[""]}
            else :
                table_names     =   {"default":str(self.tablenames[0]),"list":self.tablenames}
       
            selectDicts.append(table_names)

            flags  =   {"default":"True","list":["True","False"]}
            selectDicts.append(flags)

            if(self.build_filetype==DIM.SQLQUERY_IMPORT) :

                from dfcleanser.sw_utilities.DFCDataStores import get_Dict
                strftimedict = get_Dict("strftime")
            
                strftimekeys    =   list(strftimedict.keys())
                strftimelist    =   []
                for i in range(len(strftimekeys)) :
                    strftimelist.append(strftimekeys[i] + " : " + strftimedict.get(strftimekeys[i]))    
    
                strftimesel     =   {"default":strftimelist[0],"list": strftimelist, "callback": "select_dt_format"}
                selectDicts.append(strftimesel)


            if(DEBUG_DBUTILS) :
                print("  [DBUtils_SQLImportFormWidget][init_content] : selectDicts ",len(selectDicts))

            if(self.build_filetype==DIM.SQLTABLE_IMPORT) :

                form_parms      =   [DIM.pandas_import_sqltable_common_id,DIM.pandas_import_sqltable_common_idList,DIM.pandas_import_sqltable_common_labelList,DIM.pandas_import_sqltable_common_typeList,DIM.pandas_import_sqltable_common_placeholderList,DIM.pandas_import_sqltable_common_reqList]
                comboMethods    =   [self.update_import_sqltable_df,self.import_sqltable_get_tables,None,self.import_sqltable_set_date_format]
                file_methods    =   []
                button_methods  =   [self.import_sqltable,self.set_sql_table_columns_col,self.set_sql_table_index_col,self.set_sql_table_parse_dates,self.return_from_import_sqltable,self.help_import_sqltable]
                cfg_parms       =   self.cfg_parms
                form_title      =   "\nImport SQL Table\n"
                form_width      =   600
                
            elif(self.build_filetype==DIM.SQLQUERY_IMPORT) :

                form_parms      =   [DIM.pandas_import_sqlquery_id,DIM.pandas_import_sqlquery_idList,DIM.pandas_import_sqlquery_labelList,DIM.pandas_import_sqlquery_typeList,DIM.pandas_import_sqlquery_placeholderList,DIM.pandas_import_sqlquery_reqList]
                comboMethods    =   [self.update_import_sqlquery_df,self.import_sqlquery_get_tables,None,self.import_sqlquery_set_date_format]
                file_methods    =   []
                button_methods  =   [self.import_sqlquery,self.set_sql_query_index_col,self.set_sql_query_parse_dates,self.return_from_import_sqlquery,self.help_import_sqlquery]
                cfg_parms       =   self.cfg_parms
                form_title      =   "\nImport SQL Query\n"
                form_width      =   600


            importcomboList     =   selectDicts
        
            form_parms.append(importcomboList)
            form_parms.append(comboMethods)            
            form_parms.append(file_methods)
            form_parms.append(button_methods)            
            form_parms.append(cfg_parms)            
            form_parms.append(form_title)
            form_parms.append(form_width) 

            if(DEBUG_DBUTILS) :
                print("  [DBUtils_SQLImportFormWidget][init_content] : len(form_parms) ",len(form_parms))

            from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget, SMALL
            if(self.build_filetype==DIM.SQLTABLE_IMPORT) :
                self.import_form     =   dfcleanser_input_form_Widget(form_parms,SMALL)
            else :
                self.import_form     =   dfcleanser_input_form_Widget(form_parms,SMALL)

    
        except Exception as e:
            
            title       =   "dfcleanser exception"
            status_msg  =   "[DBUtils_SQLImportFormWidget][init_content] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

        from PyQt5.QtWidgets import QVBoxLayout        
        self.sqlinputformWidgetLayout     =   QVBoxLayout()
        self.sqlinputformWidgetLayout.addWidget(self.import_form)
        self.sqlinputformWidgetLayout.addStretch()

        self.setLayout(self.sqlinputformWidgetLayout)
        self.resize(1070,1100)
    
    def load_sql_form_values(self, cfgparms) :

        if(DEBUG_DBUTILS_SQL_FORM) :
            print("[DBUtils_SQLImportFormWidget][load_form_values] \n    ",cfgparms)
        
        self.cfg_parms          =   cfgparms
        self.import_form.load_form_values(self.cfg_parms) 


    def add_column_to_form(self, colname) :

        if(DEBUG_DBUTILS_SQL_FORM) :
            print("[DBUtils_SQLImportFormWidget][add_column_to_form] : colname : ",colname)

        from dfcleanser.Qt.data_import.DataImportModel import  SQLTABLE_IMPORT
        if(self.build_filetype==SQLTABLE_IMPORT) :

            if(self.add_flag == ADD_TO_COLUMNS) : colid     =   7
            elif(self.add_flag == ADD_TO_INDEX) : colid     =   4
            else                                : colid     =   6

        else :

            if(self.add_flag == ADD_TO_INDEX) : colid     =   4
            else                              : colid     =   7

        list_str        =   self.import_form.get_form_input_value_by_index(colid)
        
        if(DEBUG_DBUTILS_SQL_FORM) :
            print("[DBUtils_SQLImportFormWidget][add_column_to_form] : colid : list_str : ",colid,list_str)

        if(len(list_str) > 0) :

            import ast
            val_list        =  list_str.strip('][').split(', ')
            val_list.append(colname)

        else :

            val_list    =   [colname]

        if(DEBUG_DBUTILS_SQL_FORM) :
            print("[DBUtils_SQLImportFormWidget][add_column_to_form] : val_lis : ",val_list)

        val_list_str    =   "["
        for i in range(len(val_list)) :
            val_list_str    =   val_list_str + str(val_list[i])
            if(i < (len(val_list) - 1)) :
                val_list_str    =   val_list_str + ", "
            else :
                val_list_str    =   val_list_str + "]"
        
        self.import_form.set_form_input_value_by_index(colid,val_list_str)   
    

    # -----------------------------------------------------------------#
    # -            SQL Table Import Form Widgets methods              -#
    # -----------------------------------------------------------------#
    def update_import_sqltable_df(self) :

        if(DEBUG_DBUTILS) :
            print("  [DBUtils_SQLImportFormWidget][update_import_sqltable_df] ")

        df_title    =   self.import_form.get_form_input_value_by_index(1)
        self.import_form.set_form_input_value_by_index(0,df_title)

    def import_sqltable_get_tables(self) :

        if(DEBUG_DBUTILS_SQL_FORM) :
            print("  [DBUtils_SQLImportFormWidget][import_sqltable_get_tables] ")

        table_name    =   self.import_form.get_form_input_value_by_index(2)
        self.parent.columnsWidget.reload_columns(table_name,self.build_filetype)

    def import_sqltable_set_date_format(self) :

        if(DEBUG_DBUTILS_SQL_FORM) :
            print("  [DBUtils_SQLImportFormWidget][import_sqltable_set_date_format] ")

        sformat    =   self.import_form.get_form_input_value_by_index(8)
        self.import_form.set_form_input_value_by_index(7,sformat)
        
    # -----------------------------------------------------------------#
    # -            SQL Table Import Form button methods               -#
    # -----------------------------------------------------------------#
    def import_sqltable(self) :

        if(DEBUG_DBUTILS) :
            print("[DBUtils_SQLImportFormWidget][import_sqltable] ")

        num_form_values     =   11
        form_parms          =   []

        for i in range(num_form_values) :
            form_parms.append(self.import_form.get_form_input_value_by_index(i))

        if(DEBUG_DBUTILS) :
            print("[DBUtils_SQLImportFormWidget][import_sqltable] form_parms : \n  ",form_parms)

        from dfcleanser.Qt.data_import.DataImportControl import process_import_form
        from dfcleanser.Qt.data_import.DataImportModel import SQLTABLE_IMPORT
        process_import_form(SQLTABLE_IMPORT, form_parms, self.parent.display_parent)


    def set_sql_table_columns_col(self) :

        if(DEBUG_DBUTILS) :
            print("\n  [DBUtils_SQLImportFormWidget][set_sql_table_columns_col] ")

        self.add_flag           =   ADD_TO_COLUMNS
        self.parent.update_table_name(self.add_flag)

    def set_sql_table_index_col(self) :

        if(DEBUG_DBUTILS) :
            print("\n  [DBUtils_SQLImportFormWidget][set_sql_table_index_col] ")

        self.add_flag           =   ADD_TO_INDEX
        self.parent.update_table_name(self.add_flag)

    def set_sql_table_parse_dates(self) :

        if(DEBUG_DBUTILS_SQL_FORM) :
            print("\n  [DBUtils_SQLImportFormWidget][set_sql_table_parse_dates] ")

        self.add_flag           =   ADD_TO_PARSE_DATES
        self.parent.update_table_name(self.add_flag)

    def return_from_import_sqltable(self) :

        if(DEBUG_DBUTILS_SQL_FORM) :
            print("\n  [DBUtils_SQLImportFormWidget][return_from_import_sqltable] ")

        self.parent.display_parent.display_import_histories() 

    def help_import_sqltable(self) :

        if(DEBUG_DBUTILS_SQL_FORM) :
            print("\n  [DBUtils_SQLImportFormWidget][help_import_sqltable] ")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import SQLTABLE_IMPORT_URL
        display_url(SQLTABLE_IMPORT_URL)


    # -----------------------------------------------------------------#
    # -            SQL Query Import Form Widgets methods              -#
    # -----------------------------------------------------------------#
    def update_import_sqlquery_df(self) :

        if(DEBUG_DBUTILS_SQL_FORM) :
            print("\n  [DBUtils_SQLImportFormWidget][update_import_sqlquery_df] ")

        df_title    =   self.import_form.get_form_input_value_by_index(1)
        self.import_form.set_form_input_value_by_index(0,df_title)
    
    def import_sqlquery_get_tables(self) :

        if(DEBUG_DBUTILS_SQL_FORM) :
            print("\n  [DBUtils_SQLImportFormWidget][import_sqlquery_get_tables] ")

        table_name    =   self.import_form.get_form_input_value_by_index(3)
        self.parent.columnsWidget.reload_columns(table_name,self.build_filetype)

    
    def import_sqlquery_set_date_format(self) :

        if(DEBUG_DBUTILS_SQL_FORM) :
            print("\n  [DBUtils_SQLImportFormWidget][import_sqlquery_set_date_format] ")

        sformat    =   self.import_form.get_form_input_value_by_index(9)
        self.import_form.set_form_input_value_by_index(8,sformat)
    
    # -----------------------------------------------------------------#
    # -            SQL Query Import Form button methods               -#
    # -----------------------------------------------------------------#
    def import_sqlquery(self) :

        if(DEBUG_DBUTILS) :
            print("\n  [DBUtils_SQLImportFormWidget][import_sqlquery] ")


        num_form_values     =   self.import_form.get_form_fields_count()
        form_parms          =   []

        for i in range(num_form_values) :
            form_parms.append(self.import_form.get_form_input_value_by_index(i))

        if(DEBUG_DBUTILS) :
            print("[DBUtils_SQLImportFormWidget][import_sqlquery] form_parms : \n  ",form_parms)

        from dfcleanser.Qt.data_import.DataImportControl import process_import_form
        from dfcleanser.Qt.data_import.DataImportModel import SQLQUERY_IMPORT
        process_import_form(SQLQUERY_IMPORT, form_parms, self.parent.display_parent)


    def set_sql_query_index_col(self) :

        if(DEBUG_DBUTILS_SQL_FORM) :
            print("\n  [DBUtils_SQLImportFormWidget][set_sql_query_index_col] ")

        self.add_flag           =   ADD_TO_INDEX
        self.parent.update_table_name(self.add_flag)

    def set_sql_query_parse_dates(self) :

        if(DEBUG_DBUTILS_SQL_FORM) :
            print("\n  [DBUtils_SQLImportFormWidget][set_sql_query_parse_dates] ")

        self.add_flag           =   ADD_TO_PARSE_DATES
        self.parent.update_table_name(self.add_flag)

    def return_from_import_sqlquery(self) :

        if(DEBUG_DBUTILS_SQL_FORM) :
            print("\n  [DBUtils_SQLImportFormWidget][return_from_import_sqlquery] ")

        self.parent.display_parent.display_import_histories() 

    def help_import_sqlquery(self) :

        if(DEBUG_DBUTILS_SQL_FORM) :
            print("\n  [DBUtils_SQLImportFormWidget][help_import_sqlquery] ")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import SQLQUERY_IMPORT_URL
        display_url(SQLQUERY_IMPORT_URL)



class DBUtils_SQLImportInputFormWidget(QtWidgets.QWidget) :

    def __init__(self,  sqlimpparms, **kwargs):  

        super().__init__()

        self.display_parent     =   sqlimpparms[0]
        self.build_filetype     =   sqlimpparms[1]
        self.formvals           =   sqlimpparms[2]

        if(DEBUG_DBUTILS) :
            print("\n  [DBUtils_SQLImportInputFormWidget][init] : self.build_filetype : dbid : ",self.build_filetype)
            print("  [DBUtils_SQLImportInputFormWidget][init] : self.formvals : \n  ",self.formvals)

        self.init_content()
        
        if(DEBUG_DBUTILS) :
            print("  [DBUtils_SQLImportInputFormWidget][init] : end ")

    def init_content(self) :

        from dfcleanser.common.common_utils import opStatus
        opstat = opStatus()

        self.set_form_table_col_values(False,opstat)

        if(opstat.get_status()) :
           
            formparms           =   [self,self.build_filetype,self.tableslist,self.formvals]
            self.sqlformWidget  =   DBUtils_SQLImportFormWidget(formparms)
        
            if(DEBUG_DBUTILS_SQL_FORM_DETAILS) :
                print("[DBUtils_SQLImportInputFormWidget][init_content] : built widgets : \n  ",self.columnsWidget," \n  ",self.sqlformWidget)

            from PyQt5.QtWidgets import QHBoxLayout
            self.sqlimportformWidgetLayout     =   QHBoxLayout()
            self.sqlimportformWidgetLayout.addWidget(self.columnsWidget,3)
            self.sqlimportformWidgetLayout.addWidget(self.sqlformWidget,7)
            self.sqlimportformWidgetLayout.setAlignment(Qt.AlignHCenter)

            self.setLayout(self.sqlimportformWidgetLayout)
            self.resize(1070,1000)

            if(DEBUG_DBUTILS_SQL_FORM_DETAILS) :
                print("[DBUtils_SQLImportInputFormWidget][init_content] : self.sqlimportformWidgetLayout geometries : \n  ",self.sqlimportformWidgetLayout.geometry())

        #else :


    def set_form_table_col_values(self,reload_flag,opstat) :

        import dfcleanser.sw_utilities.db_utils as qdbu
        dbconDict   =   qdbu.get_current_dbcondict(qdbu.IMPORT_FLAG)
        
        if(DEBUG_DBUTILS) :
            print("[DBUtils_SQLImportInputFormWidget][set_form_table_col_values] : dbconDict : \n  ",dbconDict)

        try :

            from dfcleanser.sw_utilities.db_utils import  get_table_names 
            self.tableslist =   get_table_names(dbconDict, opstat)
        
            if(opstat.get_status()) :

                if(DEBUG_DBUTILS) :
                    print("[DBUtils_SQLImportInputFormWidget][set_form_table_col_values] : tableslist :  ",len(self.tableslist),self.tableslist[0])
                    print("[DBUtils_SQLImportInputFormWidget][set_form_table_col_values] : self.formvals[2] :  ",self.formvals[2])

                if(self.tableslist is None) :
                    current_table   =   None
                else :
                    
                    # check if input parm tanle is in the tablelist
                    
                    table_found     =   False

                    for i in range(len(self.tableslist)) :
                        if(self.tableslist[i] == self.formvals[2]) :
                            table_found     =   True
                            break

                    if(table_found) :
                        current_table   =  self.formvals[2] 

                    else :
                        
                        """
                        warning_msg     =   "form import parm 'table : " + "'" + self.formvals[2] +  "'" + "not found in connected database.<br><br>"
                        warning_msg1    =   "Verify you are connected to the correct database to find the <br> " + "'" + self.formvals[2] +  "'" + " table.<br><br>"  
                        warning_msg2    =   "Do you want to continue with the current dbconnector and <br> replace the " + "'" + self.formvals[2] +  "'"+ " table parm?.<br>"                                              

                        from PyQt5.QtWidgets import QMessageBox
                        dlg = QMessageBox()
                        dlg.setTextFormat(Qt.RichText)
                        dlg.setWindowTitle("dfcleanser import warning")
                        text_msg    =   warning_msg + warning_msg1 + warning_msg2
                        dlg.setText(text_msg)
                        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                        dlg.setStyleSheet("QLabel{min-width: 350px;}")
            
                        button = dlg.exec()
                        """
                        if(1):#button == QMessageBox.Yes) :

                            self.formvals[2]    =   self.tableslist[0]
                            current_table       =   self.tableslist[0] 

                        else :

                            opstat.set_status(False)
                            return(opstat)

                if(DEBUG_DBUTILS) :
                    print("[DBUtils_SQLImportInputFormWidget][set_form_table_col_values] : self.formvals[2] :  ",self.formvals[2])
                    print("[DBUtils_SQLImportInputFormWidget][set_form_table_col_values] : current_table :  ",current_table)

                if(not (reload_flag)) :

                    tableparms              =   [self,current_table,dbconDict,self.build_filetype]
                    self.columnsWidget      =   DBUtils_ColumnNamesWidget(tableparms) 

                else :

                    self.columnsWidget.reload_columns(current_table,self.build_filetype)
                    self.columnsWidget.set_dbcon_parms(True)

                    if(DEBUG_DBUTILS) :
                        print("[DBUtils_SQLImportInputFormWidget][set_form_table_col_values] : done :  ")

            else :

                title       =   "dfcleanser exception"
                status_msg  =   "[DBUtils_SQLImportInputFormWidget] db tables error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,opstat.get_exception())

                opstat.set_status(False)


        except Exception as e:

            title       =   "dfcleanser exception"
            status_msg  =   "[DBUtils_SQLImportInputFormWidget] db columns error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)

        return(opstat)


    def reload_sql_import_form_values(self, formvals) :

        from dfcleanser.common.common_utils import opStatus
        opstat = opStatus()

        self.display_parent     =   formvals[0]
        self.build_filetype     =   formvals[1]
        self.formvals           =   formvals[2]

        if(DEBUG_DBUTILS) :
             print("\n[DBUtils_SQLImportInputFormWidget][reload_sql_import_form_values] : self.build_filetype : ",self.build_filetype)
             print("[DBUtils_SQLImportInputFormWidget][reload_sql_import_form_values] : formvals : \n  ",self.formvals)

        self.set_form_table_col_values(True,opstat)  

        if(opstat.get_status()) :

            self.sqlformWidget.load_sql_form_values(self.formvals)
        
            import dfcleanser.sw_utilities.db_utils as qdbu
            dbconDict   =   qdbu.get_current_dbcondict(0)

            from dfcleanser.sw_utilities.db_utils import  get_table_names 
            tableslist =   get_table_names(dbconDict, opstat)
        
            if(opstat.get_status()) :

                if(DEBUG_DBUTILS) :
                    print("  [DBUtils_SQLImportInputFormWidget][reload_sql_import_form_values] : new tableslist :  ",len(tableslist),tableslist[0])

                self.tableslist     =   tableslist
                self.sqlformWidget.import_form.reset_form_combobox_by_index(2,self.tableslist)

        if(DEBUG_DBUTILS) :
             print("  [DBUtils_SQLImportInputFormWidget][reload_sql_import_form_values] : end : ")

       
    def add_column_name(self, colname) :

        if(DEBUG_DBUTILS) :
             print("[DBUtils_SQLImportInputFormWidget][add_column_name] : colname : ",colname)

        self.sqlformWidget.add_column_to_form(colname)
        

    def update_table_name(self, addflag) :

        if(DEBUG_DBUTILS) :
             print("  [DBUtils_SQLImportInputFormWidget][update_table_name] : addflag : ",addflag)

        if(self.sqlformWidget.add_flag == ADD_TO_COLUMNS)   : new_table_name  =   "'columns' Columns"
        elif(self.sqlformWidget.add_flag == ADD_TO_INDEX)   : new_table_name  =   "'index_col' Columns"
        else                                                : new_table_name  =   "'parse_dates' Columns"

        self.columnsWidget.column_names_table.set_table_name(new_table_name)


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                SQL Import Form Widgets end                    -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                 SQL Export Form Widgets                       -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

COLUMN_NAMES_TITLE_HEIGHT       =   120
COLUMN_NAMES_TITLE_STYLE        =   "font-size: 16px; font-weight: bold; font-family: Arial;" 

COLUMN_NAMES_NOTES_HEIGHT       =   300
COLUMN_NAMES_NOTES_STYLE        =   "font-size: 13px; font-weight: bold; font-family: Arial;" 

ADD_TO_COLUMNS          =   0
ADD_TO_INDEX            =   1
ADD_TO_PARSE_DATES      =   2


class DBUtils_SQLExportFormWidget(QtWidgets.QWidget) :

    def __init__(self,  sqlimpparms, **kwargs):  

        super().__init__()

        self.parent             =   sqlimpparms[0]
        self.build_filetype     =   sqlimpparms[1]
        self.cfg_parms          =   sqlimpparms[2]

        if(DEBUG_DBUTILS) :
            print("  [DBUtils_SQLExportFormWidget][init] : build_filetype : : ",self.build_filetype)
            print("  [DBUtils_SQLExortFormWidget][init] : self.cfg_parms  : \n    ",self.cfg_parms )
        
        self.init_content()
        
        if(DEBUG_DBUTILS) :
            print("  [DBUtils_SQLExportFormWidget] done : ")

    def init_content(self) :

        if(DEBUG_DBUTILS_SQL_FORM) :
            print("  [DBUtils_SQLExportFormWidget][init_content]")

        selectDicts     =   []
        
        import dfcleanser.Qt.data_export.DataExportModel as DEM

        from dfcleanser.common.common_utils import opStatus
        opstat  =   opStatus()

        try :

            from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
            active_dfs      =   get_dfc_dataframes_titles_list()
                                
            if(DEBUG_DBUTILS) :
                print("  [DBUtils_SQLExportFormWidget][init_content] : active_dfs \n    ",active_dfs)
        
            if(active_dfs is None) :
                df_titles           =   {"default":"","list":[""]}
            else :
                df_titles           =   {"default":str(active_dfs[0]),"list":active_dfs}

            selectDicts.append(df_titles)
            
            if(DEBUG_DBUTILS) :
                print("  [DBUtils_SQLExportFormWidget][init_content] : df_titles \n    ",df_titles)

            if_exists   =   {"default":"fail","list":["fail","replace","append"]}
            selectDicts.append(if_exists)
            
            flags       =   {"default":"True","list":["True","False"]}
            selectDicts.append(flags)

            methods     =   {"default":"None","list":["None","'multi'","'callable'"]}
            selectDicts.append(methods)



            if(DEBUG_DBUTILS) :
                print("  [DBUtils_SQLExportFormWidget][init_content] : selectDicts ",len(selectDicts))

            if(self.build_filetype==DEM.SQLTABLE_EXPORT) :

                form_parms      =   [DEM.pandas_export_sqltable_id,DEM.pandas_export_sqltable_idList,DEM.pandas_export_sqltable_labelList,DEM.pandas_export_sqltable_typeList,DEM.pandas_export_sqltable_placeholderList,DEM.pandas_export_sqltable_reqList]
                comboMethods    =   [self.update_export_sqltable_df,None,None,None]
                file_methods    =   []
                button_methods  =   [self.export_sqltable,self.clear_export_sqltable,self.return_from_export_sqltable,self.help_export_sqltable]
                cfg_parms       =   self.cfg_parms
                form_title      =   "\nExport SQL Table\n"
                form_width      =   600
                

            exportcomboList     =   selectDicts
        
            form_parms.append(exportcomboList)
            form_parms.append(comboMethods)            
            form_parms.append(file_methods)
            form_parms.append(button_methods)            
            form_parms.append(cfg_parms)            
            form_parms.append(form_title)
            form_parms.append(form_width) 

            if(DEBUG_DBUTILS) :
                print("[DBUtils_SQLExportFormWidget][init_content] : len(form_parms) ",len(form_parms))

            from dfcleanser.sw_utilities.dfc_qt_model import dfcleanser_input_form_Widget, SMALL
            self.export_form     =   dfcleanser_input_form_Widget(form_parms,SMALL)

            if(DEBUG_DBUTILS) :
                print("[DBUtils_SQLExportFormWidget][init_content] : form built ")

    
        except Exception as e:
            
            title       =   "dfcleanser exception"
            status_msg  =   "[DBUtils_SQLExportFormWidget][init_content] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

        from PyQt5.QtWidgets import QVBoxLayout        
        self.sqlinputformWidgetLayout     =   QVBoxLayout()
        self.sqlinputformWidgetLayout.addWidget(self.export_form)
        self.sqlinputformWidgetLayout.addStretch()

        self.setLayout(self.sqlinputformWidgetLayout)
        self.resize(1070,1100)
    
    def load_sql_form_values(self, cfgparms) :

        if(DEBUG_DBUTILS_SQL_FORM) :
            print("[DBUtils_SQLExportFormWidget][load_form_values] \n    ",cfgparms)
        
        self.cfg_parms          =   cfgparms
        self.export_form.load_form_values(self.cfg_parms) 


    # -----------------------------------------------------------------#
    # -            SQL Table Import Form Widgets methods              -#
    # -----------------------------------------------------------------#
    
    
    def update_export_sqltable_df(self) :

        if(DEBUG_DBUTILS) :
            print("  [DBUtils_SQLExportFormWidget][update_export_sqltable_df] ")

        df_title    =   self.export_form.get_form_input_value_by_index(0)
        self.export_form.set_form_input_value_by_index(1,df_title)



    # -----------------------------------------------------------------#
    # -            SQL Table Import Form button methods               -#
    # -----------------------------------------------------------------#
    def export_sqltable(self) :

        if(DEBUG_DBUTILS) :
            print("[DBUtils_SQLExportFormWidget][export_sqltable] ")

        num_form_values     =   9
        form_parms          =   []

        for i in range(num_form_values) :
            form_parms.append(self.export_form.get_form_input_value_by_index(i))

        if(DEBUG_DBUTILS) :
            print("[DBUtils_SQLExportFormWidget][export_sqltable] form_parms : \n  ",form_parms)

        from dfcleanser.Qt.data_export.DataExportControl import process_export_form
        from dfcleanser.Qt.data_export.DataExportModel import SQLTABLE_EXPORT
        process_export_form(SQLTABLE_EXPORT, form_parms, self.parent.display_parent)

    def clear_export_sqltable(self) :

        if(DEBUG_DBUTILS) :
            print("\n  [DBUtils_SQLImportFormWidget][clear_export_sqltable] ")

        total_values    =   self.export_form.get_form_fields_count()

        for i in range(total_values) :
            self.export_form. set_form_input_value_by_index(i,"")   
 
    def return_from_export_sqltable(self) :

        if(DEBUG_DBUTILS_SQL_FORM) :
            print("\n  [DBUtils_SQLExportFormWidget][return_from_export_sqltable] ")

        self.parent.display_parent.display_export_histories() 

    def help_export_sqltable(self) :

        if(DEBUG_DBUTILS_SQL_FORM) :
            print("\n  [DBUtils_SQLExportFormWidget][help_export_sqltable] ")

        from dfcleanser.common.common_utils import display_url
        from dfcleanser.common.help_utils import SQLTABLE_EXPORT_URL
        display_url(SQLTABLE_EXPORT_URL)



class DBUtils_SQLExportInputFormWidget(QtWidgets.QWidget) :

    def __init__(self,  sqlimpparms, **kwargs):  

        super().__init__()

        self.display_parent     =   sqlimpparms[0]
        self.build_filetype     =   sqlimpparms[1]
        self.formvals           =   sqlimpparms[2]

        if(DEBUG_DBUTILS) :
            print("\n  [DBUtils_SQLExportInputFormWidget][init] : self.build_filetype : ",self.build_filetype)
            print("  [DBUtils_SQLExportInputFormWidget][init] : self.formvals : \n  ",self.formvals)

        self.init_content()
        
        if(DEBUG_DBUTILS) :
            print("  [DBUtils_SQLExportInputFormWidget][init] : end ")

    def init_content(self) :

        from dfcleanser.common.common_utils import opStatus
        opstat = opStatus()

        #self.set_form_table_values(False,opstat)

        import dfcleanser.sw_utilities.db_utils as qdbu
        dbconDict   =   qdbu.get_current_dbcondict(qdbu.EXPORT_FLAG)

        tableparms              =   [self,dbconDict,self.build_filetype]
        self.tablesWidget       =   DBUtils_TableNamesWidget(tableparms) 


        if(opstat.get_status()) :
           
            formparms           =   [self,self.build_filetype,self.formvals]
            self.sqlformWidget  =   DBUtils_SQLExportFormWidget(formparms)
        
            if(DEBUG_DBUTILS_SQL_FORM_DETAILS) :
                print("[DBUtils_SQLExportInputFormWidget][init_content] : built widgets : \n  ",self.columnsWidget," \n  ",self.sqlformWidget)

            from PyQt5.QtWidgets import QHBoxLayout
            self.sqlexportformWidgetLayout     =   QHBoxLayout()
            self.sqlexportformWidgetLayout.addWidget(self.tablesWidget,3)
            self.sqlexportformWidgetLayout.addWidget(self.sqlformWidget,7)
            self.sqlexportformWidgetLayout.setAlignment(Qt.AlignHCenter)

            self.setLayout(self.sqlexportformWidgetLayout)
            self.resize(1070,1000)

            if(DEBUG_DBUTILS_SQL_FORM_DETAILS) :
                print("  [DBUtils_SQLExportInputFormWidget][init_content] : self.sqlimportformWidgetLayout geometries : \n  ",self.sqlexportformWidgetLayout.geometry())

        #else :


    def set_form_table_values(self,reload_flag,opstat) :

        try :

            import dfcleanser.sw_utilities.db_utils as qdbu
            dbconDict   =   qdbu.get_current_dbcondict(qdbu.EXPORT_FLAG)
        
            if(DEBUG_DBUTILS) :
                print("  [DBUtils_SQLExportInputFormWidget][set_form_table_col_values] : dbconDict : \n  ",dbconDict)

            from dfcleanser.sw_utilities.db_utils import  get_table_names 
            self.tableslist =   get_table_names(dbconDict, opstat)
        
            if(opstat.get_status()) :

                if(DEBUG_DBUTILS) :
                    print("  [DBUtils_SQLExportInputFormWidget][set_form_table_col_values] : tableslist :  ",len(self.tableslist),self.tableslist[0])
                    print("  [DBUtils_SQLExportInputFormWidget][set_form_table_col_values] : self.formvals[1] :  ",self.formvals[1])

                if(self.tableslist is None) :
                    current_table   =   None
                else :
                    
                    # check if input parm tanle is in the tablelist
                    
                    table_found     =   False

                    for i in range(len(self.tableslist)) :
                        if(self.tableslist[i] == self.formvals[1]) :
                            table_found     =   True
                            break

                    if(table_found) :
                        current_table   =  self.formvals[1] 

                    else :


                        self.formvals[1]    =   self.tableslist[0]
                        current_table       =   self.tableslist[0] 

                if(DEBUG_DBUTILS) :
                    print("  [DBUtils_SQLExportInputFormWidget][set_form_table_values] : self.formvals[2] :  ",self.formvals[1])
                    print("  [DBUtils_SQLExportInputFormWidget][set_form_table_values] : current_table :  ",current_table)

                if(not (reload_flag)) :

                    tableparms              =   [self,dbconDict,self.build_filetype]
                    self.tablesWidget       =   DBUtils_TableNamesWidget(tableparms) 

                else :

                    self.tablesWidget.reload_tables(self.build_filetype)
                    self.tablesWidget.set_dbcon_parms(True)

                    if(DEBUG_DBUTILS) :
                        print("  [DBUtils_SQLExportInputFormWidget][set_form_table_values] : done :  ")

            else :

                title       =   "dfcleanser exception"
                status_msg  =   "[DBUtils_SQLExportInputFormWidget] db tables error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,opstat.get_exception())

                opstat.set_status(False)


        except Exception as e:

            title       =   "dfcleanser exception"
            status_msg  =   "[set_form_table_values] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)

        return(opstat)


    def reload_sql_export_form_values(self, formvals) :

        from dfcleanser.common.common_utils import opStatus
        opstat = opStatus()

        self.display_parent     =   formvals[0]
        self.build_filetype     =   formvals[1]
        self.formvals           =   formvals[2]

        if(DEBUG_DBUTILS) :
             print("\n  [DBUtils_SQLExportInputFormWidget][reload_sql_export_form_values] : self.build_filetype : ",self.build_filetype)
             print("  [DBUtils_SQLExportInputFormWidget][reload_sql_export_form_values] : formvals : \n  ",self.formvals)

        self.set_form_table_col_values(True,opstat)  

        if(opstat.get_status()) :

            self.sqlformWidget.load_sql_form_values(self.formvals)
        
            import dfcleanser.sw_utilities.db_utils as qdbu
            dbconDict   =   qdbu.get_current_dbcondict(0)

            from dfcleanser.sw_utilities.db_utils import  get_table_names 
            tableslist =   get_table_names(dbconDict, opstat)
        
            if(opstat.get_status()) :

                if(DEBUG_DBUTILS) :
                    print("  [DBUtils_SQLImportInputFormWidget][reload_sql_import_form_values] : new tableslist :  ",len(tableslist),tableslist[0])

                self.tableslist     =   tableslist
                self.sqlformWidget.import_form.reset_form_combobox_by_index(2,self.tableslist)

        if(DEBUG_DBUTILS) :
             print("  [DBUtils_SQLImportInputFormWidget][reload_sql_import_form_values] : end : ")

       
    def set_table_name(self, tablename) :

        if(DEBUG_DBUTILS) :
             print("  [DBUtils_SQLExportInputFormWidget][set_table_name] : colname : ",tablename)

        self.sqlformWidget.export_form.set_form_input_value_by_index(1,tablename)
        

    def update_table_name(self, addflag) :

        if(DEBUG_DBUTILS) :
             print("  [DBUtils_SQLImportInputFormWidget][update_table_name] : addflag : ",addflag)

        if(self.sqlformWidget.add_flag == ADD_TO_COLUMNS)   : new_table_name  =   "'columns' Columns"
        elif(self.sqlformWidget.add_flag == ADD_TO_INDEX)   : new_table_name  =   "'index_col' Columns"
        else                                                : new_table_name  =   "'parse_dates' Columns"

        self.tablesWidget.column_names_table.set_table_name(new_table_name)


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                SQL Import Form Widgets end                    -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                   SQL Import Widgets end                      -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -               Cpmmon form dbconnector methods                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

def build_dbcon_form_data(dbconnectParms) :

    if(DEBUG_DBUTILS):#_DBCONNECTOR_FORM) :
        print("  [DBUtils_DBConnectorFormWidget][build_dbcon_form_data] dbconnectParms \n    ",dbconnectParms)

    import dfcleanser.sw_utilities.db_utils as qdbu

    if(not (dbconnectParms is None)) :
    
        servertype          =   dbconnectParms[0]

        if(DEBUG_DBUTILS_DBCONNECTOR_FORM) :
            print("  [DBUtils_DBConnectorFormWidget][build_dbcon_form_data] servertype ",type(servertype),servertype)

        if(type(servertype) == str) :
            servertype_id       =   qdbu.get_db_id_from_dbid_title(servertype)
            #servertype          =   qdbu.get_db_id_title(servertype_id)
        else :
            servertype_id       =   servertype#qdbu.get_db_id_from_dbid_title(servertype)
            server_type         =   qdbu.get_db_id_title(servertype_id)

        if(DEBUG_DBUTILS_DBCONNECTOR_FORM) :
            print("  [DBUtils_DBConnectorFormWidget][build_dbcon_form_data] servertype  ",type(servertype),servertype)
            print("  [DBUtils_DBConnectorFormWidget][build_dbcon_form_data] servertype_id  ",type(servertype_id),servertype_id)

        dblibrary           =   dbconnectParms[1]
        servername          =   dbconnectParms[2]
        database            =   dbconnectParms[3]
        user                =   dbconnectParms[4]
        password            =   dbconnectParms[5]

    else :

        servertype          =   qdbu.MySql
        servertype          =   qdbu.get_db_id_title(servertype)
        dblibrary           =   qdbu.pymysql_library
        servername          =   ""
        database            =   ""
        user                =   ""
        password            =   ""

        servertype_id       =   qdbu.get_db_id_from_dbid_title(servertype)

    formParms               =   []

    if(DEBUG_DBUTILS_DBCONNECTOR_FORM) :
        print("  [DBUtils_DBConnectorFormWidget][build_dbcon_form_data] servertype : servertype_id ",servertype,servertype_id,type(servertype_id),type(qdbu.MySql))

    if(servertype_id == qdbu.MySql)               :    
        formParms           =   [qdbu.mysql_connector_id,qdbu.mysql_connector_idList,qdbu.mysql_connector_labelList,qdbu.mysql_connector_typeList,qdbu.mysql_connector_placeholderList,qdbu.mysql_connector_reqList] 
        dblibrary_types     =   {"default":qdbu.pymysql_library,"list":[qdbu.pymysql_library,qdbu.mysql_connector_library]}
        cfg_parms           =   [servertype,dblibrary,servername,database,user,password]

        if(DEBUG_DBUTILS_DBCONNECTOR_FORM) :
            print("  [DBUtils_DBConnectorFormWidget][build_dbcon_form_data] formparms ",formParms)

    elif(servertype_id == qdbu.MS_SQL_Server)     :    
        formParms           =   [qdbu.mssql_connector_id,qdbu.mssql_connector_idList,qdbu.mssql_connector_labelList,qdbu.mssql_connector_typeList,qdbu.mssql_connector_placeholderList,qdbu.mssql_connector_reqList] 
        dblibrary_types     =   {"default":qdbu.pyodbc_library,"list":[qdbu.pyodbc_library,qdbu.pymssql_library]}
        cfg_parms           =   [servertype,dblibrary,servername,database,user,password]
    elif(servertype_id == qdbu.SQLite)            :    
        formParms           =   [qdbu.sqlite_connector_id,qdbu.sqlite_connector_idList,qdbu.sqlite_connector_labelList,qdbu.sqlite_connector_typeList,qdbu.sqlite_connector_placeholderList,qdbu.sqlite_connector_reqList] 
        dblibrary_types     =   {"default":qdbu.sqlite_library,"list":[qdbu.sqlite_library]}
        cfg_parms           =   [servertype,dblibrary,servername]
    elif(servertype_id == qdbu.Postgresql)        :    
        formParms           =   [qdbu.Postgresql_connector_id,qdbu.Postgresql_connector_idList,qdbu.Postgresql_connector_labelList,qdbu.Postgresql_connector_typeList,qdbu.Postgresql_connector_placeholderList,qdbu.Postgresql_connector_reqList] 
        dblibrary_types     =   {"default":qdbu.psycopg2_library,"list":[qdbu.psycopg2_library]}
        cfg_parms           =   [servertype,dblibrary,servername,database,user,password]
    elif(servertype_id == qdbu.Oracle)            :    
        formParms           =   [qdbu.oracle_connector_id,qdbu.oracle_connector_idList,qdbu.oracle_connector_labelList,qdbu.oracle_connector_typeList,qdbu.oracle_connector_placeholderList,qdbu.oracle_connector_reqList] 
        dblibrary_types     =   {"default":qdbu.cx_oracle_library,"list":[qdbu.cx_oracle_library]}
        cfg_parms           =   [servertype,dblibrary,servername,user,password]
    elif(servertype_id == qdbu.Custom)            :    
        formParms           =   [qdbu.custom_connector_id,qdbu.custom_connector_idList,qdbu.custom_connector_labelList,qdbu.custom_connector_typeList,qdbu.custom_connector_placeholderList,qdbu.custom_connector_reqList] 
        dblibrary_types     =   None           
        cfg_parms           =   [servertype,dblibrary,"","","",""]

    if(DEBUG_DBUTILS_DBCONNECTOR_FORM) :
        print("[DBUtils_DBConnectorFormWidget][build_dbcon_form_data] formParms : ",len(formParms))
        #for i in range(len(formParms)) :
        #    print("  formParms[",i,"] ",formParms[i])
        
    return([formParms,dblibrary_types,cfg_parms])
    




# -----------------------------------------------------------------#
# -               Cpmmon test dbconnector methods                 -#
# -----------------------------------------------------------------#

def common_test_db_connector(dbconnectParms) :

    if(DEBUG_DBUTILS) :    
        print("\n[DBUtilsWidgets][common_test_db_connector] :  dbconnectparms :  \n  ",dbconnectParms)

    import dfcleanser.sw_utilities.db_utils as qdbu
    
    dbid                    =   int(dbconnectParms[0])
    SQL_Server_Type         =   int(dbconnectParms[0])
    SQL_Server_Type_Title   =   qdbu.get_db_id_title(SQL_Server_Type)
    db_library              =   dbconnectParms[1]
    Server_Name             =   dbconnectParms[2]
    Database                =   dbconnectParms[3]
    User                    =   dbconnectParms[4]
    Password                =   dbconnectParms[5]
    
    if(DEBUG_DBUTILS):#_TEST_CONNECTOR) :    
        print("[DBUtilsWidgets][common_test_db_connector] : parms \n  ",SQL_Server_Type,db_library,Server_Name,Database,User,Password)


    if(SQL_Server_Type == qdbu.MySql) :
        dbcon_labels    =   qdbu.mysql_connector_idList[0:6]
        dbcon_vals      =   [str(SQL_Server_Type),db_library,Server_Name,Database,User,Password]
        
    elif(SQL_Server_Type == qdbu.MS_SQL_Server) :
        dbcon_labels    =   qdbu.mssql_connector_idList[0:6]
        dbcon_vals      =   [str(SQL_Server_Type),db_library,Server_Name,Database,User,Password]

    elif(SQL_Server_Type == qdbu.SQLite) :
        dbcon_labels    =   qdbu.sqlite_connector_idList[0:3]
        dbcon_vals      =   [str(SQL_Server_Type),db_library,Server_Name]

    elif(SQL_Server_Type == qdbu.Postgresql) :
        dbcon_labels    =   qdbu.Postgresql_connector_idList[0:6]
        dbcon_vals      =   [str(SQL_Server_Type),db_library,Server_Name,Database,User,Password]
        
    elif(SQL_Server_Type == qdbu.Oracle) :
        dbcon_labels    =   qdbu.oracle_connector_idList[0:5]
        dbcon_vals      =   [str(SQL_Server_Type),db_library,Server_Name,User,Password]
    
    elif(SQL_Server_Type == qdbu.Custom) :
        dbcon_labels    =   qdbu.custom_connector_idList[0]
        dbcon_vals      =   [db_library]

    dbconnect_parms     =   [dbcon_labels,dbcon_vals]
    sqlid               =   qdbu.SQL_IMPORT

    if(DEBUG_DBUTILS_TEST_CONNECTOR) :    
        print("[DBUtilsWidgets][common_test_db_connector] : sqlid : ",sqlid,"\n   ",dbconnect_parms)

    from dfcleanser.common.common_utils import (opStatus)
    opstat              =   opStatus()
    status_msg          =   ""

    test_sqlalchemy     =   True

    if(DEBUG_DBUTILS_TEST_CONNECTOR) :    
        print("[DBUtilsWidgets][common_test_db_connector] :test \n ",dbconnect_parms)

    if( not (SQL_Server_Type == qdbu.Custom)) :

        qdbu.test_db_connector(dbid,qdbu.NATIVE,dbconnect_parms,sqlid,opstat,display=False)
    
        if(DEBUG_DBUTILS_TEST_CONNECTOR) :    
            print("[DBUtilsWidgets][common_test_db_connector] : dbconnect_parms\n ",dbconnect_parms)

        if(opstat.get_status()) :

            status_msg  =  "Native " + str(SQL_Server_Type_Title) + " " + db_library + " connected successfully : " 

        else :

            status_msg  =  "Native " + str(SQL_Server_Type_Title) + " " + db_library + " dbconnector failled to connect : "

            from dfcleanser.sw_utilities.DisplayUtils import get_exception_details_text
            details_msg     =   get_exception_details_text(opstat)

            if(DEBUG_DBUTILS_TEST_CONNECTOR) :    
                print("\n\n[DBUtilsWidgets][common_test_db_connector] : details_msg ",details_msg)

            details_msg     =   details_msg.replace("\n","<br>")
            from dfcleanser.sw_utilities.dfc_qt_model import format_QMessageBox_Text
            final_msg       =   format_QMessageBox_Text(details_msg)

            from PyQt5.QtWidgets import QMessageBox
            dlg = QMessageBox()
            dlg.setTextFormat(Qt.RichText)
            dlg.setWindowTitle("Native Connector Connect Failure")
            text_msg    =   final_msg + "<br>Do you want to test SQLAlchemy Connector?"
            dlg.setText(text_msg)
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setStyleSheet("QLabel{min-width: 350px;}")
            
            button = dlg.exec()

            if button == QMessageBox.Yes:
                test_sqlalchemy     =   True
            else :
                test_sqlalchemy     =   False

    if(test_sqlalchemy) :

        qdbu.test_db_connector(dbid,qdbu.SQLALCHEMY,dbconnect_parms,sqlid,opstat,display=False)
        
        if(DEBUG_DBUTILS_TEST_CONNECTOR) :    
            print("[DBUtilsWidgets][common_test_db_connector] sqlalchemy : opstat.get_status() ",opstat.get_status())

        if(opstat.get_status()) :

            status_msg  =  status_msg + "SQLAlchemy " + str(SQL_Server_Type_Title) + " dbconnector connected successfully" 

        else :

            status_msg  =  status_msg + " : SQLAlchemy " + str(SQL_Server_Type_Title) +  " failled to connect"

            from dfcleanser.sw_utilities.DisplayUtils import get_exception_details_text
            details_msg     =   get_exception_details_text(opstat)
            details_msg     =   details_msg.replace("\n","<br>") 
            from dfcleanser.sw_utilities.dfc_qt_model import format_QMessageBox_Text
            final_msg       =   format_QMessageBox_Text(details_msg)

            if(DEBUG_DBUTILS_TEST_CONNECTOR) :    
                print("[DBUtilsWidgets][common_test_db_connector] : details_msg ",details_msg)

            from PyQt5.QtWidgets import QMessageBox
            dlg = QMessageBox()
            dlg.setTextFormat(Qt.RichText)
            dlg.setWindowTitle("SQLAlchemy Connector Connect Failure")
            text_msg    =   final_msg
            dlg.setText(text_msg)
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setStyleSheet("QLabel{min-width: 350px;}");
            button = dlg.exec()
        

    if(DEBUG_DBUTILS) :    
        print("[DBUtilsDBConnectorsTableWidget][common_test_db_connector] : end ")

    return(status_msg)


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                   DBConnector Widgets end                     -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#



















