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
import dfcleanser.sw_utilities.sw_utility_dfsubset_model as dfsm
import dfcleanser.sw_utilities.sw_utility_dfsubset_widgets as dfsw


from dfcleanser.common.table_widgets import drop_owner_tables
from dfcleanser.common.html_widgets import new_line

from dfcleanser.common.common_utils import (display_exception, display_status, opStatus, get_parms_for_input,  
                                            is_numeric_col, is_int_col, RunningClock)

   
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   main taskbar and route function
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_subset_df() :
    return(cfg.get_current_chapter_df(cfg.CURRENT_SUBSET_DF))


def get_current_subset_df(parms) :
    
    fparms          =   get_parms_for_input(parms[0],["dsdfdataframe"])
    if(len(fparms) > 0) :
        selected_df     =   fparms[0]
            
            
        if(not (len(selected_df) == 0) ) :
            cfg.set_config_value(cfg.CURRENT_SUBSET_DF,selected_df)


def display_dfsubset_utility(optionId,parms=None) :
    

    if(cfg.is_a_dfc_dataframe_loaded()) :
        
        from IPython.display import clear_output
        clear_output()
    
        if(optionId == dfsm.DISPLAY_MAIN) :
            dfsw.get_dfsubset_main_taskbar()
            clear_sw_utility_dfsubsetdata()
            
            cfg.display_data_select_df(cfg.SWDFSubsetUtility_ID)
    
        if(optionId == dfsm.DISPLAY_GET_SUBSET) :
            if(len(parms) > 0) :

                if(len(parms) == 1) :
                    get_current_subset_df(parms)
                else :
                    parmslist = dfsw.get_dfsubset_input_parms(parms)
                    cfg.set_config_value(dfsw.get_subset_input_id+"Parms",parmslist)
                    
            dfsw.display_df_subset(get_subset_df(),False) 
        
        elif(optionId ==  dfsm.PROCESS_GET_SUBSET) :
            parmslist = dfsw.get_dfsubset_input_parms(parms)
            if(len(parmslist) > 0) :
                cfg.set_config_value(dfsw.get_subset_input_id+"Parms",parmslist)
            get_df_subset(parms)
            
        elif(optionId ==  dfsm.DISPLAY_GET_SUBSET_FILTER) :
            parmslist = dfsw.get_dfsubset_input_parms(parms)
            if(len(parmslist) > 0) :
                cfg.set_config_value(dfsw.get_subset_input_id+"Parms",parmslist)
            dfsw.display_df_subset(get_subset_df(),True) 

        elif(optionId ==  dfsm.DISPLAY_GET_COL_VALUES) :
            dfsw.display_df_subset(get_subset_df(),True,parms) 

        elif(optionId ==  dfsm.PROCESS_GET_SUBSET_FILTERED) :
            get_df_subset(parms,True)
        
        elif(optionId ==  dfsm.DISPLAY_FILTERS) :
            dfsw.display_filters(get_subset_df())

        elif(optionId ==  dfsm.ADD_FILTER) :

            newfilter   =   parms[0]
            
            filtersDict     =   cfg.get_config_value(cfg.CURRENT_SUBSET_FILTERS)
            
            if(filtersDict == None) :
                title   =   "filter 0"
                filtersDict     =   {}
                newfilterDict   =   {"title":title, "code": "( " + newfilter + " )"}
                filtersDict.update({"0":newfilterDict})
            else :
                fid  =   len(filtersDict)
                title   =   "filter " + str(len(filtersDict))
                newfilterDict   =   {"title":title, "code": "( " + newfilter + " )"}
                filtersDict.update({str(fid):newfilterDict})
            
            cfg.set_config_value(cfg.CURRENT_SUBSET_FILTERS,filtersDict)
            
            filter_keys =   list(filtersDict)
            
            filter_keys.sort()
            
            newcriteria     =   ""
            
            for i in range(len(filter_keys)) :
                if(not(i==0)) :
                    newcriteria     =   newcriteria + " & " + new_line
                
                cfilter     =  filtersDict.get(filter_keys[i]) 
                newcriteria     =   newcriteria + cfilter.get("code")

            #newcriteria     =   newcriteria + "()"

            cfg.set_config_value(dfsw.get_subset_filter_input_id+"Parms",["","",newcriteria])
            dfsw.display_df_subset(get_subset_df(),True)
            
        elif(optionId ==  dfsm.EDIT_FILTER) :
            fparms  =   get_parms_for_input(parms,dfsw.get_subset_filters_idList)
            filtersDict     =   cfg.get_config_value(cfg.CURRENT_SUBSET_FILTERS)
            currentfilter   =   filtersDict.get(cfg.get_config_value(cfg.CURRENT_SUBSET_FILTER))
            currentfilter.update({"title":fparms[0]})
            currentfilter.update({"code":fparms[1]})
            
            cfg.set_config_value(dfsw.get_subset_filters_id+"Parms",[fparms[0],fparms[1]])
            
            dfsw.display_filters(get_subset_df())            
        
        elif(optionId ==  dfsm.DELETE_FILTER) :
            filtersDict     =   cfg.get_config_value(cfg.CURRENT_SUBSET_FILTERS)
            currentfilter   =   cfg.get_config_value(cfg.CURRENT_SUBSET_FILTER)
            filtersDict.pop(currentfilter)
            dfsw.display_filters(get_subset_df())        
        
        elif(optionId ==  dfsm.EDIT_CRITERIA) :
            dfsw.display_filters(get_subset_df())        
        
        elif(optionId ==  dfsm.SELECT_FILTER) :
            
            filtersDict     =   cfg.get_config_value(cfg.CURRENT_SUBSET_FILTERS)
            for key in filtersDict.keys() :
                if(filtersDict.get(key).get("title") == parms[0]) :
                    newparms    =   [parms[0],filtersDict.get(key).get("code")]
                    
            cfg.set_config_value(dfsw.get_subset_filters_id+"Parms",newparms)
            dfsw.display_filters(get_subset_df()) 
            
        elif(optionId ==  dfsm.GET_COLUMN_NAMES) :
            parmslist = get_parms_for_input(parms,dfsw.get_subset_filter_input_idList)
            cfg.set_config_value(dfsw.get_subset_filter_input_id+"Parms",parmslist)
            dfsw.display_df_subset(get_subset_df(),True) 
         
    else :
        
        dfsw.get_dfsubset_main_taskbar()
        
        cfg.drop_config_value(cfg.CURRENT_SUBSET_DF)
        clear_sw_utility_dfsubsetdata()
        
        cfg.display_data_select_df(cfg.SWDFSubsetUtility_ID)
            
        if(not(optionId == dfsm.DISPLAY_MAIN)) :
            cfg.display_no_dfs(cfg.SWDFSubsetUtility_ID)
        
        


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
    
    sclause             =   "(  ("
    eclause             =   ") )"
    orop                =   "or"
    andop               =   "and"
    clauseorop          =   "OR"
    clauseandop         =   "AND"
    
    current_index       =   0
    total_clauses       =   0
    max_clauses         =   40

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



