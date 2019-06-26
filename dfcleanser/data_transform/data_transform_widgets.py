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

from dfcleanser.common.table_widgets import (dcTable, get_row_major_table, get_table_value,
                                             SCROLL_RIGHT, ROW_MAJOR, COLUMN_MAJOR,
                                             update_col_major_table_scroll, scroll_col_major_table)

from dfcleanser.common.common_utils import (get_datatype_str, display_generic_grid, RunningClock,
                                            is_datetime_col, is_date_col, is_time_col, 
                                            get_datatype_id, is_numeric_col, whitecolor, get_select_defaults)

from dfcleanser.data_inspection.data_inspection_widgets import display_inspection_data
from dfcleanser.sw_utilities.sw_utility_geocode_widgets import get_df_col_names_table

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

datetime_format_input_typeList          =   ["text","select","text","text","button","button","button","button"]

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
#--------------------------------------------------------------------------
#   timedelta radio 
#--------------------------------------------------------------------------
"""
#timedelta_radio_id                      =   "timedeltaselect"
#timedelta_radio_idList                  =   ["dtyearscid",
#                                             "dtdayscid",
#                                             "dthourscid",
#                                             "dtminutescid",
#                                             "dtsecondscid",
#                                             "dtmsecondscid",
#                                             "dttimedeltacid"]
#
#timedelta_radio_labelList               =   ["Years","Days","Hours",
#                                             "Minutes","Seconds","MicroSeconds",
#                                             "datetime.timedelta"]

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

datetime_tdelta_input_labelList         =   ["column_name_1",
                                             "column_name_2",
                                             "timedelta_column_name",
                                             "time_units",
                                             "Calculate</br> timedelta",
                                             "Clear",
                                             "Return","Help"]

datetime_tdelta_input_typeList          =   ["text","text","text","select",
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

datetime_merge_input_typeList           =   ["text","text","text","button","button","button","button"]

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

datetime_split_input_typeList           =   ["text","text","text","button","button","button","button"]

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

datetime_comp_input_typeList            =   ["text","select","text","button","button","button"]

datetime_comp_input_placeholderList     =   ["datetime column name",
                                             "date column name",
                                             "time column name",
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
    display_inspection_data()


def display_datetime_column_taskbar() :

    from dfcleanser.common.display_utils import display_dfcleanser_taskbar
    display_dfcleanser_taskbar(ButtonGroupForm(datetime_transform_tb_id,
                                               datetime_transform_tb_keyTitleList,
                                               datetime_transform_tb_jsList,
                                               False))
            
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    datetime components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_strftime_html(strftimedict) :
    """
    * ---------------------------------------------------------
    * function : get date time formats 
    * 
    * parms :
    *  strftimedict    - dicy of formats
    *
    * returns : 
    *  formats html table
    * --------------------------------------------------------
    """

    formatsHeader      =   [""]
    formatsRows        =   []
    formatsWidths      =   [100]
    formatsAligns      =   ["left"]
    formatsHrefs       =   []
    
    formats = list(strftimedict.keys())
    formats.sort()
    
    for i in range(len(strftimedict)) :
        formatsRows.append([formats[i]])
        formatsHrefs.append([None])
        formatsRows.append([str(strftimedict.get(formats[i]))])
        formatsHrefs.append(["setformat"])
        
    formats_table = None
                
    formats_table = dcTable("%s","strftimeformats",
                            cfg.DataTransform_ID,
                            formatsHeader,formatsRows,
                            formatsWidths,formatsAligns)
            
    formats_table.set_refList(formatsHrefs)
    
    formats_table.set_small(True)
    formats_table.set_smallwidth(98)
    formats_table.set_smallmargin(10)

    formats_table.set_border(True)
        
    formats_table.set_checkLength(True)
            
    formats_table.set_textLength(26)
    formats_table.set_html_only(True) 
    
    formats_table.set_tabletype(ROW_MAJOR)
    formats_table.set_rowspertable(14)

    #formats_table.dump()
    listHtml = get_row_major_table(formats_table,SCROLL_RIGHT,False)
        
    return(listHtml)


def get_possible_datetime_cols(tableid,owner,callback,callbackParms) :
    """
    * ---------------------------------------------------------
    * function : get possible 
    * 
    * parms :
    *  tableid          - table id
    *  owner            - table owner
    *  callback         - callback for column click
    *  callbackParms    - callback parms for column click
    *
    * returns : 
    *  cols name html table
    * --------------------------------------------------------
    """

    df  =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
    
    colnames            =   df.columns.values.tolist() 
    
    colnamesHeader      =   [""]
    colnamesRows        =   []
    colnamesWidths      =   [100]
    colnamesAligns      =   ["left"]
    colnamesHrefs       =   []
    
    # go through colnames and extract candidates
    for i in range(len(colnames)) :
        candidate   =   False
        
        coldt   =   get_datatype_id(df[colnames[i]].dtype)

        from dfcleanser.common.common_utils import is_integer_datatype_id,is_datetime_datatype_id
        if(is_integer_datatype_id(coldt)) :
            candidate   =   True 
        elif(is_datetime_datatype_id(coldt)) :
            candidate   =   True 
        elif( (coldt == 15) or (coldt == 16) ) :
            
            testvals    =   []
            import pandas as pd
            
            for j in range(10) :
                
                if( not (pd.isnull(df.iloc[j][colnames[i]])) ) :
                    testvals.append(df.iloc[j][colnames[i]])
                    
                    
            testdf = pd.DataFrame({'testcol':testvals})
            
            try :
                testdf['testcol'] = pd.to_datetime(testdf['testcol'])
                candidate   =   True                        
            except :
                candidate   =   False
            

        if(candidate) :        
            colnamesrow = [colnames[i]]
            colnamesRows.append(colnamesrow)
            colnamesHrefs.append([callback])
        
    colnames_table = None
                
    colnames_table = dcTable("Cols",tableid,owner,
                              colnamesHeader,colnamesRows,
                              colnamesWidths,colnamesAligns)
            
    colnames_table.set_refList(colnamesHrefs)
    
    colnames_table.set_small(True)
    colnames_table.set_smallwidth(98)
    colnames_table.set_smallmargin(2)

    colnames_table.set_border(True)
        
    colnames_table.set_checkLength(True)
    colnames_table.set_textLength(20)
    colnames_table.set_html_only(True) 
    
    colnames_table.set_tabletype(ROW_MAJOR)
    colnames_table.set_rowspertable(14)
    
    if(not (callbackParms == None)) :
        colnames_table.set_refParm(str(callbackParms))

    listHtml = get_row_major_table(colnames_table,SCROLL_RIGHT,False)

    return(listHtml)


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
        
        list_html = get_possible_datetime_cols("datetimecolnamesTable",cfg.DataTransform_ID,"get_datetime_col",None)
    else :
        
        if(len(parms) == 1) :
            
            if(parms[0] == 0) :
                dtid    =   11
            elif(parms[0] == 1) :
                dtid    =   12
            elif(parms[0] == 2) :
                dtid    =   13
                
            cfg.drop_config_value(datetime_format_input_id+"Parms")
        
            list_html = get_possible_datetime_cols("datetimecolnamesTable",cfg.DataTransform_ID,"get_datetime_col",None)
            
            dt_datetime_custom_form = InputForm(datetime_format_input_id,
                                                datetime_format_input_idList,
                                                datetime_format_input_labelList,
                                                datetime_format_input_typeList,
                                                datetime_format_input_placeholderList,
                                                datetime_format_input_jsList,
                                                datetime_format_input_reqList)
    
        else :
        
            dtid        =   11
            from dfcleanser.sw_utilities.sw_utility_control import get_Dict
            strftimedict = get_Dict("strftime")
            list_html = get_strftime_html(strftimedict) 
            
            dt_datetime_custom_form = InputForm(datetime_format_input_id,
                                                datetime_format_input_idList,
                                                datetime_format_ftypes_input_labelList,
                                                datetime_format_input_typeList,
                                                datetime_format_input_placeholderList,
                                                datetime_format_ftypes_input_jsList,
                                                datetime_format_input_reqList)
        
    parmsList = [colname,get_datatype_str(dtid),str(nanvalue),""]
    cfg.set_config_value(datetime_format_input_id+"Parms",parmsList)

    
    selectDicts     =   [] 
        
    dtsel           =   {"default":"datetime.datetime","list":["datetime.datetime","datetime.date","datetime.time",
                                                               "datetime.timedelta","numpy.datetime64","numpy.timedelta64"]}
    selectDicts.append(dtsel)
    get_select_defaults(dt_datetime_custom_form,
                        datetime_format_input_id,
                        datetime_format_input_idList,
                        datetime_format_input_typeList,
                        selectDicts)
    
    dt_datetime_custom_form.set_shortForm(True)
    dt_datetime_custom_form.set_buttonstyle({"font-size":12, "height":75, "width":65, "left-margin":8})
    dt_datetime_custom_form.set_gridwidth(310)
    dt_datetime_custom_form.set_fullparms(True)  
    
    dt_datetime_custom_html = dt_datetime_custom_form.get_html()

    dt_datetime_title_html  =   "<div>Datetime Convert Parms</div><br>"
        
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right"]
    gridhtmls       =   [dt_datetime_title_html,list_html,dt_datetime_custom_html]
    
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
    
    
    list_html = get_possible_datetime_cols("datetimecolnamesTable",cfg.DataTransform_ID,"get_deltat_col",None)
    
    dt_datetime_custom_form = InputForm(datetime_tdelta_input_id,
                                        datetime_tdelta_input_idList,
                                        datetime_tdelta_input_labelList,
                                        datetime_tdelta_input_typeList,
                                        datetime_tdelta_input_placeholderList,
                                        datetime_tdelta_input_jsList,
                                        datetime_tdelta_input_reqList)
    selectDicts     =   [] 
        
    dtsel           =   {"default":"Seconds","list":["Years","Days","Hours","Minutes","Seconds","MicroSeconds","datetime.timedelta"]}
    selectDicts.append(dtsel)
    
    get_select_defaults(dt_datetime_custom_form,
                        datetime_tdelta_input_id,
                        datetime_tdelta_input_idList,
                        datetime_tdelta_input_typeList,
                        selectDicts)

    dt_datetime_custom_form.set_shortForm(True)
    dt_datetime_custom_form.set_buttonstyle({"font-size":12, "height":78, "width":65, "left-margin":0})
    dt_datetime_custom_form.set_gridwidth(320)
    dt_datetime_custom_form.set_fullparms(True)  
    
    dt_datetime_custom_html = dt_datetime_custom_form.get_html()
    
    dt_datetime_title_html  =   "<div>Calculate Datetime.timedelta</div><br>"
        
    gridclasses     =   ["dfcleanser-common-grid-header",
                         "dfc-left","dfc-right"]
    gridhtmls       =   [dt_datetime_title_html,
                         list_html,dt_datetime_custom_html]
    print("\n")
    display_generic_grid("dtformat-delta-wrapper",gridclasses,gridhtmls)


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
        list_html = get_df_col_names_table("datetimecolnamesTable",cfg.DataTransform_ID,"get_split_col",None,None,True)
    else :
        list_html = get_df_col_names_table("datetimecolnamesTable",cfg.DataTransform_ID,"get_merge_col",None,None,True)

    
    if(action == dtm.SPLIT) :
        
        dt_datetime_custom_form = InputForm(datetime_split_input_id,
                                            datetime_split_input_idList,
                                            datetime_split_input_labelList,
                                            datetime_split_input_typeList,
                                            datetime_split_input_placeholderList,
                                            datetime_split_input_jsList,
                                            datetime_split_input_reqList)
        
        dt_datetime_custom_form.set_shortForm(True)
        dt_datetime_custom_form.set_buttonstyle({"font-size":12, "height":78, "width":65, "left-margin":0})
        dt_datetime_custom_form.set_gridwidth(320)
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
        
        dt_datetime_custom_form.set_shortForm(True)
        dt_datetime_custom_form.set_buttonstyle({"font-size":12, "height":78, "width":65, "left-margin":0})
        dt_datetime_custom_form.set_gridwidth(320)
        dt_datetime_custom_form.set_fullparms(True)  
        
        dt_datetime_custom_html = dt_datetime_custom_form.get_html()
        
        dt_datetime_title_html  =   "<div>Merge Datetime Columns</div><br>"
        
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right"]
    gridhtmls       =   [dt_datetime_title_html,list_html,dt_datetime_custom_html]
    
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
    
    list_html = get_df_col_names_table("datetimecolnamesTable",cfg.DataTransform_ID,"get_comp_col",None,None,True)
    
    dt_datetime_comps_form = InputForm(datetime_comp_input_id,
                                       datetime_comp_input_idList,
                                       datetime_comp_input_labelList,
                                       datetime_comp_input_typeList,
                                       datetime_comp_input_placeholderList,
                                       datetime_comp_input_jsList,
                                       datetime_comp_input_reqList)
    
    selectDicts     =   [] 
        
    comps           =   {"default":"Day of Week","list":["Year","Month","Day of Week","Hour"]}
    selectDicts.append(comps)
    get_select_defaults(dt_datetime_comps_form,
                        datetime_comp_input_id,
                        datetime_comp_input_idList,
                        datetime_comp_input_typeList,
                        selectDicts)
    
    dt_datetime_comps_form.set_shortForm(True)
    dt_datetime_comps_form.set_buttonstyle({"font-size":12, "height":50, "width":80, "left-margin":25})
    dt_datetime_comps_form.set_gridwidth(320)
    dt_datetime_comps_form.set_fullparms(True)  
        
    dt_datetime_comps_html = dt_datetime_comps_form.get_html()
        
    dt_datetime_title_html  =   "<div>Get Datetime Component</div><br>"
        
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right"]
    gridhtmls       =   [dt_datetime_title_html,list_html,dt_datetime_comps_html]
    
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
        
        from dfcleanser.data_inspection.data_inspection_widgets import get_select_df_form
        select_df_form              =   get_select_df_form("Transform")
    
        gridclasses     =   ["dfc-footer"]
        gridhtmls       =   [select_df_form.get_html()]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("df-select-df-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("df-select-df-pop-up-wrapper",gridclasses,gridhtmls)

    else : 
        
        funcid = parms[0][0]
        
        if(funcid == dtm.DISPLAY_DATAFRAME_TRANSFORM) :
            
            from dfcleanser.data_transform.data_transform_dataframe_widgets import display_dataframe_transform_taskbar
            display_dataframe_transform_taskbar()
            #display_inspection_data()
                
        elif(funcid == dtm.DISPLAY_COLUMNS_TRANSFORM) :
            
            from dfcleanser.data_transform.data_transform_columns_widgets import display_base_data_transform_columns_taskbar
            display_base_data_transform_columns_taskbar()
            #display_inspection_data()
            
        elif(funcid == dtm.DISPLAY_DATETIME_TRANSFORM) :
            display_datetime_column_taskbar() 
            
        elif(funcid == dtm.DISPLAY_DF_SCHEMA_TRANSFORM) :
            print("dtm.DISPLAY_DF_SCHEMA_TRANSFORM")
            display_transform_df_schema(parms)  
            
        elif(funcid == dtm.DFC_TRANSFORM_RETURN) :
            display_main_taskbar()
            
    if(clear) :
        from dfcleanser.data_transform.data_transform_process import clear_data_transform_cfg_values
        clear_data_transform_cfg_values()


def display_transform_df_schema(parms=None) :
    """
    * ---------------------------------------------------------
    * function : display df schema
    * 
    * parms :
    *  parms       -   direction
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """

    if( not(parms is None)) :
        if(len(parms[0]) > 1) : 
            direction = parms[0][1]
        else :
            direction = SCROLL_RIGHT
    else :
        direction = SCROLL_RIGHT
        

    display_main_taskbar()            
            
    print("\n")
            
    dfschema_table = get_table_value("dfschemaTable")

    if(dfschema_table == None) :
        dfschema_table = dcTable("Dataframe Schema","dfschemaTable",cfg.DataTransform_ID)
                
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            dfschema_table.set_colsperrow(6)
        else :
            dfschema_table.set_colsperrow(3)
            
    display_df_schema(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),
                      dfschema_table,direction)


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

"""
* ----------------------------------------------------------------
*       data check numneric objects
* ----------------------------------------------------------------
""" 

chknum_col_html     =   """                                    <tr><br></tr>
                                    <tr>
                                        <div>
                                            <p width=80%;>---------------------------------------</p>
                                        </div>
                                    </tr>
                                    <tr><br></tr>
                                    <tr>
                                        <div class="input-group mb-3 dc-schema-dlist">
                                            <div class="dc-schema-dlist-div">
                                                <label class="dc-schema-dlist-label" for="XXXXcolselId">Check For</label>
                                                <select class="custom-select" id="XXXXcolselId">
                                                    <option selected  value="0">int</option>
                                                    <option  value="1">float</option>
                                                </select>
                                            </div>
                                        </div>
                                    </tr>
                                    <tr><br></tr>
                                    <tr>
                                        <div class='container dc-container dc-default-input-inner-div'>        
                                            <div class='form-group-sm'>
                                                <label  for="csvdftitle" style="text-align:left; font-size: 11px;">Sample Size (%)&nbsp;</label>
                                                <input  type="text" class="form-control" style="text-align:left; font-size: 11px;" id="csvdftitle" placeholder="dataframe title (default '100')" value="100"></input>
                                            </div>
                                        </div>
                                    </tr>
                                    <tr><br></tr>
                                    <tr>
                                        <div class="dc-schema-dlist-div">
                                            <p style='font-weight:bold;'>Check Status:</p>
                                        </div>
                                        <div>
                                            <p id="XXXXstatmsg" style='border:1px solid #428bca; background-color: #F8F5E1; width=80%;'>XXXXstatus</p>
                                            </div>
                                    </tr>
                                    <tr><br></tr>
                                    <tr>
                                        <div class="dc-schema-input-div">
                                            <button type="button" class="btn btn-grp dc-schema-button" id="XXXXbutton" style='font-size: 12px; height: 50px; color:white; background-color: #67a1f3;' onClick="XXXXcallback" XXXXdisabled>Check for</br>Numeric</button>
                                        </div>
                                    </tr>
