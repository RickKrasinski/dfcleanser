"""
#DataInspectionModel 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

DEBUG_INSPECT_DTYPES    =   False
DEBUG_INSPECT_COLUMNS   =   False
DEBUG_INSPECT_NANS      =   False
DEBUG_INSPECT_CATS      =   False
DEBUG_INSPECT_OUTLIERS  =   False
DEBUG_DISPLAY_TRACE     =   False

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    data inspection option ids
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

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
* ----------------------------------------------------
# df scroller 
* ----------------------------------------------------
""" 
class df_rows_store :
    
    # instance variables
    start_row       =   0
    num_rows        =   0
    
    # full constructor
    def __init__(self) :
        self.start_row  =   0
        self.num_rows   =   0
        
    def set_start_row(self,pstart_row) :
        self.start_row  =   pstart_row

    def get_start_row(self) :
        return(self.start_row) 
            
    def set_num_rows(self,pnum_rows) :
        self.num_rows  =   pnum_rows

    def get_num_rows(self) :
        return(self.num_rows) 
   

df_rows     =   df_rows_store()  



ROW_STATS       =   0
COLUMN_STATS    =   1

def get_nan_stats(df,stat_type) :
    """            
    #------------------------------------------------------------------
    #   get nan stats data
    #
    #   df                -   dataframe
    #   stat_type         -   start row
    #
    #   return : nan data vals list
    #
    #------------------------------------------------------------------
    """

    if(stat_type ==ROW_STATS) :
    
        rowcounts       =   0
        rowswithnulls   =   df.isnull().sum(axis=1).tolist()

        for i in range(len(rowswithnulls)) :
            if(rowswithnulls[i] != 0) :
                rowcounts = rowcounts + 1

        if(len(rowswithnulls) == 0) :
            nanstatsRows    =   str(len(df))
            totalnans       =   "0"
            statrows        =   ["Total Rows","Total Nans Found"]
            statvals        =   [nanstatsRows,totalnans]
        else :
            nanstatsRows    =   str(len(df))
            totalnans       =   str(df.isnull().sum().sum())
            totalnanrows    =   str(rowcounts)
            pctrows         =   "{0:.2f}".format(100*(rowcounts/len(df)))+"%"
            statrows        =   ["Total Rows","Total Nans Found","Number of Rows containing Nans","% of Rows containing Nans"]
            statvals        =   [nanstatsRows,totalnans,totalnanrows,pctrows]
            
    else :
        
        df_cols         =   df.columns
        df_nulls        =   df.isnull().sum()
        totnullcols     =   0
    
        for i in range(len(df_nulls)) :
            if(not df_nulls[i] == 0) :
                totnullcols = totnullcols + 1
    
        if(totnullcols == 0) :
            nanstatsCols    =   str(len(df.columns))
            totalnans       =   "0"
            statrows        =   ["Total Columns","Total Nans Found"]
            statvals        =   [nanstatsCols,totalnans]
        else :
            nanstatsCols    =   str(len(df.columns))
            totalnans       =   str(df.isnull().sum().sum())
            totalnancols    =   str(totnullcols)
            pctcols         =   "{0:.2f}".format(100*(totnullcols/len(df_cols)))+"%"
            statrows        =   ["Total Columns","Total Nans Found","Number of Cols containing Nans","% of Cols containing Nans"]
            statvals        =   [nanstatsCols,totalnans,totalnancols,pctcols]


    return([statrows,statvals])


def get_row_nans_data(df,rowsnulls) :
    """
    * -------------------------------------------------------- 
    * function : get_row_nans_data
    * 
    * parms :
    *   df          -   dataframe
    *   rowsnulls   -   list of row nulls
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    numcols         =   len(df.columns)
    #numrows         =   len(rowsnulls)
    
    maxsamplerows   =   40
    pctilecounts    =   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    pctilerows      =   [[],[],[],[],[],[],[],[],[],[],
                         [],[],[],[],[],[],[],[],[],[]]
    
    for i in range(len(rowsnulls)) :
        
        if(rowsnulls[i] > 0 ) :
            
            # get pct of nan cols for each row 
            pctnancols = int((rowsnulls[i] / numcols) * 100)
            import math
            pctile = int(math.ceil(pctnancols / 5))
            pctile = 20 - pctile
            
            pctilecounts[pctile] = pctilecounts[pctile] + 1
            if(len(pctilerows[pctile]) < maxsamplerows) :
                pctilerows[pctile].append(i)  
                
    return(pctilecounts,pctilerows)


def get_cols_nans_data(df) :
    """
    * -------------------------------------------------------- 
    * function : get the column nans grif data
    * 
    * parms :
    *   df              -   dataframe
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    df_cols         =   df.columns
    df_nulls        =   df.isnull().sum().tolist()
    numrows         =   len(df)

    df_nulls_sorted =   [] 
    
    for i in range(len(df_nulls)) :
        df_nulls_sorted.append(df_nulls[i])
    df_nulls_sorted.sort(reverse=True)
    
    df_cols_sorted  =   []
    
    for i in range(len(df_nulls_sorted)) :
        found = False;
        for j in range(len(df_nulls)) :
            if( not found) :
                if(df_nulls[j] == df_nulls_sorted[i]) :
                    found = True
                    df_nulls[j] = -1
                    df_cols_sorted.append(df_cols[j])

    return(df_nulls_sorted,df_cols_sorted)


