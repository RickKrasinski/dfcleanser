"""
# dfc_common_display_utils 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
import pandas

this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg

from dfcleanser.common.table_widgets import (SCROLL_NEXT, ROW_MAJOR, MULTIPLE, 
                                             get_mult_table, get_table_value) 

from dfcleanser.common.common_utils import  (is_numeric_col_int, is_numeric_col, get_col_uniques_by_id,
                                             is_datetime_value,is_date_value,is_time_value,is_str_value,
                                             get_first_non_nan_value, get_datatype_id, opStatus,
                                             get_datatype_title, is_numeric)


"""            
#------------------------------------------------------------------
#------------------------------------------------------------------
#
#   Common Display Utility functions
#
#------------------------------------------------------------------
#------------------------------------------------------------------
"""

"""            
#------------------------------------------------------------------
#   display col uniques  
#
#       df          -   data frame
#       colname     -   column name
#
#------------------------------------------------------------------
""" 
def display_df_unique_column(df,table,colname,sethrefs=False,incounts=None) : 
    
    if(incounts == None) :
        counts          =   df[colname].value_counts().to_dict()
    else :
        counts = incounts
    
    minvalue        =   None
    maxvalue        =   None

    if(cfg.get_config_value(cfg.UNIQUES_RANGE_KEY) != None) :

        minmax = cfg.get_config_value(cfg.UNIQUES_RANGE_KEY)
        
        if(is_numeric_col(df,colname) ) :
            if(is_numeric_col_int(df,colname) ) :
                minvalue = int(minmax[1])
                maxvalue = int(minmax[2])
            else :    
                minvalue = float(minmax[1])
                maxvalue = float(minmax[2])
    
    totnans =  df[colname].isnull().sum() 
    uniques = list(counts.keys())
    
    if(is_numeric_col(df,colname)) :
        uniques.sort()

    if(totnans > 0) :
        counts.update({"nan":totnans}) 
    
    table.set_colsperrow(5)
    if(table.get_rowspertable() == 0) :
        table.set_rowspertable(15)
    table.set_maxtables(1)

    uniqueHeader    =   ["Value","Count","Value","Count","Value","Count",
                         "Value","Count","Value","Count"]
    uniqueRows      =   []
    uniqueWidths    =   [14,6,14,6,14,6,14,6,14,6]
    uniqueAligns    =   ["center","center","center","center","center",
                         "center","center","center","center","center"]
    
    if(sethrefs) :
        uniquehrefs     =   ["chgval",None,"chgval",None,"chgval",None,
                             "chgval",None,"chgval",None]
    else :
        uniquehrefs     =   None
    
    uniquerow       =   []
 
    i = 0
    j = 0
    k = 0
    
    totaluniques = len(uniques)
    
    if(totaluniques > 250) :
        if(cfg.get_config_value(cfg.UNIQUES_RANGE_KEY) == None) :

            if(totnans > 0) :
                totaluniques = 59
            else :
                totaluniques = 60
            
    if(totnans > 0) :
        uniquerow.append("nan")
        uniquerow.append(str(totnans))
        j = 1
    
    totalfound = 0
    
    for i in range(totaluniques) :

        if(minvalue != None) :

            if((uniques[i] >= minvalue) and (uniques[i] <= maxvalue)) :

                j = j+1
                if(is_numeric_col(df,colname) ) : 
                    uniquerow.append(str(uniques[i]))
                else :
                    uniquerow.append(uniques[i])
                    
                uniquerow.append(str(counts.get(uniques[i])))
                
        else :
            j = j+1
            if(is_numeric_col(df,colname) ) : 
                uniquerow.append(str(uniques[i]))
            else :
                uniquerow.append(uniques[i])
            
            uniquerow.append(str(counts.get(uniques[i])))

            
        if(((j) % table.get_colsperrow()) == 0) :

            if(j!=0) :
                
                uniqueRows.append(uniquerow)

                totalfound = totalfound + j
                if(totalfound == totaluniques) :
                    i = totaluniques

                uniquerow      =   []
                j = 0


    if((j % table.get_colsperrow()) != 0) :

        for k in range(table.get_colsperrow() - ((j) % table.get_colsperrow())) :
            uniquerow.append("")
            uniquerow.append("")

        uniqueRows.append(uniquerow) 
            
    hiddens = [["ucolscolumnname",colname]]
    
    
    table.set_headerList(uniqueHeader)
    table.set_rowList(uniqueRows)
    table.set_widthList(uniqueWidths)
    table.set_alignList(uniqueAligns)
    table.set_refList(uniquehrefs)
    table.set_shortrow(False)    
    table.set_tabletype(ROW_MAJOR)

    table.set_hiddensList(hiddens)
    if(sethrefs) :
        table.set_note("<b>*</b> To change 'Current' or 'New' values click on value above or enter by hand. To select range of values click 'Find Values'")

    #table.dump()
    
    table.display_table()
    
def unique_list(inlist):
    
    x       =   set(inlist)
    outlist =   list(x)
    return outlist
            
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
def get_df_datatypes_data(df) : 

    df_cols     = df.columns
        
    df_dtypes   = df.dtypes.tolist()
    
    df_udtypes      =   unique_list(df_dtypes)
    df_cols         =   df_cols.tolist()
    
    dtypes_dict         = {}
    dtypes_list         = []
    dtypes_counts_list  = []
    
    non_null_values     =   []
        
    for i in range(len(df_cols)) :
        non_null_values.append(get_first_non_nan_value(df,df_cols[i]))    
 
    dtfound     =   []
    for i in range(len(df_cols)) :
        dtfound.append(False)
    
    
    for i in range(len(df_udtypes)) :
        for j in range(len(df_cols)) :
            
            if(not(dtfound[j])) :
                match           =   False
                currentdtype    =   None
            
                if(type(df_udtypes[i]) == pandas.core.dtypes.dtypes.CategoricalDtype) :
                    if(type(df_dtypes[j]) == type(df_udtypes[i])) :
                        match = True
                else :
                
                    if(get_datatype_id(df_udtypes[i]) == 16) :
                    
                        if(is_datetime_value(non_null_values[j])) :
                            match = True
                            currentdtype    =   "datetime.datetime"
                        elif(is_date_value(non_null_values[j])) :
                            match = True
                            currentdtype    =   "datetime.date"
                        elif(is_time_value(non_null_values[j])) :
                            match = True
                            currentdtype    =   "datetime.time"
                        elif(is_str_value(non_null_values[j])) : 
                            match = True
                            currentdtype    =   "str"
                        else :            
                            if(df_dtypes[j] == df_udtypes[i]) :
                                currentdtype    =   df_udtypes[i]
                                match = True
                    else : 
                    
                        if(df_dtypes[j] == df_udtypes[i]) :
                            currentdtype    =   df_udtypes[i]
                            match = True
            
                if(match) : 
                
                    dtfound[j] = True
                
                    #print(df_udtypes[i],"match found")
                    if( not ((dtypes_dict.get(currentdtype)) == None ) ): 
                        dtypes_list = dtypes_dict.get(currentdtype)
                        dtypes_list.append(df_cols[j])
                        dtypes_dict.update({currentdtype:dtypes_list})
                    else :
                        dtypes_list = []
                        dtypes_list.append(df_cols[j])
                        dtypes_dict.update({currentdtype:dtypes_list})
                    
                        if(isinstance(currentdtype,str)) :
                            if( (currentdtype == "datetime.datetime") or 
                                (currentdtype == "datetime.date") or 
                                (currentdtype == "datetime.time") or 
                                (currentdtype == "str") ) :
                                df_udtypes.append(currentdtype) 
    
    df_final_udtypes = [] 
      
    for k in range(len(df_udtypes)) :
        dtypes_vals_list    = dtypes_dict.get(df_udtypes[k])
        if(not (dtypes_vals_list == None)) :
            dtypes_counts_list.append(len(dtypes_vals_list))
            df_final_udtypes.append(df_udtypes[k])

    return([df_final_udtypes, dtypes_counts_list, dtypes_dict])


"""            
#------------------------------------------------------------------
#   get the base sizing info of a dataframe
#
#   df              -   dataframe
#
#   return : basic sizing info
#
#------------------------------------------------------------------
"""
def display_df_sizing_info(df) : 

    #print("display_df_sizing_info")
    print("        [NUMBER OF ROWS] :",len(df))
    print("        [NUMBER OF COLS] :",len(df.columns))
    



def get_num_stats(df,df_cols,i,num_stats) :

    try :
        num_stats.append(df[df_cols[i]].count())
        num_stats.append(float("{0:.2f}".format(df[df_cols[i]].mean())))
        num_stats.append(float("{0:.2f}".format(df[df_cols[i]].std())))
                
        if(is_numeric_col_int(df,df_cols[i])) :
            num_stats.append(df[df_cols[i]].min())
            num_stats.append(df[df_cols[i]].max())
        else :    
            num_stats.append(float("{0:.2f}".format(df[df_cols[i]].min())))
            num_stats.append(float("{0:.2f}".format(df[df_cols[i]].max())))
                
        num_stats.append(float("{0:.2f}".format(df[df_cols[i]].skew())))
        num_stats.append(float("{0:.2f}".format(df[df_cols[i]].kurtosis())))
                
    except : 
        num_stats = [0, 0, 0, 0, 0]
        
"""            
#------------------------------------------------------------------
#   display dataframe descriptive data
#
#   df              -   dataframe
#
#------------------------------------------------------------------
"""
def display_df_describe(df,table,datatype=None,colList=None) : #,checkboxes=False) : 
 
    if( (colList == None) or (len(colList) == 0) ) :
        df_cols     =   df.columns.tolist()
    else :
        df_cols     =   colList
        
    df_stats    =   []
    num_stats   =   []
    num_cols    =   []
    
    dtstr = get_datatype_title(get_datatype_id(datatype))

    if(not (datatype == None)) :
        dtstr = "Column Stats for datatype " + dtstr
    else :
        dtstr = "Numeric Column Stats"
        
    # build the column stats for the columns list
    for i in range(len(df_cols)) :
        
        if( is_numeric_col(df,df_cols[i]) ) :
            if(datatype == None) :
                num_cols.append(df_cols[i])
                get_num_stats(df,df_cols,i,num_stats)
                df_stats.append(num_stats)
                num_stats   =   []
            else :
                if(df[df_cols[i]].dtype == datatype) :
                    num_cols.append(df_cols[i])
                    get_num_stats(df,df_cols,i,num_stats)
                    df_stats.append(num_stats)
                    num_stats   =   []

    # build the table lists from the column stats
    dfHeader        =   ["    "]
    dfRows          =   []
    dfWidths        =   [7]
    dfAligns        =   ["center"]
    dfchrefs        =   [None]

    countrow        =   []
    meanrow         =   []
    stdrow          =   []
    minrow          =   []
    maxrow          =   []
    skewrow         =   []
    kurtrow         =   []
    
    dfHeaderList    =   []
    dfRowsList      =   []
    dfWidthsList    =   []
    dfAlignsList    =   []
    dfchrefsList    =   []
    
    table.set_colsperrow(7)
    table.set_rowspertable(8)
    table.set_maxtables(1)

    # go through column list and build table lists    
    for i in range(len(num_cols)) :
        
        if(True) :
            
            dfHeader.append(num_cols[i])
            
            countrow.append(df_stats[i][0])
            meanrow.append(df_stats[i][1])
            stdrow.append(df_stats[i][2])
            minrow.append(df_stats[i][3])
            maxrow.append(df_stats[i][4])
            skewrow.append(df_stats[i][5])
            kurtrow.append(df_stats[i][6])
            
            dfWidths.append(13)
            dfAligns.append("center")
            dfchrefs.append("ncol")
            
            if( ( ( (i+1) % table.get_colsperrow()) == 0) and (i>0) ) :
                
                dfHeaderList.append(dfHeader)    
                dfRowsList.append(get_stat_rows(table.get_tableid(),countrow,meanrow,stdrow,
                                                minrow,maxrow,skewrow,kurtrow))
                
                dfWidthsList.append(dfWidths)
                dfAlignsList.append(dfAligns)
                dfchrefsList.append(dfchrefs)
                
                dfHeader    =   ["    "]
                dfRows      =   []
                dfWidths    =   [8]
                dfAligns    =   ["center"]
                dfchrefs    =   [None]

                countrow    =   []
                meanrow     =   []
                stdrow      =   []
                minrow      =   []
                maxrow      =   []
                skewrow     =   []
                kurtrow     =   []
                
    # handle any incomplete rows    
    if( ((i+1) % table.get_colsperrow())  != 0) :
        
        for k in range((table.get_colsperrow() - ((i+1) % table.get_colsperrow())) ):#+2) :

            dfHeader.append("")
            dfRows.append("")
            dfWidths.append(13)
            dfAligns.append("center")
            dfchrefs.append(None)
            
            countrow.append("")
            meanrow.append("")
            stdrow.append("")
            minrow.append("")
            maxrow.append("")
            skewrow.append("")
            kurtrow.append("")

    if(len(dfRows) > 0) :
       
        dfHeaderList.append(dfHeader)
        dfRowsList.append(get_stat_rows(table.get_tableid(),countrow,meanrow,stdrow,
                                        minrow,maxrow,skewrow,kurtrow,))#checkboxes))
        dfWidthsList.append(dfWidths)
        dfAlignsList.append(dfAligns)
        dfchrefsList.append(dfchrefs)

    # build final multiple table    
    title = dtstr
    table.set_title(title)    
    
    table.set_headerList(dfHeaderList)
    table.set_widthList(dfWidthsList)
    table.set_alignList(dfAlignsList)
    table.set_hhrefList(dfchrefsList)
    table.set_rowList(dfRowsList)
    
    table.set_tabletype(MULTIPLE)
    table.set_numtables(len(dfHeaderList))
    table.set_note("<b>*</b> To get detailed info on any column click on the column name in the table above")

    get_mult_table(table,SCROLL_NEXT)

"""            
#------------------------------------------------------------------
#   get statistical data and form table rows
#
#   counts  -   list of counts for rows
#   means   -   list of means for rows
#   stds    -   list of counts for rows
#   mins    -   list of mins for rows
#   maxs    -   list of maxs for rows
#
#------------------------------------------------------------------
"""
def get_stat_rows(formId,counts,means,stds,mins,maxs,skews,kurtosis) :#,checkboxes) :    

    currentRow  =   []
    allrows     =   []
    
    txtCol      =   ["<b>count</b>","<b>mean</b>","<b>std</b>","<b>min</b>","<b>max</b>","<b>skew</b>","<b>kurtosis</b>"] 
    
    for i in range(len(txtCol)) :
        currentRow.append(txtCol[i])
        
        if(i == 0) :
            for j in range(len(counts)) : 
                currentRow.append(counts[j])
        elif(i == 1) :
            for j in range(len(means)) : 
                currentRow.append(means[j])
        elif(i == 2) :
            for j in range(len(stds)) : 
                currentRow.append(stds[j])
        elif(i == 3) :
            for j in range(len(mins)) : 
                currentRow.append(mins[j])
        elif(i == 4) :
            for j in range(len(maxs)) : 
                currentRow.append(maxs[j])
        elif(i == 5) :
            for j in range(len(skews)) : 
                currentRow.append(skews[j])
        else :
            for j in range(len(kurtosis)) : 
                currentRow.append(kurtosis[j])
            
        allrows.append(currentRow)
        currentRow = []
        
    return(allrows)

    
"""            
#------------------------------------------------------------------
#   display generic column data 
#
#       df          -   data frame
#
#------------------------------------------------------------------
""" 
def display_df_column_data(df,table) : 
    
    df_dtypes   = df.dtypes.tolist()
    df_cols     = df.columns.tolist()
    
    df_obj_counts   =   []
    df_obj_indices  =   []

    for i in range(len(df_dtypes)) :
        if( not (is_numeric(df[df_cols[i]].dtype)) ) :
            currentuniques = len(get_col_uniques_by_id(df,df_cols[i]))
            df_obj_indices.append(i)
            df_obj_counts.append(currentuniques)
        
    uniqueHeader   =   ["Colomn Name", "Data Type", "Count","Unique Values"]
    uniqueRows     =   []
    uniqueWidths   =   [15,10,10,65]
    uniqueAligns   =   ["center","center","center","left"]
    uniquehrefs     =   ["ucol",None,None,None]
    
    for i in range(len(df_obj_indices)) :
            
        uniqueRows.append([str(df_cols[df_obj_indices[i]]),
                           str(df_dtypes[df_obj_indices[i]]),
                           str(df_obj_counts[i]),
                           str(get_col_uniques_by_id(df,df_cols[df_obj_indices[i]]))])
    
    print("\n")
    
    table.set_headerList(uniqueHeader)
    table.set_rowList(uniqueRows)
    table.set_widthList(uniqueWidths)
    table.set_alignList(uniqueAligns)
    table.set_refList(uniquehrefs)

    table.display_table()
        

"""            
#------------------------------------------------------------------
#   display col names  
#
#       df          -   data frame
#
#------------------------------------------------------------------
""" 
def display_column_names(df,table,callback) : 

    cnames      =    df.columns.values.tolist() 
    
    table.set_colsperrow(8)
    table.set_rowspertable(8)
    table.set_maxtables(1)

    colsHeader    =   ["","","","","","","",""]
    colsRows      =   []
    colsWidths    =   [12,12,12,12,12,12,12,12]
    colsAligns    =   ["center","center","center","center",
                       "center","center","center","center"]
    colsHrefs     =   []
    
    for i in range(len(colsHeader)) :
        if(not (callback == None)) :
            colsHrefs.append(callback) 
        
    colsrow       =   []
 
    for i in range(len(cnames)) :

        if((i % table.get_colsperrow()) == 0) :

            if(i!=0) :
                colsRows.append(colsrow)
                colsrow      =   []

        colsrow.append(cnames[i])
        

    if(((i+1) % table.get_colsperrow()) != 0) :
        for k in range(table.get_colsperrow() - ((i+1) % table.get_colsperrow())) :
             colsrow.append("")
            
    colsRows.append(colsrow)    

    table.set_headerList(colsHeader)
    table.set_rowList(colsRows)
    table.set_widthList(colsWidths)
    table.set_alignList(colsAligns)
    if(len(colsHrefs) > 0) :
        table.set_refList(colsHrefs)
    if(table.get_note() == "") :
        table.set_note("<b>*</b> To get detailed info on any column click on the column name in the table above.")
    
    table.display_table()
    

"""            
#------------------------------------------------------------------
#------------------------------------------------------------------
#
#   Dataframe rows display methods
#
#------------------------------------------------------------------
#------------------------------------------------------------------
"""

"""            
#------------------------------------------------------------------
#
#  Single Sample Row components
#
#------------------------------------------------------------------
"""
max_single_rows     =   5
max_single_cols     =   10

"""            
#------------------------------------------------------------------
#   display more rows
#
#       df              -   dataframe
#       tableid         -   html table id
#       direction       -   scroll direction
#
#------------------------------------------------------------------
"""
def display_more_single_row(df,tableid,direction) : 

    sdirection = int(direction)
    
    srtable = get_table_value(tableid)
    
    srow = srtable.get_searchRow()
    scol = srtable.get_searchCol()
    
    maxcol = len(df.columns)
    
    if(sdirection == down_direction) :
        srow = srow + 1
        scol = 0
        if((len(df) - 1) < srow) : 
            srow = 0
        cfg.set_config_value(cfg.CLEANSING_ROW_KEY,str(srow))
        #from dfcleanser.data_cleansing.data_cleansing_widgets import display_row_data
        #display_row_data(df,srow,0)
        #return()

    elif(sdirection == up_direction) :
        srow = srow - 1
        scol = 0
        if(srow < 0) :
            srow = 0
        cfg.set_config_value(cfg.CLEANSING_ROW_KEY,str(srow))
        #from dfcleanser.data_cleansing.data_cleansing_widgets import display_row_data
        #display_row_data(df,srow,0)
        #return()
            
    elif(sdirection == back_direction) :
        if(scol == maxcol) :
            lastbatch = scol % (max_single_rows*max_single_cols)
            scol = scol - (max_single_rows*max_single_cols + lastbatch)
        else :
            scol = scol - (2*(max_single_rows*max_single_cols)) +1
            if(scol < 0) :
                scol = 0
            
    else :
        if(scol == (maxcol-1)) :
            scol = 0
        elif((scol + (max_single_rows*max_single_cols)) > maxcol):
            scol = scol + 1
        else :
            scol = scol + 1
    
    opstat  =   opStatus()    
    opstat, new_rows_html = display_single_row(df,srtable,srow,scol,False)
    
    return(new_rows_html)
    
"""            
#------------------------------------------------------------------
#   display single rows
#
#   df              -   dataframe
#   rowid           -   numeric row id
#   tableid         -   html table id
#   scripts         -   javascripts list
#
#------------------------------------------------------------------
"""
def display_single_row(df,table,rowid,colid,displayTable=True,headscript=None) : 

    opstat = opStatus()
    
    if(type(rowid) == str) :
        rowid = int(rowid)
    
    if(type(colid) == str) :
        colid = int(colid)
    
    if(rowid > len(df)) :
        rowid = len(df) - 1
        
    column_names = list(df.columns.values)
 
    dfRowsList      =   []
    dfhrefs         =   [] 
    dfHeaderList    =   ["","","","","","","","","",""]
    dfWidths        =   [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    dfAligns        =   ['center', 'center', 'center', 'center', 'center', 
                         'center', 'center', 'center', 'center', 'center']
      
    for i in range(max_single_rows) :
            
        rowlistIds          =   []
        rowlistvalues       =   [] 
        rowlistIdshrefs     =   []
        rowlistvalueshrefs  =   [] 

        for j in range(max_single_cols) :
            if(colid < len(column_names)) :
                
                rowlistIds.append(column_names[colid])
                rowlistIdshrefs.append("chrowval")
                rowlistvalues.append(df.iloc[rowid,colid])
                rowlistvalueshrefs.append(None)
                colid = colid + 1
                
            else :
                
                rowlistIds.append("")
                rowlistIdshrefs.append(None)
                rowlistvalues.append("")
                rowlistvalueshrefs.append(None)

        if(not (rowlistIds[0] == "")) :
            dfRowsList.append(rowlistIds)
            dfRowsList.append(rowlistvalues)
            dfhrefs.append(rowlistIdshrefs)
            dfhrefs.append(rowlistvalueshrefs)

    table.set_title("df Row Cleanser")
   
    if(len(table.get_note()) == 0) :
        table.set_note("<b>*</b> To view a specific row enter the row index and hit search icon. To change a column value click on the column id")
        
    table.set_colsperrow(10)
    table.set_rowspertable(len(dfRowsList))
    table.set_maxtables(1)
    
    table.set_headerList(dfHeaderList)
    table.set_rowList(dfRowsList)
    table.set_widthList(dfWidths)
    table.set_alignList(dfAligns)
    table.set_refList(dfhrefs)
    
    table.set_searchable(True)
    table.set_searchRow(rowid)
    table.set_searchCol(colid-1)
    
    searchParms = {}
    
    searchParms.update({"searchtext":"Row Id"})
    searchParms.update({"searchsize":14})
    searchParms.update({"searchheight":30})
    searchParms.update({"searchwidth":120})
    searchParms.update({"searchcallback":"getSingleRow('" + str(table.get_tableid()) + "'," + str(0) + ")"})
    
    searchParms.update({"upflag":True})
    searchParms.update({"upcallback":"scrollSingleRow('" + str(table.get_tableid()) + "'," + str(0) + ")"})
    searchParms.update({"downflag":True})
    searchParms.update({"downcallback":"scrollSingleRow('" + str(table.get_tableid()) + "'," + str(1) + ")"})
    
    if(len(column_names) > (max_single_rows * max_single_cols)) :
        searchParms.update({"moreflag":True})
        searchParms.update({"morecallback":"scrollSingleRow('" + str(table.get_tableid()) + "'," + str(2) + ")"})
        searchParms.update({"prevflag":True})
        searchParms.update({"prevcallback":"scrollSingleRow('" + str(table.get_tableid()) + "'," + str(3) + ")"})
    
    table.set_searchParms(searchParms)
    
    table.set_checkLength(True) 
    table.set_textLength(10) 
    
    if(displayTable) :
        table.display_table()
        return(opstat)
    else :
        
        table_html = table.get_html(False)
        return(opstat, table_html)

"""            
#------------------------------------------------------------------
#
#  Multiple Sample Row components
#
#------------------------------------------------------------------
"""

up_direction            =   0
down_direction          =   1
back_direction          =   2
forward_direction       =   3

max_rows                =   10
max_cols                =   10


"""            
#------------------------------------------------------------------
#   display more rows
#
#       df              -   dataframe
#       tableid         -   html table id
#       direction       -   scroll direction
#
#------------------------------------------------------------------
"""
def display_more_sample_rows(df,tableid,direction,rowid=-1) : 

    sdirection = int(direction)
    
    srtable = get_table_value(tableid)

    if(rowid > -1) :
        
        srow = rowid
        scol = 0
    
    else :    
        
        srow = srtable.get_searchRow()
        scol = srtable.get_searchCol()
    
    if(rowid == -1) :
        
        if(sdirection == up_direction) :
            if( (srow - ((2*max_rows)-1)) < 0) :
                srow = 0
            else :
                srow = srow - ((2*max_rows)-1)
            scol = scol - (max_cols -1)
        
        elif(sdirection == down_direction) :
            if((srow + max_rows) > len(df) ) :
                srow = 0
            else :
                srow = srow + 1
            scol = scol - (max_cols -1)

        elif(sdirection == back_direction) :
            if((scol - ((2*max_cols)-1)) < 0 ) :
                scol = 0
            else :
                scol = scol - ((2*max_cols)-1)
            srow = srow - (max_rows -1)
            
        else :
            if((scol +1) == len(df.columns)) :
                scol = 0
            elif((scol + max_cols) > len(df.columns) ) :
                scol = scol + 1#len(df.columns) - max_cols
            else :
                scol = scol + 1
                
            srow = srow - (max_rows -1)
    
    opstat  =   opStatus()    
    opstat, new_rows_html = display_sample_row(df,srtable,srow,scol,False)
    
    return(new_rows_html)


"""            
#------------------------------------------------------------------
#   display sample rows
#
#   df              -   dataframe
#   rowid           -   numeric row id
#   tableid         -   html table id
#   scripts         -   javascripts list
#
#------------------------------------------------------------------
"""
def display_sample_row(df,table,rowid,colid,displayTable=True) : 
    
    opstat = opStatus()
    
    if(type(rowid) == str) :
        rowid = int(rowid)

    df_vals_list = []
    
    if(rowid > len(df)) :
        opstat.set_status(False)
        opstat.set_errorMsg("Row Id " + str(rowid) + "out of index")
    else :
        try :
            for i in range(max_rows) :
                
                if((i+ rowid) < len(df)) :
                    df_vals     = df.iloc[[rowid+i]].values
                    df_vals_list.append(df_vals)
        except Exception as e: 
            opstat.set_status(False)
            opstat.set_errorMsg("Row Id " + str(rowid) + "out of index")

        df_vals     = df_vals[0]
    
    if(not opstat.get_status()) :
        return(opstat)
    
    table.set_title("df Browser")
   
    if(len(table.get_note()) == 0) :
        table.set_note("<b>*</b> To view a specific row enter the Row Id(index) and hit search icon.")
        
    dfHeaderList    =   []
    dfWidths        =   [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    dfAligns        =   ['center', 'center', 'center', 'center', 'center', 
                         'center', 'center', 'center', 'center', 'center']
        
    dfHeaderList    =   []
    dfRowsList      =   []
    dfhrefs         =   []
    
    table.set_colsperrow(10)
    table.set_rowspertable(max_rows)
    table.set_maxtables(1)
    
    column_names = list(df.columns.values)
    
    for i in range(max_cols) :
        if(len(column_names) > (colid + i) )  :
            dfHeaderList.append(column_names[colid + i])
        else :
            dfHeaderList.append("")
            
    lastrow     =   0
    lastcol     =   0
    
    for i in range(max_rows) :
        
        rowlistIdshrefs     =   []
        dfrow               =   []
        
        if(len(df) > (rowid + i))  :
            for j in range(max_cols) :
                if(len(column_names) > (colid + j))  : 
                    dfrow.append(df.iloc[(rowid + i),(colid + j)])
                    lastrow =  rowid + i
                    lastcol =  colid + j
                else :
                    dfrow.append("")
                    
                if(colid == 0) :
                    if((colid + j) == 0) :
                        rowlistIdshrefs.append("getsrow")
                    else :
                        rowlistIdshrefs.append(None)
                            
        
        dfRowsList.append(dfrow)
        if(colid == 0) :
            dfhrefs.append(rowlistIdshrefs)
        else :
            dfhrefs = None
    
    table.set_headerList(dfHeaderList)
    table.set_rowList(dfRowsList)
    table.set_widthList(dfWidths)
    table.set_alignList(dfAligns)
    
    if(not(dfhrefs == None)) :
        table.set_refList(dfhrefs)
        table.set_refIndex(rowid)
    else :
        table.set_refList(None)
        
    table.set_searchable(True)
    table.set_searchRow(lastrow)
    table.set_searchCol(lastcol)
    
    searchParms = {}
    
    searchParms.update({"searchtext":"Row Id"})
    searchParms.update({"searchsize":14})
    searchParms.update({"searchheight":30})
    searchParms.update({"searchwidth":120})
    searchParms.update({"searchcallback":"getSampleRow('" + str(table.get_tableid()) + "')"})
    
    searchParms.update({"upflag":True})
    searchParms.update({"upcallback":"scrollSampleRow('" + str(table.get_tableid()) + "'," + str(0) + ")"})
    searchParms.update({"downflag":True})
    searchParms.update({"downcallback":"scrollSampleRow('" + str(table.get_tableid()) + "'," + str(1) + ")"})
    searchParms.update({"moreflag":True})
    searchParms.update({"morecallback":"scrollSampleRow('" + str(table.get_tableid()) + "'," + str(2) + ")"})
    searchParms.update({"prevflag":True})
    searchParms.update({"prevcallback":"scrollSampleRow('" + str(table.get_tableid()) + "'," + str(3) + ")"})
    
    table.set_searchParms(searchParms)
    
    table.set_checkLength(True) 
    table.set_textLength(10) 
    
    if(displayTable) :
        table.display_table()
        return(opstat)
    else :
        table_html = table.get_html(False)
        return(opstat, table_html)


   
