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

DEBUG_DATA_INSPECT_COLUMNS              =   False
DEBUG_DATA_INSPECT_COLUMNS_DETAILS      =   False

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -           general Data Inspection Housekeeping                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

import logging
logger = logging.getLogger(__name__)

DEFAULT_ROW_HEIGHT                  =   20



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -               DataInspection Column Index                     -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

# -----------------------------------------------------------------#
# -              Table Model for df columns index                 -#
# -----------------------------------------------------------------#

class DataInspectionColumnsIndexModel(QtCore.QAbstractTableModel):
    def __init__(self, indexdata, colheaders):

        super(DataInspectionColumnsIndexModel, self).__init__()
        self._data          =   indexdata
        self.column_names   =   colheaders

    def reload_data(self,indexdata) :
        self._data = indexdata

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

            # odd = (section % 2) 
            #if(section == 0) :
            #    return('Data Type')
            #elif(section == 1) :
            #    return('Count')
            #else :
            #    return("Column Names")

        return super().headerData(section, orientation, role)


# -----------------------------------------------------------------#
# -    Subclass of QMainWindow to disp[lay the columns uniques    -#
# -----------------------------------------------------------------#
class DataInspectionColumnsIndexTable(QtWidgets.QTableView):

    def __init__(self, dfparms, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None

        self.df                 =   None
        self.dftitle            =   dfparms[0]

        if(DEBUG_DATA_INSPECT_COLUMNS_DETAILS) :
            print("\n  [DataInspectionColumnsIndexTable] : init")

        if(self.df is None) :
            from dfcleanser.common.cfg import get_dfc_dataframe_df 
            df          =   get_dfc_dataframe_df(self.dftitle)
            self.df     =   df
        else :
            df  =   self.df

        self.init_tableview()

        if(DEBUG_DATA_INSPECT_COLUMNS_DETAILS) :
            print("  [DataInspectionColumnsIndexTable] : init_tableview done")

    
    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(DEBUG_DATA_INSPECT_COLUMNS_DETAILS) :
            print("  [DataInspectionColumnsIndexTable] : init_tableview",self.dftitle)

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        columnsdata     =   self.load_columns_index_data()

        if(self.model is None) :
            self.model = DataInspectionColumnsIndexModel(columnsdata,self.column_headers)
            self.setModel(self.model)

        if(DEBUG_DATA_INSPECT_COLUMNS_DETAILS) :
           print("  [DataInspectionColumnsIndexTable] : model loaded",columnsdata)

        if(len(columnsdata) == 6) :
            column_widths   =   [220,278,120,120,120,120]
        else :
            column_widths   =   [220,278,120,120,120,120,120]

        self.num_rows   =   len(columnsdata)

        new_height  =   40 + (self.num_rows * DEFAULT_ROW_HEIGHT)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)

        if(DEBUG_DATA_INSPECT_COLUMNS_DETAILS) :
           print("  [DataInspectionColumnsIndexTable] : new_height",new_height)


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
        nrows = len(columnsdata)
        for row in range(nrows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        #column_widths   =   [200,90,660]
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(column_widths)) :
           self.setColumnWidth(i, column_widths[i])     
        
        self.setWordWrap(True)


    # -----------------------------------------------------------------#
    # -                 Initialize the table data                     -#
    # -----------------------------------------------------------------#
    def load_columns_index_data(self):

        if(DEBUG_DATA_INSPECT_COLUMNS_DETAILS) :
            print("  [DataInspectionColumnsIndexTable] : load_columns_index_data ")

        from dfcleanser.Qt.data_inspection.DataInspectionModel import get_df_index_columns_data
        df_data_info = get_df_index_columns_data(self.df)

        colids       =   df_data_info[0]
        coldata      =   df_data_info[1]
        dfvalues     =   df_data_info[2]

        if(DEBUG_DATA_INSPECT_COLUMNS_DETAILS) :
            print("  [DataInspectionColumnsIndexTable] : df_data_info \ncolids : \n          ",colids,"\n    coldata :\n   ",coldata,"\n    dfvalues : \n    ",dfvalues)


        index_columns   =   self.df.index.names
        index_names     =   []
        for i in range(len(index_columns)) :
            if(not (index_columns[i] is None)) :
                index_names.append(index_columns[i])

        column_headers  =   []
        data            =   []

        import pandas as pd
        if( (not (isinstance(self.df.index, pd.core.indexes.multi.MultiIndex)))  or (len(index_names) == 1)) :

            data_row    =   []
            for i in range(len(coldata)) :
                column_headers.append(colids[i])
                data_row.append(coldata[i])

            data.append(data_row)

        if(len(index_names) > 1) :
    
            for i in range(len(index_columns)) :

                data_row    =   []

                if( not (index_columns[i] is None) ) :

                    data_row.append("MultiIndex")
                    data_row.append(index_columns[i])
                    data_row.append(str(self.df.index.levels[i].dtype))
                    data_row.append(len(dfvalues))
                    data_row.append(len(self.df.index.levels[i].unique()))
                    str(self.df.index.levels[i].max())
                    str(self.df.index.levels[i].min())

                    data.append(data_row)

            for i in range(len(colids)) :
                column_headers.append(colids[i])   


        if(DEBUG_DATA_INSPECT_COLUMNS_DETAILS) :
            print("  [DataInspectionColumnsIndexTable] : data\n ",data)

        self.column_headers     =   column_headers
        self.num_rows           =   len(data)

        return(data)

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -             DataInspection Column Index end                   -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -               DataInspection Column Stats                     -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -              Table Model for df columns index                 -#
# -----------------------------------------------------------------#