def drop_df_nan_rows(df,threshold,ttype,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : drop rows with nans greater than threshold
    * 
    * parms :
    *   df        -   dataframe
    *   threshold -   threshold value
    *   ttype     -   threshold type
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    import math
    
    try     :

        if(ttype == BY_PERCENT) : 
            thold   =   math.floor(len(df.columns) * (float(threshold) * 0.01))
        else :
            thold   =   math.floor(float(threshold))
            
        nanslist    =   df.isnull().sum(axis=1).tolist() #< thold
        criteria    =   nanslist

        dropcount   =   0
        for i in range(len(nanslist)) :
            if(nanslist[i]) < thold :
                criteria[i]     =   True
            else :
                criteria[i]     =   False
                dropcount       =   dropcount + 1
                
        if(dropcount > 0) :
        
            df = df[criteria]
            from  dfcleanser.common.cfg import set_dfc_dataframe_df, get_config_value, CURRENT_INSPECTION_DF
            set_dfc_dataframe_df(get_config_value(CURRENT_INSPECTION_DF),df)
        
    except Exception as e:
        opstat.store_exception("Error dropping nan rows\n ",e)

    return([dropcount,len(df)])


def drop_df_nan_cols(df,threshold,ttype,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : drop rows with nans greater than threshold
    * 
    * parms :
    *   df        -   dataframe
    *   threshold -   threshold value
    *   ttype     -   threshold type
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    import math
    
    try     :
        
        if(ttype == BY_PERCENT) : 
            thold   =   math.floor(len(df) * (float(threshold) * 0.01))
        else :
            thold   =   math.floor(float(threshold))
            
        df_cols         =   df.columns
        colswithnulls   =   df.isnull().sum()
        droplist        =   []
    
        for i in range(len(colswithnulls)) :
            if(colswithnulls[i] >= thold) :
                droplist.append(df_cols[i])

        if(len(droplist) > 0) :
            df.drop(droplist,axis=1,inplace=True)
            df.reset_index(drop=True,inplace=True)

    except Exception as e:
        opstat.store_exception("Error dropping nan cols\n ",e)
        
    if(len(droplist) > 0) :
        from  dfcleanser.common.cfg import set_dfc_dataframe_df, get_config_value, CURRENT_INSPECTION_DF
        set_dfc_dataframe_df(get_config_value(CURRENT_INSPECTION_DF),df)


    return(len(droplist))




def get_dfc_cols_data(df) : 
    """
    * -------------------------------------------------------------------------- 
    * function : get df columns data
    * 
    * parms :
    *   df        -   dataframe
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    df_cols         =   df.columns
    
    coldtypes       =   []
    numuniques      =   []
    numnans         =   []

    means           =   []
    stddevs         =   []
    minvals         =   []
    maxvals         =   []
    skews           =   []
    kurtosiss       =   []
    
    from dfcleanser.common.common_utils import is_numeric_col, is_int_col, is_datetime_col, is_string_col, is_timedelta_col, is_categorical_col
    
    for i in range(len(df_cols)) :
        
        colname     =  df_cols[i] 
        
        if (is_categorical_col(df,colname)) :
            coldtypes.append("category")    
        elif(is_string_col(df,colname)) :
            coldtypes.append("object(str)")    
        else :    
            coldtypes.append(df[colname].dtype)
            
        numuniques.append(df[colname].nunique())
        numnans.append(df[colname].isnull().sum())
        
        if(is_categorical_col(df,colname)) :
            
            means.append(" ")
            stddevs.append(" ")
            minvals.append(" ")
            maxvals.append(" ")
            skews.append(" ")
            kurtosiss.append(" ")
            
        elif(is_numeric_col(df,colname)) :
        
            try :
            
                means.append(float("{0:.2f}".format(df[colname].mean())))
                stddevs.append(float("{0:.2f}".format(df[colname].std())))
                
                if(is_int_col(df,colname)) :
                
                    minvals.append(df[colname].min())
                    maxvals.append(df[colname].max())
                
                else : 
                
                    minvals.append(float("{0:.2f}".format(df[colname].min())))
                    maxvals.append(float("{0:.2f}".format(df[colname].max())))
                
                skews.append(float("{0:.2f}".format(df[colname].skew())))
                kurtosiss.append(float("{0:.2f}".format(df[colname].kurtosis())))
    
    
            except : 
            
                coldtypes.append(" ")       
                numuniques.append(" ")
                numnans.append(" ")
                means.append(" ")
                stddevs.append(" ")
                minvals.append(" ")
                maxvals.append(" ")
                skews.append(" ")
                kurtosiss.append(" ")
            
        else :
            
            means.append(" ")
            stddevs.append(" ")
            
            if( (is_datetime_col(df,colname)) or 
                (is_timedelta_col(df,colname)) ) :
                
                minvals.append(str(df[colname].min()))
                maxvals.append(str(df[colname].max()))
                
            elif(is_string_col(df,colname)) : 
                
                minlength   =   df[colname].map(lambda x: len(str(x))).min()
                minvals.append(str(minlength))
                maxlength   =   df[colname].map(lambda x: len(str(x))).max()
                maxvals.append(str(maxlength))
                
            else :
                
                minvals.append(" ")
                maxvals.append(" ")
                
            skews.append(" ")
            kurtosiss.append(" ")
  

    return([coldtypes, numuniques, numnans, means, stddevs, minvals, maxvals, skews, kurtosiss])


def get_df_index_columns_data(df) :
    """
    * -------------------------------------------------------------------------- 
    * function : get df index columns data
    * 
    * parms :
    *   df        -   dataframe
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    import pandas as pd
    
    dfIndex     =   df.index

    dfvalues    =   None

    
    if isinstance(df.index, pd.core.indexes.numeric.Int64Index) :
        
        indextype       =   "numeric.Int64Index"
        index_cols      =   df.index.names
        indexcolname    =   str(index_cols[0])
        indexdtype      =   "int64"
        indexstart      =   ""
        indexstop       =   ""
        indexstep       =   ""
        
        colids          =   ["indextype","indexcolname","dtype","start","stop","step"]
        coldata         =   [indextype,indexcolname,indexdtype,indexstart,indexstop,indexstep]
        

    elif isinstance(df.index, pd.core.indexes.range.RangeIndex) :
        
        indextype       =   "RangeIndex"
        indexcolname    =   "Row ID"
        indexdtype      =   "int64"
        indexstart      =   str(dfIndex.start)
        indexstop       =   str(dfIndex.stop)
        indexstep       =   str(dfIndex.step)
        
        colids          =   ["indextype","indexcolname","dtype","start","stop","step"]
        coldata         =   [indextype,indexcolname,indexdtype,indexstart,indexstop,indexstep]
        
    elif ( (isinstance(df.index, pd.core.indexes.base.Index)) or 
           (isinstance(df.index, pd.core.indexes.multi.MultiIndex)) ) : 
        
        index_columns   =   df.index.names

        index_names     =   []
        for i in range(len(index_columns)) :
            if(not (index_columns[i] is None)) :
                index_names.append(index_columns[i])
                
        if(len(index_names) == 1) :
            
            indexcolname    =   index_names[0]
        
            indextype       =   "Single Index"
            if(len(index_columns) == 1) :
                indexdtype      =   str(df.index.levels[0].dtype)
            else :
                indexdtype      =   str(df.index.levels[1].dtype)
         
            import numpy
        
            dfvalues        =   df.index.values.tolist()

            indexcount      =   str(len(dfvalues))
            
            dfvals          =   []
            for i in range(len(dfvalues)) :
                dfvals.append(dfvalues[i][1])

            npdfvalues      =   numpy.array(dfvals)
            npdfuniques     =   numpy.unique(npdfvalues)
            dfuniques       =   npdfuniques.tolist()
            
            indexuniques    =   str(len(dfuniques))
            indexmax        =   str(max(dfuniques))
            indexmin        =   str(min(dfuniques))
        
            colids          =   ["indextype","indexcolname","dtype","count","uniques","min","max"]
            coldata         =   [indextype,indexcolname,indexdtype,indexcount,indexuniques,indexmin,indexmax]
            
        else :
            
            indextype       =   "MultiIndex"
        
            indexcolname    =   ""
            indexdtype      =   ""
        
            import numpy
        
            dfvalues        =   df.index.values.tolist()
            indexcount      =   str(len(dfvalues))

            indexuniques    =   ""
            indexmax        =   ""
            indexmin        =   ""
        
            colids          =   ["indextype","indexcolname","dtype","count","uniques","min","max"]
            coldata         =   [indextype,indexcolname,indexdtype,indexcount,indexuniques,indexmin,indexmax]
    
    else :
        
        indextype       =   "Unknown"
        indexcolname    =   ""
        indexdtype      =   ""
        indexcount      =   ""
        indexuniques    =   ""
        indexmax        =   ""
        indexmin        =   ""

        colids          =   ["indextype","indexcolname","dtype","count","uniques","max","min"]
        coldata         =   [indextype,indexcolname,indexdtype,indexcount,indexuniques,indexmax,indexmin]


    return([colids,coldata,dfvalues])



def get_df_categories_data(df) : 
    """
    * -------------------------------------------------------- 
    * function : display row data
    * 
    * Parms :
    *  df                  -   dataframe    
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    import pandas as pd

    df_cols     = df.columns.tolist()
    
    uniquesCountList = []
    
    from dfcleanser.common.common_utils import get_col_num_uniques
    for i in range(len(df_cols)) :
        uniquesCountList.append(get_col_num_uniques(df, df_cols[i]))
                    
    uniquesValsList = []
    
    from dfcleanser.common.common_utils import get_col_uniques
    for i in range(len(df_cols)) :
        if( (uniquesCountList[i] < 25) and 
            (int((uniquesCountList[i]/len(df)*100)) < 20) ) :
            uniquesVals = get_col_uniques(df,df_cols[i])
            
            from dfcleanser.common.common_utils import is_categorical_col
            if(not (is_categorical_col(df,df_cols[i])) ) :
                uniquesValsList.append(uniquesVals.tolist())
            else :
                uniquesValsList.append(uniquesVals)
        else :
            uniquesValsList.append("None")
                
    catcols                 =   []
    catcandidates           =   []
    catcolsuniques          =   []
    catcandidatesuniques    =   []
                
    for i in range(len(uniquesValsList)) :
        if(is_categorical_col(df,df_cols[i])) :
            catcols.append(df_cols[i])
            catcolsuniques.append(uniquesValsList[i])
        else :
            if(not (type(uniquesValsList[i]) == str)) :
                if(int((uniquesCountList[i]/len(df)*100)) < 20) :
                    catcandidates.append(df_cols[i])
                    catcandidatesuniques.append(uniquesValsList[i])
        
    nans = []
    for i in range(len(catcandidates)) :
        nans.append(df[catcandidates[i]].isnull().sum())
                    
    whitespace = []
    for i in range(len(catcandidatesuniques)) :
        whitespacefound = False

        if(isinstance(catcandidatesuniques[i][0],str)) :
                        
            for j in range(len(catcandidatesuniques[i])) :
                if(isinstance(catcandidatesuniques[i][j],str)) :
                    if( (catcandidatesuniques[i][j][0] == ' ') or 
                         (catcandidatesuniques[i][j][len(catcandidatesuniques[i][j])-1] == ' ') or
                         (catcandidatesuniques[i][j].find("\t") > -1) ):
                        whitespacefound = True
                            
        whitespace.append(whitespacefound)
        
    catcanduniquescountList = []
    catcanddtypesList = []
    
    for i in range(len(catcandidates)) :
        catcanduniquescountList.append(len(get_col_uniques(df,catcandidates[i])))
        catcanddtypesList.append(df[catcandidates[i]].dtype)
        
    cat_candidates_list     =   [catcandidates, catcanddtypesList, nans, whitespace, catcanduniquescountList, catcandidatesuniques]
    categories_list         =   []

    # ------------------------------
    # categorical columns
    # ------------------------------
    if(len(catcols) > 0) :
        
        categories_list.append(catcols)
        
        cat_ordered_list    =   []
        cat_categories_list =   []

        for i in range(len(catcols)) :

            CI  =   pd.CategoricalIndex(df[catcols[i]])
            
            cat_ordered_list.append(str(CI.ordered))
            cat_categories_list.append(str(CI.categories.tolist()))
        
        categories_list.append(cat_ordered_list)
        categories_list.append(cat_categories_list)
        
    return([cat_candidates_list, categories_list])



"""
* ----------------------------------------------------
# df browser instances
* ----------------------------------------------------
""" 
class df_browser_title_store :
    
    # instance variables
    df_browsers     =   {}
    
    # full constructor
    def __init__(self) :
        self.df_browsers     =   {}
        
    def add_df_browser(self,df_title,dfbrowsergui) :
        self.df_browsers.update({df_title:dfbrowsergui})
    
    def pop_df_browser(self,df_title) :
        self.df_browsers.pop(df_title)

    def get_df_browser(self,df_title) :
        self.df_browsers.get(df_title)
            
    def get_df_browsers(self) :
        return(list(self.df_browsers.keys()))
   

dfc_df_browsers     =   df_browser_title_store()  


