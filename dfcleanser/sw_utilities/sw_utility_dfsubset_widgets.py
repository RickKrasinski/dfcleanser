"""
# sw_utility_dfsubset_widgets 
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

from dfcleanser.common.html_widgets import (get_button_tb_form, display_composite_form, maketextarea, ButtonGroupForm)

from dfcleanser.common.table_widgets import dcTable, get_row_major_table, SCROLL_NEXT, ROW_MAJOR

from dfcleanser.common.common_utils import (get_parms_for_input, display_grid, is_numeric_col, is_str_column)

DISPLAY_MAIN                    =   0

DISPLAY_GET_SUBSET              =   1
PROCESS_GET_SUBSET              =   2
DISPLAY_GET_SUBSET_FILTER       =   3
PROCESS_GET_SUBSET_FILTERED     =   4

CLEAR_SUBSET_FORM               =   5
CLEAR_FILTER_FORM               =   6
ADD_FILTER                      =   7
GET_COLUMN_NAMES                =   9

DISPLAY_GET_COL_VALUES          =   8

"""
#--------------------------------------------------------------------------
#    dfsubset main task bar
#--------------------------------------------------------------------------
"""
dfsubset_tb_doc_title               =   "Dataframe Subset"
dfsubset_tb_title                   =   "Dataframe Subset"
dfsubset_tb_id                      =   "dfsubsettb"

dfsubset_tb_keyTitleList            =   ["Get Dataframe Subset",
                                         "Clear","Help"]

dfsubset_tb_jsList                  =   ["get_subset_callback("+str(DISPLAY_GET_SUBSET)+")",
                                         "get_subset_callback("+str(DISPLAY_MAIN)+")",
                                         "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_TASKBAR_ID) + ")"]

dfsubset_tb_centered                =   False

"""
#--------------------------------------------------------------------------
#   get subset input 
#--------------------------------------------------------------------------
"""
get_subset_input_title                  =   "Get Dataframe Subset"
get_subset_input_id                     =   "dcdfsubset"
get_subset_input_idList                 =   ["gsrowrange",
                                             "gscolnames",
                                             "gsadddrop",
                                             "subsetfname",
                                             None,None,None,None,None]

get_subset_input_labelList              =   ["drop_row_range",
                                             "column_names_list",
                                             "keep_column_names_flag",
                                             "csv_file_name",
                                             "Define</br>Filter(s)",
                                             "Get</br>Subset",
                                             "Clear","Return","Help"]

get_subset_input_typeList               =   ["text",maketextarea(4),"text","file",
                                             "button","button","button","button","button"]

get_subset_input_placeholderList        =   ["drop row range - as slice - [0:2000] (default = no rows dropped)",
                                             "column names list to grab or drop from Column Names table (default = all columns)",
                                             "keep(True) or drop(False) columns in column name list (default = True)",
                                             "select file name to write to (default = None write to current dataframe)",
                                             None,None,None,None,None]

get_subset_input_jsList                 =   [None,None,None,None,
                                             "get_subset_callback("+str(DISPLAY_GET_SUBSET_FILTER)+")",
                                             "get_subset_callback("+str(PROCESS_GET_SUBSET)+")",
                                             "get_subset_callback("+str(CLEAR_SUBSET_FORM)+")",
                                             "get_subset_callback("+str(DISPLAY_MAIN)+")",
                                             "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_ID) + ")"]

get_subset_input_reqList                =   [0,5]

get_subset_input_form                   =   [get_subset_input_id,
                                             get_subset_input_idList,
                                             get_subset_input_labelList,
                                             get_subset_input_typeList,
                                             get_subset_input_placeholderList,
                                             get_subset_input_jsList,
                                             get_subset_input_reqList]  

"""
#--------------------------------------------------------------------------
#   get subset filter input 
#--------------------------------------------------------------------------
"""
get_subset_filter_input_title             =   "Get Dataframe Subset Search Criteria"
get_subset_filter_input_id                =   "dcdfsubsetsearch"
get_subset_filter_input_idList            =   ["gscolname",
                                               "gscolvalue",
                                               "gscoloper",
                                               "gscolandor",
                                               "gsselandor",
                                               "gsselectstring",
                                               None,None,None,None,None]

get_subset_filter_input_labelList         =   ["filter_column_name",
                                               "filter_column_value(s)",
                                               "filter_column_value(s)_operator(s)",
                                               "filter_column_value(s)_logicals",
                                               "next_filter_logical",
                                               "selection_criteria",
                                               "Add</br>Filter</br>To Criteria",
                                               "Get</br>Subset",
                                               "Clear","Return","Help"]

get_subset_filter_input_typeList          =   ["text",maketextarea(3),"text","text","text",maketextarea(8),
                                               "button","button","button","button","button"]

get_subset_filter_input_placeholderList   =   ["current filter column name - select from Condition Columns table",
                                               "current filter column value(s) - select from Column Values table or enter 'value' ",
                                               "current filter column operator(s) - '<' '<=' '>' '=>' '==' '!=' (default '==')",
                                               "select and/or logical to use between column sub filters (default = or)",
                                               "select OR/AND/NOT logical to add next filter to selection criteria (default = AND)",
                                               "select string : can be editted manually (default - None)",
                                               None,None,None,None,None]

get_subset_filter_input_jsList            =   [None,None,None,None,None,None,
                                               "get_subset_callback("+str(ADD_FILTER)+")",
                                               "get_subset_callback("+str(PROCESS_GET_SUBSET_FILTERED)+")",
                                               "get_subset_callback("+str(CLEAR_FILTER_FORM)+")",
                                               "get_subset_callback("+str(DISPLAY_MAIN)+")",
                                               "displayhelp(" + str(dfchelp.DFSUBSET_FILTER_ID) + ")"]

get_subset_filter_input_reqList           =   [5]

get_subset_filter_input_form              =   [get_subset_filter_input_id,
                                               get_subset_filter_input_idList,
                                               get_subset_filter_input_labelList,
                                               get_subset_filter_input_typeList,
                                               get_subset_filter_input_placeholderList,
                                               get_subset_filter_input_jsList,
                                               get_subset_filter_input_reqList]  
    
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_dfsubset_main_taskbar() :
    display_composite_form([get_button_tb_form(ButtonGroupForm(dfsubset_tb_id,
                                                               dfsubset_tb_keyTitleList,
                                                               dfsubset_tb_jsList,
                                                               dfsubset_tb_centered))])

def get_dfsubset_input_parms(parms) :
   return(get_parms_for_input(parms,get_subset_input_idList))

def get_dfsubset_filter_input_parms(parms) :
   return(get_parms_for_input(parms,get_subset_filter_input_idList))




"""            
#--------------------------------------------------------------------------
#    display df subset status
#--------------------------------------------------------------------------
"""
def display_df_subset_status(df,filename,filtertext) :
    
    
    statusHeader    =   ["",""]
    statusRows      =   []
    statusWidths    =   [60,40]
    statusAligns    =   ["left","left"]
    
    whitecolor  =   "#FFFFFF"
    colorList = []  
    
    statusRows.append(["Total Rows",len(df)])
    colorList.append([whitecolor,whitecolor])
    
    statusRows.append(["Total Columns",len(df.columns)])
    colorList.append([whitecolor,whitecolor])
    
    if(filename == None) :
        ftext = "original dataframe"
    else :
        ftext = filename
    statusRows.append(["Output",ftext])
    colorList.append([whitecolor,whitecolor])
    
    if(filtertext == None) :
        ftext = "no filters"
    else :
        ftext = filtertext
    statusRows.append(["Filters",ftext])
    colorList.append([whitecolor,whitecolor])
    
    status_table = dcTable("Dataframe Subset Stats","dfstatsTable",
                           cfg.SWDFSubsetUtility_ID,
                           statusHeader,statusRows,statusWidths,statusAligns)

    status_table.set_rowspertable(10)
    status_table.set_color(True)
    status_table.set_colorList(colorList)
    status_table.set_small(True)
    status_table.set_smallwidth(50)
    status_table.set_smallmargin(32)
    status_table.set_smallfsize(12)
    status_table.set_border(False)
    status_table.set_checkLength(False)
    
    status_table.display_table()


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#  dfsubset display functions 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def get_operators_table() :
    
    operatorsHeader      =   [""]

    operatorsRows        =   []
    operatorsWidths      =   [100]
    operatorsAligns      =   ["center"]
    operatorsHrefs       =   []
    
    column_operators     =   ["==","!=","<","<=",">",">="]
    clause_operators     =   ["or","and"]
    filter_operators     =   ["OR","AND","NOT"]
    
    for i in range(len(column_operators)) :
        operatorsRows.append([column_operators[i]])
        operatorsHrefs.append(["set_col_oper"])
        
    operatorsRows.append([" "])
    operatorsHrefs.append([None])
    
    for i in range(len(clause_operators)) :
        operatorsRows.append([clause_operators[i]])
        operatorsHrefs.append(["set_clause_oper"])
    
    operatorsRows.append([" "])
    operatorsHrefs.append([None])
    
    for i in range(len(filter_operators)) :
        operatorsRows.append([filter_operators[i]])
        operatorsHrefs.append(["set_filter_oper"])

    operators_table = dcTable("",
                              "dcoperatorsTable",
                              cfg.SWDFSubsetUtility_ID,
                              operatorsHeader,operatorsRows,
                              operatorsWidths,operatorsAligns)

    operators_table.set_refList(operatorsHrefs)
    
    operators_table.set_rowspertable(len(operatorsRows))
    operators_table.set_small(True)
    operators_table.set_smallwidth(98)
    operators_table.set_smallmargin(10)
    operators_table.set_smallfsize(13)
    operators_table.set_smallheader(False)
    operators_table.set_border(False)
    operators_table.set_checkLength(False)
    operators_table.set_html_only(True) 
    
    #operators_table.dump() 
    
    operatorshtml   =   "" 
    
    operatorshtml   =   operators_table.get_html()
    
    return(operatorshtml)

        

def get_col_uniques_table(df,colname) :
    
    columnuniquesHeader      =   [""]

    columnuniquesRows        =   []
    columnuniquesWidths      =   [100]
    columnuniquesAligns      =   ["left"]
    columnuniquesHrefs       =   []
    
    uniques =   [] 
        
    #check if the object is string
    if (is_str_column(cfg.get_dc_dataframe(),colname)) :
        
        uniques =   cfg.get_dc_dataframe()[colname].unique().tolist()
        for i in range(len(uniques)) :
            uniques[i]  =   str(uniques[i])
        uniques.sort()
    else :
        
        if(is_numeric_col(df,colname)) :           
            uniques =   cfg.get_dc_dataframe()[colname].unique().tolist()
            uniques.sort()

    if(len(uniques) > 0) :
        
        if(len(uniques) > 200) :
            columnuniquesRows.append([str(colname)])
            columnuniquesHrefs.append([None])
            columnuniquesRows.append([str(len(uniques))+" Unique Values : "])
            columnuniquesHrefs.append([None])
            columnuniquesRows.append(["  Min Value : "])
            columnuniquesHrefs.append([None])
            columnuniquesRows.append([str(uniques[0])])
            columnuniquesHrefs.append(["getgsval"])
            columnuniquesRows.append(["  Max Value : "])
            columnuniquesHrefs.append([None])
            columnuniquesRows.append([str(uniques[len(uniques)-1])])
            columnuniquesHrefs.append(["getgsval"])
        
        else :
            for i in range(len(uniques)) :
                if(is_numeric_col(df,colname)) :
                    columnuniquesRows.append([str(uniques[i])])
                else :
                    columnuniquesRows.append([uniques[i]])
                    
                if(len(str(uniques[i])) > 0 ) :
                    columnuniquesHrefs.append(["getgsval"])
                    
    else : 
        columnuniquesRows.append([str(colname)])
        columnuniquesHrefs.append([None])
        columnuniquesRows.append([" Unique Values not listable: "])
        columnuniquesHrefs.append([None])
        
    columnuniques_table = None
    
    columnuniques_table = dcTable("Column Values",
                                  "dcsubsetcolnamesTable",
                                  cfg.SWDFSubsetUtility_ID,
                                  columnuniquesHeader,columnuniquesRows,
                                  columnuniquesWidths,columnuniquesAligns)

    columnuniques_table.set_refList(columnuniquesHrefs)
    
    columnuniques_table.set_small(True)
    columnuniques_table.set_smallwidth(98)
    columnuniques_table.set_smallmargin(10)

    columnuniques_table.set_border(True)
        
    columnuniques_table.set_checkLength(True)
            
    columnuniques_table.set_textLength(30)
    columnuniques_table.set_html_only(True) 
    
    columnuniques_table.set_tabletype(ROW_MAJOR)
    columnuniques_table.set_rowspertable(14)

    tablehtml = get_row_major_table(columnuniques_table,SCROLL_NEXT,False)
    return(tablehtml)


def get_dfsubset_table(filters=False,colname=None) :
    
    from dfcleanser.sw_utilities.sw_utility_geocode_widgets import get_df_col_names_table
    
    if(colname==None) :
        if(filters) :
            callback = "set_filter_colname"
        else :
            callback = "set_ds_colname"
    
        # get the drop flag and col name list
        dfsparms = cfg.get_config_value(get_subset_input_id+"Parms")
        
        if( (not(dfsparms == None)) and (len(dfsparms) > 0) ):
            collist = dfsparms[1]
            collist = collist.split(",")
            if(len(collist) > 0) :
                keepcols = True
                keepflag = dfsparms[2]
                if(len(keepflag) > 0) :
                    if(keepflag == "False") :
                        keepcols = False
                
                if(keepcols) :
                    colnames = collist
                else :
                    colnames = []
                    allcols = cfg.get_dc_dataframe().columns.tolist()
                    for i in range(len(allcols)) :
                        matched = False
                        for j in range(len(collist)) : 
                            if(allcols[i] == allcols[j]) :
                                matched = True
                            
                        if(not (matched)) :
                            colnames.append(allcols[i])
                
                if(len(colnames) > 0) :
                    col_names_html = get_df_col_names_table("dcsubsetcolnamesTable",
                                                            cfg.SWDFSubsetUtility_ID,callback,colnames)    
                else :
                    col_names_html = get_df_col_names_table("dcsubsetcolnamesTable",
                                                            cfg.SWDFSubsetUtility_ID,callback)
            else :
                col_names_html = get_df_col_names_table("dcsubsetcolnamesTable",
                                                        cfg.SWDFSubsetUtility_ID,callback)
                
        else :       
            col_names_html = get_df_col_names_table("dcsubsetcolnamesTable",
                                                    cfg.SWDFSubsetUtility_ID,callback)
             
    else :
        col_names_html  =  get_col_uniques_table(cfg.get_dc_dataframe(),colname) 

    return(col_names_html) 

"""            
#------------------------------------------------------------------
#   display dataframe subset
#
#   df          -   dataframe
#
#------------------------------------------------------------------
"""
def display_df_subset(df,filters=False,colname=None) :  
    
    if(not colname==None) :
        cfg.set_config_value(get_subset_filter_input_id+"Parms",[colname,"","","","",""])

    col_names_html  =   get_dfsubset_table(filters,colname)
    
    if(filters) :
        operators_html = get_operators_table()

    get_subset_input_html = ""
    
    if(filters) :
        
        from dfcleanser.common.html_widgets import InputForm
        get_filter_subset_input_form = InputForm(get_subset_filter_input_form[0],get_subset_filter_input_form[1],
                                                 get_subset_filter_input_form[2],get_subset_filter_input_form[3],
                                                 get_subset_filter_input_form[4],get_subset_filter_input_form[5],
                                                 get_subset_filter_input_form[6])
        
        get_filter_subset_input_form.set_shortForm(False)
        get_filter_subset_input_form.set_gridwidth(550)
        get_filter_subset_input_form.set_fullparms(True)
        
        get_subset_input_html = get_filter_subset_input_form.get_html() 
        
        dfdsparms   =   cfg.get_config_value(get_subset_input_id+"Parms")
        dfdstexts   =   []
        
        if( (dfdsparms == None) or (len(dfdsparms) == 0) ) :
            dfdstexts.append("Keep All Rows")            
            dfdstexts.append("Keep All Cols")
            dfdstexts.append("Overwrite Dataframe Cleanser dataframe")
        else :
            if(dfdsparms[0] == "") :
                dfdstexts.append("Keep All Rows") 
            else :
                dfdstexts.append("Drop Rows Slice " + str(dfdsparms[0]))
            
            if(dfdsparms[2] == "") :
                opcmd = "Keep" 
            else :
                opcmd = "Drop"
                
            if(dfdsparms[1] == "") :
                dfdstexts.append("Keep All Columns") 
            else :
                dfdstexts.append(opcmd + " Cols : " + str(dfdsparms[1]))
            if(dfdsparms[3] == "") :
                dfdstexts.append("Overwrite Dataframe Cleanser dataframe") 
            else :
                dfdstexts.append("Write dataframe subset to " + str(dfdsparms[3]))

        heading_title   =   ("<div>")
        heading_title   =   (heading_title + "<h4>&nbsp;&nbsp;Get Dataframe Subset Filters</h4><br></br>")
        heading_title   =   (heading_title + "<div class='container' style='font-size:12px; border: 1px solid #428bca; width:40%; margin-left:40px;'>")
        for i in range(len(dfdstexts)) :
            heading_title   =   (heading_title + "<div>" + dfdstexts[i] + "</div>")
        heading_title   =   (heading_title + "</div>")
        heading_title   =   (heading_title + "</div>")
                
        get_subset_heading_html = heading_title
        
    else :
        
        from dfcleanser.common.html_widgets import InputForm
        subset_input_form = InputForm(get_subset_input_form[0],get_subset_input_form[1],
                                      get_subset_input_form[2],get_subset_input_form[3],
                                      get_subset_input_form[4],get_subset_input_form[5],
                                      get_subset_input_form[6])
        
        subset_input_form.set_shortForm(False)
        subset_input_form.set_gridwidth(550)
        subset_input_form.set_fullparms(True)
        
        get_subset_input_html = subset_input_form.get_html() 
            
        get_subset_heading_html = "<h4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Get Dataframe Subset</h4>"
    
    if(filters) :
        display_grid("dfsubset1_wrapper",
                     get_subset_heading_html,
                     col_names_html,
                     get_subset_input_html,
                     None,
                     operators_html)
        
    else :
        display_grid("dfsubset_wrapper",
                     get_subset_heading_html,
                     col_names_html,
                     get_subset_input_html,
                     None)

