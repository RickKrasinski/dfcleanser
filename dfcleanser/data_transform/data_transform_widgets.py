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

from dfcleanser.common.table_widgets import (dcTable)

from dfcleanser.common.common_utils import (get_dtype_str_for_datatype, display_generic_grid, display_status_note,
                                            is_numeric_col, whitecolor, get_select_defaults, get_parms_for_input)

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

data_transform_tb_keyTitleList              =   ["dataframe</br>Transform",
                                                 "columns</br>Transform",
                                                 "datetime</br>Transform",
                                                 "Clear","Reset","Help"]

data_transform_tb_jsList                    =   ["transform_task_bar_callback("+str(dtm.DISPLAY_DATAFRAME_TRANSFORM)+")",
                                                 "transform_task_bar_callback("+str(dtm.DISPLAY_COLUMNS_TRANSFORM)+")",
                                                 "transform_task_bar_callback("+str(dtm.DISPLAY_DATETIME_TRANSFORM)+")",
                                                 "transform_task_bar_callback("+str(dtm.DFC_TRANSFORM_RETURN)+")",
                                                 "process_pop_up_cmd(6)",
                                                 "displayhelp('" + str(dfchelp.TRANSFORM_MAIN_TASKBAR_ID) + "')"]

data_transform_tb_centered                  =   True


"""
#--------------------------------------------------------------------------
#    data transform pop-up task bars
#--------------------------------------------------------------------------
"""
data_transform_tbA_doc_title                =   "Transform Options"
data_transform_tbA_title                    =   "Transform Options"
data_transform_tbA_id                       =   "transformoptionstbA"

data_transform_tbA_keyTitleList             =   ["dataframe</br>Transform",
                                                 "Columns</br>Transform",
                                                 "datetime</br>Transform"]

data_transform_tbA_jsList                   =   ["transform_task_bar_callback("+str(dtm.DISPLAY_DATAFRAME_TRANSFORM)+")",
                                                 "transform_task_bar_callback("+str(dtm.DISPLAY_COLUMNS_TRANSFORM)+")",
                                                 "transform_task_bar_callback("+str(dtm.DISPLAY_DATETIME_TRANSFORM)+")"]

data_transform_tbA_centered                 =   True

data_transform_tbB_doc_title                =   "Transform Options"
data_transform_tbB_title                    =   "Transform Options"
data_transform_tbB_id                       =   "transformoptionstbB"

data_transform_tbB_keyTitleList             =   ["Clear","Reset","Help"]

data_transform_tbB_jsList                   =   ["transform_task_bar_callback("+str(dtm.DFC_TRANSFORM_RETURN)+")",
                                                 "process_pop_up_cmd(6)",
                                                 "displayhelp('" + str(dfchelp.TRANSFORM_MAIN_TASKBAR_ID) + "')"]

data_transform_tbB_centered                 =   True


"""
#--------------------------------------------------------------------------
#    datetime transform task bar
#--------------------------------------------------------------------------
"""
datetime_transform_tb_doc_title             =   "datetime Transform Options"
datetime_transform_tb_title                 =   "datetime Transform Options"
datetime_transform_tb_id                    =   "datetimetransformoptionstb"

datetime_transform_tb_keyTitleList          =   ["Convert</br>Column</br>to</br>datetime",
                                                 "Convert</br>Column</br>to</br>timedelta",
                                                 "Calculate</br>timedelta</br>Column",
                                                 "Split</br>Column</br>to</br>date,time</br>Columns",
                                                 "Merge</br>Column</br>from</br>date,time</br>Columns",
                                                 "Get</br>datetime</br>Components</br>Column",
                                                 "Return","Help"]

