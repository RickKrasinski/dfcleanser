"""
# data_cleansing_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
import dfcleanser.common.cfg  as cfg

this = sys.modules[__name__]

import dfcleanser.common.help_utils as dfchelp
import dfcleanser.data_cleansing.data_cleansing_model as dcm

from dfcleanser.common.html_widgets import (display_composite_form, get_button_tb_form, get_header_form,
                                            get_blank_line_form, displayHeading, get_input_form,
                                            get_html_spaces, ButtonGroupForm, InputForm, DEFAULT_PAGE_WIDTH)

from dfcleanser.common.table_widgets import (dcTable, MULTIPLE, SCROLL_NEXT, get_mult_table) 

from dfcleanser.common.common_utils import (is_numeric_col_int, get_datatype, get_datatype_title, 
                                            display_exception, opStatus, get_parms_for_input, is_numeric_col, 
                                            is_datatype_numeric, RunningClock, get_col_uniques_by_id, displayParms,
                                            display_notes, get_datatype_str, is_numeric_datatype_id,
                                            is_datetime_datatype)

from dfcleanser.common.display_utils import (display_df_describe, get_df_datatypes_data, 
                                             display_df_unique_column, display_single_row)

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    data cleansing widget functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def     get_options_flag(id) :
    
    if(id == dcm.UNIQUES_FLAG) :
        if(cfg.get_config_value(cfg.UNIQUES_FLAG_KEY) == None)  :
            return(False)
        else :
            return(cfg.get_config_value(cfg.UNIQUES_FLAG_KEY))
            
    elif(id == dcm.OUTLIERS_FLAG) :
        if(cfg.get_config_value(cfg.OUTLIERS_FLAG_KEY) == None)  :
            return(False)
        else :
            return(cfg.get_config_value(cfg.OUTLIERS_FLAG_KEY))
            
    elif(id == dcm.DATA_TYPES_FLAG) :
        if(cfg.get_config_value(cfg.DATA_TYPES_FLAG_KEY) == None)  :
            return(False)
        else :
            return(cfg.get_config_value(cfg.DATA_TYPES_FLAG_KEY))
        
    elif(id == dcm.ROUNDING_FLAG) :
        if(cfg.get_config_value(cfg.ROUNDING_FLAG_KEY) == None)  :
            return(False)
        else :
            return(cfg.get_config_value(cfg.ROUNDING_FLAG_KEY))

    else :
        return(False)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   data cleansing form components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    data cleansing main task bar
#--------------------------------------------------------------------------
"""
data_cleansing_tb_doc_title             =   "Cleansing Options"
data_cleansing_tb_title                 =   "Cleansing Options"
data_cleansing_tb_id                    =   "cleanseionoptionstb"

data_cleansing_tb_keyTitleList          =   ["Cleanse</br>Numeric Column",
                                             "Cleanse</br>Non Numeric</br> Column",
                                             "Cleanse Row",
                                             "Clear","Help"]

data_cleansing_tb_jsList                =   ["cleansing_tb_callback(0)",
                                             "cleansing_tb_callback(1)",
                                             "cleansing_tb_callback(2)",
                                             "cleansing_tb_callback(3)",
                                             "displayhelp(" + str(dfchelp.CLEANSE_MAIN_TASKBAR_ID) + ")"]

data_cleansing_tb_centered              =   False


"""
#--------------------------------------------------------------------------
#    columns uniques change values input
#--------------------------------------------------------------------------
"""
change_values_input_title               =   "Change Data Type Parameters"
change_values_input_id                  =   "dcchangevalsinput"
change_values_input_idList              =   ["changecval","changenval",None,None,None]

change_values_input_labelList           =   ["Current_Value",
                                             "New_Value",
                                             "Change Values",
                                             "Find Values",
                                             "Help"]

change_values_input_typeList            =   ["text","text","button","button","button"]

change_values_input_placeholderList     =   ["","",None,None,None]

change_values_input_jsList              =   [None,None,
                                             "change_uvals_callback()",
                                             "find_uvals_callback()",
                                             "displayhelp(" + str(dfchelp.CLEANSE_NUM_UNIQUE_ID) + ")"]

change_values_input_reqList             =   [0,1]
change_values_input_short               =   True

"""
#--------------------------------------------------------------------------
#    non numeric columns uniques change values input
#--------------------------------------------------------------------------
"""
nn_change_values_input_title            =   "Change Data Type Parameters"
nn_change_values_input_id               =   "dcchangevalsinput"
nn_change_values_input_idList           =   ["changecval","changenval",None,None]

nn_change_values_input_labelList        =   ["Current_Value",
                                             "New_Value",
                                             "Change Values",
                                             "Help"]

nn_change_values_input_typeList         =   ["text","text","button","button"]

nn_change_values_input_placeholderList  =   ["","",None,None]