green_color     =   QColor(173, 236, 196)
yellow_color    =   QColor(250, 246, 190)
red_color       =   QColor(241, 196, 183) 

class DataInspectionColumnsStatsModel(QtCore.QAbstractTableModel):
    def __init__(self, statsdata, col_headers):

        super(DataInspectionColumnsStatsModel, self).__init__()
        self._data = statsdata
        self.col_headers = col_headers

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

            bgcolor = QtGui.QBrush(QtCore.Qt.white)

            if(column == 0):
                bgcolor = QtGui.QBrush(QColor(240, 234, 193))
            else:

                if(column == 8) :
 
                    skew = self._data[index.row()][index.column()]

                    if ( (not (skew is None)) and (not(skew == " ")) ) : # && value !== "nan" && value !== " ") {

                        skew = float(self._data[index.row()][index.column()])

                        if ( (skew < -1.0) or (skew > 1.0) ) :
                            bgcolor     =   red_color
                        elif (skew < 66) :
                            bgcolor     =  yellow_color
                        else : 
                            bgcolor     =  green_color

                    else :
                        bgcolor = QtGui.QBrush(QtCore.Qt.white)


                elif(column == 9) : 

                    kurtosis = self._data[index.row()][index.column()]

                    if ( (not (kurtosis is None)) and (not(kurtosis == " ")) ) : # && value !== "nan" && value !== " ") {

                        kurtosis = float(self._data[index.row()][index.column()])

                        if ( (kurtosis < -2.0) or (kurtosis > 2.0) ) :
                            bgcolor     =  red_color
                        elif ( (kurtosis < -1.0) or (kurtosis > 1.0) ) :
                            bgcolor     =  yellow_color
                        else :
                            bgcolor     =  green_color
                    
                    else :
                        bgcolor = QtGui.QBrush(QtCore.Qt.white)

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

            if(section <= len(self.col_headers)) :
                return(self.col_headers[section])
            else :
                return("  ")
            
        return super().headerData(section, orientation, role)

