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

NEW_FUNCTION                        =   0
GET_FUNCTION                        =   1
SAVE_FUNCTION                       =   2
DELETE_FUNCTION                     =   3
RUN_FUNCTION                        =   4
CLEAR_FUNCTION                      =   5
RETURN_FUNCTION                     =   6

FOR_ADD_COLUMNS                     =   0
FOR_APPLY_FN                        =   1
FOR_GEN_FUNC                        =   2

reservedfunctions                   =   ["normalize_column","add_normalized_column","upperCase_column",
                                         "a_to_int_column","a_to_long_column","to_string_column"]    

