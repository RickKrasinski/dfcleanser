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

from dfcleanser.common.common_utils import (display_exception, display_status, opStatus, get_parms_for_input,  
                                            is_numeric_col, is_numeric_col_int, single_quote, RunningClock)

   
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   main taskbar and route function
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_subset_df() :
    return(cfg.get_dfc_dataframe())



def display_dfsubset_utility(optionId,parms=None) :

    if(cfg.is_a_dfc_dataframe_loaded()) :
        
        from IPython.display import clear_output
        clear_output()
    
        if(optionId == dfsw.DISPLAY_MAIN) :
            dfsw.get_dfsubset_main_taskbar()
            clear_sw_utility_dfsubsetdata()
    
        if(optionId == dfsw.DISPLAY_GET_SUBSET) :
            parmslist = dfsw.get_dfsubset_input_parms(parms)
            if(len(parmslist) > 0) :
                cfg.set_config_value(dfsw.get_subset_input_id+"Parms",parmslist)
            dfsw.display_df_subset(get_subset_df(),False) 
        
        elif(optionId ==  dfsw.PROCESS_GET_SUBSET) :
            parmslist = dfsw.get_dfsubset_input_parms(parms)
            if(len(parmslist) > 0) :
                cfg.set_config_value(dfsw.get_subset_input_id+"Parms",parmslist)
            get_df_subset(parms)
            
        elif(optionId ==  dfsw.DISPLAY_GET_SUBSET_FILTER) :
            parmslist = dfsw.get_dfsubset_input_parms(parms)
            if(len(parmslist) > 0) :
                cfg.set_config_value(dfsw.get_subset_input_id+"Parms",parmslist)
            dfsw.display_df_subset(get_subset_df(),True) 

        elif(optionId ==  dfsw.DISPLAY_GET_COL_VALUES) :
            dfsw.display_df_subset(get_subset_df(),True,parms) 

        elif(optionId ==  dfsw.PROCESS_GET_SUBSET_FILTERED) :
            get_df_subset(parms,True)
        
        elif(optionId ==  dfsw.DISPLAY_FILTERS) :
            dfsw.display_filters(get_subset_df())

        elif(optionId ==  dfsw.ADD_FILTER) :

            colname     =   parms[0]
            newfilter   =   parms[1]
            newfilter   =   newfilter.lstrip("(")
            
            filtersDict     =   cfg.get_config_value(cfg.CURRENT_SUBSET_FILTERS)
            
            if(filtersDict == None) :
                title   =   colname + " - filter 0"
                filtersDict     =   {}
                newfilterDict   =   {"title":title, "code":newfilter}
                filtersDict.update({"0":newfilterDict})
            else :
                fid  =   len(filtersDict)
                title   =   colname + " - filter " + str(len(filtersDict))
                newfilterDict   =   {"title":title, "code":newfilter}
                filtersDict.update({str(fid):newfilterDict})
            
            cfg.set_config_value(cfg.CURRENT_SUBSET_FILTERS,filtersDict)

            criteria    =   cfg.get_config_value(dfsw.get_subset_filter_input_id+"Parms")
            if(criteria == None) :
                newcriteria = "( " + title + " )"
            else :
                newcriteria = criteria[4] + " AND \n" + "( " + title + " )"
                
            #newcriteria         =   criteria.replace(newfilter,title)
            cfg.set_config_value(dfsw.get_subset_filter_input_id+"Parms",["","","","",newcriteria])
            dfsw.display_df_subset(get_subset_df(),True)
            
        elif(optionId ==  dfsw.EDIT_FILTER) :
            fparms  =   get_parms_for_input(parms,dfsw.get_subset_filters_idList)
            filtersDict     =   cfg.get_config_value(cfg.CURRENT_SUBSET_FILTERS)
            currentfilter   =   filtersDict.get(cfg.get_config_value(cfg.CURRENT_SUBSET_FILTER))
            currentfilter.update({"title":fparms[0]})
            currentfilter.update({"code":fparms[1]})
            
            cfg.set_config_value(dfsw.get_subset_filters_id+"Parms",[fparms[0],fparms[1]])
            
            dfsw.display_filters(get_subset_df())            
        
        elif(optionId ==  dfsw.DELETE_FILTER) :
            filtersDict     =   cfg.get_config_value(cfg.CURRENT_SUBSET_FILTERS)
            currentfilter   =   cfg.get_config_value(cfg.CURRENT_SUBSET_FILTER)
            filtersDict.pop(currentfilter)
            dfsw.display_filters(get_subset_df())        
        
        elif(optionId ==  dfsw.EDIT_CRITERIA) :
            print("EDIT_CRITERIA",parms)
            dfsw.display_filters(get_subset_df())        
        
        elif(optionId ==  dfsw.SELECT_FILTER) :
            
            filtersDict     =   cfg.get_config_value(cfg.CURRENT_SUBSET_FILTERS)
            for key in filtersDict.keys() :
                if(filtersDict.get(key).get("title") == parms[0]) :
                    newparms    =   [parms[0],filtersDict.get(key).get("code")]
                    
            cfg.set_config_value(dfsw.get_subset_filters_id+"Parms",newparms)
            dfsw.display_filters(get_subset_df())            
         
    else :
        dfsw.get_dfsubset_main_taskbar()
        if(not(optionId == dfsw.DISPLAY_MAIN)) :
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

    df = cfg.get_dfc_dataframe()
    
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

        
def get_df_criteria(criteria,opstat) :
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
    ccode   =   "from dfcleanser.common.cfg import get_dfc_dataframe" + new_line
    ccode   =   (ccode + "df = get_dfc_dataframe()" + new_line)
    ccode   =   (ccode + "from dfcleanser.sw_utilities.sw_utility_dfsubset_widgets import set_criteria" + new_line)
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



