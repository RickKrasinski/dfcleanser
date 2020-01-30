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

import dfcleanser.data_cleansing.data_cleansing_widgets as dcw

from dfcleanser.common.table_widgets import (dcTable, drop_owner_tables, get_table_value, SIMPLE)

from dfcleanser.common.common_utils import (display_exception, opStatus, single_quote, is_string_col,is_object_col,
                                            get_parms_for_input, RunningClock, is_datetime_col, is_datetime_type_col, display_status_note,
                                            is_existing_column, display_generic_grid, get_dtype_str_for_datatype,
                                            convert_df_cols_datatype, is_numeric_col, is_float_col, is_datetime64_col)

from dfcleanser.scripting.data_scripting_control import add_to_script

import pandas as pd

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
 

def display_final_status(opstat,dftitle=None,colname=None) :
    
    
    if(opstat.get_status()) :
        dtw.display_datetime_column_taskbar()
        print("\n")
        display_status_note(opstat.get_errorMsg())
        if( (not (dftitle is None)) and (not (colname is None)) ) :
            dcw.display_simple_col_stats(cfg.get_dfc_dataframe_df(dftitle),colname)
            
    else :
        dtw.display_datetime_column_taskbar()
        print("\n")
        display_exception(opstat)



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
    
    from dfcleanser.common.html_widgets import define_inputs, are_owner_inputs_defined
    if(not (are_owner_inputs_defined(cfg.DataTransform_ID)) ) :
        
        data_transform_Inputs   =   []
        
        for i in range(len(dtw.datatransform_inputs)) :
            data_transform_Inputs.append(dtw.datatransform_inputs[i])    

        for i in range(len(dtcw.datatransform_columns_inputs)) :
            data_transform_Inputs.append(dtcw.datatransform_columns_inputs[i])    

        for i in range(len(dtdw.datatransform_dataframe_inputs)) :
            data_transform_Inputs.append(dtdw.datatransform_dataframe_inputs[i])    

        define_inputs(cfg.DataTransform_ID,data_transform_Inputs)
    
    if(cfg.is_a_dfc_dataframe_loaded()) :

        # go ahead and process the command
        if(option == dtm.MAIN_OPTION) :
            if(not(parms is None)) :
                get_current_transform_df(parms)

            dtw.display_main_option(parms)
            if(parms is None) :
                clear_data_transform_data()

        else :
            
            # ----------------------------------------------
            # dataframe transform controls
            # ----------------------------------------------
            
            if(option == dtm.DISPLAY_COLUMN_NAMES_OPTIONS) :
                dtdw.display_dataframe_col_names_taskbar()
    
            elif(option == dtm.DISPLAY_INDICES_OPTIONS) :
                dtdw.display_dataframe_indices_taskbar()
            
            if( (option == dtm.DISPLAY_SAVE_COLUMN_NAMES_ROW) or
                (option == dtm.DISPLAY_ADD_COLUMN_NAMES_ROW) or
                (option == dtm.DISPLAY_CHANGE_COLUMN_NAMES) or
                (option == dtm.DISPLAY_WHITESPACE_COLUMN_NAMES) or
                (option == dtm.DISPLAY_SHOW_DF_INDEX) or
                (option == dtm.DISPLAY_SET_DF_INDEX) or
                (option == dtm.DISPLAY_RESET_DF_INDEX) or
                (option == dtm.DISPLAY_APPEND_TO_INDEX) or
                (option == dtm.DISPLAY_SORT_DF_INDEX) or
                (option == dtm.DISPLAY_SORT_COLUMN) or
                (option == dtm.DISPLAY_DROP_DUPLICATE_ROWS) or
                (option == dtm.DF_TRANSFORM_RETURN) or
                (option == dtm.DF_TRANSFORM_HELP) ) :
                
                dtdw.display_dataframe_options(option)
                
            elif( (option == dtm.PROCESS_SHOW_COLUMN_NAMES_ROW) or
                  (option == dtm.PROCESS_SAVE_COLUMN_NAMES_ROW) or
                  (option == dtm.PROCESS_ADD_COLUMN_NAMES_ROW) or
                  (option == dtm.PROCESS_CHANGE_COLUMN_NAMES) or
                  (option == dtm.PROCESS_DROP_COLUMN_NAMES_ROW) or
                  (option == dtm.PROCESS_WHITESPACE_COLUMN_NAMES) or
                  (option == dtm.PROCESS_SET_DF_INDEX) or
                  (option == dtm.PROCESS_RESET_DF_INDEX) or
                  (option == dtm.PROCESS_APPEND_TO_INDEX) or
                  (option == dtm.PROCESS_SORT_DF_INDEX) or
                  (option == dtm.PROCESS_SORT_COLUMN) or
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
                  (option == dtm.DISPLAY_CAT_COLUMN_EXCLUDE) or
                  (option == dtm.DISPLAY_CLEAR_COLUMN) or
                  (option == dtm.DISPLAY_SAVE_COLUMN) or
                  (option == dtm.DISPLAY_COPY_COLUMN) or
                  (option == dtm.DISPLAY_APPLY_COLUMN) or
                  (option == dtm.DISPLAY_APPLY_CHANGE_FN) or
                  (option == dtm.DISPLAY_APPLY_COLUMN_UNIQUES) or 
                  (option == dtm.DISPLAY_APPLY_USER_FN_COLUMN_UNIQUES) or 
                  (option == dtm.DISPLAY_APPLY_USER_FN_COLUMN) ) : 
                
                opstat  =   opStatus()
                
                try :
                
                    dtcw.display_column_transform_forms(option,parms)
                    
                except Exception as e:
                    opstat.store_exception("display column transform  : " + str(option),e)
                    display_exception(opstat)
                    
            elif(option == dtm.DISPLAY_CAT_COLUMN_EXTERNAL) :
                
                try :
                    
                    cfg.set_config_value(cfg.CURRENT_TRANSFORM_DF,cfg.get_config_value(cfg.CURRENT_CLEANSE_DF))
                    dtcw.display_column_transform_forms(dtm.DISPLAY_CAT_COLUMN,parms)
                    
                except Exception as e:
                    opstat.store_exception("display column transform  : " + str(option),e)
                    display_exception(opstat)
                
                  

            elif( (option == dtm.PROCESS_RENAME_COLUMN) or
                  (option == dtm.PROCESS_DROP_COLUMN) or
                  (option == dtm.PROCESS_SAVE_COLUMN) or
                  (option == dtm.PROCESS_SAVE_COLUMN_WITH_INDEX) or
                  (option == dtm.PROCESS_REORDER_COLUMNS) or
                  (option == dtm.PROCESS_COPY_COLUMN) or
                  (option == dtm.PROCESS_APPLY_COLUMN) or
                  (option == dtm.PROCESS_MAP_COLUMN) or
                  (option == dtm.PROCESS_DUMMIES_COLUMN) or
                  (option == dtm.PROCESS_CAT_COLUMN) or 
                  (option == dtm.PROCESS_CAT_COLUMN_EXCLUDE) or 
                  (option == dtm.PROCESS_CHANGE_DATATYPE_COLUMNS) or
                  (option == dtm.PROCESS_SAVE_USER_FUNC) or 
                  (option == dtm.PROCESS_DELETE_USER_FUNC) ) :
                
                dtcc.process_column_option(option,parms)

                
            # ----------------------------------------------
            # add column controls
            # ----------------------------------------------
            elif(option == dtm.DISPLAY_ADD_COLUMN) :
                 dtcw.display_add_cols_option(option,None)
                 
            elif(option == dtm.ADD_COLUMN_CLEAR) :
                print("dtm.ADD_COLUMN_CLEAR")
                 
            elif( (option == dtm.DISPLAY_ADD_COLUMN) or     
                  (option == dtm.DISPLAY_ADD_FROM_FILE_OPTION) or
                  (option == dtm.DISPLAY_ADD_FROM_FILE_WITH_INDEX_OPTION) or
                  (option == dtm.DISPLAY_ADD_FROM_CODE_OPTION) or
                  (option == dtm.DISPLAY_ADD_FROM_DFC_FUNCS) or
                  (option == dtm.DISPLAY_ADD_FROM_DFC_FUNCS_PARMS) or
                  (option == dtm.DISPLAY_ADD_FROM_DF_OPTION) or 
                  (option == dtm.DISPLAY_MAINTAIN_USER_FUNC) or 
                  (option == dtm.DISPLAY_ADD_FROM_CODE_FN_OPTION)) :
                
                dtcw.display_add_cols_option(option,parms)
            
            elif( (option == dtm.PROCESS_ADD_FROM_FILE_OPTION) or
                  (option == dtm.PROCESS_ADD_FROM_FILE_WITH_INDEX_OPTION) or
                  (option == dtm.PROCESS_ADD_FROM_CODE_OPTION) or
                  (option == dtm.PROCESS_ADD_FROM_DFC_FUNCS) or
                  (option == dtm.PROCESS_ADD_FROM_DF_OPTION) ) :
                
                dtcc.process_column_option(option,parms)
                #dtcc.process_add_column(option,parms,display=True)
                
            # ----------------------------------------------
            # datetime processing
            # ----------------------------------------------
      
            elif( (option == dtm.DISPLAY_DATETIME_OPTION) or 
                  (option == dtm.DISPLAY_DATETIME_FORMAT_OPTION) ):
                dtw.display_datetime_column_taskbar()
                dtw.display_datetime_convert(option,parms)
            
            elif(option == dtm.DISPLAY_DATETIME_TIMEDELTA_OPTION):
                dtw.display_datetime_column_taskbar()
                dtw.display_timedelta_convert(parms)
                
            elif(option == dtm.DISPLAY_TIMEDELTA_CALCULATE_OPTION):
                dtw.display_datetime_column_taskbar()
                dtw.display_datetime_timedelta(parms)
                
            elif(option == dtm.DISPLAY_DATETIME_SPLIT_OPTION):
                dtw.display_datetime_column_taskbar()
                dtw.display_datetime_split_merge(parms,dtm.SPLIT)
                
            elif(option == dtm.DISPLAY_DATETIME_MERGE_OPTION):
                dtw.display_datetime_column_taskbar()
                dtw.display_datetime_split_merge(parms,dtm.MERGE)
                
            elif(option == dtm.DISPLAY_DATETIME_COMPONNETS_OPTION):
                dtw.display_datetime_column_taskbar()
                dtw.display_datetime_components(parms)
            
            elif(option == dtm.DISPLAY_DATETIME_COMP_TD_OPTION):
                dtw.display_datetime_column_taskbar()
                dtw.display_datetime_components(parms,True)
                
            elif(option == dtm.PROCESS_DATETIME_OPTION) :
                opstat  =   process_datetime_datatype_transform(parms)
                fparms  =   get_parms_for_input(parms,dtw.datetime_format_input_idList)
                display_final_status(opstat,cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF),fparms[0])
                
            elif(option == dtm.PROCESS_DATETIME_TIMEDELTA_OPTION) :
                opstat  =   process_timedelta_datatype_transform(parms)
                fparms  =   get_parms_for_input(parms,dtw.timedelta_format_input_idList)
                display_final_status(opstat,cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF),fparms[0])        
                
            elif(option == dtm.PROCESS_TIMEDELTA_CALCULATE_OPTION) :
                opstat  =   process_datetime_timedelta_transform(parms)
                fparms  =   get_parms_for_input(parms,dtw.datetime_tdelta_input_idList)
                display_final_status(opstat,cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF),fparms[2])        

            elif(option == dtm.PROCESS_DATETIME_MERGE_OPTION) :
                opstat  =   process_datetime_merge_split_transform(dtm.MERGE,parms)
                
            elif(option == dtm.PROCESS_DATETIME_SPLIT_OPTION) :
                opstat  =   process_datetime_merge_split_transform(dtm.SPLIT,parms)
            
            elif(option == dtm.PROCESS_DATETIME_COMPONNETS_OPTION) :
                opstat  =   process_get_datetime_component(parms)
                fparms  =   get_parms_for_input(parms,dtw.datetime_comp_input_idList)
                display_final_status(opstat,cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF),fparms[1])        
        
            # ----------------------------------------------
            # change datetype processing
            # ----------------------------------------------
            elif(option == dtm.DISPLAY_DATATYPE_COLUMN) :
                dtcw.display_column_transform_forms(option,parms)
            
            elif(option == dtm.DISPLAY_DATATYPE_CHANGE_NA) :
                dtcw.display_column_transform_forms(option,parms)
                
            elif(option == dtm.DISPLAY_DATATYPE_UNIQUES) :  
                df          =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
                colname     =   cfg.get_config_value(cfg.DATA_TRANSFORM_COL_SELECTED_KEY)
                
                dtcw.get_uniques_display(df,colname)

            # ----------------------------------------------
            # check compatability options
            # ----------------------------------------------
            elif(option == dtm.DISPLAY_CHECK_COMPATABILITY) :  
                dtcw.display_column_transform_forms(option,parms)
            
            elif(option == dtm.DISPLAY_CHECK_COMPATABILITY_UNIQUES) :  
                dtcw.display_column_transform_forms(option,None)
                
            elif(option == dtm.PROCESS_CHECK_COMPATABILITY) :
                dtcw.display_column_transform_forms(dtm.DISPLAY_CHECK_COMPATABILITY,parms)
                process_dfchknum_transform(parms)

            # ----------------------------------------------
            # check datatype return
            # ----------------------------------------------
            elif(option == dtm.PROCESS_DATETIME_RETURN) :  
                dtw.display_datetime_column_taskbar()

            # ----------------------------------------------
            # external datetype change from cleansing
            # ----------------------------------------------
            elif(option == dtm.DISPLAY_DATATYPE_OPTION) :
            
                colname =   cfg.get_config_value(cfg.CLEANSING_COL_KEY)
                cfg.set_config_value(cfg.CURRENT_TRANSFORM_DF,
                                     cfg.get_config_value(cfg.CURRENT_CLEANSE_DF))
                
                df      =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
                
                dtcw.display_convert_datatype(df,colname,False,False,cfg.DataCleansing_ID)

            elif(option == dtm.PROCESS_DATATYPE_OPTION) :            
                print("dtm.PROCESS_DATATYPE_OPTION",parms)
            
                df          =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
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
        
        clear_data_transform_data()
        cfg.drop_config_value(cfg.CURRENT_TRANSFORM_DF)
        
        if(not(option == dtm.MAIN_OPTION)) :
            cfg.display_no_dfs(cfg.DataTransform_ID)
            
        else :
            dtw.display_main_option(None)
            
                             
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    datetime processng methods
#--------------------------------------------------------------------------
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
    
    opstat  =   opStatus()
    
    fparms  =   get_parms_for_input(parms,dtw.datetime_format_input_idList)
    
    colname     =   fparms[0]
    natthresh   =   fparms[1]
    
    if(len(natthresh) == 0) :
        natthresh   =   None
    else :
        try :
            natthresh   =   float(natthresh)    
        except :
            opstat.set_errorMsg("NaT threshold of '" + str(natthresh) + "' is invalid")
            opstat.set_status(False)
            
    if(opstat.get_status()) :
        
        cerrors     =   fparms[2]
    
        if(cerrors.find(dtw.error_handlers[0]) > -1)    :  cerrors     =   dtw.error_handlers[0]
        elif(cerrors.find(dtw.error_handlers[1]) > -1)  :  cerrors     =   dtw.error_handlers[1]
        elif(cerrors.find(dtw.error_handlers[2]) > -1)  :  cerrors     =   dtw.error_handlers[2]
        else                                            :  cerrors     =   dtw.error_handlers[1]                                            
    
        fstring     =   fparms[3]
        
        df          =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
    
        import pandas as pd

        fstring     =   fstring.strip(" ")
        fstring     =   fstring.rstrip(" ") 
    
        if(display) :
            clock = RunningClock()
            clock.start()
    
        try :
            
            if(not (natthresh is None)) :
        
                tdf_data    =   df[colname]
                tdf_dtype   =   df[colname].dtype
        
                tempdf      =   pd.DataFrame(data=tdf_data, dtype=tdf_dtype, columns = [colname])
        
                if(len(fstring) > 0) :
                    tempdf[colname] = pd.to_datetime(tempdf[colname], errors=cerrors, format=fstring)
                else :
                    tempdf[colname] = pd.to_datetime(tempdf[colname], errors=cerrors)
                
                total_nats  =   tempdf[colname].isnull().sum()
                
                if( (total_nats/len(tempdf)) < (natthresh * 0.01) ) :
                    df[colname]     =   tempdf[colname]
                    opstat.set_errorMsg("Column '" + colname +"' data type converted successfully to datetime64.")
                else :
                    df_nats     =   float("{0:.2f}".format((total_nats/len(tempdf)*100)))
                    opstat.set_errorMsg("Column '" + colname +"' data type not converted. " + "Convert NaTs " + str(df_nats) + "% exceeds threshold of " + str(natthresh) + "%.")
                    
            else :
                
                if(len(fstring) > 0) :
                    df[colname] = pd.to_datetime(df[colname], errors=cerrors, format=fstring)
                else :
                    df[colname] = pd.to_datetime(df[colname], errors=cerrors)
                    
                opstat.set_errorMsg("Column '" + colname +"' data type converted successfully to datetime64.")
                
            #cfg.set_dfc_dataframe_df(cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF),df)
            cfg.set_current_chapter_df(cfg.DataTransform_ID,df,opstat)
            
        except Exception as e:
            opstat.store_exception("Error converting '"  + colname + "' to datetime64 datatype. Check total nans in column. ",e)
    
        if(display) :
            clock.stop()
        
        if(opstat.get_status()) : 
        
            if(display) :
            
                #make scriptable
                add_to_script(["# change column datatype to datetime",
                               "from dfcleanser.data_transform.data_transform_control import process_datetime_datatype_transform",
                               "process_datetime_datatype_transform(" + single_quote(colname) + "," + json.dumps(fparms) + ",False)"],
                                opstat)

                
        
    return(opstat)
    
    
