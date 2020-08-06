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

from dfcleanser.common.html_widgets import (maketextarea, ButtonGroupForm, makefilearea)

from dfcleanser.common.table_widgets import dcTable, get_row_major_table, SCROLL_DOWN, ROW_MAJOR

from dfcleanser.common.common_utils import (get_parms_for_input, is_numeric_col, display_generic_grid, 
                                            get_select_defaults)

"""
#--------------------------------------------------------------------------
#    dfsubset main task bar
#--------------------------------------------------------------------------
"""
dfsubset_tb_doc_title               =   "Dataframe Subset"
dfsubset_tb_title                   =   "Dataframe Subset"
dfsubset_tb_id                      =   "dfsubsettb"

dfsubset_tb_keyTitleList            =   ["Create Dataframe</br>Subset",
                                         "Run Saved</br>Subset",
                                         "Clear","Reset","Help"]

dfsubset_tb_jsList                  =   ["get_subset_callback("+str(swsm.DISPLAY_GET_SUBSET)+")",
                                         "get_subset_callback("+str(swsm.DISPLAY_SAVED_SUBSET)+")",
                                         "get_subset_callback("+str(swsm.DISPLAY_MAIN)+")",
                                         "process_pop_up_cmd(6)",
                                         "displayhelp('" + str(dfchelp.DFSUBSET_MAIN_TASKBAR_ID) + "')"]

dfsubset_tb_centered                =   False

"""
#--------------------------------------------------------------------------
#   get subset input 
#--------------------------------------------------------------------------
"""
get_subset_input_title                  =   "Get Dataframe Subset"
get_subset_input_id                     =   "dcdfsubset"
get_subset_input_idList                 =   ["gsindataframe",
                                             "gscolnames",
                                             "gsdfcolnames",
                                             "gsadddrop",
                                             None,None,None]

get_subset_input_labelList              =   ["input_dataframe",
                                             "column_names_list",
                                             "input_dataframe_column_names",
                                             "action_for_columns_in_column_names_list",
                                             "Define</br>Subset</br>Criteria",
                                             "Return","Help"]

get_subset_input_typeList               =   ["select","text","select","select",
                                             "button","button","button"]

get_subset_input_placeholderList        =   ["dataframe to get subset from",
                                             "column names list to keep or drop from input_dataframe (default None = all columns KEEP)",
                                             "input dataframe column names",
                                             "keep(True) or drop(False) columns in column_names_list (default = True)",
                                             None,None,None]

get_subset_input_jsList                 =   [None,None,None,None,
                                             "get_subset_callback("+str(swsm.PROCESS_GET_SUBSET)+")",
                                             "get_subset_callback("+str(swsm.DISPLAY_MAIN)+")",
                                             "'displayhelp(" + str(dfchelp.DFSUBSET_MAIN_ID) + "')"]

get_subset_input_reqList                =   [0,1]

get_subset_input_form                   =   [get_subset_input_id,
                                             get_subset_input_idList,
                                             get_subset_input_labelList,
                                             get_subset_input_typeList,
                                             get_subset_input_placeholderList,
                                             get_subset_input_jsList,
                                             get_subset_input_reqList]  


"""
#--------------------------------------------------------------------------
#   get subset input 
#--------------------------------------------------------------------------
"""
get_manual_input_title                  =   "Get Dataframe Subset"
get_manual_input_id                     =   "dcdfmanualsubset"
get_manual_input_idList                 =   ["gsindataframe",
                                             "gscolnames",
                                             "gsdfcolnames",
                                             "gsadddrop",
                                             None,None,None]

get_manual_input_labelList              =   ["input_dataframe",
                                             "column_names_list",
                                             "input_dataframe_column_names",
                                             "action_for_columns_in_column_names_list",
                                             "Get</br>Next</br>Criteria",
                                             "Return","Help"]

get_manual_input_typeList               =   ["select","text","select","select",
                                             "button","button","button"]

get_manual_input_placeholderList        =   ["dataframe to get subset from",
                                             "column names list to keep or drop from input_dataframe (default None = all columns KEEP)",
                                             "input dataframe column names",
                                             "keep(True) or drop(False) columns in column_names_list (default = True)",
                                             None,None,None]

get_manual_input_jsList                 =   [None,None,None,None,
                                             "get_subset_callback("+str(swsm.PROCESS_GET_NEXT_SUBSET)+")",
                                             "get_subset_callback("+str(swsm.DISPLAY_MAIN)+")",
                                             "'displayhelp(" + str(dfchelp.DFSUBSET_MAIN_ID) + "')"]

get_manual_input_reqList                =   [0,1]

