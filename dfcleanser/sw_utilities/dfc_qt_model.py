"""
# dfc_qt_model 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""

from PyQt5 import QtWidgets, sip
from PyQt5.QtCore import Qt

DEBUG_COMMON                    =   True
DEBUG_INPUT_FORMS               =   True
DEBUG_INPUT_FORMS_DETAILS       =   False
DEBUG_COMMON_EXCEPT             =   False

def fix_ipython():
    from IPython import get_ipython
    ipython = get_ipython()
    if ipython is not None:
        ipython.magic("gui qt5")


def fix_QtWebEngineWidgets():

    # Since graphsgui might be imported after other packages already created a QApplication,
    # we need to hack around this import restriction on QtWebEngineWidgets
    # https://stackoverflow.com/a/57436077/3620725

    if "PyQt5.QtWebEngineWidgets" not in sys.modules:
        app = QtWidgets.QApplication.instance()

        if app is None:
            from PyQt5 import QtWebEngineWidgets
        else:
            logger.warning("Reinitializing existing QApplication to allow import of QtWebEngineWidgets. "
                            "This may cause problems. "
                            "To avoid this, import graphsgui or PyQt5.QtWebEngineWidgets before a QApplication is created.")
            app.quit()
            sip.delete(app)
            from PyQt5 import QtWebEngineWidgets

            app.__init__(sys.argv + ["--ignore-gpu-blacklist", "--enable-gpu-rasterization"])

import sys
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

# Set the exception hook to our wrapping function
sys.excepthook = except_hook


"""
* --------------------------------------------------------
* --------------------------------------------------------
*  Generic dfcleanser chapter button bar 
* --------------------------------------------------------
* --------------------------------------------------------
"""

def init_dfc_buttons(buttons,button_style) :
        
    for i in range(len(buttons)) :

        buttons[i].setCheckable(True)
        buttons[i].setChecked(False)
        buttons[i].setEnabled(True)

        # set button attributes
        buttons[i].setStyleSheet(button_style)                                        

def set_dfc_buttons_style(buttons,style) :
        
    for i in range(len(buttons)) :
        buttons[i].setStyleSheet(style) 

"""
* --------------------------------------------------------
* --------------------------------------------------------
*  Generic dfcleanser chapter button bar end
* --------------------------------------------------------
* --------------------------------------------------------
"""


"""
* --------------------------------------------------------
* --------------------------------------------------------
*  Generic dfcleanser splash screen 
* --------------------------------------------------------
* --------------------------------------------------------
"""

def build_chapter_splash_screen(chapterid, splashid):
    """
    * ----------------------------------------------------
    * 
    * parms :
    *   chapterid  -   dfc chapter id
    *   splashid   -   form splash id
    *
    * returns : 
    *  N/A
    * ---------------------------------------------------
    """

    from dfcleanser.common.cfg import SWCensusUtility_ID, DataframeCleanserCfgData, DataCleansing_ID, DataExport_ID, DataImport_ID, DataInspection_ID, DataTransform_ID, System_ID, SWZipcodeUtility_ID, SWGeocodeUtility_ID, dfBrowserUtility_ID

    dfcdir          =   DataframeCleanserCfgData.get_dfc_cfg_dir_name()  

    if(chapterid == DataCleansing_ID)       : splash_file     =   "DataCleansingSplash.png"
    elif(chapterid == DataImport_ID)        : splash_file     =   "DataImportSplash.png"
    elif(chapterid == DataExport_ID)        : splash_file     =   "DataExportSplash.png"
    elif(chapterid == DataInspection_ID)    : splash_file     =   "DataInspectionSplash.png"
    elif(chapterid == DataTransform_ID)     : splash_file     =   "DataTransformSplash.png"
    elif(chapterid == System_ID)            : splash_file     =   "SystemSplash.png"
    elif(chapterid == SWZipcodeUtility_ID)  : splash_file     =   "ZipCodeSplash.png"
    elif(chapterid == SWGeocodeUtility_ID)  : splash_file     =   "GeocodeSplash.png"
    elif(chapterid == dfBrowserUtility_ID)  : splash_file     =   "dfBrowserSplash.png"
    elif(chapterid == SWCensusUtility_ID)   : splash_file     =   "CensusSplash.png"

    splash_name     =   dfcdir +"\splash\\" + splash_file

    from PyQt5.QtGui import QImage, QPixmap
    image   =   QImage(splash_name)
    pixmap  =   QPixmap.fromImage(image)
        
    splashid.setPixmap(pixmap)
    splashid.resize(pixmap.width(), pixmap.height())

    splashid.show()

"""
* --------------------------------------------------------
* --------------------------------------------------------
*  Generic dfcleanser splash screen end
* --------------------------------------------------------
* --------------------------------------------------------
"""

NUMERIC_COLUMN          =   0
NON_NUMERIC_COLUMN      =   1
CATEGORICAL_COLUMN      =   2

def get_columns_info(dftitle,colname) :

    from dfcleanser.common.cfg import get_dfc_dataframe_df
    df  =   get_dfc_dataframe_df(dftitle)

    col_values  =   []
    col_type    =   -1

    col_values.append(colname)

    coldtype = df.dtypes[colname]

    from dfcleanser.common.common_utils import (is_datetime_col, is_date_col, is_time_col, is_categorical_col, is_int_col, 
                                                is_timedelta_col, is_Timestamp_col, is_Timedelta_col, is_numeric_col)    
    if(coldtype == object) :
        
        if(is_datetime_col(df,colname))     :   coldtype     =   "datetime.datetime"    
        elif(is_date_col(df,colname))       :   coldtype     =   "datetime.date" 
        elif(is_time_col(df,colname))       :   coldtype     =   "datetime.time" 
        elif(is_timedelta_col(df,colname))  :   coldtype     =   "datetime.timedelta" 
        elif(is_Timestamp_col(df,colname))  :   coldtype     =   "Timestamp" 
        elif(is_Timedelta_col(df,colname))  :   coldtype     =   "Timedelta" 
        else :                                  coldtype    =   str(coldtype)

    else :

        coldtype    =   str(coldtype)
    
    col_values.append(coldtype)

    import pandas as pd
        
    total_nans      =   df[colname].isnull().sum()
    non_nan_count   =   len(df) - total_nans
    
    if(total_nans > 0) :
        pct     =   float((100*(total_nans/len(df))))
    else :
        pct     =   0

    col_values.append(total_nans)
    col_values.append(non_nan_count)
    col_values.append(pct)

    if(is_categorical_col(df,colname)) :
        
        CI              =   pd.CategoricalIndex(df[colname])
        cats            =   CI.categories.tolist()
        cats_count      =   len(cats)
        cats_ordered    =   CI.ordered

        col_values.append(cats_count)
        col_values.append(cats_ordered)

        col_type    =  CATEGORICAL_COLUMN 
        
    else :
        
        try :
            uniques     =   df[colname].unique()
        except :
            try :
                uniques     =   list(map(list, set(map(lambda i: tuple(i), df[colname])))) 
            except :
                uniques     =   []
            
        uniques_count   =   len(uniques)
        col_values.append(uniques_count)
        
        if(is_numeric_col(df,colname)) :
            
            mean        =   df[colname].mean()
            std         =   df[colname].std()
            min         =   df[colname].min()
            max         =   df[colname].max()
            skew        =   df[colname].skew()
            kurtosis    =   df[colname].kurtosis()

            col_values.append(mean)
            col_values.append(std)
            col_values.append(min)
            col_values.append(max)
            col_values.append(skew)
            col_values.append(kurtosis)

            col_type    =  NUMERIC_COLUMN

        else :

           col_type    =  NON_NUMERIC_COLUMN 

    return([col_type,col_values])



"""
* --------------------------------------------------------
* --------------------------------------------------------
*  Generic dfcleanser current dfs imported end
* --------------------------------------------------------
* --------------------------------------------------------
"""

DFS_LABEL_GEOMETRY      =   [10,10,200,50]
DFS_LABEL_STYLE         =   "font-size: 12px; font-weight: bold; font-family: Arial; margin-left: 0px;"
DFS_LABEL_TEXT          =   "* dataframes_to_inspect"

DFS_COMBO_GEOMETRY      =   [10,32,950,30]
DFS_COMBO_STYLE         =   "font-size: 12px; font-weight: normal; font-family: Arial; margin-left: 0px;"

def build_select_dfs_layout(labeltext):
    """
    * -------------------------------------------------------- 
    * function : build the select df combobox
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    from PyQt5.QtWidgets import QLabel
    dflabel      =   QLabel()
    dflabel.setText(labeltext)
    dflabel.setStyleSheet(DFS_LABEL_STYLE)
    dflabel.setFixedSize(DFS_LABEL_GEOMETRY[2],DFS_LABEL_GEOMETRY[3])  
    dflabel.move(DFS_LABEL_GEOMETRY[0],DFS_LABEL_GEOMETRY[1])
        
    from PyQt5.QtWidgets import QComboBox
    dfcomboBox   =   QComboBox()
    dfcomboBox.setStyleSheet(DFS_COMBO_STYLE)

    from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
    dataframes     =   get_dfc_dataframes_titles_list()

    if(dataframes  is None) :
        dataframes      =   []
        dataframes.append("no dfs defined")

    for i in range(len(dataframes)) :
        dfcomboBox.addItem(dataframes[i])

    from PyQt5.QtWidgets import QVBoxLayout

    dfsSelectLayout     =   QVBoxLayout()
    dfsSelectLayout.addWidget(dflabel)
    dfsSelectLayout.addWidget(dfcomboBox)
    dfsSelectLayout.addStretch()

    return([dfcomboBox,dfsSelectLayout])


