"""
# data_transform_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg 
import dfcleanser.common.help_utils as dfchelp
import dfcleanser.data_transform.data_transform_model as dtm

from dfcleanser.common.html_widgets import (ButtonGroupForm, InputForm) 

from dfcleanser.common.table_widgets import (dcTable, SCROLL_RIGHT, COLUMN_MAJOR,get_col_major_table)

from dfcleanser.common.common_utils import (get_datatype_str, display_generic_grid, RunningClock,
                                            is_datetime_col, is_date_col, is_time_col, is_int_col,
                                            get_datatype_id, is_numeric_col, whitecolor, get_select_defaults)

#from dfcleanser.common.display_utils import get_df_col_names_table

"""
* -----------------------------------------------------
*   configuration variable keys
* -----------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   data transform form components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#    data transform task bar
#--------------------------------------------------------------------------
"""
data_transform_tb_doc_title                 =   "Transform Options"
data_transform_tb_title                     =   "Transform Options"
data_transform_tb_id                        =   "transformoptionstb"

data_transform_tb_keyTitleList              =   ["DataFrame</br> Transform",
                                                 "Columns</br> Transform",
                                                 "Datetime</br>Transform",
                                                 "Dateframe</br>Schema",
                                                 "Clear","Reset","Help"]

data_transform_tb_jsList                    =   ["transform_task_bar_callback("+str(dtm.DISPLAY_DATAFRAME_TRANSFORM)+")",
                                                 "transform_task_bar_callback("+str(dtm.DISPLAY_COLUMNS_TRANSFORM)+")",
                                                 "transform_task_bar_callback("+str(dtm.DISPLAY_DATETIME_TRANSFORM)+")",
                                                 "transform_task_bar_callback("+str(dtm.DISPLAY_DF_SCHEMA_TRANSFORM)+")",
                                                 "transform_task_bar_callback("+str(dtm.DFC_TRANSFORM_RETURN)+")",
                                                 "process_pop_up_cmd(6)",
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_MAIN_TASKBAR_ID) + ")"]

data_transform_tb_centered                  =   True


"""
#--------------------------------------------------------------------------
#    data transform pop-up task bars
#--------------------------------------------------------------------------
"""
data_transform_tbA_doc_title                =   "Transform Options"
data_transform_tbA_title                    =   "Transform Options"
data_transform_tbA_id                       =   "transformoptionstbA"

data_transform_tbA_keyTitleList             =   ["DataFrame</br> Transform",
                                                 "Columns</br> Transform",
                                                 "Datetime</br>Transform"]

data_transform_tbA_jsList                   =   ["transform_task_bar_callback("+str(dtm.DISPLAY_DATAFRAME_TRANSFORM)+")",
                                                 "transform_task_bar_callback("+str(dtm.DISPLAY_COLUMNS_TRANSFORM)+")",
                                                 "transform_task_bar_callback("+str(dtm.DISPLAY_DATETIME_TRANSFORM)+")"]

data_transform_tbA_centered                 =   True

data_transform_tbB_doc_title                =   "Transform Options"
data_transform_tbB_title                    =   "Transform Options"
data_transform_tbB_id                       =   "transformoptionstbB"

data_transform_tbB_keyTitleList             =   ["Dateframe</br>Schema",
                                                 "Clear","Reset","Help"]

data_transform_tbB_jsList                   =   ["transform_task_bar_callback("+str(dtm.DISPLAY_DF_SCHEMA_TRANSFORM)+")",
                                                 "transform_task_bar_callback("+str(dtm.DFC_TRANSFORM_RETURN)+")",
                                                 "process_pop_up_cmd(6)",
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_MAIN_TASKBAR_ID) + ")"]

data_transform_tbB_centered                 =   True


"""
#--------------------------------------------------------------------------
#    datetime transform task bar
#--------------------------------------------------------------------------
"""
datetime_transform_tb_doc_title             =   "datetime Transform Options"
datetime_transform_tb_title                 =   "datetime Transform Options"
datetime_transform_tb_id                    =   "datetimetransformoptionstb"

datetime_transform_tb_keyTitleList          =   ["Convert</br> Column</br>Datatype",
                                                 "Calculate</br> timedelta</br>Column",
                                                 "Split Column </br>to date,time</br> Columns",
                                                 "Merge Column </br>from date,time</br> Columns",
                                                 "Datetime</br>Components",
                                                 "Return","Help"]

datetime_transform_tb_jsList                =   ["dt_datetime_transform_task_bar_callback("+str(dtm.DISPLAY_DATETIME_DATATYPE)+")",
                                                 "dt_datetime_transform_task_bar_callback("+str(dtm.DISPLAY_TIMEDELTA)+")",
                                                 "dt_datetime_transform_task_bar_callback("+str(dtm.DISPLAY_DATETIME_SPLIT)+")",
                                                 "dt_datetime_transform_task_bar_callback("+str(dtm.DISPLAY_DATETIME_MERGE)+")",
                                                 "dt_datetime_transform_task_bar_callback("+str(dtm.DISPLAY_DATETIME_COMPONENTS)+")",
                                                 "transform_task_bar_callback("+str(dtm.DFC_TRANSFORM_RETURN)+")",
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_MAIN_TASKBAR_ID) + ")"]


datetimeA_transform_tb_doc_title            =   "datetime Transform Options"
datetimeA_transform_tb_title                =   "datetime Transform Options"
datetimeA_transform_tb_id                   =   "datetimeAtransformoptionstb"

datetimeA_transform_tb_keyTitleList         =   ["Convert</br> Column</br>Datatype",
                                                 "Calculate</br> timedelta</br>Column",
                                                 "Split Column </br>to date,time</br> Columns",
                                                 "Merge Column </br>from date,time</br> Columns"]

datetimeA_transform_tb_jsList               =   ["dt_datetime_transform_task_bar_callback("+str(dtm.DISPLAY_DATETIME_DATATYPE)+")",
                                                 "dt_datetime_transform_task_bar_callback("+str(dtm.DISPLAY_TIMEDELTA)+")",
                                                 "dt_datetime_transform_task_bar_callback("+str(dtm.DISPLAY_DATETIME_SPLIT)+")",
                                                 "dt_datetime_transform_task_bar_callback("+str(dtm.DISPLAY_DATETIME_MERGE)+")"]

datetimeB_transform_tb_doc_title            =   "datetime Transform Options"
datetimeB_transform_tb_title                =   "datetime Transform Options"
datetimeB_transform_tb_id                   =   "datetimeBtransformoptionstb"

datetimeB_transform_tb_keyTitleList         =   ["Datetime</br>Components",
                                                 "Return","Help"]

datetimeB_transform_tb_jsList               =   ["dt_datetime_transform_task_bar_callback("+str(dtm.DISPLAY_DATETIME_COMPONENTS)+")",
                                                 "transform_task_bar_callback("+str(dtm.DFC_TRANSFORM_RETURN)+")",
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_MAIN_TASKBAR_ID) + ")"]






"""
#--------------------------------------------------------------------------
#   datetime format input 
#--------------------------------------------------------------------------
"""
datetime_format_input_title             =   "Datetime Format Parameters"
datetime_format_input_id                =   "datetimeformatinput"
datetime_format_input_idList            =   ["dtcolname",
                                             "dtdatatype",
                                             "dtnanfillvalue",
                                             "dtformatstring",
                                             None,None,None,None]

datetime_format_input_labelList         =   ["column_name",
                                             "datetime_datatype",
                                             "nan_fill_value",
                                             "format_string",
                                             "Change</br>Data</br>Type",
                                             "Get</br>formats",
                                             "Return","Help"]

datetime_format_input_typeList          =   ["select","select","text","text","button","button","button","button"]

datetime_format_input_placeholderList   =   ["column name",
                                             "datetime datatype",
                                             "nan fill value (default = None - NaT)",
                                             "format string to use (default = infer)",
                                             None,None,None,None]

datetime_format_input_jsList            =   [None,None,None,None,
                                             "process_datetime_format_transform_callback(0)",
                                             "process_datetime_format_transform_callback(1)",
                                             "process_datetime_format_transform_callback(3)",
                                             "displayhelp(" + str(dfchelp.TRANSFORM_MAIN_TASKBAR_ID) + ")"]

datetime_format_input_reqList           =   [0,1,2]


datetime_format_ftypes_input_typeList   =   ["select","select","text","select","button","button","button","button"]

"""
datetime_format_ftypes_input_labelList  =   ["column_name",
                                             "datetime_datatype",
                                             "nan_fill_value",
                                             "format_string",
                                             "Change</br>Data</br>Type",
                                             "Get</br>Cols",
                                             "Return","Help"]