def build_boolean_criteria(df,filters,inneropers,outeropers,opstat) :
    """            
    #------------------------------------------------------------------
    #   build boolean search criteria
    #
    #   df          -   dataframe
    #   filters     -   filters 
    #   inneropers  -   inner operators 
    #   outeropers  -   outer operators 
    #   opstat      -   operation status 
    #
    #------------------------------------------------------------------
    """
    from datetime import datetime
    ctime   =  datetime.now()
    
    filterscriteriaList     =   []
    
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
                nextcriteria    =   get_df_criteria("( df[" + single_quote(colname) + "] " + otheroperslist[j] + " " + str(colval) + " )",opstat)
                
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
        
        print("build_boolean_criteria : after get criteria list",df.shape,str(datetime.now()),get_diff_secs(ctime))
        
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
                    
        print("build_boolean_criteria : after build indexer",df.shape,str(datetime.now()),get_diff_secs(ctime))
        
        #print("\n\nfinal_criteria",opstat.get_status())
        #dump_indexer(final_criteria)
        print("build_boolean_criteria : after dump indexer",df.shape,str(datetime.now()),get_diff_secs(ctime))

        return(final_criteria) 
        
    except Exception as e:
        opstat.store_exception("Error build_boolean_criteria ",e)
        return(None)
        

def get_subset_from_criteria(df,criteria,csv_file_name,opstat) :
    """            
    #------------------------------------------------------------------
    #   get the dataframe subset
    #
    #   df              -   dataframe
    #   criteria        -   boolean criteria 
    #   csv_file_name   -   file name 
    #   opstat          -   operation status 
    #
    #------------------------------------------------------------------
    """
    from datetime import datetime
    
    try :
        print("get_subset_from_criteria : start",df.shape,str(datetime.now()))
        df = df[criteria]
        print("get_subset_from_criteria : end",df.shape,str(datetime.now()))

        if(not (csv_file_name == None)) :
            df.to_csv(csv_file_name)
            
        return(df)
        
    except Exception as e:
        opstat.store_exception("Error getting subset from citeria\n ",e)


