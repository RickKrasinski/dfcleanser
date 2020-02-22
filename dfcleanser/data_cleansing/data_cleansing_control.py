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

import pandas as pd

from dfcleanser.scripting.data_scripting_control import add_to_script

import dfcleanser.common.cfg as cfg 
import dfcleanser.data_cleansing.data_cleansing_widgets as dcw
import dfcleanser.data_cleansing.data_cleansing_model as dcm

from dfcleanser.common.common_utils import (RunningClock, display_status, display_exception, is_column_in_df, 
                                            opStatus, is_numeric_col, is_int_col, display_grid_status,display_status_note,
                                            display_generic_grid, get_parms_for_input, get_numeric_from_string)

from dfcleanser.common.table_widgets import (drop_owner_tables)

from dfcleanser.data_transform.data_transform_columns_control import display_category_status

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
    
    from dfcleanser.common.html_widgets import define_inputs, are_owner_inputs_defined
    if(not (are_owner_inputs_defined(cfg.DataCleansing_ID)) ) :
        define_inputs(cfg.DataCleansing_ID,dcw.datacleansing_inputs)

    if(option == dcm.MAIN_OPTION) :
        dcw.display_dfc_cleansing_main()
        clear_data_cleansing_data()
    else :
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

    if(cfg.is_a_dfc_dataframe_loaded()) :
            
        if(option == dcm.DFS_CLEANSE_COL) :

            cfg.set_config_value(cfg.CURRENT_CLEANSE_DF,cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF))
            cfg.drop_config_value(cfg.UNIQUES_FLAG_KEY)

            cfg.set_config_value(cfg.CLEANSING_COL_KEY,parms)
            
            dcw.display_col_data()

        elif(option == dcm.CHANGE_COLUMN_OPTION) :

            clock = RunningClock()
            clock.start()
            opstat = change_unique_col_data(parms)
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
            
        elif(option == dcm.GENERIC_COLUMN_OPTION) :
                
            cfg.set_config_value(cfg.CLEANSING_COL_KEY,parms)
            dcw.display_col_data()                
        
        elif(option == dcm.CLEANSE_CURRENT_CATEGORY_COLUMN) :
                
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
                
                clock = RunningClock()
                clock.start()
                dcw.display_numeric_cols()
                clock.stop()

            elif(funcid == 1) :
                
                clock = RunningClock()
                clock.start()
                dcw.display_non_numeric_cols()
                clock.stop()
                    
            elif(funcid == 2) :
                    
                cfg.set_config_value(cfg.CLEANSING_ROW_KEY,0)
                dcw.display_row_data(cfg.get_current_chapter_df(cfg.DataCleansing_ID),0,0)
    
            elif(funcid == 3) :
                return()
                
        elif(option == dcm.DISPLAY_ROW_OPTION) :
            
            rowid = int(parms)
            cfg.set_config_value(cfg.CLEANSING_ROW_KEY,parms)
            dcw.display_row_data(cfg.get_current_chapter_df(cfg.DataCleansing_ID),rowid,0)
            
        elif(option == dcm.DROP_COL_OPTION ) : 
                    
            df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
            colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
            num_status  =   is_numeric_col(df,colname)
            
            opstat = drop_column()
                
            clear_output()
            
            # setup the button bar form
            dcw.display_data_cleansing_main_taskbar()
            
            print("\n")
                
            if(opstat.get_status()) :
                display_status("Column '" + cfg.get_config_value(cfg.CLEANSING_COL_KEY) + "' dropped successfully")
                cfg.drop_config_value(cfg.CLEANSING_COL_KEY)
                    
                if(num_status) :
                    dcw.display_numeric_cols()
                else :
                    dcw.display_non_numeric_cols()
                    
            else :
                display_exception(opstat)
                dcw.display_col_data()                    
                
        elif(option == dcm.DROP_ROWS_OPTION ) : 
                
            clock = RunningClock()
            clock.start()
            drop_value  =   parms[0]
            
            if(len(drop_value) > 0) :
                opstat = drop_value_rows(drop_value)
            else :
                opstat.set_status(False)
                opstat.set_errorMsg("Invalid drop row value '" +  drop_value + "' entered")
            
            clock.stop()
                
            print("\n")
            
            if(opstat.get_status()) :
                display_grid_status("Rows dropped successfully")
            else :
                display_exception(opstat)                
            
            dcw.display_col_data()

        elif(option ==  dcm.DISPLAY_ROUND_COLUMN_OPTION  ) : 
            dcw.display_round_option()            
        
        elif(option ==  dcm.PROCESS_ROUND_COLUMN_OPTION  ) :
            
            clock = RunningClock()
            clock.start()
            opstat = round_column_data(parms)
            clock.stop()
                
            print("\n")
            
            if(opstat.get_status()) :
                display_status("Column " + cfg.get_config_value(cfg.CLEANSING_COL_KEY) + " rounded successfully")
            else :
                display_exception(opstat)                
            
            dcw.display_col_data()
            
        elif(option ==  dcm.DISPLAY_COL_CHANGE_OPTION  ) :
            dcw.display_col_data()
            
        elif(option ==  dcm.DISPLAY_REM_WHTSPC_OPTION  ) : 
            dcw.display_whitespace_option()
            
        elif(option ==  dcm.PROCESS_REM_WHTSPC_OPTION  ) :
            
            clock = RunningClock()
            clock.start()
            opstat  =   remove_whitespace(parms)
            clock.stop()
            
            if(opstat.get_status()) :
                display_status("Column " + cfg.get_config_value(cfg.CLEANSING_COL_KEY) + " whitespace removed successfully")
            else :
                display_exception(opstat)                
            
            dcw.display_col_data()

        elif(option ==  dcm.DISPLAY_DETAILS_OPTION  ) :
            dcw.display_col_data()
           
        elif(option ==  dcm.DISPLAY_UNIQUES_OPTION  ) :
                
            df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
            colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
                
            if(not (parms is None) ) :
                if(is_numeric_col(df,colname)) :
                    fparms  =   get_parms_for_input(parms,dcw.find_values_input_idList)
                else :
                    fparms  =   get_parms_for_input(parms,dcw.nn_find_values_input_idList)
                    
                cfg.set_config_value(cfg.UNIQUES_RANGE_KEY,fparms)
                    
            dcw.display_col_data(True)
            
        elif(option ==  dcm.DISPLAY_NEW_ROW) :

            colname     =   parms
            cfg.set_config_value(cfg.CLEANSING_COL_KEY,colname)
            rowid       =   cfg.get_config_value(cfg.CLEANSING_ROW_KEY)
            
            df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
            
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
            df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID) 
            
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
                dcw.display_row_data(cfg.get_current_chapter_df(cfg.DataCleansing_ID),rowid,0)

        elif(option ==  dcm.PROCESS_ROW_COL) :
            
            func_id     =   parms[0]
            row_id      =   int(cfg.get_config_value(cfg.CLEANSING_ROW_KEY))
            
            cfg.drop_config_value(dcw.change_row_values_input_id + "Parms")           
            
            if(func_id == 0) :
                
                fparms      =   dcw.get_change_row_values_inputs(parms)
                new_value   =   fparms[1]
                
                col_id      =   int(cfg.get_config_value(cfg.CLEANSING_COL_KEY))
                
                df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
                
                if(is_numeric_col(df,col_id)) :
                    if(is_int_col(df,col_id)) :
                        new_value       =   int(new_value)
                    else :
                        new_value       =   float(new_value)
                
                if(len(new_value) > 0) :
                    df.iloc[row_id,col_id] = new_value

                dcw.display_row_data(cfg.get_current_chapter_df(cfg.DataCleansing_ID),row_id,0)
                
            elif(func_id == 1) :
                drop_row(row_id)
                dcw.display_row_data(cfg.get_current_chapter_df(cfg.DataCleansing_ID),0,0)

        # ----------------------------------------------------------- 
        #  na options
        # ----------------------------------------------------------- 
       
        elif(option == dcm.PROCESS_DROPNA_ROWS_OPTION ) :
                
            clock = RunningClock()
            clock.start()
            opstat  =   drop_col_nan_rows()
            clock.stop()
                
            print("\n")
            
            if(opstat.get_status()) :
                display_grid_status("Column '" + cfg.get_config_value(cfg.CLEANSING_COL_KEY) + "' nan rows dropped successfully.")
            else :
                display_exception(opstat)                
            
            dcw.display_col_data()

        elif(option ==  dcm.DISPLAY_FILLNA_OPTION ) :
            dcw.display_fillna_option()
            
        elif(option ==  dcm.PROCESS_FILLNA_OPTION) :
                
            clock = RunningClock()
            clock.start()
            opstat  =   fillna_column_data(parms)
            clock.stop()
                
            print("\n")
            
            if(opstat.get_status()) :
                display_grid_status("Column " + cfg.get_config_value(cfg.CLEANSING_COL_KEY) + " nan rows filled successfully.")
            else :
                display_exception(opstat)                
            
                dcw.display_col_data()
                
        elif(option ==  dcm.DISPLAY_DROPNA_OPTION ) :
            dcw.display_dropna_option()
            
        elif(option ==  dcm.PROCESS_DROPNA_OPTION) :
            
            print("PROCESS_DROPNA_OPTION")
            return()
                
            clock = RunningClock()
            clock.start()
            opstat  =   fillna_column_data(parms)
            clock.stop()
                
            print("\n")
            
            if(opstat.get_status()) :
                display_grid_status("Column " + cfg.get_config_value(cfg.CLEANSING_COL_KEY) + " nan rows filled successfully.")
            else :
                display_exception(opstat)                
            
                dcw.display_col_data()

                
        elif(option ==  dcm.DISPLAY_DATA_TYPE_OPTION) :
            
            df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
            colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
            
            from dfcleanser.data_transform.data_transform_columns_widgets import display_convert_datatype
            display_convert_datatype(df,colname,True,False,cfg.DataCleansing_ID)

        elif(option ==  dcm.PROCESS_DATA_TYPE_OPTION) :
            print("dcm.PROCESS_DATA_TYPE_OPTION",parms) 
                
        elif( (option ==  dcm.DISPLAY_ALPHANUMERIC_CHECK) or (option ==  dcm.DISPLAY_NUMERIC_CHECK) ) :
            dcw.display_check_alpha_num(option,parms[0])
                
        elif( (option ==  dcm.PROCESS_ALPHANUMERIC_CHECK) or (option ==  dcm.PROCESS_NUMERIC_CHECK) ) :
            process_chknum_compatability(option)
                
        elif( (option ==  dcm.DISPLAY_ADD_CATEGORY) or 
              (option ==  dcm.DISPLAY_REMOVE_CATEGORY) or 
              (option ==  dcm.DISPLAY_REMOVE_CATEGORY_WHITESPACE) or 
              (option ==  dcm.DISPLAY_REORDER_CATEGORY) ) :
            dcw.display_cat_option(option,parms)
                
        elif(option ==  dcm.PROCESS_RENAME_CATEGORY ) :
            process_rename_category(parms)
            dcw.display_cat_cleansing_taskbar()
            
        elif(option ==  dcm.PROCESS_ADD_CATEGORY) :
            process_add_category(parms)
            dcw.display_cat_cleansing_taskbar()
                
        elif(option ==  dcm.PROCESS_REMOVE_CATEGORY) :
            process_remove_category(parms)
            dcw.display_cat_cleansing_taskbar()
            
        elif(option ==  dcm.PROCESS_REMOVE_UNUSED_CATEGORY) :
            process_remove_unused_category(parms)
            dcw.display_cat_cleansing_taskbar()
            
        elif(option ==  dcm.PROCESS_REMOVE_CATEGORY_WHITESPACE) :
            process_remove_category_whitespace(parms)
            dcw.display_cat_cleansing_taskbar()
            
        elif(option ==  dcm.PROCESS_REORDER_CATEGORY) :
            process_reorder_category(parms)
            dcw.display_cat_cleansing_taskbar()
            
        elif(option ==  dcm.PROCESS_TOGGLE_CATEGORY_ORDER) :
            process_toggle_category_order(parms)
            dcw.display_cat_cleansing_taskbar()                

    else :
            
        cfg.drop_config_value(cfg.CURRENT_CLEANSE_DF)
            
        if(not(option == dcm.MAIN_OPTION)) :
            cfg.display_no_dfs(cfg.DataCleansing_ID)
                


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    data cleansing process options functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def drop_column() :
    """
    * -------------------------------------------------------------------------- 
    * function : drop a specific col
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    
    df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
    colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    
    droplist    =   []
    droplist.append(colname)
    
    opstat = opStatus()
    
    try :
        
        df.drop(droplist,axis=1,inplace=True)
        cfg.set_dfc_dataframe_df(cfg.get_config_value(cfg.CURRENT_CLEANSE_DF),df)
        
        print("df columns",list(df.columns))
        
        #make scriptable
        add_to_script(["# Drop Column " + colname,
                       "from dfcleanser.data_cleansing.data_cleansing_control import drop_column",
                       "drop_column()"],opstat)
        
    except Exception as e:
        opstat.store_exception("Unable to drop column " + cfg.get_config_value(cfg.CLEANSING_COL_KEY),e)
        
    return(opstat)


def drop_value_rows(value) :
    """
    * -------------------------------------------------------------------------- 
    * function : drop rows for column value
    * 
    * parms :
    *   value           -   column value to match
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat      =   opStatus()
    
    df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
    colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    
    if(value == "nan") :

        df.dropna(subset=[colname],inplace=True)
        #df.reset_index(inplace=True)
        
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
                #df.reset_index(inplace=True)
            
                #make scriptable
                add_to_script(["# Drop Values ",
                               "from dfcleanser.data_cleansing.data_cleansing_control import drop_value_rows",
                                "drop_value_rows(" + str(value) +")"],opstat)

            except Exception as e:
                opstat.store_exception("Unable to drop row values ",e)

    return(opstat)


