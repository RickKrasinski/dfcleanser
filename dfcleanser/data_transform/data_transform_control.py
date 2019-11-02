"""
# data_transform_process 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

import json 

import dfcleanser.common.cfg as cfg

import dfcleanser.data_transform.data_transform_widgets as dtw
import dfcleanser.data_transform.data_transform_model as dtm
import dfcleanser.data_transform.data_transform_columns_widgets as dtcw
import dfcleanser.data_transform.data_transform_columns_control as dtcc
import dfcleanser.data_transform.data_transform_dataframe_control as dtdc
import dfcleanser.data_transform.data_transform_dataframe_widgets as dtdw

from dfcleanser.common.table_widgets import (dcTable, drop_owner_tables, get_table_value, SIMPLE)

from dfcleanser.common.common_utils import (display_status, display_exception, opStatus, single_quote, is_string_col,is_object_col,
                                            get_parms_for_input, RunningClock, is_datetime_col, is_datetime_type_col,
                                            get_datatype_id, is_existing_column, get_datatype_str, display_generic_grid,
                                            get_units_id, convert_df_cols, get_datatype, is_numeric_col, is_float_col)

from dfcleanser.scripting.data_scripting_control import add_to_script

from IPython.display import clear_output

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
*   main routing functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_current_transform_df(parms) :
    
    if(len(parms) > 1) :
        
        if(type(parms[1]) == str) :
        
            if(parms[1].find("dtdfdataframe") > -1)  :
                fparms          =   get_parms_for_input(parms[1],["dtdfdataframe"])
                if(len(fparms) > 0) :
                    selected_df     =   fparms[0]
            
            else :
                fparms          =   get_parms_for_input(parms[1],["didfdataframe"])
                if(len(fparms) > 0) :
                    selected_df     =   fparms[0]

            if(not (len(selected_df) == 0) ) :
                cfg.set_config_value(cfg.CURRENT_TRANSFORM_DF,selected_df)
 

def display_data_transform(option,parms=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : main data transform processing
    * 
    * parms :
    *   option  -   display option
    *   parms   -   associated parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    from IPython.display import clear_output
    clear_output()
    
    if(cfg.is_a_dfc_dataframe_loaded()) :

        # go ahead and process the command
        if(option == dtm.MAIN_OPTION) :
            if(not(parms is None)) :
                get_current_transform_df(parms)

            dtw.display_main_option(parms)
            if(parms==None) :
                clear_data_transform_data()

        else :
            
            # ----------------------------------------------
            # dataframe transform controls
            # ----------------------------------------------
            if( (option == dtm.DISPLAY_SAVE_COLUMN_NAMES_ROW) or
                (option == dtm.DISPLAY_ADD_COLUMN_NAMES_ROW) or
                (option == dtm.DISPLAY_CHANGE_COLUMN_NAMES) or
                (option == dtm.DISPLAY_SET_DF_INDEX) or
                (option == dtm.DISPLAY_RESET_DF_INDEX) or
                (option == dtm.DISPLAY_APPEND_TO_INDEX) or
                (option == dtm.DISPLAY_SORT_DF_INDEX) or
                (option == dtm.DISPLAY_DROP_DUPLICATE_ROWS) or
                (option == dtm.DF_TRANSFORM_RETURN) or
                (option == dtm.DF_TRANSFORM_HELP) ) :
                
                dtdw.display_dataframe_options(option)
                
            elif( (option == dtm.PROCESS_SAVE_COLUMN_NAMES_ROW) or
                  (option == dtm.PROCESS_ADD_COLUMN_NAMES_ROW) or
                  (option == dtm.PROCESS_CHANGE_COLUMN_NAMES) or
                  (option == dtm.PROCESS_SET_DF_INDEX) or
                  (option == dtm.PROCESS_RESET_DF_INDEX) or
                  (option == dtm.PROCESS_APPEND_TO_INDEX) or
                  (option == dtm.PROCESS_SORT_DF_INDEX) or
                  (option == dtm.PROCESS_DROP_DUPLICATE_ROWS) ) :
                
                dtdc.process_df_transform(option,parms,display=True)

            
            # ----------------------------------------------
            # column transform control
            # ----------------------------------------------
            elif( (option == dtm.MORE_TASKBAR) or
                  (option == dtm.DISPLAY_RENAME_COLUMN) or
                  (option == dtm.DISPLAY_DROP_COLUMN) or
                  (option == dtm.DISPLAY_REORDER_COLUMNS) or
                  (option == dtm.DISPLAY_MAP_COLUMN) or
                  (option == dtm.DISPLAY_DUMMIES_COLUMN) or
                  (option == dtm.DISPLAY_CAT_COLUMN) or
                  (option == dtm.DISPLAY_CLEAR_COLUMN) or
                  (option == dtm.DISPLAY_SAVE_COLUMN) or
                  (option == dtm.DISPLAY_COPY_COLUMN) or
                  (option == dtm.DISPLAY_SORT_COLUMN) or
                  (option == dtm.DISPLAY_APPLY_COLUMN) ) :
                
                print("display col transform",option)
                dtcw.display_column_transform_forms(option)
                
            elif(option == dtm.DISPLAY_APPLY_COLUMN_UPDATE) :
                dtcw.display_column_transform_forms(option,parms)
                

            elif( (option == dtm.PROCESS_RENAME_COLUMN) or
                  (option == dtm.PROCESS_DROP_COLUMN) or
                  (option == dtm.PROCESS_SAVE_COLUMN) or
                  (option == dtm.PROCESS_REORDER_COLUMNS) or
                  (option == dtm.PROCESS_COPY_COLUMN) or
                  (option == dtm.PROCESS_SORT_COLUMN) or
                  (option == dtm.PROCESS_APPLY_COLUMN) or
                  (option == dtm.PROCESS_MAP_COLUMN) or
                  (option == dtm.PROCESS_DUMMIES_COLUMN) or
                  (option == dtm.PROCESS_CAT_COLUMN) ) :
                
                print("process col transform",option)
                dtcc.process_column_option(parms)

                
            # ----------------------------------------------
            # add column controls
            # ----------------------------------------------
            elif(option == dtm.DISPLAY_ADD_COLUMN) :
                 dtcw.display_add_cols_option(option,None)
                 
            elif(option == dtm.ADD_COLUMN_CLEAR) :
                print("dtm.ADD_COLUMN_CLEAR")
                 
            elif( (option == dtm.DISPLAY_ADD_COLUMN) or     
                  (option == dtm.DISPLAY_ADD_FROM_FILE_OPTION) or
                  (option == dtm.DISPLAY_ADD_FROM_CODE_OPTION) or
                  (option == dtm.DISPLAY_ADD_FROM_DFC_FUNCS) or
                  (option == dtm.DISPLAY_ADD_FROM_DFC_FUNCS_PARMS) or
                  (option == dtm.DISPLAY_ADD_FROM_DF_OPTION) ) :
                
                dtcw.display_add_cols_option(option,parms)
            
            elif( (option == dtm.PROCESS_ADD_FROM_FILE_OPTION) or
                  (option == dtm.PROCESS_ADD_FROM_CODE_OPTION) or
                  (option == dtm.PROCESS_ADD_FROM_DFC_FUNCS) or
                  (option == dtm.PROCESS_ADD_FROM_DF_OPTION) ) :
                
                dtcc.process_add_column(parms,display=True)
                
            # ----------------------------------------------
            # datetime controls
            # ----------------------------------------------
      
            elif(option == dtm.DISPLAY_DATETIME_OPTION) :
                if(not(parms is None)) :
                    get_current_transform_df(parms)
                
                dtw.display_datetime_column_taskbar()
            
                funcid = parms[0]
            
                if( (funcid == dtm.DISPLAY_DATETIME_DATATYPE) or 
                    (funcid == dtm.DISPLAY_DATE_DATATYPE) or 
                    (funcid == dtm.DISPLAY_TIME_DATATYPE) ): 
                    dtw.display_datetime_convert(parms)
                elif(funcid == dtm.DISPLAY_TIMEDELTA) : 
                    dtw.display_datetime_timedelta(parms)
                elif(funcid == dtm.DISPLAY_DATETIME_SPLIT) :    
                    dtw.display_datetime_split_merge(parms,dtm.SPLIT)
                elif(funcid == dtm.DISPLAY_DATETIME_MERGE) : 
                    dtw.display_datetime_split_merge(parms,dtm.MERGE)
                elif(funcid == dtm.DISPLAY_DATETIME_COMPONENTS) : 
                    dtw.display_datetime_components(parms)
    
            elif(option == dtm.PROCESS_DATETIME_OPTION) :
                process_datetime_datatype_transform(parms)
            
            elif(option == dtm.PROCESS_DATETIME_TIMEDELTA_OPTION) :
                process_datetime_timedelta_transform(parms)
            
            elif(option == dtm.PROCESS_DATETIME_MERGESPLIT_OPTION) :
                process_datetime_merge_split_transform(parms)
            
            elif(option == dtm.PROCESS_DATETIME_COMPONNETS_OPTION) :
                print("dtm.PROCESS_DATETIME_COMPONNETS_OPTION",parms)
                process_get_datetime_component(parms)


            # ----------------------------------------------
            # change datetype controls
            # ----------------------------------------------
            elif(option == dtm.DISPLAY_DATATYPE_COLUMN) :
                print("display col transform",option)
                dtcw.display_column_transform_forms(option,parms)
            
            elif(option == dtm.DISPLAY_DATATYPE_CHANGE_NA) :
                print("display col transform",option)
                dtcw.display_column_transform_forms(option,parms)
                
            elif(option == dtm.DISPLAY_DATATYPE_UNIQUES) :  
                print("dtm.DISPLAY_DATATYPE_UNIQUES",parms)
                df          =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
                colname     =   cfg.get_config_value(cfg.DATA_TRANSFORM_COL_SELECTED_KEY)

                dtcw.get_uniques_display(df,colname)
    
            elif(option == dtm.DISPLAY_CHECK_COMPATABILITY) :  
                dtcw.display_column_transform_forms(option,parms)
            
            elif(option == dtm.DISPLAY_CHECK_COMPATABILITY_UNIQUES) :  
                dtcw.display_column_transform_forms(option,None)
                
            elif(option == dtm.PROCESS_CHECK_COMPATABILITY) :
                process_dfchknum_transform(parms)
                

            # ----------------------------------------------
            # external datetype change from cleansing
            # ----------------------------------------------
            elif(option == dtm.DISPLAY_DATATYPE_OPTION) :
            
                df      =   cfg.get_current_chapter_df(cfg.CURRENT_CLEANSE_DF)
                colname =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
                
                print("len display",len(df))
            
                dtcw.display_convert_datatype(df,colname,False,False,cfg.DataCleansing_ID)

            elif(option == dtm.PROCESS_DROP_NA_OPTION) :
                print("dtm.PROCESS_DROP_NA_OPTION",parms)


            elif(option == dtm.PROCESS_FILL_NA_OPTION) :
                print("dtm.PROCESS_FILL_NA_OPTION",parms)    

            elif(option == dtm.PROCESS_DATATYPE_OPTION) :            
                print("dtm.PROCESS_DATATYPE_OPTION",parms)
            
                df          =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
                colname     =   cfg.get_config_value(cfg.DATA_TRANSFORM_COL_SELECTED_KEY)
                dt          =   parms[1]
                naoption    =   int(parms[2])
            
                if(naoption == dtm.DROP_NA_OPTION) :
                
                    fparms      =   get_parms_for_input(parms[3],dtcw.dt_data_type_dn_input_idList)
                
                elif(naoption == dtm.FILL_NA_OPTION) :
                
                    if(is_numeric_col(df,colname)) :
                        print("parms",dtcw.dt_data_type_fn_input_idList)
                        fparms      =   get_parms_for_input(parms[3],dtcw.dt_data_type_fn_input_idList)
                    else :
                        fparms      =   get_parms_for_input(parms[3],dtcw.dt_nn_fn_data_type_input_idList)
                
                else :
                    fparms  =   None
            
                print("dtm.PROCESS_DATATYPE_OPTION : colname ",colname)
                print("dtm.PROCESS_DATATYPE_OPTION : dt ",dt)
                print("dtm.PROCESS_DATATYPE_OPTION : naoption ",naoption)
                print("dtm.PROCESS_DATATYPE_OPTION : fparms ",fparms)
        
    else :
        
        if(not(option == dtm.MAIN_OPTION)) :

            clear_data_transform_data()
            cfg.drop_config_value(cfg.CURRENT_TRANSFORM_DF)
            cfg.display_data_select_df(cfg.DataTransform_ID)
            
            cfg.display_no_dfs(cfg.DataTransform_ID)
            
        else :
            dtw.display_main_option(None)
            clear_data_transform_data()
            cfg.drop_config_value(cfg.CURRENT_TRANSFORM_DF)
            
            if(not(parms is None)) :
                cfg.display_no_dfs(cfg.DataTransform_ID)

                             
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    datetime processng methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    change column datetime datatype
#--------------------------------------------------------------------------
"""
def process_datetime_datatype_transform(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : convert column to datetime datatype
    * 
    * parms :
    *   parms     -   change parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    
    import datetime
    
    opstat  =   opStatus()
    
    fparms  =   get_parms_for_input(parms[3],dtw.datetime_format_input_idList)
    
    colname = fparms[0]
    
    if(len(fparms[1]) == 0) :
        dtype = get_datatype_str(11)
    else :
        dtype = fparms[1]
        
    df          =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
    #df_cols     =   df.columns.tolist()
    
    import pandas as pd

    fparms[3]   =  fparms[3].strip(" ")
    fparms[3]   =  fparms[3].rstrip(" ") 
    
    if(display) :
        clock = RunningClock()
        clock.start()
    
    try :
        
        if(dtype == "datetime.datetime") :
            if(len(fparms[3]) > 0) :
                df[colname] = pd.to_datetime(df[colname], format=fparms[3])
            else :
                df[colname] = pd.to_datetime(df[colname])
        else :
            if(not (get_datatype_id(df[colname].dtype) == 11) ) :
                if(len(fparms[3]) > 0) :
                    df[colname] = pd.to_datetime(df[colname], format=fparms[3])
                else :
                    df[colname] = pd.to_datetime(df[colname])
            
            if(dtype == "datetime.date") :
                df[colname] = df[colname].apply(lambda x: datetime.datetime.date(x))
            else :
                df[colname] = df[colname].apply(lambda x: datetime.datetime.time(x))
        
        # TODO 
        # restore the original cols order  
        #cfg.get_dfc_dataframe_df()[df_cols])       

    except Exception as e:
        opstat.store_exception("Error changing "  + colname + " to datetime datatype ",e)
    
    if(display) :
        clock.stop()
        
    if(opstat.get_status()) : 
        
        if(display) :
            
            #make scriptable
            add_to_script(["# change column datatype ",
                           "from dfcleanser.data_transform.data_transform_columns_control import process_datetime_datatype_transform",
                           "process_datetime_datatype_transform(" + single_quote(colname) + "," + json.dumps(fparms) + ",False)"],
                            opstat)

            dtw.display_main_taskbar()
            print("\n")
            display_status("Column " + colname +" data type changed successfully to " + dtype)
            dtw.display_transform_col_data(df,colname)
        
    else :
        
        if(display) :
            clear_output()
            dtw.display_main_taskbar()
            display_exception(opstat)

"""
#--------------------------------------------------------------------------
#    merge split column datatype
#--------------------------------------------------------------------------
"""
def process_datetime_timedelta_transform(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : get datetime delta from columns
    * 
    * parms :
    *   parms     -   change parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    
    opstat  =   opStatus()
    
    fparms  =   get_parms_for_input(parms[1],dtw.datetime_tdelta_input_idList)

    
    colname     =   fparms[0]
    colname1    =   fparms[1]
    tdcolname   =   fparms[2] 
    units       =   fparms[3]
    units       =   get_units_id(units)
    
    df          =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
    found       =   False
    found1      =   False
    
    # check that input parms are ok
    if(len(colname) == 0) :
        opstat.set_errorMsg(colname + " is not a valid column name")
        opstat.set_status(False)
    elif(len(colname1) == 0) :
        opstat.set_errorMsg(colname1 + " is not a valid column name")
        opstat.set_status(False)
    elif(len(tdcolname) == 0) :
        opstat.set_errorMsg(tdcolname + " is not a valid column name")
        opstat.set_status(False)
    elif(is_existing_column(df,tdcolname)) :
        opstat.set_errorMsg(tdcolname + " is already defined")
        opstat.set_status(False)
    else :
        
        df_cols     =   df.columns.tolist()
        for i in range(len(df_cols)) :
            if(df_cols[i] == colname)   :   found = True
            if(df_cols[i] == colname1)  :   found1 = True
    
        if(not found) :
            opstat.set_errorMsg(colname + " is not a dataframe column")
            opstat.set_status(False)
        elif(not found1) :
            opstat.set_errorMsg(colname1 + " is not a dataframe column")
            opstat.set_status(False)
        elif(not ((is_datetime_col(df,colname)) or (get_datatype_id(df[colname].dtype) == 11) ) ):
            opstat.set_errorMsg(colname + " is not a datetime column")
            opstat.set_status(False)
        
    if(opstat.get_status()) :
    
        if(display) :
            clock = RunningClock()
            clock.start()
    
        try :

            from dfcleanser.common.common_utils import YEARS, DAYS, HOURS, MINUTES, SECONDS, MICROSECONDS, TIMEDELTA
            import pandas as pd
            
            timedeltacol = df[colname] - df[colname1]
            dtcc.add_column(cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF),tdcolname,timedeltacol,opstat)

            df = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
            
            if(opstat.get_status()) :

                if(units == SECONDS) :
                    df[tdcolname] = df[tdcolname].apply(lambda x: round(pd.Timedelta(x).total_seconds()))
                    #TODO check inplace
                else :
                    
                    if(units == YEARS) :  
                        df[tdcolname] = df[tdcolname].apply(lambda x: divmod(pd.Timedelta(x).total_seconds(), 31556926)[0])
                    elif(units == DAYS) :  
                        df[tdcolname] = df[tdcolname].apply(lambda x: divmod(pd.Timedelta(x).total_seconds(), 86400)[0])
                    elif(units == HOURS) :  
                        df[tdcolname] = df[tdcolname].apply(lambda x: divmod(pd.Timedelta(x).total_seconds(), 3600)[0])
                    elif(units == MINUTES) :  
                        df[tdcolname] = df[tdcolname].apply(lambda x: divmod(pd.Timedelta(x).total_seconds(), 60)[0])
                    elif(units == MICROSECONDS) :  
                        df[tdcolname] = df[tdcolname].apply(lambda x: x.microseconds)
                    
                    if(not (units == TIMEDELTA)) :
                        opstat = convert_df_cols(df,[tdcolname],7)
                    
                    #TODO check inplace
  
        # convert to .date or .time         
        except Exception as e:
            opstat.store_exception("Error getting timedelta between "  + colname + " : " + colname1,e)
    
        if(display) :
            clock.stop()
        
    if(opstat.get_status()) : 
        
        if(display) :
        
            #make scriptable
            add_to_script(["# calculate timedelta values ",
                           "from dfcleanser.data_transform.data_transform_columns_control import process_datetime_timedelta_transform",
                           "process_datetime_timedelta_transform(" + json.dumps(parms) + ",False)"],opstat)
            
            dtw.display_main_taskbar()
            print("\n")
            display_status("Timedelta values stored successfully in " + tdcolname)
            dtw.display_column_transform_status(df,tdcolname)
        
    else :
        
        if(display) :
            clear_output()
            dtw.display_main_taskbar()
            display_exception(opstat)



"""
#--------------------------------------------------------------------------
#    merge split column datatype
#--------------------------------------------------------------------------
"""
def process_datetime_merge_split_transform(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : merge or split a datetime column
    * 
    * parms :
    *   parms     -   change parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    print("process_datetime_merge_split_transform",parms)    
    
    import datetime
    opstat  =   opStatus()
    
    action = parms[1]

    if(action == 0) :
        fparms  =   get_parms_for_input(parms[2],dtw.datetime_split_input_idList)
    else :
        fparms  =   get_parms_for_input(parms[2],dtw.datetime_merge_input_idList)
    
    colname = fparms[0]

    df = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
    
    if(display) :
        clock = RunningClock()
        clock.start()
    
    if(action == dtm.SPLIT) :
        
        datetimecolumn  =   fparms[0]
        datecolumn      =   fparms[1]
        timecolumn      =   fparms[2]
        
        #TODO check that datetimecolumn is a datetime type
        
        if(is_existing_column(df,datecolumn)) :
            opstat.set_errorMsg(datecolumn + " is already defined")
            opstat.set_status(False)
        elif(is_existing_column(df,timecolumn)) :
            opstat.set_errorMsg(timecolumn + " is already defined")
            opstat.set_status(False)
        
        if(opstat.get_status()) :
        
            splitdate       =   []
            splittime       =   []
        
            try :
                
                splitdate = df[datetimecolumn].apply(lambda x: x.date())            
                splittime = df[datetimecolumn].apply(lambda x: x.time())            
        
                dtcw.add_column(cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF),datecolumn,splitdate,opstat)
                dtcw.add_column(cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF),timecolumn,splittime,opstat)
        
            # convert to .date or .time         
            except Exception as e:
                opstat.store_exception("Error changing "  + colname + " to datetime datatype ",e)
        
            if(display) :
                clock.stop()
    
            if(opstat.get_status()) : 
                
                if(display) :
                    
                    #make scriptable
                    add_to_script(["# split date time columns ",
                                   "from dfcleanser.data_transform.data_transform_columns_control import process_datetime_merge_split_transform",
                                   "process_datetime_merge_split_transform(" + json.dumps(parms) + ",False)"],opstat)
                
                    dtw.display_main_taskbar()
                    print("\n")
                    display_status("Column " + datetimecolumn + " split successfully to " + datecolumn +" : " + timecolumn)
                    dtw.display_transform_col_data(df,datetimecolumn)
                    dtw.display_transform_col_data(df,datecolumn)
                    dtw.display_transform_col_data(df,timecolumn)

            else :
        
                if(display) :
                    clear_output()
                    dtw.display_main_taskbar()
                    display_exception(opstat)
                    
        else :
        
            if(display) :
                clear_output()
                dtw.display_main_taskbar()
                display_exception(opstat)
        
    else :
    
        datecolumn      =   fparms[0]
        timecolumn      =   fparms[1]
        datetimecolumn  =   fparms[2]
        
        if(is_existing_column(df,datetimecolumn)) :
            opstat.set_errorMsg(datetimecolumn + " is already defined")
            opstat.set_status(False)
        
        if(opstat.get_status()) :
    
            mergeddatetime  =   []
        
            try :
            
                for i in range(len(df[datecolumn])) :
                    mergeddatetime.append(datetime.datetime.combine(df[datecolumn][i],df[timecolumn][i]))
        
                dtcc.add_column(cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF),datetimecolumn,mergeddatetime,opstat)
        
            # convert to .date or .time         
            except Exception as e:
                opstat.store_exception("Error changing "  + colname + " to datetime datatype ",e)
    
            if(display) :
                clock.stop()
        
            if(opstat.get_status()) : 
                
                if(display) :
                    
                    #make scriptable
                    add_to_script(["# merge date time columns ",
                                   "from dfcleanser.data_transform.data_transform_columns_control import process_datetime_merge_split_transform",
                                   "process_datetime_merge_split_transform(" + json.dumps(parms) + ",False)"],opstat)
                    
                    dtw.display_main_taskbar()
                    print("\n")
                    display_status("Columns " + datecolumn + ":" + timecolumn +" merged successfully to " + datetimecolumn)
                    dtw.display_transform_col_data(df,datetimecolumn)
        
            else :
        
                if(display) :
                    clear_output()
                    dtw.display_main_taskbar()
                    display_exception(opstat)

        else :
        
            if(display) :
                clear_output()
        
            dtw.display_main_taskbar()
            display_exception(opstat)


