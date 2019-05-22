"""
# sw_utility_genfunc_widgets
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    generic functions components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

DISPLAY_GENERIC_FUNCTION_TB         =   0
DISPLAY_GENERIC_FUNCTION            =   1
PROCESS_GENERIC_FUNCTION_OPTION     =   2

LOAD_FUNCTION                       =   0
SAVE_FUNCTION                       =   1
UPDATE_FUNCTION                     =   2
DISPLAY_FUNCTION                    =   3
DELETE_FUNCTION                     =   4
RETURN_FUNCTION                     =   5
SELECT_FUNCTION                     =   6
CLEAR_FUNCTION                      =   7

FOR_ADD_COLUMNS                     =   0
FOR_APPLY_FN                        =   1
FOR_GEN_FUNC                        =   2

reservedfunctions                   =   ["to_int_df_column","to_float_df_column","to_string_df_column","upperCase_df_column",
                                         "normalize_df_column","normalize_list","get_trig_values_for_column",
                                         "get_trigonometric_values","convert_df_column_to_degrees_or_radians",
                                         "convert_to_degrees_or_radians","absolute_df_column",
                                         "absolute_values","round_df_col_float","get_df_geocode_center",
                                         "get_geocode_center"]

reservedfunctionsmodule             =    "dfcleanser.sw_utilities.sw_utility_genfunc_functions"


Red     = "#FAA78F"
Green   = "#8FFAC0"
Yellow  = "#FAFB95"



