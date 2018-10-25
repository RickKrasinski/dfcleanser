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

import dfcleanser.common.cfg as cfg
import dfcleanser.sw_utilities.sw_utility_dfsubset_widgets as dfsw

from dfcleanser.common.table_widgets import drop_owner_tables
from dfcleanser.common.html_widgets import new_line

from dfcleanser.common.common_utils import (display_exception, display_status, opStatus, 
                                            is_numeric_col, is_numeric_col_int, single_quote, RunningClock)

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
   
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   main taskbar and route function
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def display_dfsubset_utility(optionId,parms=None) :

    if(cfg.is_dc_dataframe_loaded()) :
        
        from IPython.display import clear_output
        clear_output()
    
        if(optionId == DISPLAY_MAIN) :
        
            dfsw.get_dfsubset_main_taskbar()
            from dfcleanser.data_inspection.data_inspection_widgets import display_inspection_data
            display_inspection_data()
            
            clear_sw_utility_dfsubsetdata()
    
        if(optionId == DISPLAY_GET_SUBSET) :
            parmslist = dfsw.get_dfsubset_input_parms(parms)
            cfg.set_config_value(dfsw.get_subset_input_id+"Parms",parmslist)
            dfsw.display_df_subset(cfg.get_dc_dataframe(),False) 
        
        elif(optionId ==  PROCESS_GET_SUBSET) :
            parmslist = dfsw.get_dfsubset_input_parms(parms)
            cfg.set_config_value(dfsw.get_subset_input_id+"Parms",parmslist)
            dfsw.get_df_subset(cfg.get_dc_dataframe(),parms)
            
        elif(optionId ==  DISPLAY_GET_SUBSET_FILTER) :
            parmslist = dfsw.get_dfsubset_input_parms(parms)
            cfg.set_config_value(dfsw.get_subset_input_id+"Parms",parmslist)
            dfsw.display_df_subset(cfg.get_dc_dataframe(),True) 

        elif(optionId ==  DISPLAY_GET_COL_VALUES) :
            dfsw.display_df_subset(cfg.get_dc_dataframe(),True,parms) 

        elif(optionId ==  PROCESS_GET_SUBSET_FILTERED) :
            dfsw.get_df_subset(cfg.get_dc_dataframe(),parms,True)
        
    else :
        dfsw.get_dfsubset_main_taskbar()
        
        from dfcleanser.data_inspection.data_inspection_widgets import display_inspection_data
        display_inspection_data()
        