datetime_transform_tb_jsList                =   ["dt_datetime_transform_task_bar_callback(" + str(dtm.DISPLAY_DATETIME_OPTION)+")",
                                                 "dt_datetime_transform_task_bar_callback(" + str(dtm.DISPLAY_DATETIME_TIMEDELTA_OPTION)+")",
                                                 "dt_datetime_transform_task_bar_callback(" + str(dtm.DISPLAY_TIMEDELTA_CALCULATE_OPTION)+")",
                                                 "dt_datetime_transform_task_bar_callback(" + str(dtm.DISPLAY_DATETIME_SPLIT_OPTION)+")",
                                                 "dt_datetime_transform_task_bar_callback(" + str(dtm.DISPLAY_DATETIME_MERGE_OPTION)+")",
                                                 "dt_datetime_transform_task_bar_callback(" + str(dtm.DISPLAY_DATETIME_COMPONNETS_OPTION)+")",
                                                 "transform_task_bar_callback("+str(dtm.DFC_TRANSFORM_RETURN)+")",
                                                 "displayhelp('" + str(dfchelp.TRANSFORM_DATETIME_TASKBAR_ID) + "')"]


datetimeA_transform_tb_doc_title            =   "datetime Transform Options"
datetimeA_transform_tb_title                =   "datetime Transform Options"
datetimeA_transform_tb_id                   =   "datetimeAtransformoptionstb"

datetimeA_transform_tb_keyTitleList         =   ["Convert</br>Column</br>to</br>datetime",
                                                 "Convert</br>Column</br>to</br>timedelta",
                                                 "Calculate</br>timedelta</br>Column",
                                                 "Split</br>Column</br>to</br>date,time</br>Columns"]

datetimeA_transform_tb_jsList               =   ["dt_datetime_transform_task_bar_callback(" + str(dtm.DISPLAY_DATETIME_OPTION)+")",
                                                 "dt_datetime_transform_task_bar_callback(" + str(dtm.DISPLAY_DATETIME_TIMEDELTA_OPTION)+")",
                                                 "dt_datetime_transform_task_bar_callback(" + str(dtm.DISPLAY_TIMEDELTA_CALCULATE_OPTION)+")",
                                                 "dt_datetime_transform_task_bar_callback(" + str(dtm.DISPLAY_DATETIME_SPLIT_OPTION)+")"]

datetimeB_transform_tb_doc_title            =   "datetime Transform Options"
datetimeB_transform_tb_title                =   "datetime Transform Options"
datetimeB_transform_tb_id                   =   "datetimeBtransformoptionstb"

datetimeB_transform_tb_keyTitleList         =   ["Merge</br>Column</br>from</br>date,time</br>Columns",
                                                 "Get</br>datetime</br>Components</br>Column",
                                                 "Return","Help"]

datetimeB_transform_tb_jsList               =   ["dt_datetime_transform_task_bar_callback(" + str(dtm.DISPLAY_DATETIME_MERGE_OPTION)+")",
                                                 "dt_datetime_transform_task_bar_callback("+ str(dtm.DISPLAY_DATETIME_COMPONNETS_OPTION)+")",
                                                 "transform_task_bar_callback("+str(dtm.DFC_TRANSFORM_RETURN)+")",
                                                 "displayhelp('" + str(dfchelp.TRANSFORM_DATETIME_TASKBAR_ID) + "')"]


"""
#--------------------------------------------------------------------------
#   datetime format input 
#--------------------------------------------------------------------------
"""
datetime_format_input_title             =   "Datetime Format"
datetime_format_input_id                =   "datetimeformatinput"
datetime_format_input_idList            =   ["dtcolname",
                                             "dtnanthreshold",
                                             "dterrors",
                                             "dtformatstring",
                                             None,None,None,None]

datetime_format_input_labelList         =   ["column_name_to_convert",
                                             "NaT_threshold",
                                             "errors",
                                             "format_string",
                                             "Change</br>Data</br>Type",
                                             "Get</br>formats",
                                             "Return","Help"]

datetime_format_input_typeList          =   ["select","text","select","text","button","button","button","button"]

datetime_format_input_placeholderList   =   ["column name",
                                             "percent of NaTs to cancel convert : default (do not check)",
                                             "parse error handling (default = NaT)",
                                             "format string to use (default = infer)",
                                             None,None,None,None]