nn_change_values_input_jsList           =   [None,None,
                                             "change_uvals_callback()",
                                             "displayhelp(" + str(dfchelp.CLEANSE_NUM_UNIQUE_ID) + ")"]

nn_change_values_input_reqList          =   [0,1]
nn_change_values_input_short            =   True

"""
#--------------------------------------------------------------------------
#    change row values input
#--------------------------------------------------------------------------
"""
change_row_values_input_title            =   "Change Data Type Parameters"
change_row_values_input_id               =   "changerowinput"
change_row_values_input_idList           =   ["changercval","changernval",None,None,None]

change_row_values_input_labelList        =   ["Current_Value",
                                             "New_Value",
                                             "Change</br>Value",
                                             "Drop</br>Row",
                                             "Help"]

change_row_values_input_typeList         =   ["text","text","button","button","button"]

change_row_values_input_placeholderList  =   ["","",None,None,None]

change_row_values_input_jsList           =   [None,None,
                                             "change_rowvals_callback(0)",
                                             "change_rowvals_callback(1)",
                                             "displayhelp(" + str(dfchelp.CLEANSE_ROW_ID) + ")"]

change_row_values_input_reqList          =   [0,1]
change_row_values_input_short            =   True

"""
#--------------------------------------------------------------------------
#    round column input text
#--------------------------------------------------------------------------
"""
col_round_input_title                   =   ""
col_round_input_id                      =   "columnroundinput"
col_round_input_idList                  =   ["columnround",None]

col_round_input_labelList               =   ["Number_Of_Decimals",
                                             "Round Column"]

col_round_input_typeList                =   ["text","button"]

col_round_input_placeholderList         =   ["",None]

col_round_input_jsList                  =   [None,"round_col_vals_callback()"]

col_round_input_reqList                 =   [0]
col_round_input_short                   =   True

"""
#--------------------------------------------------------------------------
#    unique numeric cols round task bar
#--------------------------------------------------------------------------
"""
col_uniques_round_tb_title              =   ""
col_uniques_round_tb_title              =   ""
col_uniques_round_tb_id                 =   "coluniquesnormaloptionstb"

col_uniques_round_tb_keyTitleList       =   ["Drop Column",
                                             "Drop</br>Current Value</br>Rows",
                                             "Drop</br>Column</br>Nan Rows",
                                             "Transform</br>Column",
                                             "Round Column</br>Values",
                                             "Change</br>Data Type",
                                             "Return"]

col_uniques_round_tb_jsList             =   ["drop_column_callback()",
                                             "drop_rows_callback()",
                                             "drop_col_nans_callback()",
                                             "transform_column_callback()",
                                             "display_round_column_callback()",
                                             "convert_datatype_callback()",
                                             "cleansing_tb_callback(3)"]

col_uniques_round_tb_centered           =   True

"""
#--------------------------------------------------------------------------
#    unique int cols task bar
#--------------------------------------------------------------------------
"""
col_uniques_int_tb_title                =   ""
col_uniques_int_tb_title                =   ""
col_uniques_int_tb_id                   =   "coluniquesroundoptionstb"

col_uniques_int_tb_keyTitleList         =   ["Drop Column",
                                             "Drop</br>Current Value</br>Rows",
                                             "Drop</br>Column</br>Nan Rows",
                                             "Transform</br>Column",
                                             "Change</br>Data Type",
                                             "Return"]

col_uniques_int_tb_jsList               =   ["drop_column_callback()",
                                             "drop_rows_callback()",
                                             "drop_col_nans_callback()",
                                             "transform_column_callback()",
                                             "convert_datatype_callback()",
                                             "cleansing_tb_callback(3)"]

col_uniques_int_tb_centered             =   True

"""
#--------------------------------------------------------------------------
#    unique numeric cols change task bar
#--------------------------------------------------------------------------
"""
col_uniques_change_tb_doc_title         =   ""
col_uniques_change_tb_title             =   ""
col_uniques_change_tb_id                =   "coluniqueschangeoptionstb"

col_uniques_change_tb_keyTitleList      =   ["Drop Column",
                                             "Drop</br>Column</br>Nan Rows",
                                             "Transform</br>Column",
                                             "Change Column</br>Values",
                                             "Change</br>Data Type",
                                             "Return"]

col_uniques_change_tb_jsList            =   ["drop_column_callback()",
                                             "drop_col_nans_callback()",
                                             "transform_column_callback()",
                                             "display_change_column_callback()",
                                             "convert_datatype_callback()",
                                             "cleansing_tb_callback(3)"]

col_uniques_change_tb_centered          =   True

"""
#--------------------------------------------------------------------------
#    unique non_numeric cols change task bar
#--------------------------------------------------------------------------
"""
nn_col_uniques_change_tb_doc_title      =   ""
nn_col_uniques_change_tb_title          =   ""
nn_col_uniques_change_tb_id             =   "coluniqueschoptionstb"

