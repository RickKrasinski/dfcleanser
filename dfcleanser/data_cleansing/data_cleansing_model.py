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

PROCESS_DROPNA_ROWS_OPTION  =   5

DROP_COL_OPTION             =   6
DROP_ROWS_OPTION            =   7

DISPLAY_FILLNA_OPTION       =   8
PROCESS_FILLNA_OPTION       =   9

DISPLAY_DROPNA_OPTION       =   19
PROCESS_DROPNA_OPTION       =   20

DISPLAY_DATA_TYPE_OPTION    =   10
PROCESS_DATA_TYPE_OPTION    =   11

GENERIC_COLUMN_OPTION       =   12

DISPLAY_ROUND_COLUMN_OPTION =   13
PROCESS_ROUND_COLUMN_OPTION =   14

DISPLAY_COL_CHANGE_OPTION   =   15

DISPLAY_REM_WHTSPC_OPTION   =   16
PROCESS_REM_WHTSPC_OPTION   =   17

DROP_COL_NANS_OPTION        =   18

FIND_COLUMN_OPTION          =   21
DISPLAY_DETAILS_OPTION      =   22

DISPLAY_NEW_ROW             =   23
UPDATE_ROW_COL              =   24
PROCESS_ROW_COL             =   25

DATATYPE_OPTION             =   27

DISPLAY_UNIQUES_OPTION      =   29

DISPLAY_ALPHANUMERIC_CHECK  =   30
PROCESS_ALPHANUMERIC_CHECK  =   31

DISPLAY_NUMERIC_CHECK       =   32
PROCESS_NUMERIC_CHECK       =   33

DISPLAY_ADD_CATEGORY                =   35
DISPLAY_REMOVE_CATEGORY             =   36
DISPLAY_REMOVE_CATEGORY_WHITESPACE  =   37
DISPLAY_REORDER_CATEGORY            =   38




DISPLAY_CLEANSE_NUMERIC_COLUMNS         =   0
DISPLAY_CLEANSE_NON_NUMERIC_COLUMNS     =   1
DISPLAY_CLEANSE_ROW                     =   2
DISPLAY_CLEANSE_CLEAR                   =   3



PROCESS_RENAME_CATEGORY             =   40
PROCESS_ADD_CATEGORY                =   41
PROCESS_REMOVE_CATEGORY             =   42
PROCESS_REMOVE_UNUSED_CATEGORY      =   43
PROCESS_REMOVE_CATEGORY_WHITESPACE  =   44
PROCESS_REORDER_CATEGORY            =   45
PROCESS_TOGGLE_CATEGORY_ORDER       =   46

CLEANSE_CURRENT_CATEGORY_COLUMN     =   47


PROCESS_GET_ROW_BY_ID               =   50
PROCESS_GET_ROW_BY_INDEX            =   51

DISPLAY_SELECT_ROW_ID               =   55
PROCESS_SELECT_ROW_ID               =   56



CHANGE_ROW_VALUES                   =   0
CHANGE_ROW                          =   1
DROP_ROW                            =   2



whitespace_chars            =   ["\\t","\\n","\\f","\\r","\\b","\\v"]
whitespace_chars_text       =   ["&nbsp;Horizontal Tab","&nbsp;Linefeed","&nbsp;Formfeed","&nbsp;Cariage Return","&nbsp;Backspace","&nbsp;Vertical Tab"]
whitespace_chars_ids        =   ["HTab","Lfeed","Ffeed","CReturn","Bspace","VTab"]

DROP_NA_OPTION              =   0
FILL_NA_OPTION              =   1
NO_NA_OPTION                =   2



"""
* ----------------------------------------------------
# data cleansing check compatability 
* ----------------------------------------------------
""" 

ALPHANUMERIC    =   0
NUMERIC         =   1
     
def set_compatability_status(ctype,colname,status) :
    check_compatability_dict.set_status(ctype,colname,status)

def get_compatability_status(ctype,colname) :   
    return(check_compatability_dict.get_status(ctype,colname))

def clear_compatability_status() :   
    check_compatability_dict.clear_store()

class check_compatability_store :
    
    # instance variables
    alphanumeric_dict   =   {}
    numeric_dict        =   {}
    
    # full constructor
    def __init__(self) :
        self.alphanumeric_dict  =   {}
        self.numeric_dict       =   {}
        
    def set_status(self,ctype,colname,status) :
        
        if(ctype == ALPHANUMERIC) :
            self.alphanumeric_dict.update({colname:status}) 
        else :
            self.numeric_dict.update({colname:status}) 

    def get_status(self,ctype,colname) :
        
        if(ctype == ALPHANUMERIC) :
            self.alphanumeric_dict.get(colname,None) 
        else :
            self.numeric_dict.get(colname,None) 
            
    def clear_store(self) :
        self.alphanumeric_dict  =   {}
        self.numeric_dict       =   {}
   

check_compatability_dict     =   check_compatability_store()  







