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

from dfcleanser.common.html_widgets import (maketextarea, ButtonGroupForm)

from dfcleanser.common.table_widgets import dcTable, get_row_major_table, SCROLL_NEXT, ROW_MAJOR

from dfcleanser.common.common_utils import (get_parms_for_input, is_numeric_col, display_generic_grid, 
                                            is_str_column, get_select_defaults, whitecolor)

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

DISPLAY_FILTERS                 =   10
EDIT_FILTER                     =   11
DELETE_FILTER                   =   12
EDIT_CRITERIA                   =   13
SELECT_FILTER                   =   14

"""
#--------------------------------------------------------------------------
#    dfsubset main task bar
#--------------------------------------------------------------------------
"""
dfsubset_tb_doc_title               =   "Dataframe Subset"
dfsubset_tb_title                   =   "Dataframe Subset"
dfsubset_tb_id                      =   "dfsubsettb"

dfsubset_tb_keyTitleList            =   ["Get Dataframe Subset",
                                         "Clear","Reset","Help"]

dfsubset_tb_jsList                  =   ["get_subset_callback("+str(DISPLAY_GET_SUBSET)+")",
                                         "get_subset_callback("+str(DISPLAY_MAIN)+")",
                                         "process_pop_up_cmd(6)",
                                         "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_TASKBAR_ID) + ")"]

dfsubset_tb_centered                =   False

"""
#--------------------------------------------------------------------------
#   get subset input 
#--------------------------------------------------------------------------
"""
get_subset_input_title                  =   "Get Dataframe Subset"
get_subset_input_id                     =   "dcdfsubset"
get_subset_input_idList                 =   ["gsindataframe",
                                             "gsoutdataframe",
                                             "gscolnames",
                                             "gsadddrop",
                                             "subsetfname",
                                             None,None,None,None,None,None]

get_subset_input_labelList              =   ["input_dataframe",
                                             "output_dataframe",
                                             "column_names_list",
                                             "keep_column_names_list_flag",
                                             "csv_file_name",
                                             "Define</br>Filter(s)",
                                             "Get</br>Subset",
                                             "Display</br>Filter(s)",
                                             "Clear","Return","Help"]

get_subset_input_typeList               =   ["select","text",maketextarea(4),"select","file",
                                             "button","button","button","button","button","button"]

get_subset_input_placeholderList        =   ["dataframe to get subset from",
                                             "dataframe name to copy subset to (default - None)",
                                             "column names list to grab or drop - use Column Names table (default None = all columns)",
                                             "keep(True) or drop(False) columns in column name list (default = True)",
                                             "select file name to write to export as csv (default = None)",
                                             None,None,None,None,None,None]

get_subset_input_jsList                 =   [None,None,None,None,None,
                                             "get_subset_callback("+str(DISPLAY_GET_SUBSET_FILTER)+")",
                                             "get_subset_callback("+str(PROCESS_GET_SUBSET)+")",
                                             "get_subset_callback("+str(DISPLAY_FILTERS)+")",
                                             "get_subset_callback("+str(CLEAR_SUBSET_FORM)+")",
                                             "get_subset_callback("+str(DISPLAY_MAIN)+")",
                                             "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_ID) + ")"]

get_subset_input_reqList                =   [0,1,2]

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
                                               "gsselectstring",
                                               None,None,None,None,None,None]

get_subset_filter_input_labelList         =   ["filter_column_name",
                                               "filter_column_value(s)",
                                               "filter_column_value(s)_operator(s)",
                                               "filter_column_value(s)_logicals",
                                               "selection_criteria",
                                               "Add</br>Filter</br>To Criteria",
                                               "Display</br>Filters",
                                               "Get</br>Subset",
                                               "Clear","Return","Help"]

get_subset_filter_input_typeList          =   ["text",maketextarea(6),"text","text",maketextarea(3),
                                               "button","button","button","button","button","button"]

get_subset_filter_input_placeholderList   =   ["current filter column name - select from Condition Columns table",
                                               "current filter column value(s) - select from Column Values table or enter 'value' ",
                                               "current filter column operator(s) - '<' '<=' '>' '=>' '==' '!=' (default '==')",
                                               "select and/or logical to use between column sub filters (default = or)",
                                               "select string : can be editted manually (default - None)",
                                               None,None,None,None,None,None]

get_subset_filter_input_jsList            =   [None,None,None,None,None,
                                               "get_subset_callback("+str(ADD_FILTER)+")",
                                               "get_subset_callback("+str(DISPLAY_FILTERS)+")",
                                               "get_subset_callback("+str(PROCESS_GET_SUBSET_FILTERED)+")",
                                               "get_subset_callback("+str(CLEAR_FILTER_FORM)+")",
                                               "get_subset_callback("+str(DISPLAY_MAIN)+")",
                                               "displayhelp(" + str(dfchelp.DFSUBSET_FILTER_ID) + ")"]