def drop_col_nan_rows() :
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
    opstat = drop_value_rows("nan")

    return(opstat)


def drop_row(rowid) :
    """
    * -------------------------------------------------------------------------- 
    * function : drop a specific row
    * 
    * parms :
    *   rowid           -   row to drop
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat = opStatus()
    
    try : 
        
        df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)

        df.drop(df.index[int(rowid)],inplace=True)
        
        #make scriptable
        add_to_script(["# Drop Row " + str(rowid),
                       "from dfcleanser.data_cleansing.data_cleansing_control import drop_row",
                       "drop_row(" + str(rowid) +")"],opstat)
        
    except Exception as e:
        opstat.store_exception("Unable to drop rowid  " + str(rowid),e)

    return(opstat)
 

def round_column_data(parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : drop a specific row
    * 
    * parms :
    *   dftitle         -   dataframe title
    *   colname         -   column name
    *   parms           -   list of parms
    *                          parm[0]  number of decimals
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat = opStatus()
    
    df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
    colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)

    fparms      =   get_parms_for_input(parms,dcw.col_round_input_idList)
    
    if(len(fparms) > 0) :
        
        accuracy    =   int(fparms[0])
        rounds      =   {colname: accuracy}
    
        try :     

            df = df.round(rounds)

            #make scriptable
            import json
            add_to_script(["# Round Column ",
                           "from dfcleanser.data_cleansing.data_cleansing_control import round_column_data",
                           "round_column_data(" + json.dumps(parms) +")"],opstat)

        except Exception as e:
            opstat.store_exception("Unable to round  " + colname,e)

    return(opstat)


def fillna_column_data(parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : fillnas for a column
    * 
    * parms :
    *   parms           -   list of parms
    *                          parm[0]  fillna value
    *                          parm[1]  fillna algorithm
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat = opStatus()
    
    df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
    colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    
    if(is_numeric_col(df,colname)) :
        
        fparms          =   get_parms_for_input(parms,dcw.ndt_data_type_fn_input_idList)
        fillnaval       =   fparms[0]
        fillnaalg       =   fparms[1]
        fillnalimit     =   fparms[2]
        
    else :
        
        fparms      =   get_parms_for_input(parms,dcw.ndt_nn_fn_data_type_input_idList) 
        fillnaval       =   fparms[0]
        fillnalimit     =   fparms[1]
        fillnaalg       =   None
        
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
        
    try :
        
        if(len(fillnalimit) > 0) :
            fillnalimit     =   int(fparms[1])
        else :
            fillnalimit     =   None
            
    except :
        opstat.set_status(False)
        opstat.set_errorMsg("fillna limit of " + fillnalimit + " is invalid")
    
    if(opstat.get_status()) :
        
        print("fillna",nan_value,fill_method,fillnalimit)
    
        try :     

            df[colname] = df[colname].fillna(value=nan_value,method=fill_method,inplace=True,limit=fillnalimit)
            
            #make scriptable
            import json
            add_to_script(["# fillna Column ",
                           "from dfcleanser.data_cleansing.data_cleansing_control import fillna_column_data",
                           "fillna_column_data(" + json.dumps(parms) +")"],opstat)

        except Exception as e:
            opstat.store_exception("Unable to fillna  " + colname,e)

    return(opstat)


def remove_whitespace(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : remove leading and trailing blanks and tabs
    * 
    * parms :
    *   parms           -   column name
    *   display         -   true  : add to script log : 
    *                       false : running from script log 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat      =   opStatus()
    
    df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
    colname     =   colname = cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    
    leadflag    =   parms[0] 
    whtspcopts  =   parms[1] 
    
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
                    truth_table     =   get_truth_table(cfg.get_config_value(cfg.CURRENT_CLEANSE_DF),criteria,opstat)

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
                       "remove_whitespace(" + json.dumps(parms) +",False)"],opstat)
                
    return(opstat)
                

def change_unique_col_data(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : change unique vals for a column
    * 
    * parms :
    *   parms           -   associated col parms
    *   display         -   true  : add to script log : 
    *                       false : running from script log 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat = opStatus()
    
    df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
    
    fparms  =   get_parms_for_input(parms,dcw.nn_change_values_input_idList)
    
    if(len(fparms) > 0) :
        changefrom  =   fparms[0]
        changeto    =   fparms[1]
    else :
        changefrom  =   ""
        changeto    =   ""

    if((len(changefrom) >0) and (len(changeto) >0) ) :

        colname = cfg.get_config_value(cfg.CLEANSING_COL_KEY)

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
    
    else :
        opstat.set_status(False)
       
        errormsg    =   "Unable to change column values : "
        if(len(changefrom) < 1) :
            errormsg    =   errormsg + "Invalid 'current_value' of : '" + changefrom + "'"
        if(len(changeto) < 1) :
            errormsg    =    errormsg + "Invalid 'new_value' of : '" + changeto + "'"
            
        opstat.set_errorMsg(errormsg)
        
    if(display) :
        
        #make scriptable
        add_to_script(["# Change Unique Column Data ",
                       "from dfcleanser.data_cleansing.data_cleansing_control import change_unique_col_data",
                       "change_unique_col_data(" + json.dumps(parms) +",False)"],opstat)

    return(opstat)  
   

def process_chknum_compatability(option) :
    """
    * -------------------------------------------------------------------------- 
    * function : check column compatability
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
    
    print("process_chknum_compatability",option)
    
    df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
    colname     =   cfg.get_config_value(cfg.CHKNUM_COL_KEY)

    uniques     =   df[colname].unique().tolist() 
    
    compatable  =   True
    
    for i in range(len(uniques)) :
        
        try :

            if(not (uniques[i].isnan()) ) :
                
                if(option == dcm.PROCESS_ALPHANUMERIC_CHECK) :
                    
                    if(not (uniques[i].isalnum())) :
                        compatable  =   False
                        break
                    
                else :
                    
                    checkstr    =   uniques[i].replace("-","")
                    checkstr    =   checkstr.replace(".","")
                    
                    if(not (checkstr.isdigit())) :
                        compatable  =   False
                        break
            
        except :
            compatable  =   False


    if(option == dcm.PROCESS_ALPHANUMERIC_CHECK) :
        dcm.set_compatability_status(dcm.ALPHANUMERIC,colname,compatable)
    else :
        dcm.set_compatability_status(dcm.NUMERIC,colname,compatable)
    
    cols_heading_html  =   "<div>Non Numeric Columns</div>"
                
    clock = RunningClock()
    clock.start()

    try :
        from dfcleanser.common.table_widgets import get_table_value
        nn_df_describe_table = get_table_value("dcnngendfdesc")        

        #set_col_major_table_scroll(nn_df_describe_table,SCROLL_LEFT)

        #from dfcleanser.common.display_utils import display_df_nn_describe
        nn_cols_html    =   nn_df_describe_table.get_html() 
                    
        gridclasses     =   ["dfcleanser-common-grid-header","dfc-main"]
        gridhtmls       =   [cols_heading_html,nn_cols_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("display-df-col-cleanser-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("dfc-common-480px-2-vert-wrapper",gridclasses,gridhtmls,True)
                    
    except Exception as e:
        opstat = opStatus()
        opstat.store_exception("Unable to display non numeric column names",e)
        display_exception(opstat)

    clock.stop()
    
    if(compatable) :
        if(option == dcm.PROCESS_ALPHANUMERIC_CHECK) :
            display_status("Column " + colname + " can be alphanumeric column",display=True)
        else :
            display_status("Column " + colname + " can be numeric column",display=True)
            
    else :        
        if(option == dcm.PROCESS_ALPHANUMERIC_CHECK) :
            display_status("Column " + colname + " can not be alphanumeric : value = " + str(uniques[i]),display=True)
        else :
            display_status("Column " + colname + " can not be numeric : value = " + str(uniques[i]),display=True)


def process_rename_category(parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : rename a category
    * 
    * parms :
    *   parms           -   associated col parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    #print("process_rename_category",parms)
    opstat      =   opStatus()
    
    df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
    colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    
    fparms  =   get_parms_for_input(parms,dcw.cat_change_values_input_idList)
    
    fromcategory        =   fparms[0]
    tocategory          =   fparms[1]
    
    change_cat_dict     =   {fromcategory:tocategory}
    
    try :
        
        df[colname].cat.rename_categories(change_cat_dict,inplace=True)
        
    except Exception as e:
        opstat.store_exception("Unable to rename category",e)
        
    if(opstat.get_status()) :
        display_status_note("'" + colname + "'" + " category '" + fromcategory + "' renamed to '" + tocategory + "' successfully")
        display_category_status(colname)
    else :
        display_exception(opstat)


    
def process_add_category(parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : add a category
    * 
    * parms :
    *   parms           -   associated col parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    #print("process_add_category",parms)
    opstat      =   opStatus()
    
    df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
    colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    
    fparms  =   get_parms_for_input(parms,dcw.add_category_input_idList)
    
    newcategory         =   fparms[0]
    new_cat_list        =   [newcategory]
     
    try :
        
        df[colname].cat.add_categories(new_cat_list,inplace=True)
        
    except Exception as e:
        opstat.store_exception("Unable to add category",e)

    if(opstat.get_status()) :
        display_status_note("'" + colname + "'" + " category '" + newcategory + "' added successfully")
        display_category_status(colname)
    else :
        display_exception(opstat)


def process_remove_category(parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : remove a category
    * 
    * parms :
    *   parms           -   associated col parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat      =   opStatus()
    
    df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
    colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    
    fparms  =   get_parms_for_input(parms,dcw.remove_category_input_idList)
    
    remcategory  =   fparms[0]
    remcategory  =   remcategory.lstrip("[")
    remcategory  =   remcategory.rstrip("]")

    if(remcategory.find(",") > -1) :
        remcategory     =   remcategory.split(",")
    else :
        remcategory     =   [remcategory]
    
    rem_cat_list        =   []
    
    for i in range(len(remcategory)) :
        rem_cat_list.append(remcategory[i])    
    
    try :
        
        df[colname].cat.remove_categories(rem_cat_list,inplace=True)
        
    except Exception as e:
        opstat.store_exception("Unable to remove category",e)

    if(opstat.get_status()) :
        display_status_note("'" + colname + "'" + " categories " + str(remcategory) + " removed successfully")
        display_category_status(colname)
    else :
        display_exception(opstat)
 
    
def process_remove_unused_category(parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : remove unused categories
    * 
    * parms :
    *   parms           -   associated col parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat      =   opStatus()
    
    df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
    colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    
    try :
        
        df[colname].cat.remove_unused_categories(inplace=True)
        
    except Exception as e:
        opstat.store_exception("Unable to remove unused categories",e)

    if(opstat.get_status()) :
        display_status_note("'" + colname + "'" + " unused categories removed successfully")
        display_category_status(colname)
    else :
        display_exception(opstat)


def process_remove_category_whitespace(parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : remove category whitespace
    * 
    * parms :
    *   parms           -   associated col parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat      =   opStatus()
    
    df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
    colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    
    fparms      =   get_parms_for_input(parms,dcw.remove_cat_whtspc_input_idList)
    
    category    =   fparms[0]
    category    =   category.lstrip("[") 
    category    =   category.rstrip("]") 
    
    if(category.find(",") > -1 ) :
        categories    =   category.split(",")
    else :
        categories    =   [category]
    
    change_cat_dict     =   {}
    
    for i in range(len(categories)) :
        tocategory  =   categories[i].lstrip(" ")
        tocategory  =   tocategory.rstrip(" ")
        tocategory  =   tocategory.replace("\n","")
        tocategory  =   tocategory.replace("\t","")
        
        if(not (tocategory == categories[i]) ) :
            change_cat_dict.update({categories[i]:tocategory})
        
    
    if(len(change_cat_dict) == 0) :
        opstat.store_exception("category has no whitespace",None)
    else :
    
        try :
            
            df[colname].cat.rename_categories(change_cat_dict,inplace=True)
        
        except Exception as e:
            opstat.store_exception("Unable to remove category whitespace",e)

    if(opstat.get_status()) :
        display_status_note("'" + colname + "'" + "category '" + str(list(change_cat_dict.keys())) + "' whitespace removed successfully")
        display_category_status(colname)
    else :
        display_exception(opstat)


def process_reorder_category(parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : reorder category
    * 
    * parms :
    *   parms           -   associated col parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat      =   opStatus()
    
    df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
    colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    
    fparms      =   get_parms_for_input(parms,dcw.reorder_category_input_idList)
    
    orderlist   =   fparms[0]
    
    orderlist   =   orderlist.lstrip("[")
    orderlist   =   orderlist.rstrip("]")
    
    if(orderlist.find(",") > -1 ) :
        orderlist   =   orderlist.split(",")
    else :
        orderlist   =   [orderlist]
        
    corderlist  =   df[colname].cat.categories.tolist() 

    if( not (len(orderlist) == len(corderlist)) ) :  
        opstat.set_status(False)
        opstat.set_errorMsg("Reorder list is not complete")
        
    if(opstat.get_status()) :   
    
        orderflag   =   fparms[1]
    
        if(orderflag == "True") :
            orderflag   =   True
        else :
            orderflag   =   False
    
        try :
            df[colname].cat.reorder_categories(orderlist,ordered=orderflag,inplace=True)
        
        except Exception as e:
            opstat.store_exception("Unable to reorder categories",e)

    if(opstat.get_status()) :
        display_status_note(colname + " categories reordered successfully")
        display_category_status(colname)
    else :
        display_exception(opstat)


def process_toggle_category_order(parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : toggle category order attribute
    * 
    * parms :
    *   parms           -   associated col parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat      =   opStatus()
    
    df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
    colname     =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
    
    orderflag   =   df[colname].cat.ordered
    
    if(orderflag == True)  :
        orderflag = False
    else :
        orderflag = True
        
    corderlist  =   df[colname].cat.categories.tolist() 

    try :
        
        df[colname].cat.set_categories(corderlist,ordered=orderflag,inplace=True)
        
    except Exception as e:
        opstat.store_exception("Unable to toggle category order",e)

    if(opstat.get_status()) :
        display_status_note("'" + colname + "'" + " category order toggled successfully to " + str(orderflag))
        display_category_status(colname)
    else :
        display_exception(opstat)

   
"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   general housekeeping functions
#------------------------------------------------------------------
#------------------------------------------------------------------
""" 
def clear_data_cleansing_data() :
    
    drop_owner_tables(cfg.DataCleansing_ID)
    from dfcleanser.common.html_widgets import delete_all_inputs
    delete_all_inputs(cfg.DataCleansing_ID)
    clear_data_cleansing_cfg_values()
    
def clear_data_cleansing_cfg_values(allValues=True) :
    
    
    cfg.drop_config_value(cfg.UNIQUES_FLAG_KEY)
    cfg.drop_config_value(cfg.UNIQUES_RANGE_KEY)
    cfg.drop_config_value(cfg.DATA_TYPES_FLAG_KEY)

    if(allValues) :
        cfg.drop_config_value(cfg.CLEANSING_COL_KEY)
    cfg.drop_config_value(cfg.CLEANSING_ROW_KEY)
    cfg.drop_config_value(cfg.CHKNUM_COL_KEY)
    
    dcm.clear_compatability_status()

      

