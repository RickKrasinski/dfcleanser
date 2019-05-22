"""
# data_inspection_widgets 
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

from dfcleanser.common.common_utils import (get_num_uniques_by_id, RunningClock, get_parms_for_input, 
                                            get_col_uniques_by_id, display_status, opStatus, 
                                            display_exception, display_generic_grid,
                                            get_select_defaults, displayParms, new_line)

from dfcleanser.common.html_widgets import (InputForm, CheckboxGroupForm, ButtonGroupForm)

from dfcleanser.common.table_widgets import (dcTable, ROW_MAJOR, get_row_major_table, SCROLL_NEXT)

from dfcleanser.common.display_utils import (get_df_datatypes_data, display_sample_rows, get_datatype_id)

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    data inspection cfg variables
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def print_page_separator(title,divid) :
    
    style_name      =   "dfc-divider_" + str(divid)
    
    divider_cont    =   ("<div style='margin-left: 0px; width:95%;'>" + new_line) 
    divider1_html   =   ("        <style>" + new_line + "            hr." + style_name + " { " + new_line + "                overflow: visible; padding: 0; width: 90%; border: none; box-shadow: 0 0 10px 1px #296093; text-align: center;" + new_line + "            } " + new_line)
    divider2_html   =   ('            hr.' + style_name + ':after { ' + new_line + '                content: "' + title + '"; ')
    divider3_html   =   (" display: inline-block; position: relative; top: -0.7em; font-size: 24px; font-weight: bold;" + new_line + "                font-family: Arial; color: #236BAF; padding: 0 0.25em; background: white;" + new_line + "            }" + new_line + "        </style>" + new_line) 
    
    
    divider_start_html  =   ("    <hr class='" + style_name + "'>" + new_line + "    <div>" + new_line)
    divider_end_html    =   ("    </div>" + new_line + "</div>" + new_line + "<br>" + new_line)
    
    divider_html     =   (divider_cont + divider_start_html + divider1_html + divider2_html + divider3_html + divider_end_html) 
    
    from dfcleanser.common.common_utils import (displayHTML)
    displayHTML(divider_html)


def get_cbox_flag(id) :
    
    if(id == 0) :
        if(cfg.get_config_value(cfg.DATA_TYPES_CBOX_0_KEY) == None)  :
            return(False)
        else :
            return(cfg.get_config_value(cfg.DATA_TYPES_CBOX_0_KEY))
            
    elif(id == 1) :
        if(cfg.get_config_value(cfg.NANS_CBOX_1_KEY) == None)  :
            return(False)
        else :
            return(cfg.get_config_value(cfg.NANS_CBOX_1_KEY))
            
    elif(id == 2) :
        if(cfg.get_config_value(cfg.ROWS_CBOX_2_KEY) == None)  :
            return(False)
        else :
            return(cfg.get_config_value(cfg.ROWS_CBOX_2_KEY))
        
    elif(id == 3) :
        if(cfg.get_config_value(cfg.COLS_CBOX_3_KEY) == None)  :
            return(False)
        else :
            return(cfg.get_config_value(cfg.COLS_CBOX_3_KEY))

    elif(id == 4) :
        if(cfg.get_config_value(cfg.CATS_CBOX_4_KEY) == None)  :
            return(False)
        else :
            return(cfg.get_config_value(cfg.CATS_CBOX_4_KEY))

    else :
        return(False)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   data inspection form components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   data inspection checkboxes
#--------------------------------------------------------------------------
"""
main_inspection_checkbox_title      =   "Inspection Options"
main_inspection_checkbox_id         =   "inspection_cb"

main_inspection_checkbox_idList     =   ["datatypes","rows","columns","nans","categories"]
main_inspection_checkbox_labelList  =   ["Data Types","NaNs","Rows","Columns","Categories"]

main_inspection_checkbox_jsList     =   [None,None,None,None,None]

main_inspection_checkbox_javascript =   ["js/data_inspection.js"]

"""
#--------------------------------------------------------------------------
#    data inspection task bar
#--------------------------------------------------------------------------
"""
data_inspection_tb_doc_title       =   "Inspection Options"
data_inspection_tb_title           =   "Inspection Options"
data_inspection_tb_id              =   "inspectionoptionstb"

data_inspection_tb_keyTitleList    =   ["Inspect Data","Clear","Reset","Help"]

data_inspection_tb_jsList          =   ["inspection_task_bar_callback(0)",
                                        "inspection_task_bar_callback(1)",
                                        "process_pop_up_cmd(6)",
                                        "displayhelp(" + str(dfchelp.INSPECT_MAIN_TASKBAR_ID) + ")"]

data_inspection_tb_centered        =   False


"""
#--------------------------------------------------------------------------
#    select dataframe input form  
#--------------------------------------------------------------------------
"""
data_inspection_df_input_title             =   "Dataframe To Inspect"
data_inspection_df_input_id                =   "datainspectdf"
data_inspection_df_input_idList            =   ["didfdataframe"]