def process_timedelta_datatype_transform(parms,display=True) :
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
    
    opstat  =   opStatus()
    
    fparms  =   get_parms_for_input(parms,dtw.timedelta_format_input_idList)
    
    colname     =   fparms[0]
    natthresh   =   fparms[1]
    units       =   fparms[2]
    cerrors     =   fparms[3]
    
    if(cerrors.find(dtw.error_handlers[0]) > -1)    :  cerrors     =   dtw.error_handlers[0]
    elif(cerrors.find(dtw.error_handlers[1]) > -1)  :  cerrors     =   dtw.error_handlers[1]
    elif(cerrors.find(dtw.error_handlers[2]) > -1)  :  cerrors     =   dtw.error_handlers[2]
    else                                            :  cerrors     =   dtw.error_handlers[1]                                            
    
    if(len(natthresh) == 0) :
        natthresh   =   None
    else :
        try :
            natthresh   =   float(natthresh)    
        except :
            opstat.set_errorMsg("NaT threshold of '" + str(natthresh) + "' is invalid")
            opstat.set_status(False)
            
    if(opstat.get_status()) :
    
        df          =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
    
        import pandas as pd

        if(display) :
            clock = RunningClock()
            clock.start()
    
        try :
        
            if(not (natthresh is None)) :
        
                tdf_data    =   df[colname]
                tdf_dtype   =   df[colname].dtype
        
                tempdf      =   pd.DataFrame(data=tdf_data, dtype=tdf_dtype, columns = [colname])
        
                tempdf[colname] = pd.to_timedelta(tempdf[colname], unit=units, errors=cerrors) 
                
                total_nats  =   tempdf[colname].isnull().sum()
                
                if( (total_nats/len(tempdf)) < (natthresh * 0.01) ) :
                    df[colname]     =   tempdf[colname]
                    opstat.set_errorMsg("Column '" + colname +"' data type converted successfully to datetime64.")
                    
                else :
                    df_nats     =   float("{0:.2f}".format((total_nats/len(tempdf)*100)))
                    opstat.set_errorMsg("Column '" + colname +"' data type not converted. " + "Convert NaTs " + str(df_nats) + "% exceeds threshold of " + str(natthresh) + "%.")
        
            else :
        
                df[colname] = pd.to_timedelta(df[colname], unit=units, errors=cerrors)
                opstat.set_errorMsg("Column '" + colname +"' data type converted successfully to datetime64.")
                
        except Exception as e:
            opstat.store_exception("Error converting '"  + colname + "' to timedelta ",e)
    
        if(display) :
            clock.stop()
        
        if(opstat.get_status()) : 
        
            if(display) :
            
                #make scriptable
                add_to_script(["# change column datatype to timedelta",
                               "from dfcleanser.data_transform.data_transform_control import process_timedelta_datatype_transform",
                               "process_timedelta_datatype_transform(" + single_quote(colname) + "," + json.dumps(fparms) + ",False)"],
                                opstat)

    return(opstat)
    
    
    
    

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
    
    fparms  =   get_parms_for_input(parms,dtw.datetime_tdelta_input_idList)

    
    colname     =   fparms[0]
    colname1    =   fparms[1]
    tdcolname   =   fparms[2] 
    tdeltaflg   =   fparms[3]
    units       =   fparms[4]
    
    df          =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
    
    found       =   False
    found1      =   False
    
    # check that input parms are ok
    if(len(colname) == 0) :
        opstat.set_errorMsg("'" + colname + "' is not a valid column name")
        opstat.set_status(False)
    elif(len(colname1) == 0) :
        opstat.set_errorMsg("'" + colname1 + "' is not a valid column name")
        opstat.set_status(False)
    elif(len(tdcolname) == 0) :
        opstat.set_errorMsg("'" + tdcolname + "' is not a valid column name")
        opstat.set_status(False)
    elif(is_existing_column(df,tdcolname)) :
        opstat.set_errorMsg("'" + tdcolname + "' is already defined")
        opstat.set_status(False)
    else :
        
        df_cols     =   df.columns.tolist()
        for i in range(len(df_cols)) :
            if(df_cols[i] == colname)   :   found = True
            if(df_cols[i] == colname1)  :   found1 = True
    
        if(not found) :
            opstat.set_errorMsg("'" + colname + "' is not a dataframe column")
            opstat.set_status(False)
        elif(not found1) :
            opstat.set_errorMsg("'" + colname1 + "' is not a dataframe column")
            opstat.set_status(False)
        elif( (not (is_datetime_col(df,colname))) and (not (is_datetime64_col(df,colname))) ):
            opstat.set_errorMsg("'" + colname + "' is not a datetime compatable column")
            opstat.set_status(False)
        
    if(opstat.get_status()) :
        
        if(display) :
            clock = RunningClock()
            clock.start()
    
        try :

            timedeltacol = df[colname] - df[colname1]
            
            if(tdeltaflg == "timedelta") :
                df  =   dtcc.add_column_to_df(df,tdcolname,timedeltacol,opstat)
                
            else :
                
                if(units == "Seconds")              :   timedeltacol = timedeltacol.apply(lambda x: x.total_seconds())
                elif(units == "MilliSeconds")       :   timedeltacol = timedeltacol.apply(lambda x: x.total_seconds() * 1000)
                elif(units == "MicroSeconds")       :   timedeltacol = timedeltacol.apply(lambda x: x.total_seconds() * 1000 * 1000)
                elif(units == "Minutes")            :   timedeltacol = timedeltacol.apply(lambda x: x.total_seconds() / 60)
                elif(units == "Hours")              :   timedeltacol = timedeltacol.apply(lambda x: x.total_seconds() / 3600)
                elif(units == "Days")               :   timedeltacol = timedeltacol.apply(lambda x: x.total_seconds() / (3600*24))
                
                df  =   dtcc.add_column_to_df(df,tdcolname,timedeltacol,opstat)
            
            cfg.set_current_chapter_df(cfg.DataTransform_ID,df,opstat) 
            df  =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
                    
        # convert to .date or .time         
        except Exception as e:
            opstat.store_exception("Error getting timedelta between '"  + colname + "' : '" + colname1 + "'",e)
    
        if(display) :
            clock.stop()
        
    if(opstat.get_status()) : 
        
        if(display) :
        
            #make scriptable
            add_to_script(["# calculate timedelta values ",
                           "from dfcleanser.data_transform.data_transform_control import process_datetime_timedelta_transform",
                           "process_datetime_timedelta_transform(" + json.dumps(parms) + ",False)"],opstat)
                
            opstat.set_errorMsg("Timedelta values stored successfully in '" + tdcolname + "' as " + units)
            
    return(opstat)
        