"""


def get_df_chknum_col(colname,status=dtm.UNKNOWN_STATUS) : 

    current_html    =   ""
    
    current_html    =     chknum_col_html[0:] 
    current_html    =     current_html.replace("XXXXcolselId",colname + "colselId")
    current_html    =     current_html.replace("XXXXstatmsg",colname + "statmsg")
    current_html    =     current_html.replace("XXXXbutton",colname + "button")
    current_html    =     current_html.replace("XXXXcallback","col_checknum('" + colname + "')")
    
    if(status==dtm.UNKNOWN_STATUS) :
        current_html    =     current_html.replace("XXXXstatus",dtm.UNKNOWN_TEXT)
        current_html    =     current_html.replace("XXXXdisbaled"," ")
    else :
        if((status==dtm.INT_STATUS) or () ) :
            current_html    =     current_html.replace("XXXXdisabled","disabled")  
        else :
            current_html    =     current_html.replace("XXXXdisabled"," ")
        
        if(status==dtm.INT_STATUS) :
            current_html    =     current_html.replace("XXXXstatus",dtm.INT_TEXT)
        elif(status==dtm.FLOAT_STATUS) :
            current_html    =     current_html.replace("XXXXstatus",dtm.FLOAT_TEXT)
        elif(status==dtm.NOT_INT_STATUS) :
            current_html    =     current_html.replace("XXXXstatus",dtm.NOT_INT_TEXT)
        elif(status==dtm.NOT_FLOAT_STATUS) :
            current_html    =     current_html.replace("XXXXstatus",dtm.NOT_FLOAT_TEXT)
    

    if(colname.find("#Location") > -1) :
        print(current_html)
       
    return(current_html)


"""
* -----------------------------------------------------------------------*
* Dataframe Schema Table html 
* -----------------------------------------------------------------------*
"""
schema_col_table_start = """
                            <div class="dc-schema-col-container">
                                <table class="table table-bordered">"""
schema_col_table_end = """                                </table>
                            </div>
                        """

schema_col_datatype_row_start = """
                                    <tr>
                                        <div class="input-group mb-3 dc-schema-dlist">
                                            <div class="dc-schema-dlist-div">
                                                <label class="dc-schema-dlist-label" for="dfschselXXXX">datatype</label>
                                                <select class="custom-select"  id="dfschselXXXX">