datetime_format_input_jsList            =   [None,None,None,None,
                                             "process_datetime_format_transform_callback(" + str(dtm.PROCESS_DATETIME_OPTION) + ")",
                                             "process_datetime_format_transform_callback(" + str(dtm.DISPLAY_DATETIME_FORMAT_OPTION) + ")",
                                             "process_datetime_format_transform_callback(" + str(dtm.PROCESS_DATETIME_RETURN) + ")",
                                             "displayhelp('" + str(dfchelp.TRANSFORM_DATETIME_FORMAT_ID) + "')"]

datetime_format_input_reqList           =   [0,1,2]


datetime_format_ftypes_input_typeList   =   ["select","select","text","select","text","button","button","button","button"]


"""
#--------------------------------------------------------------------------
#   datetime format input 
#--------------------------------------------------------------------------
"""
timedelta_format_input_title            =   "timedelta Format"
timedelta_format_input_id               =   "timedeltaformatinput"
timedelta_format_input_idList           =   ["tdcolname",
                                             "dtnanthreshold",
                                             "tdunits",
                                             "tderrors",
                                             None,None,None]

timedelta_format_input_labelList        =   ["column_name_to_convert",
                                             "NaT_threshold",
                                             "units",
                                             "errors",
                                             "Change</br>Data</br>Type",
                                             "Return","Help"]

timedelta_format_input_typeList         =   ["select","text","select","select","button","button","button"]

timedelta_format_input_placeholderList  =   ["column name",
                                             "percent of NaTs to cancel convert : default (do not check)",
                                             "units of time (default = infer)",
                                             "parse error handling (default = NaT)",
                                             None,None,None]

timedelta_format_input_jsList           =   [None,None,None,None,
                                             "process_datetime_format_transform_callback(" + str(dtm.PROCESS_DATETIME_TIMEDELTA_OPTION) + ")",
                                             "process_datetime_format_transform_callback(" + str(dtm.PROCESS_DATETIME_RETURN) + ")",
                                             "displayhelp('" + str(dfchelp.TRANSFORM_DATETIME_DELTA_ID) + "')"]

timedelta_format_input_reqList          =   [0,1,2,3]


timedelta_units         =   ["Y","M","W","D","hours","minutes","seconds","milliseconds","microseconds","nanoseconds"]


error_handlers          =   ["raise","coerce","ignore"]
error_handlers_text     =   ["raise exception and terminate","coerce and set result to NaT","ignore and set result to input"]


"""
#--------------------------------------------------------------------------
#   datetime timedelta input 
#--------------------------------------------------------------------------
"""
datetime_tdelta_input_title             =   "Datetime timedelta"
datetime_tdelta_input_id                =   "datetimetdeltainput"
datetime_tdelta_input_idList            =   ["dttdcolname",
                                             "dttdcolname1",
                                             "dttdrescolname",
                                             "dttdelta",
                                             "dttdunits",
                                             None,None,None,None]

datetime_tdelta_input_labelList         =   ["datetime_column_name_1",
                                             "datetime_column_name_2",
                                             "new_timedelta_column_name",
                                             "new_timedelta_column_name_data_type",
                                             "time_units",
                                             "Calculate</br>timedelta",
                                             "Clear",
                                             "Return","Help"]

datetime_tdelta_input_typeList          =   ["select","select","text","select","select",
                                             "button","button","button","button"]

datetime_tdelta_input_placeholderList   =   ["first column name",
                                             "second column name",
                                             "result time delta column name",
                                             "result time delta column name data type",
                                             "time delta units",
                                              None,None,None,None]

