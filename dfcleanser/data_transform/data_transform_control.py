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

from dfcleanser.common.table_widgets import (dcTable, drop_owner_tables, get_table_value)

from dfcleanser.common.common_utils import (display_status, display_exception, opStatus, single_quote, 
                                            get_parms_for_input, RunningClock, is_datetime_column, 
                                            get_datatype_id, is_existing_column, get_datatype_str, 
                                            is_datetime_datatype, convert_df_cols, get_datatype)

from dfcleanser.scripting.data_scripting_control import add_to_script

from dfcleanser.common.display_utils import display_df_unique_column

from IPython.display import clear_output

from dfcleanser.data_transform.data_transform_columns_widgets import (display_column_transform_status)
 
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
*   main routing functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def display_data_transform(option,parms=None) :
    
    from IPython.display import clear_output
    clear_output()
    
    if(not (cfg.is_a_dfc_dataframe_loaded()) ) :
        dtw.display_no_dataframe()
        if(not(parms==None)) :
            from dfcleanser.data_inspection.data_inspection_widgets import display_inspection_data
            display_inspection_data()
        
        clear_data_transform_data()

    else :
        
        # go ahead and process the command
        if(option == dtm.MAIN_OPTION) :

            dtw.display_main_option(parms)
            if(parms==None) :
                clear_data_transform_data()
      
        elif(option == dtm.EXTERNAL_MAP_OPTION) :
            
            if(type(parms) != str) :
                colname = parms[0]
            else :
                colname = parms
 
            print("\n")

            uniques_table = dcTable("Unique Values and Counts for Column " + colname,
                                    colname+"uvalsTable",
                                    cfg.DataTransform_ID)

            display_df_unique_column(cfg.get_dfc_dataframe(),uniques_table,colname)
           
            dtw.display_single_column_taskbar() 
            
        elif(option == dtm.DISPLAY_MAP_OPTION) :

            if(type(parms) != str) :
                colname = parms[0]
            else :
                colname = parms
                
            dtw.display_mapping_column_taskbar()
            print("\n")
            
            uniques_table = dcTable("Unique Values and Counts for Column " + colname,
                                    colname+"uvalsTable",
                                    cfg.DataTransform_ID)
            
            display_df_unique_column(cfg.get_dfc_dataframe(),uniques_table,colname)
            
            from dfcleanser.data_transform.data_transform_columns_widgets import display_mapping_col
            display_mapping_col(cfg.get_dfc_dataframe(),colname) 

        elif(option == dtm.DISPLAY_DUMMY_OPTION) :

            if(type(parms) != str) :
                colname = parms[0]
            else :
                colname = parms
                
            dtw.display_dummies_column_taskbar()
            print("\n")

            if(colname != "List") :
                uniques_table = dcTable("Unique Values and Counts for Column " + colname,
                                        colname+"uvalsTable",
                                        cfg.DataTransform_ID)
                display_df_unique_column(cfg.get_dfc_dataframe(),uniques_table,colname)
                
            dtw.display_dummies_column_input()

        elif(option == dtm.DISPLAY_CATEGORY_OPTION) :
            
            if(type(parms) != str) :
                colname = parms[0]
            else :
                colname = parms
                
            dtw.display_cats_column_taskbar()
            print("\n")

            uniques_table = dcTable("Unique Values and Counts for Column " + colname,
                                    colname+"uvalsTable",
                                    cfg.DataTransform_ID)
            display_df_unique_column(cfg.get_dfc_dataframe(),uniques_table,colname)

            dtw.display_cats_column_input()


        elif(option == dtm.TRANSFORM_OPTION) :
            
            from dfcleanser.data_transform.data_transform_columns_control import process_column_option
            process_column_option(parms)

        elif(option == dtm.DATAFRAME_DISPLAY_OPTION ) :
            
            from dfcleanser.data_transform.data_transform_dataframe_widgets import display_dataframe_options
            display_dataframe_options(parms)               

        elif(option == dtm.DATAFRAME_PROCESS_OPTION ) :
            
            from dfcleanser.data_transform.data_transform_dataframe_widgets import process_dataframe_transform
            process_dataframe_transform(parms)
        
        elif(option == dtm.DISPLAY_TRANSFORM_COLS_OPTION) :
            
            from dfcleanser.data_transform.data_transform_columns_widgets import display_transform_cols_option
            display_transform_cols_option(parms)

        elif(option == dtm.DISPLAY_DATETIME_TRANSFORM_OPTION) :
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

        elif(option == dtm.PROCESS_DATETIME_TRANSFORM_OPTION) :
            process_datetime_datatype_transform(parms)
            
        elif(option == dtm.PROCESS_DATETIME_TIMEDELTA_OPTION) :
            process_datetime_timedelta_transform(parms)
            
        elif(option == dtm.PROCESS_DATETIME_MERGESPLIT_OPTION) :
            process_datetime_merge_split_transform(parms)
            
        elif(option == dtm.PROCESS_DF_SCHEMA_TRANSFORM_OPTION) :
            process_datatype_transform(parms)
            
            
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
    
    import datetime
    
    opstat  =   opStatus()
    
    fparms  =   get_parms_for_input(parms[3],dtw.datetime_format_input_idList)
    
    colname = fparms[0]
    
    if(len(fparms[1]) == 0) :
        dtype = get_datatype_str(11)
    else :
        dtype = fparms[1]
        
    df          =   cfg.get_dfc_dataframe()
    df_cols     =   df.columns.tolist()
    
    import pandas as pd

    fparms[3]   =  fparms[3].strip(" ")
    fparms[3]   =  fparms[3].rstrip(" ") 
    
    if(display) :
        clock = RunningClock()
        clock.start()
    
    try :
        if(dtype == "datetime.timedelta") :
            df[colname] = df[colname].apply(lambda x: pd.Timedelta(x))
        elif(dtype == "datetime.datetime") :
            if(len(fparms[3]) > 0) :
                df[colname] = pd.to_datetime(df[colname], format=fparms[3])
            else :
                df[colname] = pd.to_datetime(df[colname])
        else :
            datatype = 0
            if(not (is_datetime_datatype(datatype)) ) :
                if(len(fparms[3]) > 0) :
                    df[colname] = pd.to_datetime(df[colname], format=fparms[3])
                else :
                    df[colname] = pd.to_datetime(df[colname])
            
            #TODO set using lambda
            dtcomps = []
            for i in range(len(df[colname])) :
                if(dtype == "datetime.date") :
                    dtcomps.append(df[colname][i].date())
                else :
                    dtcomps.append(df[colname][i].time())
            
            # rename current column 
            namesdict = {}
            namesdict.update({colname:colname+"temp"})
            
            try :
                cfg.set_current_dfc_dataframe(df.rename(columns=namesdict))
            except Exception as e:
                opstat.store_exception("Error renaming " + colname + " to " + colname+"temp",e)
            
            if(opstat.get_status()) :
                from dfcleanser.data_transform.data_transform_columns_widgets import add_column
                add_column(colname,dtcomps,opstat)
                
                df = cfg.get_dfc_dataframe()
                if(opstat.get_status()) :
                    try :
                        
                        if(dtype == "datetime.date") :
                            df[colname] = df[colname].astype(datetime.date)
                        else :
                            df[colname] =df[colname].astype(datetime.time)
                                                
                        cfg.set_current_dfc_dataframe(df.drop([colname+"temp"],axis=1))
                    except Exception as e:
                        opstat.store_exception("Error dropping " + colname+"temp",e)
        
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
                           "from dfcleanser.data_transform.data_transform_columns_widgets import process_datetime_datatype_transform",
                           "process_datetime_datatype_transform(" + single_quote(colname) + "," + json.dumps(fparms) + ",False)"],
                            opstat)

            dtw.display_main_taskbar()
            print("\n")
            display_status("Column " + colname +" data type changed successfully to " + dtype)
            dtw.display_col_data(cfg.get_dfc_dataframe(),colname)
        
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
    
    opstat  =   opStatus()
    
    fparms  =   get_parms_for_input(parms[2],dtw.datetime_tdelta_input_idList)

    units       =   int(parms[1])
    colname     =   fparms[0]
    colname1    =   fparms[1]
    tdcolname   =   fparms[2] 
    
    df          =   cfg.get_dfc_dataframe()
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
        elif(not ((is_datetime_column(df,colname)) or (get_datatype_id(df[colname].dtype) == 11) ) ):
            opstat.set_errorMsg(colname + " is not a datetime column")
            opstat.set_status(False)
        elif(0):#not is_datetime_column(colname1) ) :
            opstat.set_errorMsg(colname1 + " is not a datetime column")
            opstat.set_status(False)
        
    if(opstat.get_status()) :
    
        if(display) :
            clock = RunningClock()
            clock.start()
    
        try :

            from dfcleanser.common.common_utils import YEARS, DAYS, HOURS, MINUTES, SECONDS, MICROSECONDS, TIMEDELTA
            from dfcleanser.data_transform.data_transform_columns_widgets import add_column
            import pandas as pd
            
            timedeltacol = df[colname] - df[colname1]
            add_column(tdcolname,timedeltacol,opstat)

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
                           "from dfcleanser.data_transform.data_transform_columns_widgets import process_datetime_timedelta_transform",
                           "process_datetime_timedelta_transform(" + json.dumps(parms) + ",False)"],opstat)
            
            dtw.display_main_taskbar()
            print("\n")
            display_status("Timedelta values stored successfully in " + tdcolname)
            display_column_transform_status(cfg.get_dfc_dataframe(),tdcolname)
        
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
        
                from dfcleanser.data_transform.data_transform_columns_widgets import add_column
                add_column(datecolumn,splitdate,opstat)
                add_column(timecolumn,splittime,opstat)
        
            # convert to .date or .time         
            except Exception as e:
                opstat.store_exception("Error changing "  + colname + " to datetime datatype ",e)
        
            if(display) :
                clock.stop()
    
            if(opstat.get_status()) : 
                
                if(display) :
                    
                    #make scriptable
                    add_to_script(["# split date time columns ",
                                   "from dfcleanser.data_transform.data_transform_widgets import process_datetime_merge_split_transform",
                                   "process_datetime_merge_split_transform(" + json.dumps(parms) + ",False)"],opstat)
                
                    dtw.display_main_taskbar()
                    print("\n")
                    display_status("Column " + datetimecolumn + " split successfully to " + datecolumn +" : " + timecolumn)
                    dtw.display_col_data(cfg.get_dfc_dataframe(),datetimecolumn)
                    dtw.display_col_data(cfg.get_dfc_dataframe(),datecolumn)
                    dtw.display_col_data(cfg.get_dfc_dataframe(),timecolumn)

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
        
                from dfcleanser.data_transform.data_transform_columns_widgets import add_column
                add_column(datetimecolumn,mergeddatetime,opstat)
        
            # convert to .date or .time         
            except Exception as e:
                opstat.store_exception("Error changing "  + colname + " to datetime datatype ",e)
    
            if(display) :
                clock.stop()
        
            if(opstat.get_status()) : 
                
                if(display) :
                    
                    #make scriptable
                    add_to_script(["# merge date time columns ",
                                   "from dfcleanser.data_transform.data_transform_widgets import process_datetime_merge_split_transform",
                                   "process_datetime_merge_split_transform(" + json.dumps(parms) + ",False)"],opstat)
                    
                    dtw.display_main_taskbar()
                    print("\n")
                    display_status("Columns " + datecolumn + ":" + timecolumn +" merged successfully to " + datetimecolumn)
                    dtw.display_col_data(cfg.get_dfc_dataframe(),datetimecolumn)
        
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