datetime_format_ftypes_input_jsList     =   [None,None,None,None,
                                             "process_datetime_format_transform_callback(0)",
                                             "process_datetime_format_transform_callback(4)",
                                             "process_datetime_format_transform_callback(3)",
                                             "displayhelp(" + str(dfchelp.TRANSFORM_MAIN_TASKBAR_ID) + ")"]
"""
"""
#--------------------------------------------------------------------------
#   datetime timedelta input 
#--------------------------------------------------------------------------
"""
datetime_tdelta_input_title             =   "Datetime timedelta Parameters"
datetime_tdelta_input_id                =   "datetimetdeltainput"
datetime_tdelta_input_idList            =   ["dttdcolname",
                                             "dttdcolname1",
                                             "dttdrescolname",
                                             "dttdunits",
                                             None,None,None,None]

datetime_tdelta_input_labelList         =   ["datetime_column_name_1",
                                             "datetime_column_name_2",
                                             "timedelta_column_name",
                                             "time_units",
                                             "Calculate</br> timedelta",
                                             "Clear",
                                             "Return","Help"]

datetime_tdelta_input_typeList          =   ["select","select","text","select",
                                             "button","button","button","button"]

datetime_tdelta_input_placeholderList   =   ["first column name",
                                             "second column name",
                                             "time delta column name",
                                             "time delta units",
                                              None,None,None,None]

datetime_tdelta_input_jsList            =   [None,None,None,None,
                                             "process_datetime_tdelta_callback(0)",
                                             "process_datetime_tdelta_callback(1)",
                                             "process_datetime_tdelta_callback(2)",
                                             "displayhelp(" + str(dfchelp.TRANSFORM_MAIN_TASKBAR_ID) + ")"]

datetime_tdelta_input_reqList           =   [0,1,2,3]

"""
#--------------------------------------------------------------------------
#   datetime merge input 
#--------------------------------------------------------------------------
"""
datetime_merge_input_title              =   "Datetime Merge Parameters"
datetime_merge_input_id                 =   "datetimetmergeinput"
datetime_merge_input_idList             =   ["dtmdatecolname",
                                             "dtmtimecolname",
                                             "dtmdatetimecolname",
                                             None,None,None,None]

datetime_merge_input_labelList          =   ["date_column_name",
                                             "time_column_name",
                                             "datetime_column_name",
                                             "Merge</br>Columns",
                                             "Clear",
                                             "Return","Help"]

datetime_merge_input_typeList           =   ["select","select","text","button","button","button","button"]

datetime_merge_input_placeholderList    =   ["date column name",
                                             "time column name",
                                             "new merged column name",
                                              None,None,None,None]

datetime_merge_input_jsList             =   [None,None,None,
                                             "process_datetime_merge_split_callback(0,"+str(dtm.MERGE)+")",
                                             "process_datetime_merge_split_callback(1,"+str(dtm.MERGE)+")",
                                             "process_datetime_merge_split_callback(2,"+str(dtm.MERGE)+")",
                                             "displayhelp(" + str(dfchelp.TRANSFORM_MAIN_TASKBAR_ID) + ")"]

datetime_merge_input_reqList            =   [0,1,2]

"""
#--------------------------------------------------------------------------
#   datetime split input 
#--------------------------------------------------------------------------
"""
datetime_split_input_title              =   "Datetime Split Parameters"
datetime_split_input_id                 =   "datetimetsplitinput"
datetime_split_input_idList             =   ["dtsdatetimecolname",
                                             "dtsdatecolname",
                                             "dtstimecolname",
                                             None,None,None,None]

datetime_split_input_labelList          =   ["datetime_column_name",
                                             "date_column_name",
                                             "time_column_name",
                                             "Split</br>Column",
                                             "Clear",
                                             "Return","Help"]

datetime_split_input_typeList           =   ["select","text","text","button","button","button","button"]

datetime_split_input_placeholderList    =   ["datetime column name",
                                             "date column name",
                                             "time column name",
                                              None,None,None,None]

datetime_split_input_jsList             =   [None,None,None,
                                             "process_datetime_merge_split_callback(0,"+str(dtm.SPLIT)+")",
                                             "process_datetime_merge_split_callback(1,"+str(dtm.SPLIT)+")",
                                             "process_datetime_merge_split_callback(2,"+str(dtm.SPLIT)+")",
                                             "displayhelp(" + str(dfchelp.TRANSFORM_MAIN_TASKBAR_ID) + ")"]

datetime_split_input_reqList            =   [0,1,2]


"""
#--------------------------------------------------------------------------
#   datetime components input 
#--------------------------------------------------------------------------
"""
datetime_comp_input_title               =   "Datetime Split Parameters"
datetime_comp_input_id                  =   "datetimecompinput"
datetime_comp_input_idList              =   ["dtcdatetimecolname",
                                             "dtccomptype",
                                             "dtcresultcolname",
                                             None,None,None]

datetime_comp_input_labelList           =   ["datetime_column_name",
                                             "datetime_component",
                                             "result_column_name",
                                             "Get</br>Component",
                                             "Return","Help"]

datetime_comp_input_typeList            =   ["select","select","text","button","button","button"]

datetime_comp_input_placeholderList     =   ["datetime column name",
                                             "date column name",
                                             "result column name",
                                              None,None,None]

datetime_comp_input_jsList              =   [None,None,None,
                                             "process_datetime_components_callback(0)",
                                             "process_datetime_components_callback(1)",
                                             "displayhelp(" + str(dfchelp.TRANSFORM_MAIN_TASKBAR_ID) + ")"]

datetime_comp_input_reqList             =   [0,1,2]


"""
#--------------------------------------------------------------------------
#   datatime radio 
#--------------------------------------------------------------------------
"""
datetime_radio_id                       =   "datetimeselect"
datetime_radio_idList                   =   ["datetimercid","datercid","timercid","deltarcid",]

datetime_radio_labelList                =   ["datetime.datetime","&nbsp;&nbsp;datetime.date&nbsp;&nbsp;",
                                             "&nbsp;&nbsp;datetime.time&nbsp;&nbsp;",
                                             "&nbsp;&nbsp;datetime.timedelta&nbsp;&nbsp;"]


datetime_radio_form                     =   [datetime_radio_id,
                                             datetime_radio_idList,
                                             datetime_radio_labelList]

datetime_radio_jslist                   =   ["select_datetime_dt(0)",
                                             "select_datetime_dt(1)",
                                             "select_datetime_dt(2)",
                                             "select_datetime_dt(3)"]


datatransform_inputs        =   [datetime_format_input_id,datetime_tdelta_input_id,datetime_merge_input_id,
                                 datetime_split_input_id,datetime_comp_input_id]


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    data transform display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def display_main_taskbar() :
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        from dfcleanser.common.display_utils import display_dfcleanser_taskbar
        display_dfcleanser_taskbar(ButtonGroupForm(data_transform_tb_id,
                                                   data_transform_tb_keyTitleList,
                                                   data_transform_tb_jsList,
                                                   data_transform_tb_centered))
    else :
        
        transform_tb_A     =   ButtonGroupForm(data_transform_tbA_id,
                                               data_transform_tbA_keyTitleList,
                                               data_transform_tbA_jsList,
                                               data_transform_tbA_centered)
        
        transform_tb_A.set_gridwidth(480)
        transform_tb_A_html    =   transform_tb_A.get_html()
        
        transform_tb_B     =   ButtonGroupForm(data_transform_tbB_id,
                                               data_transform_tbB_keyTitleList,
                                               data_transform_tbB_jsList,
                                               data_transform_tbB_centered)
        
        transform_tb_B.set_gridwidth(480)
        transform_tb_B_html    =   transform_tb_B.get_html()
        
        gridclasses     =   ["dfc-top-","dfc-footer"]
        gridhtmls       =   [transform_tb_A_html,transform_tb_B_html]
    
        display_generic_grid("dfcleanser-system-tb-pop-up-wrapper",gridclasses,gridhtmls)

        
    
def display_no_dataframe() :
        
    display_main_taskbar()
    
def display_transform_columns_taskbar() :
    
    from dfcleanser.data_transform.data_transform_columns_widgets import display_base_data_transform_columns_taskbar
    display_base_data_transform_columns_taskbar()


def display_datetime_column_taskbar() :

    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        from dfcleanser.common.display_utils import display_dfcleanser_taskbar
        display_dfcleanser_taskbar(ButtonGroupForm(datetime_transform_tb_id,
                                                   datetime_transform_tb_keyTitleList,
                                                   datetime_transform_tb_jsList,
                                                   False))
    else :
        
        dtA_taskbar     =   ButtonGroupForm(datetimeA_transform_tb_id,
                                            datetimeA_transform_tb_keyTitleList,
                                            datetimeA_transform_tb_jsList,
                                            False)
        
        dtB_taskbar     =   ButtonGroupForm(datetimeB_transform_tb_id,
                                            datetimeB_transform_tb_keyTitleList,
                                            datetimeB_transform_tb_jsList,
                                            False)
       
        dtA_taskbar.set_gridwidth(460)
        dtA_taskbar_html    =   dtA_taskbar.get_html()
        
        dtB_taskbar.set_gridwidth(460)
        dtB_taskbar_html    =   dtB_taskbar.get_html()
        
        
        gridclasses     =   ["dfc-top-","dfc-footer"]
        gridhtmls       =   [dtA_taskbar_html,dtB_taskbar_html]
    
        display_generic_grid("dfcleanser-system-tb-pop-up-wrapper",gridclasses,gridhtmls)

        
            
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    datetime components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def display_datetime_convert(parms=None) :
    """
    * ---------------------------------------------------------
    * function : display date time convert input screen
    * 
    * parms :
    *  parms          - datatype parms
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """

    dtid        =   ""
    colname     =   ""
    nanvalue    =   ""
    
    if(parms == None) :
        cfg.drop_config_value(datetime_format_input_id+"Parms")
        
    else :
        
        if(len(parms) == 1) :
            
            if(parms[0] == 0) :
                dtid    =   11
            elif(parms[0] == 1) :
                dtid    =   12
            elif(parms[0] == 2) :
                dtid    =   13
                
            cfg.drop_config_value(datetime_format_input_id+"Parms")
        
            dt_datetime_custom_form = InputForm(datetime_format_input_id,
                                                datetime_format_input_idList,
                                                datetime_format_input_labelList,
                                                datetime_format_input_typeList,
                                                datetime_format_input_placeholderList,
                                                datetime_format_input_jsList,
                                                datetime_format_input_reqList)
            
            strftimelist    =   None
    
        else :
        
            dtid        =   11
            from dfcleanser.sw_utilities.sw_utility_control import get_Dict
            strftimedict = get_Dict("strftime")
            
            strftimekeys    =   list(strftimedict.keys())
            strftimelist    =   []
            for i in range(len(strftimekeys)) :
                strftimelist.append(strftimekeys[i] + " : " + strftimedict.get(strftimekeys[i]))    
            
            dt_datetime_custom_form = InputForm(datetime_format_input_id,
                                                datetime_format_input_idList,
                                                datetime_format_input_labelList,
                                                datetime_format_ftypes_input_typeList,
                                                datetime_format_input_placeholderList,
                                                datetime_format_input_jsList,
                                                datetime_format_input_reqList)
        
    parmsList = [colname,get_datatype_str(dtid),str(nanvalue),""]
    cfg.set_config_value(datetime_format_input_id+"Parms",parmsList)

    
    selectDicts     =   [] 
    
    current_df      =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
    colnames        =   current_df.columns.tolist()
    cnames          =   {"default":colnames[0],"list": colnames}
    selectDicts.append(cnames)
        
    dtsel           =   {"default":"datetime.datetime","list":["datetime.datetime","datetime.date","datetime.time",
                                                               "datetime.timedelta","numpy.datetime64","numpy.timedelta64"]}
    selectDicts.append(dtsel)
    
    if(not(strftimelist is None)) :
        strftimesel     =   {"default":strftimelist[0],"list": strftimelist}
        selectDicts.append(strftimesel)
    
        get_select_defaults(dt_datetime_custom_form,
                            datetime_format_input_id,
                            datetime_format_input_idList,
                            datetime_format_ftypes_input_typeList,
                            selectDicts)
    
    else :
        
        get_select_defaults(dt_datetime_custom_form,
                            datetime_format_input_id,
                            datetime_format_input_idList,
                            datetime_format_input_typeList,
                            selectDicts)
    
    dt_datetime_custom_form.set_shortForm(True)
    dt_datetime_custom_form.set_buttonstyle({"font-size":12, "height":75, "width":100, "left-margin":22})
    dt_datetime_custom_form.set_gridwidth(480)
    dt_datetime_custom_form.set_fullparms(True)  
    
    dt_datetime_custom_html = dt_datetime_custom_form.get_html()

    dt_datetime_title_html  =   "<br><div>Datetime Convert Parms</div><br>"
        
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
    gridhtmls       =   [dt_datetime_title_html,dt_datetime_custom_html]
    
    display_generic_grid("dtformat-wrapper",gridclasses,gridhtmls)


def display_datetime_timedelta(parms)  :
    """
    * ---------------------------------------------------------
    * function : display date time timedelta input screen
    * 
    * parms :
    *  parms          - datatype parms
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """
    
    dt_datetime_custom_form = InputForm(datetime_tdelta_input_id,
                                        datetime_tdelta_input_idList,
                                        datetime_tdelta_input_labelList,
                                        datetime_tdelta_input_typeList,
                                        datetime_tdelta_input_placeholderList,
                                        datetime_tdelta_input_jsList,
                                        datetime_tdelta_input_reqList)
    selectDicts     =   [] 
    
    current_df      =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
    colnames        =   current_df.columns.tolist()
    cnames          =   {"default":colnames[0],"list": colnames}
    selectDicts.append(cnames)
    selectDicts.append(cnames)
        
    dtsel           =   {"default":"Seconds","list":["Years","Days","Hours","Minutes","Seconds","MicroSeconds","datetime.timedelta"]}
    selectDicts.append(dtsel)
    
    get_select_defaults(dt_datetime_custom_form,
                        datetime_tdelta_input_id,
                        datetime_tdelta_input_idList,
                        datetime_tdelta_input_typeList,
                        selectDicts)

    dt_datetime_custom_form.set_shortForm(True)
    dt_datetime_custom_form.set_buttonstyle({"font-size":12, "height":75, "width":100, "left-margin":22})
    dt_datetime_custom_form.set_gridwidth(480)
    dt_datetime_custom_form.set_fullparms(True)  
    
    dt_datetime_custom_html = dt_datetime_custom_form.get_html()
    
    dt_datetime_title_html  =   "<div>Calculate Datetime.timedelta</div><br>"
        
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
    gridhtmls       =   [dt_datetime_title_html,dt_datetime_custom_html]
    print("\n")
    display_generic_grid("dtformat-wrapper",gridclasses,gridhtmls)


def display_datetime_split_merge(parms,action) :
    """
    * ---------------------------------------------------------
    * function : display date time split or merge input screen
    * 
    * parms :
    *  parms          - datatype parms
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """
    
    if(action == dtm.SPLIT) :
        
        dt_datetime_custom_form = InputForm(datetime_split_input_id,
                                            datetime_split_input_idList,
                                            datetime_split_input_labelList,
                                            datetime_split_input_typeList,
                                            datetime_split_input_placeholderList,
                                            datetime_split_input_jsList,
                                            datetime_split_input_reqList)
        
        selectDicts     =   [] 
    
        current_df      =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
        colnames        =   current_df.columns.tolist()
        cnames          =   {"default":colnames[0],"list": colnames}
        selectDicts.append(cnames)
        
        get_select_defaults(dt_datetime_custom_form,
                            datetime_split_input_id,
                            datetime_split_input_idList,
                            datetime_split_input_typeList,
                            selectDicts)
        
        dt_datetime_custom_form.set_shortForm(True)
        dt_datetime_custom_form.set_buttonstyle({"font-size":12, "height":75, "width":100, "left-margin":20})
        dt_datetime_custom_form.set_gridwidth(480)
        dt_datetime_custom_form.set_fullparms(True)  
        
        dt_datetime_custom_html = dt_datetime_custom_form.get_html()

        dt_datetime_title_html  =   "<div>Split Datetime Column Parameters</div><br>"
        
    else :
        
        dt_datetime_custom_form = InputForm(datetime_merge_input_id,
                                            datetime_merge_input_idList,
                                            datetime_merge_input_labelList,
                                            datetime_merge_input_typeList,
                                            datetime_merge_input_placeholderList,
                                            datetime_merge_input_jsList,
                                            datetime_merge_input_reqList)
        
        selectDicts     =   [] 
    
        current_df      =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
        colnames        =   current_df.columns.tolist()
        cnames          =   {"default":colnames[0],"list": colnames}
        selectDicts.append(cnames)
        selectDicts.append(cnames)
        
        get_select_defaults(dt_datetime_custom_form,
                            datetime_merge_input_id,
                            datetime_merge_input_idList,
                            datetime_merge_input_typeList,
                            selectDicts)
        
        dt_datetime_custom_form.set_shortForm(True)
        dt_datetime_custom_form.set_buttonstyle({"font-size":12, "height":75, "width":100, "left-margin":22})
        dt_datetime_custom_form.set_gridwidth(480)
        dt_datetime_custom_form.set_fullparms(True)  
        
        dt_datetime_custom_html = dt_datetime_custom_form.get_html()
        
        dt_datetime_title_html  =   "<div>Merge Datetime Columns</div><br>"
        
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
    gridhtmls       =   [dt_datetime_title_html,dt_datetime_custom_html]
    
    print("\n")
    display_generic_grid("dtformat-wrapper",gridclasses,gridhtmls)


def display_datetime_components(parms) :
    """
    * ---------------------------------------------------------
    * function : display date time split or merge input screen
    * 
    * parms :
    *  parms          - datatype parms
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """
    
    dt_datetime_comps_form = InputForm(datetime_comp_input_id,
                                       datetime_comp_input_idList,
                                       datetime_comp_input_labelList,
                                       datetime_comp_input_typeList,
                                       datetime_comp_input_placeholderList,
                                       datetime_comp_input_jsList,
                                       datetime_comp_input_reqList)
    
    selectDicts     =   [] 
    
    current_df      =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
    colnames        =   current_df.columns.tolist()
    cnames          =   {"default":colnames[0],"list": colnames}
    selectDicts.append(cnames)
        
    comps           =   {"default":"Day of Week","list":["numpy.datetime64","year","quarter","month","week","week of year","day","day of year","day of week","hour","minute","second"]}
    selectDicts.append(comps)
    get_select_defaults(dt_datetime_comps_form,
                        datetime_comp_input_id,
                        datetime_comp_input_idList,
                        datetime_comp_input_typeList,
                        selectDicts)
    
    dt_datetime_comps_form.set_shortForm(True)
    dt_datetime_comps_form.set_buttonstyle({"font-size":12, "height":50, "width":140, "left-margin":15})
    dt_datetime_comps_form.set_gridwidth(480)
    dt_datetime_comps_form.set_fullparms(True)  
        
    dt_datetime_comps_html = dt_datetime_comps_form.get_html()
        
    dt_datetime_title_html  =   "<div>Get Datetime Component</div><br>"
        
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
    gridhtmls       =   [dt_datetime_title_html,dt_datetime_comps_html]
    
    print("\n")
    display_generic_grid("dtformat-wrapper",gridclasses,gridhtmls)

       
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    data transfrom display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    display main option widgets
#--------------------------------------------------------------------------
"""
def display_main_option(parms,clear=False) :
    """
    * ---------------------------------------------------------
    * function : display main options
    * 
    * parms :
    *  parms          - datatype parms
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """

    if(parms == None) :
            
        display_main_taskbar()
        cfg.display_data_select_df(cfg.DataTransform_ID)
        
    else : 
        
        if(cfg.is_a_dfc_dataframe_loaded()) :
            
            funcid = parms[0][0]
        
            if(funcid == dtm.DISPLAY_DATAFRAME_TRANSFORM) :
            
                from dfcleanser.data_transform.data_transform_dataframe_widgets import display_dataframe_transform_taskbar
                display_dataframe_transform_taskbar()
                
            elif(funcid == dtm.DISPLAY_COLUMNS_TRANSFORM) :
            
                from dfcleanser.data_transform.data_transform_columns_widgets import display_base_data_transform_columns_taskbar
                display_base_data_transform_columns_taskbar()
            
            elif(funcid == dtm.DISPLAY_DATETIME_TRANSFORM) :
                display_datetime_column_taskbar() 
            
            elif(funcid == dtm.DISPLAY_DF_SCHEMA_TRANSFORM) :
                display_main_taskbar()
                print("\n")
                display_df_schema_table() 
                
            elif(funcid == dtm.DFC_TRANSFORM_RETURN) :
                display_main_taskbar()
                
        else :
            
            display_main_taskbar()
            cfg.display_data_select_df(cfg.DataTransform_ID)

            
    if(clear) :
        from dfcleanser.data_transform.data_transform_process import clear_data_transform_cfg_values
        clear_data_transform_cfg_values()


