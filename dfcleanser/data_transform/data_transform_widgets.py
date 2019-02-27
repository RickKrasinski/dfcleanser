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

from dfcleanser.common.html_widgets import (display_composite_form, get_button_tb_form, get_html_spaces,
                                            get_input_form, get_header_form, ButtonGroupForm,
                                            get_radio_button_form, RadioGroupForm, InputForm) 

from dfcleanser.common.table_widgets import (dcTable, get_row_major_table, get_table_value,
                                             SCROLL_NEXT, ROW_MAJOR, SCROLL_PREVIOUS, COLUMN_MAJOR)

from dfcleanser.common.common_utils import (get_datatype_str, display_generic_grid, RunningClock,
                                            is_datetime_column, is_date_column, is_time_column, 
                                            get_datatype_id, is_numeric_col, whitecolor)

from dfcleanser.data_inspection.data_inspection_widgets import display_inspection_data

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
                                                 "Clear","Help"]

data_transform_tb_jsList                    =   ["transform_task_bar_callback("+str(dtm.DISPLAY_DATAFRAME_TRANSFORM)+")",
                                                 "transform_task_bar_callback("+str(dtm.DISPLAY_COLUMNS_TRANSFORM)+")",
                                                 "transform_task_bar_callback("+str(dtm.DISPLAY_DATETIME_TRANSFORM)+")",
                                                 "transform_task_bar_callback("+str(dtm.DISPLAY_DF_SCHEMA_TRANSFORM)+")",
                                                 "transform_task_bar_callback("+str(dtm.DFC_TRANSFORM_RETURN)+")",
                                                 "displayhelp(" + str(dfchelp.TRANSFORM_MAIN_TASKBAR_ID) + ")"]

"""
#--------------------------------------------------------------------------
#    single column transform task bar - called externally
#--------------------------------------------------------------------------
"""
single_col_cat_tb_doc_title        =   ""
single_col_cat_tb_title            =   ""
single_col_cat_tb_id               =   "singlecolcatoptionstb"

single_col_cat_tb_keyList          =   ["Map","Dummies","Categories",
                                        "Return","Help"]

single_col_cat_tb_jsList           =   ["single_col_categorical_callback(2)",
                                        "single_col_categorical_callback(3)",
                                        "single_col_categorical_callback(4)",
                                        "single_col_categorical_callback(5)",
                                        "displayhelp(" + str(dfchelp.TRANSFORM_COLS_MDC_ID) + ")"]

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
                                                 "Return","Help"]

datetime_transform_tb_jsList                =   ["dt_transform_task_bar_callback("+str(dtm.DISPLAY_DATETIME_DATATYPE)+")",
                                                 "dt_transform_task_bar_callback("+str(dtm.DISPLAY_TIMEDELTA)+")",
                                                 "dt_transform_task_bar_callback("+str(dtm.DISPLAY_DATETIME_SPLIT)+")",
                                                 "dt_transform_task_bar_callback("+str(dtm.DISPLAY_DATETIME_MERGE)+")",
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
                                             None,None,None,None,None]

datetime_format_input_labelList         =   ["column_name",
                                             "datetime_datatype",
                                             "nan_fill_value",
                                             "format_string",
                                             "Change</br> DataType",
                                             "Get</br>formats",
                                             "Clear",
                                             "Return","Help"]

datetime_format_input_typeList          =   ["text","text","text","text","button","button","button","button","button"]

datetime_format_input_placeholderList   =   ["column name",
                                             "datetime datatype",
                                             "nat fill value (default = None - NaT)",
                                             "format string to use (default = auto detect * very slow)",
                                             None,None,None,None,None]

datetime_format_input_jsList            =   [None,None,None,None,
                                             "process_datetime_format_transform_callback(0)",
                                             "process_datetime_format_transform_callback(1)",
                                             "process_datetime_format_transform_callback(2)",
                                             "process_datetime_format_transform_callback(3)",
                                             "displayhelp(" + str(dfchelp.TRANSFORM_MAIN_TASKBAR_ID) + ")"]

datetime_format_input_reqList           =   [0,1,2]

"""
#--------------------------------------------------------------------------
#   timedelta radio 
#--------------------------------------------------------------------------
"""
timedelta_radio_id                      =   "timedeltaselect"
timedelta_radio_idList                  =   ["dtyearscid",
                                             "dtdayscid",
                                             "dthourscid",
                                             "dtminutescid",
                                             "dtsecondscid",
                                             "dtmsecondscid",
                                             "dttimedeltacid"]