def process_get_datetime_component(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the datatime component into a column
    * 
    * parms :
    *   parms     -   change parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    
    #TODO
    print("process_get_datetime_component",parms)    
    
    


def convert_nan_value(dtype,nanvalue,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : convert a nan value to ok data type
    * 
    * parms :
    *   parms     -   change parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    try :
                
        # covert nan value to dattype                
                
                
        nanvalue = float(nanvalue)    
    except :
        opstat.set_status(False)
        opstat.set_errorMsg("Nan fill value is invalid")


def get_nan_value(dtid, nanmethod, nanval, opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : get a nan value for a data type
    * 
    * parms :
    *   parms     -   change parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
     
    if(nanmethod == 0) :
        if(len(nanval) > 0) :
            
            if( ((dtid >= 0) and (dtid <= 7)) or (dtid == 17) ) :
                try :
                    nanvalue    =   int(nanval)
                except :
                    opstat.set_status(False)
                    opstat.set_errorMsg("Nan fill value is not an int")
                    
            elif( ((dtid >= 8) and (dtid <= 10)) or (dtid == 18) ) :
                try :
                    nanvalue    =   float(nanval)
                except :
                    opstat.set_status(False)
                    opstat.set_errorMsg("Nan fill value is not a float")
                    
        else :
            nanvalue    =   None
    else :
        nanvalue    =   None 
        
    return(nanvalue)

    
"""
#--------------------------------------------------------------------------
#    change column datatype
#--------------------------------------------------------------------------
"""
def process_dfschema_datatype_transform(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : process the datatype change from dfschema
    * 
    * parms :
    *   parms     -   change parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat  =   opStatus()

    print("process_dfschema_datatype_transform",parms)

    colname     =   parms[0]
    dtid        =   int(parms[1])
    nafunc      =   parms[2]
    
    nanmethod   =   parms[4]  
    
    df          =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
    col_nans    =   df[colname].isnull().sum() 

    if(col_nans > 0) :
        if(nafunc == "fillna") :
            nanvalue    =   get_nan_value(dtid, nanmethod, parms[3], opstat)        
        else :
            nanvalue = None
            
    if(opstat.get_status())  :          
        currentdtype = df[colname].dtype
    
        if( (dtid == -1) or (get_datatype(dtid) == get_datatype_id(currentdtype)) ) :
            opstat.set_status(False)
            opstat.set_errorMsg("Unable to convert data type - No New Data Type Selected")
        
    if(opstat.get_status()) :
        dtstr = get_datatype_str(dtid) 

        if((dtstr == "datetime.datetime") ) :
            
            convparms = [dtstr,colname,nanvalue]
            from dfcleanser.data_transform.data_transform_widgets import display_datetime_convert
            display_datetime_convert(convparms)
            return()
            
        else :
            if(dtid > 11) :
                dtid = dtid + 3
                
            opstat = convert_df_cols(df,[colname],dtid,nanvalue)
    
    if(display) :
    
        from IPython.display import clear_output
        clear_output()
    
        dtw.display_main_taskbar()
        print("\n")
    
        dfschema_table = get_table_value("dfschemaTable")

        if(dfschema_table == None) :
            dfschema_table = dcTable("Dataframe Schema","dfschemaTable",cfg.DataTransform_ID)
            dfschema_table.set_colsperrow(6)
        else :
            dfschema_table.set_lastcoldisplayed(-1)
    
        if(opstat.get_status()) : 
        
            #make scriptable
            add_to_script(["# change column datatype ",
                           "from dfcleanser.data_transform.data_transform_control import process_datatype_transform",
                           "process_datatype_transform(" + json.dumps(parms) + ",False)"],opstat)
        
            display_status("Column " + colname +" data type changed successfully to " + get_datatype_str(dtid))
            dtw.display_column_transform_status(df,colname)
        
        else :
        
            display_exception(opstat)


"""
#--------------------------------------------------------------------------
#    check compatability helper methods 
#--------------------------------------------------------------------------
"""
def is_int_desiredtype(dtype) :
    
    if( (dtype == "np.int8") or (dtype == "np.int16") or (dtype == "np.int32") or (dtype == "np.int64") or
        (dtype == "np.uint8") or (dtype == "np.uint16") or (dtype == "np.uint32") or (dtype == "np.uint64") or
        (dtype == "int") ) :
        
        return(True)
        
    else :
        return(False)


def is_float_desiredtype(dtype) :
    
    if( (dtype == "np.float16") or (dtype == "np.float32") or (dtype == "np.float64") or (dtype == "float") ) :
        return(True)
    else :
        return(False)

def is_numeric_desiredtype(dtype) :
    
    if( (is_int_desiredtype(dtype)) or (is_float_desiredtype(dtype)) ) :
        return(True)
    else :
        return(False)

def is_dateime_desiredtype(dtype) :
    
    if( (dtype == "datetime.datetime") or (dtype == "datetime.date") or 
        (dtype == "datetime.time") or (dtype == "datetime.timedelta") or 
        (dtype == "np.datetime64") or (dtype == "np.timedelta64") or 
        (dtype == "pd.timestamp") ) :
        
        return(True)
        
    else :
        return(False)


def total_seconds(timedelta):
    
    import numpy as np
    
    try:
        seconds = timedelta.total_seconds()
    except AttributeError:  # no method total_seconds
        one_second = np.timedelta64(1000000000, 'ns')
        # use nanoseconds to get highest possible precision in output
        seconds = timedelta / one_second
    return seconds


"""
#--------------------------------------------------------------------------
#    check compatability by datatype methods 
#--------------------------------------------------------------------------
"""

def check_numeric_compatability(df,colname,desireddatatype,minval,maxval,values) :
    """
    * -------------------------------------------------------------------------- 
    * function : check conversion compatability for a numeric column
    * 
    * parms :
    *   df              -   dataframe
    *   colname         -   column name
    *   desireddatatype -   datatype to convert to
    *   minval          -   column min value
    *   maxval          -   column max value
    *   values          -   column unique values
    *
    * returns : 
    *  list - [reason_code,reason_parms]
    * --------------------------------------------------------
    """
    
    import numpy as np
    import math

    check_results   =   False
    reason_code     =   dtm.VALUES_OK
    reason_parms    =   []
    
    precision_loss  =   0
    total_losses    =   0
    
    if(desireddatatype == "np.int8") :
        if( (minval > np.iinfo(np.int8).min) and (maxval < np.iinfo(np.int8).max) )          :   
            check_results = True
        else :
            if(minval < np.iinfo(np.int8).min) :    reason_parms    =   ["less than",str(np.iinfo(np.int8).min)]
            else :                                  reason_parms    =   ["greater than",str(np.iinfo(np.int8).max)]
                        
    elif(desireddatatype == "np.int16") :
        if( (minval > np.iinfo(np.int16).min) and (maxval < np.iinfo(np.int16).max) )        :   
            check_results = True
        else :
            if(minval < np.iinfo(np.int16).min) :   reason_parms    =   ["less than",str(np.iinfo(np.int16).min)]
            else :                                  reason_parms    =   ["greater than",str(np.iinfo(np.int16).max)]
                    
    elif(desireddatatype == "np.int32") :
        if( (minval > np.iinfo(np.int32).min) and (maxval < np.iinfo(np.int32).max) )        :   
            check_results = True
        else :
            if(minval < np.iinfo(np.int32).min) :   reason_parms    =   ["less than",str(np.iinfo(np.int32).min)]
            else :                                  reason_parms    =   ["greater than",str(np.iinfo(np.int32).max)]
                    
    elif(desireddatatype == "np.int64") :
        if( (minval > np.iinfo(np.int64).min) and (maxval < np.iinfo(np.int64).max) )        :   
            check_results = True
        else :
            if(minval < np.iinfo(np.int64).min) :   reason_parms    =   ["less than",str(np.iinfo(np.int64).min)]
            else :                                  reason_parms    =   ["greater than",str(np.iinfo(np.int64).max)]
                    
    elif(desireddatatype == "np.uint8") :
        if( (minval > np.iinfo(np.uint8).min) and (maxval < np.iinfo(np.uint8).max) )        :   
            check_results = True
        else :
            if(minval < np.iinfo(np.uint8).min) :   reason_parms    =   ["less than",str(np.iinfo(np.uint8).min)]
            else :                                  reason_parms    =   ["greater than",str(np.iinfo(np.uint8).max)]
                    
    elif(desireddatatype == "np.uint16") :
        if( (minval > np.iinfo(np.uint16).min) and (maxval < np.iinfo(np.uint16).max) )      :   
            check_results = True
        else :
            if(minval < np.iinfo(np.uint16).min) :  reason_parms    =   ["less than",str(np.iinfo(np.uint16).min)]
            else :                                  reason_parms    =   ["greater than",str(np.iinfo(np.uint16).max)]
                    
    elif(desireddatatype == "np.uint32") :
        if( (minval > np.iinfo(np.uint32).min) and (maxval < np.iinfo(np.uint32).max) )      :   
            check_results = True
        else :
            if(minval < np.iinfo(np.uint32).min) :  reason_parms    =   ["less than",str(np.iinfo(np.uint32).min)]
            else :                                  reason_parms    =   ["greater than",str(np.iinfo(np.uint32).max)]
                    
    elif(desireddatatype == "np.uint64") :
        if( (minval > np.iinfo(np.uint64).min) and (maxval < np.iinfo(np.uint64).max) )      :   
            check_results = True
        else :
            if(minval < np.iinfo(np.uint64).min) :  reason_parms    =   ["less than",str(np.iinfo(np.uint64).min)]
            else :                                  reason_parms    =   ["greater than",str(np.iinfo(np.uint64).max)]
                    
    elif(desireddatatype == "np.float16") :
        if( (minval > np.finfo(np.float16).min) and (maxval < np.finfo(np.float16).max) )    :   
            check_results = True
        else :
            if(minval < np.finfo(np.float16).min) : reason_parms    =   ["less than",str(np.finfo(np.float16).min)]
            else :                                  reason_parms    =   ["greater than",str(np.finfo(np.float16).max)]
                    
    elif(desireddatatype == "np.float32") :
        if( (minval > np.finfo(np.float32).min) and (maxval < np.finfo(np.float32).max) )    :   
            check_results = True
        else :
            if(minval < np.finfo(np.float32).min) : reason_parms    =   ["less than",str(np.finfo(np.float32).min)]
            else :                                  reason_parms    =   ["greater than",str(np.finfo(np.float32).max)]
                    
    elif(desireddatatype == "np.float64") :
        if( (minval > np.finfo(np.float64).min) and (maxval < np.finfo(np.float64).max) )    :   
            check_results = True
        else :
            if(minval < np.finfo(np.float64).min) : reason_parms    =   ["less than",str(np.finfo(np.float64).min)]
            else :                                  reason_parms    =   ["greater than",str(np.finfo(np.float64).max)]
                    
    elif(desireddatatype == "float") :
        if( (minval > sys.float_info.min) and (maxval < sys.float_info.max) )                :   
            check_results = True
        else :
            if(minval < sys.float_info.min) :       reason_parms    =   ["less than",str(sys.float_info.min)]
            else :                                  reason_parms    =   ["greater than",str(sys.float_info.max)]
    
    elif(desireddatatype == "datetime.timedelta") :
        if( (minval > dtm.MIN_DATETIME_TIMEDELTA_NANOSECONDS) and (maxval < dtm.MAX_DATETIME_TIMEDELTA_NANOSECONDS) )                :   
            check_results = True
        else :
            if( (minval > dtm.MIN_DATETIME_TIMEDELTA_MICROSECONDS) and (maxval < dtm.MAX_DATETIME_TIMEDELTA_MICROSECONDS) )          :   
                check_results = True
                reason_parms    =   ["only microseconds or above",None]
            else :
                if( (minval > dtm.MIN_DATETIME_TIMEDELTA_MILLISECONDS) and (maxval < dtm.MAX_DATETIME_TIMEDELTA_MILLISECONDS) )          :   
                    check_results = True
                    reason_parms    =   ["only milliseconds or above",None]
                else :
                    if( (minval > dtm.MIN_DATETIME_TIMEDELTA_SECONDS) and (maxval < dtm.MAX_DATETIME_TIMEDELTA_SECONDS) )          :   
                        check_results   =   True
                        reason_parms    =   ["only seconds",None]
                    else :
                        if(minval < dtm.MIN_DATETIME_TIMEDELTA_SECONDS) :       reason_parms    =   ["less than",str(dtm.MIN_DATETIME_TIMEDELTA_SECONDS)]
                        else :                                                  reason_parms    =   ["greater than",str(dtm.MAX_DATETIME_TIMEDELTA_SECONDS)]
    
    elif(desireddatatype == "np.timedelta64") :
        if( (minval > dtm.MIN_NP_TIMEDELTA_NANOSECONDS) and (maxval < dtm.MAX_NP_TIMEDELTA_NANOSECONDS) )                :   
            check_results = True
        else :
            if( (minval > dtm.MIN_NP_TIMEDELTA_MICROSECONDS) and (maxval < dtm.MAX_NP_TIMEDELTA_MICROSECONDS) )          :   
                check_results   =   True
                reason_parms    =   ["only microseconds or above",None]
            else :
                if( (minval > dtm.MIN_NP_TIMEDELTA_MILLISECONDS) and (maxval < dtm.MAX_NP_TIMEDELTA_MILLISECONDS) )          :   
                    check_results   =   True
                    reason_parms    =   ["only milliseconds or above",None]
                else :
                    if( (minval > dtm.MIN_NP_TIMEDELTA_SECONDS) and (maxval < dtm.MAX_NP_TIMEDELTA_SECONDS) )          :   
                        check_results   =   True
                        reason_parms    =   ["only seconds",None]
                    else :
                        if(minval < dtm.MIN_DATETIME_TIMEDELTA_SECONDS) :       reason_parms    =   ["less than",str(dtm.MIN_NP_TIMEDELTA_SECONDS)]
                        else :                                                  reason_parms    =   ["greater than",str(dtm.MAX_NP_TIMEDELTA_SECONDS)]
                   
    elif(desireddatatype == "int") :
        if(is_int_desiredtype(str(df[colname].dtype)) )                :     
            check_results = True
            
    if(not check_results) :
        reason_code     =    dtm.VALUE_OUT_OF_RANGE
        if(reason_parms[0] == "less_than") :
            reason_parms.append(str(minval))
        else :
            reason_parms.append(str(maxval))
            
    else :
        
        if(is_float_col(df,colname)) :
                
            if(is_int_desiredtype(desireddatatype)) :
                    
                for i in range(len(values)) :
                    frac, whole     =   math.modf(values[i])
                        
                    if(frac > 0) :
                        precision_loss  =   precision_loss + (frac/whole)
                        total_losses    =   total_losses + 1
                            
                if(total_losses > 0)  :
                    reason_code      =   dtm.PRECISION_LOSS
                    reason_parms     =   [precision_loss,total_losses]
           
    return([reason_code,reason_parms])

    
def check_datetime_compatability(df,colname,desireddatatype,minval,maxval) :
    """
    * -------------------------------------------------------------------------- 
    * function : check conversion compatability for a datetime object or string  column
    * 
    * parms :
    *   df              -   dataframe
    *   colname         -   column name
    *   desireddatatype -   datatype to convert to
    *   minval          -   column min value
    *   maxval          -   column max value
    *   values          -   column unique values
    *
    * returns : 
    *  list - [reason_code,reason_parms]
    * --------------------------------------------------------
    """

    import datetime    
    
    check_results   =   False
    reason_code     =   dtm.VALUES_OK
    reason_parms    =   []
    
    if(desireddatatype == "datetime.datetime") :
        if( (minval > datetime.datetime.min) and (maxval < datetime.datetime.max) )      :   
            check_results = True
        else :
            if(minval < datetime.datetime.min) :    reason_parms    =   ["less than",str(datetime.datetime.min)]
            else :                                  reason_parms    =   ["greater than",str(datetime.datetime.max)]
                    
    elif(desireddatatype == "datetime.date") :
        if( (minval > datetime.date.min) and (maxval < datetime.date.max) )              :   
            check_results = True
        else :
            if(minval < datetime.date.min) :        reason_parms    =   ["less than",str(datetime.date.min)]
            else :                                  reason_parms    =   ["greater than",str(datetime.date.max)]
                    
    elif(desireddatatype == "datetime.time") :
        if( (minval > datetime.time.min) and (maxval < datetime.time.max) )              :   
            check_results = True
        else :
            if(minval < datetime.time.min) :        reason_parms    =   ["less than",str(datetime.time.min)]
            else :                                  reason_parms    =   ["greater than",str(datetime.time.max)] 
                    
    elif(desireddatatype == "np.datetime64") :
        if( (minval > datetime.timedelta.min) and (maxval < datetime.timedelta.max) )    :   
            check_results = True
        else :
            if(minval < datetime.timedelta.min) :   reason_parms    =   ["less than",str(datetime.timedelta.min)]
            else :                                  reason_parms    =   ["greater than",str(datetime.timedelta.max)]

    elif(desireddatatype == "pd.timestamp") :
        if( (minval > datetime.timedelta.min) and (maxval < datetime.timedelta.max) )    :   
            check_results = True
        else :
            if(minval < datetime.timedelta.min) :   reason_parms    =   ["less than",str(datetime.timedelta.min)]
            else :                                  reason_parms    =   ["greater than",str(datetime.timedelta.max)]
            
    if(not check_results) :
        reason_code     =    dtm.VALUE_OUT_OF_RANGE
        if(reason_parms[0] == "less_than") :
            reason_parms.append(str(minval))
        else :
            reason_parms.append(str(maxval))
    
    return([reason_code,reason_parms])

    


def check_datatype_compatability(df,colname,desireddatatype,values,minval,maxval,samplesize=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : drop cols with nans greater than threshold
    * 
    * parms :
    *   parms     -   cheknum parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    #print("check_datatype_compatability",colname,desireddatatype,type(desireddatatype),len(values),minval,maxval,samplesize)
    
    reason_code     =   dtm.VALUES_OK
    reason_parms    =   []
    
    import datetime
    import pandas as pd
    import numpy as np
    
    """
    print("\n")                
    print("datetime min ",datetime.datetime.min) 
    print("datetime max ",datetime.datetime.max) 
    print("max datetime ordinal",datetime.datetime.max.toordinal())
    #maxdt   =  datetime.datetime.max 
    #print("maxdt",maxdt,type(maxdt))
    #print("datetime max total seconds",maxdt.total_seconds())
    
    print("\n")
    print("date min ",datetime.date.min)  
    print("date max ",datetime.date.max)  
    print("max date ordinal",datetime.date.max.toordinal())
    
    print("\n") 
    print("time min ",datetime.time.min)
    print("time max ",datetime.time.max)
    
    print("\n")
    print("timedelta min ",datetime.timedelta.min)
    tdelta  =   datetime.timedelta(-999999999)
    print("timedelta datetime min ",tdelta)
    print("timedelta datetime min seconds ",tdelta.total_seconds())
    print("timedelta datetime min seconds ",total_seconds(tdelta))   
    
    print("timedelta max ",datetime.timedelta.max)
    tdelta  =   datetime.timedelta(days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999)
    print("timedelta datetime max ",tdelta)
    print("timedelta datetime max seconds ",tdelta.total_seconds())
    print("timedelta datetime max milliseconds ", 1000 * tdelta.total_seconds())
    print("timedelta datetime max microseconds ", 1000 * 1000 * tdelta.total_seconds())
    print("timedelta datetime max nanoseconds ", 1000 * 1000 * 1000 * tdelta.total_seconds())
    
    
    
    print("\n") 
    
    dt1 = np.datetime64(datetime.date.min)
    dt2 = np.datetime64(datetime.date.max)
    my_timedelta = dt2 - dt1
    print("timedelta np.timedelta max ",my_timedelta,type(my_timedelta))
    print("timedelta np.timedelta seconds max ",total_seconds(my_timedelta))
    print("timedelta np.timedelta milliseconds max ",1000 * total_seconds(my_timedelta))
    print("timedelta np.timedelta microseconds max ",1000 * 1000 * total_seconds(my_timedelta))
    print("timedelta np.timedelta nanoseconds max ",1000 * 1000 * 1000 * total_seconds(my_timedelta))
    
    my_timedelta = dt1 - dt2
    print("timedelta np.timedelta min ",my_timedelta,type(my_timedelta))
    print("timedelta np.timedelta seconds min ",total_seconds(my_timedelta))
    
    
    print("\n")
    print("pandas Timestamp min ",pd.Timestamp.min)
    print("pandas Timestamp max ",pd.Timestamp.max)
     
    pdtmstmp    =  pd.Timestamp(year=1677, month=9, day=21, hour=0, minute=12, second=44)
    print("pandas Timestamp min ",pdtmstmp)
    
    pdtmstmp    =  pd.Timestamp(year=2262, month=4, day=11, hour=23, minute=47, second=16)
    print("pandas Timestamp max ",pdtmstmp)
    
    pdtmstmp1    =  pd.Timestamp("1677-09-21T00:12:43.145225")
    print("pandas Timestamp min ",pdtmstmp1)
    
    pdtmstmp2    =  pd.Timestamp("2262-04-11T23:47:16.854775807")
    print("pandas Timestamp max ",pdtmstmp2)
    
    #pdtmstmpsecs = pdtmstmp2 - pdtmstmp1
    #pdtmstmpsecs = pdtmstmpsecs/np.timedelta64(1,'s')  
    #print("pandas Timestamp max seconds",pdtmstmpsecs)

    pdtmstmp    =  pd.Timestamp(year=1, month=1, day=1, hour=0, minute=0, second=0)
    print("pandas datetime Timestamp min ",pdtmstmp)
    
    pdtmstmp    =  pd.Timestamp(year=9999, month=12, day=31, hour=23, minute=59, second=59)
    print("pandas datetime Timestamp max ",pdtmstmp)


    
    print("\n")
    
    pdtmstmp    =  pd.Timestamp.min 
    print("pandas Timestamp",pdtmstmp,pdtmstmp.toordinal())

    pdtmstmp    =  pd.Timestamp.max 
    print("pandas Timestamp",pdtmstmp,pdtmstmp.toordinal())
   
    pdtmstmp    =  pd.Timestamp(1513393355.5, unit='s') 
    print("pandas Timestamp",pdtmstmp,pdtmstmp.toordinal())
    
    pdtmstmp    =  pd.Timestamp(datetime.datetime.min) 
    print("pandas Timestamp",pdtmstmp,pdtmstmp.toordinal())
    
    pdtmstmp    =  pd.Timestamp(datetime.datetime.max) 
    print("pandas Timestamp",pdtmstmp,pdtmstmp.toordinal())
    
    
    pdtmstmp    =  pd.Timestamp.min
    print("pandas Timestamp",pdtmstmp,pdtmstmp.toordinal())
    pdtmstmp    =  pd.Timestamp.max
    print("pandas Timestamp",pdtmstmp,pdtmstmp.toordinal())
    """
    

    if(is_numeric_col(df,colname)) :
        
        if(is_numeric_desiredtype(desireddatatype)) :
            
            num_compatability_data  =   check_numeric_compatability(df,colname,desireddatatype,minval,maxval,values)
            reason_code             =   num_compatability_data[0]
            reason_parms            =   num_compatability_data[1]
    
    elif(is_datetime_type_col(df,colname)) :
        
        print("")        
            
    elif( (is_string_col(df,colname)) or (is_object_col(df,colname)) ) :
        
        if(samplesize == 100) :
            loopsize    =   len(values)
        else :
            loopsize    =   len(values) * (samplesize * 0.01)
        
        if(is_numeric_desiredtype(desireddatatype)) :
            
            for i in range(loopsize) :
                
                if(samplesize == 100)   :
                    k   =   i
                else :
                    import random
                    k   =  random.randint(0,len(values)) 
                
                try :
                    numval  =   values[k].replace('.','',1)
                    numval  =   numval.replace('-','',1)
                    if(not (numval.isdigit()) ) :  
                        reason_code     =   dtm.VALUE_NOT_NUMERIC
                        reason_parms    =   [k,values[k]]
                        break;
                except :
                        reason_code     =   dtm.VALUE_NOT_NUMERIC
                        reason_parms    =   [k,values[k]]
                        break;
                    
            
            if(reason_code == dtm.VALUES_OK) :
                str_compatability_data  =   check_numeric_compatability(df,colname,desireddatatype,float(minval),float(maxval),values)
                reason_code             =   str_compatability_data[0]
                reason_parms            =   str_compatability_data[1]
        
            
        elif(is_dateime_desiredtype(desireddatatype)) :
            
            for i in range(loopsize) :
                
                if(samplesize == 100)   :
                    k   =   i
                else :
                    import random
                    k   =  random.randint(0,len(values)) 
                
                try :
                    
                    if(desireddatatype == "datetime.datetime")  :   datetime.datetime(values[k])
                    if(desireddatatype == "datetime.date")      :   datetime.date(values[k])
                    if(desireddatatype == "datetime.time")      :   datetime.time(values[k])
                    if(desireddatatype == "np.datetime64")      :   np.datetime64(values[k])
                    if(desireddatatype == "pd.Timestamp")       :   pd.Timestamp(values[k])
                
                except :
                    reason_code     =   dtm.VALUE_NOT_NUMERIC
                    reason_parms    =   [k,values[k]]
                    break;
               
    return([reason_code,reason_parms])                    
    
        
def process_dfchknum_transform(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : drop cols with nans greater than threshold
    * 
    * parms :
    *   parms     -   cheknum parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat      =   opStatus()
    
    if(parms.find("checkdtsmaplesize") > -1 ) :
        fparms      =   get_parms_for_input(parms,dtcw.dt_str_check_data_type_input_idList)
        sample_size =   fparms[2]
    else :    
        fparms      =   get_parms_for_input(parms,dtcw.dt_check_data_type_input_idList)
        sample_size = None
    
    colname     =   fparms[0]
    check_list  =   fparms[1].split(",")
    
    df          =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF) 
 
    uniques     =   df[colname].unique().tolist()
    
    mincolval       =   min(uniques)
    maxcolval       =   max(uniques)
    
    dtw.display_main_option(None)
    
    print("\n")
    
    if(len(check_list) > 0) :
        
        check_results_list  =   []
        
        for i in range(len(check_list)) :
            
            check_results   =   check_datatype_compatability(df,colname,check_list[i],uniques,mincolval,maxcolval,sample_size) 
            check_results_list.append(check_results)
            
        status_html     =    display_check_compatability_status(colname,check_results_list,check_list,False)
        
        gridclasses     =   ["dfc-main"]
        gridhtmls       =   [status_html]
        
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) : 
            display_generic_grid("check-compatability-status-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("check-compatability-status-pop-up-wrapper",gridclasses,gridhtmls)
         
    else :
        
        opstat.set_status(False)
        opstat.set_errorMsg("No data types chosen to check for compatability")
    
    return()


def display_check_compatability_status(colname,check_status_list,check_dtype_list,display=True) : 
    """
    * -------------------------------------------------------------------------- 
    * function : display col uniques
    * 
    * parms :
    *  check_status_list  -   list of statuses
    *  colname     -   column name
    *  display            -   boolean display flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    chkstatHeader    =   ["Datatype","Converion Status","Notes"]
    chkstatWidths    =   [15,15,70]
    chkstatAligns    =   ["center","center","left"]
    
    chkstatRows      =   []
    chkstatrow       =   []
    
    for i in range(len(check_status_list)) :
        
        compatability_status        =   check_status_list[i][0]    
        compatability_stats         =   check_status_list[i][1] 
        
        if(compatability_status == dtm.VALUES_OK) :
            
            chkstatrow       =   [str(check_dtype_list[i]),"OK","column can be converted successfully"]
            chkstatRows.append(chkstatrow)
            
        elif(compatability_status == dtm.VALUE_OUT_OF_RANGE) :
            
            if(compatability_stats[0] == "less than") :
                chkstatrow       =   [str(check_dtype_list[i]),"Values Out</br>Of Range","value of " + compatability_stats[2] + " is less than " + check_dtype_list[i] + " min value of " + compatability_stats[1]]
            else :
                chkstatrow       =   [str(check_dtype_list[i]),"Values Out</br>Of Range","value of " + compatability_stats[2] + " is greater than " + check_dtype_list[i] + " max value of " + compatability_stats[1]]
            
            chkstatRows.append(chkstatrow)
                
                
        elif(compatability_status == dtm.PRECISION_LOSS) :
            
            precision_loss  =   float(compatability_stats[0])
            total_losses    =   float(compatability_stats[1])
    
            stat_msg    =   "  is not compatable with datatype conversion : loss of precision will occur.  "
            stat_msg    =   (stat_msg + "<br>&nbsp;%nbsp;&nbsp;%nbsp;Total amount of precision lost : " + str(precision_loss))
            stat_msg    =   (stat_msg + "<br>&nbsp;%nbsp;&nbsp;%nbsp;Total number of values losing precision : " + str(total_losses))
            stat_msg    =   (stat_msg + "<br>&nbsp;%nbsp;&nbsp;%nbsp;Average precision loss per value losing precision : " + str(precision_loss/total_losses))

            chkstatrow       =   [str(check_dtype_list[i]),"Precision</br>Loss",stat_msg]
            chkstatRows.append(chkstatrow)
        
        
        elif(compatability_status == dtm.VALUE_NOT_NUMERIC) :
        
            chkstatrow       =   [str(check_dtype_list[i]),"VALUE NOT</br>NUMERIC","column can not be converted successfully. Value : " + str(compatability_stats[1]) + " is nopt numeric"]
            chkstatRows.append(chkstatrow)
        
    chkstat_table = dcTable("Datatype Conversion Status for Column " + colname,
                            "dtchkstatTable",
                            cfg.DataTransform_ID,
                            chkstatHeader,chkstatRows,
                            chkstatWidths,chkstatAligns)
    
    chkstat_table.set_tabletype(SIMPLE)
    chkstat_table.set_table_column_parms({"font":12})
    chkstat_table.set_checkLength(False)
    chkstat_table.set_rowspertable(len(check_status_list))
    
    if(display) :
        chkstat_table.display_table()
    else :
        return(chkstat_table.get_html())

   
def clear_data_transform_data() :
    """
    * -------------------------------------------------------------------------- 
    * function : clear data transform working vars
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    drop_owner_tables(cfg.DataTransform_ID)
    from dfcleanser.common.html_widgets import delete_all_inputs, define_inputs
    
    dfctransformList    =   dtw.datatransform_inputs
    dfctransformList.extend(dtcw.datatransform_cols_inputs)
    dfctransformList.extend(dtdw.datatransform_df_inputs)    
    define_inputs(cfg.DataTransform_ID,dfctransformList)
    delete_all_inputs(cfg.DataTransform_ID)
    clear_data_transform_cfg_values()
    dtm.checknum_status.clear_chknum_status()    
    
def clear_data_transform_cfg_values() :
    
    cfg.drop_config_value(dtw.datetime_format_input_id+"Parms")
    cfg.drop_config_value(dtw.datetime_format_input_id+"ParmsProtect")
    cfg.drop_config_value(cfg.CURRENT_TRANSFORM_DF)
   
    dtdc.clear_dataframe_transform_cfg_values()
    dtcc.clear_dataframe_columns_transform_cfg_values()
    
    return
    


    