def display_transform_col_data(df,colname,display=True) :
    """
    * ---------------------------------------------------------
    * function : display transform col data
    * 
    * parms :
    *  df          -   dataframe
    *  colname     -   column name
    *  display     -   display flag
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """

    statsHeader    =   ["",""]
    statsRows      =   []
    statsWidths    =   [60,40]
    statsAligns    =   ["left","left"]
    
    colorList = []    
    
    statsRows.append(["Column Name",colname])
    colorList.append([whitecolor,whitecolor])
    
    found = -1
    
    df_cols     = df.columns.tolist()
    df_dtypes   = df.dtypes.tolist()
    for i in range(len(df_cols)) :
        if(df_cols[i] == colname) :
            found = i
    
    if(found != -1) :
        ftype = df_dtypes[found]
    
    if(is_datetime_col(df,colname)) :
        typestr = get_datatype_str(11)
    elif(is_date_col(df,colname)) :
        typestr = get_datatype_str(12)
    elif(is_time_col(df,colname)) :
        typestr = get_datatype_str(13)
    else :
        typestr = get_datatype_str(get_datatype_id(ftype))
        
    statsRows.append(["Column Data Type",typestr])
    colorList.append([whitecolor,whitecolor])
    
    nans      =     df[colname].isnull().sum()
    statsRows.append(["Total Nans",nans])
    colorList.append([whitecolor,whitecolor])
    
    try :
        uniques   =     df[colname].unique()    
        statsRows.append(["Column Uniques Count",len(uniques)])
        colorList.append([whitecolor,whitecolor])
    except :
        statsRows.append(["",""])
        colorList.append([whitecolor,whitecolor])
    
    if(is_numeric_col(df,colname)) :
        statsRows.append(["Min Value",df[colname].min()])
        colorList.append([whitecolor,whitecolor])
        statsRows.append(["Max Value",df[colname].max()])
        colorList.append([whitecolor,whitecolor])
    
    stats_table = dcTable("Column Stats","colstatsTable",cfg.DataTransform_ID,
                          statsHeader,statsRows,statsWidths,statsAligns)

    stats_table.set_rowspertable(10)
    stats_table.set_color(True)
    stats_table.set_colorList(colorList)
    if(display) :
        stats_table.set_small(True)
        stats_table.set_smallwidth(30)
        stats_table.set_smallmargin(32)

    stats_table.set_border(False)
    stats_table.set_checkLength(False)
    
    if(display) :
        stats_table.display_table()
    else :
        return(stats_table.get_html())


