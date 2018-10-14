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
#import dfcleanser.data_inspection.data_inspection_model as dim

from dfcleanser.common.common_utils import (get_num_uniques_by_id, RunningClock, get_parms_for_input, 
                                            get_col_uniques_by_id, new_line, displayHTML)

from dfcleanser.common.html_widgets import (display_composite_form, get_button_tb_form, InputForm, 
                                            get_checkbox_form, displayHeading,
                                            get_input_form, CheckboxGroupForm, ButtonGroupForm)

from dfcleanser.common.table_widgets import (dcTable, ROW_MAJOR, get_row_major_table, SCROLL_NEXT)

from dfcleanser.common.display_utils import (get_df_datatypes_data, display_sample_row, get_datatype_id)

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    data inspection cfg variables
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


def     get_cbox_flag(id) :
    
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

data_inspection_tb_keyTitleList    =   ["Inspect Data","Clear","Help"]

data_inspection_tb_jsList          =   ["inspection_task_bar_callback(0)",
                                        "inspection_task_bar_callback(1)",
                                        "displayhelp(" + str(dfchelp.INSPECT_MAIN_TASKBAR_ID) + ")"]

data_inspection_tb_centered        =   False

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
                                             "Drop Columns </br> with Nan Row Count</br>  > Threshold"]

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
def get_inspection_main_taskbar() :
    return(get_button_tb_form(ButtonGroupForm(data_inspection_tb_id,
                                              data_inspection_tb_keyTitleList,
                                              data_inspection_tb_jsList,
                                              data_inspection_tb_centered)))

def get_inspection_dfschema_taskbar() :
    return(get_button_tb_form(ButtonGroupForm(data_inspection_dfschema_tb_id,
                                              data_inspection_dfschema_tb_keyTitleList,
                                              data_inspection_dfschema_tb_jsList,
                                              data_inspection_dfschema_tb_centered)))

def get_inspection_check_form_parms(parms,current_checkboxes) :
    
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

    main_inspection_checkbox    =  CheckboxGroupForm(main_inspection_checkbox_id,
                                                     main_inspection_checkbox_idList,
                                                     main_inspection_checkbox_labelList,
                                                     main_inspection_checkbox_jsList,
                                                     current_checkboxes,
                                                     [0,0,0,0,0])

    inspection_checkboxForm = get_checkbox_form("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Inspection Options",
                                                main_inspection_checkbox)
    
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



def display_inspection_html(title) :

    status_html = ""
    status_html = (status_html + '<div class="container status-header" style="width:20%; margin-left:25px; margin-bottom:5px; ">' + new_line)
    status_html = (status_html + '    <div class="row" style="margin-bottom:0px;">' + new_line)
    status_html = (status_html + '        <div class="panel panel-primary" style="border:0px; margin-bottom:0px;">' + new_line)
    status_html = (status_html + '            <div class="panel-heading dc-table-panel-heading" style="height:40px; margin-bottom:0px;">' + new_line)
    status_html = (status_html + '                <div class="input-group">' + new_line)
    status_html = (status_html + '                    <p class="dc-table-title">' + title + '</p>' + new_line)
    status_html = (status_html + '                </div>' + new_line)
    status_html = (status_html + '            </div>' + new_line)
    status_html = (status_html + '        </div>' + new_line) 
    status_html = (status_html + '    </div>' + new_line) 
    status_html = (status_html + '</div>')

    displayHTML(status_html)

"""            
#------------------------------------------------------------------
#   display data inspection header
#------------------------------------------------------------------
"""           
def display_inspection_data() :
    
    if(cfg.is_dc_dataframe_loaded()) :
        display_inspection_html("dataframe Imported")
        print("         [NUMBER OF ROWS] :",len(cfg.get_dc_dataframe()),flush=True)
        print("         [NUMBER OF COLS] :",len(cfg.get_dc_dataframe().columns))
    else :
        display_inspection_html("No dataframe imported yet")


