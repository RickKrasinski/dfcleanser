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

import dfcleanser.sw_utilities.sw_utility_dfsubset_model as swsm
import dfcleanser.sw_utilities.sw_utility_dfsubset_control as swsc

from dfcleanser.common.html_widgets import (maketextarea, ButtonGroupForm)

from dfcleanser.common.table_widgets import dcTable, get_row_major_table, SCROLL_DOWN, ROW_MAJOR

from dfcleanser.common.common_utils import (get_parms_for_input, is_numeric_col, display_generic_grid, 
                                            is_str_column, get_select_defaults, whitecolor)

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

dfsubset_tb_jsList                  =   ["get_subset_callback("+str(swsm.DISPLAY_GET_SUBSET)+")",
                                         "get_subset_callback("+str(swsm.DISPLAY_MAIN)+")",
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
                                             None,None,None,None,None]

get_subset_input_labelList              =   ["input_dataframe",
                                             "output_dataframe",
                                             "column_names_list",
                                             "grab_columns_in_column_names_list_flag",
                                             "csv_file_name",
                                             "Define</br>Filter(s)",
                                             "Get</br>Subset",
                                             "Clear","Return","Help"]

get_subset_input_typeList               =   ["select","text","selectmultiple","select","file",
                                             "button","button","button","button","button"]

get_subset_input_placeholderList        =   ["dataframe to get subset from",
                                             "dataframe name to copy subset to (default - None overwrite input_dataframe)",
                                             "column names list to grab or drop from input_dataframe (default None = all columns grabbed)",
                                             "keep(True) or drop(False) columns in column name list (default = True)",
                                             "select file name to export as csv file (default = None)",
                                             None,None,None,None,None,None]

get_subset_input_jsList                 =   [None,None,None,None,None,
                                             "get_subset_callback("+str(swsm.DISPLAY_GET_SUBSET_FILTER)+")",
                                             "get_subset_callback("+str(swsm.PROCESS_GET_SUBSET)+")",
                                             "get_subset_callback("+str(swsm.CLEAR_SUBSET_FORM)+")",
                                             "get_subset_callback("+str(swsm.DISPLAY_MAIN)+")",
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
                                               "gsfilterselectstring",
                                               "gsselectstring",
                                               None,None,None,None,None]

get_subset_filter_input_labelList         =   ["filter_column_name",
                                               "filter_select_string",
                                               "subset_selection_criteria",
                                               "Add</br>Filter</br>To Criteria",
                                               "Get</br>Subset",
                                               "Clear</br>Current</br>Filter","Return","Help"]

get_subset_filter_input_typeList          =   ["text",maketextarea(3),maketextarea(6),
                                               "button","button","button","button","button"]

get_subset_filter_input_placeholderList   =   ["current filter column name - select from Condition Columns table",
                                               "current filter column value(s) - select from Column Values table or enter 'value' ",
                                               "select string : can be editted manually (default - None)",
                                               None,None,None,None,None]

get_subset_filter_input_jsList            =   [None,None,None,
                                               "get_subset_callback("+str(swsm.ADD_FILTER)+")",
                                               "get_subset_callback("+str(swsm.PROCESS_GET_SUBSET_FILTERED)+")",
                                               "get_subset_callback("+str(swsm.CLEAR_FILTER_FORM)+")",
                                               "get_subset_callback("+str(swsm.DISPLAY_MAIN)+")",
                                               "displayhelp(" + str(dfchelp.DFSUBSET_FILTER_ID) + ")"]

get_subset_filter_input_reqList           =   [0,1,2]

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
                                             "get_subset_callback("+str(swsm.EDIT_FILTER)+")",
                                             "get_subset_callback("+str(swsm.DELETE_FILTER)+")",
                                             "get_subset_callback("+str(swsm.DISPLAY_GET_SUBSET_FILTER)+")",
                                             "displayhelp(" + str(dfchelp.DFSUBSET_MAIN_ID) + ")"]

get_subset_filters_reqList              =   [0,1]

get_subset_filters_form                 =   [get_subset_filters_id,
                                             get_subset_filters_idList,
                                             get_subset_filters_labelList,
                                             get_subset_filters_typeList,
                                             get_subset_filters_placeholderList,
                                             get_subset_filters_jsList,
                                             get_subset_filters_reqList]  

import dfcleanser.data_inspection.data_inspection_widgets as diw

SWUtility_subset_inputs                 =   [get_subset_input_id, get_subset_filter_input_id, get_subset_filters_id, diw.data_subset_df_input_id] 