data_inspection_df_input_labelList        =   ["dataframe_to_inspect"]

data_inspection_df_input_typeList         =   ["select"]

data_inspection_df_input_placeholderList  =   ["dataframe to inspect"]

data_inspection_df_input_jsList           =   [None]

data_inspection_df_input_reqList          =   [0]

data_inspection_df_input_form             =   [data_inspection_df_input_id,
                                               data_inspection_df_input_idList,
                                               data_inspection_df_input_labelList,
                                               data_inspection_df_input_typeList,
                                               data_inspection_df_input_placeholderList,
                                               data_inspection_df_input_jsList,
                                               data_inspection_df_input_reqList]  

data_cleansing_df_input_id                =   "datacleansedf"
data_transform_df_input_id                =   "datatransformdf"
data_export_df_input_id                   =   "dataexportdf"


"""
#--------------------------------------------------------------------------
#    column search data  
#--------------------------------------------------------------------------
"""
data_inspection_colsearch_title            =   "Column Values To Search For"
data_inspection_colsearch_id               =   "datainspectcolsearch"
data_inspection_colsearch_idList           =   ["colsearchnames",
                                                "colsearchvalues",
                                                None]

data_inspection_colsearch_labelList        =   ["column_names",
                                                "column_values",
                                                "Get Rows Matching colunm_values"]

data_inspection_colsearch_typeList         =   ["select","text","button"]

data_inspection_colsearch_placeholderList  =   ["columns to search in",
                                                "column values to search for [] ",
                                                None]

data_inspection_colsearch_jsList           =   [None,None,
                                                "get_col_rows_callback()"]

data_inspection_colsearch_reqList          =   [0,1]

data_inspection_colsearch_form             =   [data_inspection_colsearch_id,
                                               data_inspection_colsearch_idList,
                                               data_inspection_df_input_labelList,
                                               data_inspection_colsearch_typeList,
                                               data_inspection_colsearch_placeholderList,
                                               data_inspection_colsearch_jsList,
                                               data_inspection_colsearch_reqList]  



"""
#--------------------------------------------------------------------------
#    drop rows input form
#--------------------------------------------------------------------------
"""
drop_rows_input_title                =   ""
drop_rows_input_id                   =   "droprowsinput"
drop_rows_input_idList               =   ["droprowthreshold",None,None]

drop_rows_input_labelList            =   ["Nan_Threshold",
                                          "Drop Rows </br> with % of Cols</br>  > Threshold",
                                          "Drop Rows </br> with Nan Count</br>  > Threshold"]

drop_rows_input_typeList             =   ["text","button","button"]

drop_rows_input_placeholderList      =   ["",None,None]

drop_rows_input_jsList               =   [None,
                                          "dc_drop_rows_callback(0)",
                                          "dc_drop_rows_callback(1)"]

drop_rows_input_reqList              =   [0]

drop_rows_input_short                =   True

drop_columns_input_title                =   ""
drop_columns_input_id                   =   "dropcolsinput"
drop_columns_input_idList               =   ["dropcolthreshold",None,None]

drop_columns_input_labelList            =   ["Nan_Threshold",
                                             "Drop Columns </br> with % of Rows</br>  > Threshold",
                                             "Drop Columns </br> with Nan</br>Row Count</br>  > Threshold"]

drop_columns_input_typeList             =   ["text","button","button"]

drop_columns_input_placeholderList      =   ["",None,None]

drop_columns_input_jsList               =   [None,
                                            "dc_drop_cols_callback(0)",
                                            "dc_drop_cols_callback(0)"]

drop_columns_input_reqList              =   [0]


"""
#--------------------------------------------------------------------------
#    get dataframe schema
#--------------------------------------------------------------------------
"""
data_inspection_dfschema_tb_doc_title       =   "Inspection dfSchema"
data_inspection_dfschema_tb_title           =   "Inspection dfSchema"
data_inspection_dfschema_tb_id              =   "inspectiondfschematb"

data_inspection_dfschema_tb_keyTitleList    =   ["Show Dataframe Schema"]

from dfcleanser.data_transform.data_transform_model import DISPLAY_DF_SCHEMA_TRANSFORM
data_inspection_dfschema_tb_jsList          =   ["transform_task_bar_callback("+str(DISPLAY_DF_SCHEMA_TRANSFORM)+")"]

data_inspection_dfschema_tb_centered        =   True


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    data inspection display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def display_inspection_main_taskbar() :
    
    from dfcleanser.common.display_utils import display_dfcleanser_taskbar
    display_dfcleanser_taskbar(ButtonGroupForm(data_inspection_tb_id,
                                               data_inspection_tb_keyTitleList,
                                               data_inspection_tb_jsList,
                                               data_inspection_tb_centered))