"""            
#------------------------------------------------------------------
#   parse raw select string for filters
#
#   filters_text    -   select string 
#   opstat          -   operation status 
#
#------------------------------------------------------------------
"""
def parse_subset_filters(filters_text,opstat) :

    all_clauses_found   =   False
    clauses             =   []
    clauses_oper        =   []
    
    sclause             =   "( ("
    eclause             =   ") )"
    orop                =   "or"
    andop               =   "and"
    clauseorop          =   "OR"
    clauseandop         =   "AND"
    
    current_index       =   0
    total_clauses       =   0
    max_clauses         =   15

    try :
    
        while( not all_clauses_found ) :
        
            total_clauses   =   total_clauses + 1
            if(total_clauses > max_clauses) : all_clauses_found = True 
        
            start_clause    =   filters_text[current_index:].find(sclause)
            end_clause      =   filters_text[current_index:].find(eclause)
            new_clause      =   filters_text[current_index+start_clause:current_index+(end_clause+len(eclause))]
            new_clause      =   new_clause.replace("\n"," ")
            clauses.append(new_clause)
        
            next_start  =  filters_text[current_index+end_clause+len(eclause):].find(sclause) 
            if(next_start == -1) :
                all_clauses_found   =   True
            else :
                opertext = filters_text[current_index+end_clause+len(eclause):current_index+end_clause+len(eclause)+next_start]

                if(opertext.find(clauseorop) > -1) :
                    clauses_oper.append(clauseorop)
                else :
                    if(opertext.find(clauseandop) > -1) :
                        clauses_oper.append(clauseandop)
                
                current_index   =   current_index + end_clause + len(eclause)
            
        inner_clauses   =   []
        inner_oper      =   []
        sinner          =   "( "
        einner          =   " )"
    
        for i in range(len(clauses)) :
    
            clauses[i]  =   clauses[i].lstrip("(")
            clauses[i]  =   clauses[i].rstrip(")")
        
            all_inner_clauses_found =   False
            total_clauses           =   0
            current_index           =   0
        
            inner_clauses.append([])
            inner_oper.append([])
        
            while( not all_inner_clauses_found ) :

                total_clauses   =   total_clauses + 1
                if(total_clauses > max_clauses) : all_inner_clauses_found = True 
    
                sinner_clause       =   clauses[i][current_index:].find(sinner)
                einner_clause       =   clauses[i][current_index:].find(einner)
                new_inner_clause    =   clauses[i][current_index+sinner_clause:current_index+(einner_clause+len(einner))]
                inner_clauses[i].append(new_inner_clause)

                next_sinner  =  clauses[i][current_index+einner_clause+len(einner):].find(sinner) 

                if(next_sinner == -1) :
                    all_inner_clauses_found   =   True
                else :
                    opertext = clauses[i][current_index+einner_clause+len(einner):current_index+einner_clause+len(einner)+next_sinner]
 
                    if(opertext.find(orop) > -1) :
                        inner_oper[i].append(orop)
                    else :
                        if(opertext.find(andop) > -1) :
                            inner_oper[i].append(andop)
                
                    current_index   =   current_index + einner_clause + len(einner)

        return([inner_clauses, inner_oper, clauses_oper])
        
    except Exception as e:
        opstat.store_exception("Error parsing subset filters\n "  + filters_text,e)
        return(None)
        
"""            
#------------------------------------------------------------------
#   check if column is being kept
#
#   df          -   dataframe 
#   colname     -   column name 
#   colList     -   column list 
#   keepflag    -   keep or drop column list 
#
#------------------------------------------------------------------
"""
def is_valid_column(df,colname,colList,keepflag) :
    
    if(colList == None) :
        
        cols    =   df.columns.tolist()
        found   =   False
        
        for i in range(len(cols)) :
            if(cols[i] == colname) :
                found = True
                
        return(found)
        
    else :
        found   =   False
        for i in range(len(colList)) :
            if(colList[i] == colname) :
                found   =   True
                
        if(keepflag) :
            if(found)   :   return(True)
            else        :   return(False)
        else :
            if(found)   :   return(False)
            else        :   return(True)