# -----------------------------------------------------------------#
# -    Subclass of QMainWindow to disp[lay the columns uniques    -#
# -----------------------------------------------------------------#
class DataInspectionColumnsStatsTable(QtWidgets.QTableView):

    def __init__(self, dfparms, **kwargs):  

        super().__init__()

        self.mainLayout         =   None
        self.model              =   None
        self.df                 =   None

        self.dftitle            =   dfparms[0]
        self.max_num_rows       =   dfparms[1]
        self.select_callback    =   dfparms[2]

        self.colname            =   None

        from dfcleanser.common.cfg import df_Column_Changed_signal
        df_Column_Changed_signal.connectSignal(self.reload_data)

        if(DEBUG_DATA_INSPECT_COLUMNS) :
            print("    [DataInspectionColumnsStatsTable] : init : dftitle : ",self.dftitle,self.max_num_rows,self.colname)

        if(1):#self.df is None) :
            from dfcleanser.common.cfg import get_dfc_dataframe_df 
            df          =   get_dfc_dataframe_df(self.dftitle)
            self.df     =   df
        else :
            df  =   self.df

        if(self.select_callback is None) :
            self.doubleClicked.connect(self.select_column_to_inspect) 
        else :
            self.doubleClicked.connect(self.select_callback)

        self.init_tableview()

        if(DEBUG_DATA_INSPECT_COLUMNS_DETAILS) :
            print("    [DataInspectionColumnsStatsTable] : done")

    
    def reload_data(self) :

        if(DEBUG_DATA_INSPECT_COLUMNS_DETAILS) :
            print("    [DataInspectionColumnsStatsTable][reload_data] : dftitle : ",self.dftitle)

        reload_data     =   self.load_columns_stats_data()
        self.model.reload_data(reload_data)        


    # -----------------------------------------------------------------#
    # -                 Initialize the tableview                      -#
    # -----------------------------------------------------------------#
        
    def init_tableview(self):

        if(DEBUG_DATA_INSPECT_COLUMNS) :
            print("    [DataInspectionColumnsStatsTable] : init_tableview",self.dftitle)

        #-----------------------------------------#
        #   load data into the tableview model    #
        #-----------------------------------------#
        columnsdata     =   self.load_columns_stats_data()

        if(self.model is None) :
            self.model = DataInspectionColumnsStatsModel(columnsdata, self.column_headers)
            self.setModel(self.model)

        if(DEBUG_DATA_INSPECT_COLUMNS) :
           print("    [DataInspectionColumnsStatsTable] : model loaded")

        self.num_rows   =   len(columnsdata)

        if(self.max_num_rows is None) :
            num_rows_limit  =   25
        else :
            num_rows_limit  =   self.max_num_rows

        if(self.num_rows < num_rows_limit) :
            new_height  =   40 + (self.num_rows * DEFAULT_ROW_HEIGHT)
        else :
            new_height  =   40 + (num_rows_limit * DEFAULT_ROW_HEIGHT)

        self.setMinimumHeight(new_height)
        self.setMaximumHeight(new_height)

        if(DEBUG_DATA_INSPECT_COLUMNS_DETAILS) :
           print("    [DataInspectionColumnsStatsTable] : new_height",self.num_rows,new_height)


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
        nrows = len(columnsdata)
        for row in range(nrows):
            self.setRowHeight(row, DEFAULT_ROW_HEIGHT) 
        
        column_widths   =   [240,100,80,80,80,80,80,80,80,80]
        # set table view columns
        self.verticalHeader().setVisible(False)
        for i in range(len(column_widths)) :
           self.setColumnWidth(i, column_widths[i])     
        
        self.setWordWrap(True)


    # -----------------------------------------------------------------#
    # -                 Initialize the table data                     -#
    # -----------------------------------------------------------------#
    def load_columns_stats_data(self):

        if(DEBUG_DATA_INSPECT_COLUMNS) :
            print("    [DataInspectionColumnsStatsTable] : load_columns_stats_data ")

        df_cols         =   self.df.columns.tolist()

        from dfcleanser.Qt.data_inspection.DataInspectionModel import get_dfc_cols_data
        df_data_info =  get_dfc_cols_data(self.df)

        coldtypes   =   df_data_info[0]
        numuniques  =   df_data_info[1]
        numnans     =   df_data_info[2]
        means       =   df_data_info[3]
        stddev      =   df_data_info[4]
        minvals     =   df_data_info[5]
        maxvals     =   df_data_info[6]
        skews       =   df_data_info[7]
        kurtosiss   =   df_data_info[8]

        if(DEBUG_DATA_INSPECT_COLUMNS_DETAILS) :
            print("[df_data_info] : \n  df_cols\n    ",df_cols,"\n  coldtypes : \n    ",coldtypes,"\n  numuniques \n    ",numuniques)
            print("[df_data_info] : \n  numnans\n    ",numnans,"\n  means : \n    ",means,"\n  stddev \n    ",stddev)
            print("[df_data_info] : \n  minvals\n    ",minvals,"\n  maxvals : \n    ",maxvals,"\n  skews \n    ",skews, "\n  kurtosiss \n    ",kurtosiss)
        
        data            =   []

        for i in range(len(df_cols)) :

            data_row    =   []
            data_row.append(df_cols[i])
            data_row.append(str(coldtypes[i]))
            data_row.append(numuniques[i])
            data_row.append(str(numnans[i]))
            data_row.append(means[i])
            data_row.append(stddev[i])
            data_row.append(str(minvals[i]))
            data_row.append(str(maxvals[i]))
            data_row.append(skews[i])
            data_row.append(kurtosiss[i]) 

            data.append(data_row)

        if(DEBUG_DATA_INSPECT_COLUMNS_DETAILS) :
            print("    [DataInspectionColumnsStatsTable] : data\n ")
            for i in range(len(data)) :
                print("  [data row ",i,"] : ",data[i])

        self.column_headers     =   ["Column Name","Data Type","Uniques","Total Nans","Mean","Std Dev","Min","Max","Skew","Kurtosis"]

        self.num_rows           =   len(data)

        return(data)


    def select_column_to_inspect(self) :

        if(DEBUG_DATA_INSPECT_COLUMNS) :
            print("  [DataInspectionColumnsStatsTable][select_column_to_inspect]")
   
        row_number      =   None
        column_number   =   None


        if(0):#len(self.colsStats.selectionModel().selectedIndexes()) == 0) :

            self.statusBar().showMessage('No Column selected to inspect')

        else :

            for idx in self.selectionModel().selectedIndexes():
                row_number = int(idx.row())
                column_number = int(idx.column())

            if(DEBUG_DATA_INSPECT_COLUMNS_DETAILS) :
                print("  [DataInspectionColumnsStatsTable][select_column_to_inspect] ",row_number,column_number)

            model   =   self.model
            tdata   =   model.get_data()
            cell    =   tdata[row_number][0]

            from dfcleanser.common.cfg import get_dfc_dataframe_df 
            df          =   get_dfc_dataframe_df(self.dftitle)

            from dfcleanser.common.common_utils import is_numeric_col
            if(is_numeric_col(df,cell)) :

                self.colname =  cell
                #self.statusBar().showMessage(cell + ' Column selected to inspect')
            
                if(DEBUG_DATA_INSPECT_COLUMNS) :    
                    print("  [DataInspectionColumnsStatsTable][select_column_to_inspect] : self.columnname [",self.colname,"]")

            else :

                title       =   "dfcleanser error : [select_column_to_inspect]"        
                status_msg  =   "column selected is not numeric"
                from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                display_error_msg(title,status_msg)

            if(DEBUG_DATA_INSPECT_COLUMNS) :    
                print("  [DataInspectionColumnsStatsTable][select_column_to_inspect] : colname [",cell,"]")

    def get_column_to_inspect(self) :

        if(DEBUG_DATA_INSPECT_COLUMNS) :    
            print("  [DataInspectionColumnsStatsTable][get_column_to_inspect] : self.colname [",self.colname,"]")

        return(self.colname)



