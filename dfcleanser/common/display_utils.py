"""
# dfc_common_display_utils 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys

this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg

from dfcleanser.common.table_widgets import (SCROLL_DOWN, ROW_MAJOR, MULTIPLE, 
                                             get_mult_table, get_table_value) 

from dfcleanser.common.common_utils import  (is_int_col, is_numeric_col, get_col_uniques,
                                             get_datatype_id, opStatus, get_datatype_title, display_generic_grid)


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
def display_df_unique_column(df,table,colname,sethrefs=False,incounts=None,display=True) : 
    
    if(incounts == None) :
        counts          =   df[colname].value_counts().to_dict()
    else :
        counts = incounts
    
    minvalue        =   None
    maxvalue        =   None

    if(cfg.get_config_value(cfg.UNIQUES_RANGE_KEY) != None) :

        minmax = cfg.get_config_value(cfg.UNIQUES_RANGE_KEY)
        
        if(is_numeric_col(df,colname) ) :
            if(is_int_col(df,colname) ) :
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
    else :
        if(totnans > 0) :
            import pandas as pd
            pd.Series(uniques).fillna("nan").tolist()
        else :
            uniques.sort()
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        table.set_colsperrow(5)
    
        uniqueHeader    =   ["Value","Count","Value","Count","Value","Count",
                             "Value","Count","Value","Count"]
        uniqueRows      =   []
        uniqueWidths    =   [14,6,14,6,14,6,14,6,14,6]
        uniqueAligns    =   ["center","center","center","center","center",
                             "center","center","center","center","center"]
        
    else :
        table.set_colsperrow(3)
        
        uniqueHeader    =   ["Value","Count","Value","Count","Value","Count"]
        uniqueRows      =   []
        uniqueWidths    =   [22,12,28,12,28,18]
        uniqueAligns    =   ["center","center","center","center","center","center"]
        
        
    if(table.get_rowspertable() == 0) :
        table.set_rowspertable(8)
    table.set_maxtables(1)

    
    if(sethrefs) :
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            uniquehrefs     =   ["chgval",None,"chgval",None,"chgval",None,
                                 "chgval",None,"chgval",None]
        else :
            uniquehrefs     =   ["chgval",None,"chgval",None,"chgval",None]
    else :
        uniquehrefs     =   None
    
    uniquerow       =   []
 
    i = 0
    j = 0
    k = 0
    
    totaluniques = len(uniques)
    
    if(totaluniques > 100) :
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
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            table.set_note("<b>*</b> To change 'Current' or 'New' values click on value above or enter by hand. To select range of values enter min and max and click 'Find Values'")
        else :
            table.set_note("<b>*</b> To change 'Current' or 'New' values click on value above or enter by hand.<br>&nbsp;&nbsp; To select range of values enter min and max and click 'Find Values'")
            

    #table.dump()
    
    table_html  =   table.get_html(False)
    
    if(display) :
    
        unique_column_heading_html      =   "<div>Unique Column Values</div>"
            
        gridclasses     =   ["display-df-unique-columns-base-wrapper-header", "dfc-top-centered"]
        gridhtmls       =   [unique_column_heading_html, table_html]
    
        display_generic_grid("display-df-unique-columns-base-wrapper",gridclasses,gridhtmls)
    
    else :
        
        return(table_html)
        
    
def unique_list(inlist):
    
    x       =   set(inlist)
    outlist =   list(x)
    return outlist
            



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
                
        if(is_int_col(df,df_cols[i])) :
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
def display_df_describe(df,table,datatype=None,colList=None,display=True) : 
 
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
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        table.set_colsperrow(7)
    else :
        table.set_colsperrow(4)
        
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

    if(display) :
        get_mult_table(table,SCROLL_DOWN)
    else :
        mult_html   =   get_mult_table(table,SCROLL_DOWN,False)
        return(mult_html)

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
        if( not (is_numeric_col(df,df_cols[i])) ) :
            currentuniques = len(get_col_uniques(df,df_cols[i]))
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
                           str(get_col_uniques(df,df_cols[df_obj_indices[i]]))])
    
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
def display_column_names(df,table,callback,display=True) : 

    cnames      =    df.columns.values.tolist() 
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        
        table.set_colsperrow(8)
        table.set_rowspertable(8)
        table.set_maxtables(1)

        colsHeader    =   ["","","","","","","",""]
        colsRows      =   []
        colsWidths    =   [12,12,12,12,12,12,12,12]
        colsAligns    =   ["center","center","center","center",
                           "center","center","center","center"]
        
    else :
        
        table.set_colsperrow(4)
        table.set_rowspertable(16)
        table.set_maxtables(1)

        colsHeader    =   ["","","",""]
        colsRows      =   []
        colsWidths    =   [24,25,25,25]
        colsAligns    =   ["center","center","center","center"]
        
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
    
    table.set_small(True)
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        table.set_smallwidth(90)
        table.set_smallmargin(45)
    else :
        table.set_smallwidth(94)
        table.set_smallmargin(20)
        

    
    if(display) :
        table.display_table()
    else :
        return(table.get_html())
    

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
def display_more_single_row(df,tableid,direction,opstat) : 

    sdirection = int(direction)
    
    srtable = get_table_value(tableid)
    
    srow = srtable.get_searchRow()
    scol = srtable.get_searchCol()
    
    maxcol = len(df.columns)
    
    from dfcleanser.common.table_widgets import SCROLL_DOWN, SCROLL_UP, SCROLL_LEFT
    
    if(sdirection == SCROLL_DOWN) :
        
        srow = srow + 1
        scol = 0
        
        if((len(df) - 1) < srow) : 
            srow = 0
        
        cfg.set_config_value(cfg.CLEANSING_ROW_KEY,str(srow))

    elif(sdirection == SCROLL_UP) :
        
        srow = srow - 1
        scol = 0
        
        if(srow < 0) :
            srow = 0
        
        cfg.set_config_value(cfg.CLEANSING_ROW_KEY,str(srow))
            
    elif(sdirection == SCROLL_LEFT) :
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
    
    new_rows_html = display_single_row(df,srtable,srow,scol,opstat,False)
    
    return(new_rows_html)

    
def display_single_row(df,table,rowid,colid,opstat,displayTable=True,headscript=None) : 
    """
    * -------------------------------------------------------------------------- 
    * function : display a single df row
    * 
    * parms :
    *   df              -   dataframe
    *   table           -   dfc table
    *   rowid           -   numeric row id
    *   colid           -   cokumn id
    *   opstat          -   op status var
    *   displayTable    -   display table flag
    *   headscript      -   header hhref
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    dfHeaderList    =   []
    dfWidths        =   []
    dfAligns        =   [] 
    dfRowsList      =   []
    dfhrefs         =   []
    
    if(type(rowid) == str) :
        rowid = int(rowid)
    
    if(type(colid) == str) :
        colid = int(colid)
    
    if(rowid > len(df)) :
        rowid = len(df) - 1


    results     =   setup_sample_row_lists(df,table,rowid,colid,opstat)
    
    dfWidths    =   results[0]
    dfAligns    =   results[1]
    numcols     =   results[2]
        
    column_names = list(df.columns.values)
    num_cols        =   len(column_names)

    # populat the trable rows
    for i in range(max_single_rows) :
            
        rowlistIds          =   []
        rowlistvalues       =   [] 
        rowlistIdshrefs     =   []
        rowlistvalueshrefs  =   [] 

        for j in range(numcols) :
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
    
    table.set_headerList(dfHeaderList)
    table.set_rowList(dfRowsList)
    table.set_widthList(dfWidths)
    table.set_alignList(dfAligns)
    table.set_refList(dfhrefs)

    if(len(table.get_note()) == 0) :
        tnote   =  "<b>*</b> To view a specific row enter the row index and hit search icon. To change a column value click on the column id"
    else :
        tnote   =   None

    searchParms = {}
    
    setup_sample_row_table(table,
                           "df Row Cleanser",
                           tnote,
                           numcols,
                           len(dfRowsList),
                           rowid,
                           colid-1,
                           searchParms,
                           opstat) 
       
    searchParms.update({"searchcallback":"getSingleRow('" + str(table.get_tableid()) + "'," + str(0) + ")"})
    
    if(len(column_names) > (max_single_rows * max_single_cols)) :
        searchParms.update({"SCROLL_UP":True})
        searchParms.update({"SCROLL_UP_callback":"scrollSingleRow('" + str(table.get_tableid()) + "'," + str(0) + ")"})
        searchParms.update({"SCROLL_DOWN":True})
        searchParms.update({"SCROLL_DOWN_callback":"scrollSingleRow('" + str(table.get_tableid()) + "'," + str(1) + ")"})
    
    if(len(column_names) > (max_single_rows * max_single_cols)) :
        searchParms.update({"SCROLL_RIGHT":True})
        searchParms.update({"SCROLL_RIGHT_callback":"scrollSingleRow('" + str(table.get_tableid()) + "'," + str(2) + ")"})
        searchParms.update({"SCROLL_LEFT":True})
        searchParms.update({"SCROLL_LEFT_callback":"scrollSingleRow('" + str(table.get_tableid()) + "'," + str(3) + ")"})
    
    table.set_searchParms(searchParms)
    
    if(num_cols > max_cols) :
        table.set_checkLength(True) 
        table.set_textLength(10)
    else :
        table.set_checkLength(False)

    if(displayTable) :
        table.display_table()
        return(opstat)
    else :
        
        table_html = table.get_html(False)
        return(table_html)


