"""
# data_inspection_widgets 
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
#    data inspection option ids
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
MAIN_OPTION                 =   0
DISPLAY_DATATYPES_OPTION    =   1
DISPLAY_NANS_OPTION         =   2
DISPLAY_ROWS_OPTION         =   3
DISPLAY_COLS_OPTION         =   4
DISPLAY_CATEGORIES_OPTION   =   5

DROP_ROW_NANS_OPTION        =   6
DROP_COL_NANS_OPTION        =   7

DISPLAY_ROW_OPTION          =   8


OPEN_EXCEL_OPTION           =   9
DISPLAY_FULL_COLUMN_NAMES   =   10

MATCH_VALS_OPTION           =   11

DISPLAY_COL_GRAPHS          =   12
DISPLAY_COL_OUTLIERS        =   13

CLEANSE_COLUMN              =   14

BY_PERCENT      =   0
BY_COUNT        =   1


"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   column datatypes objects
#------------------------------------------------------------------
#------------------------------------------------------------------
"""

def get_df_datatypes_data(df) : 
    """            
    #------------------------------------------------------------------
    #   get datatype info for a dataframe
    #
    #   df              -   dataframe
    #
    #   return : list of [[unique data types],
    #                     [column count for each datatype],
    #                     {dict of col names list for each unique datatype}]
    #
    #------------------------------------------------------------------
    """

    df_cols     = df.columns
    df_dtypes   = df.dtypes.tolist()
    
    dtypes_dict         = {}
    dtypes_list         = []
    dtypes_counts_list  = []
    
    col_stats   =   col_dts()
    
    for i in range(len(df_dtypes)) :
        col_stats.add_column(df_dtypes[i],df_cols[i])
    
    dtypes_list          =  col_stats.get_dtype_list() 
    
    for i in range(len(dtypes_list)) :
        dtypes_counts_list.append(col_stats.get_dtype_count(dtypes_list[i]))
        
    for i in range(len(dtypes_list)) :
        dtypes_dict.update({dtypes_list[i]:col_stats.get_dtype_col_list(dtypes_list[i])})
        
    return([dtypes_list, dtypes_counts_list, dtypes_dict])


"""
#------------------------------------------------------------------
#   column datatype 
#------------------------------------------------------------------
""" 

class col_dt_stats :
   
    # full constructor
    def __init__(self,dt) :
        
        # minimum init attributes
        self.count      =   1
        self.col_list   =   []
        
    def add_to_count(self) :
        self.count      =   self.count + 1
        
    def add_colname(self,cname) :
        self.col_list.append(cname)

    def get_count(self) :
        return(self.count)
        
    def get_colnames(self) :
        return(self.col_list)


"""
#------------------------------------------------------------------
#   column datatype list 
#------------------------------------------------------------------
""" 

class col_dts :
   
    # full constructor
    def __init__(self) :
        
        # minimum init attributes
        self.statusdict     =   {}
        
    def add_column(self,dtype,colname) :
        
        dtype_stats     =   self.statusdict.get(dtype)
        if(dtype_stats is None) :
            dt_stats    =   col_dt_stats(dtype)
            dt_stats.add_colname(colname)
            self.statusdict.update({dtype:dt_stats})
        else :
            dtype_stats.add_to_count()
            dtype_stats.add_colname(colname)
            self.statusdict.update({dtype:dtype_stats})

    def get_dtype_count(self,dt) :
        dtype_stats     =   self.statusdict.get(dt) 
        if(dtype_stats is None) :
            return(0)
        else :
            return(dtype_stats.get_count())
            
    def get_dtype_col_list(self,dt) :
        dtype_stats     =   self.statusdict.get(dt) 
        if(dtype_stats is None) :
            return(None)
        else :
            return(dtype_stats.get_colnames())
    
    def get_dtype_list(self) :
        return(list(self.statusdict.keys()))