"""

schema_col_datatype_row_end = """                                                </select>
                                            </div>
                                        </div>
                                    </tr>
                                    <tr><br></tr>
"""


schema_col_nancount_row = """                                    <tr>
                                        <div class="dc-schema-dlist-div">
                                            <p style='font-weight:bold;'>Nan Count:</p>
                                        </div>
                                        <div width=90px;>
                                            <p id="nancountid" style='border:1px solid #428bca; background-color: #F8F5E1;' width=90px;>&nbsp;&nbsp;XXXXnancount</p>
                                        </div>
                                    </tr>
"""

schema_col_uniques_row = """                                    <tr>
                                        <div class="dc-schema-dlist-div">
                                            <p style='font-weight:bold;'>Uniques Count:</p>
                                        </div>
                                        <div width=90px;>
                                            <p id="uniquecountid" style='border:1px solid #428bca; background-color: #F8F5E1;' width=90px;>&nbsp;&nbsp;XXXXuniquecount</p>
                                        </div>
                                    </tr>
"""

schema_col_button_row = """
                                     <tr>
                                        <div class="dc-schema-input-div">
                                            <button type="button" class="btn btn-grp dc-schema-button" style='font-size: 12px; height: 50px; color:white; background-color: #67a1f3;' onClick="dfsch_changedt('XXXXcolname')" >Change</br>Datatype</button>
                                        </div>
                                     </tr>
