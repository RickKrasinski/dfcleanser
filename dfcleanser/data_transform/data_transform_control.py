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

from dfcleanser.common.table_widgets import (dcTable, drop_owner_tables, get_table_value)

from dfcleanser.common.common_utils import (display_status, display_exception, opStatus, single_quote, 
                                            get_parms_for_input, RunningClock, is_datetime_col, 
                                            get_datatype_id, is_existing_column, get_datatype_str, 
                                            get_units_id, convert_df_cols, get_datatype, is_numeric_col)

from dfcleanser.scripting.data_scripting_control import add_to_script

from IPython.display import clear_output

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
*   main routing functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

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

    if(not (cfg.is_a_dfc_dataframe_loaded()) ) :
        dtw.display_no_dataframe()
        if(not(parms==None)) :
            from dfcleanser.data_inspection.data_inspection_widgets import display_inspection_data
            display_inspection_data()
        
        clear_data_transform_data()
        

    else :
        
        if(option == dtm.DISPLAY_DF_SCHEMA_TRANSFORM) :
        
            if(not(parms==None)) :
            
                from dfcleanser.data_inspection.data_inspection_widgets import data_inspection_df_input_idList
                if(len(parms) > 1) :
                    fparms          =   get_parms_for_input(parms[1],data_inspection_df_input_idList)
                    if(len(fparms) > 0) :
                        selected_df     =   fparms[0]
            
                        if(not (len(selected_df) == 0) ) :
                            cfg.set_config_value(cfg.CURRENT_TRANSFORM_DF,selected_df)
       
        # go ahead and process the command
        if(option == dtm.MAIN_OPTION) :

            dtw.display_main_option(parms)
            if(parms==None) :
                clear_data_transform_data()
      
        elif(option == dtm.TRANSFORM_OPTION) :
            dtcc.process_column_option(parms)

        elif(option == dtm.DATAFRAME_DISPLAY_OPTION ) :
            dtdw.display_dataframe_options(parms)               

        elif(option == dtm.DATAFRAME_PROCESS_OPTION ) :
            dtdw.process_dataframe_transform(parms)
        
        elif(option == dtm.DISPLAY_TRANSFORM_COLS_OPTION) :
            dtcw.display_transform_cols_option(parms)
        
        elif(option == dtm.DISPLAY_DATETIME_OPTION) :
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
            
        elif(option == dtm.PROCESS_DF_SCHEMA_OPTION) :
            process_dfschema_datatype_transform(parms)
            
        elif(option == dtm.CHANGE_NA_OPTION) :
            if(parms[0] == 'fillna') :
                dropflag    =   False
            else :
                dropflag    =   True
                
            df      =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
            dtcw.display_convert_datatype(df,
                                          cfg.get_config_value(cfg.DATA_TRANSFORM_COL_SELECTED_KEY),
                                          dropflag,True,cfg.DataTransform_ID) 

        elif(option == dtm.DISPLAY_DROP_NA_OPTION) :
            print("dtm.DISPLAY_DROP_NA_OPTION",parms)

            if(parms[0] == cfg.DataCleansing_ID) :
                df      =   cfg.get_current_chapter_df(cfg.CURRENT_CLEANSE_DF)
                colname =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
            
            dtcw.display_dropna(df,colname)

        elif(option == dtm.DISPLAY_FILL_NA_OPTION) :
            print("dtm.DISPLAY_FILL_NA_OPTION",parms)    
            
            if(parms[0] == cfg.DataCleansing_ID) :
                df      =   cfg.get_current_chapter_df(cfg.CURRENT_CLEANSE_DF)
                colname =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
            
            dtcw.display_fillna(df,colname)

        elif(option == dtm.DISPLAY_DATATYPE_OPTION) :
            print("dtm.DISPLAY_FILL_NA_OPTION",parms)    
            
            if(parms[0] == cfg.DataCleansing_ID) :
                df      =   cfg.get_current_chapter_df(cfg.CURRENT_CLEANSE_DF)
                colname =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
            
            dtcw.display_convert_datatype(df,colname)

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
        
        elif(option == dtm.PROCESS_CHECK_NUMERIC) :
            print("dtm.PROCESS_CHECK_NUMERIC",parms)
            process_dfchknum_transform(parms)

        elif(option == dtm.PROCESS_DATETIME_COMPONNETS_OPTION) :
            print("dtm.PROCESS_DATETIME_COMPONNETS_OPTION",parms)
            process_get_datetime_component(parms)


                             
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
    df_cols     =   df.columns.tolist()
    
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
         
        # restore the original cols order  
        cfg.set_current_dfc_dataframe(cfg.get_dfc_dataframe()[df_cols])       

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
            dtw.display_transform_col_data(cfg.get_dfc_dataframe(),colname)
        
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
    elif(is_existing_column(cfg.get_dfc_dataframe(),tdcolname)) :
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

            df = cfg.get_dfc_dataframe()
            
            if(opstat.get_status()) :

                if(units == SECONDS) :
                    df[tdcolname] = df[tdcolname].apply(lambda x: round(pd.Timedelta(x).total_seconds()))
                    cfg.set_current_dfc_dataframe(df)
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
                    
                    cfg.set_current_dfc_dataframe(df)
  
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
            dtcw.display_column_transform_status(cfg.get_dfc_dataframe(),tdcolname)
        
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

    df = cfg.get_dfc_dataframe()
    
    if(display) :
        clock = RunningClock()
        clock.start()
    
    if(action == dtm.SPLIT) :
        
        datetimecolumn  =   fparms[0]
        datecolumn      =   fparms[1]
        timecolumn      =   fparms[2]
        
        #TODO check that datetimecolumn is a datetime type
        
        if(is_existing_column(cfg.get_dfc_dataframe(),datecolumn)) :
            opstat.set_errorMsg(datecolumn + " is already defined")
            opstat.set_status(False)
        elif(is_existing_column(cfg.get_dfc_dataframe(),timecolumn)) :
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
                    dtw.display_transform_col_data(cfg.get_dfc_dataframe(),datetimecolumn)
                    dtw.display_transform_col_data(cfg.get_dfc_dataframe(),datecolumn)
                    dtw.display_transform_col_data(cfg.get_dfc_dataframe(),timecolumn)

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
        
        if(is_existing_column(cfg.get_dfc_dataframe(),datetimecolumn)) :
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
                    dtw.display_transform_col_data(cfg.get_dfc_dataframe(),datetimecolumn)
        
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
    
    
    
    print("process_get_datetime_component",parms)    
    
    import datetime
    opstat  =   opStatus()
    
    #year = datetime.date.today().year
    #month = datetime.date.today().month
    #hour = datetime.date.today().hour

    #today.get_weekday()
    
    action = parms[1]

    if(action == 0) :
        fparms  =   get_parms_for_input(parms[2],dtw.datetime_split_input_idList)
    else :
        fparms  =   get_parms_for_input(parms[2],dtw.datetime_merge_input_idList)
    
    colname = fparms[0]

    df = cfg.get_dfc_dataframe()
    
    if(display) :
        clock = RunningClock()
        clock.start()
    
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
            #display_status("Columns " + datecolumn + ":" + timecolumn +" merged successfully to " + datetimecolumn)
            #dtw.display_transform_col_data(cfg.get_dfc_dataframe(),datetimecolumn)
        
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
    
    col_nans    =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)[colname].isnull().sum() 

    if(col_nans > 0) :
        if(nafunc == "fillna") :
            nanvalue    =   get_nan_value(dtid, nanmethod, parms[3], opstat)        
        else :
            nanvalue = None
            
    if(opstat.get_status())  :          
        currentdtype = cfg.get_dfc_dataframe()[colname].dtype
    
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
                
            opstat = convert_df_cols(cfg.get_dfc_dataframe(),[colname],dtid,nanvalue)
    
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
    
        from dfcleanser.data_transform.data_transform_widgets import display_df_schema
        display_df_schema(cfg.get_dfc_dataframe(),dfschema_table)    
        
        if(opstat.get_status()) : 
        
            #make scriptable
            add_to_script(["# change column datatype ",
                           "from dfcleanser.data_transform.data_transform_control import process_datatype_transform",
                           "process_datatype_transform(" + json.dumps(parms) + ",False)"],opstat)
        
            display_status("Column " + colname +" data type changed successfully to " + get_datatype_str(dtid))
            dtcw.display_column_transform_status(cfg.get_dfc_dataframe(),colname)
        
        else :
        
            display_exception(opstat)

        
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

    print("process_dfchknum_transform",parms)

    colname     =   parms[0]
    dtid        =   int(parms[1])
 
    uniques         =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)[colname].unique().tolist()
    
    numericOK   =   True
    
    for i in range(len(uniques)) :
        
        import pandas as pd
        if(pd.notnull(uniques[i])) :
        
            if(dtid == 0) :
                try :
                    if(not (uniques[i].isdigit()) ) :
                        numericOK=  False
                        i = len(uniques) + 1
                except :
                    numericOK=  False
                    i = len(uniques) + 1
                
            else :
                try :
                    float(uniques[i]) 
                except :
                    numericOK=  False
                    i = len(uniques) + 1
                
    if(numericOK) :
    
        if(dtid == 0) :
            dtm.checknum_status.set_col_status(colname,dtm.INT_STATUS) 
        else :
            dtm.checknum_status.set_col_status(colname,dtm.FLOAT_STATUS) 

    else :

        if(dtid == 0) :
            dtm.checknum_status.set_col_status(colname,dtm.NOT_INT_STATUS) 
        else :
            dtm.checknum_status.set_col_status(colname,dtm.NOT_FLOAT_STATUS) 
            
    dtw.display_transform_df_schema(None)

def clear_data_transform_data() :
    
    drop_owner_tables(cfg.DataTransform_ID)
    clear_data_transform_cfg_values()
    dtm.checknum_status.clear_chknum_status()    
    
def clear_data_transform_cfg_values() :
    
    cfg.drop_config_value(dtw.datetime_format_input_id+"Parms")
    cfg.drop_config_value(dtw.datetime_format_input_id+"ParmsProtect")
    cfg.drop_config_value(cfg.CURRENT_TRANSFORM_DF)
   
    dtdc.clear_dataframe_transform_cfg_values()
    dtcc.clear_dataframe_columns_transform_cfg_values()
    
    return
    


    