get_manual_input_form                   =   [get_manual_input_id,
                                             get_manual_input_idList,
                                             get_manual_input_labelList,
                                             get_manual_input_typeList,
                                             get_manual_input_placeholderList,
                                             get_manual_input_jsList,
                                             get_manual_input_reqList]  



"""
#--------------------------------------------------------------------------
#   get subset criteria input 
#--------------------------------------------------------------------------
"""
get_subset_criteria_input_title           =   "Get Dataframe Subset Search Criteria"
get_subset_criteria_input_id              =   "dcdfsubsetsearch"
get_subset_criteria_input_idList          =   ["dfsubsettitle",
                                               "dfselectpreamble",
                                               "gsselectstring",
                                               "dfselectpostamble",
                                               None,None,None,None]

get_subset_criteria_input_labelList       =   ["subset_dataframe_title",
                                               " ",
                                               "subset_selection_criteria",
                                               " ",
                                               "Get Subset</br>From</br>Criteria",
                                               "Clear","Return","Help"]

get_subset_criteria_input_typeList        =   ["text",maketextarea(2),maketextarea(12),maketextarea(3),
                                               "button","button","button","button"]

get_subset_criteria_input_placeholderList =   ["enter title for subset df created via criteria",
                                               " ",
                                               "select string : can be editted manually (default - None)",
                                               " ",
                                               None,None,None,None]

get_subset_criteria_input_jsList          =   [None,None,None,None,
                                               "get_subset_callback("+str(swsm.PROCESS_RUN_CRITERIA)+")",
                                               "get_subset_callback("+str(swsm.CLEAR_FILTER_FORM)+")",
                                               "get_subset_callback("+str(swsm.DISPLAY_MAIN)+")",
                                               "displayhelp('" + str(dfchelp.DFSUBSET_FILTER_ID) + "')"]

get_subset_criteria_input_reqList         =   [0,2]




get_next_criteria_input_id                =   "dcdfnextsearch"
get_next_criteria_input_idList            =   ["dfsubsettitle",
                                               "dfselectpreamble",
                                               "gsnextselectstring",
                                               "dfselectpostamble",
                                               None,None,None,None]

get_next_criteria_input_labelList         =   ["subset_dataframe_title",
                                               " ",
                                               "subset_selection_criteria",
                                               " ",
                                               "Run</br>Next</br>Criteria",
                                               "Clear","Return","Help"]

get_next_criteria_input_jsList            =   [None,None,None,None,
                                               "get_subset_callback("+str(swsm.PROCESS_NEXT_CRITERIA)+")",
                                               "get_subset_callback("+str(swsm.CLEAR_NEXT_FILTER_FORM)+")",
                                               "get_subset_callback("+str(swsm.DISPLAY_MAIN)+")",
                                               "displayhelp('" + str(dfchelp.DFSUBSET_FILTER_ID) + "')"]


"""
#--------------------------------------------------------------------------
#   get process subset criteria input 
#--------------------------------------------------------------------------
"""
get_subset_run_input_title              =   "Run Dataframe Subset"
get_subset_run_input_id                 =   "dcrundfsubset"
get_subset_run_input_idList             =   ["rundataframe",
                                             "runcolnames",
                                             "rundfcolnames",
                                             "runadddrop",
                                             None,None,None,None,None,None]

get_subset_run_input_labelList          =   ["subset_dataframe_title",
                                             "subset_dataframe_column_names_list",
                                             "subset_dataframe_column_names",
                                             "action_for_columns_in_subset_dataframe_column_names_list",
                                             "Save</br>Subset</br>And Exit",
                                             "Get</br>Next</br>Subset",
                                             "Inspect</br>Subset</br>Dataframe",
                                             "Open</br>Subset</br>In Excel",
                                             "Return","Help"]

get_subset_run_input_typeList           =   ["text","text","select","select",
                                             "button","button","button","button","button","button"]

get_subset_run_input_placeholderList    =   ["subset dataframe title",
                                             "column names list to keep or drop from subset_dataframe (default None = all columns KEEP)",
                                             "subset dataframe column names",
                                             "Keep or Drop columns in column_names_list (default = Keep)",
                                             None,None,None,None,None,None]

get_subset_run_input_jsList             =   [None,None,None,None,
                                             "get_subset_callback("+str(swsm.DISPLAY_SAVE_SUBSET) + ")",
                                             "get_subset_callback("+str(swsm.DISPLAY_SAVE_AND_GET_SUBSET)+")",
                                             "get_subset_callback("+str(swsm.INSPECT_DF)+")",
                                             "get_subset_callback("+str(swsm.OPEN_IN_EXCEL)+")",
                                             "get_subset_callback("+str(swsm.DISPLAY_MAIN)+")",
                                             "'displayhelp(" + str(dfchelp.DFSUBSET_MAIN_ID) + "')"]

