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
import dfcleanser.data_inspection.data_inspection_model as dim

from dfcleanser.common.common_utils import (get_col_num_uniques, RunningClock, get_datatype_id,
                                            get_col_uniques, display_status, display_grid_status, opStatus, 
                                            display_exception, display_generic_grid, is_numeric_col,
                                            get_select_defaults, displayParms, is_categorical_col)

from dfcleanser.common.html_widgets import (InputForm, ButtonGroupForm)

from dfcleanser.common.table_widgets import (dcTable, ROW_MAJOR, get_row_major_table,SCROLL_DOWN)

from dfcleanser.common.display_utils import (display_sample_rows)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   data inspection form components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    data inspection task bar
#--------------------------------------------------------------------------
"""
data_inspection_tb_doc_title       =   "Inspection Options"
data_inspection_tb_title           =   "Inspection Options"
data_inspection_tb_id              =   "inspectionoptionstb"

data_inspection_tb_keyTitleList    =   ["Data</br>Types","Nans","Rows","Columns","Categories","Clear","Reset","Help"]

data_inspection_tb_jsList          =   ["inspection_task_bar_callback(" + str(dim.DISPLAY_DATATYPES_OPTION) + ")",
                                        "inspection_task_bar_callback(" + str(dim.DISPLAY_NANS_OPTION) + ")",
                                        "inspection_task_bar_callback(" + str(dim.DISPLAY_ROWS_OPTION) + ")",
                                        "inspection_task_bar_callback(" + str(dim.DISPLAY_COLS_OPTION) + ")",
                                        "inspection_task_bar_callback(" + str(dim.DISPLAY_CATEGORIES_OPTION) + ")",
                                        "inspection_task_bar_callback(" + str(dim.MAIN_OPTION) + ")",
                                        "process_pop_up_cmd(6)",
                                        "displayhelp('" + str(dfchelp.INSPECT_MAIN_TASKBAR_ID) + "')"]

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
data_subset_df_input_id                   =   "datasubsetdf"



"""
#--------------------------------------------------------------------------
#    column search data  
#--------------------------------------------------------------------------
"""
data_inspection_colsearch_title            =   "Column Values To Search For"
data_inspection_colsearch_id               =   "datainspectcolsearch"
data_inspection_colsearch_idList           =   ["colsearchoutdf",
                                                "colsearchnames",
                                                "colsearchvalues0",
                                                "colsearchvalues1",
                                                "colsearchvalues2",
                                                None,None,None,None]

data_inspection_colsearch_labelList        =   ["df_output_title",
                                                "column_names",
                                                "column_values",
                                                "column_values",
                                                "column_values",
                                                "Get Rows</br> Matching</br>Numeric</br>colunm_values",
                                                "Get </br>Non Numeric</br>Colunms",
                                                "Return","Help"]

data_inspection_colsearch_typeList         =   ["text","selectmultiple","text","text","text","button","button","button","button"]

data_inspection_colsearch_placeholderList  =   ["df title to put search results in",
                                                "columns to search in",
                                                "numeric column values list to search for [0, ...] ",
                                                "numeric column values list to search for [0, ...] ",
                                                "numeric column values list to search for [0, ...] ",
                                                None,None,None,None]

data_inspection_colsearch_jsList           =   [None,None,None,None,None,
                                                "get_col_rows_callback(0)",
                                                "get_col_rows_callback(1)",
                                                "inspection_task_bar_callback(1)",
                                                "displayhelp('" + str(dfchelp.INSPECT_ROW_SEARCH_ID) + "')"]

data_inspection_colsearch_reqList          =   [0,1,2]

data_inspection_colsearch_form             =   [data_inspection_colsearch_id,
                                               data_inspection_colsearch_idList,
                                               data_inspection_df_input_labelList,
                                               data_inspection_colsearch_typeList,
                                               data_inspection_colsearch_placeholderList,
                                               data_inspection_colsearch_jsList,
                                               data_inspection_colsearch_reqList]  


data_inspection_nn_colsearch_title         =   "Column Values To Search For"
data_inspection_nn_colsearch_id            =   "datainspectcolsearch"
data_inspection_nn_colsearch_idList        =   ["colsearchoutdf",
                                                "colsearchnames",
                                                "colsearchvalues0",
                                                "colsearchvalues1",
                                                "colsearchvalues2",
                                                None,None,None,None]

data_inspection_nn_colsearch_labelList     =   ["df_output_title",
                                                "column_names",
                                                "column_values",
                                                "column_values",
                                                "column_values",
                                                "Get Rows</br> Matching</br>string</br>colunm_values",
                                                "Get </br>Numeric</br>Colunms",
                                                "Return","Help"]

data_inspection_nn_colsearch_typeList      =   ["text","selectmultiple","text","text","text","button","button","button","button"]

data_inspection_nn_colsearch_placeholderList=   ["df title to put search results in",
                                                 "columns to search in",
                                                "string column values list to search for [0, ...] ",
                                                "string column values list to search for [0, ...] ",
                                                "string column values list to search for [0, ...] ",
                                                None,None,None,None]

data_inspection_nn_colsearch_jsList        =   [None,None,None,None,None,
                                                "get_col_rows_callback(2)",
                                                "get_col_rows_callback(3)",
                                                "inspection_task_bar_callback(1)",
                                                "displayhelp('" + str(dfchelp.INSPECT_ROW_NN_SEARCH_ID) + "')"]

data_inspection_nn_colsearch_reqList       =   [0,1,2]

data_inspection_nn_colsearch_form          =   [data_inspection_nn_colsearch_id,
                                               data_inspection_nn_colsearch_idList,
                                               data_inspection_nn_colsearch_labelList,
                                               data_inspection_nn_colsearch_typeList,
                                               data_inspection_nn_colsearch_placeholderList,
                                               data_inspection_nn_colsearch_jsList,
                                               data_inspection_nn_colsearch_reqList]  

"""
#--------------------------------------------------------------------------
#    drop rows input form
#--------------------------------------------------------------------------
"""
drop_rows_input_title                =   ""
drop_rows_input_id                   =   "droprowsinput"
drop_rows_input_idList               =   ["droprowthreshold",None,None,None]

drop_rows_input_labelList            =   ["Nan_Threshold",
                                          "Drop Rows </br> with % of Cols</br>  > Threshold",
                                          "Drop Rows </br> with Nan Count</br>  > Threshold",
                                          "Help"]

drop_rows_input_typeList             =   ["text","button","button","button"]

drop_rows_input_placeholderList      =   ["",None,None,None]

drop_rows_input_jsList               =   [None,
                                          "dc_drop_rows_callback(0)",
                                          "dc_drop_rows_callback(1)",
                                          "displayhelp('" + str(dfchelp.INSPECT_ROW_NANS_ID) + "')"]

drop_rows_input_reqList              =   [0]

drop_rows_input_short                =   True

drop_columns_input_title                =   ""
drop_columns_input_id                   =   "dropcolsinput"
drop_columns_input_idList               =   ["dropcolthreshold",None,None,None]

drop_columns_input_labelList            =   ["Nan_Threshold",
                                             "Drop Columns </br> with % of Rows</br>  > Threshold",
                                             "Drop Columns </br> with Nan</br>Row Count</br>  > Threshold",
                                             "Help"]

drop_columns_input_typeList             =   ["text","button","button","button"]

drop_columns_input_placeholderList      =   ["",None,None,None]

drop_columns_input_jsList               =   [None,
                                            "dc_drop_cols_callback(0)",
                                            "dc_drop_cols_callback(1)",
                                            "displayhelp('" + str(dfchelp.INSPECT_COL_NANS_ID) + "')"]

drop_columns_input_reqList              =   [0]


"""
#--------------------------------------------------------------------------
#    open dataframe in excel
#--------------------------------------------------------------------------
"""
data_inspection_open_excel_tb_doc_title       =   "Inspection open_excel"
data_inspection_open_excel_tb_title           =   "Inspection open_excel"
data_inspection_open_excel_tb_id              =   "inspectiondfopen_exceltb"

data_inspection_open_excel_tb_keyTitleList    =   ["Open Dataframe In Excel"]

data_inspection_open_excel_tb_jsList          =   ["inspection_task_bar_callback("+str(dim.OPEN_EXCEL_OPTION)+")"]

data_inspection_open_excel_tb_centered        =   True


datainspection_inputs       =   [data_inspection_df_input_id,data_inspection_colsearch_id,
                                 data_inspection_nn_colsearch_id,drop_rows_input_id,drop_columns_input_id]

"""
#--------------------------------------------------------------------------
#    full column names list   
#--------------------------------------------------------------------------
"""
full_col_names_input_title                  =   "Full Names List"
full_col_names_input_id                     =   "datainspectfull"
full_col_names_input_idList                 =   ["dffullnames"]

full_col_names_input_labelList              =   ["column_names"]

full_col_names_input_typeList               =   ["select"]

full_col_names_input_placeholderList        =   ["column names"]

full_col_names_input_jsList                 =   [None]

full_col_names_input_reqList                =   [0]

full_col_names_input_form                   =   [full_col_names_input_id,
                                                 full_col_names_input_idList,
                                                 full_col_names_input_labelList,
                                                 full_col_names_input_typeList,
                                                 full_col_names_input_placeholderList,
                                                 full_col_names_input_jsList,
                                                 full_col_names_input_reqList]  

"""
#--------------------------------------------------------------------------
#    inspect numeric column select form   
#--------------------------------------------------------------------------
"""
inspect_col_input_title                =   ""
inspect_col_input_id                   =   "inspectcolsinput"
inspect_col_input_idList               =   ["inspectcolname",
                                            None,None,None,None]

inspect_col_input_labelList            =   ["column_name",
                                            "Display</br>Graphs",
                                            "Display</br>Outliers",
                                            "Cleanse</br>Column",
                                            "Return"]

inspect_col_input_typeList             =   ["select","button","button","button","button"]

inspect_col_input_placeholderList      =   ["",None,None,None,None]

inspect_col_input_jsList               =   [None,
                                            "inspection_task_bar_callback(" + str(dim.DISPLAY_COL_GRAPHS) + ")",
                                            "inspection_task_bar_callback(" + str(dim.DISPLAY_COL_OUTLIERS) + ")",
                                            "inspection_task_bar_callback(" + str(dim.CLEANSE_COLUMN) + ")",
                                            "inspection_task_bar_callback(" + str(dim.MAIN_OPTION) + ")"]

inspect_col_input_reqList              =   [0]


"""
#--------------------------------------------------------------------------
#    inspect non numeric column select form   
#--------------------------------------------------------------------------
"""
inspect_nn_col_input_title                =   ""
inspect_nn_col_input_id                   =   "inspectcolsinput"
inspect_nn_col_input_idList               =   ["inspectcolname",
                                               None,None]

inspect_nn_col_input_labelList            =   ["column_name",
                                               "Cleanse</br>Column",
                                               "Return"]

inspect_nn_col_input_typeList             =   ["select","button","button"]

inspect_nn_col_input_placeholderList      =   ["",None,None]

inspect_nn_col_input_jsList               =   [None,
                                               "inspection_task_bar_callback(" + str(dim.CLEANSE_COLUMN) + ")",
                                               "inspection_task_bar_callback(" + str(dim.MAIN_OPTION) + ")"]

inspect_nn_col_input_reqList              =   [0]


datainspection_inputs       =   [data_inspection_df_input_id, data_inspection_colsearch_id, data_inspection_nn_colsearch_id,
                                 drop_rows_input_id, full_col_names_input_id, inspect_col_input_id, inspect_nn_col_input_id]


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


def get_inspection_openexcel_taskbar() :
    
    return(ButtonGroupForm(data_inspection_open_excel_tb_id,
                           data_inspection_open_excel_tb_keyTitleList,
                           data_inspection_open_excel_tb_jsList,
                           data_inspection_open_excel_tb_centered))


def display_dfc_inspection_main() :
    """
    * -------------------------------------------------------------------------- 
    * function : display the dfc inspection taskbar and select forms
    * 
    * parms :
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    display_inspection_main_taskbar()
    cfg.display_data_select_df(cfg.DataInspection_ID)

    import matplotlib.pyplot as plt



