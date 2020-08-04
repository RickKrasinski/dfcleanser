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

DISPLAY_COL_GRAPHS          =   12
DISPLAY_COL_OUTLIERS        =   13

CLEANSE_COLUMN              =   14

GET_SUBSET_OPTION           =   15

DISPLAY_SCROLL_TO_DF_ROW    =   16
PROCESS_SCROLL_TO_DF_ROW    =   17

SCROLL_DF_ROWS_DOWN         =   18
SCROLL_DF_ROWS_UP           =   19

DISPLAY_DF_ROW              =   20

DISPLAY_DF_ROW_REMOTE       =   21

BY_PERCENT                  =   0
BY_COUNT                    =   1



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
    
    import datetime
    
    for i in range(len(df_dtypes)) :
        
        if(df_dtypes[i] == "object") :
            
            if(isinstance(df[df_cols[i]][0],datetime.date)):
                col_stats.add_dtype_column("object[datetime.date]",df_cols[i])
            elif(isinstance(df[df_cols[i]][0],datetime.time)): 
                col_stats.add_dtype_column("object[datetime.time]",df_cols[i])
            elif(isinstance(df[df_cols[i]][0],str)):
                col_stats.add_dtype_column("object[str]",df_cols[i])
    
            else :
                col_stats.add_dtype_column(df_dtypes[i],df_cols[i])
                
        else :         
            col_stats.add_dtype_column(df_dtypes[i],df_cols[i])
    
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
        
    def add_dtype_column(self,dtype,colname) :
        
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


"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   slick grid html 
#------------------------------------------------------------------
#------------------------------------------------------------------
""" 

slick_grid_start_display_df     =   """


    <style>
        .cell-row-id-title {
            font-weight: bold;
            background-color: #ccffff;
            text-align: center;
        }
        
        .cell-index-title {
            background-color: #ffffcc;
        }
    </style>
    
    <style type="text/css" rel="stylesheet">
        .slickgrid_947187 .slick-header-column {
            left: 1000px;
        }
        
        .slickgrid_947187 .slick-top-panel {
            height: 25px;
        }
        
        .slickgrid_947187 .slick-headerrow-columns {
            height: 25px;
        }
        
        .slickgrid_947187 .slick-cell {
            height: 20px;
        }
        
        .slickgrid_947187 .slick-row {
            height: 25px;
        }
        
        .slickgrid_947187 .l0 {}
        
        .slickgrid_947187 .r0 {}
        
        .slickgrid_947187 .l1 {}
        
        .slickgrid_947187 .r1 {}
        
        .slickgrid_947187 .l2 {}
        
        .slickgrid_947187 .r2 {}
        
        .slickgrid_947187 .l3 {}
        
        .slickgrid_947187 .r3 {}
        
        .slickgrid_947187 .l4 {}
        
        .slickgrid_947187 .r4 {}
        
        .slickgrid_947187 .l5 {}
        
        .slickgrid_947187 .r5 {}
        
        .slickgrid_947187 .l6 {}
        
        .slickgrid_947187 .r6 {}
        
        .slickgrid_947187 .l7 {}
        
        .slickgrid_947187 .r7 {}
        
        .slickgrid_947187 .l8 {}
        
        .slickgrid_947187 .r8 {}
        
        .slickgrid_947187 .l9 {}
        
        .slickgrid_947187 .r9 {}
    </style>
    
<div style="background-color: #ffffff;">

    <table width="100% background-color: #ffffff">
        <tbody>
            <tr>
                <td valign="top" width="80%">
                    <div id="myGrid" style="width: 920px; height: 300px; margin-left: 25px; overflow: hidden; outline: 0px; position: relative;" class="slickgrid_959604 ui-widget"></div>
                </td>
            </tr>
        </tbody>
    </table>
    
    <script src="./PandasDataframeCleanser_files/jquery-1.7.min.js"></script>
 

    <script>
        // a standard formatter returns a string
        function formatter(row, cell, value, columnDef, dataContext) {
            return value;
        }

        var linkFormatter = function(row, cell, value, columnDef, dataContext) {
            var fstring = '<a style="text-decoration: none" title = "display row ' + value + '"' + ' href="#"' + ' onclick = "get_df_row(' + "'" + value + "'" + ')" ' + '>' + value + '</a>';
            return fstring;
        };

        var grid;