get_subset_run_input_reqList            =   [0,1,2,3]

get_subset_run_input_form               =   [get_subset_run_input_id,
                                             get_subset_run_input_idList,
                                             get_subset_run_input_labelList,
                                             get_subset_run_input_typeList,
                                             get_subset_run_input_placeholderList,
                                             get_subset_run_input_jsList,
                                             get_subset_run_input_reqList]  


"""
#--------------------------------------------------------------------------
#   get save subset input 
#--------------------------------------------------------------------------
"""
get_subset_save_input_title             =   "Save Dataframe Subset"
get_subset_save_input_id                =   "dcsavedfsubset"
get_subset_save_input_idList            =   ["gsoutdataframe",
                                             "subsetfname",
                                             "savesubsetname",
                                             None,None,None]

get_subset_save_input_labelList         =   ["dfc_dataframe_name_to_save_final_subset_dataframe_to",
                                             "csv_file_name_to_save_final_subset_dataframe_to",
                                             "subset_sequence_name",
                                             "Save</br>Subset</br>dataframe",
                                             "Return","Help"]

get_subset_save_input_typeList          =   ["text",makefilearea(2),"text",
                                             "button","button","button"]

get_subset_save_input_placeholderList   =   ["dfc dataframe name to copy final subset dataframe to (default - Not saved as dfc dataframe)",
                                             "select file name to export final subset dataframe to as csv file (default = None)",
                                             "name to save subset sequence to : default( None - squence not saved)",
                                             None,None,None]

get_subset_save_input_jsList            =   [None,None,None,
                                             "get_subset_callback("+str(swsm.PROCESS_SAVE_SUBSET) + ")",
                                             "get_subset_callback("+str(swsm.DISPLAY_MAIN)+")",
                                             "'displayhelp(" + str(dfchelp.DFSUBSET_MAIN_ID) + "')"]

get_subset_save_input_reqList           =   [0,1,2]

get_subset_save_input_form              =   [get_subset_save_input_id,
                                             get_subset_save_input_idList,
                                             get_subset_save_input_labelList,
                                             get_subset_save_input_typeList,
                                             get_subset_save_input_placeholderList,
                                             get_subset_save_input_jsList,
                                             get_subset_save_input_reqList]  


"""
#--------------------------------------------------------------------------
#   get saved save subset input 
#--------------------------------------------------------------------------
"""
get_saved_save_input_title              =   "Save Dataframe Subset"
get_saved_save_input_id                 =   "dcsavesavedfsubset"
get_saved_save_input_idList             =   ["gsoutdataframe",
                                             "subsetfname",
                                             "savesubsetname",
                                             "savesubsetdropflag",
                                             None,None,None,None]

get_saved_save_input_labelList          =   ["dfc_dataframe_name_to_save_final_subset_dataframe_to",
                                             "csv_file_name_to_save_final_subset_dataframe_to",
                                             "subset_sequence_name",
                                             "drop_original_sequence",
                                             "Save</br>Subset</br>dataframe",
                                             "Add</br>New</br>Step",
                                             "Return","Help"]

get_saved_save_input_typeList           =   ["text",makefilearea(2),"text","select",
                                             "button","button","button","button"]

get_saved_save_input_placeholderList    =   ["dfc dataframe name to copy final subset dataframe to (default - Not saved as dfc dataframe)",
                                             "select file name to export final subset dataframe to as csv file (default = None)",
                                             "name to save subset sequence to : default( None - squence not saved)",
                                             "drop original subset sequence : default( False)",
                                             None,None,None,None]

get_saved_save_input_jsList             =   [None,None,None,None,
                                             "get_subset_callback("+str(swsm.PROCESS_SAVE_SAVED_SUBSET) + ")",
                                             "get_subset_callback("+str(swsm.DISPLAY_NEW_STEP) + ")",
                                             "get_subset_callback("+str(swsm.DISPLAY_MAIN)+")",
                                             "'displayhelp(" + str(dfchelp.DFSUBSET_MAIN_ID) + "')"]

get_saved_save_input_reqList            =   [0,1,2,3]

get_saved_save_input_form               =   [get_saved_save_input_id,
                                             get_saved_save_input_idList,
                                             get_saved_save_input_labelList,
                                             get_saved_save_input_typeList,
                                             get_saved_save_input_placeholderList,
                                             get_saved_save_input_jsList,
                                             get_saved_save_input_reqList]  