"""
#--------------------------------------------------------------------------
#    change column datatype
#--------------------------------------------------------------------------
"""
def process_datatype_transform(parms,display=True) :

    opstat  =   opStatus()

    colname     =   parms[0]
    dtid        =   int(parms[1])
    dropflag    =   int(parms[2])
    nanvalue    =   float(parms[3])

    col_nans     =   cfg.get_dfc_dataframe()[colname].isnull().sum() 

    if(col_nans > 0) :
        if(not(dropflag)) :
            #TODO convert to native datatype
            if(len(parms[3]) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("No Nan fill value is specified")
            else : 
                try :
                    nanvalue = float(nanvalue)    
                except :
                    opstat.set_status(False)
                    opstat.set_errorMsg("Nan fill value is invalid")
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
            display_column_transform_status(cfg.get_dfc_dataframe(),colname)
        
        else :
        
            display_exception(opstat)
        

def clear_data_transform_data() :
    
    drop_owner_tables(cfg.DataTransform_ID)
    clear_data_transform_cfg_values()
    
def clear_data_transform_cfg_values() :
    from dfcleanser.data_transform.data_transform_dataframe_control import clear_dataframe_transform_cfg_values
    clear_dataframe_transform_cfg_values()
    
    from dfcleanser.data_transform.data_transform_columns_control import clear_dataframe_columns_transform_cfg_values
    clear_dataframe_columns_transform_cfg_values()
    
    return
    


    