nn_col_uniques_change_tb_keyTitleList   =   ["Drop</br> Column",
                                             "Drop</br>Current Value</br>Rows",
                                             "Drop</br>Column</br>Nan Rows",
                                             "Transform</br>Column",
                                             "Remove</br>Whitespace",
                                             "Return"]

nn_col_uniques_change_tb_jsList         =   ["drop_column_callback()",
                                             "drop_rows_callback()",
                                             "drop_col_nans_callback()",
                                             "transform_column_callback()",
                                             "remove_whitespace_callback()",
                                             "cleansing_tb_callback(3)"]

nn_col_uniques_change_tb_centered       =   True

"""
#--------------------------------------------------------------------------
#    convert datatype task bar
#--------------------------------------------------------------------------
"""
conv_datatype_doc_title                 =   ""
conv_datatype_title                     =   ""
conv_datatype_id                        =   "convdatatype"

conv_datatype_keyTitleList              =   ["Convert DataType"]
conv_datatype_jsList                    =   ["convert_datatype_callback()"]

conv_datatype_centered                  =   False

"""
#--------------------------------------------------------------------------
#    list unique values task bar
#--------------------------------------------------------------------------
"""
list_unique_doc_title                   =   ""
list_unique_title                       =   ""
list_unique_id                          =   "listuniques"

list_unique_keyTitleList                =   ["Show Unique Values"]
list_unique_jsList                      =   ["show_uniques_callback()"]

list_unique_centered                    =   False

"""
#--------------------------------------------------------------------------
#    graphs values task bar
#--------------------------------------------------------------------------
"""
show_graphs_doc_title                   =   ""
show_graphs_title                       =   ""
show_graphs_id                          =   "listuniques"

show_graphs_keyTitleList                =   ["Show Column Graphs"]
show_graphs_jsList                      =   ["show_graphs_callback()"]

show_graphs_centered                    =   False

"""
#--------------------------------------------------------------------------
#    outliers task bar
#--------------------------------------------------------------------------
"""
outliers_tb_doc_title                   =   ""
outliers_tb_title                       =   ""
outliers_tb_id                          =   "outlierstb"

outliers_tb_keyTitleList                =   ["Show Outliers"]

outliers_tb_jsList                      =   ["show_outliers_callback()"]

outliers_tb_centered                    =   False

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    data cleansing display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def display_no_data_heading() :
    display_data_cleansing_main_taskbar()
    displayHeading("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[No data imported yet]",4)

def display_data_cleansing_main_taskbar() :
    display_composite_form([get_button_tb_form(ButtonGroupForm(data_cleansing_tb_id,
                                                               data_cleansing_tb_keyTitleList,
                                                               data_cleansing_tb_jsList,
                                                               data_cleansing_tb_centered)),
                            get_header_form("&nbsp;&nbsp;&nbsp;Data")]) 

def get_change_row_values_inputs(parms) :
    return(get_parms_for_input(parms[1],change_row_values_input_idList))


"""            
#------------------------------------------------------------------
#   display column data heading 
#
#   df          -   dataframe
#   colname     -   column name 
#
#------------------------------------------------------------------
"""
def     display_column_header_data(df,colname) :

    print("\n")
    display_col_stats(df,colname, False)

"""            
#------------------------------------------------------------------
#   display column data
#
#------------------------------------------------------------------
"""
def display_col_data() :
    
    df = cfg.get_dc_dataframe()

    colname = cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    
    if(is_numeric_col(df,colname)) :
        display_numeric_col_data(df)
    else :
        #if(not(showuniques)) :
#        display_convert_datatype_data(True)

        display_unique_col_data(df)


