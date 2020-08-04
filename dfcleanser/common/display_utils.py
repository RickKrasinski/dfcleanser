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

from dfcleanser.common.table_widgets import (SCROLL_DOWN, ROW_MAJOR,  dcTable, SCROLL_RIGHT, SCROLL_NONE, get_col_major_table,
                                             get_table_value, get_row_major_table, COLUMN_MAJOR) 

from dfcleanser.common.common_utils import  (is_int_col, is_numeric_col, get_col_uniques,patch_html, displayHTML,
                                             opStatus, display_generic_grid, is_categorical_col,whitecolor)


"""            
#------------------------------------------------------------------
#------------------------------------------------------------------
#
#   Common Display Utility functions
#
#------------------------------------------------------------------
#------------------------------------------------------------------
"""

def display_df_unique_column(df,table,colname,sethrefs=False,display=True) : 
    """            
    #------------------------------------------------------------------
    #   display col uniques and count 
    #
    #       df          -   data frame
    #       table       -   dc table
    #       colname     -   column name
    #       sethrefs    -   set hrefs flag
    #       display     -   display or html flag
    #
    #------------------------------------------------------------------
    """ 
    
    import pandas as pd
    import numpy as np
    
    if(not(is_categorical_col(df,colname))) :
    
        counts      =   df[colname].value_counts().to_dict()
        uniques     =   list(counts.keys())
        uniques.sort()
        
    else :
        
        CI          =   pd.CategoricalIndex(df[colname])
        codes       =   CI.codes
        uniques     =   CI.categories.tolist()
        
        cunique, ccounts = np.unique(codes, return_counts=True)
        cunique     =   cunique.tolist()
        ccounts     =   ccounts.tolist()
        counts      =   {}
        
        for i in range(len(cunique)) :
            if(not (cunique[i] == -1)) :
                counts.update({cunique[i]:ccounts[i]})
                
        cuniques    =   list(counts.keys())
        cuniques.sort()
        
        for i in range(len(cuniques)) :
            counts.update({uniques[cuniques[i]]:counts.get(cuniques[i])})
            counts.pop(cuniques[i],None)
            
        cfg.drop_config_value(cfg.UNIQUES_RANGE_KEY)
    
    totnans     =  df[colname].isnull().sum()
    
    minvalue        =   None
    maxvalue        =   None
    contains_value  =   None
    
    if(cfg.get_config_value(cfg.UNIQUES_RANGE_KEY) != None) :

        findparms = cfg.get_config_value(cfg.UNIQUES_RANGE_KEY)
        
        if(is_numeric_col(df,colname) ) :
            
            if(is_int_col(df,colname) ) :
                
                if(len(findparms[0]) < 1) :
                    minvalue    =   int(min(uniques))
                else :
                    minvalue = int(findparms[0])
                    
                if(len(findparms[1]) < 1) :
                    minvalue    =   int(max(uniques))
                else :
                    maxvalue    =   int(findparms[1])
            
            else :
                
                if(len(findparms[0]) < 1) :
                    minvalue    =   float(min(uniques))
                else :
                    minvalue    =   float(findparms[0])
                
                if(len(findparms[1]) < 1) :
                    minvalue    =   float(max(uniques))
                else :
                    maxvalue    =   float(findparms[1])
                    
        else :
            
            contains_value  =   findparms[0]

    final_uniques     =   []
    
    if(is_numeric_col(df,colname)) :
        if((minvalue is None) and (maxvalue is None)) :
            final_uniques     =   uniques
        else :
            for i in range(len(uniques)) :
                if(not (minvalue is None)) :
                    if(not (maxvalue is None)) :
                        if( (uniques[i] >= minvalue) and (uniques[i] <= maxvalue) ) :
                            final_uniques.append(uniques[i])
                    else :
                        if( (uniques[i] >= minvalue) ) :
                            final_uniques.append(uniques[i])
                else :
                    if( (uniques[i] <= maxvalue) ) :
                        final_uniques.append(uniques[i])
                        
    else :
        
        if(not(is_categorical_col(df,colname))) :

            if((contains_value is None)) :
                final_uniques     =   uniques
            else :
                for i in range(len(uniques)) :
                    if(uniques[i].find(contains_value) > -1) :
                        final_uniques.append(uniques[i]) 
                        
        else :
            
            final_uniques     =   uniques    

    if( (totnans > 0) and (not(is_categorical_col(df,colname))) ) :
        counts.update({"nan":totnans}) 
        
    table.set_colsperrow(3)
    
    if(not(is_categorical_col(df,colname))) :
        uniqueHeader    =   ["Value","Count","Value","Count","Value","Count"]
    else :
        uniqueHeader    =   ["Category","Count","Category","Count","Category","Count"]
        
    uniqueRows      =   []
    uniqueWidths    =   [22,12,23,12,23,12]
    uniqueAligns    =   ["center","center","center","center","center","center"]
        
    if(table.get_rowspertable() == 0) :
        table.set_rowspertable(8)
    table.set_maxtables(1)
    
    if(sethrefs) :
        
        if(not(is_categorical_col(df,colname))) :
            
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                uniquehrefs     =   ["chgval",None,"chgval",None,"chgval",None,
                                     "chgval",None,"chgval",None]
            else :
                uniquehrefs     =   ["chgval",None,"chgval",None,"chgval",None]
                
        else :
            
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                uniquehrefs     =   ["chgcat",None,"chgcat",None,"chgcat",None,
                                     "chgcat",None,"chgcat",None]
            else :
                uniquehrefs     =   ["chgcat",None,"chgcat",None,"chgcat",None]
                
    else :
        uniquehrefs     =   None
    
    uniquerow       =   []
 
    i = 0
    j = 0
    k = 0

    totaluniques = len(final_uniques)
    
    if(totaluniques > 100) :
        if(cfg.get_config_value(cfg.UNIQUES_RANGE_KEY) == None) :

            if(totnans > 0) :
                totaluniques = 59
            else :
                totaluniques = 60
            
    if( (totnans > 0) and (not(is_categorical_col(df,colname))) ) :
        uniquerow.append("nan")
        uniquerow.append(str(totnans))
        j = 1
        
    totalfound = 0
    
    for i in range(totaluniques) :

        uniquerow.append(str(final_uniques[i]))
        uniquerow.append(str(counts.get(final_uniques[i])))
        j = j + 1

            
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
        
        if(not(is_categorical_col(df,colname))) :
            
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                table.set_note("<b>*</b> To select 'Current' or 'New' values click on value above or enter by hand. To select range of values enter min and max and click 'Find Values'")
            else :
                table.set_note("<b>*</b> To select 'Current' or 'New' values click on value above or enter by hand.<br>&nbsp;&nbsp; To select range of values enter min and max and click 'Find Values'")
                
        else :
            
            table.set_note("<b>*</b> To select a category click on the category above or enter by hand.")            
    
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
            