get_subset_filter_input_reqList           =   [0,1,2,3,4]

get_subset_filter_input_form              =   [get_subset_filter_input_id,
                                               get_subset_filter_input_idList,
                                               get_subset_filter_input_labelList,
                                               get_subset_filter_input_typeList,
                                               get_subset_filter_input_placeholderList,
                                               get_subset_filter_input_jsList,
                                               get_subset_filter_input_reqList]  


"""
#--------------------------------------------------------------------------
#   get subset input 
#--------------------------------------------------------------------------
"""
get_subset_filters                      =   "Dataframe Subset Filters"
get_subset_filters_id                   =   "dcdfsubsetfilters"
get_subset_filters_idList               =   ["gsfiltername",
                                             "gsfilterlogic",
                                             None,None,None,None]

get_subset_filters_labelList            =   ["filter_name",
                                             "filter_logic",
                                             "Edit</br>Filter",
                                             "Delete</br>Filter",
                                             "Return","Help"]

get_subset_filters_typeList             =   ["text",maketextarea(10),
                                             "button","button","button","button"]

get_subset_filters_placeholderList      =   ["filter name",
                                             "filter logic",
                                             "df subset selection criteria",
                                             None,None,None,None]

get_subset_filters_jsList               =   [None,None,
                                             "get_subset_callback("+str(EDIT_FILTER)+")",
                                             "get_subset_callback("+str(DELETE_FILTER)+")",
                                             "get_subset_callback("+str(DISPLAY_GET_SUBSET_FILTER)+")",
                                             "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_ID) + ")"]

get_subset_filters_reqList              =   [0,1]

get_subset_filters_form                 =   [get_subset_filters_id,
                                             get_subset_filters_idList,
                                             get_subset_filters_labelList,
                                             get_subset_filters_typeList,
                                             get_subset_filters_placeholderList,
                                             get_subset_filters_jsList,
                                             get_subset_filters_reqList]  

    
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_dfsubset_main_taskbar() :
    
    from dfcleanser.common.display_utils import display_dfcleanser_taskbar
    display_dfcleanser_taskbar(ButtonGroupForm(dfsubset_tb_id,
                                               dfsubset_tb_keyTitleList,
                                               dfsubset_tb_jsList,
                                               dfsubset_tb_centered),False)


def get_dfsubset_input_parms(parms) :
   return(get_parms_for_input(parms,get_subset_input_idList))

def get_dfsubset_filter_input_parms(parms) :
   return(get_parms_for_input(parms,get_subset_filter_input_idList))


"""            
#--------------------------------------------------------------------------
#    display df subset status
#--------------------------------------------------------------------------
"""
def display_df_subset_status(df,out_df,filename,filtertext=None) :
    """
    * -------------------------------------------------------- 
    * function : display df subset status
    * 
    * parms :
    *   df          - dataframe
    *   out_df      - output dataframe
    *   filename    - output file name
    *   filtertext  - filter description
    *   
    * returns : operators html
    * --------------------------------------------------------
    """
    
    statusHeader    =   ["",""]
    statusRows      =   []
    statusWidths    =   [60,40]
    statusAligns    =   ["left","left"]
    
    colorList = []  
    
    statusRows.append(["Total Rows",len(df)])
    colorList.append([whitecolor,whitecolor])
    
    statusRows.append(["Total Columns",len(df.columns)])
    colorList.append([whitecolor,whitecolor])
    
    statusRows.append(["output dataframe",out_df])
    colorList.append([whitecolor,whitecolor])
    
    if(not (filename == None)) :
        statusRows.append(["output file",filename])
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
    """
    * -------------------------------------------------------- 
    * function : get math operators table
    * 
    * parms :
    *
    * returns : operators html
    * --------------------------------------------------------
    """
    
    operatorsHeader      =   [""]

    operatorsRows        =   []
    operatorsWidths      =   [100]
    operatorsAligns      =   ["center"]
    operatorsHrefs       =   []
    
    column_operators     =   ["==","!=","<","<=",">",">="]
    clause_operators     =   ["or","and"]
    
    for i in range(len(column_operators)) :
        operatorsRows.append([column_operators[i]])
        operatorsHrefs.append(["set_col_oper"])
        
    operatorsRows.append([" "])
    operatorsHrefs.append([None])
    operatorsRows.append([" "])
    operatorsHrefs.append([None])
    
    for i in range(len(clause_operators)) :
        operatorsRows.append([clause_operators[i]])
        operatorsHrefs.append(["set_clause_oper"])
    
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
    operators_table.set_smallheader(False)
    operators_table.set_border(False)
    operators_table.set_checkLength(False)
    operators_table.set_html_only(True) 
    
    operatorshtml   =   "" 
    operatorshtml   =   operators_table.get_html()
    
    return(operatorshtml)
        

