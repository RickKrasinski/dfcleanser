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

from dfcleanser.common.html_widgets import (get_button_tb_form, display_composite_form, ButtonGroupForm)

from dfcleanser.common.common_utils import (get_parms_for_input)


"""
#--------------------------------------------------------------------------
#    dfconcat main task bar
#--------------------------------------------------------------------------
"""
dfconcat_tb_doc_title               =   "Dataframe Concat"
dfconcat_tb_title                   =   "Dataframe Concat"
dfconcat_tb_id                      =   "dfconcat"

dfconcat_tb_keyTitleList            =   ["Simple Dataframe</br> Concatenation",
                                         "Full Dataframe</br> Concatenation",
                                         "Clear","Help"]

dfconcat_tb_jsList                  =   ["process_concat_callback("+str(dfcm.DISPLAY_SIMPLE_CONCAT)+")",
                                         "process_concat_callback("+str(dfcm.DISPLAY_FULL_CONCAT)+")",
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
df_concat_input_idList                  =   ["dflist",
                                             "caxis",
                                             "cjoin",
                                             "cresult",
                                             "cresrow",
                                             None,None,None,None,None]

df_concat_input_labelList              =   ["dataframes_to_concatenate",
                                             "axis_to_concatenate_over",
                                             "join_value",
                                             "dataframe_to_store_result_in",
                                             "reset_row_index_flag",
                                             "Concat</br>Dataframes",
                                             "Clear",
                                             "Return",
                                             "Pandas</br>Help","Help"]

df_concat_input_typeList                =   ["text","text","text","text","text",
                                             "button","button","button","button","button"]

df_concat_input_placeholderList         =   ["dataframes to concatenate",
                                             "axis to concatenate ( 0-rows : 1-columns default eows )",
                                             "('inner' or 'outer' default : 'outer')",
                                             "dataframe to store concatentaion result in",
                                             "reset row index after concatentaion (default : False)",
                                             None,None,None,None,None]

df_concat_input_jsList                  =   [None,None,None,None,None,
                                             "process_concat_callback(" + str(dfcm.PROCESS_SIMPLE_CONCAT) + ")",
                                             "process_concat_callback(" + str(dfcm.DISPLAY_SIMPLE_CONCAT) + ")",
                                             "process_concat_callback(" + str(dfcm.DISPLAY_MAIN) + ")",
                                             "display_help_url(" + "'" + concat_help_url + "'" + ")",
                                             "displayhelp(" + str(dfchelp.DFCONCAT_SIMPLE_INPUT_ID) + ")"]

df_concat_input_reqList                 =   [0,1,2,3,4]


"""
#--------------------------------------------------------------------------
#   dataframe full concat input 
#--------------------------------------------------------------------------
"""
fconcat_help_url                         =   "https://pandas.pydata.org/pandas-docs/stable/generated/pandas.concat.html"

df_fconcat_input_title                   =   "dataframe Concat Parameters"
df_fconcat_input_id                      =   "fconcatinput"
df_fconcat_input_idList                  =   ["dflist",
                                             "caxis",
                                             "cjoin",
                                             "cjoinaxis",
                                             "cignore",
                                             "ckeys",
                                             "clevelss",
                                             "cvintergrity",
                                             "csort",
                                             "ccopy",
                                             "dfname",
                                             "scriptflag",
                                             None,None,None,None,None]

df_fconcat_input_labelList              =   ["objs",
                                             "axis",
                                             "join",
                                             "join_axes",
                                             "ignore_index",
                                             "keys",
                                             "levels",
                                             "names",
                                             "verify_integrity",
                                             "sort",
                                             "copy",
                                             "resultant_df_name",
                                             "add_to_script",
                                             "Concat</br>Dataframes",
                                             "Clear",
                                             "Return",
                                             "Help"]

df_fconcat_input_typeList                =   ["text","text","text","text","text","text",
                                              "text","text","text","text","text","text","text",
                                             "button","button","button","button"]

df_fconcat_input_placeholderList         =   ["a sequence or mapping of Series, DataFrame, or Panel objects",
                                             "{0/’index’, 1/’columns’}, default 0",
                                             " {‘inner’, ‘outer’}, default ‘outer’",
                                             "list of Index objects",
                                             "boolean, default False",
                                             "sequence, default None",
                                             "list of sequences, default None",
                                             "list, default None",
                                             "boolean, default False",
                                             "boolean, default None",
                                             "boolean, default True",
                                             "resultant df name, default 'full_Concat'",
                                             "store call in script log, default False",
                                             None,None,None,None]

df_fconcat_input_jsList                  =   [None,None,None,None,None,None,None,
                                              None,None,None,None,None,None,
                                             "process_concat_callback(" + str(dfcm.PROCESS_FULL_CONCAT) + ")",
                                             "process_concat_callback(" + str(dfcm.DISPLAY_FULL_CONCAT) + ")",
                                             "process_concat_callback(" + str(dfcm.DISPLAY_MAIN) + ")",
                                             "display_help_url(" + "'" + fconcat_help_url + "'" + ")"]

df_fconcat_input_reqList                 =   [0]








"""
#--------------------------------------------------------------------------
#    concat example button
#--------------------------------------------------------------------------
"""
df_concat_example_tb_doc_title          =   ""
df_concat_example_tb_title              =   ""
df_concat_example_tb_id                 =   "concatexampletb"

df_concat_example_tb_keyTitleList       =   ["Show Concatenation Example"]

df_concat_example_tb_jsList             =   ["displayhelp(" + str(dfchelp.TRANSFORM_MAIN_TASKBAR_ID) + ")"]

df_concat_example_tb_centered           =   True

    
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

def get_full_concat_input_parms(parms) :
   return(get_parms_for_input(parms,df_fconcat_input_idList))

def display_simple_concat() :

    from dfcleanser.common.html_widgets import InputForm, get_input_form
    concat_input_form = get_input_form(InputForm(df_concat_input_id,
                                                 df_concat_input_idList,
                                                 df_concat_input_labelList,
                                                 df_concat_input_typeList,
                                                 df_concat_input_placeholderList,
                                                 df_concat_input_jsList,
                                                 df_concat_input_reqList),
                                       df_concat_input_title) 

    display_composite_form([concat_input_form])

def display_full_concat() :

    from dfcleanser.common.html_widgets import InputForm, get_input_form
    fconcat_input_form = get_input_form(InputForm(df_fconcat_input_id,
                                                  df_fconcat_input_idList,
                                                  df_fconcat_input_labelList,
                                                  df_fconcat_input_typeList,
                                                  df_fconcat_input_placeholderList,
                                                  df_fconcat_input_jsList,
                                                  df_fconcat_input_reqList),
                                       df_fconcat_input_title) 

    display_composite_form([fconcat_input_form])

        