"""            
#------------------------------------------------------------------
#
#  Multiple rows components
#
#------------------------------------------------------------------
"""

max_rows                =   10
max_cols                =   10
popup_max_cols          =   5

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
        
        srow    =   rowid
        scol    =   0
    
    else :    
        
        srow    =   srtable.get_searchRow()
        scol    =   srtable.get_searchCol()
        
    print("display_more_sample_rows",tableid,rowid,"srow - ",srow,"scol - ",scol) 
    
    from dfcleanser.common.table_widgets import SCROLL_DOWN, SCROLL_UP, SCROLL_LEFT
    
    if(rowid == -1) :
        
        if(sdirection == SCROLL_UP) :
            
            if( (srow - (max_rows)-1) < 0) :
                srow = 0
            else :
                srow = srow - ((max_rows))
                
            #scol = scol - (max_cols -1)
        
        elif(sdirection == SCROLL_DOWN) :
            
            if((srow + max_rows) > len(df) ) :
                srow = 0
            else :
                srow = srow + max_rows
                
            #scol = scol - (max_cols -1)

        elif(sdirection == SCROLL_LEFT) :
            if((scol - (max_cols-1)) < 0 ) :
                scol = 0
            else :
                scol = scol - ((max_cols))
                
            #srow = srow - (max_rows -1)
            
        else :
            if((scol + max_cols) > len(df.columns) ) :
                scol = 0
            else :
                scol = scol + max_cols
                
    print("display_more_sample_rows after",tableid,rowid,srow,scol) 
    
    opstat  =   opStatus()    
    new_rows_html = display_sample_rows(df,srtable,srow,scol,opstat,False)
    
    return(new_rows_html)