"""            
#------------------------------------------------------------------
#   build_and_validate_search_criteria
#
#   df          -   dataframe
#   colslist    -   columns list
#   keepflag    -   keep or drop columns fllag 
#   filters     -   filters 
#   inneropers  -   inner operators 
#   inneropers  -   outer operators 
#   opstat      -   operation status 
#
#------------------------------------------------------------------
"""
def build_and_validate_search_criteria(colslist,keepflag,filters,inneropers,outeropers,opstat) :

    filtersList     =   []

    df = cfg.get_dc_dataframe()
    
    try :
        
        for i in range(len(filters)) :
        
            subfiltersList  =   []
        
            for j in range(len(filters[i])) :
                currentsubfilter    =   filters[i][j]    
                currentsubfilter    =   currentsubfilter.replace("(","")
                currentsubfilter    =   currentsubfilter.replace(")","")
                currentsubfilter    =   currentsubfilter.lstrip(" ")
                currentsubfilter    =   currentsubfilter.rstrip(" ")
    
                oper    =   ""
                
                if(currentsubfilter.find("==") == -1) :
                    if(currentsubfilter.find(">=") == -1) :
                        if(currentsubfilter.find("<=") == -1) :
                            if(currentsubfilter.find("<") == -1) :
                                if(currentsubfilter.find(">") == -1) :
                                    if(currentsubfilter.find("!=") > 0) :
                                        oper = "!="
                                    else :
                                        oper = "=="
                                else :
                                    oper = ">" 
                            else :
                                oper = "<" 
                        else :
                            oper = "<=" 
                    else :
                        oper = ">=" 
                else :
                    oper = "=="  
                  
                if(len(oper) == 0) : 
                    opstat.set_status(False)
                    opstat.set_errorMsg("Invalid operator in filter " + filters[i][j])

                else :
                
                    currentsubfilter    =   currentsubfilter.replace("'","")
                    subfiltervals       =   currentsubfilter.split(oper)

                    if( (type(subfiltervals) == list) and (len(subfiltervals) == 2))  :
                    
                        # check if valid column name 
                        if(is_valid_column(df,subfiltervals[0],colslist,keepflag)) :
                            filtersubclause = [subfiltervals,oper]
                        else :
                            opstat.set_status(False)
                            opstat.set_errorMsg("Invalid column name in filter " + filters[i][j])

                    else :
                        opstat.set_status(False)
                        opstat.set_errorMsg("Invalid values in filter " + filters[i][j])
    
                if(opstat.get_status()) :
                    subfiltersList.append(filtersubclause) 
                else :
                    break;
        
            if(opstat.get_status()) :
                filtersList.append(subfiltersList) 
            else :
                break
    
        # validate outeroperators
        for i in range(len(outeropers)) :
            if( not ((outeropers[i] == "OR") or 
                     (outeropers[i] == "AND") or
                     (outeropers[i] == "OR NOT") or
                     (outeropers[i] == "AND NOT")) ) :
                
                opstat.set_status(False)
                opstat.set_errorMsg("Invalid operator between filters " + str(i-1) + " and " + str(i))
        
        filters     =   []     
        
        if(opstat.get_status()) :

            for i in range(len(filtersList)) :
                colname     =   ""
                colvals     =   []
                colopers    =   []
        
                for j in range(len(filtersList[i])) :
                    if(j==0) :
                        colname     =   filtersList[i][j][0][0]
                    colvals.append(filtersList[i][j][0][1])
                    colopers.append(filtersList[i][j][1])
        
                filters.append([colname,colvals,colopers])
        
        return(filters)
        
    except Exception as e:
        opstat.store_exception("build_and_validate_search_criteria ",e)
        return(None)


def convert_value_datatype(df,colname,value) :
    
    ctype = 0
        
    if(is_numeric_col(df,colname)) :
        if(is_numeric_col_int(df,colname)) :
            ctype = 1
        else :
            ctype = 2

    if(ctype == 0) :
        return(value) 
    else :

        try :
            if(ctype == 1) :
                return(int(value))
            else :
                return(float(value))
        except :
            return(value)
 

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dataframe subset criteria
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def get_criteria() :
    return(dfCriteria.get_dfcriteria()) 
   
def set_criteria(dfcriteria) :
    dfCriteria.set_dfcriteria(dfcriteria)
    
class DataframeCriteria :
    
    criteria   =   None

    def __init__(self):
        self.criteria = None
    def set_dfcriteria(self,criteriaParm) :
        self.criteria = criteriaParm
    def get_dfcriteria(self) :
        return(self.criteria)

dfCriteria = DataframeCriteria()



"""            
#------------------------------------------------------------------
#  get a dataframe criteria
#
#   criteria    -   criteria logic
#   opstat      -   operation status 
#
#------------------------------------------------------------------
"""           
def get_df_criteria(criteria,opstat) :
    
    ccode   =   "from dfcleanser.common.cfg import get_dc_dataframe" + new_line
    ccode   =   (ccode + "df = get_dc_dataframe()" + new_line)
    ccode   =   (ccode + "from dfcleanser.sw_utilities.sw_utility_dfsubset_widgets import set_criteria" + new_line)
    ccode   =   (ccode + "new_criteria = " + criteria + new_line)
    ccode   =   (ccode + "set_criteria(new_criteria)" + new_line)

    try :
        
        exec(ccode)
        next_criteria = get_criteria()
        return(next_criteria)
        
    except Exception as e:
        opstat.store_exception("Error get_df_criteria ",e)