datetime_tdelta_input_jsList            =   [None,None,None,None,None,
                                             "process_datetime_tdelta_callback(" + str(dtm.PROCESS_TIMEDELTA_CALCULATE_OPTION) + ")",
                                             "process_datetime_tdelta_callback(" + str(dtm.DISPLAY_TIMEDELTA_CALCULATE_OPTION) + ")",
                                             "process_datetime_tdelta_callback(" + str(dtm.PROCESS_DATETIME_RETURN) + ")",
                                             "displayhelp('" + str(dfchelp.TRANSFORM_DATETIME_DELTA_COL_ID) + "')"]

datetime_tdelta_input_reqList           =   [0,1,2,3,4]


"""
#--------------------------------------------------------------------------
#   datetime merge input 
#--------------------------------------------------------------------------
"""
datetime_merge_input_title              =   "Datetime Merge"
datetime_merge_input_id                 =   "datetimetmergeinput"
datetime_merge_input_idList             =   ["dtmdatecolname",
                                             "dtmtimecolname",
                                             "dtmdatetimecolname",
                                             "dtmdatatype",
                                             None,None,None,None]

datetime_merge_input_labelList          =   ["datetime.date_column_name",
                                             "datetime.time_column_name",
                                             "new_datetime_column_name",
                                             "new_datetime_column_data_type",
                                             "Merge</br>Columns",
                                             "Clear",
                                             "Return","Help"]

datetime_merge_input_typeList           =   ["select","select","text","select","button","button","button","button"]

datetime_merge_input_placeholderList    =   ["datetime.date column name",
                                             "datetime.time column name",
                                             "new datetime merged column name",
                                             "new datetime merged column data type",
                                              None,None,None,None]

datetime_merge_input_jsList             =   [None,None,None,None,
                                             "process_datetime_merge_split_callback(" + str(dtm.PROCESS_DATETIME_MERGE_OPTION) + ")",
                                             "process_datetime_merge_split_callback(" + str(dtm.DISPLAY_DATETIME_MERGE_OPTION) + ")",
                                             "process_datetime_merge_split_callback(" + str(dtm.PROCESS_DATETIME_RETURN) + ")",
                                             "displayhelp('" + str(dfchelp.TRANSFORM_DATETIME_MERGE_ID) + "')"]

datetime_merge_input_reqList            =   [0,1,2,3]

"""
#--------------------------------------------------------------------------
#   datetime split input 
#--------------------------------------------------------------------------
"""
datetime_split_input_title              =   "Datetime Split"
datetime_split_input_id                 =   "datetimetsplitinput"
datetime_split_input_idList             =   ["dtsdatetimecolname",
                                             "dtsdatecolname",
                                             "dtstimecolname",
                                             None,None,None,None]

datetime_split_input_labelList          =   ["datetime_column_name",
                                             "new_datetime.date_column_name",
                                             "new_datetime.time_column_name",
                                             "Split</br>Column",
                                             "Clear",
                                             "Return","Help"]

datetime_split_input_typeList           =   ["select","text","text","button","button","button","button"]

datetime_split_input_placeholderList    =   ["datetime column name",
                                             "date column name",
                                             "time column name",
                                              None,None,None,None]

datetime_split_input_jsList             =   [None,None,None,
                                             "process_datetime_merge_split_callback(" + str(dtm.PROCESS_DATETIME_SPLIT_OPTION) + ")",
                                             "process_datetime_merge_split_callback(" + str(dtm.DISPLAY_DATETIME_SPLIT_OPTION) + ")",
                                             "process_datetime_merge_split_callback(" + str(dtm.PROCESS_DATETIME_RETURN) + ")",
                                             "displayhelp('" + str(dfchelp.TRANSFORM_DATETIME_SPLIT_ID) + "')"]

datetime_split_input_reqList            =   [0,1,2]


"""
#--------------------------------------------------------------------------
#   datetime components input 
#--------------------------------------------------------------------------
"""
datetime_comp_input_title               =   "Datetime Split"
datetime_comp_input_id                  =   "datetimecompinput"
datetime_comp_input_idList              =   ["dtcdatetimecolname",
                                             "dtcresultcolname",
                                             "dtccomptype",
                                             None,None,None]