# -----------------------------------------------------------------#
# -                 Inspect Column Graphs Widget                  -#
# -----------------------------------------------------------------#

HISTOGRAM_GRAPH        =   0
ZSCORES_GRAPH          =   1
HEAT_MAP_GRAPH         =   2
BOXPLOT_GRAPH          =   3


class DataInspection_Column_Graphs_Widget(QtWidgets.QWidget):

    def __init__(self, dfparms):  


        super().__init__()

        self.parent             =   dfparms[0]
        self.dftitle            =   dfparms[1]   
        self.stats_table        =   dfparms[2]
        self.colname            =   self.stats_table.colname
        
        if(DEBUG_DATA_INSPECT_COLUMNS) :
            print("\n[DataInspection_Column_Graphs_Widget][init] dftitle : ",self.dftitle,self.colname)

        self.init_form()

        if(DEBUG_DATA_INSPECT_COLUMNS) :
            print("[DataInspection_Column_Graphs_Widget] end")

    def reload_data(self,parent,dftitle) :
        
        if(DEBUG_DATA_INSPECT_COLUMNS_DETAILS) :
            print("  [DataInspection_Column_Graphs_Widget][reload_data] ")

        self.parent         =   parent
        self.dftitle        =   dftitle


    def init_form(self):  

        if(DEBUG_DATA_INSPECT_COLUMNS_DETAILS) :
            print("  [DataInspection_Column_Graphs_Widget][init_form]")

        # display graphs bar
        from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLabel

        heatmap_label   =   QLabel()
        cfgdir  = cfg.DataframeCleanserCfgData.get_dfc_qt_dir_name()
        image_name = cfgdir + "\data_inspection\\HeatMap.jpg"
        from PyQt5.QtGui import QImage, QPixmap
        image   =   QImage(image_name)
        pixmap  =   QPixmap.fromImage(image)
        heatmap_label.setPixmap(pixmap)
        heatmap_label.resize(70, 70)

        heatmap_button        =   QPushButton()     
        heatmap_button.setText("HeatMap")
        heatmap_button.setFixedSize(90,30)
        heatmap_button.setToolTip("HeatMap")
        heatmap_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 12px; font-weight: bold; font-family: Tahoma; ")
        heatmap_button.clicked.connect(self.display_heatmap) 
        
        heatmapLayout   =   QVBoxLayout()
        heatmapLayout.addWidget(heatmap_label)
        heatmapLayout.addWidget(heatmap_button)
        heatmapLayout.addStretch()
        heatmapLayout.setAlignment(Qt.AlignCenter)

        boxplot_label   =   QLabel()
        cfgdir  = cfg.DataframeCleanserCfgData.get_dfc_qt_dir_name()
        image_name = cfgdir + "\data_inspection\\Boxplot.png"
        from PyQt5.QtGui import QImage, QPixmap
        image   =   QImage(image_name)
        pixmap  =   QPixmap.fromImage(image)
        boxplot_label.setPixmap(pixmap)
        boxplot_label.resize(70, 70)

        boxplot_button        =   QPushButton()     
        boxplot_button.setText("BoxPlot")
        boxplot_button.setFixedSize(90,30)
        boxplot_button.setToolTip("BoxPlot")
        boxplot_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 12px; font-weight: bold; font-family: Tahoma; ")
        boxplot_button.clicked.connect(self.display_boxplot)

        boxplotLayout   =   QVBoxLayout()
        boxplotLayout.addWidget(boxplot_label)
        boxplotLayout.addWidget(boxplot_button)
        boxplotLayout.addStretch()
        boxplotLayout.setAlignment(Qt.AlignCenter)

        histo_label   =   QLabel()
        cfgdir  = cfg.DataframeCleanserCfgData.get_dfc_qt_dir_name()
        image_name = cfgdir + "\data_inspection\Histogram.jpg"
        from PyQt5.QtGui import QImage, QPixmap
        image   =   QImage(image_name)
        pixmap  =   QPixmap.fromImage(image)
        histo_label.setPixmap(pixmap)
        histo_label.resize(70, 70)

        histo_button        =   QPushButton()     
        histo_button.setText("Histogram")
        histo_button.setFixedSize(90,30)
        histo_button.setToolTip("Histogram")
        histo_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 12px; font-weight: bold; font-family: Tahoma; ")
        histo_button.clicked.connect(self.display_histogram) 

        histoLayout   =   QVBoxLayout()
        histoLayout.addWidget(histo_label)
        histoLayout.addWidget(histo_button)
        histoLayout.addStretch()
        histoLayout.setAlignment(Qt.AlignCenter)

        zscore_label   =   QLabel()
        cfgdir  = cfg.DataframeCleanserCfgData.get_dfc_qt_dir_name()
        image_name = cfgdir + "\data_inspection\ZScores.png"
        from PyQt5.QtGui import QImage, QPixmap
        image   =   QImage(image_name)
        pixmap  =   QPixmap.fromImage(image)
        zscore_label.setPixmap(pixmap)
        zscore_label.resize(70, 70)

        zscore_button        =   QPushButton()     
        zscore_button.setText("ZScores")
        zscore_button.setFixedSize(90,30)
        zscore_button.setToolTip("ZScores")
        zscore_button.setStyleSheet("background-color:#0c4ca7; color:white; font-size: 12px; font-weight: bold; font-family: Tahoma; ")
        zscore_button.clicked.connect(self.display_zscores) 

        zscoreLayout   =   QVBoxLayout()
        zscoreLayout.addWidget(zscore_label)
        zscoreLayout.addWidget(zscore_button)
        zscoreLayout.addStretch()
        zscoreLayout.setAlignment(Qt.AlignCenter)

        from PyQt5.QtWidgets import QHBoxLayout
        self.cmd_buttonsLayout  =   QHBoxLayout()

        self.cmd_buttonsLayout.addLayout(heatmapLayout)
        self.cmd_buttonsLayout.addLayout(boxplotLayout)
        self.cmd_buttonsLayout.addLayout(histoLayout)
        self.cmd_buttonsLayout.addLayout(zscoreLayout)
        self.cmd_buttonsLayout.setAlignment(Qt.AlignCenter)
        
        self.setLayout(self.cmd_buttonsLayout)

    def set_column_name(self,colname) :

        if(DEBUG_DATA_INSPECT_COLUMNS) :
            print("  [DataInspection_Column_Graphs_Widget][set_column_name]",colname)

        self.colname    =   colname

    def display_heatmap(self) :

        self.colname    =   self.stats_table.colname

        if(DEBUG_DATA_INSPECT_COLUMNS) :
            print("  [DataInspection_Column_Graphs_Widget][display_heatmap] dftitle : ",self.dftitle,self.colname)

        parms   =   [HEAT_MAP_GRAPH,self.dftitle,self.colname]
        display_inspect_graph(parms)

    def display_boxplot(self) :

        self.colname    =   self.stats_table.colname

        if(DEBUG_DATA_INSPECT_COLUMNS) :
            print("  [DataInspection_Column_Graphs_Widget][display_boxplot]")

        parms   =   [BOXPLOT_GRAPH,self.dftitle,self.colname]
        display_inspect_graph(parms)

    def display_histogram(self) :

        self.colname    =   self.stats_table.colname
        
        self.colname            =   self.stats_table.get_column_to_inspect()    

        if(DEBUG_DATA_INSPECT_COLUMNS) :
            print("  [DataInspection_Column_Graphs_Widget][display_histogram]",self.dftitle,self.colname)
        
        parms   =   [HISTOGRAM_GRAPH,self.dftitle,self.colname]
        display_inspect_graph(parms)

    def display_zscores(self) :

        self.colname    =   self.stats_table.colname

        if(DEBUG_DATA_INSPECT_COLUMNS) :
            print("  [DataInspection_Column_Graphs_Widget][display_zscores]")
        
        parms   =   [ZSCORES_GRAPH,self.dftitle,self.colname]
        display_inspect_graph(parms)