"""
* ----------------------------------------------------------------
* ----------------------------------------------------------------
*             dataframe schema objects
* ----------------------------------------------------------------
* ----------------------------------------------------------------
"""

schema_data_type_button    =   """
                            <div>
                                        <button type='button' class='btn btn-grp dc-schema-button' style='margin-left:15px;' id="dtXXXXbutton" onClick="dfsch_changedt('XXXXcolname')">Change</br>Datatype</button>
                            </div>
"""

schema_compat_button    =   """
                            <table>
                                <tr>
                                    <td align='center' style='width:100%'>
                                        <button type='button' class='btn btn-grp dc-schema-button' style='margin-left:15px;' id="ccXXXXbutton" onClick="dfsch_chkcompat('XXXXcolname')">Check</br>Compatability</button>
                                    </td>
                                </tr>
                            </table>
"""


def update_df_schema_table(schema_table,direction=SCROLL_RIGHT,display=True) : 
    """            
    #------------------------------------------------------------------
    #   update df schema data
    #
    #   df              -   dataframe
    #   schema_table    -   schema table
    #   display         -   display flag
    #
    #------------------------------------------------------------------
    """

    #print("update_df_schema_table",schema_table.get_lastcoldisplayed(),schema_table.get_colsperrow(),direction)

    df  =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
    
    from dfcleanser.common.table_widgets import set_col_major_table_scroll
    set_col_major_table_scroll(schema_table,direction)
    
    # build the table lists from the column stats
    dfHeader        =   ["    "]
    dfWidths        =   [7]
    dfAligns        =   ["center"]
    
    datatyperow     =   ["<b>datatype</b>"]
    numuniquesrow   =   ["<b>num uniques</b>"]
    numnansrow      =   ["<b>num nans</b>"]
    meanrow         =   ["<b>mean</b>"]
    stdrow          =   ["<b>std dev</b>"]
    minrow          =   ["<b>min</b>"]
    maxrow          =   ["<b>max</b>"]
    skewrow         =   ["<b>skew</b>"]
    kurtrow         =   ["<b>kurtosis</b>"]
       
    dtbuttonrow     =   [" "]
    dtcompatbuttonrow = [" "]
    
    dfRowsList      =   []
    
    df_cols     =   df.columns.tolist()
    df_dtypes   =   df.dtypes.tolist()
    
    start_col       =   schema_table.get_lastcoldisplayed()
    if( not (start_col == 0)) :
        start_col       =   start_col + 1
        
    current_col     =   schema_table.get_lastcoldisplayed()
    
    #print("update_df_schema_table start_col" ,start_col)
    
    for i in range(schema_table.get_colsperrow()) :
        
        current_col     =   start_col + i
        #print("update_df_schema_table current_col",current_col)
        
        if(current_col > len(df_cols)) :
            
            dfHeader.append(" ")
            
            datatyperow.append(" ")
            numuniquesrow.append(" ")
            numnansrow.append(" ")
            meanrow.append(" ")
            stdrow.append(" ")
            minrow.append(" ")
            maxrow.append(" ")
            skewrow.append(" ")
            kurtrow.append(" ")
            dtbuttonrow.append(" ")
            dtcompatbuttonrow.append(" ")
            
        else :

            dfHeader.append(df_cols[current_col])
        
            datatyperow.append(str(df_dtypes[current_col]))      
        
            numuniquesrow.append(df[df_cols[current_col]].nunique())
            numnansrow.append(df[df_cols[current_col]].isnull().sum())
        
            if(is_numeric_col(df,df_cols[current_col])) :
            
                try :
                    meanrow.append(float("{0:.2f}".format(df[df_cols[current_col]].mean())))
                    stdrow.append(float("{0:.2f}".format(df[df_cols[current_col]].std())))
                
                    if(is_int_col(df,df_cols[current_col])) :
                        minrow.append(df[df_cols[current_col]].min())
                        maxrow.append(df[df_cols[current_col]].max())
                    else :    
                        minrow.append(float("{0:.2f}".format(df[df_cols[current_col]].min())))
                        maxrow.append(float("{0:.2f}".format(df[df_cols[current_col]].max())))
                
                    skewrow.append(float("{0:.2f}".format(df[df_cols[current_col]].skew())))
                    kurtrow.append(float("{0:.2f}".format(df[df_cols[current_col]].kurtosis())))
                
                except : 
                    
                    datatyperow.append(" ")
                    numuniquesrow.append(" ")
                    numnansrow.append(" ")
                    meanrow.append(" ")
                    stdrow.append(" ")
                    minrow.append(" ")
                    maxrow.append(" ")
                    skewrow.append(" ")
                    kurtrow.append(" ")
                    dtbuttonrow.append(" ")
                    dtcompatbuttonrow.append(" ")
                    
            else :
                
                meanrow.append(" ")
                stdrow.append(" ")
                minrow.append(" ")
                maxrow.append(" ")
                skewrow.append(" ")
                kurtrow.append(" ")

                
            dtbutton_html     =   schema_data_type_button
            dtbutton_html     =   dtbutton_html.replace("XXXXbutton","col" + str(i))#df_cols[current_col])
            dtbutton_html     =   dtbutton_html.replace("XXXXcolname",df_cols[current_col])
            dtbuttonrow.append(dtbutton_html)
                    
            ccbutton_html     =   schema_compat_button
            ccbutton_html     =   ccbutton_html.replace("XXXXbutton","col" + str(i))
            ccbutton_html     =   ccbutton_html.replace("XXXXcolname",df_cols[current_col])
            dtcompatbuttonrow.append(ccbutton_html)
                   
        dfWidths.append(13)
        dfAligns.append("center")
        
    dfRowsList.append(datatyperow)
    dfRowsList.append(numuniquesrow)
    dfRowsList.append(numnansrow)
    dfRowsList.append(meanrow)
    dfRowsList.append(stdrow)
    dfRowsList.append(minrow)
    dfRowsList.append(maxrow)
    dfRowsList.append(skewrow)
    dfRowsList.append(kurtrow)
    dfRowsList.append(dtbuttonrow)
    dfRowsList.append(dtcompatbuttonrow)
    
    schema_table.set_title("df Schema Table")    
    
    schema_table.set_headerList(dfHeader)
    schema_table.set_widthList(dfWidths)
    schema_table.set_alignList(dfAligns)
    schema_table.set_rowList(dfRowsList)
    
    schema_table.set_tabletype(COLUMN_MAJOR)
    schema_table.set_lastcoldisplayed(current_col)
    schema_table.set_maxcolumns(len(df_cols))
    
    #print("lastcoldisplayed",schema_table.get_lastcoldisplayed(),current_col)
    
    if(display) :
        
        df_schema_html   =   get_col_major_table(schema_table,False)
        #print(df_schema_html)
        get_col_major_table(schema_table,True)
    
    else :
        
        df_schema_html   =   get_col_major_table(schema_table,False)
        return(df_schema_html)


def display_df_schema_table(display=True) : 
    """            
    #------------------------------------------------------------------
    #   display df schema data
    #
    #   df          -   dataframe
    #   display     -   display flag
    #
    #------------------------------------------------------------------
    """
 
    df_schema_table = dcTable("dataframe schema ",
                              "dfschema",
                              cfg.DataTransform_ID)
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        df_schema_table.set_colsperrow(7)
    else :
        df_schema_table.set_colsperrow(4)
        
    df_schema_table.set_rowspertable(11)
    df_schema_table.set_lastcoldisplayed(0)
    
    if(display) :
        update_df_schema_table(df_schema_table,SCROLL_RIGHT,True)
    else :
        df_schema_html   =   update_df_schema_table(df_schema_table,SCROLL_RIGHT,False)
        
        return(df_schema_html)


def display_column_transform_status(df,colname) :
    """
    * -------------------------------------------------------------------------- 
    * function : display column transform status
    * 
    * parms :
    *  df          -   data frame
    *  colname     -   column name
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    from dfcleanser.data_transform.data_transform_widgets import display_transform_col_data    
    display_transform_col_data(df,colname)


    


    