keypad_container = """
    <div style="margin-top:5px; padding-top:5px;">
    <div class='container dc-table-container' style="margin-left:30px; width:640px; margin-top:5px;">
        <div>
            <table class="table dc-table" id="keypadTable" style="border:3px solid #428bca;">
                <tbody>
                    <tr class="dc-describe-table-body-row">
                        <td style=" width:9%; width:20px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="keypad(0)">0</button>
                        </td>
                        <td style=" width:9%; width:20px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="keypad(1)">1</button>
                        </td>
                        <td style=" width:8%; width:20px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="keypad(2)">2</button>
                        </td>
                        <td style=" width:8%; width:20px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="keypad(3)">3</button>
                        </td>
                        <td style=" width:8%; width:20px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="keypad(4)">4</button>
                        </td>
                        <td style=" width:8%; width:20px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="keypad(5)">5</button>
                        </td>
                        <td style=" width:8%; width:20px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="keypad(6)">6</button>
                        </td>
                        <td style=" width:8%; width:20px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="keypad(7)">7</button>
                        </td>
                        <td style=" width:8%; width:20px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="keypad(8)">8</button>
                        </td>
                        <td style=" width:8%; width:20px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="keypad(9)">9</button>
                        </td>
                        <td style=" width:9%; width:20px; height:20px;">
                            <button type="button" style="font-size:12px; font-weight:bold;" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="keypad('.')"><span style='font-size:20px; font-weight:bold;'>.</span></button>
                        </td>
                        <td style=" width:9%; width:20px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="keypad(',')"><span style='font-size:20px; font-weight:bold;'>,</span></button>
                        </td>

                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    </div>
"""

operator_keypad_container = """
    <div class='container dc-table-container' style=" margin-left:30px; width:640px; padding-top:5px; font-family:arial; font-size:12px;">
        <div>
            <table class="table dc-table" id="opeatorTable" style="border:3px solid #428bca;">
                <tbody>
                    <tr class="dc-describe-table-body-row">
                        <td style=" width:10%; width:20px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="operpad('==')">==</button>
                        </td>
                        <td style=" width:10%; width:20px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="operpad('!=')">!=</button>
                        </td>
                        <td style=" width:9%; width:20px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="operpad('<')">&lt;</button>
                        </td>
                        <td style=" width:10%; width:20px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="operpad('<=')">&lt;=</button>
                        </td>
                        <td style=" width:9%; width:20px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="operpad('>')">></button>
                        </td>
                        <td style=" width:10%; width:20px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="operpad('>=')">>=</button>
                        </td>
                        <td style=" width:13%; width:40px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="operpad('.isin()')">isin</button>
                        </td>
                        <td style=" width:14%; width:40px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="operpad('.isnull()')">isnull</button>
                        </td>
                        <td style=" width:15%; width:40px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="operpad('.notnull()')">notnull</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
"""