def display_df_sizing_info(df) : 
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

    #print("display_df_sizing_info")
    print("        [NUMBER OF ROWS] :",len(df))
    print("        [NUMBER OF COLS] :",len(df.columns))
    



#def get_num_stats(df,df_cols,i,num_stats) :
    """            
    #------------------------------------------------------------------
    #   get numeric column stats
    #
    #   df   -   dfc table for display
    #   direction           -   scroll direction
    #   display             -   display flag
    #
    #------------------------------------------------------------------
    """
    """
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
    
"""            
#------------------------------------------------------------------
#------------------------------------------------------------------
#   display numeric df column data objects
#------------------------------------------------------------------
#------------------------------------------------------------------
"""

def update_df_describe(df_describe_table,direction=SCROLL_RIGHT,display=True) : 
    """            
    #------------------------------------------------------------------
    #   display df column data
    #
    #   df_describe_table   -   dfc table for display
    #   direction           -   scroll direction
    #   display             -   display flag
    #
    #------------------------------------------------------------------
    """
    
    df  =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
    
    from dfcleanser.common.table_widgets import set_col_major_table_scroll
    set_col_major_table_scroll(df_describe_table,direction)
    
    dfHeader        =   ["    "]
    dfWidths        =   [7]
    dfAligns        =   ["center"]
    dfchrefs        =   [None] 
    
    numuniquesrow   =   ["<b>uniques</b>"]
    numnansrow      =   ["<b>nans</b>"]
    meanrow         =   ["<b>mean</b>"]
    stdrow          =   ["<b>std dev</b>"]
    minrow          =   ["<b>min</b>"]
    maxrow          =   ["<b>max</b>"]
    skewrow         =   ["<b>skew</b>"]
    kurtrow         =   ["<b>kurtosis</b>"]
       
    dfRowsList      =   []
    
    df_cols         =   df.columns.tolist()
    
    start_col       =   df_describe_table.get_lastcoldisplayed()
    
    if( not (start_col == 0)) :
        start_col   =   start_col + 1

    num_displayed   =   0
    
    cols_to_display =   []
    
    current_col     =   start_col
        
    while (num_displayed < df_describe_table.get_colsperrow()) :
        
        if(current_col < len(df_cols)) :
            
            if(is_numeric_col(df,df_cols[current_col])) :
                cols_to_display.append(current_col)
                num_displayed   =   num_displayed + 1
                
            current_col     =   current_col + 1
            
        else :
            
            if(len(cols_to_display) == 0) :
                current_col     =   0
            else :
                cols_to_display.append(-1)
                num_displayed   =   num_displayed + 1
            
    for i in range(len(cols_to_display)) :
        
        if(cols_to_display[i] == -1) :
            
            dfHeader.append(" ")
            
            numuniquesrow.append(" ")
            numnansrow.append(" ")
            meanrow.append(" ")
            stdrow.append(" ")
            minrow.append(" ")
            maxrow.append(" ")
            skewrow.append(" ")
            kurtrow.append(" ")
            
        else :
            
            dfHeader.append(df_cols[cols_to_display[i]])
        
            numuniquesrow.append(df[df_cols[cols_to_display[i]]].nunique())
            numnansrow.append(df[df_cols[cols_to_display[i]]].isnull().sum())
        
            try :
                meanrow.append(float("{0:.2f}".format(df[df_cols[cols_to_display[i]]].mean())))
                stdrow.append(float("{0:.2f}".format(df[df_cols[cols_to_display[i]]].std())))
                
                if(is_int_col(df,df_cols[cols_to_display[i]])) :
                    minrow.append(df[df_cols[cols_to_display[i]]].min())
                    maxrow.append(df[df_cols[cols_to_display[i]]].max())
                else :    
                    minrow.append(float("{0:.2f}".format(df[df_cols[cols_to_display[i]]].min())))
                    maxrow.append(float("{0:.2f}".format(df[df_cols[cols_to_display[i]]].max())))
                
                skewrow.append(float("{0:.2f}".format(df[df_cols[cols_to_display[i]]].skew())))
                kurtrow.append(float("{0:.2f}".format(df[df_cols[cols_to_display[i]]].kurtosis())))
            
            except : 
                    
                numuniquesrow.append(" ")
                numnansrow.append(" ")
                meanrow.append(" ")
                stdrow.append(" ")
                minrow.append(" ")
                maxrow.append(" ")
                skewrow.append(" ")
                kurtrow.append(" ")
            
        dfWidths.append(13)
        dfAligns.append("center")
        dfchrefs.append("ncol")
        
    dfRowsList.append(numuniquesrow)
    dfRowsList.append(numnansrow)
    dfRowsList.append(meanrow)
    dfRowsList.append(stdrow)
    dfRowsList.append(minrow)
    dfRowsList.append(maxrow)
    dfRowsList.append(skewrow)
    dfRowsList.append(kurtrow)
    
    df_describe_table.set_title("Numeric Column Stats")    
    
    df_describe_table.set_headerList(dfHeader)
    df_describe_table.set_widthList(dfWidths)
    df_describe_table.set_alignList(dfAligns)
    df_describe_table.set_rowList(dfRowsList)
    df_describe_table.set_hhrefList(dfchrefs)
    
    df_describe_table.set_tabletype(COLUMN_MAJOR)
    
    df_describe_table.set_lastcoldisplayed(current_col)
    df_describe_table.set_maxcolumns(len(df_cols))
    
    df_describe_table.set_note("* To cleanse any column click on the column name in the table above")

    if(display) :
        get_col_major_table(df_describe_table,True)
    
    else :
        return(get_col_major_table(df_describe_table,False))

        
def display_df_describe(display=True) : 
    """            
    #------------------------------------------------------------------
    #   display df column data
    #
    #   display     -   display flag
    #
    #------------------------------------------------------------------
    """
    df_describe_table = dcTable("Numeric Column Names ",
                                  "dcgendfdesc",
                                  cfg.DataCleansing_ID)
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        df_describe_table.set_colsperrow(7)
    else :
        df_describe_table.set_colsperrow(4)
        
    df_describe_table.set_rowspertable(8)
    df_describe_table.set_lastcoldisplayed(0)
    
    if(display) :
        update_df_describe(df_describe_table,SCROLL_RIGHT,True)
    else :
        df_describe_html   =   update_df_describe(df_describe_table,SCROLL_RIGHT,False)
        return(df_describe_html)


"""            
#------------------------------------------------------------------
#------------------------------------------------------------------
#   display non numeric df column data objects
#------------------------------------------------------------------
#------------------------------------------------------------------
"""

nn_alpha_numeric_button  =   """
                            <div>
                                        <button type='button' class='btn btn-grp dc-schema-button' style='margin-left:15px;' id="canXXXXbutton" onClick="nn_check_compatability(0,'XXXXcolname')">Check</br>Alpha</br>Numeric</button>
                            </div>
