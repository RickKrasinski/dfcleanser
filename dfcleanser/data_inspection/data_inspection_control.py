"""
# data_inspection_control
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg
import dfcleanser.data_inspection.data_inspection_model as dim
import dfcleanser.data_inspection.data_inspection_widgets as diw

from dfcleanser.common.table_widgets import drop_owner_tables, dcTable

from dfcleanser.scripting.data_scripting_control import add_to_script

from dfcleanser.common.common_utils import (RunningClock, opStatus, display_exception, 
                                            get_parms_for_input, is_numeric_col,
                                            display_generic_grid, display_status)

from dfcleanser.common.display_utils import (display_column_names, display_df_describe)

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    data inspection process data functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


def display_data_inspection(option, parms=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : main data inspection processing
    * 
    * parms :
    *   option  -   function option
    *   parms   -   associated parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    from IPython.display import clear_output
    clear_output()
    
    no_df_selected  =   False
    
    opstat  =   opStatus()  
      
    # setup the checkbox form 
    current_checkboxes      =  []
    
    # display the default insoection data
    if(option == dim.MAIN_OPTION) :
        current_checkboxes     =   [False, False, False, False, False] 
        clear_data_inspection_data()
        
    # refresh the current insoection data     
    elif (option == dim.REFRESH_OPTION) : 
        
        # check if parms have checkbox flags
        if(not(parms==None)) :
            
            fparms  =   get_parms_for_input(parms[0],diw.data_inspection_df_input_idList)

            if(not (len(fparms) == 0) ) :
                #cfg.set_current_dfc_dataframe_title(fparms[0])
                cfg.set_config_value(cfg.CURRENT_INSPECTION_DF,fparms[0])
            else :
                no_df_selected  =   True
            
            import json
            inspcbs     =   json.loads(parms[1])
            
            for i in range(len(inspcbs)) :
                if(inspcbs[i] == "True") :   
                    current_checkboxes.append(True)
                else :
                    current_checkboxes.append(False)
    
        # no checkbox parms so read from cfg file
        else :
            parms = []
            diw.get_inspection_check_form_parms(parms,current_checkboxes)           
                
    else :

        inparm = parms
        parms = []
        diw.get_inspection_check_form_parms(parms,current_checkboxes)  


    diw.display_dfc_inspection_main(current_checkboxes)

    # parse the input parms
    if( (option == dim.DISPLAY_ROW_OPTION) or 
        (option == dim.DROP_ROWS_OPTION) or 
        (option == dim.DROP_COLS_OPTION) ) :
        
        if( option == dim.DISPLAY_ROW_OPTION ) :
            rowid = inparm
        else :
            
            thresholdType = inparm[0]
            
            if(option == dim.DROP_ROWS_OPTION) :
                fparms = diw.get_drop_rows_input_parms(inparm[1])
            else :
                fparms = diw.get_drop_cols_input_parms(inparm[1])
                
            threshold = int(fparms[0])
            
        parms = diw.get_drop_cbox_flags()
        parms = []
        
        if( option == dim.DISPLAY_ROW_OPTION ) :
            parms.append(rowid)
        
        if (option == dim.DROP_ROWS_OPTION) :
            
            drop_nan_rows(cfg.get_dfc_dataframe(),threshold,thresholdType,opstat)
            
            if(not(opstat.get_status())) :
                display_exception(opstat)    
            
        if (option == dim.DROP_COLS_OPTION) :
            
            drop_nan_cols(cfg.get_dfc_dataframe(),threshold,thresholdType,opstat) 
            
            if(not(opstat.get_status())) :
                display_exception(opstat)   
                
    if( (option == dim.REFRESH_OPTION)   or (option == dim.DISPLAY_ROW_OPTION) or 
        (option == dim.DROP_ROWS_OPTION) or (option == dim.DROP_COLS_OPTION) ) :

        if( (cfg.is_a_dfc_dataframe_loaded()) and
            (not (no_df_selected)) ) :

            clock = RunningClock()
            clock.start()

            df_data_info = dim.get_df_datatypes_data(cfg.get_current_chapter_df(cfg.CURRENT_INSPECTION_DF))

            clock.stop() 
            
            import json
            inspcbs     =   json.loads(parms[1])

            
            # if display data types
            if(inspcbs[dim.INSPECT_DATATYPES] == "True") : 
                
                opstat = opStatus()
                
                import matplotlib.pyplot as plt
                
                cfg.set_config_value(cfg.DATA_TYPES_CBOX_0_KEY,"True")
                
                print("\n")
                diw.print_page_separator("Data Types",0)
                
                clock = RunningClock()
                clock.start()

                try :                
                
                    data_types_table = dcTable("Column Data Types",
                                               "datatypesTable",
                                               cfg.DataInspection_ID)
                    data_types_html         =   diw.display_df_datatypes(data_types_table,df_data_info[0],df_data_info[1],df_data_info[2],False) 
                    
                    data_types_schema_tb    =   diw.get_inspection_dfschema_taskbar()
                    data_types_schema_tb.set_gridwidth(240)
                    data_types_schema_tb.set_customstyle({"font-size":13, "height":40, "width":240, "left-margin":10})
                    data_types_schema_html  =   data_types_schema_tb.get_html()

                    gridclasses     =   ["dfc-top","dfc-footer"]
                    gridhtmls       =   [data_types_html,data_types_schema_html]
                    
                    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                        display_generic_grid("df-inspection-data-type-wrapper",gridclasses,gridhtmls)
                    else :
                        display_generic_grid("df-inspection-data-type-pop-up-wrapper",gridclasses,gridhtmls)

                    print("\n")
                    import matplotlib.pyplot as plt
                    import numpy as np

                    font =  {'fontsize': 14 }
                    font2 = {'fontsize': 18 }
                
                    objects = []
                    for i in range(len(df_data_info[0])) :
                        ttype = str(df_data_info[0][i]) 
                        ttype = ttype.replace("datetime.","")
                        ttype = ttype.replace("datetime64[ns]","datetime")
                        ttype = ttype.replace("timedelta64[ns]","timedelta")
                        objects.append(ttype)    
                    y_pos = np.arange(len(objects))
                
                    plt.bar(y_pos, df_data_info[1], align='center', alpha=0.5, color='#428bca')
                    plt.xticks(y_pos, objects,rotation='vertical')
                    plt.ylabel('Type Counts',fontdict=font)
                    plt.xlabel('Data Types',fontdict=font)
                    plt.title('Column Data Types',fontdict=font2)
 
                    plt.show()
                
                except Exception as e:
                    opstat.store_exception("Error displaying data types\n ",e)

                clock.stop()
                
                if(not (opstat.get_status())) :
                    display_exception(opstat)
 
               
            # if display nan data
            if(inspcbs[dim.INSPECT_NANS] == "True") : 
                
                cfg.set_config_value(cfg.NANS_CBOX_1_KEY,"True")
                
                print("\n")
                diw.print_page_separator("NaNs Data",1)
                
                nans_rows_table = dcTable("Rows with most NaNs","nansrowTable",cfg.DataInspection_ID)
                nans_cols_table = dcTable("Columns with most NaNs","nansTable",cfg.DataInspection_ID)
                diw.display_null_data(cfg.get_current_chapter_df(cfg.CURRENT_INSPECTION_DF),
                                      nans_rows_table,nans_cols_table,120)
 
           
            # if display sample row data
            if(inspcbs[dim.INSPECT_ROWS] == "True") : 

                opstat = opStatus()
                
                cfg.set_config_value(cfg.ROWS_CBOX_2_KEY,"True")
                
                print("\n")
                diw.print_page_separator("Rows Data",2)
                
                clock = RunningClock()
                clock.start()

                try :                
                
                    row_stats_html      =   diw.display_row_stats(cfg.get_current_chapter_df(cfg.CURRENT_INSPECTION_DF),
                                                                  cfg.get_config_value(cfg.CURRENT_INSPECTION_DF),
                                                                  False)
                    rows_table          =   dcTable("Start Row","DIsamplerows",cfg.DataInspection_ID)
                    sample_row_html     =   diw.display_df_row_data(cfg.get_current_chapter_df(cfg.CURRENT_INSPECTION_DF),
                                                                    rows_table,0,0,opstat,False)
                    searchcols_form     =   diw.get_colsearch_form(cfg.get_current_chapter_df(cfg.CURRENT_INSPECTION_DF))
                    searchcols_html     =   searchcols_form.get_html()
                    
                    gridclasses     =   ["dfc-top","dfc-main","dfc-footer"]
                    gridhtmls       =   [row_stats_html,sample_row_html,searchcols_html]
                    
                    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                        display_generic_grid("df-inspection-row-data-wrapper",gridclasses,gridhtmls)
                    else :
                        display_generic_grid("df-inspection-row-data-pop-up-wrapper",gridclasses,gridhtmls)
             
                except Exception as e:
                    opstat.store_exception("Error displaying row data\n ",e)
                    import traceback
                    traceback.print_exc()

                clock.stop()
                
                if(not (opstat.get_status())) :
                    display_exception(opstat)

                    
            #if display column data
            if(inspcbs[dim.INSPECT_COLS] == "True") : 
                                
                opstat = opStatus()

                cfg.set_config_value(cfg.COLS_CBOX_3_KEY,"True")
                
                clock = RunningClock()
                clock.start()

                try : 
                    
                    print("\n")
                    diw.print_page_separator("Columns Data",3)
                    #print("\n")
                
                    col_names_table = dcTable("Column Names ","cnamesTable",cfg.DataInspection_ID)
                    column_names_html   =   display_column_names(cfg.get_current_chapter_df(cfg.CURRENT_INSPECTION_DF),
                                                                 col_names_table,"scol",False)   

                    df_cols     =   cfg.get_dfc_dataframe().columns.tolist()
                
                    found_numeric   =   False
                    for i in range(len(df_cols)) :
                        if( is_numeric_col(cfg.get_dfc_dataframe(),df_cols[i]) ) :
                            found_numeric   =   True
                            break
                    
                    if(found_numeric) :
                        num_col_names_table =   dcTable("Numeric Column Stats Numeric Column Stats","gendfdesc",cfg.DataInspection_ID)
                        num_col_stats_html  =   display_df_describe(cfg.get_current_chapter_df(cfg.CURRENT_INSPECTION_DF),
                                                                    num_col_names_table,None,None,False)
                
                        gridclasses     =   ["dfc-header","dfc-footer"]
                        gridhtmls       =   [column_names_html,num_col_stats_html]
    
                        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                            display_generic_grid("df-inspection-numeric-column-data-wrapper",gridclasses,gridhtmls)
                        else :
                            display_generic_grid("df-inspection-numeric-pop-up-column-data-wrapper",gridclasses,gridhtmls)
                    
                    else :
                    
                        gridclasses     =   ["dfc-header"]
                        gridhtmls       =   [column_names_html]
    
                        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                            display_generic_grid("df-inspection-nn-column-data-wrapper",gridclasses,gridhtmls)
                        else :
                            display_generic_grid("df-inspection-nn-pop-up-column-data-wrapper",gridclasses,gridhtmls)
                    
                except Exception as e:
                    opstat.store_exception("Error displaying column data\n ",e)

                clock.stop()
                
                if(not (opstat.get_status())) :
                    display_exception(opstat)

            #if display categories data
            if(inspcbs[dim.INSPECT_CATS] == "True") : 
                
                opstat = opStatus()

                cfg.set_config_value(cfg.CATS_CBOX_4_KEY,"True")
                print("\n")
                diw.print_page_separator("Category Data",4)
                
                clock = RunningClock()
                clock.start()
                
                try : 

                    cattable = dcTable("Category Columns",
                                       "catcolsTable",
                                       cfg.DataInspection_ID)

                    catcandidatetable = dcTable("Category Candidate Columns",
                                                "catcandcolsTable",
                                                cfg.DataInspection_ID)
                
                    numcats, numcands = diw.display_df_categories(cfg.get_current_chapter_df(cfg.CURRENT_INSPECTION_DF),
                                                                  cattable,catcandidatetable)
                    
                except Exception as e:
                    opstat.store_exception("Error displaying category data\n ",e)

                clock.stop()
                
                if(not (opstat.get_status())) :
                    display_exception(opstat)
                
        else :
            display_status("No Dataframe seleted for inspection", 1) 
            
    elif(option == dim.MATCH_VALS_OPTION) :
        
        opstat  =   opStatus()
        
        print("dim.MATCH_VALS_OPTION",inparm)
        column_type     =   inparm[0]
        
        fparms          =   get_parms_for_input(inparm[1],diw.data_inspection_colsearch_idList)
        
        cols_string     =   fparms[0]
        cols_list       =   cols_string.split(",")
        
        vals_string     =   fparms[1]
        
        if(len(vals_string) > 0) :
            
            vals_string     =   vals_string.replace("[","]")
            vals_string     =   vals_string.replace("[","]")
            vals_list       =   vals_string.split(",")
        
        else :
            vals_list   =   []
            
        if(len(vals_list) > 0) :
        
            from dfcleanser.common.common_utils import is_int_col
            df  =   cfg.get_current_chapter_df(cfg.CURRENT_INSPECTION_DF)        
        
            import pandas as pd
            final_criteria  =   pd.Series()
            
            for i in range(len(cols_list)) :
            
                for j in range(len(vals_list)) :
                
                    final_vals_list     =   []
                    
                    if(column_type == 0) :
                    
                        if(is_int_col(df,cols_list[i])) : 
                            try :
                                final_vals_list.append(int(vals_list[j]))
                            except :
                                status  =   False
                        else :
                            try :
                                final_vals_list.append(float(vals_list[j]))
                            except :
                                status  =   False
                                
                    else :
                        try :
                            final_vals_list.append(str(vals_list[j]))
                        except :
                            status  =   False
                            
                if(len(final_vals_list) > 0) :
                    
                    current_criteria    =   df[cols_list[i]].isin(final_vals_list)
                    final_criteria      =   final_criteria | current_criteria
                    
                    
                else :
                    opstat.set_status(False) 
                    opstat.set_errorMsg("no valid column_values entered for " + cols_list[i])
            
            # get the subset df
            clock = RunningClock()
            clock.start()
            
            search_df = df[final_criteria].copy()
            
            clock.stop() 
                
            from dfcleanser.common.cfg import dfc_dataframe,add_dfc_dataframe
            
            search_df_notes     =   "search subset from " + cfg.get_config_value(cfg.CURRENT_INSPECTION_DF)
            search_df_title     =   cfg.get_config_value(cfg.CURRENT_INSPECTION_DF) + "search"
            new_dfcdf           =   dfc_dataframe(search_df_title,search_df,search_df_notes)
            add_dfc_dataframe(new_dfcdf)
            
        else :
            opstat.set_status(False) 
            opstat.set_errorMsg("no column_values entered")
            
    from dfcleanser.common.display_utils import  display_pop_up_buffer   
    display_pop_up_buffer()


def drop_nan_rows(df,threshold,ttype,opstat,display=True) :
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
    
    if(display) :
            
        clock = RunningClock()
        clock.start()
        

    try     :
        if(ttype == dim.BY_PERCENT) : 
            thold   =   len(df.columns) * (float(threshold) * 0.01)
        else :
            thold   =   float(threshold)
     
        criteria = df.isnull().sum(axis=1) < thold

        df = df[criteria]
        cfg.set_current_dfc_dataframe(df)

    except Exception as e:
        opstat.store_exception("Error droppint nan rows\n ",e)

    if(display) :
        clock.stop()
        
        #make scriptable
        add_to_script(["# Drop NAN Rows ",
                       "from dfcleanser.data_inspection.data_inspection_control import drop_nan_rows",
                       "drop_nan_rows(" + str(threshold) + ",False)"],opstat)


def drop_nan_cols(df,threshold,ttype,opstat,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : drop cols with nans greater than threshold
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
    
    if(display) :
            
        clock = RunningClock()
        clock.start()

    try     :
        
        if(ttype == dim.BY_PERCENT) : 
            thold   =   len(df) * (float(threshold) * 0.01)
        else :
            thold   =   float(threshold)

        df_cols         =   df.columns
        colswithnulls   =   df.isnull().sum()
        droplist        =   []
    
        for i in range(len(colswithnulls)) :
            if(colswithnulls[i] >= thold) :
                droplist.append(df_cols[i])

        if(len(droplist) > 0) :
            df.drop(droplist,axis=1,inplace=True)

    except Exception as e:
        opstat.store_exception("Error droppint nan rows\n ",e)

    if(display) :
        
        clock.stop()
        
        #make scriptable try catch
        add_to_script(["# Drop NAN Cols ",
                       "from dfcleanser.data_inspection.data_inspection_control import drop_nan_cols",
                       "drop_nan_cols(" + str(threshold) + ",False)"],opstat)



"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   general housekeeping functions
#------------------------------------------------------------------
#------------------------------------------------------------------
"""  

     
def clear_data_inspection_data() :
    
    drop_owner_tables(cfg.DataInspection_ID)
    clear_data_inspection_cfg_values()
    
    
def clear_data_inspection_cfg_values() :
    
    cfg.drop_config_value(cfg.DATA_TYPES_CBOX_0_KEY)
    cfg.drop_config_value(cfg.NANS_CBOX_1_KEY)
    cfg.drop_config_value(cfg.ROWS_CBOX_2_KEY)
    cfg.drop_config_value(cfg.COLS_CBOX_3_KEY)
    cfg.drop_config_value(cfg.CATS_CBOX_4_KEY)