def get_header_widths(labels,values) :

    maxlabellength = 0
    maxvaluelength = 0
    
    for i in range(len(labels)) :
        if(len(labels[i]) > maxlabellength)  :
            maxlabellength = len(labels[i])
            
    for i in range(len(values)) :
        if(len(values[i]) > maxvaluelength)  :
            maxvaluelength = len(values[i])
            
    import math
    charwidth = int(math.ceil((DEFAULT_PAGE_WIDTH / 9 )))
    width = int(math.ceil( ((maxlabellength + maxvaluelength + 1) / charwidth) * 100) )     
    pctlabels =  int(math.ceil((maxlabellength / (maxlabellength + maxvaluelength)) * 100)) - 4       
    pctvalues =  100 - pctlabels 

    return([width,pctlabels,pctvalues])    
    
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
def display_col_stats(df,colname, numeric=True) :

    df_col = df[colname]

    num_stats = []

    labels  =   []
    values  =   []
    
    try :
        num_stats.append(df_col.count())
        if(numeric) :
            num_stats.append(float("{0:.3f}".format(df_col.mean())))
            num_stats.append(float("{0:.3f}".format(df_col.std())))
            
            if(is_numeric_col_int(df,colname)) :
                num_stats.append(df_col.min())
                num_stats.append(df_col.max())
            else :
                num_stats.append(float("{0:.3f}".format(df_col.min())))
                num_stats.append(float("{0:.3f}".format(df_col.max())))
            
            num_stats.append(float("{0:.3f}".format(df_col.skew())))
            num_stats.append(float("{0:.3f}".format(df_col.kurtosis())))
                
    except : 
        num_stats = [0, 0, 0, 0, 0, 0, 0]

    statsHeader    =   ["",""]
    statsRows      =   []
    statsWidths    =   []
    statsAligns    =   ["left","left"]
    
    whitecolor  =   "#FFFFFF"
    yellowcolor =   "#FAF6BE"
    redcolor    =   "#F1C4B7"
    greencolor  =   "#ADECC4"
    
    colorList = []    

    statsRows.append(["Column Name",colname])
    labels.append("Column Name")
    values.append(colname)

    colorList.append([whitecolor,whitecolor])

    found = -1
    df_cols     = df.columns.tolist()
    df_dtypes   = df.dtypes.tolist()
    for i in range(len(df_cols)) :
        if(df_cols[i] == colname) :
            found = i
    
    if(found != -1) :
        ftype = df_dtypes[found]
    
    statsRows.append(["Column Data Type",str(ftype)])
    labels.append("Column Data Type")
    values.append(str(ftype))
    colorList.append([whitecolor,whitecolor])

    statsRows.append(["Non Nan Count",num_stats[0]])
    labels.append("Non Nan Count")
    values.append(str(num_stats[0]))
    colorList.append([whitecolor,whitecolor])
    
    df_col    =     df[colname]
    nans      =     df[colname].isnull().sum()
    
    statsRows.append(["Total Nans",nans])
    labels.append("Total Nans")
    values.append(str(nans))
    colorList.append([whitecolor,whitecolor])
    
    if(nans > 0) :
        pct = float("{0:.3f}".format(100*(nans/len(df))))
        statsRows.append(["&nbsp;&nbsp;% of Total Col Values",str(pct)+"%"])
        labels.append("&nbsp;&nbsp;% of Total Col Values")
        values.append(str(pct)+"%")
        colorList.append([whitecolor,whitecolor])

    uniques   =     df[colname].unique()    
    statsRows.append(["Column Uniques Count",len(uniques)])
    labels.append("Column Uniques Count")
    values.append(str(len(uniques)))
    colorList.append([whitecolor,whitecolor])
    
    if(numeric) :
        statsRows.append(["Mean",num_stats[1]])
        labels.append("Mean")
        values.append(str(num_stats[1]))
        
        statsRows.append(["Std",num_stats[2]])
        labels.append("Std")
        values.append(str(num_stats[2]))
        
        statsRows.append(["Min",num_stats[3]])
        labels.append("Min")
        values.append(str(num_stats[3]))
        
        statsRows.append(["Max",num_stats[4]])
        labels.append("Max")
        values.append(str(num_stats[4]))
        
        statsRows.append(["Skew",num_stats[5]])
        labels.append("Skew")
        values.append(str(num_stats[5]))

        statsRows.append(["Kurtosis",num_stats[6]])
        labels.append("Kurtosis")
        values.append(str(num_stats[6]))

    if(numeric) :
        for i in range(4) :
            colorList.append([whitecolor,whitecolor])
        
        if( (num_stats[5] < -1.0) or (num_stats[5] > 1.0) ) :
            colorList.append([whitecolor,redcolor])
        elif( (num_stats[5] < -0.5) or (num_stats[5] > 0.5) ) :
            colorList.append([whitecolor,yellowcolor])
        else : 
            colorList.append([whitecolor,greencolor])
        
        if( (num_stats[6] < -2.0) or (num_stats[6] > 2.0) ) :
            colorList.append([whitecolor,redcolor])
        elif( (num_stats[6] < -1.0) or (num_stats[6] > 1.0) ) :
            colorList.append([whitecolor,yellowcolor])
        else :
            colorList.append([whitecolor,greencolor])
    

    headerdata = get_header_widths(labels,values)
    statsWidths = [str(headerdata[1]),str(headerdata[2])]
    
    stats_table = dcTable("Column Stats","colstatsTable",cfg.DataCleansing_ID,
                          statsHeader,statsRows,statsWidths,statsAligns)

    stats_table.set_rowspertable(len(statsRows))
    stats_table.set_color(True)
    stats_table.set_colorList(colorList)
    stats_table.set_small(True)
    
    stats_table.set_smallwidth(headerdata[0])
    stats_table.set_smallmargin(32)
    stats_table.set_smallfsize(12)
    
    stats_table.set_border(False)
    stats_table.set_checkLength(False)
    
    stats_table.display_table()