def get_diff_secs(then) :
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

    print("get_df_subset",parms)

    timeit  =   True
    
    dfsparms    =   cfg.get_config_value(dfsw.get_subset_input_id+"Parms")
    df          =   cfg.get_dfc_dataframe(dfsparms[0])
    
    if(timeit) :
        from datetime import datetime
        starttime   =  datetime.now()
        if(timeit) : print("\nget_df_subset : start",df.shape,str(starttime),"\n")

    opstat  =   opStatus()

    # get the subset control parms
    filter_parms    =   []
    no_filters      =   True
    
    col_names       =   []
    
    if(not filtered) :
        subsetparms     =   dfsw.get_dfsubset_input_parms(parms)
        cfg.set_config_value(dfsw.get_subset_input_id+"Parms",subsetparms)
    else :
        subsetparms     =   cfg.get_config_value(dfsw.get_subset_input_id+"Parms")
        criteria        =   dfsw.get_dfsubset_filter_input_parms(parms)[4]
        criteria        =   criteria.replace('\n',' ')

        filtersDict     =   cfg.get_config_value(cfg.CURRENT_SUBSET_FILTERS)
            

        for key in filtersDict.keys():  
            
            sfilter         =   filtersDict.get(key)

            criteria        =   criteria.replace(sfilter.get("title"),sfilter.get("code"))
            final_criteria  =   criteria

        filter_parms    =   parse_subset_filters(criteria,opstat)

    if( (subsetparms == None) or (len(subsetparms) == 0) ):
        col_names       =   None
        keep_flag       =   True
        csv_file_name   =   None
    else :
        
        col_names = cfg.get_cfg_parm_from_input_list(dfsw.get_subset_input_id,
                                                     "column_names_list",
                                                     dfsw.get_subset_input_labelList)
        
        if(len(col_names) > 0) :  
            col_names   =   col_names.rstrip(" ")
            col_names   =   col_names.lstrip(" ")
            col_names   =   col_names.replace("'","")
            col_names   =   col_names.split(",")
            
            for i in range(len(col_names)) :
                #col_names[i]    =   col_names[i].replace("'","")
                col_names[i]    =   col_names[i].rstrip(" ")
                col_names[i]    =   col_names[i].lstrip(" ")        
        else :
            col_names   =   None

        keepflag = cfg.get_cfg_parm_from_input_list(dfsw.get_subset_input_id,
                                                    "keep_column_names_flag",
                                                    dfsw.get_subset_input_labelList)
        keep_flag   =   True
        if(not (keepflag == None)) :
            if(len(keepflag) > 0) :
                if(keepflag == "False") :
                    keep_flag       =   False
        
        filename = cfg.get_cfg_parm_from_input_list(dfsw.get_subset_input_id,
                                                    "csv_file_name",
                                                    dfsw.get_subset_input_labelList)
        if(len(filename) > 0) :
            csv_file_name   =   filename
        else : 
            csv_file_name   =   None
        
    if(len(filter_parms) > 0) :   
        no_filters  =   False
    
    if(timeit) :    print("\nget_df_subset : get filter parms",df.shape,get_diff_secs(starttime),no_filters)

    if(opstat.get_status()) :
    
        if(display) :
            clock = RunningClock()
            clock.start()
    
        try :

            if(opstat.get_status()) :
                if(timeit) :    print("get_df_subset : drop cols ",df.shape,get_diff_secs(starttime))
                # dfrop cols if requested
                if(not (col_names == None)) :
                    if(len(col_names) > 0) :
                        drop_columns    =   []
                        
                        if(keep_flag) :

                            columns = df.columns.tolist()

                            for i in range(len(columns)) :
                                if(not(columns[i] in col_names)) :
                                    drop_columns.append(columns[i])
                                    
                        else :
                            drop_columns = col_names
                            
                        for i in range(len(drop_columns)) :
                            df = df.drop([drop_columns[i]],axis=1)#,inplace=True)
                            
                        if(timeit) :    print("get_df_subset : after drop cols ",df.shape,get_diff_secs(starttime))
                
                if(not (no_filters)) :
                    if(timeit) :    print("get_df_subset : build_and_validate_search_criteria",df.shape,get_diff_secs(starttime))
                    goodFilters = build_and_validate_search_criteria(col_names,
                                                                     keep_flag,
                                                                     filter_parms[0],
                                                                     filter_parms[1],
                                                                     filter_parms[2],
                                                                     opstat) 
                    if(timeit) :    print("get_df_subset : after build_and_validate_search_criteria",df.shape,get_diff_secs(starttime))
                    if(opstat.get_status()) :
                
                        if(timeit) :    print("get_df_subset : build_boolean_criteria ",df.shape,get_diff_secs(starttime))
                        criteria = build_boolean_criteria(df,goodFilters,filter_parms[1],filter_parms[2],opstat) 
                        if(timeit) :    print("get_df_subset : after build_boolean_criteria ",df.shape,get_diff_secs(starttime))
                        
                        if(opstat.get_status()) :
                            
                            if(timeit) :    print("get_df_subset : get_subset_from_criteria",df.shape,get_diff_secs(starttime))
                            df = get_subset_from_criteria(df,criteria,csv_file_name,opstat)
                            if(timeit) :    print("get_df_subset : after get_subset_from_criteria",df.shape,get_diff_secs(starttime))

        except Exception as e:
            opstat.store_exception("Error processing dataframe subset ",e)

        if(display) :
            clock.stop()

    
    if(timeit) :    print("\nget_subset_data end",df.shape,get_diff_secs(starttime),"\n")
       
    if(opstat.get_status()) : 
        
        out_df = cfg.get_cfg_parm_from_input_list(dfsw.get_subset_input_id,
                                                  "output_dataframe",
                                                   dfsw.get_subset_input_labelList)

        if(len(out_df) > 0) :
            outdf   =   cfg.dfc_dataframe(out_df,df)
            cfg.add_dfc_dataframe(outdf)
        else :
            out_df = cfg.get_cfg_parm_from_input_list(dfsw.get_subset_input_id,
                                                      "input_dataframe",
                                                      dfsw.get_subset_input_labelList)
            outdf   =   cfg.dfc_dataframe(out_df,df)
            cfg.add_dfc_dataframe(outdf)
        
        if(display) :
            cfg.drop_config_value(dfsw.get_subset_input_id+"Parms")
            dfsw.get_dfsubset_main_taskbar()

            print("\n")
            display_status("Dataframe subset retrieved successfully ")
            if(not(no_filters)) :
                filters = final_criteria
            else :
                filters = None
                
            dfsw.display_df_subset_status(df,outdf.get_title(),csv_file_name,filters)
        
    else :
        
        if(display) :
            from IPython.display import clear_output
            if(not timeit) :    clear_output()
        
            cfg.drop_config_value(dfsw.get_subset_input_id+"Parms")
            dfsw.display_df_subset(cfg.get_dfc_dataframe(),False) 
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
 
    cfg.drop_config_value(cfg.CURRENT_SUBSET_FILTERS)
    cfg.drop_config_value(cfg.CURRENT_SUBSET_FILTER)
    
    cfg.drop_config_value(dfsw.get_subset_input_id+"Parms")
    cfg.drop_config_value(dfsw.get_subset_filter_input_id+"Parms")
    cfg.drop_config_value(dfsw.get_subset_filters_id+"Parms")
    
    return()




    
    
    
    
    
    
    
    
    
    
    
    