"""

def get_df_schema_table_col(df,colname,datatypeId,nancount,uniquescount) : 
    """
    * -------------------------------------------------------------------------- 
    * function : get dataframe schema table
    * 
    * parms :
    *   col_name       -   column name
    *   datatypeId     -   col datatype 
    *   nancount       -   col nancount 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    from dfcleanser.common.html_widgets import addattribute, new_line
    
    df_schema_HTML  =   ""
    df_schema_HTML  =   (df_schema_HTML + schema_col_table_start)


    # display datatype table select row
    df_schema_HTML  =   (df_schema_HTML + schema_col_datatype_row_start)
    df_schema_HTML  =   df_schema_HTML.replace("dfschselXXXX","dfschsel" + colname)

    from dfcleanser.common.common_utils import get_datatype_str
    
    num_dtypes      =   21

    for i in range(num_dtypes) :
        df_schema_HTML  =   (df_schema_HTML + "                                                    <option ")
        if(i == datatypeId) :
            df_schema_HTML  =   (df_schema_HTML + "selected ") 
        df_schema_HTML  =   (df_schema_HTML + addattribute("value",str(i))+">")
        df_schema_HTML  =   (df_schema_HTML + get_datatype_str(i) + "</option>" + new_line)
    
    df_schema_HTML  =   (df_schema_HTML + schema_col_datatype_row_end)

    df_schema_HTML  =   (df_schema_HTML + schema_col_nancount_row)
    df_schema_HTML  =   df_schema_HTML.replace("XXXXnancount",str(nancount))
    
    df_schema_HTML  =   (df_schema_HTML + schema_col_uniques_row)
    df_schema_HTML  =   df_schema_HTML.replace("XXXXuniquecount",str(uniquescount))
    
    # display nan table button row
    df_schema_HTML  =   (df_schema_HTML + schema_col_button_row)
    df_schema_HTML  =   df_schema_HTML.replace("XXXXcolname",colname)
    
    from dfcleanser.common.common_utils import is_string_col, is_object_col
    if ( (is_string_col(df,colname)) or (is_object_col(df,colname)) ) :
       
        precheck    =   dtm.checknum_status.get_col_status(colname) 
        
        if(not (precheck is None)) :
            df_schema_HTML  =   (df_schema_HTML + get_df_chknum_col(colname)) 
        else :
            df_schema_HTML  =   (df_schema_HTML + get_df_chknum_col(colname,precheck))    
    
    df_schema_HTML  =   (df_schema_HTML + schema_col_table_end)

    if( (colname == "#DR Number") or (colname == "#Area ID") ):
        print(df_schema_HTML)

    return(df_schema_HTML)