def display_inspect_graph(parms) :

    graphid         =   parms[0]
    dftitle         =   parms[1]
    column_name     =   parms[2]

    if(DEBUG_DATA_INSPECT_COLUMNS) :
        print("  [display_inspect_graph]",graphid,dftitle,column_name)


    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df          =   get_dfc_dataframe_df(dftitle)

    if(df is None) :
                                    
        title       =   "dfcleanser error"       
        status_msg  =   "Invalid dfc dataframe defined"
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        return(None)
        
    else :

        if(column_name is None) :

            title       =   "dfcleanser error"       
            status_msg  =   "No column slected to graph"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

            return(None)
            
        else :

            from dfcleanser.common.common_utils import is_numeric_col
            if(not is_numeric_col(df,column_name)) :

                title       =   "dfcleanser error"       
                status_msg  =   "column selected to graph is not numeric"
                from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                display_error_msg(title,status_msg)

                return(None)
                
            else :

                from dfcleanser.common.common_utils import run_jscript
                #jscript     =   "display_column_graph(" + str(graphid) + ",'" + str(dftitle) + "','" + str(column_name) + "');"
                jscript     =   "display_column_graph(" + str(graphid) + ",'" + str(dftitle) + "','" + str(column_name) + "');"

                if(DEBUG_DATA_INSPECT_COLUMNS) :
                    print("  [DataInspection_Column_Graphs_Widget][display_inspect_graph][jscript]",jscript)

                run_jscript(jscript,"fail to display graph : ")