"""            
#------------------------------------------------------------------
#   display numeric column data
#
#   df          -   dataframe
#
#------------------------------------------------------------------
"""
def display_numeric_col_data(df) :
    
    colname         =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    
    outliers        =   cfg.get_config_value(cfg.OUTLIERS_FLAG_KEY)
    if(outliers == None) : 
        outliers = False
        
    showuniques     =   cfg.get_config_value(cfg.UNIQUES_FLAG_KEY)
    if(showuniques == None) : 
        showuniques = False

    print("\n")
    
    display_col_stats(df,colname)
    
    displayHeading("Column Unique Values",4)

    if (showuniques == False) :
        display_composite_form([get_button_tb_form(ButtonGroupForm(list_unique_id,
                                                                   list_unique_keyTitleList,
                                                                   list_unique_jsList,
                                                                   list_unique_centered))])

    else :
       #print("\n")
       display_unique_col_data(df)#,colname)
       print("\n")

    displayHeading("Column Graphs",4)
    
    if(cfg.get_config_value(cfg.GRAPHS_FLAG_KEY) == None) :
        display_composite_form([get_button_tb_form(ButtonGroupForm(show_graphs_id,
                                                                   show_graphs_keyTitleList,
                                                                   show_graphs_jsList,
                                                                   show_graphs_centered))])
    else :
    
        clock = RunningClock()
        clock.start()

        try :
            
            import numpy as np
            counts  =   df[colname].value_counts().to_dict()
            uniques =   list(counts.keys())
            uniques =   np.asarray(uniques)
            ucounts =   list(counts.values())
            ucounts =   np.asarray(ucounts)

            import matplotlib.pyplot as plt
            plt.style.use('ggplot')
            plt.hist(uniques,weights=ucounts)
            plt.title("'" + colname + "'" + " Histogram") 
            plt.show()
            
        except Exception as e: 
            opstat = opStatus()
            opstat.store_exception("Unable to plot column",e)
            display_exception(opstat)

        clock.stop()
        
    displayHeading("Outliers",4)
    
    if(outliers == False) :
    
        display_composite_form([get_button_tb_form(ButtonGroupForm(outliers_tb_id,
                                                                   outliers_tb_keyTitleList,
                                                                   outliers_tb_jsList,
                                                                   outliers_tb_centered))])
        print("\n")
       
    else :
        
        get_simple_outliers(df,cfg.get_config_value(cfg.CLEANSING_COL_KEY))