datetime_comp_input_labelList           =   ["datetime_column_name",
                                             "new_datetime_component_column_name",
                                             "datetime_component",
                                             "Get</br>Component",
                                             "Return","Help"]

datetime_comp_input_typeList            =   ["select","text","select","button","button","button"]

datetime_comp_input_placeholderList     =   ["datetime column name",
                                             "result column name",
                                             "result component",
                                              None,None,None]

datetime_comp_input_jsList              =   [None,None,None,
                                             "process_datetime_components_callback(" + str(dtm.PROCESS_DATETIME_COMPONNETS_OPTION) + ")",
                                             "process_datetime_components_callback(" + str(dtm.PROCESS_DATETIME_RETURN) + ")",
                                             "displayhelp('" + str(dfchelp.TRANSFORM_DATETIME_COMP_ID) + "')"]

datetime_comp_input_reqList             =   [0,1,2]

import dfcleanser.data_inspection.data_inspection_widgets as diw 

datatransform_inputs                    =   [datetime_format_input_id, timedelta_format_input_id, datetime_tdelta_input_id,
                                             datetime_merge_input_id, datetime_split_input_id, datetime_comp_input_id,
                                             diw.data_transform_df_input_id]

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
#    datetime convert methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def display_datetime_convert(option,parms=None) :
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

    colname     =   ""
    
    df          =   cfg.get_current_chapter_df(cfg.DataTransform_ID) 
    
    if( not(option == dtm.DISPLAY_DATETIME_FORMAT_OPTION) ) :
            
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
            
        fparms  =   get_parms_for_input(parms,datetime_format_input_idList)
            
        colname     =   fparms[0]
        natthresh   =   fparms[1]
        errors      =   fparms[2]
        formatstr   =   fparms[3]

        cfg.set_config_value(datetime_format_input_id+"Parms",[colname,natthresh,errors,formatstr])
        
        from dfcleanser.sw_utilities.sw_utility_model import get_Dict
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
    
    selectDicts     =   [] 
    
    current_df      =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
    colnames        =   current_df.columns.tolist()
    
    cnames          =   []
    
    for i in range(len(colnames)) :
        if(not (is_numeric_col(df,colnames[i])) ) :
            cnames.append(colnames[i])
    
    if(len(colname) == 0) :
        colname     =   cnames[0]
        
    cnames          =   {"default":colname,"list": cnames}#, "callback":"change_convert_dtype_callback"}
    selectDicts.append(cnames)
    
    errorssel         =   {"default":error_handlers_text[1],"list":error_handlers_text}
    selectDicts.append(errorssel)
    
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
    dt_datetime_custom_form.set_buttonstyle({"font-size":12, "height":75, "width":100, "left-margin":28})
    dt_datetime_custom_form.set_gridwidth(480)
    dt_datetime_custom_form.set_fullparms(True)  
    
    dt_datetime_custom_html = dt_datetime_custom_form.get_html()

    dt_datetime_title_html  =   "<br><div>Convert Column to Datetime</div><br>"
        
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
    gridhtmls       =   [dt_datetime_title_html,dt_datetime_custom_html]

    print("\n")
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls,True)
        


