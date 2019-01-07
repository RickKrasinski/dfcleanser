"""
# sw_utility_dfconcat_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""

import sys
this = sys.modules[__name__]

import dfcleanser.common.help_utils as dfchelp
import dfcleanser.sw_utilities.sw_utility_dfconcat_model as dfcm

from dfcleanser.common.html_widgets import (get_button_tb_form, display_composite_form, 
                                            ButtonGroupForm, maketextarea)

from dfcleanser.common.common_utils import (get_parms_for_input, display_generic_grid)

import dfcleanser.common.cfg as cfg


"""
#--------------------------------------------------------------------------
#    dfconcat main task bar
#--------------------------------------------------------------------------
"""
dfconcat_tb_doc_title               =   "Dataframe Concat"
dfconcat_tb_title                   =   "Dataframe Concat"
dfconcat_tb_id                      =   "dfconcat"

dfconcat_tb_keyTitleList            =   ["Simple Dataframe</br> Concatenation",
                                         "Clear","Help"]

dfconcat_tb_jsList                  =   ["process_concat_callback("+str(dfcm.DISPLAY_SIMPLE_CONCAT)+")",
                                         "process_concat_callback("+str(dfcm.DISPLAY_MAIN)+")",
                                         "displayhelp(" + str(dfchelp.DFCONCAT_MAIN_TASKBAR_ID) + ")"]

dfconcat_tb_centered                =   False

"""
#--------------------------------------------------------------------------
#   df concat input 
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   dataframe simple concat input 
#--------------------------------------------------------------------------
"""
concat_help_url                         =   "https://pandas.pydata.org/pandas-docs/stable/generated/pandas.concat.html"

df_concat_input_title                   =   "dataframe Concat Parameters"
df_concat_input_id                      =   "concatinput"
df_concat_input_idList                  =   ["dftoconcatto",
                                             "caxis",
                                             "cjoin",
                                             "cresrow",
                                             None,None,None,None]

df_concat_input_labelList              =   ["dataframe_to_save_to",
                                             "axis_to_concatenate_over",
                                             "join_value",
                                             "reset_row_index_flag",
                                             "Concat</br>dfs",
                                             "Clear",
                                             "Return",
                                             "Help"]

df_concat_input_typeList                =   ["text","select","select","select",
                                             "button","button","button","button"]

df_concat_input_placeholderList         =   ["dataframe to save concatentation to",
                                             "axis to concatenate ( 0-rows : 1-columns default eows )",
                                             "('inner' or 'outer' default : 'outer')",
                                             "reset row index after concatentaion (default : False)",
                                             None,None,None,None]

df_concat_input_jsList                  =   [None,None,None,None,None,
                                             "process_concat_callback(" + str(dfcm.PROCESS_SIMPLE_CONCAT) + ")",
                                             "process_concat_callback(" + str(dfcm.DISPLAY_SIMPLE_CONCAT) + ")",
                                             "process_concat_callback(" + str(dfcm.DISPLAY_MAIN) + ")",
                                             "displayhelp(" + str(dfchelp.DFCONCAT_SIMPLE_INPUT_ID) + ")"]

df_concat_input_reqList                 =   [0,1,2,3]



"""
#--------------------------------------------------------------------------
#    dataframe select inputs
#--------------------------------------------------------------------------
"""
df_concat_df1_input_title           =   "Dataframes Manager"
df_concat_df1_input_id              =   "df1toconcat"
df_concat_df1_input_idList          =   ["dataframe1title",
                                         "df1numrows",
                                         "df1numcols",
                                         "df1diffcols",
                                         None]

df_concat_df1_input_labelList       =   ["df1_title",
                                         "num_rows",
                                         "num_cols",
                                         "cols_not_in_df2",
                                         "Save Result To"]

df_concat_df1_input_typeList        =   ["select","text","text",maketextarea(4),"button"]

df_concat_df1_input_placeholderList =   ["dataframe title",
                                         "number of rows",
                                         "number of columns",
                                         "df1 columns not in df2",
                                         None]

df_concat_df1_input_jsList          =   [None,None,None,None,
                                         "set_concat_direction('df1')"]

df_concat_df1_input_reqList         =   [0]

df_concat_df1_input_form            =   [df_concat_df1_input_id,
                                         df_concat_df1_input_idList,
                                         df_concat_df1_input_labelList,
                                         df_concat_df1_input_typeList,
                                         df_concat_df1_input_placeholderList,
                                         df_concat_df1_input_jsList,
                                         df_concat_df1_input_reqList]  



df_concat_df2_input_id             =   "df2toconcat"
df_concat_df2_input_idList         =   ["dataframe2title",
                                        "df2numrows",
                                        "df2numcols",
                                        "df2diffcols",
                                        None]

df_concat_df2_input_labelList        = ["df2_title",
                                        "num_rows",
                                        "num_cols",
                                        "cols_not_in_df1",
                                        "Save Result To"]

df_concat_df2_input_placeholderList =   ["dataframe title",
                                         "number of rows",
                                         "number of columns",
                                         "df2 columns not in df1",
                                         None]

df_concat_df2_input_jsList         =   [None,None,None,None,
                                        "set_concat_direction('df2')"]

df_concat_df2_input_form            =  [df_concat_df2_input_id,
                                        df_concat_df2_input_idList,
                                        df_concat_df2_input_labelList,
                                        df_concat_df1_input_typeList,
                                        df_concat_df2_input_placeholderList,
                                        df_concat_df2_input_jsList,
                                        df_concat_df1_input_reqList]  

    
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   display functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_concat_main_taskbar() :
    display_composite_form([get_button_tb_form(ButtonGroupForm(dfconcat_tb_id,
                                                               dfconcat_tb_keyTitleList,
                                                               dfconcat_tb_jsList,
                                                               dfconcat_tb_centered))])

def get_simple_concat_input_parms(parms) :
   return(get_parms_for_input(parms,df_concat_input_idList))

def get_simple_concat_input_df_parms(parms) :
    
    dfparms     =   []
    dfparms.append(get_parms_for_input(parms[0],df_concat_df1_input_idList))
    dfparms.append(get_parms_for_input(parms[0],df_concat_df2_input_idList))
    
    return(dfparms)
    

def display_simple_concat_grid() :

    """
    * -------------------------------------------------------- 
    * function : display simple concatenation grid
    * 
    * parms :
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    df_concat_heading_html  =   "<p>&nbsp;Simple Dataframes Concatenation</p>"

    df1_concat_input_html = ""
    
    from dfcleanser.common.html_widgets import InputForm
    df1_concat_input_form   =   InputForm(df_concat_df1_input_form[0],df_concat_df1_input_form[1],
                                          df_concat_df1_input_form[2],df_concat_df1_input_form[3],
                                          df_concat_df1_input_form[4],df_concat_df1_input_form[5],
                                          df_concat_df1_input_form[6])
        
    df1_concat_input_form.set_gridwidth(240)
    df1_concat_input_form.set_custombwidth(160)
    
    df1_select_dict     =   cfg.get_dfc_dataframes_select_list()
    df1_select_dict.update({"default":""})
    df1_select_dict.update({"callback":"select_concat_df"})
    df1_option_list     =   df1_select_dict.get("list",None)
    df1_option_list.append("")
    df1_select_dict.update({"list":df1_option_list})

    df1_concat_input_form.add_select_dict("dataframe1title",df1_select_dict)
     
    df1_concat_input_html = df1_concat_input_form.get_html() 

    df2_concat_input_html = ""
    
    from dfcleanser.common.html_widgets import InputForm
    df2_concat_input_form   =   InputForm(df_concat_df2_input_form[0],df_concat_df2_input_form[1],
                                          df_concat_df2_input_form[2],df_concat_df2_input_form[3],
                                          df_concat_df2_input_form[4],df_concat_df2_input_form[5],
                                          df_concat_df2_input_form[6])
        
    df2_concat_input_form.set_gridwidth(240)
    df2_concat_input_form.set_custombwidth(160)
    
    df2_select_dict     =   cfg.get_dfc_dataframes_select_list()
    df2_select_dict.update({"default":""})
    df2_select_dict.update({"callback":"select_concat_df"})
    df2_option_list     =   df2_select_dict.get("list",None)
    df2_option_list.append("")
    df2_select_dict.update({"list":df2_option_list})

    df2_concat_input_form.add_select_dict("dataframe2title",df2_select_dict)
    
    df2_concat_input_html = df2_concat_input_form.get_html() 
    
    from dfcleanser.common.html_widgets import InputForm
    concat_input_form = InputForm(df_concat_input_id,
                                  df_concat_input_idList,
                                  df_concat_input_labelList,
                                  df_concat_input_typeList,
                                  df_concat_input_placeholderList,
                                  df_concat_input_jsList,
                                  df_concat_input_reqList) 
    
    concat_input_form.set_custombwidth(75)
    concat_input_form.set_gridwidth(320)
    
    axissel           =   {"default":"0","list":["0","1"]}
    concat_input_form.add_select_dict("caxis",axissel)
    
    joinsel           =   {"default":"outer","list":["inner","outer"]}
    concat_input_form.add_select_dict("cjoin",joinsel)
    
    resisel           =   {"default":"False","list":["True","False"]}
    concat_input_form.add_select_dict("cresrow",resisel)
   
    concat_input_html   =   concat_input_form.get_html()
    
    gridclasses     =   ["df-concat-header","dfc-left","dfc-main","dfc-right"]
    gridhtmls       =   [df_concat_heading_html,df1_concat_input_html,
                         df2_concat_input_html,concat_input_html]
    
    display_generic_grid("df-concat-wrapper",gridclasses,gridhtmls)


def display_simple_concat() :
    
    display_simple_concat_grid()
    


        