"""            
#------------------------------------------------------------------
#   display unique vals for a column
#
#   df          -   dataframe
#
#------------------------------------------------------------------
"""
def display_unique_col_data(df) :
    
    dfcol = cfg.get_config_value(cfg.CLEANSING_COL_KEY)

    opstat = opStatus()
    
    if not (is_numeric_col(df,dfcol) ) :
        display_column_header_data(df,dfcol)

    if(cfg.get_config_value(cfg.UNIQUES_RANGE_KEY) != None) :

        minmax = cfg.get_config_value(cfg.UNIQUES_RANGE_KEY)
        
        if( (len(minmax[1]) < 1) or (len(minmax[2]) < 1)) :
            
            opstat.set_status(False)
            opstat.set_errorMsg("Find values input values are invalid")
            display_exception(opstat)
            
            parmslabels = ["Min Value","Max Value"]
            parmsvals   = [minmax[1],minmax[2]]
            displayParms("Find Values Inputs",parmslabels,parmsvals,cfg.DataCleansing_ID)
            cfg.drop_config_value(cfg.UNIQUES_RANGE_KEY)
            
            #return()

    counts      =   df[dfcol].value_counts().to_dict()
    uniques     =   list(counts.keys())
    
    displayHeading("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Unique Values",4)
    
    toomanyUniques  =   False
            
    clock = RunningClock()
    clock.start()

    try :
        
        col_uniques_table = dcTable("Unique Values and Counts for Column " + dfcol,
                                    "uvalsTbl",
                                    cfg.DataCleansing_ID)
        
        if(cfg.get_config_value(cfg.UNIQUES_RANGE_KEY) == None) :
            if(len(uniques) < 250) :
                print("\n")
            else :
                display_notes(["* Number of Uniques is " + str(len(uniques)) +" and is too large to display all uniques. A sample set of 60 unique values is displayed",
                               "* To find a subset of unique values hit 'Find Values' and enter 'Min Value' and 'Max Value' and hit 'Find Values' again"])
                toomanyUniques  =   True
                
            display_df_unique_column(df,col_uniques_table,dfcol,True,counts)
        else :
            #print("range",parms)
            display_df_unique_column(df,col_uniques_table,dfcol,True,counts)
            
    except Exception as e:
        
        opstat.store_exception("Unable to display column uniques",e)
        display_exception(opstat)

    clock.stop()
    
    if(get_options_flag(ROUNDING_FLAG) == True) : 
        cleansing_text_inputs   =   get_input_form(InputForm(col_round_input_id,
                                                             col_round_input_idList,
                                                             col_round_input_labelList,
                                                             col_round_input_typeList,
                                                             col_round_input_placeholderList,
                                                             col_round_input_jsList,
                                                             col_round_input_reqList,
                                                             col_round_input_short))
        
    else :
        if(is_numeric_col(df,dfcol)) :
            cleansing_text_inputs   =   get_input_form(InputForm(change_values_input_id,
                                                                 change_values_input_idList,
                                                                 change_values_input_labelList,
                                                                 change_values_input_typeList,
                                                                 change_values_input_placeholderList,
                                                                 change_values_input_jsList,
                                                                 change_values_input_reqList,
                                                                 change_values_input_short)) 
        else :
            if(toomanyUniques) :
                cleansing_text_inputs   =   get_input_form(InputForm(change_values_input_id,
                                                                     change_values_input_idList,
                                                                     change_values_input_labelList,
                                                                     change_values_input_typeList,
                                                                     change_values_input_placeholderList,
                                                                     change_values_input_jsList,
                                                                     change_values_input_reqList,
                                                                     change_values_input_short))
            else :
                cleansing_text_inputs   =   get_input_form(InputForm(nn_change_values_input_id,
                                                                     nn_change_values_input_idList,
                                                                     nn_change_values_input_labelList,
                                                                     nn_change_values_input_typeList,
                                                                     nn_change_values_input_placeholderList,
                                                                     nn_change_values_input_jsList,
                                                                     nn_change_values_input_reqList,
                                                                     nn_change_values_input_short)) 
    
    blank_line      =   get_blank_line_form()
    
    if(get_options_flag(ROUNDING_FLAG) == True) :
        
        col_uniques_tb  =   get_button_tb_form(ButtonGroupForm(col_uniques_change_tb_id,
                                                               col_uniques_change_tb_keyTitleList,
                                                               col_uniques_change_tb_jsList,
                                                               col_uniques_change_tb_centered))
        
    else :
        
        if (is_numeric_col(df,dfcol) ) :
            if(is_numeric_col_int(df,dfcol)) :
                
                col_uniques_tb  =   get_button_tb_form(ButtonGroupForm(col_uniques_int_tb_id,
                                                                       col_uniques_int_tb_keyTitleList,
                                                                       col_uniques_int_tb_jsList,
                                                                       col_uniques_int_tb_centered))
                
            else :
        
                col_uniques_tb  =   get_button_tb_form(ButtonGroupForm(col_uniques_round_tb_id,
                                                                       col_uniques_round_tb_keyTitleList,
                                                                       col_uniques_round_tb_jsList,
                                                                       col_uniques_round_tb_centered))

        else :
            
            col_uniques_tb  =   get_button_tb_form(ButtonGroupForm(nn_col_uniques_change_tb_id,
                                                                   nn_col_uniques_change_tb_keyTitleList,
                                                                   nn_col_uniques_change_tb_jsList,
                                                                   nn_col_uniques_change_tb_centered))
            
    if(get_options_flag(dcm.ROUNDING_FLAG) == True) : 
        
        cleansing_text_inputs_forms    =   [cleansing_text_inputs,
                                            blank_line,
                                            col_uniques_tb]
        
    else : 
        
        cleansing_text_inputs_forms    =   [cleansing_text_inputs,
                                            blank_line,
                                            col_uniques_tb]

    display_composite_form(cleansing_text_inputs_forms)


"""            
#------------------------------------------------------------------
#   display the objects that change
#
#   df          -   dataframe
#   formid      -   from to read
#   dtype       -   data type
#   colList     -   column list
#
#------------------------------------------------------------------
"""
def display_change_objects(df,formid,dtypeId,colList=None) :#,skipactionbar=False) :
    
    typeparm = get_datatype(dtypeId)
    
    print("display_change_objects",formid,dtypeId,colList)
    print(get_datatype_str(dtypeId),typeparm)
    
    change_objects_table = dcTable("Columns for Data Type " + get_datatype_title(dtypeId), 
                                   formid,
                                   cfg.DataCleansing_ID)
    
    # numeric datatypes
    if(is_numeric_datatype_id(dtypeId))  : 
        display_df_describe(df,change_objects_table,typeparm,colList)#,True)
    else :
        display_non_numeric_df_describe(df,change_objects_table,typeparm,colList)#,True)
        
    cfg.set_config_value(cfg.OBJ_TYPE_PARM_KEY,dtypeId)     

     