timedelta_radio_labelList               =   ["Years","Days","Hours",
                                             "Minutes","Seconds","MicroSeconds",
                                             "datetime.timedelta"]

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
                                             None,None,None,None]

datetime_tdelta_input_labelList         =   ["column_name_1",
                                             "column_name_2",
                                             "timedelta_column_name",
                                             "Calculate</br> timedelta",
                                             "Clear",
                                             "Return","Help"]

datetime_tdelta_input_typeList          =   ["text","text","text","button","button","button","button"]

datetime_tdelta_input_placeholderList   =   ["first column name",
                                             "second column name",
                                             "time delta column name",
                                              None,None,None,None]

datetime_tdelta_input_jsList            =   [None,None,None,
                                             "process_datetime_tdelta_callback(0)",
                                             "process_datetime_tdelta_callback(1)",
                                             "process_datetime_tdelta_callback(2)",
                                             "displayhelp(" + str(dfchelp.TRANSFORM_MAIN_TASKBAR_ID) + ")"]

datetime_tdelta_input_reqList           =   [0,1,2]

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
    display_composite_form([get_button_tb_form(ButtonGroupForm(data_transform_tb_id,
                                                               data_transform_tb_keyTitleList,
                                                               data_transform_tb_jsList,
                                                               False))])

def display_no_dataframe() :
        
    display_composite_form([get_button_tb_form(ButtonGroupForm(data_transform_tb_id,
                                                               data_transform_tb_keyTitleList,
                                                               data_transform_tb_jsList,
                                                               False))])
    
def display_transform_columns_taskbar() :
    
    from dfcleanser.data_transform.data_transform_columns_widgets import display_data_transform_columns_taskbar
    display_data_transform_columns_taskbar()
    display_inspection_data()

def display_single_column_taskbar() :
    
    display_composite_form([get_button_tb_form(ButtonGroupForm(single_col_cat_tb_id,
                                                               single_col_cat_tb_keyList,
                                                               single_col_cat_tb_jsList,
                                                               True))])

def display_mapping_column_taskbar() :

    from dfcleanser.data_transform.data_transform_columns_widgets import display_data_transform_columns_taskbar
    display_data_transform_columns_taskbar()
    display_composite_form([get_header_form("&nbsp;&nbsp;&nbsp;Column Mapping")])

def display_dummies_column_taskbar() :

    from dfcleanser.data_transform.data_transform_columns_widgets import display_data_transform_columns_taskbar
    display_data_transform_columns_taskbar()
    display_composite_form([get_header_form("&nbsp;&nbsp;&nbsp;Column Dummies")])

def display_dummies_column_input() :

    from dfcleanser.data_transform.data_transform_columns_widgets import transform_dummy_input_form
    display_composite_form([get_input_form(transform_dummy_input_form)])

def display_cats_column_taskbar() :
    
    from dfcleanser.data_transform.data_transform_columns_widgets import display_data_transform_columns_taskbar
    display_data_transform_columns_taskbar()
    display_composite_form([get_header_form("&nbsp;&nbsp;&nbsp;Column Categories")])

def display_cats_column_input() :
    
    from dfcleanser.data_transform.data_transform_columns_widgets import transform_category_input_form
    display_composite_form([get_input_form(transform_category_input_form)])