def get_inspection_dfschema_taskbar() :
    
    return(ButtonGroupForm(data_inspection_dfschema_tb_id,
                           data_inspection_dfschema_tb_keyTitleList,
                           data_inspection_dfschema_tb_jsList,
                           data_inspection_dfschema_tb_centered))


def get_select_df_form(title="Inspect") :
    """
    * -------------------------------------------------------------------------- 
    * function : display select dataframe form
    * 
    * parms :
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    if(title == "Cleanse") :
        labellist   =   ["dataframe_to_cleanse"]
        formid      =   "datacleansedf"

    elif(title == "Transform") :
        labellist   =   ["dataframe_to_transform"]
        formid      =   "datatransformdf"

    elif(title == "Export") :
        labellist   =   ["dataframe_to_export"]
        formid      =   "dataexportdf"

    else :
        labellist   =   data_inspection_df_input_labelList
        formid      =   data_inspection_df_input_id
    
    select_df_form  =   InputForm(formid,
                                  data_inspection_df_input_idList,
                                  labellist,
                                  data_inspection_df_input_typeList,
                                  data_inspection_df_input_placeholderList,
                                  data_inspection_df_input_jsList,
                                  data_inspection_df_input_reqList)
    
    df_list     =   cfg.get_dfc_dataframes_select_list()

    if(not (df_list.get("list") == None)) :
        dataframes      =   df_list
    else :
        dataframes      =   {'default': "", 'list': [""]}

    selectDicts     =   []
    selectDicts.append(dataframes)

    get_select_defaults(select_df_form,
                        data_inspection_df_input_id,
                        data_inspection_df_input_idList,
                        data_inspection_df_input_typeList,
                        selectDicts)

    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        select_df_form.set_gridwidth(780)
    else :
        select_df_form.set_gridwidth(480)
    
    return(select_df_form)


def get_colsearch_form() :
    """
    * -------------------------------------------------------------------------- 
    * function : display column search form
    * 
    * Parms :
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    colsearch_form  =   InputForm(data_inspection_colsearch_id,
                                  data_inspection_colsearch_idList,
                                  data_inspection_colsearch_labelList,
                                  data_inspection_colsearch_typeList,
                                  data_inspection_colsearch_placeholderList,
                                  data_inspection_colsearch_jsList,
                                  data_inspection_colsearch_reqList)
    
    col_names   =   cfg.get_dfc_dataframe().columns.tolist()
    col_names.append("ALL")
    cnames      =   {'default': "ALL", 'list': col_names}
    
    selectDicts     =   []
    selectDicts.append(cnames)

    get_select_defaults(colsearch_form,
                        data_inspection_colsearch_id,
                        data_inspection_colsearch_idList,
                        data_inspection_colsearch_typeList,
                        selectDicts)

    colsearch_form.set_shortForm(True)
    colsearch_form.set_gridwidth(240)
    colsearch_form.set_custombwidth(240)
    colsearch_form.set_buttonstyle({"font-size":12})
    
    return(colsearch_form)

    
def get_inspection_check_form_parms(parms,current_checkboxes) :
    """
    * -------------------------------------------------------------------------- 
    * function : display inspection checkbox form
    * 
    * Parms :
    *   parms               -   check boxes to set
    *   current_checkboxes  -   current check boxes set
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    parms = []
            
    parms.append(get_cbox_flag(0))
    current_checkboxes.append(get_cbox_flag(0))
    parms.append(get_cbox_flag(1))
    current_checkboxes.append(get_cbox_flag(1))
    parms.append(get_cbox_flag(2))
    current_checkboxes.append(get_cbox_flag(2))
    parms.append(get_cbox_flag(3))
    current_checkboxes.append(get_cbox_flag(3))
    parms.append(get_cbox_flag(4))
    current_checkboxes.append(get_cbox_flag(4))
    
    return()

def get_main_checkbox_form(current_checkboxes) :
    """
    * -------------------------------------------------------------------------- 
    * function : display inspection checkbox form
    * 
    * Parms :
    *   current_checkboxes  -   current check boxes set
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    inspection_checkboxForm    =  CheckboxGroupForm(main_inspection_checkbox_id,
                                                    main_inspection_checkbox_idList,
                                                    main_inspection_checkbox_labelList,
                                                    main_inspection_checkbox_jsList,
                                                    current_checkboxes,
                                                    [0,0,0,0,0])
    
    if(not (cfg.get_dfc_mode() == cfg.INLINE_MODE)) :
        inspection_checkboxForm.set_rows_count([3,2])   
    
    return(inspection_checkboxForm)


def get_drop_rows_input_parms(parms) :
    return(get_parms_for_input(parms,drop_rows_input_idList))

def get_drop_cols_input_parms(parms) :
    return(get_parms_for_input(parms,drop_columns_input_idList))

def get_drop_cbox_flags() :

    parms = []
    parms.append(get_cbox_flag(0))
    parms.append(get_cbox_flag(1))
    parms.append(get_cbox_flag(2))
    parms.append(get_cbox_flag(3))
    parms.append(get_cbox_flag(4))
        
    return(parms)