"""            
#------------------------------------------------------------------
#   get simple outliers
#
#   df         -   dataframe
#   colname    -   column name
#
#------------------------------------------------------------------
"""   
def get_simple_outliers(df,colname) :  
    
    opstat = opStatus()
    
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
        
        outliers_table.display_table()
            
    except Exception as e: 
        opstat = opStatus()
        opstat.store_exception("Unable to get simple outliers",e)
        display_exception(opstat)

    clock.stop() 
           
    return(opstat)    
        
"""            
#------------------------------------------------------------------
#   display row data
#
#   df          -   dataframe
#   rowid       -   row id 
#   colid       -   column id 
#
#------------------------------------------------------------------
"""
def display_row_data(df,rowid,colid) :
    
    rows_table = dcTable("Sample Row","dcdisrow",cfg.DataCleansing_ID)
    
    refList = []
    
    for i in range(3) :
        refList.append([None,None,None,None,None,None,None,None,None,None])
        refList.append(["frval","frval","frval","frval","frval",
                        "frval","frval","frval","frval","frval"])
        
    rows_table.set_refList(refList)
    
    opstat = opStatus()
    opstat = display_single_row(df,rows_table,rowid,colid)
    
    if(not opstat.get_status()) :
        display_exception(opstat)
        
    # setup the button bar form
    display_composite_form([get_input_form(InputForm(change_row_values_input_id,
                                                     change_row_values_input_idList,
                                                     change_row_values_input_labelList,
                                                     change_row_values_input_typeList,
                                                     change_row_values_input_placeholderList,
                                                     change_row_values_input_jsList,
                                                     change_row_values_input_reqList,
                                                     change_row_values_input_short))])
        
    print("\n")
    
""" 
#------------------------------------------------------------------
#------------------------------------------------------------------
#   Datacleansing dispaly utilities 
#------------------------------------------------------------------
#------------------------------------------------------------------
""" 