def get_col_uniques_table(df,colname) :
    """
    * -------------------------------------------------------- 
    * function : get unique column values
    * 
    * parms :
    *  df       -   dataframe 
    *  colname  -   filters column name 
    *
    * returns : unique columns html
    * --------------------------------------------------------
    """
    
    columnuniquesHeader      =   [""]

    columnuniquesRows        =   []
    columnuniquesWidths      =   [100]
    columnuniquesAligns      =   ["left"]
    columnuniquesHrefs       =   []
    
    uniques =   [] 
        
    #check if the object is string
    if (is_str_column(cfg.get_dfc_dataframe(),colname)) :
        
        uniques =   cfg.get_dfc_dataframe()[colname].unique().tolist()
        for i in range(len(uniques)) :
            uniques[i]  =   str(uniques[i])
        uniques.sort()
    else :
        
        if(is_numeric_col(df,colname)) :           
            uniques =   cfg.get_dfc_dataframe()[colname].unique().tolist()
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


def get_dfsubset_table(df,filters=False,colname=None) :
    """
    * --------------------------------------------------------- 
    * function : get dfsubset table
    * 
    * parms :
    *  filters -   filters flag 
    *  colname -   filters column name 
    *
    * returns : N/A
    * --------------------------------------------------------
    """
 
    from dfcleanser.sw_utilities.sw_utility_geocode_widgets import get_df_col_names_table
    
    if(colname==None) :
        if(filters) :
            callback = "set_filter_colname"
        else :
            callback = "set_ds_colname"
    
        # get the drop flag and col name list
        dfsparms = cfg.get_config_value(get_subset_input_id+"Parms")
        
        if( (not(dfsparms == None)) and (len(dfsparms) > 0) ):
            collist = cfg.get_cfg_parm_from_input_list(get_subset_input_id,
                                                       "column_names_list",
                                                       get_subset_input_labelList)
            
            if(collist == "") :
                collist =  df.columns.get_values().tolist() 
            else :    
                #collist = dfsparms[3]
                collist = collist.split(",")
                for i in range(len(collist)) :
                    collist[i]  =   collist[i].rstrip(" ")    
            
            if(len(collist) > 0) :
                keepcols = True
                keepflag = cfg.get_cfg_parm_from_input_list(get_subset_input_id,
                                                           "column_names_list_flag",
                                                           get_subset_input_labelList)
                #keepflag = dfsparms[4]
                if(not (keepflag is None) ) :
                    if(keepflag == "False") :
                        keepcols = False
                
                if(keepcols) :
                    colnames = collist
                else :
                    colnames = []
                    allcols = cfg.get_dfc_dataframe().columns.tolist()
                    for i in range(len(allcols)) :
                        matched = False
                        for j in range(len(collist)) : 
                            if(allcols[i] == allcols[j]) :
                                matched = True
                            
                        if(not (matched)) :
                            colnames.append(allcols[i])
                
                if(len(colnames) > 0) :
                    col_names_html = get_df_col_names_table("dcsubsetcolnamesTable",
                                                            cfg.SWDFSubsetUtility_ID,callback,None,colnames)    
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
        col_names_html  =  get_col_uniques_table(cfg.get_dfc_dataframe(),colname) 

    return(col_names_html) 