"""

from dfcleanser.common.common_utils import new_line

def build_slick_grid_column_headers(index_cols,data_cols,add_row_id_col=True) : 
    """            
    #------------------------------------------------------------------
    #   build column headers for slick grid
    #
    #   index_col_names   -   index cols
    #   data_col-namess   -   data cols
    #
    #   return : column headers html
    #
    #------------------------------------------------------------------
    """
    
    #print("build_slick_grid_column_headers",index_cols,data_cols,add_row_id_col)

    col_headers_html    =   ("        var columns = [" + new_line)
    
    if(add_row_id_col) :

        col_headers_html    =   (col_headers_html + '        {' + new_line)    
        col_headers_html    =   (col_headers_html + '          id: "rowidtitle",' + new_line)    
        col_headers_html    =   (col_headers_html + '          name: "Row ID",' + new_line)    
        col_headers_html    =   (col_headers_html + '          field: "rowidtitle",' + new_line)    
        col_headers_html    =   (col_headers_html + '          cssClass: "cell-row-id-title",' + new_line)    
        col_headers_html    =   (col_headers_html + '          formatter: linkFormatter' + new_line)    
        col_headers_html    =   (col_headers_html + '        },' + new_line)
        
    for i in range(len(index_cols)) :
        
        col_headers_html    =   (col_headers_html + '        {' + new_line)    
        col_headers_html    =   (col_headers_html + '          id: "' + index_cols[i] + "title" + '",' + new_line)    
        col_headers_html    =   (col_headers_html + '          name: "' + index_cols[i] + '",' + new_line)    
        col_headers_html    =   (col_headers_html + '          field: "' + index_cols[i] + "title" + '",' + new_line)    
        col_headers_html    =   (col_headers_html + '          cssClass: "cell-index-title"' + new_line)    
        col_headers_html    =   (col_headers_html + '        },' + new_line)
        
    for i in range(len(data_cols)) :
        
        col_headers_html    =   (col_headers_html + '        {' + new_line)    
        col_headers_html    =   (col_headers_html + '          id: "' + data_cols[i] + "title" + '",' + new_line)    
        col_headers_html    =   (col_headers_html + '          name: "' + data_cols[i] + '",' + new_line)    
        col_headers_html    =   (col_headers_html + '          field: "' + data_cols[i] + "title" + '"' + new_line) 
        
        if(i == ((len(data_cols)) - 1)) :
            col_headers_html    =   (col_headers_html + '        }' + new_line) 
        else :
            col_headers_html    =   (col_headers_html + '        },' + new_line)

    col_headers_html    =   (col_headers_html + '        ];' + new_line)
        
    return(col_headers_html)


slick_grid_middle_display_df     =   """

        var options = {
            editable: true,
            enableColumnReorder: false,
            enableCellNavigation: true
        };

        $(function() {
        
            
"""

def build_slick_grid_column_data(index_cols,data_cols,df,start_row,total_rows,add_row_id_col=True) : 
    """            
    #------------------------------------------------------------------
    #   build column headers for slick grid
    #
    #   index_col_names   -   index cols
    #   data_col-names    -   data cols
    #   df                -   dataframe
    #
    #   return : column data html
    #
    #------------------------------------------------------------------
    """
    
    from dfcleanser.common.common_utils import is_numeric_col

    import numpy
    
    if(len(df) < (start_row + total_rows)) :
        num_rows    =   (len(df) - start_row) + 1
    else :
        num_rows    =   total_rows
    
    col_data_html    =   ("        var data = [" + new_line)
    

    if(len(index_cols[0]) > 0) :
        

        index_array         =   df.index.values

        index_names         =   []
        index_dtypes        =   []
        index_val_offsets   =   [] 
            
        index_columns       =   df.index.names
         
        if(len(index_columns) > 0) :
            for i in range(len(index_columns)) :
                if( not (index_columns[i] is None) ) :
                    index_names.append(index_columns[i])
                    index_dtypes.append(df.index.get_level_values(i).dtype)
                    index_val_offsets.append(i)
        
    if((start_row + num_rows) > len(df)) :
        end_row     =   len(df)
    else :
        end_row     =   (start_row + num_rows)
    
    for i in range(start_row , end_row) :
        
        next_row_html   =   "          {"
    
        if(add_row_id_col) :
            next_row_html   =   (next_row_html + "rowidtitle : " + str(i) + ",") 
        
        if(len(index_cols[0]) > 0) :
            
            from dfcleanser.common.common_utils import is_numeric_datatype
            
            for j in range(len(index_names)) :
                
                try :
                    
                    if(is_numeric_datatype(index_dtypes[j])) :
                        
                        index_col_val   =   index_array[i][index_val_offsets[j]]
                        
                        if(numpy.isnan(index_col_val)) :
                            next_row_html   =   (next_row_html + index_names[j] + "title : 'nan'") 
                        else :
                            next_row_html   =   (next_row_html + index_names[j] + "title : " + str(index_col_val))  
                        
                    else :
                        
                        index_col_val   =   index_array[i][index_val_offsets[j]]
                        next_row_html   =   (next_row_html + index_names[j] + "title : '" + str(index_col_val) + "'")  

                    if(not (j == (len(index_cols[0]) - 1) ) ) :
                        next_row_html   =   (next_row_html +  ",") 
                    else :
                        if(len(data_cols) > 0) :
                            next_row_html   =   (next_row_html +  ",") 
                        
                except :
                    next_row_html   =   (next_row_html + index_names[j] + "title : '" + "format error" + "'") 
            
        
        for j in range(len(data_cols)) :
            
            try :
                
                if(is_numeric_col(df,data_cols[j])) :
                    
                    if(numpy.isnan(df.iloc[i,j])) :
                        
                        next_row_html   =   (next_row_html + data_cols[j] + "title : 'nan'") 
                
                    else :
                        
                        next_row_html   =   (next_row_html + data_cols[j] + "title : " + str(df.iloc[i,j]))  
                        
                else :
                    
                    next_row_html   =   (next_row_html + data_cols[j] + "title : '" + str(df.iloc[i,j]) + "'")  

                if(not (j == (len(data_cols) - 1) ) ) :
                    next_row_html   =   (next_row_html +  ",")   
                        
            except :
                
                next_row_html   =   (next_row_html + data_cols[j] + "title : " + "'format error'") 
                
                if(not (j == (len(data_cols) - 1) ) ) :
                    next_row_html   =   (next_row_html +  ",")   

                
                
        next_row_html   =   (next_row_html +  "}") 
            
        if( i < ((start_row + total_rows) - 1) ) :
            next_row_html   =   (next_row_html +  "," + new_line) 
        
        col_data_html   =   (col_data_html + next_row_html)
        
    col_data_html   =   (col_data_html + "        ];" + new_line)  
    
        
    return(col_data_html)

        
slick_grid_end_display_df     =   """
        
            grid = new Slick.Grid("#myGrid", data, columns, options);
        })
    </script>