def get_df_schema_table(df,table) : 
    """
    * ---------------------------------------------------------
    * function : display transform col data
    * 
    * parms :
    *  df          -   dataframe
    *  table       -   dfc table
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """

    if( (dtm.schema_dict.get_df_title() == None) or 
        (not (dtm.schema_dict.get_df_title() == cfg.get_current_dfc_dataframe_title())) ):
        
        df_cols     =   df.columns.tolist()
        df_dtypes   =   df.dtypes.tolist()
        
        df_nans     =   []
        df_uniques  =   []
        
        for i in range(len(df_cols)) :
            nans     =   df[df_cols[i]].isnull().sum()
            df_nans.append(nans)
            uniques     =   df[df_cols[i]].unique().tolist()
            df_uniques.append(len(uniques))
        
        df_title    =   cfg.get_current_dfc_dataframe_title()
        
        schema_dict =   {"df_title":df_title, "df_cols":df_cols, "df_dtypes":df_dtypes, "df_nans":df_nans, "df_uniques":df_uniques}
        dtm.schema_dict.reload_dfschema_stats(schema_dict)
        
    else :
        
        df_cols     =   dtm.schema_dict.get_col_list()
        df_dtypes   =   dtm.schema_dict.get_col_dtypes()
        df_nans     =   dtm.schema_dict.get_col_nans()
        df_uniques  =   dtm.schema_dict.get_col_uniques()
            
    colstart = table.get_lastcoldisplayed() + 1
    
    dfHeaderList    =   []
    dfRowsList      =   []
    dfWidthsList    =   []
    dfAlignsList    =   []
    dfchrefsList    =   []

    dfRow   =   []
    
    for i in range(table.get_colsperrow()) :
        
        if((i+colstart) < len(df_cols)) :
            
            dfHeaderList.append(df_cols[i + colstart])
            
            colHTML     =  get_df_schema_table_col(df,
                                                   df_cols[i + colstart],
                                                   get_datatype_id(df_dtypes[i + colstart]),
                                                   df_nans[i + colstart],
                                                   df_uniques[i + colstart]) 
            dfRow.append(colHTML)
        else :
            dfHeaderList.append("")
            dfRow.append("&nbsp;")

    dfRowsList.append(dfRow)
    
    if(cfg.get_dfc_mode() == cfg.POP_UP_MODE) :
        table.set_small(True)
        table.set_smallwidth(98)
        table.set_smallmargin(2)
    
    for i in range(table.get_colsperrow())  :
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            dfWidthsList.append(16)
        else :
            dfWidthsList.append(32)
            
        dfAlignsList.append("center")
        dfchrefsList.append("dfscleansecol")
        
    table.set_title("Dataframe Schema")    
    
    table.set_headerList(dfHeaderList)
    table.set_widthList(dfWidthsList)
    table.set_alignList(dfAlignsList)
    table.set_hhrefList(None)
    table.set_rowList(dfRowsList)
    table.set_hhrefList(dfchrefsList)    
    
    table.set_tabletype(COLUMN_MAJOR)
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        table.set_colsperrow(6)
    else :
        table.set_colsperrow(3)
    table.set_maxcolumns(len(df_cols))
    table.set_checkLength(False) 
    
    update_col_major_table_scroll(table)

    
def display_df_schema(df,table,direction=SCROLL_RIGHT,display=True) : 
    """
    * ---------------------------------------------------------
    * function : display df schema
    * 
    * parms :
    *  df          -   dataframe
    *  table       -   dfc table
    *  direction   -   scroll direction
    *  display     -   display flag
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """

    scroll_col_major_table(table,direction)

    clock = RunningClock()
    clock.start()
        
    get_df_schema_table(df,table)
    
    schema_html     =   table.get_html()
    
    gridclasses     =   ["dfc-top"]
    gridhtmls       =   [schema_html]
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("dataframe-schema-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("dataframe-schema-pop-up-wrapper",gridclasses,gridhtmls)
    
    clock.stop()
    
    if( table.get_lastcoldisplayed() >= table.get_maxcolumns() ) :
        table.set_lastcoldisplayed(-1)
   



    


    