"""            
#------------------------------------------------------------------
#   display drop nan rows threshold form 
#------------------------------------------------------------------
""" 
def display_drop_rows() :
    
    display_composite_form([get_input_form(InputForm(drop_rows_input_id,
                                                     drop_rows_input_idList,
                                                     drop_rows_input_labelList,
                                                     drop_rows_input_typeList,
                                                     drop_rows_input_placeholderList,
                                                     drop_rows_input_jsList,
                                                     drop_rows_input_reqList,
                                                     drop_rows_input_short))]) 
    
"""            
#------------------------------------------------------------------
#   display drop nan cols threshold form 
#------------------------------------------------------------------
""" 
def display_drop_cols() :
    
    display_composite_form([get_input_form(InputForm(drop_columns_input_id,
                                                     drop_columns_input_idList,
                                                     drop_columns_input_labelList,
                                                     drop_columns_input_typeList,
                                                     drop_columns_input_placeholderList,
                                                     drop_columns_input_jsList,
                                                     drop_columns_input_reqList,
                                                     True))]) 

"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   specific data inspection display routines
#------------------------------------------------------------------
#------------------------------------------------------------------
"""       

"""            
#------------------------------------------------------------------
#   display datatypes  
#
#       dtypes_list         -   list of datatype
#       colnames_count_list -   list of colnames count for datatype
#       colnames_list       -   list of colnames for datatype
#
#------------------------------------------------------------------
""" 
def display_df_datatypes(table,dtypes_list,colnames_count_list,colnames_dict) : 

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
    table.set_textLength(25) 
    
    table.set_note("<b>*</b> To perform group actions on a specific data type click on the data type above.")
    
    table.display_table()

    
"""            
#------------------------------------------------------------------
#   display null data info for a dataframe
#
#   df              -   dataframe
#
#------------------------------------------------------------------
"""
def display_null_data(df,rownantable,colnantable,rowsize) :
    
    df_cols         =   df.columns
    df_nulls        =   df.isnull().sum()
    totnullcols     =   0
    
    df_nulls_dict   =   {}

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
        
        displayHeading("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Row NaNs",4)
        
        clock = RunningClock()
        clock.start()

        #print("\n")
        rowswithnulls, rowcounts = display_row_nan_stats(df)
        display_df_row_nans(df,rownantable,rowswithnulls,rowcounts,50)
        from dfcleanser.data_inspection.data_inspection_widgets import display_drop_rows
        display_drop_rows()
        
        clock.stop()
        
        print("\n")
        
        displayHeading("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Column NaNs",4)
        
        clock = RunningClock()
        clock.start()

        #print("\n")
        display_col_nan_stats(df)
        display_df_col_nans(df,colnantable)
        from dfcleanser.data_inspection.data_inspection_widgets import display_drop_cols
        display_drop_cols()

        clock.stop()
            
"""            
#------------------------------------------------------------------
#   display row nan stats
#
#   df              -   dataframe
#
#------------------------------------------------------------------
"""
def display_row_nan_stats(df) :
    
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
    nan_stats_table.set_smallwidth(35)
    nan_stats_table.set_smallmargin(32)
    nan_stats_table.set_smallfsize(12)
    nan_stats_table.set_border(False)
    nan_stats_table.set_checkLength(False)
    
    nan_stats_table.display_table()
    
    return(rowswithnulls , rowcounts)


"""            
#------------------------------------------------------------------
#   display row nans  
#
#       df              -   dataframe
#       table           -   table to populate
#       numworstRows    -   count of worst nan rows
#
#------------------------------------------------------------------
""" 
def display_df_row_nans(df,table,rowsnulls,rowcounts,numworstRows) :

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
    nanHeaders  =   ["% Nan<br>Cols","Rows<br> Count","% of <br>Rows","Sample Row Ids"]
    nanWidths   =   [10,10,10,70]
    nanAligns   =   ["center","center","center","left"]
    
    table.set_colsperrow(5)
    table.set_rowspertable(10)
    table.set_maxtables(1)
    
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
    
    table.set_tabletype(ROW_MAJOR)
    table.set_rowspertable(20)
    #table.set_lastrowdisplayed(-1)

    get_row_major_table(table,SCROLL_NEXT)


"""            
#------------------------------------------------------------------
#   display columns nan stats
#
#   df              -   dataframe
#
#------------------------------------------------------------------
"""
def display_col_nan_stats(df) :
    
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
    nan_stats_table.set_smallwidth(35)
    nan_stats_table.set_smallmargin(32)
    nan_stats_table.set_smallfsize(12)
    nan_stats_table.set_border(False)
    nan_stats_table.set_checkLength(False)
    
    nan_stats_table.display_table()


"""            
#------------------------------------------------------------------
#   display col nans  
#
#       df          -   dataframe
#       table       -   table to populate
#
#------------------------------------------------------------------
""" 
def display_df_col_nans(df,table) :
    
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
    #table.set_lastrowdisplayed(-1)

    get_row_major_table(table,SCROLL_NEXT)
 

"""            
#------------------------------------------------------------------
#   display row data   
#
#       df          -   dataframe
#       tableid     -   html tableid
#       rowid       -   row id
#       colid       -   col id
#
#------------------------------------------------------------------
""" 
def display_df_row_data(df,table,rowid,colId) : #,numworstRows) :
    
    print("\n")
    display_row_stats(df,rowid)
    
    if(type(rowid) == str) :
        return(display_sample_row(df,table,int(rowid),int(colId)))
    else :
        return(display_sample_row(df,table,rowid,colId))

"""            
#------------------------------------------------------------------
#   display row stats
#
#   df              -   dataframe
#   rowid           -   numeric row id
#
#------------------------------------------------------------------
"""
def display_row_stats(df,rowid) :#,colId) :
    
    rowstatsHeader    =   ["",""]
    rowstatsRows      =   []
    rowstatsWidths    =   [75,25]
    rowstatsAligns    =   ["left","left"]
    
    rowstatsRows.append(["Number of Rows Imported",str(len(df))])
    rowstatsRows.append(["&nbsp;","&nbsp;"])#"Number of Unique Row ID Values",str(uniqueRowIdsCount)])
    
    row_stats_table = dcTable("Row Stats","rowstatsTable",
                              cfg.DataInspection_ID,
                              rowstatsHeader,rowstatsRows,
                              rowstatsWidths,rowstatsAligns)

    row_stats_table.set_rowspertable(len(rowstatsRows))
    row_stats_table.set_small(True)
    row_stats_table.set_smallwidth(35)
    row_stats_table.set_smallmargin(32)
    row_stats_table.set_smallfsize(12)
    row_stats_table.set_border(False)
    row_stats_table.set_checkLength(False)
    
    row_stats_table.display_table()



"""            
#------------------------------------------------------------------
#   display categories  
#
#       df                  -   dataframe
#       cattable            -   category table
#       catcandidatetable   -   category candidate table
#
#------------------------------------------------------------------
""" 
def display_df_categories(df,cattable,catcandidatetable) : 

    df_cols     = df.columns.tolist()
    datatypesList, datatypesCountList, datatypesColsList = get_df_datatypes_data(df)

    uniquesCountList = []
    for i in range(len(df_cols)) :
        uniquesCountList.append(get_num_uniques_by_id(df, df_cols[i]))
                    
    uniquesValsList = []
    #import pandas
                
    for i in range(len(df_cols)) :
        if(uniquesCountList[i] < 25) :
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

    if(len(catcandidates) > 0) :
        
        #catcandhref         =   ["scatcol",None,None,None,None,None]
    
        catcandHeader       =   ["Column Name","Column</br>Data Type","Nan</br>Count",
                                 "White</br>Space","Unique</br>Count","Unique Values"]
        catcandRows         =   []
        catcandHrefs        =   []

        catcandWidths       =   [15,15,10,7,8,45]
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
        
        catcandidatetable.display_table()
        
    return(len(catcols), len(catcandidates))

    
    
    
    