"""
#--------------------------------------------------------------------------
#   get save subset input 
#--------------------------------------------------------------------------
"""
get_subset_sequences_input_title             =   "Display Subset Sequences"
get_subset_sequences_input_id                =   "sequencesubset"
get_subset_sequences_input_idList            =   ["subseqtitle",
                                                  "subseqrun",
                                                  None,None,None]

get_subset_sequences_input_labelList         =   ["subset_sequence_title",
                                                  "subset_sequence_run_method",
                                                  "Run</br>Subset</br>Sequence",
                                                  "Return","Help"]

get_subset_sequences_input_typeList          =   ["select","select",
                                                  "button","button","button"]

get_subset_sequences_input_placeholderList   =   ["subset sequence title",
                                                  "subset sequence run method",
                                                  None,None,None]

get_subset_sequences_input_jsList            =   [None,None,
                                                  "get_subset_callback("+str(swsm.PROCESS_SUBSET_SEQUENCE) + ")",
                                                  "get_subset_callback("+str(swsm.DISPLAY_MAIN)+")",
                                                  "'displayhelp(" + str(dfchelp.DFSUBSET_MAIN_ID) + "')"]

get_subset_sequences_input_reqList           =   [0,1]

get_subset_sequences_input_form              =   [get_subset_sequences_input_id,
                                                  get_subset_sequences_input_idList,
                                                  get_subset_sequences_input_labelList,
                                                  get_subset_sequences_input_typeList,
                                                  get_subset_sequences_input_placeholderList,
                                                  get_subset_sequences_input_jsList,
                                                  get_subset_sequences_input_reqList]  



SWUtility_subset_inputs                 =   [get_subset_input_id, get_subset_criteria_input_id, get_subset_run_input_id, get_subset_save_input_id, get_subset_sequences_input_id] 



   
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
   return(get_parms_for_input(parms,get_subset_criteria_input_idList))