def display_timedelta_convert(parms=None) :
    """
    * ---------------------------------------------------------
    * function : display timedelta convert input screen
    * 
    * parms :
    *  parms          - datatype parms
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """

    if(not(parms is None)) :
    
        fparms  =   get_parms_for_input(parms,datetime_format_input_idList)
            
        colname     =   fparms[0]
        nanthresh   =   fparms[1]
        units       =   fparms[2]
        errors      =   fparms[3]
    
        
        cfg.set_config_value(timedelta_format_input_id+"Parms",[colname,nanthresh,units,errors])
        
    else :
        
        colname     =   ""
        nanthresh   =   ""
        units       =   "seconds"

        cfg.drop_config_value(timedelta_format_input_id+"Parms")
        
    
    df          =   cfg.get_current_chapter_df(cfg.DataTransform_ID) 
    
    dt_timedelta_custom_form = InputForm(timedelta_format_input_id,
                                         timedelta_format_input_idList,
                                         timedelta_format_input_labelList,
                                         timedelta_format_input_typeList,
                                         timedelta_format_input_placeholderList,
                                         timedelta_format_input_jsList,
                                         timedelta_format_input_reqList)
            
    selectDicts     =   [] 
    
    current_df      =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
    colnames        =   current_df.columns.tolist()
    cnames          =   []
    
    for i in range(len(colnames)) :
        if(is_numeric_col(df,colnames[i])) :
            cnames.append(colnames[i])
    
    if(len(colname) == 0) :
        colname     =   cnames[0]
        
    cnamessel       =   {"default":colname,"list": cnames}#, "callback":"change_convert_dtype_callback"}
    selectDicts.append(cnamessel)
        
    unitsel           =   {"default":units,"list":timedelta_units}
    selectDicts.append(unitsel)
    
    errorssel         =   {"default":error_handlers_text[1],"list":error_handlers_text}
    selectDicts.append(errorssel)
    
    get_select_defaults(dt_timedelta_custom_form,
                        timedelta_format_input_id,
                        timedelta_format_input_idList,
                        timedelta_format_input_typeList,
                        selectDicts)
    
    dt_timedelta_custom_form.set_shortForm(True)
    dt_timedelta_custom_form.set_buttonstyle({"font-size":12, "height":75, "width":100, "left-margin":90})
    dt_timedelta_custom_form.set_gridwidth(480)
    dt_timedelta_custom_form.set_fullparms(True)  
    
    dt_timedelta_custom_form_html = dt_timedelta_custom_form.get_html()

    dt_timedelta_title_html  =   "<br><div>Convert Column to Timedelta</div><br>"
        
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
    gridhtmls       =   [dt_timedelta_title_html,dt_timedelta_custom_form_html]

    print("\n")
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls,True)


def get_datetime_column_names(df)  :

    colnames        =   df.columns.tolist()
    
    datetimecols    =   []
             
    from dfcleanser.common.common_utils import is_datetime_type_col
       
    for i in range(len(colnames)) :
            
        if(is_datetime_type_col(df,colnames[i])) :   
            datetimecols.append(colnames[i])
    
    return(datetimecols)    
    
    