"""

nn_numeric_button       =   """
                            <table>
                                <tr>
                                    <td align='center' style='width:100%'>
                                        <button type='button' class='btn btn-grp dc-schema-button' style='margin-left:11px;' id="cnXXXXbutton" onClick="nn_check_compatability(1,'XXXXcolname')">Check</br>Numeric</button>
                                    </td>
                                </tr>
                            </table>
"""


def update_df_nn_describe(nn_df_describe_table,direction=SCROLL_RIGHT,display=True) : 
    """            
    #------------------------------------------------------------------
    #   display df column data
    #
    #   nn_df_describe_table    -   dfc table for display
    #   direction               -   scroll direction
    #   display                 -   display flag
    #
    #------------------------------------------------------------------
    """
    
    df  =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
    
    if(not (direction==SCROLL_NONE)) :
        from dfcleanser.common.table_widgets import set_col_major_table_scroll
        set_col_major_table_scroll(nn_df_describe_table,direction)
    
    # build the table lists from the column stats
    dfHeader        =   ["    "]
    dfWidths        =   [7]
    dfAligns        =   ["center"]
    dfchrefs        =   [None] 
    
    numuniquesrow   =   ["<b>uniques Count</b>"]
    numnansrow      =   ["<b>nans Count</b>"]
    alphanumrow     =   ["<b>Alpha Numeric</b>"]
    numrow          =   ["<b>Numeric</b>"]
       
    dfRowsList      =   []
    
    df_cols     =   df.columns.tolist()
    
    start_col       =   nn_df_describe_table.get_lastcoldisplayed()
    if( not (start_col == 0)) :
        start_col       =   start_col + 1
        
    num_displayed   =   0
    
    cols_to_display     =   []
    
    current_col         =   start_col
        
    while (num_displayed < nn_df_describe_table.get_colsperrow()) :
        
        if(current_col < len(df_cols)) :
            
            if(not (is_numeric_col(df,df_cols[current_col]))) :
                cols_to_display.append(current_col)
                num_displayed   =   num_displayed + 1
                
            current_col     =   current_col + 1
            
        else :
            
            if(len(cols_to_display) == 0) :
                current_col     =   0
            else :
                cols_to_display.append(-1)
                num_displayed   =   num_displayed + 1
            
    for i in range(len(cols_to_display)) :
        
        if(cols_to_display[i] == -1) :
            
            dfHeader.append(" ")
            
            numuniquesrow.append(" ")
            numnansrow.append(" ")
            alphanumrow.append(" ")
            numrow.append(" ")
            
        else :
            
            dfHeader.append(df_cols[cols_to_display[i]])
        
            numuniquesrow.append(df[df_cols[cols_to_display[i]]].nunique())
            numnansrow.append(df[df_cols[cols_to_display[i]]].isnull().sum())


            from dfcleanser.common.common_utils import is_string_col, is_object_col, is_categorical_col
            if( ( (is_string_col(df,df_cols[cols_to_display[i]])) or 
                  (is_object_col(df,df_cols[cols_to_display[i]])) ) and
                ( (not (is_categorical_col(df,df_cols[cols_to_display[i]]))) ) ) :
                    
                from dfcleanser.data_cleansing.data_cleansing_model import ALPHANUMERIC, NUMERIC, get_compatability_status
                
                cstatus     =   get_compatability_status(ALPHANUMERIC,cols_to_display[i])
                    
                if(cstatus is None) :
                        
                    alphanumbutton_html =   nn_alpha_numeric_button
                    alphanumbutton_html =   alphanumbutton_html.replace("XXXXbutton","col" + str(i))
                    alphanumbutton_html =   alphanumbutton_html.replace("XXXXcolname",df_cols[cols_to_display[i]])
                    alphanumrow.append(alphanumbutton_html)
                        
                else :
                        
                    if(cstatus) :
                        alphanumrow.append("True")
                    else :
                        alphanumrow.append("False")
                            
                cstatus     =   get_compatability_status(NUMERIC,cols_to_display[i])
                    
                if(cstatus is None) :
                    
                    numbutton_html      =   nn_numeric_button
                    numbutton_html      =   numbutton_html.replace("XXXXbutton","col" + str(i))
                    numbutton_html      =   numbutton_html.replace("XXXXcolname",df_cols[cols_to_display[i]])
                    numrow.append(numbutton_html)
                        
                else :
                        
                    if(cstatus) :
                        numrow.append("True")
                    else :
                        numrow.append("False")
                
            else : 
                    
                alphanumrow.append(" ")
                numrow.append(" ")

            
        dfWidths.append(13)
        dfAligns.append("center")
        dfchrefs.append("ncol")
        
    dfRowsList.append(numuniquesrow)
    dfRowsList.append(numnansrow)
    dfRowsList.append(alphanumrow)
    dfRowsList.append(numrow)
    
    nn_df_describe_table.set_title("Non Numeric Column Stats")    
    
    nn_df_describe_table.set_headerList(dfHeader)
    nn_df_describe_table.set_widthList(dfWidths)
    nn_df_describe_table.set_alignList(dfAligns)
    nn_df_describe_table.set_rowList(dfRowsList)
    nn_df_describe_table.set_hhrefList(dfchrefs)
    
    nn_df_describe_table.set_tabletype(COLUMN_MAJOR)
    
    #print("current_col",current_col)
    
    nn_df_describe_table.set_lastcoldisplayed(current_col)
    #print("lastcoldisplayed",df_describe_table.get_lastcoldisplayed())
    nn_df_describe_table.set_maxcolumns(len(df_cols))
    
    nn_df_describe_table.set_note("* To cleanse any non numeric column click on the column name in the table above")

    if(display) :
        get_col_major_table(nn_df_describe_table,True)
    
    else :
        return(get_col_major_table(nn_df_describe_table,False))

 
def display_df_nn_describe(display=True,no_scroll=False) : 
    """            
    #------------------------------------------------------------------
    #   display non numeric df column data
    #
    #   display     -   display flag
    #
    #------------------------------------------------------------------
    """
    
    if(no_scroll) :
        df_nn_describe_table = get_table_value("dcnngendfdesc")        
    else :
    
        df_nn_describe_table = dcTable("Non Numeric Column Names ",
                                       "dcnngendfdesc",
                                       cfg.DataCleansing_ID)
        
        df_nn_describe_table.set_lastcoldisplayed(0)
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        df_nn_describe_table.set_colsperrow(7)
    else :
        df_nn_describe_table.set_colsperrow(4)
        
    df_nn_describe_table.set_rowspertable(4)
    
    
    if(display) :
        update_df_nn_describe(df_nn_describe_table,SCROLL_RIGHT,True)
    else :
        df_nn_describe_html   =   update_df_nn_describe(df_nn_describe_table,SCROLL_RIGHT,False)
        return(df_nn_describe_html)


def get_stat_rows(formId,counts,means,stds,mins,maxs,skews,kurtosis) :#,checkboxes) :    
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
        if(not (callback is None)) :
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
        if(callback == "select_reorder_cols") :
            table.set_note("<b>*</b> To set the column_to_move or column_to_move_after click on the column name in the table above.")
        else :    
            table.set_note("<b>*</b> To get detailed info on any column click on the column name in the table above.")
    else :
        if(table.get_note() == "None") :    
            table.set_note("")
            
    table.set_small(True)
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        
        table.set_smallwidth(95)
        table.set_smallmargin(35)
        table.set_smallfsize(13)
        table.set_large_body_row_font_size()        
    else :
        
        table.set_small(True)
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
max_single_rows     =   1
max_single_cols     =   10

max_total_cols      =   100

    
def get_single_row(df,table,rowid,colid,opstat,displayTable=True,headscript=None) : 
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

    results         =   setup_sample_row_lists(df,table,rowid,colid,opstat)
    
    dfWidths        =   results[0]
    dfAligns        =   results[1]
    cols_per_row    =   results[2]
    
    #print("cols_per_row",cols_per_row)
    
    index_columns   =   df.index.names
    
    index_names     =   []
    col_names       =   []
    row_id_offset   =   0
                    
    if(len(index_columns) > 0) :
        for i in range(len(index_columns)) :
            if( not (index_columns[i] is None) ) :
                index_names.append(index_columns[i])
            else :
                row_id_offset   =   1

    if(len(index_names) > 0) :
        for i in range(len(index_names)) :
            col_names.append(index_names[i])
        
    column_names    =   list(df.columns.values)
    for i in range(len(column_names)) :
        col_names.append(column_names[i])    
    
    num_cols        =   len(col_names)
    
    if(num_cols > max_total_cols) :
        num_cols    =   max_total_cols
        
    #print("num_cols",num_cols)
        
    import math
    num_rows    =    int(math.ceil(num_cols / cols_per_row))

    #print("num_rows",num_rows)
    
    if(len(index_names) > 0) :
        index_vals  =   df.index.values
    
    # populat the table rows
    for i in range(num_rows) :
            
        rowlistIds          =   []
        rowlistvalues       =   [] 
        rowlistIdshrefs     =   []
        rowlistvalueshrefs  =   [] 

        colid   =   (i * cols_per_row)
        
        #print("colid",colid)
        
        for j in range(cols_per_row) :
            
            #print("inner colid",colid,num_cols)
            
            if(colid < num_cols) :
                
                #print("inner colid less ",colid,num_cols)
                 
                rowlistIds.append(col_names[colid])
                rowlistIdshrefs.append("chrowval")
                
                if(col_names[colid] in index_names) :
                    rowlistvalues.append(index_vals[rowid][colid + row_id_offset])    
                else :   
                    rowlistvalues.append(df.iloc[rowid,colid-len(index_names)])
                    
                rowlistvalueshrefs.append(None)
                colid   =   colid + 1
                
            else :
                
                #print("inner colid not less ",colid,num_cols)
                
                rowlistIds.append("")
                rowlistIdshrefs.append(None)
                rowlistvalues.append("")
                rowlistvalueshrefs.append(None)

        dfRowsList.append(rowlistIds)
        dfRowsList.append(rowlistvalues)
        dfhrefs.append(rowlistIdshrefs)
        dfhrefs.append(rowlistvalueshrefs)


    
    table.set_headerList(dfHeaderList)
    table.set_rowList(dfRowsList)
    table.set_widthList(dfWidths)
    table.set_alignList(dfAligns)
    table.set_refList(dfhrefs)
    table.set_rowspertable(2*num_rows)
    
    #table.dump()

    
    if(num_cols > max_single_cols) :
        table.set_checkLength(True) 
        table.set_textLength(10)
    else :
        table.set_checkLength(False)

    if(displayTable) :
        table.display_table()
        return(opstat)
    else :
        
        table_html = table.get_html()
        
        #print(table_html)
        return(table_html)


"""            
#------------------------------------------------------------------
#
#  Multiple rows components
#
#------------------------------------------------------------------
"""


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
    
    
    max_cols                =   10
    popup_max_cols          =   5
   
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


def get_df_col_names_table(df,tableid,owner,callback,callbackParms=None,colsList=None,nonnumericOnly=False) :
    """
    * ---------------------------------------------------------
    * function : get dataframe column names html table
    * 
    * parms :
    *  df               - dataframe
    *  tableid          - table id
    *  owner            - table owner
    *  callback         - callback for column click
    *  callbackParms    - callback parms for column click
    *  colsList         - df columns list or None for all cols
    *  nonnumericOnly   - numeric only cols flag
    *
    * returns : 
    *  cols name html table
    * --------------------------------------------------------
    """
    
    if(not (colsList == None)) :
        colnames = colsList
    else :
        colnames            =   df.columns.values.tolist() 
    
    colnamesHeader      =   [""]
    colnamesRows        =   []
    colnamesWidths      =   [100]
    colnamesAligns      =   ["left"]
    colnamesHrefs       =   []
    
    for i in range(len(colnames)) :
        
        if( (nonnumericOnly)  and (colsList == None) ): 
            if( not (is_numeric_col(df,colnames[i])) ) :
                colnamesrow = [colnames[i]]
                colnamesRows.append(colnamesrow)
                colnamesHrefs.append([callback])
                
        else : 
            colnamesrow = [colnames[i]]
            colnamesRows.append(colnamesrow)
            colnamesHrefs.append([callback])
        
    colnames_table = None
    
    colnames_table = dcTable("Column Names",tableid,owner,
                              colnamesHeader,colnamesRows,
                              colnamesWidths,colnamesAligns)
            
    colnames_table.set_refList(colnamesHrefs)
    
    colnames_table.set_small(True)
    colnames_table.set_smallwidth(98)
    colnames_table.set_smallmargin(10)

    colnames_table.set_border(True)
        
    colnames_table.set_checkLength(True)
            
    colnames_table.set_textLength(26)
    colnames_table.set_html_only(True) 
    
    colnames_table.set_tabletype(ROW_MAJOR)
    colnames_table.set_rowspertable(14)
    
    if(not (callbackParms == None)) :
        colnames_table.set_refParm(str(callbackParms))

    listHtml = get_row_major_table(colnames_table,SCROLL_DOWN,False)

    return(listHtml)


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
    



import dfcleanser.common.table_widgets as tblw 
#from dfcleanser.common.common_utils import (get_dfc_dataframe_df)

def get_column_samples_html(colname) :
    """
    * ---------------------------------------------------------
    * function : get column samples
    * 
    * Parms :
    *  colname    - column name
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    columnsamplesHeader      =   [""]

    columnsamplesRows        =   []
    columnsamplesWidths      =   [100]
    columnsamplesAligns      =   ["left"]
    columnsamplesHrefs       =   []
    
    uniques =   [] 
     
    #TODO blank df
    #check if the object is string
    if (isinstance(cfg.get_dfc_dataframe_df()[colname][0], str)) :
        
        uniques =   cfg.get_dfc_dataframe_df()[colname].unique().tolist()
        for i in range(len(uniques)) :
            uniques[i]  =   str(uniques[i])
        uniques.sort()
    else :
        if(is_numeric_col(cfg.get_dfc_dataframe_df(),colname)) :           
            uniques =   cfg.get_dfc_dataframe_df()[colname].unique().tolist()
            uniques.sort()

    if(len(uniques) > 0) :

        if(len(uniques) > 3) :
            count = 3
        else :
            count = len(uniques)
            
        for i in range(count) :
            columnsamplesRows.append([str(uniques[i])])
            columnsamplesHrefs.append([None])

    else : 
        columnsamplesRows.append([str(colname)])
        columnsamplesHrefs.append([None])
        columnsamplesRows.append([" Unique Values not listable: "])
        columnsamplesHrefs.append([None])
        
    columnsamples_table = None

    columnsamples_table = tblw.dcTable("Column Samples",
                                       "datetimecolnamesTable",cfg.DataTransform_ID,
                                       columnsamplesHeader,columnsamplesRows,
                                       columnsamplesWidths,columnsamplesAligns)
    
    columnsamples_table.set_refList(columnsamplesHrefs)

    columnsamples_table.set_small(True)
    columnsamples_table.set_smallwidth(98)
    columnsamples_table.set_smallmargin(10)

    columnsamples_table.set_border(True)
        
    columnsamples_table.set_checkLength(True)
            
    columnsamples_table.set_textLength(30)
    columnsamples_table.set_html_only(True) 
    
    columnsamples_table.set_tabletype(tblw.ROW_MAJOR)
    columnsamples_table.set_rowspertable(14)

    tablehtml = tblw.get_row_major_table(columnsamples_table,tblw.SCROLL_DOWN,False)


    
    startinner = tablehtml.find('<div class="row">')
    endinner    =   len(tablehtml) - 7
    
    return(tablehtml[startinner:endinner])