def process_datetime_merge_split_transform(action,parms,display=True) :
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
    
    if(action == dtm.SPLIT) :
        fparms  =   get_parms_for_input(parms,dtw.datetime_split_input_idList)
    else :
        fparms  =   get_parms_for_input(parms,dtw.datetime_merge_input_idList)
    
    colname = fparms[0]

    df = cfg.get_current_chapter_df(cfg.DataTransform_ID)
    
    if(display) :
        clock = RunningClock()
        clock.start()
    
    if(action == dtm.SPLIT) :
        
        datetimecolumn  =   fparms[0]
        datecolumn      =   fparms[1]
        timecolumn      =   fparms[2]
        
        if(not (is_existing_column(df,datetimecolumn))) :
            opstat.set_errorMsg("'" + datetimecolumn + "' is not defined")
            opstat.set_status(False)
        elif(is_existing_column(df,datecolumn)) :
            opstat.set_errorMsg("'" + datecolumn + "' is already defined")
            opstat.set_status(False)
        elif(is_existing_column(df,timecolumn)) :
            opstat.set_errorMsg("'" + timecolumn + "' is already defined")
            opstat.set_status(False)
        
        if(opstat.get_status()) :
        
            splitdate       =   []
            splittime       =   []
        
            try :
                
                splitdate = df[datetimecolumn].apply(lambda x: x.date())            
                splittime = df[datetimecolumn].apply(lambda x: x.time())  
        
                df  =   dtcc.add_column_to_df(df,datecolumn,splitdate,opstat)
                cfg.set_current_chapter_df(cfg.DataTransform_ID,df,opstat) 
                df  =   cfg.get_current_chapter_df(cfg.DataTransform_ID)  
                
                if(opstat.get_status()) :
                    df  =   dtcc.add_column_to_df(df,timecolumn,splittime,opstat)
                    cfg.set_current_chapter_df(cfg.DataTransform_ID,df,opstat)
                    df  =   cfg.get_current_chapter_df(cfg.DataTransform_ID)  
                    
                    if(0):#opstat.get_status()) :
                        df[datecolumn]  =   df[datecolumn].astype(datetime.date)
                        df[timecolumn]  =   df[timecolumn].astype(datetime.time)
        
            # convert to .date or .time         
            except Exception as e:
                opstat.store_exception("Error splitting '"  + colname + "' to date and time columns ",e)
        
            if(display) :
                clock.stop()
    
            if(opstat.get_status()) : 
                
                if(display) :
                    
                    #make scriptable
                    add_to_script(["# split date time columns ",
                                   "from dfcleanser.data_transform.data_transform_control import process_datetime_merge_split_transform",
                                   "process_datetime_merge_split_transform(" + str(action) + "," + json.dumps(parms) + ",False)"],opstat)
                    
                    dtw.display_datetime_column_taskbar()
                    print("\n")
                    display_status_note("Column '" + datetimecolumn + "' split successfully to '" + datecolumn +"' : '" + timecolumn + "'")
                    cfg.delete_df(df)
                    df = cfg.get_current_chapter_df(cfg.DataTransform_ID)
                    dcw.display_simple_col_stats(df,datecolumn)
                    dcw.display_simple_col_stats(df,timecolumn)

                else :
                    dtw.display_datetime_column_taskbar()
                    print("\n")
                    display_exception(opstat)
                
            else :
        
                if(display) :
                    dtw.display_datetime_column_taskbar()
                    print("\n")
                    display_exception(opstat)
                    
        else :
        
            if(display) :
                dtw.display_datetime_column_taskbar()
                print("\n")
                display_exception(opstat)
        
    else :
    
        datecolumn      =   fparms[0]
        timecolumn      =   fparms[1]
        datetimecolumn  =   fparms[2]
        
        if(is_existing_column(df,datetimecolumn)) :
            opstat.set_errorMsg("'" + datetimecolumn + "' is already defined")
            opstat.set_status(False)
        if(len(datetimecolumn) == 0) :
            opstat.set_errorMsg("'" + datetimecolumn + "' datetime+column_name is invalid")
            opstat.set_status(False)
        elif(not (is_existing_column(df,datecolumn))) :
            opstat.set_errorMsg("'" + datecolumn + "' is not defined")
            opstat.set_status(False)
        elif(not (is_existing_column(df,timecolumn))) :
            opstat.set_errorMsg("'" + timecolumn + "' is not defined")
            opstat.set_status(False)
        
        if(opstat.get_status()) :
    
            mergeddatetime  =   []
        
            try :
            
                for i in range(len(df[datecolumn])) :
                    mergeddatetime.append(datetime.datetime.combine(df[datecolumn][i],df[timecolumn][i]))
        
                df  =   dtcc.add_column_to_df(df,datetimecolumn,mergeddatetime,opstat)
                cfg.set_current_chapter_df(cfg.DataTransform_ID,df,opstat)
                df  =   cfg.get_current_chapter_df(cfg.DataTransform_ID)  
        
            # convert to .date or .time         
            except Exception as e:
                opstat.store_exception("Error merging '"  + datetimecolumn + "' from date time columns ",e)
    
            if(display) :
                clock.stop()
        
            if(opstat.get_status()) : 
                
                if(display) :
                    
                    #make scriptable
                    add_to_script(["# merge date time columns ",
                                   "from dfcleanser.data_transform.data_transform_control import process_datetime_merge_split_transform",
                                   "process_datetime_merge_split_transform(" + str(action) + "," + json.dumps(parms) + ",False)"],opstat)
                    
                    dtw.display_datetime_column_taskbar()
                    print("\n")
                    display_status_note("Columns '" + datecolumn + "' : '" + timecolumn +"' merged successfully to '" + datetimecolumn + "'")
                    dcw.display_simple_col_stats(df,datetimecolumn)
        
            else :
        
                if(display) :
                    dtw.display_datetime_column_taskbar()
                    print("\n")
                    display_exception(opstat)

        else :
        
            if(display) :
                dtw.display_datetime_column_taskbar()
                print("\n")
                display_exception(opstat)
            
    return(opstat)


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
    
    opstat  =   opStatus()

    fparms      =   get_parms_for_input(parms,dtw.datetime_comp_input_idList)
    
    df = cfg.get_current_chapter_df(cfg.DataTransform_ID)
    
    colname         =   fparms[0]
    rescolname      =   fparms[1]
    comptype        =   fparms[2]
    
    coldtype        =   "datetime"    
    colvalslist     =   []
    
    if(not (is_existing_column(df,colname))) :
        opstat.set_errorMsg("'" + colname + "' is not defined")
        opstat.set_status(False)
    elif(not (is_datetime64_col(df,colname))) :
        opstat.set_errorMsg("'" + colname + "' is not datetime compatable datatype")
        opstat.set_status(False)
    elif(is_existing_column(df,rescolname)) :
        opstat.set_errorMsg("'" + rescolname + "' is already defined")
        opstat.set_status(False)
        
    if(opstat.get_status()) :
        
        if(display) :
            clock = RunningClock()
            clock.start()
        
        try :
            
            if(coldtype == "datetime") :
                        
                didx    =  pd.DatetimeIndex(df[colname]) 
        
                if(comptype == "date")              :   colvalslist     =   didx.date
                elif(comptype == "year")            :   colvalslist     =   didx.year
                elif(comptype == "quarter")         :   colvalslist     =   didx.quarter
                elif(comptype == "month")           :   colvalslist     =   didx.month
                elif(comptype == "week")            :   colvalslist     =   didx.week
                elif(comptype == "week of year")    :   colvalslist     =   didx.weekofyear
                elif(comptype == "day")             :   colvalslist     =   didx.day
                elif(comptype == "day of year")     :   colvalslist     =   didx.dayofyear
                elif(comptype == "day of week")     :   colvalslist     =   didx.dayofweek
                elif(comptype == "time")            :   colvalslist     =   didx.time
                elif(comptype == "hour")            :   colvalslist     =   didx.hour
                elif(comptype == "minute")          :   colvalslist     =   didx.minute
                elif(comptype == "second")          :   colvalslist     =   didx.second
                elif(comptype == "microsecond")     :   colvalslist     =   didx.microsecond
                elif(comptype == "nanosecond")      :   colvalslist     =   didx.nanosecond
                else :
                    opstat.set_errorMsg("datetime component type " + comptype + " is not supported")
                    opstat.set_status(False)
                    
            else :
                
                tdidx    =  pd.TimedeltaIndex(df[colname]) 
                
                if(comptype == "days")              :   colvalslist     =   tdidx.date
                elif(comptype == "seconds")         :   colvalslist     =   tdidx.seconds
                elif(comptype == "microseconds")    :   colvalslist     =   tdidx.microseconds
                elif(comptype == "nanoseconds")     :   colvalslist     =   tdidx.nanoseconds
                
                else :
                    opstat.set_errorMsg("timedelta component type " + comptype + " is not supported")
                    opstat.set_status(False)
                    
            df  =   dtcc.add_column_to_df(df,rescolname,colvalslist,opstat)
            cfg.set_current_chapter_df(cfg.DataTransform_ID,df,opstat)
            df  =   cfg.get_current_chapter_df(cfg.DataTransform_ID)  
        
        except Exception as e:
            opstat.store_exception("Error getting '"  + colname + "' datetime components ",e)

        if(display) :
            clock.stop()

    if(opstat.get_status()) : 
        
        if(display) :
            
            #make scriptable
            add_to_script(["# retrieve datetime component ",
                           "from dfcleanser.data_transform.data_transform_control import process_get_datetime_component",
                           "process_get_datetime_component(" + json.dumps(fparms) + ",False)"],
                            opstat)

            opstat.set_errorMsg(comptype + " for column '" + colname +"' stored successfully in '" + rescolname + "'")
        
    return(opstat)
    

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
    
    df          =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
    col_nans    =   df[colname].isnull().sum() 

    if(col_nans > 0) :
        if(nafunc == "fillna") :
            nanvalue    =   get_nan_value(dtid, nanmethod, parms[3], opstat)        
        else :
            nanvalue = None
            
    if(opstat.get_status())  :          
        currentdtype = df[colname].dtype
    
        if( (dtid == -1) ) :
            opstat.set_status(False)
            opstat.set_errorMsg("Unable to convert data type - No New Data Type Selected")
        
    if(opstat.get_status()) :
        dtstr = get_dtype_str_for_datatype(currentdtype) 

        if((dtstr == "datetime.datetime") ) :
            
            convparms = [dtstr,colname,nanvalue]
            from dfcleanser.data_transform.data_transform_widgets import display_datetime_convert
            display_datetime_convert(convparms)
            return()
            
        else :
            if(dtid > 11) :
                dtid = dtid + 3
                
            opstat = convert_df_cols_datatype(df,[colname],dtid,nanvalue)
    
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

            display_status_note("Column " + colname +" data type changed successfully to " + get_dtype_str_for_datatype(currentdtype))
            dcw.display_simple_col_stats(df,colname)
        
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