"""          
#------------------------------------------------------------------
#   display non numeric column descriptive data
#
#   df              -   dataframe
#
#------------------------------------------------------------------
"""
def display_non_numeric_df_describe(df,table,datatype,colList=None) :#,checkboxes=False) : 

    import pandas
    import datetime

    df_cols     =   df.columns.tolist()
    nanrow      =   []
    uniquerow   =   []
    maxlrow     =   []
    
    nn_cols         =   []
    col_stats       =   []
    df_stats        =   []

    # build the column stats for the columns list
    if(colList == None) :

        if(datatype == None) :
            
            for i in range(len(df_cols)) :
                if(not(is_datatype_numeric(df[df_cols[i]].dtype))) :
                    nn_cols.append(df_cols[i])    
        else :
            
            df_data_info = get_df_datatypes_data(df) 

            for i in range(len(df_data_info[0])) :
                if(datatype == object) :
                    if(df_data_info[0][i] == object) :
                        nn_cols = df_data_info[2].get(df_data_info[0][i])
                elif(datatype == str) :
                    if(df_data_info[0][i] == "str") :
                        nn_cols = df_data_info[2].get(df_data_info[0][i])
                elif(datatype == datetime.datetime) :
                    if(is_datetime_datatype(df_data_info[0][i])) :
                        nn_cols = df_data_info[2].get(df_data_info[0][i])
        
                elif(datatype == pandas.core.dtypes.dtypes.CategoricalDtype) :
                    if(df_data_info[0][i] == pandas.core.dtypes.dtypes.CategoricalDtype) :
                        nn_cols = df_data_info[2].get("category")
                    
    else :
        nn_cols = colList
    
    for i in range(len(nn_cols)) :
        
        try :
                
            col_stats.append(df[nn_cols[i]].isnull().sum())
            uniques = get_col_uniques_by_id(df,nn_cols[i])
            col_stats.append(len(uniques))
                
            maxlength = 0 
            alphanum  = False
            for j in range(len(uniques)) :
                if(len(str(uniques[j])) > maxlength) :
                    maxlength =  len(str(uniques[j])) 
                if(str(uniques[j]).isalnum()) :
                    alphanum = True
            col_stats.append(maxlength)
            col_stats.append(alphanum)
        except : 
            col_stats = [0, 0, 0, 0, False]
                
                
        df_stats.append(col_stats)
        col_stats   =   []
        
    # build the table lists from the column stats
    dfHeader        =   ["    "]
    dfRows          =   []
    dfWidths        =   [9]
    dfAligns        =   ["center"]
    dfchrefs        =   [None]
    
    nanrow          =   []
    uniquerow       =   []
    maxlrow         =   []
    alphanumrow     =   []
    
    dfHeaderList    =   []
    dfRowsList      =   []
    dfWidthsList    =   []
    dfAlignsList    =   []
    dfchrefsList    =   []
    
    table.set_colsperrow(7)
    table.set_rowspertable(5)
    table.set_maxtables(1)
    
    import datetime
    if(datatype == object) :
        dtstr = "Column Stats for datatype "+"&#60;object&#62;"
    elif(datatype == str) :
        dtstr = "Column Stats for datatype "+"&#60;str&#62;"
    elif(datatype == datetime.datetime) :
        dtstr = "Column Stats for datatype "+"&#60;datetime&#62;"
    elif(datatype == datetime.timedelta) :
        dtstr = "Column Stats for datatype "+"&#60;timedelta&#62;"
    elif(datatype == pandas.core.dtypes.dtypes.CategoricalDtype) :
        dtstr = "Column Stats for datatype "+"&#60;category&#62;"
    elif(datatype == None) :
        dtstr = "Non Numeric Columns"
    else :
        dtstr = "Column Stats for datatype "+"&#60;other&#62;"
    
    for i in range(len(nn_cols)) :
        
        dfHeader.append(nn_cols[i])
        nanrow.append(df_stats[i][0])
        uniquerow.append(df_stats[i][1])
        maxlrow.append(df_stats[i][2])
        alphanumrow.append(df_stats[i][3])
        
        dfWidths.append(13)
        dfAligns.append("center")
        dfchrefs.append("ncol")
        
        if( ( ((i+1) % table.get_colsperrow()) == 0) and (i>0) ) :
                
            dfHeaderList.append(dfHeader)
            dfRowsList.append(get_nn_rows(table.get_tableid(),nanrow,
                                          uniquerow,maxlrow,alphanumrow))#,checkboxes))
            
            dfWidthsList.append(dfWidths)
            dfAlignsList.append(dfAligns)
            dfchrefsList.append(dfchrefs)
                
            dfHeader    =   ["    "]
            dfRows      =   []
            dfWidths    =   [9]
            dfAligns    =   ["center"]
            dfchrefs    =   [None]

            nanrow          =   []
            uniquerow       =   []
            maxlrow         =   []
            alphanumrow     =   []
            
    # handle any incomplete rows 
    if( ((i+1) % table.get_colsperrow())  != 0) :
        
        for k in range((table.get_colsperrow() - ((i+1) % table.get_colsperrow()))):#+2) :
            dfHeader.append("")
            dfRows.append("")
            dfWidths.append(13)
            dfAligns.append("center")
            dfchrefs.append(None)
            
            nanrow.append("")
            uniquerow.append("")
            maxlrow.append("")
            alphanumrow.append("")
            
    if(len(dfRows) > 0) :
        
        dfHeaderList.append(dfHeader)    
        dfRowsList.append(get_nn_rows(table.get_tableid(),nanrow,
                                      uniquerow,maxlrow,alphanumrow))#,checkboxes))
                
        dfWidthsList.append(dfWidths)
        dfAlignsList.append(dfAligns)
        dfchrefsList.append(dfchrefs)

    title = dtstr
    table.set_title(title)    
    
    table.set_headerList(dfHeaderList)
    table.set_widthList(dfWidthsList)
    table.set_alignList(dfAlignsList)
    table.set_hhrefList(dfchrefsList)
    table.set_rowList(dfRowsList)
    
    table.set_tabletype(MULTIPLE)
    table.set_numtables(len(dfHeaderList))
    table.set_note(get_html_spaces(10)+"<b>*</b> To select column to cleanse click on Column Name above")

    #table.dump()

    get_mult_table(table,SCROLL_NEXT)


"""            
#------------------------------------------------------------------
#   get non numeric data and form table rows
#
#   counts  -   list of counts for rows
#   means   -   list of means for rows
#   stds    -   list of counts for rows
#   mins    -   list of mins for rows
#   maxs    -   list of maxs for rows
#
#------------------------------------------------------------------
"""
def get_nn_rows(formId,nans,uniques,maxlens,alphanums) :#,checkboxes) :    

    currentRow  =   []
    allrows     =   []
    
    txtCol      =   ["<b>NaNs</b>","<b>Uniques</b>","<b>Max Len</b>","<b>AlphaNum</b>"] 
    
    for i in range(len(txtCol)) :
        currentRow.append(txtCol[i])
        
        if(i == 0) :
            for j in range(len(nans)) : 
                currentRow.append(nans[j])
        elif(i == 1) :
            for j in range(len(uniques)) : 
                currentRow.append(uniques[j])
        elif(i == 2) :
            for j in range(len(maxlens)) : 
                currentRow.append(maxlens[j])
        elif(i == 3) :
            for j in range(len(alphanums)) : 
                currentRow.append(alphanums[j])
            
        allrows.append(currentRow)
        currentRow = []
        
    return(allrows)
    

"""            
#------------------------------------------------------------------
#   get a simplelist of outliers based on stddev from means
#
#   return : list of lists [[count,[vals]]]
#
#   df              -   dataframe
#   threshold       -   the number of std devs away from the mean 
#   getvals         -   boolean flag to retrieve vals as well as counts
#
#------------------------------------------------------------------
"""
def get_simple_col_outliers(df,colname) :

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