"""            
#------------------------------------------------------------------
#  dump the truth values of the indexer
#
#   indexer         -   indexer
#   display_all     -   display truths table and counts 
#
#------------------------------------------------------------------
"""   
def dump_indexer(indexer,display_all=False) :

    outtext = ""
    
    totalTrues      =   0
    totalFalses     =   0
   
    for i in range(len(indexer)) :
        
        if(indexer.iloc[i] == True) :
            outtext     =   (outtext + "T ")
            totalTrues  =   totalTrues + 1
        elif(indexer.iloc[i] == False) :
            outtext     =   (outtext + "F ")
            totalFalses =   totalFalses + 1
        
        if(display_all) :
            if((i%50) == 0) :
                if(i == 0) :
                    print("indexer len",len(indexer))
                else :
                    print(outtext)
                    outtext = ""
                    
            if(len(outtext) > 0) :
                print(outtext)

    print("Total Trues       : ",totalTrues)
    print("Total Falses      : ",totalFalses)

"""            
#------------------------------------------------------------------
#   build_and_validate_search_criteria
#
#   df          -   dataframe
#   filters     -   filters 
#   inneropers  -   inner operators 
#   inneropers  -   outer operators 
#   opstat      -   operation status 
#
#------------------------------------------------------------------
"""
def build_boolean_criteria(filters,inneropers,outeropers,opstat) :

    filterscriteriaList     =   []
    df = cfg.get_dc_dataframe()
    
    import pandas as pd
    
    try :
    
        for i in range(len(filters)) :
            
            equalvalslist       =   []
            notequalvalslist    =   []
            othervalslist       =   []
            otheroperslist      =   []
            otherindexlist      =   []
        
            equalcriteria       =   pd.Series()
            notequalcriteria    =   pd.Series()
        
            colname     =   filters[i][0].replace("'","")
            
            colvals     =   filters[i][1]
            colopers    =   filters[i][2]
            
            for j in range(len(colopers)) :
                if(colopers[j] == "==") :
                    equalvalslist.append(colvals[j]) 
                elif(colopers[j] == "!=") :
                    notequalvalslist.append(colvals[j])
                else :
                    othervalslist.append(colvals[j])
                    otheroperslist.append(colopers[j])    
                    otherindexlist.append(j)
            
            #print("\nbuild_boolean_criteria ",str(i)," : equalvalslist notequalvalslist othervalslist ","\n",equalvalslist,notequalvalslist,othervalslist)
            #print("build_boolean_criteria ",str(i)," : otheroperslist otherindexlist","\n",otheroperslist,otherindexlist)
                
            if(len(equalvalslist) > 0) : 
                for k in range(len(equalvalslist)) :
                    equalvalslist[k]    =   convert_value_datatype(df,colname,equalvalslist[k])                  
                equalcriteria   =   df[colname].isin(equalvalslist)
            if(len(notequalvalslist) > 0) : 
                for k in range(len(notequalvalslist)) :
                    notequalvalslist[k]    =   convert_value_datatype(df,colname,notequalvalslist[k])                  
                notequalcriteria   =  (~df[colname].isin(notequalvalslist))
            
            #if(not(equalcriteria.empty)) :
                #print("\nequalcriteria")
                #dump_indexer(equalcriteria)
            #if(not(notequalcriteria.empty)) :
                #print("\nnotequalcriteria")
                #dump_indexer(notequalcriteria)
                
            current_criteria     =   pd.Series()
        
            if(not(equalcriteria.empty))        :  
                if(not(notequalcriteria.empty))     :
                    current_criteria    =  (equalcriteria & notequalcriteria)
                else :
                    current_criteria    =  equalcriteria
            else :
                if(not(notequalcriteria.empty))     :   
                    current_criteria    =  notequalcriteria
            
            for j in range(len(othervalslist)) :
            
                nextcriteria            =   pd.Series()
            
                colval          =   convert_value_datatype(df,colname,othervalslist[j])
                nextcriteria    =  get_df_criteria("( df[" + single_quote(colname) + "] " + otheroperslist[j] + " " + str(colval) + " )",opstat)
                
                if((j==0) or (current_criteria.empty)) :
                    current_criteria = nextcriteria
                else :
                    if(inneropers[i][j-1] == "or") :
                        current_criteria = current_criteria | nextcriteria
                    elif(inneropers[i][j-1] == "and") :
                        current_criteria = current_criteria & nextcriteria
                    else :
                        current_criteria = current_criteria | nextcriteria
                        
            filterscriteriaList.append(current_criteria)
        
        #for i in range(len(filterscriteriaList)) :
        #    print("filters criteria : ",str(i))
        #    dump_indexer(filterscriteriaList[i])
        print("\n")
        
        for i in range(len(filterscriteriaList))  :
            
            if(i == 0) :
                final_criteria = (filterscriteriaList[0])
            else :
                if(outeropers[i-1] == "OR") :
                    final_criteria = (final_criteria | filterscriteriaList[i])
                elif(outeropers[i-1] == "AND") :
                    final_criteria = (final_criteria & filterscriteriaList[i])
                elif(outeropers[i-1] == "OR NOT") :
                    final_criteria = (final_criteria | ~(filterscriteriaList[i]))
                elif(outeropers[i-1] == "AND NOT") :
                    final_criteria = (final_criteria & ~(filterscriteriaList[i]))
                else :
                    final_criteria = (final_criteria | filterscriteriaList[i])
                    
            #print("current final criteria : ",str(i))
            dump_indexer(final_criteria)
        
        #print("\n\nfinal_criteria",opstat.get_status())
        dump_indexer(final_criteria)

        return(final_criteria) 
        
    except Exception as e:
        opstat.store_exception("Error build_boolean_criteria ",e)
        return(None)
        
