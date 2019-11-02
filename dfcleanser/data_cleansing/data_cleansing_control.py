"""
# data_cleansing_control 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

from dfcleanser.scripting.data_scripting_control import add_to_script

import dfcleanser.common.cfg as cfg 
import dfcleanser.data_cleansing.data_cleansing_widgets as dcw
import dfcleanser.data_cleansing.data_cleansing_model as dcm

from dfcleanser.common.common_utils import (RunningClock, display_status, display_exception, is_column_in_df, 
                                            opStatus, single_quote, is_numeric_col, is_int_col, display_grid_status,
                                            display_generic_grid, get_parms_for_input, get_numeric_from_string)

from dfcleanser.common.table_widgets import (drop_owner_tables)
from dfcleanser.common.display_utils import (display_df_describe, display_df_nn_describe) 

from IPython.display import clear_output

import json

def display_data_cleansing(option,parms=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : main data cleansing processing
    * 
    * parms :
    *   option  -   display option
    *   parms   -   associated parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    clear_output()
    
    opstat  =   opStatus()

    if(not cfg.check_if_dc_init()) :
        dcw.display_no_data_heading()
        return
    
    # setup the button bar form
    dcw.display_data_cleansing_main_taskbar()
    
    if(not(parms==None)) :
        if(option == dcm.DISPLAY_COLS_OPTION) :
            
            from dfcleanser.data_inspection.data_inspection_widgets import data_inspection_df_input_idList
            fparms          =   get_parms_for_input(parms[1],data_inspection_df_input_idList)
            
            if(len(fparms) > 0) :
                selected_df     =   fparms[0]
            
                if(not (len(selected_df) == 0) ) :
                    cfg.set_config_value(cfg.CURRENT_CLEANSE_DF,selected_df)

        
    cfg.set_config_value(cfg.DATA_TYPES_FLAG_KEY,False)

    if(option == dcm.MAIN_OPTION) :
        clear_data_cleansing_data()
        cfg.display_data_select_df(cfg.DataCleansing_ID)
            
    else :
        
        if(cfg.is_a_dfc_dataframe_loaded()) :
            
            if(option == dcm.DFS_CLEANSE_COL) :

                cfg.set_config_value(cfg.CURRENT_CLEANSE_DF,cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF))
                cfg.drop_config_value(cfg.UNIQUES_FLAG_KEY)

                cfg.set_config_value(cfg.CLEANSING_COL_KEY,parms)
            
                dcw.display_col_data()

            elif(option == dcm.CHANGE_COLUMN_OPTION) :

                clock = RunningClock()
                clock.start()
            
                opstat = change_unique_col_data(cfg.get_config_value(cfg.CURRENT_CLEANSE_DF),parms)
                cfg.drop_config_value(cfg.UNIQUES_RANGE_KEY)
            
                clock.stop()
            
                if(opstat.get_status()) :
                    display_status("Column " + cfg.get_config_value(cfg.CLEANSING_COL_KEY) + " values changed successfully")
                else :
                    display_exception(opstat)                
            
                dcw.display_col_data()
            
            elif(option == dcm.FIND_COLUMN_OPTION) :
                cfg.set_config_value(cfg.UNIQUES_RANGE_KEY,parms)
                dcw.display_col_data()
        
            elif(option == dcm.GENERIC_COL_OPTION) :
                
                cfg.drop_config_value(cfg.UNIQUES_FLAG_KEY)

                if(not (parms is None)) :
                    
                    if(type(parms) == list) :
                        from dfcleanser.data_inspection.data_inspection_widgets import data_inspection_df_input_idList
                        fparms = get_parms_for_input(parms[0],data_inspection_df_input_idList)
                        cfg.set_config_value(cfg.CURRENT_CLEANSE_DF,fparms[0])

                        cfg.set_config_value(cfg.CLEANSING_COL_KEY,parms[1])
                    else :
                        cfg.set_config_value(cfg.CLEANSING_COL_KEY,parms)
            
                dcw.display_col_data()
            
            elif(option == dcm.DISPLAY_COLS_OPTION) :
                cfg.drop_config_value(cfg.UNIQUES_FLAG_KEY)
                cfg.drop_config_value(cfg.DATA_TYPES_FLAG_KEY)            
            
                cfg.drop_config_value(cfg.CLEANSING_COL_KEY)
                cfg.drop_config_value(cfg.CLEANSING_ROW_KEY)

                funcid = int(parms[0])
                
                fparms  =   get_parms_for_input(parms[1],["dcdfdataframe"])
                if(len(fparms) > 0) :
                    cfg.set_config_value(cfg.CURRENT_CLEANSE_DF,fparms[0])    
            
                if(funcid == 0) :
                
                    cols_heading_html  =   "<div>Numeric Columns</div>"

                    clock = RunningClock()
                    clock.start()

                    try :
                    
                        col_table_html  =   display_df_describe(False)
                    
                        gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
                        gridhtmls       =   [cols_heading_html,col_table_html]
    
                        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                            display_generic_grid("display-df-col-cleanser-wrapper",gridclasses,gridhtmls)
                        else :
                            display_generic_grid("display-df-col-cleanser-pop-up-wrapper",gridclasses,gridhtmls)
                        
                    except Exception as e: 
                        opstat = opStatus()
                        opstat.store_exception("Unable to display numeric column names",e)
                        display_exception(opstat)

                    clock.stop()
                
                    from dfcleanser.common.display_utils import display_pop_up_buffer
                    display_pop_up_buffer()

                elif(funcid == 1) :
                
                    cols_heading_html  =   "<div>Non Numeric Columns</div>"
                
                    clock = RunningClock()
                    clock.start()

                    try :
                    
                        nn_cols_html    =   display_df_nn_describe(False) 
                    
                        gridclasses     =   ["dfcleanser-common-grid-header","dfc-footer"]
                        gridhtmls       =   [cols_heading_html,nn_cols_html]
    
                        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                            display_generic_grid("display-df-col-cleanser-wrapper",gridclasses,gridhtmls)
                        else :
                            display_generic_grid("display-df-col-cleanser-pop-up-wrapper",gridclasses,gridhtmls)
                    
                    except Exception as e:
                        opstat = opStatus()
                        opstat.store_exception("Unable to display non numeric column names",e)
                        display_exception(opstat)

                    clock.stop()
                    
                elif(funcid == 2) :
                    cfg.set_config_value(cfg.CLEANSING_ROW_KEY,0)
                    dcw.display_row_data(cfg.get_current_chapter_df(cfg.CURRENT_CLEANSE_DF),0,0)
    
                elif(funcid == 3) :
                    return()
                
            elif(option == dcm.DISPLAY_ROW_OPTION) :
            
                rowid = int(parms)
                cfg.set_config_value(cfg.CLEANSING_ROW_KEY,parms)
                dcw.display_row_data(cfg.get_current_chapter_df(cfg.CURRENT_CLEANSE_DF),rowid,0)
            
            elif(option == dcm.DROP_COL_OPTION ) : 
            
                opstat = drop_column(cfg.get_config_value(cfg.CURRENT_CLEANSE_DF),
                                     cfg.get_config_value(cfg.CLEANSING_COL_KEY))
            
                clear_output()
            
                # setup the button bar form
                dcw.display_data_cleansing_main_taskbar()
            
                if(opstat.get_status()) :
                    display_status("Column " + cfg.get_config_value(cfg.CLEANSING_COL_KEY) + " dropped successfully")
                    cfg.drop_config_value(cfg.CLEANSING_COL_KEY)
                else :
                    display_exception(opstat)                
            
                from dfcleanser.data_inspection.data_inspection_widgets import display_df_size_data
                display_df_size_data()

            elif(option == dcm.DROP_ROWS_OPTION ) : 
                
                clock = RunningClock()
                clock.start()
            
                drop_value  =   parms[0]
            
                if(len(drop_value) > 0) :
                    opstat = drop_value_rows(cfg.get_config_value(cfg.CURRENT_CLEANSE_DF),
                                             cfg.get_config_value(cfg.CLEANSING_COL_KEY),
                                             drop_value)
                else :
                    opstat.set_status(False)
                    opstat.set_errorMsg("Invalid row value '" +  drop_value + "' entered")
            
                clock.stop()
            
                if(opstat.get_status()) :
                    display_grid_status("Rows dropped successfully")
                else :
                    display_exception(opstat)                
            
                dcw.display_col_data()

            elif(option ==  dcm.DISPLAY_ROUND_COLUMN_OPTION  ) : 
            
                df          =   cfg.get_current_chapter_df(cfg.CURRENT_CLEANSE_DF)
                colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
            
                dcw.display_round_option(df,colname)            
        
            elif(option ==  dcm.PROCESS_ROUND_COLUMN_OPTION  ) :
            
                clock = RunningClock()
                clock.start()
            
                opstat = round_column_data(cfg.get_config_value(cfg.CURRENT_CLEANSE_DF),
                                           cfg.get_config_value(cfg.CLEANSING_COL_KEY),
                                           parms)
            
                clock.stop()
            
                if(opstat.get_status()) :
                    display_status("Column " + cfg.get_config_value(cfg.CLEANSING_COL_KEY) + " rounded successfully")
                else :
                    display_exception(opstat)                
            
                dcw.display_col_data()
            
            elif(option ==  dcm.DISPLAY_COL_CHANGE_OPTION  ) :
            
                dcw.display_col_data()
            
            
            elif(option ==  dcm.DISPLAY_REM_WHTSPC_OPTION  ) : 

                df          =   cfg.get_current_chapter_df(cfg.CURRENT_CLEANSE_DF)
                colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
                dcw.display_whitespace_option(df,colname)
            
            elif(option ==  dcm.PROCESS_REM_WHTSPC_OPTION  ) :
            
                clock = RunningClock()
                clock.start()
            
                remove_whitespace(cfg.get_config_value(cfg.CURRENT_CLEANSE_DF),parms,opstat)
            
                clock.stop()
            
                if(opstat.get_status()) :
                    display_status("Column " + cfg.get_config_value(cfg.CLEANSING_COL_KEY) + " whitespace removed successfully")
                else :
                    display_exception(opstat)                
            
                dcw.display_col_data()

            elif(option ==  dcm.DISPLAY_DETAILS_OPTION  ) :
                dcw.display_col_data()
           
            elif(option ==  dcm.DISPLAY_UNIQUES_OPTION  ) :
                cfg.set_config_value(cfg.UNIQUES_RANGE_KEY,parms)
                dcw.display_col_data(True)
            
            elif(option ==  dcm.DISPLAY_NEW_ROW) :

                colname     =   parms
                cfg.set_config_value(cfg.CLEANSING_COL_KEY,colname)
                rowid       =   cfg.get_config_value(cfg.CLEANSING_ROW_KEY)
            
                df          =   cfg.get_current_chapter_df(cfg.CURRENT_CLEANSE_DF)
            
                column_names = list(df.columns.values)
            
                found = -1
                for i in range(len(column_names)) :
                    if(column_names[i] == colname) :
                        found = i
            
                if(found > -1) :
                    colid = found
                    cfg.set_config_value(cfg.CLEANSING_COL_KEY,colid)
            
                chval = df.iloc[rowid,colid]
            
            elif(option ==  dcm.UPDATE_ROW_COL) :
            
                colname     =   parms
            
                rowid       =   int(cfg.get_config_value(cfg.CLEANSING_ROW_KEY))
                df          =   cfg.get_current_chapter_df(cfg.CURRENT_CLEANSE_DF) 
            
                column_names = list(df.columns.values)
            
                found = -1
                for i in range(len(column_names)) :
                    if(column_names[i] == colname) :
                        found = i
            
                if(found > -1) :
                    colid = found
                    cfg.set_config_value(cfg.CLEANSING_COL_KEY,colid)
            
                chval = df.iloc[rowid,colid]

                cfg.set_config_value(dcw.change_row_values_input_id + "Parms",[str(chval),""])           
                dcw.display_row_data(cfg.get_current_chapter_df(cfg.CURRENT_CLEANSE_DF),rowid,0)

            elif(option ==  dcm.PROCESS_ROW_COL) :
            
                func_id     =   parms[0]
                row_id      =   int(cfg.get_config_value(cfg.CLEANSING_ROW_KEY))
            
                cfg.drop_config_value(dcw.change_row_values_input_id + "Parms")           
            
                if(func_id == 0) :
                
                    fparms      =   dcw.get_change_row_values_inputs(parms)
                    new_value   =   fparms[1]
                
                    col_id      =   int(cfg.get_config_value(cfg.CLEANSING_COL_KEY))
                
                    df          =   cfg.get_current_chapter_df(cfg.CURRENT_CLEANSE_DF)
                
                    if(is_numeric_col(df,col_id)) :
                        if(is_int_col(df,col_id)) :
                            new_value       =   int(new_value)
                        else :
                            new_value       =   float(new_value)
                
                    if(len(new_value) > 0) :
                        df.iloc[row_id,col_id] = new_value

                    dcw.display_row_data(cfg.get_current_chapter_df(cfg.CURRENT_CLEANSE_DF),row_id,0)
                
                elif(func_id == 1) :
                    drop_row(cfg.CURRENT_CLEANSE_DF,row_id)
                    dcw.display_row_data(cfg.get_current_chapter_df(cfg.CURRENT_CLEANSE_DF),0,0)

            # ----------------------------------------------------------- 
            #  na options
            # ----------------------------------------------------------- 
       
            elif(option == dcm.DISPLAY_DROPNA_OPTION ) :
            
                df          =   cfg.get_current_chapter_df(cfg.CURRENT_CLEANSE_DF)
                colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
                dcw.display_dropna_option(df,colname)
            
            elif(option ==  dcm.DISPLAY_FILLNA_OPTION ) :
            
                df          =   cfg.get_current_chapter_df(cfg.CURRENT_CLEANSE_DF)
                colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
                dcw.display_fillna_option(df,colname)




            elif(option == dcm.PROCESS_DROP_NA_OPTION ) :
            
                print("PROCESS_DROP_NA_OPTION",parms) 
            
            
            elif(option ==  dcm.PROCESS_FILLNA_OPTION) :
            
                print("PROCESS_FILLNA_OPTION",parms)
            
            elif(option ==  dcm.DISPLAY_DATA_TYPE_OPTION) :
            
                print("dcm.DISPLAY_DATA_TYPE_OPTION",parms) 
            
                df          =   cfg.get_current_chapter_df(cfg.CURRENT_CLEANSE_DF)
                colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
            
                from dfcleanser.data_transform.data_transform_columns_widgets import display_convert_datatype
                display_convert_datatype(df,colname,True,False,cfg.DataCleansing_ID)

            elif(option ==  dcm.PROCESS_DATA_TYPE_OPTION) :
                print("dcm.PROCESS_DATA_TYPE_OPTION",parms) 
            

        else :
            
            cfg.drop_config_value(cfg.CURRENT_CLEANSE_DF)
            clear_data_cleansing_data()
            
            cfg.display_data_select_df(cfg.DataCleansing_ID)
            
            if(not(option == dcm.MAIN_OPTION)) :
                cfg.display_no_dfs(cfg.DataCleansing_ID)

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    data cleansing process data functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def drop_column(dftitle,colname,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : drop a specific col
    * 
    * parms :
    *  dftitle     -   dataframe title
    *  colname     -   column name
    *  display     -   boolean display
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    droplist    =   []
    droplist.append(colname)
    
    df  =   cfg.get_dfc_dataframe_df(dftitle) 
    
    opstat = opStatus()
    
    try :
        df.drop(droplist,axis=1,inplace=True)
        
        if(display) :
            #make scriptable
            add_to_script(["# Drop Column " + colname,
                           "from dfcleanser.data_cleansing.data_cleansing_control import drop_column",
                           "drop_column(" + single_quote(dftitle) + ","  + single_quote(colname)  + ")"],opstat)
        
    except Exception as e:
        opstat.store_exception("Unable to drop column " + cfg.get_config_value(cfg.CLEANSING_COL_KEY),e)
        
    return(opstat)


def drop_value_rows(dftitle,colname,value,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : drop rows for column value
    * 
    * parms :
    *   dftitle         -   dataframe title
    *   colname         -   column to drop 
    *   value           -   column value to match
    *   display         -   true  : add to script log : 
    *                       false : running from script log 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat      =   opStatus()
    
    df  =   cfg.get_dfc_dataframe_df(dftitle)    
    if(value == "nan") :

        df.dropna(subset=[colname],inplace=True)
        df.reset_index(inplace=True)
        
    else :
        
        droplist    =   []
        
        #TODO change using indexer
        dfcoldata = df[colname].tolist()
        isnumeric = is_numeric_col(df,colname)
    
        for i in range(len(dfcoldata)) :
            if(isnumeric) :
                if(str(dfcoldata[i]) == value) :
                    droplist.append(i)
            else :
                if(dfcoldata[i] == value) :
                    droplist.append(i)    

        if(len(droplist) > 0) :
        
            try :
                df.drop(droplist,axis=0,inplace=True)
                df.reset_index(inplace=True)
            
                if(display) :
                    #make scriptable
                    add_to_script(["# Drop Values ",
                                   "from dfcleanser.data_cleansing.data_cleansing_control import drop_value_rows",
                                   "drop_value_rows(" + single_quote(dftitle) + "," + single_quote(colname) + "," + str(value) +")"],opstat)

            except Exception as e:
                opstat.store_exception("Unable to drop row values ",e)

    return(opstat)


def drop_col_nans(dftitle,colname) :
    """
    * -------------------------------------------------------------------------- 
    * function : drop column nans
    * 
    * parms :
    *   dftitle         -   dataframe title
    *   colname         -   column to drop 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat = opStatus()
    opstat = drop_value_rows(dftitle,colname,"nan")

    return(opstat)