"""            
#------------------------------------------------------------------
#   display data inspection header
#------------------------------------------------------------------
"""           
def display_inspection_data(display=True,forExport=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : display inspection data form
    * 
    * Parms :
    *   display     -   display flag
    *   forExport   -   for Export flag
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    if(cfg.is_a_dfc_dataframe_loaded()) :
        
        labels  =   ["NUMBER OF ROWS","NUMBER OF COLS"]
        values  =   [str(len(cfg.get_dfc_dataframe())),str(len(cfg.get_dfc_dataframe().columns))]
        
        if(display) :
            displayParms("&nbsp;dataframe Imported",labels,values,"inspectdata",width=None)
        else :
            if(forExport) :
                return(displayParms("&nbsp;dataframe Exported",labels,values,"inspectdata",100,0,False))
            else :
                return(displayParms("&nbsp;dataframe Imported",labels,values,"inspectdata",100,0,False))
            
    else :
        display_status("No Dataframe selected for inspection", 1)


def display_drop_rows() :
    """
    * -------------------------------------------------------------------------- 
    * function : display drop nan rows threshold form
    * 
    * Parms :
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    drop_form   =   InputForm(drop_rows_input_id,
                              drop_rows_input_idList,
                              drop_rows_input_labelList,
                              drop_rows_input_typeList,
                              drop_rows_input_placeholderList,
                              drop_rows_input_jsList,
                              drop_rows_input_reqList)
    
    drop_form.set_buttonstyle({"font-size":12})
    drop_form.set_gridwidth(240)
    return(drop_form.get_html())
    
    
def display_drop_cols() :
    """
    * -------------------------------------------------------- 
    * function : display drop nan cols threshold form
    * 
    * Parms :
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    drop_form   =   InputForm(drop_columns_input_id,
                              drop_columns_input_idList,
                              drop_columns_input_labelList,
                              drop_columns_input_typeList,
                              drop_columns_input_placeholderList,
                              drop_columns_input_jsList,
                              drop_columns_input_reqList)
    
    drop_form.set_buttonstyle({"font-size":12,"height":85})
    drop_form.set_gridwidth(240)    
    return(drop_form.get_html())

"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   specific data inspection display routines
#------------------------------------------------------------------
#------------------------------------------------------------------
"""       


def display_df_datatypes(table,dtypes_list,colnames_count_list,colnames_dict,display=True) : 
    """
    * -------------------------------------------------------------------------- 
    * function : display drop nan cols threshold form
    * 
    * Parms :
    *  table               -   table object
    *  dtypes_list         -   list of datatype
    *  colnames_count_list -   list of colnames count for datatype    
    *  colnames_dict       -   list of colnames for datatype    
    *  display             -   display flag    
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    dtypesHeader   =   ["Data Type","Count","Column Names"]
    dtypesRows     =   []
    dtypesHrefs    =   []

    dtypesWidths   =   [15,10,75]
    dtypesAligns   =   ["left","center","left"]

    dtypesrow      =   []
    
    table.set_colsperrow(3)
    table.set_rowspertable(50)
    table.set_maxtables(1)
    
    for i in range(len(dtypes_list)) :
        
        dtypeshref    =   [None,None,None]
        
        if(dtypes_list[i] == "str") :
            hrefdtid = get_datatype_id(str) 
        else :
            hrefdtid = get_datatype_id(dtypes_list[i])
            
        dtypeshref[0] = "display_objects_callback(" + str(hrefdtid) + ")"
        dtypesHrefs.append(dtypeshref)
        
        if(dtypes_list[i] == "datetime64[ns]") :
            dtypesrow.append("[datetime.datetime]")
        elif(dtypes_list[i] == "timedelta64[ns]") :
            dtypesrow.append("[datetime.timedelta]")
        else :
            dtypesrow.append("["+str(dtypes_list[i])+"]")
            
        dtypesrow.append(colnames_count_list[i])
        dtypesrow.append(colnames_dict.get(dtypes_list[i])) 
        
        dtypesRows.append(dtypesrow)
        dtypesrow       =   []
    
    table.set_headerList(dtypesHeader)
    table.set_rowList(dtypesRows)
    table.set_widthList(dtypesWidths)
    table.set_alignList(dtypesAligns)
    #table.set_refList(dtypesHrefs)
    table.set_checkLength(True) 
    table.set_textLength(21) 
    
    if(display) :
        table.display_table()
    else :
        return(table.get_html())

    
"""            
#------------------------------------------------------------------
#   display null data info for a dataframe
#
#   df              -   dataframe
#
#------------------------------------------------------------------
"""
def display_null_data(df,rownantable,colnantable,rowsize) :
    """
    * -------------------------------------------------------------------------- 
    * function : display null data info for a dataframe
    * 
    * Parms :
    *  df           -   dataframe    
    *  rownantable  -   row nan table object
    *  colnantable  -   col nan table object
    *  rowsize      -   row size    
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    df_cols         =   df.columns
    df_nulls        =   df.isnull().sum()
    totnullcols     =   0
    
    df_nulls_dict   =   {}
    
    opstat  =   opStatus()
    
    clock = RunningClock()
    clock.start()

    try :                

        for i in range(len(df_nulls)) :
            if(not df_nulls[i] == 0) :
                totnullcols = totnullcols + 1
            
                if( not ((df_nulls_dict.get(df_nulls[i], None)) == None ) ): 
                    df_nulls_list = df_nulls_dict.get(df_nulls[i])
                    df_nulls_list.append(df_cols[i])
                    df_nulls_dict.update({df_nulls[i]:df_nulls_list})
                else :
                    df_nulls_list = []
                    df_nulls_list.append(df_cols[i])
                    df_nulls_dict.update({df_nulls[i]:df_nulls_list})
    
        if(sum(df_nulls) == 0) :
            display_row_nan_stats(df)
        else : 
        
            row_nans_header_html    =   "<div>Row Nans</div>"
            rowswithnulls, rowcounts, row_nan_stats_html = display_row_nan_stats(df,False)
            row_nans_html           =   display_df_row_nans(df,rownantable,rowswithnulls,rowcounts,50,False)
            drop_row_nans_html      =   display_drop_rows()
            
            gridclasses     =   ["dfcleanser-common-grid-header",
                                 "dfc-top",
                                 "dfc-main",
                                 "dfc-footer"]
                
            gridhtmls       =   [row_nans_header_html,
                                 row_nan_stats_html,
                                 row_nans_html,
                                 drop_row_nans_html]
            
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :       
                display_generic_grid("df-inspection-nan-wrapper",gridclasses,gridhtmls)
            else :
                display_generic_grid("df-inspection-nan-pop-up-wrapper",gridclasses,gridhtmls)
                
            print("\n")

            col_nans_header_html    =   "<div>Column Nans</div>"
            col_nan_stats_html      =   display_col_nan_stats(df,False)
            col_nans_html           =   display_df_col_nans(df,colnantable,False)
            drop_col_nans_html      =   display_drop_cols()
            
            gridclasses     =   ["dfcleanser-common-grid-header",
                                 "dfc-top",
                                 "dfc-main",
                                 "dfc-footer"]
            
            gridhtmls       =   [col_nans_header_html,
                                 col_nan_stats_html,
                                 col_nans_html,
                                 drop_col_nans_html]
            
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :       
                display_generic_grid("df-inspection-nan-col-wrapper",gridclasses,gridhtmls)
            else :
                display_generic_grid("df-inspection-nan-pop-up-wrapper",gridclasses,gridhtmls)
            

    except Exception as e:
        opstat.store_exception("Error displaying nan data\n ",e)

    clock.stop()
                
    if(not (opstat.get_status())) :
        display_exception(opstat)

            

def display_row_nan_stats(df,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : display row nan stats
    * 
    * Parms :
    *  df           -   dataframe    
    *  display      -   display flag    
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    nanstatsHeader    =   ["",""]
    nanstatsRows      =   []
    nanstatsWidths    =   [75,25]
    nanstatsAligns    =   ["left","left"]
    
    rowcounts       =   0
    rowswithnulls   =   df.isnull().sum(axis=1).tolist()

    for i in range(len(rowswithnulls)) :
        if(rowswithnulls[i] != 0) :
            rowcounts = rowcounts + 1
    
    if(len(rowswithnulls) == 0) :
        nanstatsRows.append(["No Nans Found",""]) 
    else :
        nanstatsRows.append(["Total Nans Found",str(df.isnull().sum().sum())])
        nanstatsRows.append(["Number of Rows containing Nans",str(rowcounts)])
        nanstatsRows.append(["&nbsp;&nbsp;% of Rows containing Nans",
                             "{0:.2f}".format(100*(rowcounts/len(df)))+"%"])
    
    nan_stats_table = dcTable("Row Nan Stats","rownanstatsTable",
                              cfg.DataInspection_ID,
                              nanstatsHeader,nanstatsRows,
                              nanstatsWidths,nanstatsAligns)

    nan_stats_table.set_rowspertable(len(nanstatsRows))
    nan_stats_table.set_small(True)
    nan_stats_table.set_smallwidth(99)
    nan_stats_table.set_smallmargin(2)
    nan_stats_table.set_table_column_parms({"font":12})
    nan_stats_table.set_border(False)
    nan_stats_table.set_checkLength(False)
    
    if(display) :
        nan_stats_table.display_table()
        return(rowswithnulls , rowcounts)
    else :
        table_html  =   nan_stats_table.get_html()
        #nan_stats_table.dump()
        #print(table_html)
        return(rowswithnulls , rowcounts, table_html)


def display_df_row_nans(df,table,rowsnulls,rowcounts,numworstRows,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : display row nans
    * 
    * Parms :
    *  df           -   dataframe    
    *  table           -   table to populate
    *  numworstRows    -   count of worst nan rows
    *  display      -   display flag    
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    numcols         =   len(df.columns)
    numrows         =   len(rowsnulls)
    
    maxsamplerows   =   20
    pctilecounts    =   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    pctilerows      =   [[],[],[],[],[],[],[],[],[],[],
                         [],[],[],[],[],[],[],[],[],[]]
    
    for i in range(len(rowsnulls)) :
        
        if(rowsnulls[i] > 0 ) :
            
            # get pct of nan cols for each row 
            pctnancols = int((rowsnulls[i] / numcols) * 100)
            import math
            pctile = int(math.ceil(pctnancols / 5))
            pctile = 20 - pctile
            
            pctilecounts[pctile] = pctilecounts[pctile] + 1
            if(len(pctilerows[pctile]) < maxsamplerows) :
                pctilerows[pctile].append(i)    
     
    nanrow      =   []
    #nanRefs     =   []
    
    nanRows     =   []
    nanHeaders  =   ["% Nan<br>Cols","Rows<br>Count","% of <br>Rows","Sample Row Ids"]
    nanWidths   =   [15,13,13,59]
    nanAligns   =   ["center","center","center","left"]
    
    for i in range(len(pctilecounts)) :

        if(pctilecounts[i] > 0) :
            nanrow.append(str(100 - (i*5)) + " - " + str(100 - ((i+1)*5)) + " %")
            nanrow.append(str(pctilecounts[i]))
            
            nanrow.append("{0:.2f}".format(100*(pctilecounts[i]/numrows))+"%")
            nanrow.append(str(pctilerows[i]))
        
            nanRows.append(nanrow)
            nanrow = []
        
    table.set_headerList(nanHeaders)
    table.set_rowList(nanRows)
    table.set_widthList(nanWidths)
    table.set_alignList(nanAligns)
    table.set_note("<b>*</b> To drop all rows greater than a threshold set Nan Threshold.")
    
    table.set_rowspertable(len(nanRows))
    table.set_small(True)
    table.set_smallwidth(99)
    table.set_smallmargin(2)

    if(display) :
        table.display_table()
    else :
        table_html = table.get_html()#get_row_major_table(table,SCROLL_NEXT,False)
        return(table_html)


def display_col_nan_stats(df,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : display col nans
    * 
    * Parms :
    *  df           -   dataframe    
    *  display      -   display flag    
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    df_cols         =   df.columns
    df_nulls        =   df.isnull().sum()
    totnullcols     =   0
    
    for i in range(len(df_nulls)) :
        if(not df_nulls[i] == 0) :
            totnullcols = totnullcols + 1
    
    nanstatsHeader    =   ["",""]
    nanstatsRows      =   []
    nanstatsWidths    =   [75,25]
    nanstatsAligns    =   ["left","left"]
    
    if(totnullcols == 0) :
        nanstatsRows.append(["No Nans Found",""]) 
    else :
        nanstatsRows.append(["Total Nans Found",str(df.isnull().sum().sum())])
        nanstatsRows.append(["Number of Cols containing Nans",str(totnullcols)])
        nanstatsRows.append(["&nbsp;&nbsp;% of Cols containing Nans",
                             "{0:.2f}".format(100*(totnullcols/len(df_cols)))+"%"])
    
    nan_stats_table = dcTable("Column Nan Stats","colnanstatsTable",
                              cfg.DataInspection_ID,
                              nanstatsHeader,nanstatsRows,
                              nanstatsWidths,nanstatsAligns)

    nan_stats_table.set_rowspertable(len(nanstatsRows))
    nan_stats_table.set_small(True)
    nan_stats_table.set_smallwidth(99)
    nan_stats_table.set_smallmargin(2)
    nan_stats_table.set_table_column_parms({"font":12})
    nan_stats_table.set_border(False)
    nan_stats_table.set_checkLength(False)
    
    if(display) :
        nan_stats_table.display_table()
    else :
        return(nan_stats_table.get_html())


def display_df_col_nans(df,table,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : display col nans
    * 
    * Parms :
    *  df           -   dataframe    
    *  table        -   table to populate
    *  display      -   display flag    
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    df_cols         =   df.columns
    df_nulls        =   df.isnull().sum().tolist()
    numrows         =   len(df)

    df_nulls_sorted =   [] 
    for i in range(len(df_nulls)) :
        df_nulls_sorted.append(df_nulls[i])
    df_nulls_sorted.sort(reverse=True)
    
    df_cols_sorted  =   []
    
    for i in range(len(df_nulls_sorted)) :
        found = False;
        for j in range(len(df_nulls)) :
            if( not found) :
                if(df_nulls[j] == df_nulls_sorted[i]) :
                    found = True
                    df_nulls[j] = -1
                    df_cols_sorted.append(df_cols[j])
                    
    nanHeader   =   ["Column Name","Nan Row</br>Count","% of </br>Rows"]
    nanWidths   =   [45,30,25]
    nanAligns   =   ["left","center","center"]
    nanRefs     =   ["scol",None,None]
        
    nanRows     =   []
    nanrow      =   []

    for i in range(len(df_nulls_sorted)) :
        
        if(df_nulls_sorted[i] > 0) :
            
            nanrow.append(str(df_cols_sorted[i]))
            nanrow.append(str(df_nulls_sorted[i]))
            nanrow.append("{0:.2f}".format(100*(df_nulls_sorted[i]/numrows))+"%")
            nanRows.append(nanrow)
            nanrow = []
    
    table.set_colsperrow(3)
    table.set_rowspertable(10)
    table.set_maxtables(1)
    
    table.set_headerList(nanHeader)
    table.set_rowList(nanRows)
    table.set_widthList(nanWidths)
    table.set_alignList(nanAligns)
    table.set_refList(nanRefs)
    table.set_note("<b>*</b> To drop all cols greater than a threshold set Nan Threshold.")

    table.set_shortrow(False)
    table.set_tabletype(ROW_MAJOR)

    if(display) :
        get_row_major_table(table,SCROLL_NEXT)
    else :
        return(get_row_major_table(table,SCROLL_NEXT,False))
 

def display_df_row_data(df,table,rowid,colId,opstat,display=True) : #,numworstRows) :
    """
    * -------------------------------------------------------------------------- 
    * function : display row data
    * 
    * Parms :
    *  df           -   dataframe    
    *  table        -   table to populate
    *  rowid        -   row id    
    *  colid        -   col id    
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    if(type(rowid) == str) :
        if(display) :
            display_sample_rows(df,table,int(rowid),int(colId),opstat)
        else :
            return(display_sample_rows(df,table,int(rowid),int(colId),opstat,False))
    else :
        if(display) :
            display_sample_rows(df,table,rowid,colId,opstat)
        else :
            return(display_sample_rows(df,table,rowid,colId,opstat,False))


def display_row_stats(df,dftitle,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : display row data
    * 
    * Parms :
    *  df           -   dataframe    
    *  dftitle      -   dataframe title
    *  display      -   display flag    
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    rowstatsHeader    =   ["",""]
    rowstatsRows      =   []
    rowstatsWidths    =   [80,20]
    rowstatsAligns    =   ["left","left"]
    
    rowstatsRows.append(["Number of Rows in "+ dftitle,str(len(df))])
    #rowstatsRows.append(["&nbsp;","&nbsp;"])#"Number of Unique Row ID Values",str(uniqueRowIdsCount)])
    
    row_stats_table = dcTable("Row Stats","rowstatsTable",
                              cfg.DataInspection_ID,
                              rowstatsHeader,rowstatsRows,
                              rowstatsWidths,rowstatsAligns)

    row_stats_table.set_rowspertable(len(rowstatsRows))
    row_stats_table.set_small(True)
    row_stats_table.set_smallwidth(95)
    row_stats_table.set_smallmargin(2)
    row_stats_table.set_table_column_parms({"font":12})
    row_stats_table.set_border(False)
    row_stats_table.set_checkLength(False)
    
    if(display) :
        row_stats_table.display_table()
    else :
        return(row_stats_table.get_html())


def display_df_categories(df,cattable,catcandidatetable) : 
    """
    * -------------------------------------------------------------------------- 
    * function : display row data
    * 
    * Parms :
    *  df                  -   dataframe    
    *  cattable            -   category table
    *  catcandidatetable   -   category candidate table    
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    df_cols     = df.columns.tolist()
    datatypesList, datatypesCountList, datatypesColsList = get_df_datatypes_data(df)

    uniquesCountList = []
    for i in range(len(df_cols)) :
        uniquesCountList.append(get_num_uniques_by_id(df, df_cols[i]))
                    
    uniquesValsList = []
                
    for i in range(len(df_cols)) :
        if( (uniquesCountList[i] < 25) and 
            (int((uniquesCountList[i]/len(df)*100)) < 20) ) :
            uniquesVals = get_col_uniques_by_id(df,df_cols[i])
            
            if(not (df[df_cols[i]].dtype.name == "category")) :
                uniquesValsList.append(uniquesVals.tolist())
            else :
                uniquesValsList.append(uniquesVals)
        else :
            uniquesValsList.append("None")
                
    catcols                 =   []
    catcandidates           =   []
    catcolsuniques          =   []
    catcandidatesuniques    =   []
                
    for i in range(len(uniquesValsList)) :
        if(df[df_cols[i]].dtype.name == "category") :
            catcols.append(df_cols[i])
            catcolsuniques.append(uniquesValsList[i])
        else :
            if(not (type(uniquesValsList[i]) == str)) :
                if(int((uniquesCountList[i]/len(df)*100)) < 20) :
                    catcandidates.append(df_cols[i])
                    catcandidatesuniques.append(uniquesValsList[i])
        
    nans = []
    for i in range(len(catcandidates)) :
        nans.append(df[catcandidates[i]].isnull().sum())
    #print("\nnans",nans,"\n")
                    
    whitespace = []
    for i in range(len(catcandidatesuniques)) :
        whitespacefound = False

        if(isinstance(catcandidatesuniques[i][0],str)) :
                        
            for j in range(len(catcandidatesuniques[i])) :
                if(isinstance(catcandidatesuniques[i][j],str)) :
                    if( (catcandidatesuniques[i][j][0] == ' ') or 
                         (catcandidatesuniques[i][j][len(catcandidatesuniques[i][j])-1] == ' ') or
                         (catcandidatesuniques[i][j].find("\t") > -1) ):
                        whitespacefound = True
                            
        whitespace.append(whitespacefound)
    
    if(len(catcols) > 0) :

        categoryHeader      =   ["Column Name","Uniques Count","Unique Values"]
        categoryRows        =   []
        categoryHrefs       =   []

        categoryWidths      =   [20,10,70]
        categoryAligns      =   ["left","center","left"]

        categoryrow         =   []

        cattable.set_colsperrow(3)
        cattable.set_rowspertable(50)
        cattable.set_maxtables(1)

        for i in range(len(catcols)) :

            categoryHrefs.append([None,None,None])
            
            categoryrow.append(catcols[i])
            categoryrow.append(len(catcolsuniques[i]))
            categoryrow.append(catcolsuniques[i])
        
            categoryRows.append(categoryrow)
            categoryrow       =   []

        cattable.set_headerList(categoryHeader)
        cattable.set_rowList(categoryRows)
        cattable.set_widthList(categoryWidths)
        cattable.set_alignList(categoryAligns)
        cattable.set_refList(categoryHrefs)
        cattable.set_note("<b>*</b> To select a column click on the column name.")

        cattable.display_table()
        
        print("\n")

        gridclasses     =   ["dfcleanser-common-grid-header",
                             "df-inspection-category-data-wrapper-footer"]
                
        gridhtmls       =   ["<p>Categorical Columns</p>",
                             cattable.get_html()]
                    
        display_generic_grid("df-inspection-category-data-wrapper",gridclasses,gridhtmls)



    if(len(catcandidates) > 0) :
        
        #catcandhref         =   ["scatcol",None,None,None,None,None]
    
        catcandHeader       =   ["Column Name","Column</br>Data Type","Nan</br>Count",
                                 "White</br>Space","Unique</br>Count","Unique Values"]
        catcandRows         =   []
        catcandHrefs        =   []
            
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            catcandWidths       =   [15,15,10,7,8,45]
        else :    
            catcandWidths       =   [20,15,10,10,10,35]
            
        catcandAligns       =   ["left","center","center","center","center","left",]

        catcandrow          =   []
     
        catcandidatetable.set_colsperrow(6)
        catcandidatetable.set_rowspertable(50)
        catcandidatetable.set_maxtables(1)

        for i in range(len(catcandidates)) :

            if( (nans[i] == 0) and (not whitespace[i]) ) :
                catcandHrefs.append(["scatcol",None,None,None,None,None])
            else :
                catcandHrefs.append(["scol",None,None,None,None,None])
            
            catcandrow.append(catcandidates[i])
            catcandrow.append(df[catcandidates[i]].dtype)#]get_datatype_str(get_datatype_id(catcandidatesuniques[i][0])))
            catcandrow.append(str(nans[i]))
            catcandrow.append(str(whitespace[i]))
            catcandrow.append(len(catcandidatesuniques[i]))
            catcandrow.append(catcandidatesuniques[i])
        
            catcandRows.append(catcandrow)
            catcandrow       =   []
            
        catcandidatetable.set_headerList(catcandHeader)
        catcandidatetable.set_rowList(catcandRows)
        catcandidatetable.set_widthList(catcandWidths)
        catcandidatetable.set_alignList(catcandAligns)
        catcandidatetable.set_refList(catcandHrefs)
        catcandidatetable.set_note("<b>*</b> To select a column click on the column name.")
        catcandidatetable.set_checkLength(False)
        
        if(len(catcandRows) > 0) :
            
            gridclasses     =   ["dfcleanser-common-grid-header","df-inspection-category-data-wrapper-footer"]
            gridhtmls       =   ["<div>Categorical Candidate Columns</div>",catcandidatetable.get_html()]
             
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                display_generic_grid("df-inspection-category-data-wrapper",gridclasses,gridhtmls)
            else :
                display_generic_grid("df-inspection-category-data-pop-up-wrapper",gridclasses,gridhtmls)
            
            #catcandidatetable.display_table()
        else :
            display_status("no Candidate Category Columns found",1)
            
    else :
        display_status("no Candidate Category Columns found",1)
        
    return(len(catcols), len(catcandidates))

    
    
    
    