def display_df_subset(df,filters=False,colname=None) :  
    """
    * -------------------------------------------------------------------------- 
    * function : display current df subset form
    * 
    * parms :
    *  df      -   dataframe to subset from
    *  filters -   filters form 
    *  colname -   filters column name 
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    if(not colname==None) :
        cfg.set_config_value(get_subset_filter_input_id+"Parms",[colname,"","","","",""])

    col_names_html  =   get_dfsubset_table(df,filters,colname)
    
    if(filters) :
        operators_html = get_operators_table()

    
    get_subset_input_html = ""
    
    if(filters) :
        
        from dfcleanser.common.html_widgets import InputForm
        get_filter_subset_input_form = InputForm(get_subset_filter_input_form[0],get_subset_filter_input_form[1],
                                                 get_subset_filter_input_form[2],get_subset_filter_input_form[3],
                                                 get_subset_filter_input_form[4],get_subset_filter_input_form[5],
                                                 get_subset_filter_input_form[6])
        
        get_filter_subset_input_form.set_shortForm(True)
        get_filter_subset_input_form.set_gridwidth(590)
        get_filter_subset_input_form.set_custombwidth(85)
        get_filter_subset_input_form.set_fullparms(True)
        
        get_subset_input_html = get_filter_subset_input_form.get_html() 
        
        print("\n")
        get_subset_heading_html =   "<div>Create Dataframe Subset Filter</div><br></br>"        

    else :
        
        from dfcleanser.common.html_widgets import InputForm
        subset_input_form = InputForm(get_subset_input_form[0],get_subset_input_form[1],
                                      get_subset_input_form[2],get_subset_input_form[3],
                                      get_subset_input_form[4],get_subset_input_form[5],
                                      get_subset_input_form[6])
    
    
        selectDicts     =   []
        
        dataframes      =   cfg.get_dfc_dataframes_select_list()
        selectDicts.append(dataframes)
        
        subssel         =   {"default":"True","list":["True","False"]}
        selectDicts.append(subssel)
        
        get_select_defaults(subset_input_form,
                            get_subset_input_form[0],
                            get_subset_input_form[1],
                            get_subset_input_form[3],
                            selectDicts)
        
        subset_input_form.set_shortForm(False)
        subset_input_form.set_gridwidth(700)
        subset_input_form.set_custombwidth(100)
        subset_input_form.set_fullparms(True)
        
        get_subset_input_html = subset_input_form.get_html() 
            
        get_subset_heading_html =   "<div>Get Dataframe Subset</div><br></br>"
    
    if(filters) :
        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-main","dfc-right"]
        gridhtmls       =   [get_subset_heading_html,col_names_html,operators_html,get_subset_input_html]
    
        display_generic_grid("dfsubset-wrapper",gridclasses,gridhtmls)
        
    else :
        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right"]
        gridhtmls       =   [get_subset_heading_html,col_names_html,get_subset_input_html]
        
        print("\n")
        display_generic_grid("sw-utils-wrapper",gridclasses,gridhtmls)



def get_filters_table() :
    """
    * -------------------------------------------------------- 
    * function : get filters table
    * 
    * parms :
    *
    * returns : filters html
    * --------------------------------------------------------
    """
    
    filtersHeader     =   [""]

    filtersRows       =   []
    filtersWidths     =   [100]
    filtersAligns     =   ["left"]
    filtersHrefs      =   []
    
    filtersDict       =   cfg.get_config_value(cfg.CURRENT_SUBSET_FILTERS)
    
    if(not(filtersDict == None)) :
        
        for key in filtersDict.keys() :
            filtersRows.append([filtersDict.get(key).get("title")])
            filtersHrefs.append(["select_filter"])
        
    else :
        filtersRows.append(["no Filters"])
        filtersHrefs.append([""])
        
    filters_table = dcTable("Subset Filters",
                            "dcfiltersTable",
                            cfg.SWDFSubsetUtility_ID,
                            filtersHeader,filtersRows,
                            filtersWidths,filtersAligns)

    filters_table.set_refList(filtersHrefs)
    filters_table.set_small(True)
    filters_table.set_smallwidth(98)
    filters_table.set_smallmargin(10)
    filters_table.set_border(True)
    filters_table.set_checkLength(True)
    filters_table.set_textLength(40)
    filters_table.set_html_only(True) 
    filters_table.set_tabletype(ROW_MAJOR)
    filters_table.set_rowspertable(14)

    filtershtml = get_row_major_table(filters_table,SCROLL_NEXT,False)

    return(filtershtml)
        

def display_filters(df) :
    """
    * -------------------------------------------------------------------------- 
    * function : display current df subset form
    * 
    * parms :
    *  df      -   dataframe to subset from
    *  filters -   filters form 
    *  colname -   filters column name 
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    print("display_filters")    
    
    
    filter_names_html  =   get_filters_table()
    
    
    filters_input_html = ""
    
    from dfcleanser.common.html_widgets import InputForm
    filters_input_form = InputForm(get_subset_filters_form[0],get_subset_filters_form[1],
                                   get_subset_filters_form[2],get_subset_filters_form[3],
                                   get_subset_filters_form[4],get_subset_filters_form[5],
                                   get_subset_filters_form[6])
    
    dataframes      =   cfg.get_dfc_dataframes_select_list()
        
    get_select_defaults(filters_input_form,
                        get_subset_filters_form[0],
                        get_subset_filters_form[1],
                        get_subset_filters_form[3],
                        [dataframes])
        
    filters_input_form.set_shortForm(False)
    filters_input_form.set_gridwidth(700)
    filters_input_form.set_custombwidth(110)
    filters_input_form.set_fullparms(True)
        
    filters_input_html = filters_input_form.get_html() 
            
    filters_heading_html =   "<div>Dataframe Subset Filters</div><br></br>"
    
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right"]
    gridhtmls       =   [filters_heading_html,filter_names_html,filters_input_html]
    
    print("\n")    
    display_generic_grid("sw-utils-wrapper",gridclasses,gridhtmls)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    