def get_colsearch_form(df,numeric=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : display column search form
    * 
    * Parms :
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    if(numeric) :
        colsearch_form  =   InputForm(data_inspection_colsearch_id,
                                      data_inspection_colsearch_idList,
                                      data_inspection_colsearch_labelList,
                                      data_inspection_colsearch_typeList,
                                      data_inspection_colsearch_placeholderList,
                                      data_inspection_colsearch_jsList,
                                      data_inspection_colsearch_reqList)
    else :
        colsearch_form  =   InputForm(data_inspection_nn_colsearch_id,
                                      data_inspection_nn_colsearch_idList,
                                      data_inspection_nn_colsearch_labelList,
                                      data_inspection_nn_colsearch_typeList,
                                      data_inspection_nn_colsearch_placeholderList,
                                      data_inspection_nn_colsearch_jsList,
                                      data_inspection_nn_colsearch_reqList)
    
    colnames    =   df.columns.tolist()
    col_names   =   []
    
    from dfcleanser.common.common_utils import is_numeric_col, is_string_col, is_object_col
    
    for i in range(len(colnames)) :
        
        if(numeric) :
            if(is_numeric_col(df,colnames[i])) :
                col_names.append(colnames[i])
        else :
            if( (is_string_col(df,colnames[i])) or (is_object_col(df,colnames[i])) ) :
                col_names.append(colnames[i]) 
    
    if(len(col_names) > 0) : 
        
        col_names_list  =   ["None"]
        for i in range(len(col_names)) :
            col_names_list.append(col_names[i])
            
        cnames      =   {'default': col_names_list[0], 'list': col_names_list,"callback":"change_colsearch_cols", "size":10}
    else :
        cnames      =   {'default': "None", 'list': ["None"]}

    selectDicts     =   []
    selectDicts.append(cnames)

    if(numeric) :
        get_select_defaults(colsearch_form,
                            data_inspection_colsearch_id,
                            data_inspection_colsearch_idList,
                            data_inspection_colsearch_typeList,
                            selectDicts)
    else :
        get_select_defaults(colsearch_form,
                            data_inspection_nn_colsearch_id,
                            data_inspection_nn_colsearch_idList,
                            data_inspection_nn_colsearch_typeList,
                            selectDicts)

    colsearch_form.set_shortForm(True)
    colsearch_form.set_gridwidth(480)
    colsearch_form.set_buttonstyle({"font-size":12, "height":90, "width":110, "left-margin":5})
    colsearch_form.set_fullparms(True)
    
    return(colsearch_form)


"""            
#------------------------------------------------------------------
#   display data inspection header
#------------------------------------------------------------------
"""           
def display_df_size_data(display=True,forExport=False) :
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
        values  =   [str(len(cfg.get_current_chapter_df(cfg.DataInspection_ID))),
                     str(len(cfg.get_current_chapter_df(cfg.DataInspection_ID).columns))]
        
        if(display) :
            displayParms("&nbsp;dataframe Imported",labels,values,"inspectdata",width=None)
        else :
            if(forExport) :
                return(displayParms("&nbsp;dataframe Exported",labels,values,"inspectdata",100,0,False))
            else :
                return(displayParms("&nbsp;dataframe Imported",labels,values,"inspectdata",100,0,False))
            
    else :
        display_grid_status("No dataframe imported to select", 1)


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
    
    drop_form.set_buttonstyle({"font-size":12, "height":75, "width":110, "left-margin":1})
    drop_form.set_gridwidth(360)
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
    
    drop_form.set_buttonstyle({"font-size":12, "height":75, "width":110, "left-margin":1})
    drop_form.set_gridwidth(360)    
    return(drop_form.get_html())


"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   specific data inspection display routines
#------------------------------------------------------------------
#------------------------------------------------------------------
"""       

def display_df_datatypes(table,dtypes_list,colnames_count_list,colnames_dict,optionid,display=True) : 
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

    #print("display_df_datatypes\n",dtypes_list,"\n",colnames_count_list,"\n",colnames_dict)

    if(not(optionid == dim.DISPLAY_FULL_COLUMN_NAMES)) :
        
        dtypesHeader   =   ["Data Type","Count","Column Names"]
        dtypesRows     =   []
        dtypesHrefs    =   []

        dtypesWidths   =   [25,10,65]
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
        
            dtypes_col_names    =  colnames_dict.get(dtypes_list[i]) 
            if(len(dtypes_col_names) < 40) :
                dtypesrow.append(colnames_dict.get(dtypes_list[i]))
            else :

                colnames_str    =   ""
                for i in range(40) :
                    colnames_str    =   (colnames_str + dtypes_col_names[i] + ",")
                colnames_str    =   (colnames_str + "<a onclick='get_columns_name_list()'><span style = 'font-size:14px; font-wight:bold;'> ... More ...<span></a>")
                dtypesrow.append(colnames_str)
        
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
            
    else :
        
        names_html  =   ""
        
        for i in range(len(dtypes_list)) :
            
            if(dtypes_list[i] == "datetime64[ns]") :
                title_type  =   ("[datetime.datetime]")
            elif(dtypes_list[i] == "timedelta64[ns]") :
                title_type  =   ("[datetime.timedelta]")
            else :
                title_type  =   ("["+str(dtypes_list[i])+"]")
                
            full_names_list_form  =   InputForm(full_col_names_input_id,
                                                full_col_names_input_idList,
                                                [title_type],
                                                full_col_names_input_typeList,
                                                full_col_names_input_placeholderList,
                                                full_col_names_input_jsList,
                                                full_col_names_input_reqList)

            selectDicts     =   []
            new_col_names_dict         =   {"default":None,"list":colnames_dict.get(dtypes_list[i]),"size":40}
            selectDicts.append(new_col_names_dict)  
            
            full_names_list_form.set_gridwidth(480)
        
        
            get_select_defaults(full_names_list_form,
                                full_col_names_input_id,
                                full_col_names_input_idList,
                                full_col_names_input_typeList,
                                selectDicts)
            
            #print("get_hml dtypes",full_names_list_form.dump())
            
            try :
                names_html  =   (names_html + full_names_list_form.get_html() + "<br>")
            except :
                print("shit")    
        
        return(names_html)

    
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
        
            row_nans_header_html    =   "<div>Row Nans</div><br>"
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
                display_generic_grid("df-inspection-nan-wrapper",gridclasses,gridhtmls,True)
                
            print("\n")

            col_nans_header_html    =   "<div>Column Nans</div><br>"
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
                display_generic_grid("df-inspection-nan-wrapper",gridclasses,gridhtmls)
            else :
                display_generic_grid("df-inspection-nan-wrapper",gridclasses,gridhtmls,True)
            

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
        nanstatsRows.append(["Total Rows",str(len(df))])
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
        table_html = table.get_html()
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
        nanstatsRows.append(["Total Columns",str(len(df.columns))])
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
        get_row_major_table(table,SCROLL_DOWN)
    else :
        return(get_row_major_table(table,SCROLL_DOWN,False))
 

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
    
    row_stats_table = dcTable("Row Stats","rowstatsTable",
                              cfg.DataInspection_ID,
                              rowstatsHeader,rowstatsRows,
                              rowstatsWidths,rowstatsAligns)

    row_stats_table.set_rowspertable(len(rowstatsRows))
    row_stats_table.set_small(True)
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        row_stats_table.set_smallwidth(50)
        row_stats_table.set_smallmargin(240)
    else :
        row_stats_table.set_smallwidth(98)
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
    
    import pandas as pd

    df_cols     = df.columns.tolist()
    datatypesList, datatypesCountList, datatypesColsList = dim.get_df_datatypes_data(df)

    uniquesCountList = []
    for i in range(len(df_cols)) :
        uniquesCountList.append(get_col_num_uniques(df, df_cols[i]))
                    
    uniquesValsList = []
                
    for i in range(len(df_cols)) :
        if( (uniquesCountList[i] < 25) and 
            (int((uniquesCountList[i]/len(df)*100)) < 20) ) :
            uniquesVals = get_col_uniques(df,df_cols[i])
            
            if(not (is_categorical_col(df,df_cols[i])) ) :
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
        if(is_categorical_col(df,df_cols[i])) :
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

        categoryHeader      =   ["Column Name","Ordered","Categories"]
        categoryRows        =   []
        categoryHrefs       =   []

        categoryWidths      =   [20,10,70]
        categoryAligns      =   ["left","center","left"]

        categoryrow         =   []

        cattable.set_colsperrow(4)
        cattable.set_rowspertable(50)
        cattable.set_maxtables(1)

        for i in range(len(catcols)) :

            categoryHrefs.append(["process_category_column",None,None])
            
            CI  =   pd.CategoricalIndex(df[catcols[i]])
            
            categoryrow.append(catcols[i])
            categoryrow.append(str(CI.ordered))
            categoryrow.append(str(CI.categories.tolist()))
        
            categoryRows.append(categoryrow)
            categoryrow       =   []

        cattable.set_headerList(categoryHeader)
        cattable.set_rowList(categoryRows)
        cattable.set_widthList(categoryWidths)
        cattable.set_alignList(categoryAligns)
        cattable.set_refList(categoryHrefs)
        cattable.set_note("<b>*</b> To select a column click on the column name.")

        #cattable.display_table()
        
        print("\n")

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
        gridhtmls       =   ["<div>Categorical Columns</div>",cattable.get_html()]
                    
        display_generic_grid("df-inspection-category-data-wrapper",gridclasses,gridhtmls)

    # category candidate table
    if(len(catcandidates) > 0) :
        
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
                catcandHrefs.append(["scatcol",None,None,None,None,None])
            
            catcandrow.append(catcandidates[i])
            catcandrow.append(df[catcandidates[i]].dtype)
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
            
            gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
            gridhtmls       =   ["<div>Categorical Candidate Columns</div>",catcandidatetable.get_html()]
             
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                display_generic_grid("df-inspection-category-data-wrapper",gridclasses,gridhtmls)
            else :
                display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls,True)
            
            #catcandidatetable.display_table()
        else :
            display_status("no Candidate Category Columns found")
            
    else :
        display_status("no Candidate Category Columns found")
        
    return(len(catcols), len(catcandidates))


def display_common_graphs(colname) :
    """
    * -------------------------------------------------------------------------- 
    * function : display numeric column data
    * 
    * parms :
    *   colname     -   column name
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    clock = RunningClock()
    clock.start()

    try :
        
        try :
            import os
            os.remove("hist.png")
            os.remove("zscore.png")
        except :
            df = None   
        
        df = cfg.get_current_chapter_df(cfg.DataInspection_ID)
        
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
        fig.savefig("hist.png")
        plt.close()
        
        cmean       =   df[colname].mean() 
        cstd        =   df[colname].std()

        zscores      =   []
        for i in range(len(dfuniques)) :
            zscores.append((dfuniques[i]-cmean)/cstd)
        
        # dictionary of lists  
        zdict = {'ZScore': zscores, 'Frequency': ucounts}  
    
        import pandas as pd
        zdf     =   pd.DataFrame(zdict)     
        ax = zdf.plot(x='ZScore', y='Frequency', kind='kde', figsize=(10, 6))
        fig1    =   ax.get_figure()
        arr = ax.get_children()[0]._x
        plt.xticks(np.linspace(arr[0], arr[-1]), rotation=90)
        plt.title("'" + colname + "'" + " ZScores")
        fig1.savefig("zscore.png")
        plt.close()
        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right"]
        
        title_html      =   "<div>Column Graphs</div>"
        hist_html       =   "<br><br><img src='hist.png' alt='Histogram' height='400' width='400'>"
        zscore_html     =   "<img src='zscore.png' alt='ZScores' height='480' width='640'>"
        
        gridhtmls       =   [title_html,hist_html,zscore_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("display-dfcleansing-graphs-wrapper",gridclasses,gridhtmls)
        else :
            gridclasses     =   ["dfcleanser-common-grid-header","dfc-top","dfc-footer"]
            display_generic_grid("display-dfcleansing-graphs-pop-up-wrapper",gridclasses,gridhtmls)
        
    except Exception as e: 
        opstat = opStatus()
        opstat.store_exception("Unable to plot column",e)
        display_exception(opstat)

    clock.stop()

   
def get_simple_col_outliers(df,colname) :
    """
    * -------------------------------------------------------------------------- 
    * function : get a simplelist of outliers based on stddev from means
    * 
    * parms :
    *   df       -   dataframe
    *   colname  -   column name
    *
    * returns : 
    *  outliers
    * --------------------------------------------------------
    """

    outliers        =   []
    outlierscount   =   []
    
    numstddevs      =   15
    
    for i in range(numstddevs) :
        outliers.append([])
        outlierscount.append(0)
    
    mean    =   df[colname].mean()
    std     =   df[colname].std()
    
    counts  =   df[colname].value_counts().to_dict()
    uniques =   list(counts.keys())
    
    if(is_numeric_col(df,colname)) :
        uniques.sort()

    for i in range(len(uniques)) :
        import pandas as pd
        if( not pd.isnull(uniques[i])) :
            difference = abs(mean - uniques[i])
        
            import math
            outindex = math.floor(difference / std)
            outlierscount[outindex] = outlierscount[outindex] + counts.get(uniques[i])
    
    return(outlierscount)        

    
def get_simple_outliers(df,colname,opstat,display=True) :  
    """
    * -------------------------------------------------------------------------- 
    * function : get simple outliers
    * 
    * parms :
    *   df          -   dataframe
    *   colname    -   column name
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    clock = RunningClock()
    clock.start()
        
    totrows     =   len(df)
    
    std         =   df[colname].std()
    mean        =   df[colname].mean()
    minv        =   df[colname].min()
    maxv        =   df[colname].max()

    Red     = "#FAA78F"
    Green   = "#8FFAC0"
    Yellow  = "#FAFB95"

    try :
        
        outliersCount = get_simple_col_outliers(df,colname)
            
        outHeader    =   ["Num</br>std devs</br>from Mean","Count","% Total</br>Values","Values Range"]
        outRows      =   []
        outWidths    =   [10,10,15,65]
        outAligns    =   ["center","center","center","left"]
        colorList    =   []    
        
        for i in range(len(outliersCount)) :

            outrow      =   []
            colorRow    =   []
            
            if(outliersCount[i] > 0) :
                outrow.append(i)
                outrow.append(str(outliersCount[i]))
                outrow.append(float("{0:.5f}".format(100 * (outliersCount[i] / totrows))))
                if(i == 0) :
                    outrow.append("{0:.2f}".format(mean - ((i+1)*std)) + " - " + "{0:.2f}".format(mean + ((i+1)*std)))
                    colorRow = [Green,Green,Green,Green]

                else :

                    lowermin = mean - ((i+1)*std)
                    lowermax = mean - ((i)*std)
                    if(lowermin < minv) : lowermin = minv
                    if(lowermax < minv) : lowermax = minv
                    
                    uppermin = mean + ((i)*std)
                    uppermax = mean + ((i+1)*std)
                    if(uppermin > maxv) : uppermin = maxv
                    if(uppermax > maxv) : uppermax = maxv
                    
                    rangestr    =   ""
                    rangestr1   =   ""
                    
                    if(lowermax > minv) :
                        rangestr = "{0:.2f}".format(lowermin) + " - " + "{0:.2f}".format(lowermax)
                    if(uppermin < maxv) :
                        rangestr1 = rangestr1 + "{0:.2f}".format(uppermin) + " - " + "{0:.2f}".format(uppermax)
                    
                    if( (len(rangestr) > 0) and (len(rangestr1) > 0) ) :
                            rangestr = rangestr + "  and  " + rangestr1
                    else :
                        rangestr = rangestr + rangestr1
                    
                    outrow.append(rangestr)
                    if(i > 2) :
                        colorRow = [Red,Red,Red,Red]
                    else :
                        colorRow = [Yellow,Yellow,Yellow,Yellow]
                    
                outRows.append(outrow)
                colorList.append(colorRow)
          

        outliers_table = dcTable("Simple Outliers","simpleoutliers",cfg.DataCleansing_ID,
                                 outHeader,outRows,outWidths,outAligns)
        
        outliers_table.set_colsperrow(4)
        outliers_table.set_rowspertable(30)
        outliers_table.set_maxtables(1)
        outliers_table.set_checkLength(False)
        outliers_table.set_color(True)
        outliers_table.set_colorList(colorList)
        
        clock.stop() 
        
        if(display) :
            outliers_table.display_table()
            return()
        else :
            outliers_html   =   outliers_table.get_html()
            return(outliers_html)
            
            
    except Exception as e: 
        opstat = opStatus()
        opstat.store_exception("Unable to get simple outliers",e)
        display_exception(opstat)

    clock.stop() 
           





    