def build_and_validate_search_criteria(colslist,keepflag,filters,inneropers,outeropers,opstat) :
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
    print("\nbuild_and_validate_search_criteria",colslist,keepflag,filters,inneropers,outeropers)
    
    filtersList     =   []

    df = get_subset_df()
    
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
        if(is_int_col(df,colname)) :
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

        
def get_truth_table(df_title,criteria,opstat) :
    """            
    #------------------------------------------------------------------
    #  get a dataframe criteria
    #
    #   criteria    -   criteria logic
    #   opstat      -   operation status 
    #
    #   returns :
    #     next criteria
    #------------------------------------------------------------------
    """       
    ccode   =   "from dfcleanser.common.cfg import get_dfc_dataframe_df" + new_line
    ccode   =   (ccode + "df = get_dfc_dataframe_df('" + df_title +"')" + new_line)
    ccode   =   (ccode + "from dfcleanser.sw_utilities.sw_utility_dfsubset_control import set_criteria" + new_line)
    ccode   =   (ccode + "new_criteria = " + criteria + new_line)
    ccode   =   (ccode + "set_criteria(new_criteria)" + new_line)

    try :
        
        exec(ccode)
        next_criteria = get_criteria()
        return(next_criteria)
        
    except Exception as e:
        opstat.store_exception("Error get_df_criteria ",e)

 
def dump_indexer(indexer,display_all=False) :
    """
    #------------------------------------------------------------------
    #  dump the truth values of the indexer
    #
    #   indexer         -   indexer
    #   display_all     -   display truths table and counts 
    #
    #------------------------------------------------------------------
    """
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


def get_filter_connectors(criteria) :
    """            
    #------------------------------------------------------------------
    #   get the criteria connectors
    #
    #   criteria        -   boolean criteria 
    #
    #------------------------------------------------------------------
    """
    
    fconnectors         =   []
    
    if( (criteria.find("and") > -1) or (criteria.find("or") > -1) ) :
        
        for i in range(len(criteria)) :
            if(criteria[i] == "&") :
                fconnectors.append("&")
            else :
                if(criteria[i] == "|") :
                    fconnectors.append("|")  
                    
    return(fconnectors)
            