def displayParms(title,labels,values,tblid,width=None,leftMargin=0,display=True,font=None) :
    """
    #--------------------------------------------------------------------------
    #   display a list of parms as a table
    #
    #       title  - parms title 
    #       labels - parm labels
    #       values - parm values
    #       id     - table id
    #       width  - fixed table width in pixels
    #
    #   return table of parms
    #
    #--------------------------------------------------------------------------
    """ 
    
    maxllabels      =   0
    maxlvalues      =   0

    if( not ( (len(labels)>0) and (len(labels) == len(values)) ) ) :
        return("<p>Invalid Parameter List</p>")
        
    for i in range(len(labels)) :
        if(len(labels[i])>maxllabels) :
            maxllabels = len(labels[i])
            
    for i in range(len(values)) :
        if(len(values[i])>maxlvalues) :
            
            # check for line breaks
            if("<br/>" in values[i]) :
                #print("line break in parm")
                nextlinebreak   =   0
                lastlinebreak   =   0
                totcount = 0
                while ( (nextlinebreak != -1) and (totcount < 10)) :
                    
                    totcount = totcount + 1
                    nextlinebreak = values[i][lastlinebreak:].find("<br/>")  
                    if(nextlinebreak != -1) :
                         if( (nextlinebreak + len("<br/>") > maxlvalues) ) :
                            maxlvalues = (nextlinebreak + len("<br/>"))
                         lastlinebreak = lastlinebreak + nextlinebreak + len("<br/>")
    
            else :
                maxlvalues = len(values[i])
                
    if(display) :      
        print("\n")        
    
    import math
    labelwidth = int(math.ceil((maxllabels / (maxllabels + maxlvalues)) * 100)) 
    if(labelwidth < 20) :
        labelwidth  =   20
    
    valuewidth = (100 - 4) - labelwidth
    
    if( (len(labels) == 1) and (len(labels[0]) == 1) ) :
        parmsWidths    =   [1,labelwidth,1,valuewidth+4]
    else :
        parmsWidths    =   [1,labelwidth,3,valuewidth]
        
    parmsAligns    =   ["center","left","center","left"]
    
    colorList = []    
    
    parmsRows      =   []
    
    for i in range(len(labels)) : 
        if( (len(labels[i]) > 0) and (len(values[i]) > 0) ) :
            if( (len(labels) == 1) and (len(labels[0]) == 1) ) :
                parmsRows.append([" ",labels[i]," ",values[i]]) 
            else :
                parmsRows.append([" ",labels[i],"<b>:</b>",values[i]])
            colorList.append([whitecolor,whitecolor,whitecolor,whitecolor])
    
    parmsHeader    =   ["","","",""]
    parms_table = tblw.dcTable(title,"parmsTable",tblid,
                               parmsHeader,parmsRows,parmsWidths,parmsAligns)

    parms_table.set_rowspertable(len(labels))
    parms_table.set_small(True)

    if(not (width is None)) :
        parms_table.set_smallwidth(width)

    parms_table.set_smallmargin(leftMargin)
    parms_table.set_border(False)
    parms_table.set_checkLength(False)
    if(not(font is None)) :
        parms_table.set_table_column_parms({"font":font})
        
    if(display) :
        parms_table.display_table()
    else :
        return(parms_table.get_html())