def get_column_stats_table(df_title,df,small=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : get col stats for df columns
    * 
    * parms :
    *  df_title -   dataframe title
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    #print("get_column_stats_table",df_title,small)
    
    
    colstatsHeader        =   ["Column Name","Dtype","Max","Min","Num Uniques"]
    colstatsRows          =   []
    colstatsWidths        =   [30,15,20,20,15]
    colstatsAligns        =   ["left","left","left","left","center"]
    
    rowColors             =   []
    
    index_columns   =   df.index.names
    
    if(len(index_columns) > 0) :
        for i in range(len(index_columns)) :
            if( not (index_columns[i] is None) ) :
                colstatsRows.append([index_columns[i],
                                     str(df.index.levels[i].dtype),
                                     str(df.index.levels[i].max()),
                                     str(df.index.levels[i].min()),
                                     str(len(df.index.levels[i].unique()))])
                
                rowColors.append("#ffffcc")
                                 
    columns     =   list(df.columns)
    
    for i in range(len(columns)) :
        
        col_dtype  =   df[columns[i]].dtype
        
        if(is_numeric_col(df,columns[i])) :
            col_max     =   str(df[columns[i]].max())
            col_min     =   str(df[columns[i]].min())
        else :
            col_max     =   ""
            col_min     =   ""
            
        col_unique_count    =   str(len(df[columns[i]].unique()))
        
        colstatsRows.append([columns[i],str(col_dtype),col_max,col_min,col_unique_count])
    
    colstats_table        =   None
    
    from dfcleanser.common.table_widgets import dcTable, get_row_major_table, ROW_MAJOR, SCROLL_DOWN
    
    colstats_table        =   dcTable("Column Stats For dataframe '" + str(df_title) + "'",'colstatsid',
                                      cfg.SWDFSubsetUtility_ID,
                                      colstatsHeader,colstatsRows,
                                      colstatsWidths,colstatsAligns)
            
    colstats_table.set_small(True)
    
    if(len(rowColors) > 0) :
       colstats_table.set_row_color_list(rowColors)     
    
    if(small) :
        colstats_table.set_smallwidth(60)
        colstats_table.set_smallmargin(200)
    else :   
        colstats_table.set_smallwidth(90)
        colstats_table.set_smallmargin(30)
    
    colstats_table.set_checkLength(True)

    colstats_table.set_border(True)
    colstats_table.set_tabletype(ROW_MAJOR)
    colstats_table.set_rowspertable(50)
    colstatsHtml = get_row_major_table(colstats_table,SCROLL_DOWN,False)
    
    return(colstatsHtml+"<br>")


def display_df_subset_setup() :  
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
    df_title    =   cfg.get_config_value(cfg.CURRENT_SUBSET_DF)
    df          =   cfg.get_dfc_dataframe_df(df_title)
    
    col_stats_table     =   get_column_stats_table(df_title,df)
        
    from dfcleanser.common.html_widgets import InputForm
    subset_input_form = InputForm(get_subset_input_id,
                                  get_subset_input_idList,
                                  get_subset_input_labelList,
                                  get_subset_input_typeList,
                                  get_subset_input_placeholderList,
                                  get_subset_input_jsList,
                                  get_subset_input_reqList)
    
    
    selectDicts     =   []
        
    dataframes      =   cfg.get_dfc_dataframes_select_list(cfg.SWDFSubsetUtility_ID)
    selectDicts.append(dataframes)
        
    current_df      =   cfg.get_current_chapter_df(cfg.SWDFSubsetUtility_ID)
    colnames        =   current_df.columns.tolist()
    cols_name_list  =   [" "]
    for i in range(len(colnames)) :
        cols_name_list.append(colnames[i])
            
    cnames          =   {"default":cols_name_list[0],"list": cols_name_list, "callback" : "change_subset_cols"}
    selectDicts.append(cnames)
        
    subssel         =   {"default":"Keep","list":["Keep","Drop"]}
    selectDicts.append(subssel)
        
    get_select_defaults(subset_input_form,
                        get_subset_input_form[0],
                        get_subset_input_form[1],
                        get_subset_input_form[3],
                        selectDicts)
        
    subset_input_form.set_shortForm(False)
    subset_input_form.set_gridwidth(680)
    subset_input_form.set_custombwidth(140)
    subset_input_form.set_fullparms(True)
        
    get_subset_input_html = subset_input_form.get_html() 
            
    get_subset_heading_html =   "<div>Get Dataframe Subset</div><br></br>"
    
    gridclasses     =   ["dfc-top","dfcleanser-common-grid-header","dfc-bottom"]
    gridhtmls       =   [col_stats_table,get_subset_heading_html,get_subset_input_html]
        
    print("\n")
    display_generic_grid("sw-utils-subset-wrapper",gridclasses,gridhtmls)



def display_df_criteria(df_title,df) :  
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
    
    col_stats_table     =   get_column_stats_table(df_title,df)
    
    from dfcleanser.common.html_widgets import InputForm
    subset_input_form = InputForm(get_subset_criteria_input_id,
                                  get_subset_criteria_input_idList,
                                  get_subset_criteria_input_labelList,
                                  get_subset_criteria_input_typeList,
                                  get_subset_criteria_input_placeholderList,
                                  get_subset_criteria_input_jsList,
                                  get_subset_criteria_input_reqList)
    
    subset_input_form.set_label_note({2:[dfchelp.SUBSET_CRITERIA,"dataframe subset criteria","subsetcriteriaimageid"]}) 
    
    subset_input_form.set_textarea_resize_flag(1,False)
    subset_input_form.set_textarea_resize_flag(3,False)  
    
    subset_input_form.set_shortForm(False)
    subset_input_form.set_gridwidth(620)
    subset_input_form.set_custombwidth(110)
    subset_input_form.set_fullparms(True)
    subset_input_form.set_custom_font_size("gsselectstring",14)   
    
    cfg.set_config_value(get_subset_criteria_input_id+"Parms",["",swsm.starting_criteria_preamble,swsm.starting_criteria,swsm.starting_criteria_postamble])
    cfg.set_config_value(get_subset_criteria_input_id+"ParmsProtect",[False,True,False,True])
        
    get_subset_input_html = subset_input_form.get_html() 
    
    get_subset_heading_html =   "<div>Get Dataframe Subset</div><br></br>"
        
    gridclasses     =   ["dfc-top","dfcleanser-common-grid-header","dfc-bottom"]
    gridhtmls       =   [col_stats_table,get_subset_heading_html,get_subset_input_html]
        
    print("\n")
    display_generic_grid("sw-utils-subset-wrapper",gridclasses,gridhtmls)


def get_df_stats_table(df_title,df,small=False) :
    """
    * -------------------------------------------------------------------------- 
    * function : get col stats for df columns
    * 
    * parms :
    *  df_title -   dataframe title
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    colstatsHeader        =   []
    colstatsRows          =   []
    colstatsWidths        =   [40,60]
    colstatsAligns        =   ["left","left"]
    
    columns     =   list(df.columns)
    
    colstatsRows.append(["Number Of Rows",str(len(df))])
    colstatsRows.append(["Number Of Columns",str(len(columns))])
    
    colstats_table        =   None
    
    colstats_table        =   dcTable("df Stats For dataframe '" + str(df_title) + "'",'dfcolstatsid',
                                      cfg.SWDFSubsetUtility_ID,
                                      colstatsHeader,colstatsRows,
                                      colstatsWidths,colstatsAligns)
            
    colstats_table.set_small(True)
    
    if(small) :
        colstats_table.set_smallwidth(50)
        colstats_table.set_smallmargin(260)
    else :
        colstats_table.set_smallwidth(50)
        colstats_table.set_smallmargin(160)
        
    colstats_table.set_checkLength(False)

    colstats_table.set_border(True)
    colstats_table.set_tabletype(ROW_MAJOR)
    colstats_table.set_rowspertable(50)
    colstatsHtml = get_row_major_table(colstats_table,SCROLL_DOWN,False)
    
    return(colstatsHtml+"<br>")




def display_process_subset() :  
    """
    * -------------------------------------------------------------------------- 
    * function : display current df subset form
    * 
    * parms :
    *  df      -   dataframe to subset from
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    current_step    =   swsm.get_current_subset_step()
    dftitle         =   current_step.get_output_subset_df_title()
    
    subset_df       =   swsm.get_current_subset_df()
    
    df_stats_table  =   get_df_stats_table(dftitle,subset_df)
    df_cols_table   =   get_column_stats_table(dftitle,subset_df)
    
    from dfcleanser.common.html_widgets import InputForm
    subset_input_form = InputForm(get_subset_run_input_id,
                                  get_subset_run_input_idList,
                                  get_subset_run_input_labelList,
                                  get_subset_run_input_typeList,
                                  get_subset_run_input_placeholderList,
                                  get_subset_run_input_jsList,
                                  get_subset_run_input_reqList)
    
    selectDicts     =   []
        
    colnames        =   subset_df.columns.tolist()
    cols_name_list  =   [" "]
    for i in range(len(colnames)) :
        cols_name_list.append(colnames[i])
            
    cnames          =   {"default":cols_name_list[0],"list": cols_name_list, "callback" : "change_run_subset_cols"}
    selectDicts.append(cnames)
        
    subssel         =   {"default":"Keep","list":["Keep","Drop"]}
    selectDicts.append(subssel)
    
    savesel         =   {"default":"True","list":["True","False"]}
    selectDicts.append(savesel)
    
    get_select_defaults(subset_input_form,
                        get_subset_run_input_form[0],
                        get_subset_run_input_form[1],
                        get_subset_run_input_form[3],
                        selectDicts)
    
    subset_input_form.set_shortForm(False)
    subset_input_form.set_gridwidth(680)
    subset_input_form.set_custombwidth(90)
    subset_input_form.set_fullparms(True)
    
    cfg.set_config_value(get_subset_run_input_id+"Parms",[dftitle,"","",""])
    cfg.set_config_value(get_subset_run_input_id+"ParmsProtect",[True,False,False,False])
        
    get_subset_input_html = subset_input_form.get_html() 
            
    get_subset_heading_html =   "<div>Process Dataframe Subset</div><br>"
        
    gridclasses     =   ["dfc-top","dfc-main","dfcleanser-common-grid-header","dfc-bottom"]
    gridhtmls       =   [df_stats_table,df_cols_table,get_subset_heading_html,get_subset_input_html]
        
    print("\n")
    display_generic_grid("sw-utils-subset-run-wrapper",gridclasses,gridhtmls)


def display_save_subset(df_title,df,auto=False) :  
    """
    * -------------------------------------------------------------------------- 
    * function : display current df subset form
    * 
    * parms :
    *  df      -   dataframe to subset from
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    df_stats_table  =   get_df_stats_table(df_title,df)
    df_cols_table   =   get_column_stats_table(df_title,df)
    
    from dfcleanser.common.html_widgets import InputForm
    subset_input_form = InputForm(get_subset_save_input_id,
                                  get_subset_save_input_idList,
                                  get_subset_save_input_labelList,
                                  get_subset_save_input_typeList,
                                  get_subset_save_input_placeholderList,
                                  get_subset_save_input_jsList,
                                  get_subset_save_input_reqList)
    
    
    subset_input_form.set_shortForm(False)
    subset_input_form.set_gridwidth(680)
    subset_input_form.set_custombwidth(140)
    subset_input_form.set_fullparms(True)
    
    cfg.set_config_value(get_subset_save_input_id+"Parms",[df_title,"./" + df_title + ".csv", df_title])
    
    if(auto) :
        cfg.set_config_value(get_subset_save_input_id+"ParmsProtect",[False,False,True])
    else :
        cfg.drop_config_value(get_subset_save_input_id+"ParmsProtect")
    
    get_subset_input_html = subset_input_form.get_html() 
            
    get_subset_heading_html =   "<div>Save Dataframe Subset</div><br>"
        
    gridclasses     =   ["dfc-top","dfc-main","dfcleanser-common-grid-header","dfc-bottom"]
    gridhtmls       =   [df_stats_table,df_cols_table,get_subset_heading_html,get_subset_input_html]
        
    print("\n")
    display_generic_grid("sw-utils-subset-run-wrapper",gridclasses,gridhtmls)



def display_saved_subset_sequences() :  
    """
    * -------------------------------------------------------------------------- 
    * function : display current saved sequences
    * 
    * parms :
    *  df      -   dataframe to subset from
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    from dfcleanser.common.html_widgets import InputForm
    subset_input_form = InputForm(get_subset_sequences_input_id,
                                  get_subset_sequences_input_idList,
                                  get_subset_sequences_input_labelList,
                                  get_subset_sequences_input_typeList,
                                  get_subset_sequences_input_placeholderList,
                                  get_subset_sequences_input_jsList,
                                  get_subset_sequences_input_reqList)
    
    selectDicts     =   []
        
    sequences       =   swsm.get_sequences_list()

    if(len(sequences) > 0) :           
        seqdict         =   {"default":sequences[0],"list": sequences}
    else :
        seqdict         =   {"default":"no saved sequences","list": ["no saved sequences"]}
        
        
    selectDicts.append(seqdict)
        
    subsetact       =   {"default":"Auto Run","list":["Auto Run","Manual Run"]}
    selectDicts.append(subsetact)
    
    
    get_select_defaults(subset_input_form,
                        get_subset_sequences_input_form[0],
                        get_subset_sequences_input_form[1],
                        get_subset_sequences_input_form[3],
                        selectDicts)
    
    subset_input_form.set_shortForm(False)
    subset_input_form.set_gridwidth(680)
    subset_input_form.set_custombwidth(140)
    subset_input_form.set_fullparms(True)
    
    get_subset_input_html = subset_input_form.get_html() 
            
    get_subset_heading_html =   "<div>Run Saved Subset Sequence</div><br>"
        
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
    gridhtmls       =   [get_subset_heading_html,get_subset_input_html]
        
    print("\n")
    display_generic_grid("sw-utils-subset-main-wrapper",gridclasses,gridhtmls)

    
    
def display_manual_df_subset_setup(sequence_title,input_df_title,colnames_list,cols_action,stepid) :  
    """
    * -------------------------------------------------------------------------- 
    * function : display current manual df subset form
    * 
    * parms :
    *  df      -   dataframe to subset from
    *  filters -   filters form 
    *  colname -   filters column name 
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    df           =   swsm.get_current_subset_df()
    col_stats_table     =   get_column_stats_table(input_df_title,df)
        
    from dfcleanser.common.html_widgets import InputForm
    subset_input_form = InputForm(get_manual_input_id,
                                  get_manual_input_idList,
                                  get_manual_input_labelList,
                                  get_manual_input_typeList,
                                  get_manual_input_placeholderList,
                                  get_manual_input_jsList,
                                  get_manual_input_reqList)
    
    selectDicts     =   []
        
    dataframes      =   {"default":input_df_title,"list":[input_df_title]}#cfg.get_dfc_dataframes_select_list(cfg.SWDFSubsetUtility_ID)
    
    selectDicts.append(dataframes)
        
    current_df      =   df#cfg.get_dfc_dataframe_df(input_df_title)
    colnames        =   current_df.columns.tolist()
    cols_name_list  =   [" "]
    for i in range(len(colnames)) :
        cols_name_list.append(colnames[i])
            
    cnames          =   {"default":cols_name_list[0],"list": cols_name_list, "callback" : "change_subset_cols"}
    selectDicts.append(cnames)
    
    if(cols_action == "Keep") :   
        subssel         =   {"default":"Keep","list":["Keep","Drop"]}
    else :
        subssel         =   {"default":"Drop","list":["Keep","Drop"]}
    selectDicts.append(subssel)
        
    get_select_defaults(subset_input_form,
                        get_manual_input_form[0],
                        get_manual_input_form[1],
                        get_manual_input_form[3],
                        selectDicts)
    
    if(len(colnames_list) > 0) :
        cnames  =   str(colnames_list)
    else :
        cnames  =   ""
        
    cfg.set_config_value(get_manual_input_id + "Parms",["",cnames,"",cols_action])
    cfg.set_config_value(get_manual_input_id + "ParmsProtect",[True,False,False,False])
        
    subset_input_form.set_shortForm(False)
    subset_input_form.set_gridwidth(680)
    subset_input_form.set_custombwidth(140)
    subset_input_form.set_fullparms(True)
        
    get_subset_input_html = subset_input_form.get_html() 
            
    get_subset_heading_html =   "<div>Run Subset Sequence '" + str(sequence_title) + "' Step " + str(stepid) + "</div><br></br>"
    
    gridclasses     =   ["dfc-top","dfcleanser-common-grid-header","dfc-bottom"]
    gridhtmls       =   [col_stats_table,get_subset_heading_html,get_subset_input_html]
        
    print("\n")
    display_generic_grid("sw-utils-subset-wrapper",gridclasses,gridhtmls)
    
    
def display_next_criteria(df_title,df,criteria,output_df_title) :  
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
    
    col_stats_table     =   get_column_stats_table(df_title,df)
    
    from dfcleanser.common.html_widgets import InputForm
    subset_input_form = InputForm(get_next_criteria_input_id,
                                  get_next_criteria_input_idList,
                                  get_next_criteria_input_labelList,
                                  get_subset_criteria_input_typeList,
                                  get_subset_criteria_input_placeholderList,
                                  get_next_criteria_input_jsList,
                                  get_subset_criteria_input_reqList)
    
    subset_input_form.set_label_note({2:[dfchelp.SUBSET_CRITERIA,"dataframe subset criteria","subsetcriteriaimageid"]}) 
    
    subset_input_form.set_textarea_resize_flag(1,False)
    subset_input_form.set_textarea_resize_flag(3,False)  
    
    subset_input_form.set_shortForm(False)
    subset_input_form.set_gridwidth(620)
    subset_input_form.set_custombwidth(110)
    subset_input_form.set_fullparms(True)
    subset_input_form.set_custom_font_size("gsnextselectstring",14)   
    
    cfg.set_config_value(get_next_criteria_input_id+"Parms",[output_df_title,swsm.starting_criteria_preamble,criteria,swsm.starting_criteria_postamble])
    cfg.set_config_value(get_next_criteria_input_id+"ParmsProtect",[False,True,False,True])
        
    get_subset_input_html = subset_input_form.get_html() 
    
    get_subset_heading_html =   "<div>Get Dataframe Subset</div><br></br>"
        
    gridclasses     =   ["dfc-top","dfcleanser-common-grid-header","dfc-bottom"]
    gridhtmls       =   [col_stats_table,get_subset_heading_html,get_subset_input_html]
        
    print("\n")
    display_generic_grid("sw-utils-subset-wrapper",gridclasses,gridhtmls)
    
    
def display_sequence_save_subset(df_title,df,auto=False) :  
    """
    * -------------------------------------------------------------------------- 
    * function : display current df subset run 
    * 
    * parms :
    *  df      -   dataframe to subset from
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    df_stats_table  =   get_df_stats_table(df_title,df)
    df_cols_table   =   get_column_stats_table(df_title,df)
    
    from dfcleanser.common.html_widgets import InputForm
    subset_input_form = InputForm(get_saved_save_input_id,
                                  get_saved_save_input_idList,
                                  get_saved_save_input_labelList,
                                  get_saved_save_input_typeList,
                                  get_saved_save_input_placeholderList,
                                  get_saved_save_input_jsList,
                                  get_saved_save_input_reqList)
    
    selectDicts     =   []
    
    dropsel         =   {"default":"False","list":["True","False"]}
    selectDicts.append(dropsel)
        
    get_select_defaults(subset_input_form,
                        get_saved_save_input_id,
                        get_saved_save_input_idList,
                        get_saved_save_input_typeList,
                        selectDicts)

    subset_input_form.set_shortForm(False)
    subset_input_form.set_gridwidth(680)
    subset_input_form.set_custombwidth(140)
    subset_input_form.set_fullparms(True)
    
    cfg.set_config_value(get_saved_save_input_id+"Parms",[df_title,"./" + df_title + ".csv", df_title,"False"])
    cfg.drop_config_value(get_saved_save_input_id+"ParmsProtect")
    
    get_subset_input_html = subset_input_form.get_html() 
            
    get_subset_heading_html =   "<div>Save Dataframe Subset</div><br>"
        
    gridclasses     =   ["dfc-top","dfc-main","dfcleanser-common-grid-header","dfc-bottom"]
    gridhtmls       =   [df_stats_table,df_cols_table,get_subset_heading_html,get_subset_input_html]
        
    print("\n")
    display_generic_grid("sw-utils-subset-run-wrapper",gridclasses,gridhtmls)
    
    
    
    
    
    