</div>

"""

def display_df_rows(df,startrow,num_rows) : #table,rowid,colid,opstat,displayTable=True) : 
    """
    * -------------------------------------------------------------------------- 
    * function : display sample rows
    * 
    * parms :
    *   df              -   dataframe
    *   startrow        -   starting df row
    *   num_rows        -   number of rows
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    
    from dfcleanser.data_inspection.data_inspection_model import (slick_grid_start_display_df, build_slick_grid_column_headers,
                                                                  slick_grid_middle_display_df, build_slick_grid_column_data,
                                                                  slick_grid_end_display_df)
    
    df_html     =   ""
    df_html     =   (df_html + slick_grid_start_display_df)
    
    indices     =   df.index
    index_names =   indices.names
    
    indexcnames         =   []
    indexcnames_ids     =   []
    
    if( (index_names is None) or 
        ( ((len(index_names) == 1) and (index_names[0] is None)) ) ):
        indexcnames     =   []
    else :
        
        for i in range(len(index_names)) :
            
            if(not (index_names[i] is None)) :
                indexcnames.append(index_names[i])
                indexcnames_ids.append(i)
    
    colnames    =   df.columns.tolist()
    df_html     =   (df_html + build_slick_grid_column_headers(indexcnames,colnames))
    df_html     =   (df_html + slick_grid_middle_display_df)
    df_html     =   (df_html + build_slick_grid_column_data([indexcnames,indexcnames_ids],colnames,df,startrow,num_rows))
    df_html     =   (df_html + slick_grid_end_display_df)  
    
    return(df_html)





