def get_filters_criteria(criteria,opstat) :
    """            
    #------------------------------------------------------------------
    #   get the criteria for a filter
    #
    #   criteria        -   boolean criteria 
    #   opstat          -   status variable 
    #
    #------------------------------------------------------------------
    """
    
    filter_connectors   =   get_filter_connectors(criteria)
    
    filters_list        =   []
    final_filters_list  =   []
    filters_sub_list    =   []
    
    if(criteria.find("&") > -1) :
        
        filters_list    =   criteria.split("&") 
    
        for i in range(len(filters_list)) :
        
            if(filters_list[i].find("|") > -1) :
                next_sub_list    =   filters_list[i].split("|")     
                filters_sub_list.append(next_sub_list)
            else :
                filters_sub_list.append(None)
                
    else :
        
       if(criteria.find("|") > -1) :   
           filters_list    =   criteria.split("|")    
    
    if(len(filters_list) > 0) : 
        
        for i in range(len(filters_list)) :
            if(not (filters_sub_list[i] is None)) :
                for j in range(len(filters_sub_list[i])) :
                    final_filters_list.append(filters_sub_list[i][j])
            else :
                final_filters_list.append(filters_list[i]) 
    else :
        final_filters_list.append(criteria)
        
    for i in range(len(final_filters_list)) :
        final_filters_list[i]   =   final_filters_list[i].replace(" and "," & ")
        final_filters_list[i]   =   final_filters_list[i].replace(" or "," | ")
        
    return([final_filters_list,filter_connectors])       
       

def get_subset_from_criteria(df_title,filters,filters_flag,newdf_title,csv_file_name,opstat) :
    """            
    #------------------------------------------------------------------
    #   get the dataframe subset
    #
    #   df_title        -   source dataframe title
    #   criteria        -   boolean criteria 
    #   newdf           -   new df name 
    #   csv_file_name   -   file name 
    #   opstat          -   operation status 
    #
    #------------------------------------------------------------------
    """

    dfssubset_parms     =   get_filters_criteria(filters,opstat)

    import pandas as pd
    df                  =   cfg.get_dfc_dataframe_df(df_title)

    truth_table         =   pd.Series()
    truth_table_list    =   []
    final_truth         =   pd.Series()
    
    try :
        
        if(not (filters_flag)) :
            
            if(newdf_title is None) :
                df      =   df[filters]
            else :
                new_df  =   df[filters]    
            
        else : 
            
            criteria        =   dfssubset_parms[0]
            criteria_ops    =   dfssubset_parms[1]
            
            for i in range(len(criteria)) :
            
                truth_table     =    get_truth_table(df_title,criteria[i],opstat)
                truth_table_list.append(truth_table)
                
            for i in range(len(criteria)) :
                if(i==0) :
                    final_truth     =    truth_table_list[0] 
                else :
                    if(criteria_ops[(i-1)] == "&") :
                        final_truth     =    final_truth & truth_table_list[i]
                    else :
                        final_truth     =    final_truth | truth_table_list[i]
                        
            if(newdf_title is None) :
                #print("\n\nafter final truth before final apply to df")
                #print("before final_truth",type(df),len(df),len(df.columns))
                df[final_truth]
                #print("after final_truth",type(df),len(df),len(df.columns))
            else :
                #print("before final truth apply : newdf ",type(df),len(df),len(df.columns))
                new_df  =   df[final_truth].copy()
                #print("after final truth apply : newdf ",type(new_df),len(new_df),len(new_df.columns))
            
                from dfcleanser.common.cfg import dfc_dataframe,add_dfc_dataframe
                subsetparms     =   cfg.get_config_value(dfsw.get_subset_input_id + "Parms")
            
                new_dfcnotes    =   "Subset dataframe from " + subsetparms[0] + "\n criteria : \n" + filters
                new_dfcdf       =   dfc_dataframe(newdf_title,new_df,new_dfcnotes)
                add_dfc_dataframe(new_dfcdf)

            
        return(df)
        
    except Exception as e:
        opstat.store_exception("Error getting subset from citeria\n ",e)

    if(opstat.get_status()) :
        
        if(not (csv_file_name == None)) :
            
            try :
                df.to_csv(csv_file_name)
            except Exception as e:
                opstat.store_exception("Error saving subset as csv file\n ",e)
        

def get_diff_secs(then) :
    """            
    #------------------------------------------------------------------
    #   get datetime diff in secs
    #
    #   then       -   start time 
    #
    #------------------------------------------------------------------
    """  

    from datetime import datetime
    now     =   datetime.now()
    diff    =   now-then 
    then    =   now
    return(diff.total_seconds())