"""            
#------------------------------------------------------------------
#   get the dataframe subset
#
#   df              -   dataframe
#   criteria        -   boolean criteria 
#   csv_file_name   -   file name 
##   opstat         -   operation status 
#
#------------------------------------------------------------------
"""
def get_subset_from_criteria(criteria,csv_file_name,opstat) :

    df = cfg.get_dc_dataframe()
    
    try :
        
        df = df[criteria]
        cfg.set_dc_dataframe(df)

        if(not (csv_file_name == None)) :
            df.to_csv(csv_file_name)
        
    except Exception as e:
        opstat.store_exception("Error getting subset from citeria\n ",e)

"""            
#------------------------------------------------------------------
#   get dataframe subset
#
#   df          -   dataframe
#   parms       -   associated col parms 
#   filterflag  -   associated col parms 
#
#------------------------------------------------------------------
"""
def get_df_subset(df,parms,filtered=False,display=True) :

    opstat  =   opStatus()

    # get the subset control parms
    filter_parms    =   []
    no_filters      =   True
    fparms          =   None
    
    col_names       =   []
    
    if(not filtered) :
        subsetparms     =   dfsw.get_dfsubset_input_parms(parms)
        cfg.set_config_value(dfsw.get_subset_input_id+"Parms",subsetparms)
    else :
        subsetparms     =   cfg.get_config_value(dfsw.get_subset_input_id+"Parms")
        fparms          =   dfsw.get_dfsubset_filter_input_parms(parms)
        filter_parms    =   parse_subset_filters(fparms[5],opstat)

    if( (subsetparms == None) or (len(subsetparms) == 0) ):
        row_range       =   None 
        col_names       =   None
        keep_flag       =   True
        csv_file_name   =   None
    else :
        if(len(subsetparms[0]) > 0) :
            rowvals = subsetparms[0]
            rowvals = rowvals.replace("[","")
            rowvals = rowvals.replace("]","")
            row_range = rowvals.split(":")
        else :
            row_range   =   None
            
        if(len(subsetparms[1]) > 0) :    
            col_names       =   subsetparms[1].split(",")
            for i in range(len(col_names)) :
                col_names[i]    =   col_names[i].replace("'","")
                col_names[i]    =   col_names[i].rstrip(" ")
                col_names[i]    =   col_names[i].lstrip(" ")        
        else :
            col_names   =   None
            
        if(len(subsetparms[2]) > 0) :
            keep_flag       =   False
        else :
            keep_flag       =   True
            
        if(len(subsetparms[3]) > 0) :
            csv_file_name   =   subsetparms[3]
        else : 
            csv_file_name   =   None

    #print("row_range",row_range)
    #print("col_names",col_names)
    #print("keep_flag",keep_flag)
    #print("csv_file_name",csv_file_name)
    
    if(len(filter_parms) > 0) :   
    #    print("\nfilter_parms")
    #    print(filter_parms[0]) 
    #    print(filter_parms[1])
    #    print(filter_parms[2])
        no_filters  =   False

    if(opstat.get_status()) :
    
        if(display) :
            clock = RunningClock()
            clock.start()
    
        try :

            # drop rows if requested
            if(not (row_range == None)) :
                if( ((int(row_range[0])<0) or (int(row_range[0])>len(df))) and 
                    ((int(row_range[1])<0) or (int(row_range[1])>len(df))) ) :
                    opstat.set_status(False) 
                    opstat.set_errorMsg("Row Range Drop Parm is invalid : " + subsetparms[0])
                else :
                    df.drop(df.index[int(row_range[0]):int(row_range[1])],inplace=True)
                    cfg.set_dc_dataframe(df)
                    df = cfg.get_dc_dataframe()
            
            if(opstat.get_status()) :

                # dfrop cols if requested
                if(not (col_names == None)) :
                    if(len(col_names) > 0) :
                        drop_columns    =   []
                        if(keep_flag) :

                            columns = df.columns.tolist()

                            for i in range(len(columns)) :
                                found = False
                                for j in range(len(col_names)) :
                                    if(col_names[j] == columns[i]) :
                                        found = True
                                
                                if(not found)  :
                                    drop_columns.append(columns[i])
                        else :
                            drop_columns = col_names
                                
                        for i in range(len(drop_columns)) :
                            df = df.drop([drop_columns[i]],axis=1)
                    
                        cfg.set_dc_dataframe(df)
                        df = cfg.get_dc_dataframe()
                
                if(not (no_filters)) :
                    #print("getting df subset - build_and_validate_search_criteria")
                    goodFilters = build_and_validate_search_criteria(col_names,
                                                                     keep_flag,
                                                                     filter_parms[0],
                                                                     filter_parms[1],
                                                                     filter_parms[2],
                                                                     opstat) 
            
                    if(opstat.get_status()) :
                
                        #print("getting df subset - goodFilters")
                        #for i in range(len(goodFilters)) :
                        #    print("filter ",str(i),"\n",goodFilters[i])

                        #print("getting df subset - build_boolean_criteria",opstat.get_status())
                        criteria = build_boolean_criteria(goodFilters,filter_parms[1],filter_parms[2],opstat) 
                
                    if(opstat.get_status()) :
                        get_subset_from_criteria(criteria,csv_file_name,opstat)
                        df = cfg.get_dc_dataframe()

        except Exception as e:
            opstat.store_exception("Error processing dataframe subset ",e)

        if(display) :
            clock.stop()

        
    if(opstat.get_status()) : 
        
        if(display) :
            cfg.drop_config_value(dfsw.get_subset_input_id+"Parms")
            dfsw.get_dfsubset_main_taskbar()

            print("\n")
            display_status("Dataframe subset retrieved successfully ")
            if(not(no_filters)) :
                filters = fparms[5]
            else :
                filters = None
                
            dfsw.display_df_subset_status(df,csv_file_name,filters)
        
    else :
        
        if(display) :
            from IPython.display import clear_output
            clear_output()
        
            cfg.drop_config_value(dfsw.get_subset_input_id+"Parms")
            dfsw.display_df_subset(cfg.get_dc_dataframe(),False) 
            display_exception(opstat)

"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   Geocoders utility functions
#------------------------------------------------------------------
#------------------------------------------------------------------
""" 
def clear_sw_utility_dfsubsetdata() :
    
    drop_owner_tables(cfg.SWDFSubsetUtility_ID)
    clear_sw_utility_dfsubset_cfg_values()


def clear_sw_utility_dfsubset_cfg_values() :
 
    #drop_config_value(ADDR_CONV_COL_LIST_PARM)
    return




    
    
    
    
    
    
    
    
    
    
    
    