logic_keypad_container = """
    <div class='container dc-table-container' style=" margin-left:30px; width:640px; padding-top:5px;">
        <div>
            <table class="table dc-table" id="opeatorTable" style="border:3px solid #428bca;">
                <tbody>
                    <tr class="dc-describe-table-body-row">
                        <td style=" width:20%; width:20px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="logicpad('or')">or</button>
                        </td>
                        <td style=" width:20%; width:20px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="logicpad('and')">and</button>
                        </td>
                        <td style=" width:20%; width:20px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="logicpad('|')">|</button>
                        </td>
                        <td style=" width:20%; width:20px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="logicpad('&')">&</button>
                        </td>
                        <td style=" width:20%; width:20px; height:20px;">
                            <button type="button" class="btn btn-outline-primary waves-effect dc-btn-subset" onclick="logicpad('~')">~</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
"""
    
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
def display_df_subset_status(out_df,filename,runtime,filtertext=None) :
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
    
    statusRows.append(["output dataframe",out_df])
    colorList.append([whitecolor,whitecolor])
    
    statusRows.append(["Total Rows",len(cfg.get_dfc_dataframe_df(out_df))])
    colorList.append([whitecolor,whitecolor])
    
    statusRows.append(["Total Columns",len(cfg.get_dfc_dataframe_df(out_df).columns)])
    colorList.append([whitecolor,whitecolor])
    
    statusRows.append(["Total Run Time",runtime])
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
    if (is_str_column(swsc.get_subset_df(),colname)) :
        
        uniques =   swsc.get_subset_df()[colname].unique().tolist()
        for i in range(len(uniques)) :
            uniques[i]  =   str(uniques[i])
        uniques.sort()
    else :
        
        if(is_numeric_col(df,colname)) :           
            uniques =   swsc.get_subset_df()[colname].unique().tolist()
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

    tablehtml = get_row_major_table(columnuniques_table,SCROLL_DOWN,False)
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
 
    from dfcleanser.common.display_utils import get_df_col_names_table
    
    if(colname==None) :
        if(filters) :
            callback = "set_filter_colname"
        else :
            callback = "set_ds_colname"
        
        col_names_html = get_df_col_names_table(df,"dcsubsetcolnamesTable",
                                                cfg.SWDFSubsetUtility_ID,callback)

    else :
        col_names_html  =  get_col_uniques_table(df,colname) 

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
    
    print("display_df_subset",filters,colname)
    
    if(not colname==None) :
        cfg.set_config_value(get_subset_filter_input_id+"Parms",[colname,"","","","",""])

    col_names_html  =   get_dfsubset_table(df,filters,colname)
    
    get_subset_input_html = ""
    
    if(filters) :
        
        from dfcleanser.common.html_widgets import InputForm
        get_filter_subset_input_form = InputForm(get_subset_filter_input_form[0],get_subset_filter_input_form[1],
                                                 get_subset_filter_input_form[2],get_subset_filter_input_form[3],
                                                 get_subset_filter_input_form[4],get_subset_filter_input_form[5],
                                                 get_subset_filter_input_form[6])
        
        get_filter_subset_input_form.set_shortForm(False)
        get_filter_subset_input_form.set_gridwidth(680)
        get_filter_subset_input_form.set_custombwidth(110)
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
        
        dataframes      =   cfg.get_dfc_dataframes_select_list(cfg.SWDFSubsetUtility_ID)
        selectDicts.append(dataframes)
        
        current_df      =   cfg.get_current_chapter_df(cfg.SWDFSubsetUtility_ID)
        colnames        =   current_df.columns.tolist()
        cols_name_list  =   ["all"]
        for i in range(len(colnames)) :
            cols_name_list.append(colnames[i])
            
        cnames          =   {"default":cols_name_list[0],"list": cols_name_list,"size":10}
        selectDicts.append(cnames)
        
        subssel         =   {"default":"True","list":["True","False"]}
        selectDicts.append(subssel)
        
        get_select_defaults(subset_input_form,
                            get_subset_input_form[0],
                            get_subset_input_form[1],
                            get_subset_input_form[3],
                            selectDicts)
        
        subset_input_form.set_shortForm(False)
        subset_input_form.set_gridwidth(680)
        subset_input_form.set_custombwidth(110)
        subset_input_form.set_fullparms(True)
        
        get_subset_input_html = subset_input_form.get_html() 
            
        get_subset_heading_html =   "<div>Get Dataframe Subset</div><br></br>"
    
    if(filters) :
        
        if(cfg.get_config_value(cfg.CURRENT_SUBSET_FILTERS) is None) :
            help_note           =   "Select a column name to use as the value for the filter."
        else :
            help_note           =   "If defining another filter select '|' or '&' to join new filter to old filters and then select a column name to use as the value for the filter.</br>If done defining filters hit 'Get Subset' to get the subset."
        
        from dfcleanser.common.common_utils import get_help_note_html
        filter_notes_html   =   get_help_note_html(help_note,None,None,"addfilternote")

        gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right","dfc-top","dfc-main","dfc-bottom","dfc-footer"]
        gridhtmls       =   [get_subset_heading_html,col_names_html,get_subset_input_html,keypad_container,operator_keypad_container,logic_keypad_container,filter_notes_html]
    
        display_generic_grid("dfsubset-wrapper",gridclasses,gridhtmls)
        
    else :
        
        help_note           =   "Select columns to keep or drop with the 'column_names_list." + "<br>" + "Once you select the columns you can get a subset or define filters to get a subset."
        from dfcleanser.common.common_utils import get_help_note_html
        subset_notes_html   =   get_help_note_html(help_note,None,None,"addfilternote")

        
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-bottom","dfc-footer"]
        gridhtmls       =   [get_subset_heading_html,get_subset_input_html,subset_notes_html]
        
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

    filtershtml = get_row_major_table(filters_table,SCROLL_DOWN,False)

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
    #print("display_filters")    
    
    
    filter_names_html  =   get_filters_table()
    
    
    filters_input_html = ""
    
    from dfcleanser.common.html_widgets import InputForm
    filters_input_form = InputForm(get_subset_filters_form[0],get_subset_filters_form[1],
                                   get_subset_filters_form[2],get_subset_filters_form[3],
                                   get_subset_filters_form[4],get_subset_filters_form[5],
                                   get_subset_filters_form[6])
    
    dataframes      =   cfg.get_dfc_dataframes_select_list(cfg.SWDFSubsetUtility_ID)
        
    get_select_defaults(filters_input_form,
                        get_subset_filters_form[0],
                        get_subset_filters_form[1],
                        get_subset_filters_form[3],
                        [dataframes])
        
    filters_input_form.set_shortForm(False)
    filters_input_form.set_gridwidth(600)
    filters_input_form.set_custombwidth(110)
    filters_input_form.set_fullparms(True)
        
    filters_input_html = filters_input_form.get_html() 
            
    filters_heading_html =   "<div>Dataframe Subset Filters</div><br></br>"
    
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right"]
    gridhtmls       =   [filters_heading_html,filter_names_html,filters_input_html]
    
    print("\n")    
    display_generic_grid("sw-utils-filters-wrapper",gridclasses,gridhtmls)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    