def convert_datetime_value(value,desireddatatype) :
    """
    * -------------------------------------------------------------------------- 
    * function : convert datetime data type
    * 
    * parms :
    *   value           -   value to convert
    *   valuedatatype   -   value data type
    *   desireddatatype -   desired datatype
    *
    * returns : 
    *  True - False
    * --------------------------------------------------------
    """
    
    import datetime
    import numpy as np
    import pandas as pd

    try :
                    
        if(desireddatatype == "datetime.datetime")      :   datetime.datetime(value)
        elif(desireddatatype == "datetime.date")        :   datetime.date(value)
        elif(desireddatatype == "datetime.time")        :   datetime.time(value)
        elif(desireddatatype == "np.datetime64")        :   np.datetime64(value)
        elif(desireddatatype == "pd.Timestamp")         :   pd.Timestamp(value)
        
        return(True)
                
    except :

        return(False)

    
def check_datetime_compatability(df,colname,desireddatatype,samplesize) :
    """
    * -------------------------------------------------------------------------- 
    * function : check conversion compatability for a datetime object
    * 
    * parms :
    *   df              -   dataframe
    *   colname         -   column name
    *   desireddatatype -   datatype to convert to
    *   samplesize      -   percent to sample over
    *
    * returns : 
    *  list - [reason_code,reason_parms]
    * --------------------------------------------------------
    """
    
    print("check_datetime_compatability",colname,desireddatatype,samplesize)

    reason_code     =   dtm.VALUES_OK
    reason_parms    =   []
    
    uniques         =   df[colname].unique().tolist()
    
    if(samplesize == 100) :
        loopsize    =   len(uniques)
    else :
        loopsize    =   len(uniques) * (samplesize * 0.01)
        
        
    for i in range(loopsize) :
                
        if(samplesize == 100)   :
            k   =   i
        else :
            import random
            k   =  random.randint(0,len(uniques)) 
                
            if( not(uniques[k].isnull())) :
                status  =   convert_datetime_value(uniques[k],desireddatatype)
            else :
                status  =   True
                
            if(not status) :
                reason_code     =   dtm.VALUE_NOT_DATATYPE_COMPATABLE
                reason_parms    =   [k,uniques[k]]
                break;
    
    return([reason_code,reason_parms])
    
    
