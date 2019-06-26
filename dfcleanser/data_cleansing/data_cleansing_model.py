"""
# data_cleansing_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    data cleansing option ids
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

DFS_CLEANSE_COL             =   -1


UNIQUES_FLAG                =   0
OUTLIERS_FLAG               =   1
DATA_TYPES_FLAG             =   2

DROP_OBJ_COLUMNS            =   0
DROP_OBJ_NAN_ROWS           =   1
TRANSFORM_OBJ_COLUMNS       =   2
REMOVE_COLS_WHITESPACE      =   3 

ROUND_OBJ_COLUMNS           =   1
CH_DATATYPES_OBJ_COLUMNS    =   2

"""
*
*-----------------------------------------------------------
* processing function ids
*-----------------------------------------------------------
*
"""
MAIN_OPTION                 =   0

CHANGE_COLUMN_OPTION        =   1

DISPLAY_COLS_OPTION         =   2
DISPLAY_ROW_OPTION          =   3

DISPLAY_DROP_NA_OPTION      =   4
PROCESS_DROP_NA_OPTION      =   5

DROP_COL_OPTION             =   6
DROP_ROWS_OPTION            =   7

DISPLAY_FILLNA_OPTION       =   8
PROCESS_FILLNA_OPTION       =   9

DISPLAY_DATA_TYPE_OPTION    =   10
PROCESS_DATA_TYPE_OPTION    =   11

GENERIC_COL_OPTION          =   12

DISPLAY_ROUND_COLUMN_OPTION =   13
PROCESS_ROUND_COLUMN_OPTION =   14

DISPLAY_COL_CHANGE_OPTION   =   15

DISPLAY_REM_WHTSPC_OPTION   =   16
PROCESS_REM_WHTSPC_OPTION   =   17

DROP_COL_NANS_OPTION        =   18

DISPLAY_GRAPHS_OPTION       =   19
DISPLAY_OUTLIERS_OPTION     =   20

FIND_COLUMN_OPTION          =   21
DISPLAY_UNIQUES_OPTION      =   22

DISPLAY_NEW_ROW             =   23
UPDATE_ROW_COL              =   24
PROCESS_ROW_COL             =   25

DATATYPE_OPTION             =   27

CHANGE_NA_OPTION            =   28

whitespace_chars            =   ["\\t","\\n","\\f","\\r","\\b","\\v"]
whitespace_chars_text       =   ["&nbsp;Horizontal Tab","&nbsp;Linefeed","&nbsp;Formfeed","&nbsp;Cariage Return","&nbsp;Backspace","&nbsp;Vertical Tab"]
whitespace_chars_ids        =   ["HTab","Lfeed","Ffeed","CReturn","Bspace","VTab"]