def get_scroll_table_html(tableid,direction) :
    """
    * ---------------------------------------------------------
    * function : get a scrolled dc table html
    * 
    * Parms :
    *  tableid    - table id
    *  direction  - scroll direction
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    
    if(tblw.get_table_value(tableid).get_tabletype() == tblw.ROW_MAJOR) : 
         table_html = tblw.get_row_major_table(tblw.get_table_value(tableid),direction,False)
    
    elif(tblw.get_table_value(tableid).get_tabletype() == tblw.COLUMN_MAJOR) : 
        tblw.scroll_col_major_table(tblw.get_table_value(tableid),direction)
        return(None)
    
    elif(tblw.get_table_value(tableid).get_tabletype() == tblw.ROW_COL_MAJOR) : 
        return(None)
        
    else :
        return(None)
    
    if(tblw.get_table_value(tableid).get_tabletype() == tblw.COLUMN_MAJOR) :
        
        #print("COLUMN_MAJOR")
        tablehtmlloc    = table_html.find("<thead")
        tableendhtmlloc = table_html.find("</tbody>")
        table_html = table_html[tablehtmlloc:tableendhtmlloc+len("</tbody>")]
        
    else :
        # check for no header tables
        if(table_html.find("<thead") == -1) :
            tablehtmlloc    = table_html.find("<tbody")
            table_html      = table_html[tablehtmlloc + len("<tbody"):]
            tablehtmlloc    = table_html.find("<tbody>")
            table_html      = table_html[tablehtmlloc:]
            tableendhtmlloc = table_html.find("</tbody>")
            table_html = table_html[:tableendhtmlloc+len("</tbody>")]
    
    new_table_html = patch_html(table_html)
    
    return(new_table_html)



def flatten_json_dict(jdict) :
    """
    * ---------------------------------------------------------
    * function : flatten a json dict
    * 
    * Parms :
    *  jdict    - json representation of a dict
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    dicthex     =   []
    ashex       =   []
    commashex   =   []
                
    for i in range(len(jdict)) :
        dicthex.append(hex(ord(jdict[i])))
                    
    for i in range(len(dicthex)) :
        if([i] == '0xa') :
            ashex.append(i)
        
        if(dicthex[i] == '0x22') : 
            if(len(ashex) > len(commashex)) :
                commashex.append(i)
               
    flatdict     =   ""
                
    startok = 0
    for i in range(len(ashex)) :
                    
        flatdict    =   flatdict + jdict[startok:ashex[i]] + " "
        startok = commashex[i]
                
    flatdict    =   flatdict + jdict[startok:]
                
    return(flatdict)





