"""
def display_heat_map_graph(dftitle,colname) :

    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df
    df  =   get_dfc_dataframe_df(dftitle)

    col_uniques     =   df[colname].unique().tolist()
    col_counts      =   df[colname].value_counts().tolist()

    graph_uniques   =   []
    graph_counts    =   []
    for i in range(len(col_uniques)) :
        if(not(pd.isnull(col_uniques[i]))) :
            graph_uniques.append(col_uniques[i])
            graph_counts.append(df[colname].value_counts()[col_uniques[i]])

    graphdf = pd.DataFrame({colname: graph_uniques},index=graph_counts)

    sns.heatmap(graphdf, annot=True, fmt="g", cmap='viridis')

    plt.show()  


def display_box_plot_graph(dftitle,colname) :

    # Import libraries
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df
    df  =   get_dfc_dataframe_df(dftitle)
 

    # Creating dataset
    np.random.seed(10)
 
    data_1 = np.random.normal(100, 10, 200)
    data_2 = np.random.normal(90, 20, 200)
    data_3 = np.random.normal(80, 30, 200)
    data_4 = np.random.normal(70, 40, 200)
    data = [data_1, data_2, data_3, data_4]


    fig = plt.figure(figsize =(10, 7))
    sns.boxplot(data=df,x=colname)

    # Creating axes instance
    #ax = fig.add_axes([0, 0, 1, 1])
 
    # Creating plot
    #bp = ax.boxplot(data)
 
    # show plot
    plt.show()    


def display_histogram_graph(dftitle,colname) :

    from dfcleanser.common.cfg import get_dfc_dataframe_df
    df  =   get_dfc_dataframe_df(dftitle)

    import numpy as np
    counts      =   df[colname].value_counts().to_dict()
    dfuniques   =   list(counts.keys())
    uniques     =   np.asarray(dfuniques)
    ucounts     =   list(counts.values())
    ucounts     =   np.asarray(ucounts)

    import matplotlib.pyplot as plt
        
    fig     =   plt.figure()
    plt.style.use('ggplot')
    plt.hist(uniques,weights=ucounts)
    plt.title("'" + colname + "'" + " Histogram")

    plt.show()



def calculate_column_zscores(df,colname) :
    
    import numpy as np

    counts      =   df[colname].value_counts().to_dict()
    dfuniques   =   list(counts.keys())
    uniques     =   np.asarray(dfuniques)
    ucounts     =   list(counts.values())
    ucounts     =   np.asarray(ucounts)

    cmean       =   df[colname].mean() 
    cstd        =   df[colname].std()

    zscores      =   []
    for i in range(len(dfuniques)) :
        zscores.append((dfuniques[i]-cmean)/cstd)
        
    # dictionary of lists  
    zdict = {'ZScore': zscores, 'Frequency': ucounts}  

    return(zdict)



def display_zscores_graph(dftitle,colname):

    from dfcleanser.common.cfg import get_dfc_dataframe_df
    df  =   get_dfc_dataframe_df(dftitle)

    zdict   =   calculate_column_zscores(df,colname)
    
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    zdf     =   pd.DataFrame(zdict)     
    ax = zdf.plot(x='ZScore', y='Frequency', kind='kde', figsize=(10, 6))
    fig1    =   ax.get_figure()
    arr = ax.get_children()[0]._x
    plt.xticks(np.linspace(arr[0], arr[-1]), rotation=90)
    plt.title("'" + colname + "'" + " ZScores")

    plt.show()

"""

