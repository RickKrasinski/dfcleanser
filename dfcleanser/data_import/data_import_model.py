"""
# data_import_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Sept 13 22:29:22 2018

@author: Rick
"""
import sys
this = sys.modules[__name__]

"""
#--------------------------------------------------------------------------
#   pandas import ids
#--------------------------------------------------------------------------
"""
CSV_IMPORT              =   0
FWF_IMPORT              =   1
EXCEL_IMPORT            =   2
JSON_IMPORT             =   3
HTML_IMPORT             =   4
SQLTABLE_IMPORT         =   5
SQLQUERY_IMPORT         =   6

CUSTOM_IMPORT           =   7
PROCESS_CUSTOM_IMPORT   =   8
CLEAR_CUSTOM_IMPORT     =   9
RETURN_CUSTOM_IMPORT    =   10

DISPLAY_COLUMN_NAMES        =   15
DISPLAY_DATETIME_FORMATS    =   16
DISPLAY_INDEX_NAMES         =   17

CLEAR_CSV_IMPORT                =   20
CLEAR_FWF_IMPORT                =   21
CLEAR_EXCEL_IMPORT              =   22
CLEAR_JSON_IMPORT               =   23
CLEAR_HTML_IMPORT               =   24
CLEAR_SQLTABLE_IMPORT           =   25
CLEAR_SQLTABLE_CUSTOM_IMPORT    =   26
CLEAR_SQLQUERY_IMPORT           =   27

DISPLAY_HTML_IMPORT_DF          =   30
SAVE_HTML_IMPORT_DF             =   31
RETURN_HTML_IMPORT_DFS          =   32



"""
#--------------------------------------------------------------------------
#   import option ids
#--------------------------------------------------------------------------
"""
IMPORT_TB_ONLY                          =   0
IMPORT_PANDAS_TB_ONLY                   =   1
IMPORT_PANDAS_TB_PLUS_DETAILS           =   2
IMPORT_CUSTOM_ONLY                      =   3

"""
#------------------------------------------------------------------
#   sql input table identifiers 
#------------------------------------------------------------------
"""
DBLIBS              =   0
TABLE_NAMES         =   1
COLUMN_NAMES        =   2
DATETIME_FORMATS    =   3
INDEX_NAMES         =   4

SQL_CUSTOM      =   0
SQL_COMMON      =   1


"""
* ----------------------------------------------------
# html import df list
* ----------------------------------------------------
""" 

     
def set_dfs_list(dfs_list) :
    dfsList.set_dfs_list(dfs_list)

def get_dfs_list() :   
    return(dfsList.get_dfs_list())

def clear_dfs_list() :   
    dfsList.drop_dfs_list()

def get_current_df_id() :   
    return(dfsList.get_df_id())

def set_current_df_id(dfid) :   
    dfsList.set_df_id(dfid)

def get_current_df_url() :   
    return(dfsList.get_df_url())

def set_current_df_url(url) :   
    dfsList.set_df_url(url)

class dfs_list :
    
    # instance variables
    dfs_list        =   None
    df_id           =   None
    df_url          =   None
    
    # full constructor
    def __init__(self) :
        self.dfs_list        =   None
        self.df_id           =   None
        self.df_url          =   None
        
    def set_dfs_list(self,dfslist) :
        self.dfs_list  =   dfslist

    def get_dfs_list(self) :
        return(self.dfs_list)
        
    def set_df_id(self,dfid) :
        self.df_id  =   dfid

    def get_df_id(self) :
        return(self.df_id)
        
    def set_df_url(self,dfurl) :
        self.df_url  =   dfurl

    def get_df_url(self) :
        return(self.df_url)
        
    def drop_dfs_list(self) :
        self.dfs_list   =   None
        self.df_id      =   None
        self.df_url     =   None

dfsList     =   dfs_list() 