def build_select_dfs_layout1(labeltext):
    """
    * -------------------------------------------------------- 
    * function : build the select df combobox
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    from PyQt5.QtWidgets import QLabel
    dflabel      =   QLabel()
    dflabel.setText(labeltext)
    dflabel.setStyleSheet(DFS_LABEL_STYLE)
    dflabel.setFixedSize(DFS_LABEL_GEOMETRY[2],DFS_LABEL_GEOMETRY[3])  
    dflabel.move(DFS_LABEL_GEOMETRY[0],DFS_LABEL_GEOMETRY[1])
        
    from PyQt5.QtWidgets import QComboBox
    dfcomboBox   =   QComboBox()
    dfcomboBox.setStyleSheet(DFS_COMBO_STYLE)

    from dfcleanser.common.cfg import get_dfc_dataframes_titles_list
    dataframes     =   get_dfc_dataframes_titles_list()

    if(dataframes  is None) :
        dataframes      =   []
        dataframes.append("no dfs defined")

    for i in range(len(dataframes)) :
        dfcomboBox.addItem(dataframes[i])

    return([dflabel,dfcomboBox])






"""
* --------------------------------------------------------
* --------------------------------------------------------
*  Generic dfcleanser current dfs imported end
* --------------------------------------------------------
* --------------------------------------------------------
"""

"""
* --------------------------------------------------------
* --------------------------------------------------------
*  Gneric dfcleanser imput form widget
* --------------------------------------------------------
* --------------------------------------------------------
"""


QT_INPUT_FORM_TITLE_HEIGHT                  =   40
QT_INPUT_FORM_TITLE_STYLE                   =   "font-size: 16px; font-weight: bold; font-family: Arial;" 

QT_INPUT_FORM_ENTRY_TITLE_HEIGHT            =   30
QT_INPUT_FORM_ENTRY_TITLE_STYLE             =   "font-size: 13px; font-weight: bold; font-family: Arial;" 

QT_INPUT_FORM_ENTRY_VALUE_HEIGHT            =   30
QT_INPUT_FORM_ENTRY_VALUE_STYLE             =   "font-size: 13px; font-weight: normal; font-family: Arial; color: black;" 

QT_INPUT_FORM_ENTRY_BUTTON_STYLE            =   "background-color:#0c4ca7; color:white; font-size: 14px; font-weight: bold; font-family: Tahoma; "

QT_SMALL_INPUT_FORM_TITLE_HEIGHT            =   30
QT_SMALL_INPUT_FORM_TITLE_STYLE             =   "font-size: 16px; font-weight: bold; font-family: Arial;" 

QT_SMALL_INPUT_FORM_ENTRY_TITLE_HEIGHT      =   20
QT_SMALL_INPUT_FORM_ENTRY_TITLE_STYLE       =   "font-size: 11px; font-weight: bold; font-family: Arial;" 

QT_SMALL_INPUT_FORM_ENTRY_VALUE_HEIGHT      =   20
QT_SMALL_INPUT_FORM_ENTRY_VALUE_STYLE       =   "font-size: 11px; font-weight: normal; font-family: Arial;" 

QT_SMALL_INPUT_FORM_ENTRY_BUTTON_STYLE      =   "background-color:#0c4ca7; color:white; font-size: 12px; font-weight: bold; font-family: Tahoma; "

QT_LARGE_TEXTEDIT_ENTRY_VALUE_STYLE         =   "font-size: 16px; font-weight: normal; font-family: Arial;" 


NORMAL          =   0
SMALL           =   1
LARGE_TEXTEDIT  =   2

class dfcleanser_input_form_Widget(QtWidgets.QWidget) :
    """
    * --------------------------------------------------------
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """


    def __init__(self,  formparms, size=NORMAL, **kwargs):  

        super().__init__()
        
        if(DEBUG_INPUT_FORMS_DETAILS) :
            print("  [dfcleanser_input_formWidget] : start : len(formparms) : ",len(formparms))
            for i in range(len(formparms)) :
                print(    "formparms[",i,"] : ",formparms[i])

        self.form_ID                 =   formparms[0]
        self.formIds_List            =   formparms[1] 
        self.formLabels_List         =   formparms[2] 
        self.formTypes_List          =   formparms[3] 
        self.formInitVals_List       =   formparms[4] 
        self.formRequired_List       =   formparms[5] 

        self.comboLists              =   formparms[6]
        self.combomethods            =   formparms[7]
        self.fileselectmethods       =   formparms[8]
        self.buttonmethods           =   formparms[9]
        self.cfgParms                =   formparms[10]
        self.form_title              =   formparms[11]
        self.form_width              =   formparms[12]

        if(size == NORMAL) :

            self.FORM_TITLE_HEIGHT           =   QT_INPUT_FORM_TITLE_HEIGHT
            self.FORM_TITLE_STYLE            =   QT_INPUT_FORM_TITLE_STYLE 
            self.FORM_ENTRY_TITLE_HEIGHT     =   QT_INPUT_FORM_ENTRY_TITLE_HEIGHT
            self.FORM_ENTRY_TITLE_STYLE      =   QT_INPUT_FORM_ENTRY_TITLE_STYLE   
            self.FORM_ENTRY_VALUE_HEIGHT     =   QT_INPUT_FORM_ENTRY_VALUE_HEIGHT
            self.FORM_ENTRY_VALUE_STYLE      =   QT_INPUT_FORM_ENTRY_VALUE_STYLE
            self.FORM_ENTRY_BUTTON_STYLE     =   QT_INPUT_FORM_ENTRY_BUTTON_STYLE 
            self.FORM_ENTRY_TEXTEDIT_STYLE   =   QT_INPUT_FORM_ENTRY_VALUE_STYLE
        
        elif(size == LARGE_TEXTEDIT) :

            self.FORM_TITLE_HEIGHT           =   QT_INPUT_FORM_TITLE_HEIGHT
            self.FORM_TITLE_STYLE            =   QT_INPUT_FORM_TITLE_STYLE 
            self.FORM_ENTRY_TITLE_HEIGHT     =   QT_INPUT_FORM_ENTRY_TITLE_HEIGHT
            self.FORM_ENTRY_TITLE_STYLE      =   QT_INPUT_FORM_ENTRY_TITLE_STYLE   
            self.FORM_ENTRY_VALUE_HEIGHT     =   QT_INPUT_FORM_ENTRY_VALUE_HEIGHT
            self.FORM_ENTRY_VALUE_STYLE      =   QT_INPUT_FORM_ENTRY_VALUE_STYLE
            self.FORM_ENTRY_BUTTON_STYLE     =   QT_INPUT_FORM_ENTRY_BUTTON_STYLE 
            self.FORM_ENTRY_TEXTEDIT_STYLE   =   QT_LARGE_TEXTEDIT_ENTRY_VALUE_STYLE

        else :

            if(DEBUG_INPUT_FORMS_DETAILS) :
                print("  [dfcleanser_input_formWidget] using small sttles")

            self.FORM_TITLE_HEIGHT           =   QT_SMALL_INPUT_FORM_TITLE_HEIGHT
            self.FORM_TITLE_STYLE            =   QT_SMALL_INPUT_FORM_TITLE_STYLE 
            self.FORM_ENTRY_TITLE_HEIGHT     =   QT_SMALL_INPUT_FORM_ENTRY_TITLE_HEIGHT
            self.FORM_ENTRY_TITLE_STYLE      =   QT_SMALL_INPUT_FORM_ENTRY_TITLE_STYLE   
            self.FORM_ENTRY_VALUE_HEIGHT     =   QT_SMALL_INPUT_FORM_ENTRY_VALUE_HEIGHT
            self.FORM_ENTRY_VALUE_STYLE      =   QT_SMALL_INPUT_FORM_ENTRY_VALUE_STYLE
            self.FORM_ENTRY_BUTTON_STYLE     =   QT_SMALL_INPUT_FORM_ENTRY_BUTTON_STYLE 
            self.FORM_ENTRY_TEXTEDIT_STYLE   =   QT_INPUT_FORM_ENTRY_VALUE_STYLE

        self.input_fields_list       =   []

        if(DEBUG_INPUT_FORMS) :
            print("  [dfcleanser_input_formWidget] : start : end ")

        self.init_form()

        from dfcleanser.common.cfg import get_config_value
        form_cfg_parms  =   get_config_value(self.form_ID+"Parms")

        if(not (form_cfg_parms is None)) :
            self.load_form_values(form_cfg_parms)
        else :
            self.load_form_values(self.cfgParms)

        #if(not (self.cfgParms is None)) :
        #    self.load_form_values(self.cfgParms)


        if(DEBUG_INPUT_FORMS_DETAILS) :
            print("  [dfcleanser_input_formWidget] : end\n")

    def init_form(self) :

        if(DEBUG_INPUT_FORMS) :
            print("  [dfcleanser_input_formWidget][init_form]")

        from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QTextEdit
        from PyQt5.QtWidgets import QLabel, QLineEdit, QComboBox, QPushButton
        from PyQt5.QtCore import Qt

        max_new_button_lines    =   0

        from dfcleanser.common.common_utils import opStatus
        opstat  =   opStatus()

        try :

            self.num_form_buttons  =   0

            for i in range(len(self.formTypes_List)) :
                    
                if(self.formTypes_List[i] == "button") :

                    self.num_form_buttons   =   self.num_form_buttons + 1

                    button_text     =   self.formLabels_List[i]
                    import re
                    num_lines   =   len(re.findall('(?=(</br>))', button_text))
                    if(num_lines > max_new_button_lines) :
                        max_new_button_lines = num_lines

            if(self.num_form_buttons > 0) :
                self.form_button_height     =   (max_new_button_lines + 1) * 30
                self.form_button_width      =   int(self.form_width / self.num_form_buttons)
                if(self.form_button_width > 200) :
                    self.form_button_width  =   200


            self.formInputsLayout        =   QVBoxLayout()
            self.formButtonsLayout       =   QHBoxLayout()

            self.current_button_count    =   0
            self.current_select_count    =   0
            self.file_browse_count       =   0

            # set the form title
            self.input_form_title    =   QLabel()
            self.input_form_title.setText(self.form_title)
            self.input_form_title.setAlignment(Qt.AlignCenter)
            self.input_form_title.resize(QT_INPUT_FORM_TITLE_HEIGHT ,self.form_width)
            self.input_form_title.setStyleSheet(self.FORM_TITLE_STYLE)
            self.formInputsLayout.addWidget(self.input_form_title)

            if(DEBUG_INPUT_FORMS_DETAILS) :
                print("  [dfcleanser_input_formWidget][init_form] : len(self.formIds_List) : ",len(self.formIds_List))
                
            for i in range(len(self.formIds_List)) :

                if(DEBUG_INPUT_FORMS_DETAILS) :
                    print("  [dfcleanser_input_formWidget][init_form] : form inputs [",i,"] : ",self.formTypes_List[i])
                        
                if( not (self.formTypes_List[i] == "button") ) :

                    # insert the form entry label
                    input_entry_label    =   QLabel()

                    if(i in self.formRequired_List) :
                        input_entry_label.setText("*"+str(self.formLabels_List[i]))
                    else :
                        input_entry_label.setText(str(self.formLabels_List[i]))

                    input_entry_label.setAlignment(Qt.AlignLeft)
                    input_entry_label.resize(QT_INPUT_FORM_ENTRY_TITLE_HEIGHT,self.form_width)
                    input_entry_label.setStyleSheet(self.FORM_ENTRY_TITLE_STYLE)
                    self.formInputsLayout.addWidget(input_entry_label)

                # insert the form imput widget
                if(type(self.formTypes_List[i]) == list) :

                    compound_input   =  self.formTypes_List[i]

                    if(compound_input[0] == "textarea") :
                        ctype       =   "textarea"
                        numrows     =   int(compound_input[1])
                        scroll      =   compound_input[2]

                    elif(compound_input[0] == "filearea") :
                        ctype       =   "textarea"
                        numrows     =   int(compound_input[1])
                        
                    input_entry_value    =   QTextEdit()
                    qte_height  =  (QT_INPUT_FORM_ENTRY_TITLE_HEIGHT * numrows)
                    input_entry_value.setMinimumHeight(qte_height)
                    input_entry_value.setMaximumHeight(qte_height)

                    #input_entry_value.setMaximumWidth(self.form_width)

                    input_entry_value.setStyleSheet(self.FORM_ENTRY_TEXTEDIT_STYLE)
                    self.input_fields_list.append(input_entry_value)
                    self.formInputsLayout.addWidget(input_entry_value)

                else :

                    if(self.formTypes_List[i] == "qtlist") :
                        
                        from PyQt5.QtWidgets import  QListWidget, QListWidgetItem, QAbstractItemView
                        input_entry_value     =   QListWidget()
                        input_entry_value.setStyleSheet(self.FORM_ENTRY_VALUE_STYLE)
                        input_entry_value.setMaximumHeight(200)
                        self.input_fields_list.append(input_entry_value)
                        self.formInputsLayout.addWidget(input_entry_value)

                    elif(self.formTypes_List[i] == "text") :
                        
                        input_entry_value    =   QLineEdit()
                        input_entry_value.setStyleSheet(self.FORM_ENTRY_VALUE_STYLE)
                        self.input_fields_list.append(input_entry_value)
                        self.formInputsLayout.addWidget(input_entry_value)
                
                    elif(self.formTypes_List[i] == "select") :
                        input_entry_value       =   QComboBox()

                        current_select          =   self.comboLists[self.current_select_count] 
                        default                 =   current_select.get("default")
                        sel_list                =   current_select.get("list")

                        current_index   =   0
                        for j in range(len(sel_list)) :

                            input_entry_value.addItem(sel_list[j])
                            if(sel_list[j] == default) :
                                current_index   =   j

                        input_entry_value.setCurrentIndex(current_index)
                        input_entry_value.setStyleSheet(self.FORM_ENTRY_VALUE_STYLE)

                        if(not (self.combomethods[self.current_select_count] is None) ) :

                            if(DEBUG_INPUT_FORMS_DETAILS) :
                                print("  [dfcleanser_input_formWidget] : combomethod[",self.current_select_count,"] : \n      ",self.combomethods[self.current_select_count])

                            input_entry_value.currentIndexChanged.connect(self.combomethods[self.current_select_count])

                        self.current_select_count    =   self.current_select_count + 1
                        self.input_fields_list.append(input_entry_value)
                        self.formInputsLayout.addWidget(input_entry_value)

                    elif(self.formTypes_List[i] == "file") :

                        input_entry_value    =   QLineEdit() 
                        input_entry_value.setAlignment(Qt.AlignLeft)
                        input_entry_value.resize(self.form_width,self.FORM_ENTRY_VALUE_HEIGHT)
                        input_entry_value.setStyleSheet(self.FORM_ENTRY_VALUE_STYLE)
                        self.input_fields_list.append(input_entry_value)
                        self.formInputsLayout.addWidget(input_entry_value)
                        
                        if(DEBUG_INPUT_FORMS_DETAILS) :
                            print("  [dfcleanser_input_formWidget] : file LineEdit ",self.file_browse_count)

                        file_select_button         =   QPushButton()     
                        file_select_button.setText("Browse To File")
                        file_select_button.setFixedSize(160,self.FORM_ENTRY_VALUE_HEIGHT)
                        file_select_button.setStyleSheet(self.FORM_ENTRY_BUTTON_STYLE)
                        file_select_button.clicked.connect(self.fileselectmethods[self.file_browse_count]) 
                        self.file_browse_count    =  self.file_browse_count + 1
                        self.formInputsLayout.addWidget(file_select_button)

                        if(DEBUG_INPUT_FORMS_DETAILS) :
                            print("  [dfcleanser_input_formWidget] : file done ",self.file_browse_count)

                    elif(self.formTypes_List[i] == "button") :

                        input_entry_button    =   QPushButton() 
           
                        button_text     =   self.formLabels_List[i]
                        button_text     =   button_text.replace("</br>","\n")

                        input_entry_button.setText(button_text)
                        input_entry_button.setFixedSize(self.form_button_width,self.form_button_height)
                        input_entry_button.setStyleSheet(self.FORM_ENTRY_BUTTON_STYLE)
                        input_entry_button.clicked.connect(self.buttonmethods[self.current_button_count]) 
                        self.current_button_count    =  self.current_button_count + 1
                        self.formButtonsLayout.addWidget(input_entry_button)

                        if(DEBUG_INPUT_FORMS_DETAILS) :
                            print("  [dfcleanser_input_formWidget] : button ",len(button_text),button_text)


        except Exception as e:
            
            title       =   "dfcleanser exception"
            status_msg  =   "[dfcleanser_input_form_Widget][init_form][error] \n [form_type] : " + self.formTypes_List[i] + " : " + str(i)
            display_exception(title,status_msg,e)
                        
            if(DEBUG_INPUT_FORMS_DETAILS) :
                print("  [dfcleanser_input_formWidget] : exception thrown ")


        self.formButtonsLayout.setAlignment(Qt.AlignHCenter)
        self.formInputsLayout.addLayout(self.formButtonsLayout) 
        self.formInputsLayout.addStretch() 

        self.setLayout(self.formInputsLayout)
        
        if(DEBUG_INPUT_FORMS_DETAILS) :
            print("  [dfcleanser_input_formWidget][init_form] end\n")

    """
    * -------------------------------------------------------- 
    *  get values from the input form methods
    * --------------------------------------------------------
    """
    def load_form_values(self, formvals) :
        
        if(DEBUG_INPUT_FORMS) :
            print("\n\n  [dfcleanser_input_formWidget][load_form_values] : form_vals : \n  ",formvals)

        if( (not (formvals is None)) and (len(formvals) > 0) ) :

            if(DEBUG_INPUT_FORMS) :
                print("  [dfcleanser_input_formWidget][load_form_values] : self.input_fields_list :  count : ",len(self.input_fields_list))
                print("  [dfcleanser_input_formWidget][load_form_values] len(self.input_fields_list) ",len(self.input_fields_list)," len(formvals) ",len(formvals))
 
            if(len(self.input_fields_list) == len(formvals)) :

                for i in range(len(formvals)) :

                    if(DEBUG_INPUT_FORMS_DETAILS) :
                        print("    [dfcleanser_input_formWidget][load_form_values] formval[",i,"] : ",formvals[i])

                    self.set_form_input_value_by_index(i, str(formvals[i]))

        if(DEBUG_INPUT_FORMS) :
            print("  [dfcleanser_input_formWidget][load_form_values] : end \n")

    def get_form_fields_count(self) :

        if(DEBUG_INPUT_FORMS_DETAILS) :
            print("[dfcleanser_input_formWidget][get_form_field_counts] ")

        return(len(self.input_fields_list))
        

    """
    * -------------------------------------------------------- 
    *  get values from the input form methods
    * --------------------------------------------------------
    """
    def get_form_input_value(self, inputId) :

        if(DEBUG_INPUT_FORMS_DETAILS) :
            print("  [dfcleanser_input_formWidget] : get_form_input_value",inputId)

        input_index    =   -1

        for i in range (len(self.formIds_List)) :
            if(inputId == self.formIds_List[i]) :
                input_index     =   i
                break

        if(input_index > 0) :
            form_value  =   self.get_form_value(input_index)
            return(form_value)
        else:
            return(None)

    def get_form_input_value_by_index(self, input_index) :

        if(DEBUG_INPUT_FORMS_DETAILS) :
            print("  [dfcleanser_input_formWidget] : get_form_input_value_by_index",input_index)

        if( (input_index > -1) and (input_index < len(self.formIds_List)) ) :
            form_value  =   self.get_form_value(input_index)
            return(form_value)
        else :
            return(None)        

    def get_form_value(self, input_index) :

        if(DEBUG_INPUT_FORMS_DETAILS) :
            print("  [dfcleanser_input_formWidget] : get_form_value",input_index)
            print("  [dfcleanser_input_formWidget] : self.formTypes_List",self.formTypes_List)
            print("  [dfcleanser_input_formWidget] : self.input_fields_list",self.input_fields_list)

        if(type(self.formTypes_List[input_index]) == list) :
            value = self.input_fields_list[input_index].toPlainText()      
        elif(self.formTypes_List[input_index] == "text") :
            value = self.input_fields_list[input_index].text()
        elif(self.formTypes_List[input_index] == "file") :
            value = self.input_fields_list[input_index].text()
        elif(self.formTypes_List[input_index] == "select") :
            value = self.input_fields_list[input_index].currentText()
        else :
            value = None
        
        if(DEBUG_INPUT_FORMS_DETAILS) :
            print("  [dfcleanser_input_formWidget] : get_form_value",input_index,value)

        return(value)

    """
    * -------------------------------------------------------- 
    *  set values to the input form methods
    * --------------------------------------------------------
    """
    def set_form_input_value(self, inputId, value) :

        if(DEBUG_INPUT_FORMS_DETAILS) :
            print("    [dfcleanser_input_formWidget] : set_form_input_value",inputId,value)

        input_index    =   -1

        for i in range (len(self.formIds_List)) :
            if(inputId == self.formIds_List[i]) :
                input_index     =   i
                break

        if(input_index > 0) :
            self.set_form_value(input_index,value)

    def set_form_input_value_by_index(self, input_index, value) :

        if(DEBUG_INPUT_FORMS_DETAILS) :
            print("    [dfcleanser_input_formWidget][set_form_input_value_by_index]",input_index,value)

        if( (input_index > -1) and (input_index < len(self.formIds_List)) ) :
            self.set_form_value(input_index,value)

    def set_form_value(self, input_index, value) :

        if(DEBUG_INPUT_FORMS_DETAILS) :
            print("      [dfcleanser_input_formWidget][set_form_value][",input_index,"] : ",self.formTypes_List[input_index],value)
            #print("      [dfcleanser_input_formWidget][set_form_value]",self.formTypes_List[input_index])

        if(type(self.formTypes_List[input_index]) == list) :
            self.input_fields_list[input_index].setPlainText(value)      
        elif(self.formTypes_List[input_index] == "text") :
            self.input_fields_list[input_index].setText(value)
        elif(self.formTypes_List[input_index] == "file") :
            self.input_fields_list[input_index].setText(value)
        
        elif(self.formTypes_List[input_index] == "select") :
            num_items       =  self.input_fields_list[input_index].count() 
            match_found     =   False

            if(DEBUG_INPUT_FORMS_DETAILS) :
                print("      [dfcleanser_input_formWidget][set_form_value] num_items : ",num_items)

            for i in range(num_items) :

                if(DEBUG_INPUT_FORMS_DETAILS) :
                    print("      [dfcleanser_input_formWidget][set_form_value] item[",i,"] : ",self.input_fields_list[input_index].itemText(i))

                if(self.input_fields_list[input_index].itemText(i) == value) :
                    match_found     =   True
                    break

            if(not(match_found)) :
                self.input_fields_list[input_index].setCurrentIndex(0) 
            else :   
                self.input_fields_list[input_index].setCurrentIndex(i)

        else :
            self.input_fields_list[input_index].setText(value)
       
        if(DEBUG_INPUT_FORMS_DETAILS) :
            print("      [dfcleanser_input_formWidget][set_form_value][ end ")


    def reset_form_combobox_by_index(self, input_index, combo_list) :

        if(DEBUG_INPUT_FORMS_DETAILS) :
            print("[dfcleanser_input_formWidget][reset_form_combobox_by_index]",input_index,"\n",combo_list)

        self.input_fields_list[input_index].clear() 

        self.input_fields_list[input_index].addItems(combo_list)
        self.input_fields_list[input_index].setCurrentIndex(0)  

    def set_form_combobox_index(self, input_index, list_index) :

        if(DEBUG_INPUT_FORMS_DETAILS) :
            print("[dfcleanser_input_formWidget][reset_form_combobox_by_index]",input_index,"\n",list_index)

        self.input_fields_list[input_index].setCurrentIndex(list_index)

    def set_form_input_title(self, new_title) :

        if(DEBUG_INPUT_FORMS_DETAILS) :
            print("[dfcleanser_input_formWidget] :set_form_input_title",new_title)

        self.form_title     =  new_title 
        self.input_form_title.setText(self.form_title)        



"""
* --------------------------------------------------------
* --------------------------------------------------------
*  Gneric dfcleanser imput form widget end 
* --------------------------------------------------------
* --------------------------------------------------------
"""




# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -     Common exception and error message handler methods        -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

max_line_len    =   60


def split_up_text(text_line) :

    if(DEBUG_COMMON_EXCEPT) :    
        print("[dfc_qt_model][split_up_text] : text_line \n",text_line)

    split_text_lines    =   []

    line_text       =   text_line
    new_line_text   =   ""

    next_blank_char     =   -1
    last_blank_char     =   -1

    keep_parsing    =   True

    while(keep_parsing) :

        next_blank_char     =   line_text.find(" ")

        if(next_blank_char > -1) :

            if( (len(new_line_text) + len(line_text[0:(next_blank_char+1)]) ) < max_line_len) :

                new_line_text       =   new_line_text + line_text[0:(next_blank_char+1)]
                line_text           =   line_text[(next_blank_char+1):]
                
                if(DEBUG_COMMON_EXCEPT) :
                    print("new_line_text",len(new_line_text),"\n  ",new_line_text)
                    print("line_text ",len(line_text),"\n  ",line_text)

            else :
                
                split_text_lines.append(new_line_text + "<br>")
                new_line_text       =   ""

                if(len(line_text) < max_line_len) :
                    split_text_lines.append(line_text) 
                    keep_parsing    =   False   
                
                if(DEBUG_COMMON_EXCEPT) :
                    print("**new_line_text",len(new_line_text),"\n  ",new_line_text)
                    print("**line_text ",len(line_text),"\n  ",line_text)
        
        else :

            if( (len(new_line_text) + len(line_text)) > max_line_len) :
                split_text_lines.append(new_line_text + "<br>")
                split_text_lines.append(line_text + "<br>") 
            else :
                split_text_lines.append(new_line_text + line_text + "<br>")

            keep_parsing    =   False

    return(split_text_lines)            


def format_QMessageBox_Text(msg_text) :

    if(DEBUG_COMMON_EXCEPT) :    
        print("    [dfc_qt_model][format_QMessageBox_Text] : msg_text \n      ",msg_text)

    current_text    =   msg_text
    new_text_lines  =   []

    if(len(msg_text) <= max_line_len) :
        return(msg_text)

    while(len(current_text) > 0) :

        new_line_loc    =   current_text.find("<br>")

        if(new_line_loc > -1) :
            text_line   =   current_text[0:(new_line_loc+4)]
            new_text_lines.append(text_line)
            current_text    =   current_text[(new_line_loc+4):]
        else :
            text_line   =   current_text
            new_text_lines.append(text_line)
            current_text    =   ""

    final_text  =   ""
    
    if(DEBUG_COMMON_EXCEPT) :    
        print("    [new_text_lines]") 
        for j in range(len(new_text_lines)) :
            print("     [",j,"] ",len(new_text_lines[j]),new_text_lines[j])

    for i in range(len(new_text_lines)) :
        if(len(new_text_lines[i]) <= max_line_len) :
            final_text      =   final_text + new_text_lines[i]
        else :
            split_lines     =   split_up_text(new_text_lines[i])
            for j in range(len(split_lines)) :
                final_text      =   final_text + split_lines[j]    

    return(final_text)


def display_exception(title,status_msg,e) :

    if(DEBUG_COMMON_EXCEPT) :    
        print("\n    [dfc_qt_model][display_exception] : status_msg \n      ",status_msg)

    from dfcleanser.common.common_utils import opStatus
    opstat  =   opStatus()

    opstat.store_exception(status_msg,e)

    from dfcleanser.sw_utilities.DisplayUtils import get_exception_details_text
    details_msg     =   get_exception_details_text(opstat)
    details_msg     =   details_msg.replace("\n","<br>")

    final_msg       =   format_QMessageBox_Text(details_msg)
    
    from PyQt5 import QtCore
    from PyQt5.QtWidgets import QMessageBox
    
    dlg = QMessageBox()
    dlg.setTextFormat(Qt.RichText)
    dlg.setWindowTitle(title)
    text_msg    =   status_msg + "<br>" + final_msg
    dlg.setText(text_msg)
    dlg.setStandardButtons(QMessageBox.Ok)
    dlg.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
    dlg.setStyleSheet("QLabel{min-width: 350px;}")
            
    button = dlg.exec()

    if(DEBUG_COMMON_EXCEPT) :    
        print("    [dfc_qt_model][display_exception] : end \n")
 

def display_error_msg(title,status_msg) :

    if(DEBUG_COMMON_EXCEPT) :    
        print("\n    [dfc_qt_model][display_error_msg] : status_msg \n      ",status_msg)
    
    from PyQt5 import QtCore 
    from PyQt5.QtWidgets import QMessageBox

    dlg = QMessageBox()
    dlg.setTextFormat(Qt.RichText)
    dlg.setWindowTitle(title)
    dlg.setText(status_msg)
    dlg.setStandardButtons(QMessageBox.Ok)
    dlg.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
    dlg.setStyleSheet("QLabel{min-width: 400px;}")
            
    button = dlg.exec()

    if(DEBUG_COMMON_EXCEPT) :    
        print("    [dfc_qt_model][display_error_msg] : end \n")
 
def display_status_msg(title,status_msg) :

    if(DEBUG_COMMON_EXCEPT) :    
        print("\n    [dfc_qt_model][display_status_msg] : status_msg \n      ",status_msg)

    from PyQt5 import QtCore
    from PyQt5.QtWidgets import QMessageBox

    dlg = QMessageBox()
    dlg.setTextFormat(Qt.RichText)
    dlg.setWindowTitle(title)
    dlg.setText(status_msg)
    dlg.setStandardButtons(QMessageBox.Ok)
    dlg.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
    dlg.setStyleSheet("QLabel{min-width: 350px;}")
            
    button = dlg.exec()

    if(DEBUG_COMMON_EXCEPT) :    
        print("    [dfc_qt_model][display_status_msg] : end \n")

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -    Common exception and error message handler methods end     -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#




# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                   Common layout utilities                     -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

def clearLayout(layout):

    from PyQt5 import QtGui
    from PyQt5.QtWidgets import QWidgetItem, QSpacerItem

    for i in reversed(range(layout.count())):
        item = layout.itemAt(i)

        if isinstance(item, QWidgetItem):
            #print "widget" + str(item)
            item.widget().close()
            # or
            # item.widget().setParent(None)
        elif isinstance(item, QSpacerItem):
            #print "spacer " + str(item)
            # no need to do extra stuff
            spacer = item
        else:
            print( "layout " + str(item))
            #self.clearLayout(item.layout())

        # remove the item from layout
        layout.removeItem(item)  


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                   Common button bar utilities                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def build_button_bar(buttonLayout,button_list,text_list,size_list,tool_tip_list,style_sheet,connect_list):
        
    #from PyQt5.QtWidgets import QHBoxLayout, QPushButton
    #cmdbuttonsLayout  =   QHBoxLayout()

    for i in range(len(button_list) ) :

        button_list[i].setText(text_list[i])
        button_list[i].setFixedSize(size_list[0],size_list[1])
        button_list[i].setToolTip(tool_tip_list[i])
        button_list[i].setStyleSheet(style_sheet)
        button_list[i].clicked.connect(connect_list[i]) 
        buttonLayout.addWidget(button_list[i])

    buttonLayout.setAlignment(Qt.AlignHCenter)


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                 Common build cfg parms for form               -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def build_cfg_parms_from_history(ptitles,pvalues,formlabels,ADDL_PARMS=True):
        

    cfg_parms   =   []

    DEBUG_BUILD_CFG     =   False

    addl_parms_found    =   False

    if(ADDL_PARMS) :
        addl_parms_index    =   ptitles.index('Additional Parm(s)')
    else :
        addl_parms_index    =   -1

    if(addl_parms_index > -1) :
        
        parms_len           =   addl_parms_index + 1

        if(not (addl_parms_index == (len(ptitles)-1))) :

            addl_parms_found    =   True

            num_addl_parms      =   (len(ptitles) - addl_parms_index) - 1
            start_addl_parms    =   addl_parms_index + 1

            addl_parms  =   "{"

            if(DEBUG_BUILD_CFG) :
                print("addl_parms_index",addl_parms_index)
                print("num_addl_parms",num_addl_parms)
                print("start_addl_parms",start_addl_parms)

            for j in range(num_addl_parms) :

                addl_parm_title     =   ptitles[start_addl_parms + j]
                addl_parms_value    =   str(pvalues[start_addl_parms + j]) 

                if(DEBUG_BUILD_CFG) :
                    print("addl_parm_title : addl_parms_value ",addl_parm_title,addl_parms_value)
            
                addl_parm_title     =   '"' + addl_parm_title + '" : '
                addl_parms_value    =   '"' + addl_parms_value + '"'

                if(DEBUG_BUILD_CFG) :
                    print("addl_parm_title : addl_parms_value ",addl_parm_title,addl_parms_value)

                new_addl_parm       =   addl_parm_title + addl_parms_value

                if(DEBUG_BUILD_CFG) :
                    print("new_addl_parm  ",new_addl_parm)

                addl_parms  =   addl_parms + new_addl_parm

                if(DEBUG_BUILD_CFG) :
                    print("addl_parms",addl_parms)

                if(not (j==(num_addl_parms-1)) ) :
                    addl_parms  =   addl_parms + '\n'
                else :
                    addl_parms  =   addl_parms + '}'  
            
            if(DEBUG_BUILD_CFG) :
                print("addl_parms",addl_parms)

    else :

        parms_len   =   len(formlabels)

    if(DEBUG_BUILD_CFG) :
        print("parms_len",parms_len)

    for i in range(parms_len) :
               
        parm_to_match    =   formlabels[i]
        
        if(DEBUG_BUILD_CFG) : 
            print("parm_to_match",parm_to_match)

        if(parm_to_match in ptitles) :

            match_index     =   ptitles.index(parm_to_match)
            if(match_index > -1) :
                cfg_parms.append(pvalues[match_index])

        else :

            if(parm_to_match.find("_history") > -1) :
                cfg_parms.append(cfg_parms[1])
            else :
                cfg_parms.append("''")

    if(addl_parms_found) :
        cfg_parms.append(addl_parms)

    return(cfg_parms)



"""
#--------------------------------------------------------------------------
#  common html form functions
#--------------------------------------------------------------------------
"""


def maketextarea(rows, scroll=False):
    return(["textarea", str(rows), scroll])


def isenlargedtextarea(taObject):
    if(type(taObject) == list):
        return(True)
    else:
        return(False)


def gettextarearows(taObject):
    if(isenlargedtextarea(taObject)):
        return(taObject[1])
    else:
        return(3)


def gettextareascroll(taObject):
    return(taObject[2])


def makefilearea(rows):
    return(["filearea", str(rows)])


def getfilearearows(faObject):
    return(faObject[1])


def isfilearea(typeobj):
    if(type(typeobj) == list):
        if(typeobj[0] == "filearea"):
            return(True)

    return(False)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#  common dfcleanser is working thread
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, QEventLoop

# thread to update the status bar
class UpdateStatusBarThread(QThread):
    
    start   =   None

    def update_status_bar(self) :

        print ("update_status_bar")

        from datetime import datetime
        now = datetime.now()

        if(self.start is None) :
            self.start  =   now
        
        delta       =   now - self.start
        seconds     =   delta.seconds

        statmsg     =   self.status_message + str(seconds)
        self.statusbar.showMessage(statmsg)
        

     
    def __init__(self, taskparms):
        QThread.__init__(self)
        
        self.statusbar          =   taskparms[0]
        self.status_message     =   taskparms[1]

        #print("taskparms",taskparms)
        #self.statusbar.showMessage(self.status_message)

        #declaring the timer
        self.statusTimer = PyQt5.QtCore.QTimer()
        self.statusTimer.moveToThread(self)
        self.statusTimer.timeout.connect(self.update_status_bar)


    def run(self):

        print("thread run")
        #self.statusTimer.start(10000)
        print("after start qtimer")
        #loop = QEventLoop()
        #loop.exec_()

# control wraper around status bar thread
class DataCaptureControl():
       
    capctrlparms    =   None

    def __init__(self, ctrlparms):

        super(self.__class__, self).__init__()

        self.capctrlparms  =   ctrlparms

    def startThread(self):
        statusbar          =   self.capctrlparms[0]
        statusbar.showMessage(self.capctrlparms[1])

    def stopThread(self):
        statusbar          =   self.capctrlparms[0]
        statusbar.showMessage(self.capctrlparms[1] + " : Complete") 