def display_datetime_timedelta(parms=None)  :
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
    
    current_df      =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
    
    datetimecols    =   get_datetime_column_names(current_df)
    
    if(len(datetimecols) > 0) :
             
        datetimenames          =   {"default":datetimecols[0],"list": datetimecols}
    
        selectDicts.append(datetimenames)
        selectDicts.append(datetimenames)
    
        tdeltasel         =   {"default":"timedelta","list":["timedelta","float64"], "callback":"change_convert_dtype_callback"}
        selectDicts.append(tdeltasel)
        
        dtsel           =   {"default":"Seconds","list":["Days","Hours","Minutes","Seconds","MilliSeconds","MicroSeconds"], "callback":"change_convert_units_callback"}
        selectDicts.append(dtsel)
   
        get_select_defaults(dt_datetime_custom_form,
                            datetime_tdelta_input_id,
                            datetime_tdelta_input_idList,
                            datetime_tdelta_input_typeList,
                            selectDicts)
    
        cfg.set_config_value(datetime_tdelta_input_id+"Parms",[datetimecols[0],datetimecols[0],"timedelta_column_timedelta","timedelta","Seconds"])
        
        cfg.set_config_value(datetime_tdelta_input_id+"ParmsProtect",[False,False,False,False,True])

        dt_datetime_custom_form.set_shortForm(True)
        dt_datetime_custom_form.set_buttonstyle({"font-size":12, "height":75, "width":100, "left-margin":25})
        dt_datetime_custom_form.set_gridwidth(480)
        dt_datetime_custom_form.set_fullparms(True)  
    
        dt_datetime_custom_html = dt_datetime_custom_form.get_html()
    
        dt_datetime_title_html  =   "<div>Calculate timedelta</div><br>"
        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
        gridhtmls       =   [dt_datetime_title_html,dt_datetime_custom_html]
    
        print("\n")
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls,True)

    else :

        print("\n")

        display_status_note("No datetime columns found in dataframe")


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

    current_df      =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
    datetimecols    =   get_datetime_column_names(current_df)
    
    if(len(datetimecols) > 0) :
             
        datetimenames          =   {"default":datetimecols[0],"list": datetimecols}
    
        if(action == dtm.SPLIT) :
        
            dt_datetime_custom_form = InputForm(datetime_split_input_id,
                                                datetime_split_input_idList,
                                                datetime_split_input_labelList,
                                                datetime_split_input_typeList,
                                                datetime_split_input_placeholderList,
                                                datetime_split_input_jsList,
                                                datetime_split_input_reqList)
        
            selectDicts     =   [] 
    
            current_df      =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
            colnames        =   current_df.columns.tolist()
        
            datetimenames          =   {"default":datetimecols[0],"list": datetimecols}
        
            selectDicts.append(datetimenames)
        
            get_select_defaults(dt_datetime_custom_form,
                                datetime_split_input_id,
                                datetime_split_input_idList,
                                datetime_split_input_typeList,
                                selectDicts)
        
            dt_datetime_custom_form.set_shortForm(True)
            dt_datetime_custom_form.set_buttonstyle({"font-size":12, "height":75, "width":100, "left-margin":25})
            dt_datetime_custom_form.set_gridwidth(480)
            dt_datetime_custom_form.set_fullparms(True)  
        
            dt_datetime_custom_html = dt_datetime_custom_form.get_html()

            dt_datetime_title_html  =   "<div>Split Datetime Column</div><br>"
        
        else :
        
            dt_datetime_custom_form = InputForm(datetime_merge_input_id,
                                                datetime_merge_input_idList,
                                                datetime_merge_input_labelList,
                                                datetime_merge_input_typeList,
                                                datetime_merge_input_placeholderList,
                                                datetime_merge_input_jsList,
                                                datetime_merge_input_reqList)
        
            selectDicts     =   [] 
    
            current_df      =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
            colnames        =   current_df.columns.tolist()
        
            datecols        =   []
            timecols        =   []
             
            from dfcleanser.common.common_utils import is_date_col, is_time_col
       
            for i in range(len(colnames)) :
            
                if(is_date_col(current_df,colnames[i])) :   datecols.append(colnames[i])
                if(is_time_col(current_df,colnames[i])) :   timecols.append(colnames[i])
            
            if(len(datecols) > 0) :
                datenames          =   {"default":datecols[0],"list": datecols}
            else :
                datenames          =   {"default":"No datetime.date Columns to Select","list": ["No datetime.date Columns to Select"]}
                
            if(len(timecols) > 0) :
                timenames          =   {"default":timecols[0],"list": timecols}
            else :
                timenames          =   {"default":"No datetime.time Columns to Select","list": ["No datetime.time Columns to Select"]}
                
            selectDicts.append(datenames)
            selectDicts.append(timenames)
        
            ctypes          =   {"default":"datetime.datetime","list": ["datetime.datetime","np.datetime64","pd.Timestamp"]}
            selectDicts.append(ctypes)
        
            get_select_defaults(dt_datetime_custom_form,
                                datetime_merge_input_id,
                                datetime_merge_input_idList,
                                datetime_merge_input_typeList,
                                selectDicts)
        
            dt_datetime_custom_form.set_shortForm(True)
            dt_datetime_custom_form.set_buttonstyle({"font-size":12, "height":75, "width":100, "left-margin":30})
            dt_datetime_custom_form.set_gridwidth(480)
            dt_datetime_custom_form.set_fullparms(True)  
        
            dt_datetime_custom_html = dt_datetime_custom_form.get_html()
        
            dt_datetime_title_html  =   "<div>Merge Datetime Columns</div><br>"
        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
        gridhtmls       =   [dt_datetime_title_html,dt_datetime_custom_html]
    
        print("\n")
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls,True)
            
    else :

        print("\n")

        display_status_note("No datetime columns found in dataframe")