def drop_row(dftitle,rowid) :
    """
    * -------------------------------------------------------------------------- 
    * function : drop a specific row
    * 
    * parms :
    *   dftitle         -   dataframe title
    *   rowid           -   row to drop
    *   display         -   true  : add to script log : 
    *                       false : running from script log 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat = opStatus()
    
    df  =   cfg.get_dfc_dataframe_df(dftitle)    
    try :     
        df.drop(df.index[int(rowid)],inplace=True)
        
        #make scriptable
        add_to_script(["# Drop Row " + str(rowid),
                       "from dfcleanser.data_cleansing.data_cleansing_control import drop_row",
                       "drop_row(" + single_quote(dftitle) + "," + str(rowid) +")"],opstat)
        
    except Exception as e:
        opstat.store_exception("Unable to drop rowid  " + str(rowid),e)

    return(opstat)
 

def round_column_data(dftitle,colname,parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : drop a specific row
    * 
    * parms :
    *   dftitle         -   dataframe title
    *   colname         -   column name
    *   parms           -   list of parms
    *                          parm[0]  colname
    *                          parm[1]  number of decimals
    *   display         -   true  : add to script log : 
    *                       false : running from script log 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    
    colname     =   parms[0]
    accuracy    =   int(parms[1])
    rounds      =   {colname: accuracy}
    
    opstat = opStatus()
    
    df  =   cfg.get_dfc_dataframe_df(dftitle) 
    
    try :     

        df = df.round(rounds)

        #make scriptable
        import json
        add_to_script(["# Round Column ",
                       "from dfcleanser.data_cleansing.data_cleansing_control import round_column_data",
                       "round_column_data(" + single_quote(dftitle) + "," + single_quote(colname) + "," + json.dumps(parms) +")"],opstat)

    except Exception as e:
        opstat.store_exception("Unable to round  " + colname,e)

    return(opstat)


def fillna_column_data(dftitle,colname,parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : fillnas for a column
    * 
    * parms :
    *   dftitle         -   dataframe title
    *   colname         -   column name
    *   parms           -   list of parms
    *                          parm[0]  colname
    *                          parm[1]  fillna algorithm
    *                          parm[2]  fillna value
    *   display         -   true  : add to script log : 
    *                       false : running from script log 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    
    colname     =   parms[0]
    fillnaalg   =   parms[1]
    fillnaval   =   parms[2]

    opstat = opStatus()
    
    df  =   cfg.get_dfc_dataframe_df(dftitle)
    
    if(is_column_in_df(df,colname)) :

        if(fillnaalg == "None") :
            
            fill_method  =   None
            if(len(fillnaval) > 0) :
                if(is_numeric_col(df,colname)) :
                    nan_value   =   get_numeric_from_string(fillnaval)
                
                    if(nan_value == None) :
                        opstat.set_status(False)
                        opstat.set_errorMsg("NaN value is not valid numeric value for a numeric column")
                else :
                    nan_value   =   fillnaval
                
            else :
                opstat.set_status(False)
                opstat.set_errorMsg("invalid fillna value")
                
        else :
            
            if(fillnaalg == "mean") :
                fill_method     =   None
                nan_value       =   df[colname].mean()
                
            else :
                
                nan_value       =   None
                fill_method     =   fillnaalg
        
    else :
        opstat.set_status(False)
        opstat.set_errorMsg(colname + " not in df")
    
    if(opstat.get_status()) :
    
        try :     

            df = df[colname].fillna(nan_value,fill_method,1)
            
            #make scriptable
            import json
            add_to_script(["# fillna Column ",
                           "from dfcleanser.data_cleansing.data_cleansing_control import fillna_column_data",
                           "fillna_column_data(" + single_quote(dftitle) + ","  + single_quote(colname) + "," + json.dumps(parms) +")"],opstat)

        except Exception as e:
            opstat.store_exception("Unable to fillna  " + colname,e)

    return(opstat)


def remove_whitespace(dftitle,parms,opstat,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : remove leading and trailing blanks and tabs
    * 
    * parms :
    *   dftitle         -   dataframe title
    *   parms           -   column name
    *   display         -   true  : add to script log : 
    *                       false : running from script log 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat      =   opStatus()
    
    df          =   cfg.get_dfc_dataframe_df(dftitle) 
    
    colname     =   colname = cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    leadflag    =   parms[0] 
    whtspcopts  =   parms[1] 
    
    print("remove_whitespace",colname,leadflag,whtspcopts) 
    
    uniques     =   df[colname].unique()
    foundList   =   []
    
    try :
    
        for i in range(len(whtspcopts)) :
        
            founduniques   =   []
        
            if(whtspcopts[i] == "true") :
    
                for j in range(len(uniques)) :
                
                    index   =  uniques[j].find(dcm.whitespace_chars[i])
                
                    if(not (leadflag == "All")) :
                        lastchar =  uniques[j][(len(uniques[j])-1)]
                        if(lastchar == dcm.whitespace_chars[i]) :
                            lindex  =  len(uniques[j])-1
                        else :
                            lindex  =   -1
        
                    if(not (leadflag == "All")) :
                    
                        if( (index == 0) or (lindex == len(uniques[j])) ) :
                            founduniques.append(j)
        
                    else :
                        if(index > -1) :
                            founduniques.append(j)
                        
                if(len(founduniques) > 0) :
                    foundList.append(founduniques)
                else :
                    foundList.append(None)

    except Exception as e :
        opstat.store_exception("Unable to parse whitespace chars",e)
        
    if(opstat.get_status()) :
        
        import pandas as pd
        truth_table         =   pd.Series()
        
        try :
                
            # go though the found list 
            for i in range(len(foundList)) :
        
                if(not(foundList[i] is None)) :
            
                    criteria   =   ""
            
                    for j in range(len(foundList[i])) :
                
                        if(not (j ==0)) :
                            criteria   =   criteria + " or "
                    
                        criteria   =   (criteria + "(df['" + colname + "'] == '" + uniques[foundList[i][j]] + "')")
                
                    from dfcleanser.sw_utilities.sw_utility_dfsubset_control import get_truth_table
                    truth_table     =   get_truth_table(dftitle,criteria,opstat)

                    if(not (leadflag == "All")) :
                        df[truth_table].replace(dcm.whitespace_chars[i],"")
                    else :
                        df[truth_table].lstrip(dcm.whitespace_chars[i])
                        df[truth_table].rstrip(dcm.whitespace_chars[i])

        except Exception as e :
            opstat.store_exception("Unable to remove whitespace from  " + colname,e)

    if(opstat.get_status()) :
               
        #make scriptable
        add_to_script(["# Remove Whitespace for " + colname,
                       "from dfcleanser.data_cleansing.data_cleansing_control remove_whitespace",
                       "remove_whitespace(" + single_quote(dftitle) + "," + json.dumps(parms) +",False)"],opstat)
                
    return(opstat)
                

def change_unique_col_data(dftitle,parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : change unique vals for a column
    * 
    * parms :
    *   dftitle         -   dataframe title
    *   parms           -   associated col parms
    *   display         -   true  : add to script log : 
    *                       false : running from script log 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat = opStatus()
    
    df  =   cfg.get_dfc_dataframe_df(dftitle) 

    if(type(parms) != str) :

        colname     =   parms[0]
        changefrom  =   parms[1]
        changeto    =   parms[2]

        if(changefrom == 'nan') :

            try :
                if(is_numeric_col(df,colname)) :
                    if(is_int_col(df,colname)) :
                        toval       =   int(changeto)
                    else :
                        toval       =   float(changeto)
                else :
                    toval       =   changeto
                    
                df.fillna({colname : toval},axis=1,inplace=True)
                
            except Exception as e :
                opstat.store_exception("Unable to change value for " + colname,e) 
                
        else :
            
            try     :
                if(is_numeric_col(df,colname)) :
                    if(is_int_col(df,colname)) :
                        fromval     =   int(changefrom)
                        toval       =   int(changeto)
                    else :
                        fromval     =   float(changefrom)
                        toval       =   float(changeto)
                else :
                    fromval     =   changefrom
                    toval       =   changeto   

                criteria        =   df[colname] == fromval    
                df[criteria]    =   toval
                
            except Exception as e :
                opstat.store_exception("Unable to change value for " + colname,e)            
        
    if(opstat.get_status()) :
        
        #make scriptable
        add_to_script(["# Change Unique Column Data ",
                       "from dfcleanser.data_cleansing.data_cleansing_control import change_unique_col_data",
                       "change_unique_col_data(" + single_quote(dftitle) + "," + json.dumps(parms) +",False)"],opstat)

    return(opstat)  
   
   
"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   general housekeeping functions
#------------------------------------------------------------------
#------------------------------------------------------------------
""" 
def clear_data_cleansing_data() :
    
    drop_owner_tables(cfg.DataCleansing_ID)
    from dfcleanser.common.html_widgets import delete_all_inputs, define_inputs
    define_inputs(cfg.DataCleansing_ID,dcw.datacleansing_inputs)
    delete_all_inputs(cfg.DataCleansing_ID)
    clear_data_cleansing_cfg_values()
    
def clear_data_cleansing_cfg_values(allValues=True) :
    
    cfg.drop_config_value(cfg.CURRENT_CLEANSE_DF) 
    cfg.drop_config_value(cfg.UNIQUES_FLAG_KEY)
    cfg.drop_config_value(cfg.UNIQUES_RANGE_KEY)
    cfg.drop_config_value(cfg.DATA_TYPES_FLAG_KEY)
    
    if(allValues) :
        cfg.drop_config_value(cfg.CLEANSING_COL_KEY)
    cfg.drop_config_value(cfg.CLEANSING_ROW_KEY)
    
    cfg.drop_config_value("changerowinputParms")
    cfg.drop_config_value(dcw.col_round_input_id+"Parms")
    cfg.drop_config_value(dcw.change_values_input_id+"Parms")
    cfg.drop_config_value(dcw.nn_change_values_input_id+"Parms")
    cfg.drop_config_value(dcw.change_row_values_input_id+"Parms")

      

