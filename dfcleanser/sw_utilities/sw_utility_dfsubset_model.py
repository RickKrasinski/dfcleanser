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

import dfcleanser.sw_utilities.sw_utility_dfsubset_widgets as swdfw

dfsubset_inputs             =   [swdfw.get_subset_input_id,swdfw.get_subset_filter_input_id,swdfw.get_subset_filters_id]