def get_df_subset(parms,filtered=False,display=True) :
    """            
    #------------------------------------------------------------------
    #   get dataframe subset
    #
    #   parms       -   associated col parms 
    #   filtered    -   has filters flag 
    #   display     -   display flag 
    #
    #------------------------------------------------------------------
    """  

    from datetime import datetime
    starttime   =  datetime.now()
    
    opstat  =   opStatus()

    subsetparms         =   cfg.get_config_value(dfsw.get_subset_input_id+"Parms")
    filterparms         =   dfsw.get_dfsubset_filter_input_parms(parms)
    filterparms[2]      =   filterparms[2].replace("\n","")

    if(len(subsetparms[0]) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("input_dataframe is not set")
        
    else :
        
        if(not filtered) :   
            if(len(subsetparms[2]) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("no filters and columns_names_list is not set")
        
        else :
            
            if(len(filterparms[2]) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("subset_selection_criteria is not set")
            
    if(opstat.get_status()) :
        
        if(display) :
            
            clock = RunningClock()
            clock.start()

        try :
            
            if(filtered) :
                subset_query    =   filterparms[2]
                
                if(len(subsetparms[1]) > 0) :
                    get_subset_from_criteria(subsetparms[0],subset_query,filtered,subsetparms[1],subsetparms[4],opstat)
                    out_df_title  =   subsetparms[1]
                else :
                    get_subset_from_criteria(subsetparms[0],subset_query,filtered,None,subsetparms[4],opstat)
                    out_df_title  =   subsetparms[0]
            
        except Exception :
            opstat.set_status(False)
            opstat.set_errorMsg("unable to run df subset")

        if(display) :
            clock.stop()
            
            
    if(opstat.get_status()) :
        
        col_names_list  =   subsetparms[2]  
        keep_flag       =   subsetparms[3]
        
        if(len(col_names_list) > 0) :
            col_names   =   col_names_list.split(",")
            
            if(keep_flag == "True") :
                keep    =   True
            else :
                keep    =   False
                
            df              =   cfg.get_dfc_dataframe_df(subsetparms[0])
            all_col_names   =   df.columns.tolist() 
            
            if(keep) :
                drop_columns    =   []
                for i in range(len(all_col_names)) :
                    if(not (all_col_names[i] in col_names)) :
                        
                        drop_columns.append(all_col_names[i])
            else :
                drop_columns    =  col_names 
                
            try :
                
                if(len(subsetparms[1]) > 0) :
                    
                    newdf   =   cfg.get_dfc_dataframe_df(subsetparms[1])
                    newdf   =   df.drop(drop_columns,axis=1)
                    cfg.set_dfc_dataframe(subsetparms[1],newdf)
                else :
                    df.drop(drop_columns,inplace=True,axis=1)
                    
            except Exception :
                opstat.set_status(False)
                opstat.set_errorMsg("unable to drop columns")
       
    if(opstat.get_status()) : 
        
        if(display) :
            
            cfg.drop_config_value(dfsw.get_subset_input_id+"Parms")
            dfsw.get_dfsubset_main_taskbar()

            print("\n")
            display_status("Dataframe subset retrieved successfully ")

            elapsed_time    =   get_diff_secs(starttime)
            dfsw.display_df_subset_status(out_df_title,subsetparms[4],elapsed_time,subset_query)
        
    else :
        
        if(display) :
            from IPython.display import clear_output
            clear_output()
            
            cfg.drop_config_value(dfsw.get_subset_input_id+"Parms")
            dfsw.display_df_subset(get_subset_df(),False) 
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
    from dfcleanser.common.html_widgets import delete_all_inputs, define_inputs
    define_inputs(cfg.SWDFSubsetUtility_ID,dfsm.dfsubset_inputs)
    delete_all_inputs(cfg.SWDFSubsetUtility_ID)
    clear_sw_utility_dfsubset_cfg_values()


def clear_sw_utility_dfsubset_cfg_values() :
 
    cfg.drop_config_value(cfg.CURRENT_SUBSET_FILTERS)
    cfg.drop_config_value(cfg.CURRENT_SUBSET_FILTER)
    
    cfg.drop_config_value(dfsw.get_subset_input_id+"Parms")
    cfg.drop_config_value(dfsw.get_subset_filter_input_id+"Parms")
    cfg.drop_config_value(dfsw.get_subset_filters_id+"Parms")
    
    return()




    
    
    
    
    
    
    
    
    
    
    
    