def setup_sample_row_lists(df,table,rowid,colid,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : set sample row table lists
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    dfWidths        =   []
    dfAligns        =   []
            
    column_names    =   list(df.columns.values)
    num_cols        =   len(column_names)
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        maxCols     =   max_cols
    else :
        maxCols     =   popup_max_cols
    
    if(num_cols < maxCols) :
        
        #if first column is numeric make narrow
        from dfcleanser.common.common_utils import is_numeric_col
        if(is_numeric_col(df,column_names[0])) :
            dfWidths.append(10)
            dfAligns.append('center')
            more_cols   =  num_cols-1
        else :
            more_cols   =  num_cols
        
        for i in range(more_cols) :
            dfWidths.append(int((max_cols/more_cols) * 10))
            dfAligns.append('center')
            
        numcolsdisplayed    =   num_cols
        
    else :
        
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        
            dfWidths            =   [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
            dfAligns            =   ['center', 'center', 'center', 'center', 'center', 
                                     'center', 'center', 'center', 'center', 'center']
            
        else :
            
            dfWidths            =   [10, 10, 10, 10, 10]
            dfAligns            =   ['center', 'center', 'center', 'center', 'center'] 
        
        numcolsdisplayed    =   maxCols

    return([dfWidths, dfAligns, numcolsdisplayed])


def setup_sample_row_table(table,title,note,numcols,max_rows,searchrow,searchcol,searchParms,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : set sample row table attributes
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    table.set_title(title)
    
    if(len(table.get_note()) == 0) :
        if(not (note is None)) :
            table.set_note(note)
    
    table.set_colsperrow(numcols)
    table.set_rowspertable(max_rows)
    table.set_maxtables(1)
   
    table.set_searchable(True)
    table.set_searchRow(searchrow)
    table.set_searchCol(searchcol)

    searchParms.update({"searchtext":"Row Id"})
    searchParms.update({"searchsize":14})
    searchParms.update({"searchheight":30})
    searchParms.update({"searchwidth":120})
 
    searchParms.update({"searchcoltext":"Column Value"})
    searchParms.update({"searchcolsize":18})
    searchParms.update({"searchcolheight":30})
    searchParms.update({"searchcolwidth":140})
    

def display_sample_rows(df,table,rowid,colid,opstat,displayTable=True) : 
    """
    * -------------------------------------------------------------------------- 
    * function : display sample rows
    * 
    * parms :
    *   df              -   dataframe
    *   table           -   dfc table 
    *   rowid           -   numeric row id
    *   colid           -   cokumn id
    *   opstat          -   op status var
    *   displayTable    -   display table flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    dfHeaderList    =   []
    dfWidths        =   []
    dfAligns        =   [] 
    dfRowsList      =   []
    dfhrefs         =   []
    
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
        except Exception : 
            opstat.set_status(False)
            opstat.set_errorMsg("Row Id " + str(rowid) + "out of index")

        df_vals     = df_vals[0]
    
    if(not (opstat.get_status()) ) :
        return(opstat)
    
    results     =   setup_sample_row_lists(df,table,rowid,colid,opstat)
    
    dfWidths    =   results[0]
    dfAligns    =   results[1]
    numcols     =   results[2]

    column_names    =   list(df.columns)#.values)
    num_cols        =   len(column_names)

    for i in range(numcols) :
        if(len(column_names) > (colid + i) )  :
            dfHeaderList.append(column_names[colid + i])
        else :
            if(numcols > max_cols) :
                dfHeaderList.append("")
    
    if(len(df) >= max_rows) :
        num_rows    =   max_rows
    else :
        num_rows    =   len(df)
    
    for i in range(num_rows) :
        
        rowlistIdshrefs     =   []
        dfrow               =   []
        
        if(len(df) > (rowid + i))  :
            for j in range(numcols) :
                if(len(column_names) > (colid + j))  : 
                    dfrow.append(df.iloc[(rowid + i),(colid + j)])
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
    from dfcleanser.common.table_widgets import ROW_COL_MAJOR
    table.set_tabletype(ROW_COL_MAJOR)
    table.set_rowspertable(10)
    table.set_colsperrow(10)
    table.set_lastcoldisplayed(colid+9)
    table.set_lastrowdisplayed(rowid+9)
    
    
    if(not(dfhrefs == None)) :
        table.set_refList(dfhrefs)
        table.set_refIndex(rowid)
    else :
        table.set_refList(None)
        
    if(len(table.get_note()) == 0) :
        tnote   =   "<b>*</b> To view a specific row enter the Row Id(index) and hit search icon."
    else :
        tnote   =   None
   
    if(len(table.get_note()) == 0) :
        if(not (tnote is None)) :
            table.set_note(tnote)
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        title   =   "df Browser"
    else :
        title   =   "df"
        
    table.set_title(title)
    
    
    searchParms = {}
    
    table.set_searchable(True)
    table.set_searchRow(rowid)
    table.set_searchCol(colid)

    searchParms.update({"searchcallback":"getSampleRow('" + str(table.get_tableid()) + "')"})
    searchParms.update({"searchinputtext":"Row ID"})
    searchParms.update({"searchinputId":"DIsamplerowsInputId"})
    
    if(num_rows >= max_rows) :
        searchParms.update({"SCROLL_UP":True})
        searchParms.update({"SCROLL_UP_callback":"scrollSampleRow('" + str(table.get_tableid()) + "'," + str(0) + ")"})
        searchParms.update({"SCROLL_DOWN":True})
        searchParms.update({"SCROLL_DOWN_callback":"scrollSampleRow('" + str(table.get_tableid()) + "'," + str(1) + ")"})
    
    if(num_cols > max_cols) :
        searchParms.update({"SCROLL_RIGHT":True})
        searchParms.update({"SCROLL_RIGHT_callback":"scrollSampleRow('" + str(table.get_tableid()) + "'," + str(2) + ")"})
        searchParms.update({"SCROLL_LEFT":True})
        searchParms.update({"SCROLL_LEFT_callback":"scrollSampleRow('" + str(table.get_tableid()) + "'," + str(3) + ")"})
    
    table.set_searchParms(searchParms)
    
    if(num_cols > max_cols) :
        table.set_checkLength(True) 
        table.set_textLength(10)
    else :
        table.set_checkLength(False)

    if(displayTable) :
        table.display_table()

    else :
        table_html = table.get_html(False)
        return(table_html)


def display_dfcleanser_taskbar(tbform,checkInline=True) :
    
    tb_html     =   tbform.get_html()
    #print("display_dfcleanser_taskbar",tb_html)
    #print(tbform.dump())
    
    gridclasses     =   ["dfcleanser-common-grid-header"]
    gridhtmls       =   [tb_html]

    if(checkInline) :
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("dfc-taskbar-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("dfc-taskbar-pop-up-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("dfc-taskbar-wrapper",gridclasses,gridhtmls)
        
        
def display_pop_up_buffer() :
    
    if(not(cfg.get_dfc_mode() == cfg.INLINE_MODE)) :
        print("\n")
        print("\n")
    
