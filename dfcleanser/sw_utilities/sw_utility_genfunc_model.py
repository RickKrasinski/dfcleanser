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
DELETE_FUNCTION                     =   2
CLEAR_FUNCTION                      =   3
RETURN_FUNCTION                     =   4
SELECT_FUNCTION                     =   5

FOR_ADD_COLUMNS                     =   0
FOR_APPLY_FN                        =   1
FOR_GEN_FUNC                        =   2

reservedfunctions                   =   ["normalize_column","add_normalized_column","upperCase_column",
                                         "get_normalized_column_values","get_trigonometric_column_values",
                                         "convert_to_degrees","convert_to_radians","absolute_column",
                                         "round_float","round_to_int"]

Red     = "#FAA78F"
Green   = "#8FFAC0"
Yellow  = "#FAFB95"

"""
numpy.exp
log

square
sqrt

DataFrame[colname].values
Return a Numpy representation of the DataFrame

nparray to df column
df= DataFrame(test)
df['preds']=preds
"""