def display_datetime_column_taskbar() :

    display_composite_form([get_button_tb_form(ButtonGroupForm(datetime_transform_tb_id,
                                                               datetime_transform_tb_keyTitleList,
                                                               datetime_transform_tb_jsList,
                                                               False))])
            
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    datetime components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    get datetime formats html
#--------------------------------------------------------------------------
""" 
def get_strftime_html(strftimedict) :

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
                
    formats_table = dcTable("Datetime Formats","strftimeformats",
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
    listHtml = get_row_major_table(formats_table,SCROLL_NEXT,False)
        
    return(listHtml)

"""
#--------------------------------------------------------------------------
#    display datetime convert inputs
#--------------------------------------------------------------------------
"""     
def display_datetime_convert(parms=None) :

    datetime_radio     =   RadioGroupForm(datetime_radio_form)
    datetime_radio.set_checked(0)
    display_composite_form([get_radio_button_form(datetime_radio)])
    
    dtid        =   ""
    colname     =   ""
    nanvalue    =   ""
    
    if(parms == None) :
        cfg.drop_config_value(datetime_format_input_id+"Parms")
        
        from dfcleanser.sw_utilities.sw_utility_geocode_widgets import get_df_col_names_table
        list_html = get_df_col_names_table("datetimecolnamesTable",cfg.DataTransform_ID,"get_datetime_col",None,True)
    else :
        if(len(parms) == 1) :
            if(parms[0] == 0) :
                dtid    =   11
            elif(parms[0] == 1) :
                dtid    =   12
            else :    
                dtid    =   13
                
            cfg.drop_config_value(datetime_format_input_id+"Parms")
        
            from dfcleanser.sw_utilities.sw_utility_geocode_widgets import get_df_col_names_table
            list_html = get_df_col_names_table("datetimecolnamesTable",cfg.DataTransform_ID,"get_datetime_col",None,True)
    
        else :
            dtid        =   11
            colname     =   parms[1]
            nanvalue    =   parms[2]
        
            from dfcleanser.sw_utility.sw_utility_widgets import get_Dict
            strftimedict = get_Dict("strftime")
            list_html = get_strftime_html(strftimedict)
    
    parmsList = [colname,get_datatype_str(dtid),str(nanvalue),""]
    cfg.set_config_value(datetime_format_input_id+"Parms",parmsList)

    dt_datetime_custom_form = InputForm(datetime_format_input_id,
                                        datetime_format_input_idList,
                                        datetime_format_input_labelList,
                                        datetime_format_input_typeList,
                                        datetime_format_input_placeholderList,
                                        datetime_format_input_jsList,
                                        datetime_format_input_reqList)
    
    dt_datetime_custom_form.set_shortForm(False)
    dt_datetime_custom_form.set_gridwidth(640)    
    dt_datetime_custom_form.set_fullparms(True)    
    
    dt_datetime_custom_html = dt_datetime_custom_form.get_html()

    dt_datetime_title_html  =   "<p>" + get_html_spaces(50) + "Datetime Convert Parms </p>"
        
    gridclasses     =   ["dtformat-wrapper-header","dfc-right","dfc-left"]
    gridhtmls       =   [dt_datetime_title_html,list_html,dt_datetime_custom_html]
    
    display_generic_grid("dtformat-wrapper",gridclasses,gridhtmls)


"""
#--------------------------------------------------------------------------
#    display datetime timedelta inputs
#--------------------------------------------------------------------------
""" 
def display_datetime_timedelta(parms)  :
    
    timedelta_radio     =   RadioGroupForm(timedelta_radio_id,
                                           timedelta_radio_idList,
                                           timedelta_radio_labelList)
    timedelta_radio.set_checked(4)
    display_composite_form([get_radio_button_form(timedelta_radio)])
    print("\n")
    
    from dfcleanser.sw_utilities.sw_utility_geocode_widgets import get_df_col_names_table
    list_html = get_df_col_names_table("datetimecolnamesTable",cfg.DataTransform_ID,"get_deltat_col",None,True)

    dt_datetime_custom_form = InputForm(datetime_tdelta_input_id,
                                        datetime_tdelta_input_idList,
                                        datetime_tdelta_input_labelList,
                                        datetime_tdelta_input_typeList,
                                        datetime_tdelta_input_placeholderList,
                                        datetime_tdelta_input_jsList,
                                        datetime_tdelta_input_reqList)
    
    dt_datetime_custom_form.set_shortForm(False) 
    dt_datetime_custom_form.set_gridwidth(640)
    dt_datetime_custom_form.set_fullparms(True) 
    dt_datetime_custom_html = dt_datetime_custom_form.get_html()
    
    dt_datetime_title_html  =   "<p>" + get_html_spaces(50) + "Calculate Datetime.timedelta </p>"
        
    gridclasses     =   ["dtformat-wrapper-header","dfc-right","dfc-left"]
    gridhtmls       =   [dt_datetime_title_html,list_html,dt_datetime_custom_html]
    
    display_generic_grid("dtformat-wrapper",gridclasses,gridhtmls)


"""
#--------------------------------------------------------------------------
#    display datetime merge/split inputs
#--------------------------------------------------------------------------
"""     
def display_datetime_split_merge(parms,action) :
    
    from dfcleanser.sw_utilities.sw_utility_geocode_widgets import get_df_col_names_table
    if(action == dtm.SPLIT) :
        list_html = get_df_col_names_table("datetimecolnamesTable",cfg.DataTransform_ID,"get_split_col",None,True)
    else :
        list_html = get_df_col_names_table("datetimecolnamesTable",cfg.DataTransform_ID,"get_merge_col",None,True)

    dt_datetime_custom_form = InputForm(datetime_tdelta_input_id,
                                        datetime_tdelta_input_idList,
                                        datetime_tdelta_input_labelList,
                                        datetime_tdelta_input_typeList,
                                        datetime_tdelta_input_placeholderList,
                                        datetime_tdelta_input_jsList,
                                        datetime_tdelta_input_reqList)
    
    dt_datetime_custom_form.set_shortForm(False) 
    dt_datetime_custom_form.set_gridwidth(640)
    dt_datetime_custom_form.set_fullparms(True) 
    dt_datetime_custom_html = dt_datetime_custom_form.get_html()
    
    if(action == dtm.SPLIT) :
        
        dt_datetime_custom_form = InputForm(datetime_split_input_id,
                                            datetime_split_input_idList,
                                            datetime_split_input_labelList,
                                            datetime_split_input_typeList,
                                            datetime_split_input_placeholderList,
                                            datetime_split_input_jsList,
                                            datetime_split_input_reqList)
        
        dt_datetime_custom_form.set_shortForm(False)
        dt_datetime_custom_form.set_gridwidth(640)
        dt_datetime_custom_form.set_fullparms(True)
        dt_datetime_custom_html = dt_datetime_custom_form.get_html()

        dt_datetime_title_html  =   "<p>" + get_html_spaces(50) + "Split Datetime Column Parameters </p>"
        
    else :
        
        dt_datetime_custom_form = InputForm(datetime_merge_input_id,
                                            datetime_merge_input_idList,
                                            datetime_merge_input_labelList,
                                            datetime_merge_input_typeList,
                                            datetime_merge_input_placeholderList,
                                            datetime_merge_input_jsList,
                                            datetime_merge_input_reqList)
        
        dt_datetime_custom_form.set_shortForm(False)
        dt_datetime_custom_form.set_gridwidth(640)
        dt_datetime_custom_form.set_fullparms(True)
        dt_datetime_custom_html = dt_datetime_custom_form.get_html()
        
        dt_datetime_title_html  =   "<p>" + get_html_spaces(50) + "Merge Datetime Column </p>"
        
    gridclasses     =   ["dtformat-wrapper-header","dfc-right","dfc-left"]
    gridhtmls       =   [dt_datetime_title_html,list_html,dt_datetime_custom_html]
    
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

    if(parms == None) :
            
        data_transform_forms  =   [get_button_tb_form(ButtonGroupForm(data_transform_tb_id,
                                                                      data_transform_tb_keyTitleList,
                                                                      data_transform_tb_jsList,
                                                                      False))]

        display_composite_form(data_transform_forms)
        
        from dfcleanser.data_inspection.data_inspection_widgets import get_select_df_form
        select_df_form              =   get_select_df_form("Transform")
    
        gridclasses     =   ["dfc-footer"]
        gridhtmls       =   [select_df_form.get_html()]
    
        display_generic_grid("df-select-df-wrapper",gridclasses,gridhtmls)


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

            display_composite_form([get_button_tb_form(ButtonGroupForm(datetime_transform_tb_id,
                                                                       datetime_transform_tb_keyTitleList,
                                                                       datetime_transform_tb_jsList,
                                                                       False))])
        
        elif(funcid == dtm.DISPLAY_DF_SCHEMA_TRANSFORM) :
            
            if(len(parms[0]) > 1) : 
                direction = parms[0][1]
            else :
                direction = SCROLL_NEXT

            display_composite_form([get_button_tb_form(ButtonGroupForm(data_transform_tb_id,
                                                                       data_transform_tb_keyTitleList,
                                                                       data_transform_tb_jsList,
                                                                       False))])
            print("\n")
            dfschema_table = get_table_value("dfschemaTable")

            if(dfschema_table == None) :
                dfschema_table = dcTable("Dataframe Schema","dfschemaTable",cfg.DataTransform_ID)
                dfschema_table.set_colsperrow(6)
            
            display_df_schema(cfg.get_dfc_dataframe(),dfschema_table,direction)

        elif(funcid == dtm.DFC_TRANSFORM_RETURN) :
                    
            display_composite_form([get_button_tb_form(ButtonGroupForm(data_transform_tb_id,
                                                                          data_transform_tb_keyTitleList,
                                                                          data_transform_tb_jsList,
                                                                          False))])

    if(clear) :
        from dfcleanser.data_transform.data_transform_process import clear_data_transform_cfg_values
        clear_data_transform_cfg_values()

"""            
#------------------------------------------------------------------
#   display_col_stats
#
#   df          -   dataframe
#   colname     -   column name 
#   numeric     -   numeric column flag
#
#------------------------------------------------------------------
"""
def display_col_data(df,colname,display=True) :

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
    
    if(is_datetime_column(df,colname)) :
        typestr = get_datatype_str(11)
    elif(is_date_column(df,colname)) :
        typestr = get_datatype_str(12)
    elif(is_time_column(df,colname)) :
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
    stats_table.set_smallfsize(12)
    stats_table.set_border(False)
    stats_table.set_checkLength(False)
    
    if(display) :
        stats_table.display_table()
    else :
        return(stats_table.get_html())



"""            
#------------------------------------------------------------------
#   get dataframe schema table
#
#   df              -   dataframe
#
#------------------------------------------------------------------
"""
def get_df_schema_table(df,table) : 
   
    
    schema_parms    =   cfg.df_schema_dict 
    
    if( (schema_parms == None) or 
        (not (schema_parms.get("df_title",None) == cfg.get_current_dfc_dataframe_title())) ):
        
        df_cols     =   df.columns.tolist()
        df_dtypes   =   df.dtypes.tolist()
        df_nans     =   df.isnull().sum()
        df_title    =   cfg.get_current_dfc_dataframe_title()
        
        schema_dict =   {"df_title":df_title, "df_cols":df_cols, "df_dtypes":df_dtypes, "df_nans":df_nans}
        cfg.df_schema_dict  =   schema_dict
        
    else :
        df_cols     =   schema_parms.get("df_cols",None)
        df_dtypes   =   schema_parms.get("df_dtypes",None)
        df_nans     =   schema_parms.get("df_nans",None)
            
    colstart = table.get_lastcoldisplayed() + 1
    
    dfHeaderList    =   []
    dfRowsList      =   []
    dfWidthsList    =   []
    dfAlignsList    =   []
    dfchrefsList    =   []

    dfRow   =   []
    
    print("get_df_schema_table : colstart",colstart)
    
    from dfcleanser.common.table_widgets import get_df_schema_table_col
    for i in range(table.get_colsperrow()) :
        if((i+colstart) < len(df_cols)) :
            dfHeaderList.append(df_cols[i + colstart])
            
            colHTML     =  get_df_schema_table_col(df_cols[i + colstart],
                                                   get_datatype_id(df_dtypes[i + colstart]),
                                                   df_nans[i + colstart]) 
            dfRow.append(colHTML)
        else :
            dfRow.append("&nbsp;")

    dfRowsList.append(dfRow)
    
    for i in range(table.get_colsperrow())  :
        dfWidthsList.append(16)
        dfAlignsList.append("center")
        dfchrefsList.append("scol")
        
    table.set_title("Dataframe Schema")    
    
    table.set_headerList(dfHeaderList)
    table.set_widthList(dfWidthsList)
    table.set_alignList(dfAlignsList)
    table.set_hhrefList(None)
    table.set_rowList(dfRowsList)
    table.set_hhrefList(dfchrefsList)    
    
    table.set_tabletype(COLUMN_MAJOR)
    table.set_colsperrow(6)
    table.set_maxcolumns(len(df_cols))
    table.set_checkLength(False) 
    table.set_lastcoldisplayed(table.get_lastcoldisplayed() + table.get_colsperrow())
    
"""            
#------------------------------------------------------------------
#   display dataframe schema
#
#   df              -   dataframe
#
#------------------------------------------------------------------
"""
def display_df_schema(df,table,direction=SCROLL_NEXT,display=True) : 

    if(direction == SCROLL_PREVIOUS) :
        if((table.get_lastcoldisplayed() + 1) >= table.get_colsperrow()) :
            if( (table.get_lastcoldisplayed() + 1) == table.get_colsperrow()) :
                table.set_lastcoldisplayed(-1) 
            else :
                table.set_lastcoldisplayed(table.get_lastcoldisplayed()-(2*table.get_colsperrow()))
                if(table.get_lastcoldisplayed() < 0) :
                    table.set_lastcoldisplayed(-1)
    
    clock = RunningClock()
    clock.start()
        
    get_df_schema_table(df,table)
    table.display_table() 
    
    clock.stop()
    
    if( table.get_lastcoldisplayed() >= table.get_maxcolumns() ) :
        table.set_lastcoldisplayed(-1)
   



    