dtcomps           =   ["year","quarter","month","week","week of year","day","day of year","day of week","time","hour","minute","second","microsecond","nanosecond"]
tdcomps           =   ["days","seconds","microseconds","nanoseconds"]
   

def display_datetime_components(parms,tddtype=False) :
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
    
    current_df      =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
    datetimecols    =   get_datetime_column_names(current_df)
    
    if(len(datetimecols) > 0) :
    
        dt_datetime_comps_form = InputForm(datetime_comp_input_id,
                                           datetime_comp_input_idList,
                                           datetime_comp_input_labelList,
                                           datetime_comp_input_typeList,
                                           datetime_comp_input_placeholderList,
                                           datetime_comp_input_jsList,
                                           datetime_comp_input_reqList)
    
        selectDicts     =   [] 
    
        df              =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
        colnames        =   df.columns.tolist()
    
        dt_colnames     =   []
    
    
        for i in range(len(colnames)) :
        
            if(not tddtype) :
        
                from dfcleanser.common.common_utils import is_datetime_type_col
                if(is_datetime_type_col(df,colnames[i])) :            
                    dt_colnames.append(colnames[i])
                
            else :
            
                from dfcleanser.common.common_utils import is_datetime_type_col, is_numeric_col
                if( (is_datetime_type_col(df,colnames[i])) or (is_numeric_col(colnames[i])) ) :            
                    dt_colnames.append(colnames[i])
            
        if(len(dt_colnames) > 0)   :
            cnames          =   {"default": dt_colnames[0],"list": dt_colnames, "callback":"change_component_callback"}
        else :
            cnames          =   {"default": "No datetime columns found","list": ["No datetime columns found"]}
            
        selectDicts.append(cnames)
    
        if(not tddtype) :    
            comps           =   {"default":dtcomps[0],"list":dtcomps, "callback":"change_component_callback"}
        else :
            comps           =   {"default":tdcomps[0],"list":tdcomps, "callback":"change_component_callback"}
        
        selectDicts.append(comps)
    
        get_select_defaults(dt_datetime_comps_form,
                            datetime_comp_input_id,
                            datetime_comp_input_idList,
                            datetime_comp_input_typeList,
                            selectDicts)
    
        if(not tddtype) :
            if(len(dt_colnames) > 0) :
                cfg.set_config_value(datetime_comp_input_id+"Parms",[dt_colnames[0],dt_colnames[0] + "_" + dtcomps[0],dtcomps[0]])
            else :
                cfg.set_config_value(datetime_comp_input_id+"Parms",["","",dtcomps[0]])
        else :
            if(len(dt_colnames) > 0) :
                cfg.set_config_value(datetime_comp_input_id+"Parms",[dt_colnames[0],dt_colnames[0] + "_" + tdcomps[0],tdcomps[0]])
            else :
                cfg.set_config_value(datetime_comp_input_id+"Parms",["","",tdcomps[0]])
    
        dt_datetime_comps_form.set_shortForm(True)
        dt_datetime_comps_form.set_buttonstyle({"font-size":12, "height":50, "width":140, "left-margin":15})
        dt_datetime_comps_form.set_gridwidth(480)
        dt_datetime_comps_form.set_fullparms(True)  
        
        dt_datetime_comps_html = dt_datetime_comps_form.get_html()
        
        dt_datetime_title_html  =   "<div>Get Datetime Component Column</div><br>"
        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
        gridhtmls       =   [dt_datetime_title_html,dt_datetime_comps_html]
    
        print("\n")
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls,True)
            
    else :

        print("\n")

        display_status_note("No datetime columns found in dataframe")
    

       
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
    
    typestr = get_dtype_str_for_datatype(ftype)

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


   


    