def check_str_compatability(df,colname,desireddatatype,samplesize) :
    """
    * -------------------------------------------------------------------------- 
    * function : check conversion compatability for a datetime object or string  column
    * 
    * parms :
    *   df              -   dataframe
    *   colname         -   column name
    *   desireddatatype -   datatype to convert to
    *   samplesize      -   percent to sample over
    *
    * returns : 
    *  list - [reason_code,reason_parms]
    * --------------------------------------------------------
    """
    
    import numpy as np
    
    print("check_str_compatability",colname,desireddatatype,samplesize)

    reason_code     =   dtm.VALUES_OK
    reason_parms    =   []
    
    uniques             =   df[colname].unique().tolist()
    converted_uniques   =   []
    
    if(samplesize == 100) :
        loopsize    =   len(uniques)
    else :
        loopsize    =   len(uniques) * (samplesize * 0.01)
        
        
    for i in range(loopsize) :
                
        if(is_numeric_desiredtype(desireddatatype)) :
            
            minval  =   np.finfo(np.float64).max
            maxval  =   np.finfo(np.float64).min

            for i in range(loopsize) :
                
                if(samplesize == 100)   :
                    k   =   i
                else :
                    import random
                    k   =  random.randint(0,len(uniques)) 
                
                try :
                    
                    numval  =   uniques[k].replace('.','',1)
                    numval  =   numval.replace('-','',1)
                    if(not (numval.isdigit()) ) :  
                        reason_code     =   dtm.VALUE_NOT_NUMERIC
                        reason_parms    =   [k,uniques[k]]
                        break;
                    else :
                        if(float(uniques[k]) > maxval)     :   maxval  =   float(uniques[k])
                        elif(float(uniques[k]) < minval)   :   minval  =   float(uniques[k])
                        
                    converted_uniques   =   converted_uniques.append(float(uniques[k]))
                        
                except :
                        reason_code     =   dtm.VALUE_NOT_NUMERIC
                        reason_parms    =   [k,uniques[k]]
                        break;
                    
            
            if(reason_code == dtm.VALUES_OK) :
                str_compatability_data  =   check_numeric_compatability(df,colname,desireddatatype,float(minval),float(maxval),converted_uniques)
                reason_code             =   str_compatability_data[0]
                reason_parms            =   str_compatability_data[1]
        
            
        elif(is_dateime_desiredtype(desireddatatype)) :
            
            for i in range(loopsize) :
                
                if(samplesize == 100)   :
                    k   =   i
                else :
                    import random
                    k   =  random.randint(0,len(uniques)) 
                
                if( not(uniques[k].isnull())) :
                    status  =   convert_datetime_value(uniques[k],desireddatatype)
                else :
                    status  =   True
                
                if(not status) :
                    reason_code     =   dtm.VALUE_NOT_DATATYPE_COMPATABLE
                    reason_parms    =   [k,uniques[k]]
                    break;
            
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
        
        dt_compatability_data   =   check_datetime_compatability(df,colname,desireddatatype.samplesize)        
        reason_code             =   dt_compatability_data[0]
        reason_parms            =   dt_compatability_data[1]
            
    elif( (is_string_col(df,colname)) or (is_object_col(df,colname)) ) :
        
        str_compatability_data  =   check_str_compatability(df,colname,desireddatatype,samplesize)
        reason_code             =   str_compatability_data[0]
        reason_parms            =   str_compatability_data[1]
        
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
        sample_size =   None
    
    colname     =   fparms[0]
    check_list  =   fparms[1].split(",")
    
    df          =   cfg.get_current_chapter_df(cfg.DataTransform_ID) 
 
    if(is_numeric_col(df,colname)) :
        
        uniques     =   df[colname].unique().tolist()
    
        mincolval       =   min(uniques)
        maxcolval       =   max(uniques)
        
    else :
        
        mincolval       =   None
        maxcolval       =   None
        uniques         =   None
    
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
    
    print("display_check_compatability_status",colname,check_status_list,check_dtype_list)

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
    
    from dfcleanser.common.html_widgets import delete_all_inputs
    delete_all_inputs(cfg.DataTransform_ID)
    clear_data_transform_cfg_values()
    dtm.checknum_status.clear_chknum_status()    
    
def clear_data_transform_cfg_values() :
    
    dtdc.clear_dataframe_transform_cfg_values()
    dtcc.clear_dataframe_columns_transform_cfg_values()
    
    return
    


    