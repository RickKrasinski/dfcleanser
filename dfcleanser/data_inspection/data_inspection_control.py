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
                                            get_parms_for_input, is_numeric_col, is_int_col,
                                            display_generic_grid, display_status, get_select_defaults)

from dfcleanser.common.html_widgets import (InputForm)

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

    opstat  =   opStatus()  
    
    from dfcleanser.common.html_widgets import define_inputs, are_owner_inputs_defined
    if(not (are_owner_inputs_defined(cfg.DataInspection_ID)) ) :
        define_inputs(cfg.DataInspection_ID,diw.datainspection_inputs)

    if(option == dim.MAIN_OPTION) :
        diw.display_dfc_inspection_main()
        clear_data_inspection_data()
    else :
        diw.display_inspection_main_taskbar()
    
    if(cfg.is_a_dfc_dataframe_loaded()) :
        
        if((option == dim.DISPLAY_DATATYPES_OPTION) or
           (option == dim.DISPLAY_NANS_OPTION) or
           (option == dim.DISPLAY_ROWS_OPTION) or
           (option == dim.DISPLAY_COLS_OPTION) or
           (option == dim.DISPLAY_CATEGORIES_OPTION)) :
            
            fparms = get_parms_for_input(parms[0],diw.data_inspection_df_input_idList)

            if(len(fparms) > 0) :
                cfg.set_config_value(cfg.CURRENT_INSPECTION_DF,fparms[0])
        
        if( (option == dim.DISPLAY_DATATYPES_OPTION) or 
            (option == dim.DISPLAY_FULL_COLUMN_NAMES) ):
            df_data_info = dim.get_df_datatypes_data(cfg.get_current_chapter_df(cfg.DataInspection_ID))
            display_inspect_datatypes(option,df_data_info)
        
        elif(option == dim.DISPLAY_NANS_OPTION) :
            display_inspect_nans()
    
        elif(option == dim.DISPLAY_ROWS_OPTION) :
            display_inspect_rows()
        
        elif(option == dim.DISPLAY_COLS_OPTION) :
            if(len(parms) > 1) :
                display_inspect_cols(parms[1])
            else :
                display_inspect_cols(None)

        elif(option == dim.DISPLAY_CATEGORIES_OPTION) :
            display_inspect_categories()

        elif( (option == dim.DROP_ROW_NANS_OPTION) or 
              (option == dim.DROP_ROW_NANS_OPTION) ):
            
            thresholdType = parms[0]
            
            if(option == dim.DROP_ROW_NANS_OPTION) :
                fparms = get_parms_for_input(parms[1],diw.drop_rows_input_idList)
            else :
                fparms = get_parms_for_input(parms[1],diw.drop_columns_input_idList)
            
            if(len(fparms) > 0) :
                try :
                    threshold   =   int(fparms[0])
                except :
                    opstat.set_status(False)
                    if( option == dim.DROP_ROW_NANS_OPTION ) :
                        opstat.set_errorMsg("Drop Nan Rows Threshold value '" + fparms[0] + "' is invalid")
                    else :
                        opstat.set_errorMsg("Drop Nan Cols Threshold value '" + fparms[0] + "' is invalid")

                    threshold   =   None
                    
            else :
                opstat.set_status(False)
                if( option == dim.DROP_ROW_NANS_OPTION ) :
                    opstat.set_errorMsg("Drop Nan Rows Threshold value is not defined")
                else :
                    opstat.set_errorMsg("Drop Nan Cols Threshold value is not defined")
                
                threshold   =   None
            
            if (option == dim.DROP_ROW_NANS_OPTION) :
            
                if(opstat.get_status()) :
                    dropstats   =   drop_nan_rows(cfg.get_current_chapter_df(cfg.DataInspection_ID),threshold,thresholdType,opstat)
            
                if(not(opstat.get_status())) :
                    display_exception(opstat) 
                else :
                    if(dropstats[0] > 0) :
                        display_status(str(dropstats[0]) + " Nan Rows Dropped Successfully") 
                    else :
                        display_status("No Rows matching threshold were dropped")
                        
            else :
                        
                if(opstat.get_status()) :
                    numcolsdropped  =   drop_nan_cols(cfg.get_current_chapter_df(cfg.DataInspection_ID),threshold,thresholdType,opstat) 
            
                if(not(opstat.get_status())) :
                    display_exception(opstat)   
                else :
                    if(numcolsdropped > 0) :
                        display_status(str(numcolsdropped) + " Columns with Nans Dropped Successfully")
                    else :
                        display_status(" No Columns matching threshold were dropped")
                        
        elif(option == dim.DISPLAY_ROW_OPTION) : 
            
            rowid = parms
            display_inspect_rows(rowid)   

        elif(option == dim.MATCH_VALS_OPTION) :
            match_values_rows(parms) 
        
        elif(option == dim.DISPLAY_COL_GRAPHS) :
            display_inspect_graphs(parms)
        
        elif(option == dim.DISPLAY_COL_OUTLIERS) :
            display_inspect_outliers(parms[0])
            
    else :
            
        cfg.drop_config_value(cfg.CURRENT_INSPECTION_DF)
        
        if(not (option == dim.MAIN_OPTION)) :
            cfg.display_no_dfs(cfg.DataInspection_ID)
        
    from dfcleanser.common.display_utils import  display_pop_up_buffer   
    display_pop_up_buffer()


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    main inspection categories  
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def display_inspect_datatypes(option,df_data_info) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the datatypes option
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat = opStatus()
                
    import matplotlib.pyplot as plt
                
    clock = RunningClock()
    clock.start()

    try :                
                
        if(not(option == dim.DISPLAY_FULL_COLUMN_NAMES)) :
            data_types_table    = dcTable("Column Data Types",
                                          "datatypesTable",
                                          cfg.DataInspection_ID)
        else :
            data_types_table    =   None
                        
        data_types_html         =   diw.display_df_datatypes(data_types_table,df_data_info[0],df_data_info[1],df_data_info[2],option,False) 
                    

        gridclasses     =   ["dfc-main"]
        gridhtmls       =   [data_types_html]
                    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("df-inspection-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("df-inspection-pop-up-wrapper",gridclasses,gridhtmls)

        print("\n")
        
        import matplotlib.pyplot as plt
        import numpy as np

        font =  {'fontsize': 14 }
        font2 = {'fontsize': 18 }
                
        objects = []
        for i in range(len(df_data_info[0])) :
            ttype = str(df_data_info[0][i]) 
            ttype = ttype.replace("datetime.","")
            #ttype = ttype.replace("datetime64[ns]","datetime")
            #ttype = ttype.replace("timedelta64[ns]","timedelta")
            print(ttype)
            
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


def display_inspect_nans() :
    """
    * -------------------------------------------------------------------------- 
    * function : display the inspect nans option
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    nans_rows_table = dcTable("Rows with most NaNs","nansrowTable",cfg.DataInspection_ID)
    nans_cols_table = dcTable("Columns with most NaNs","nansTable",cfg.DataInspection_ID)
    diw.display_null_data(cfg.get_current_chapter_df(cfg.DataInspection_ID),nans_rows_table,nans_cols_table,120)
    

def display_inspect_rows(rowid=0) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the inspect rows option
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat = opStatus()
                
    clock = RunningClock()
    clock.start()

    try :                
                
        row_stats_html      =   diw.display_row_stats(cfg.get_current_chapter_df(cfg.DataInspection_ID),
                                                      cfg.get_config_value(cfg.CURRENT_INSPECTION_DF),
                                                      False)
                    
        rows_openexcel_tb   =   diw.get_inspection_openexcel_taskbar()
        rows_openexcel_tb.set_gridwidth(280)
        rows_openexcel_tb.set_customstyle({"font-size":13, "height":40, "width":280, "left-margin":10})
        rows_openexcel_html =   rows_openexcel_tb.get_html()
        rows_openexcel_html =   (rows_openexcel_html + "<br>")
                    
        rows_table          =   dcTable("Start Row","DIsamplerows",cfg.DataInspection_ID)
        sample_row_html     =   diw.display_df_row_data(cfg.get_current_chapter_df(cfg.DataInspection_ID),
                                                        rows_table,rowid,0,opstat,False)
        searchcols_form     =   diw.get_colsearch_form(cfg.get_current_chapter_df(cfg.DataInspection_ID))
        searchcols_form.set_fullparms(True)
                    
        cfg.set_config_value(diw.data_inspection_colsearch_id+"Parms",["temp_search_df","","","",""])
        cfg.set_config_value(diw.data_inspection_colsearch_id+"ParmsProtect",[False,False,True,True,True])
                    
        searchcols_html     =   searchcols_form.get_html()
        
        help_note           =   "To save the df subset retrieved chnage the default df_output_title of 'temp_search_df'. </br> The 'temp_search_df' is dropped on every chapter reset."
        from dfcleanser.common.common_utils import get_help_note_html
        get_rows_notes_html =   get_help_note_html(help_note,50,250)
        
        gridclasses     =   ["dfc-header","dfc-top","dfc-main","dfc-bottom","dfc-footer"]
        gridhtmls       =   [row_stats_html,rows_openexcel_html,sample_row_html,searchcols_html,get_rows_notes_html]
                    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("df-inspection-row-data-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("df-inspection-row-data-pop-up-wrapper",gridclasses,gridhtmls)
             
    except Exception as e:
        opstat.store_exception("Error displaying row data\n ",e)
        display_exception(opstat)
        
        import traceback
        traceback.print_exc()

    clock.stop()


def display_inspect_cols(parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the inspect cols option
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat = opStatus()

    clock = RunningClock()
    clock.start()

    try : 
        
        df          =   cfg.get_current_chapter_df(cfg.DataInspection_ID)
        colnames    =   df.columns.tolist()
        
        if(not (parms is None)) :
            colname     =   parms
        else :
            colname     =   colnames[0]

        cnames      =   {'default': colname, 'list': colnames,"callback":"change_inspect_cols_col", "size":10}
        
        if(is_numeric_col(df,colname)) :

            coldetails_form  =   InputForm(diw.inspect_col_input_id,
                                           diw.inspect_col_input_idList,
                                           diw.inspect_col_input_labelList,
                                           diw.inspect_col_input_typeList,
                                           diw.inspect_col_input_placeholderList,
                                           diw.inspect_col_input_jsList,
                                           diw.inspect_col_input_reqList)
        else :
            
            coldetails_form  =   InputForm(diw.inspect_nn_col_input_id,
                                           diw.inspect_nn_col_input_idList,
                                           diw.inspect_nn_col_input_labelList,
                                           diw.inspect_nn_col_input_typeList,
                                           diw.inspect_nn_col_input_placeholderList,
                                           diw.inspect_nn_col_input_jsList,
                                           diw.inspect_nn_col_input_reqList)

        selectDicts     =   []
        selectDicts.append(cnames)

        get_select_defaults(coldetails_form,
                            diw.inspect_col_input_id,
                            diw.inspect_col_input_idList,
                            diw.inspect_col_input_typeList,
                            selectDicts)
        
        coldetails_form.set_shortForm(True)
        coldetails_form.set_fullparms(True)
        
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            
            coldetails_form.set_gridwidth(360)
            if(is_numeric_col(df,colname)) :
                coldetails_form.set_buttonstyle({"font-size":12, "height":75, "width":85, "left-margin":2})
            else :
                coldetails_form.set_buttonstyle({"font-size":12, "height":75, "width":85, "left-margin":75})
                
        else :
            
            coldetails_form.set_gridwidth(480)
            if(is_numeric_col(df,colname)) :
                coldetails_form.set_buttonstyle({"font-size":12, "height":75, "width":110, "left-margin":2})
            else :
                coldetails_form.set_buttonstyle({"font-size":12, "height":75, "width":110, "left-margin":110})
        
        coldetails_html     =   coldetails_form.get_html()
        
        from dfcleanser.data_cleansing.data_cleansing_widgets import display_col_stats
        col_stats_html  =   display_col_stats(df,colname,False,True)

        gridclasses     =   ["dfc-left","dfc-right"]
        gridhtmls       =   [col_stats_html,coldetails_html]
    
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            display_generic_grid("df-inspection-column-data-wrapper",gridclasses,gridhtmls)
        else :
            display_generic_grid("df-inspection-pop-up-column-data-wrapper",gridclasses,gridhtmls)

    except Exception as e:
        opstat.store_exception("Error displaying column data\n ",e)

    clock.stop()
                
    if(not (opstat.get_status())) :
        display_exception(opstat)


def display_inspect_categories() :
    """
    * -------------------------------------------------------------------------- 
    * function : display the inspect categoriies option
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat = opStatus()

    clock = RunningClock()
    clock.start()
                
    try : 

        cattable = dcTable("Category Columns",
                           "catcolsTable",
                           cfg.DataInspection_ID)

        catcandidatetable = dcTable("Category Candidate Columns",
                                    "catcandcolsTable",
                                    cfg.DataInspection_ID)
                
        numcats, numcands = diw.display_df_categories(cfg.get_current_chapter_df(cfg.DataInspection_ID),
                                                      cattable,catcandidatetable)
                    
    except Exception as e:
        opstat.store_exception("Error displaying category data\n ",e)

    clock.stop()
                
    if(not (opstat.get_status())) :
        display_exception(opstat)


def display_inspect_graphs(parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the inspect outliers option
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    display_inspect_cols(parms[0])
    diw.display_common_graphs(parms[0]) 


def display_inspect_outliers(colname) :
    """
    * -------------------------------------------------------------------------- 
    * function : display the inspect outliers option
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat  =   opStatus()
    
    display_inspect_cols(colname)
    
    outliers_html   =   diw.get_simple_outliers(cfg.get_current_chapter_df(cfg.DataInspection_ID),
                                                colname,opstat,display=False) 

    gridclasses     =   ["dfc-main"]
    gridhtmls       =   [outliers_html]
    
    print("\n")
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("df-inspection-outliers-data-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("df-inspection-outliers-pop-up-data-wrapper",gridclasses,gridhtmls)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    inspection control methods  
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def check_values_datatypes(cols_lists,vals_lists,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : find rows in df matching the col names and values
    * 
    * parms :
    *   cols_list -   col names
    *   vals_list -   column values
    *   opstat    -   status object
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    df  =   cfg.get_current_chapter_df(cfg.DataInspection_ID)  

    print("\n\ncheck_values_datatypes\n",cols_lists,"\n",vals_lists)      

    for i in range(len(cols_lists)) :
        
        vals_list   =   vals_lists[i]
        vals_list   =   vals_list.replace("[","")
        vals_list   =   vals_list.replace("]","")
        
        #print("check_values_datatypes vals_list after replace",type(vals_list),vals_list,len(vals_list))
            
        vals_list   =   vals_list.split(",")   

        #print("check_values_datatypes vals_list after split ",i,type(vals_list),vals_list)         
        
        for j in range(len(vals_list)) : 
            
            if(is_numeric_col(df,cols_lists[i])) :  
                if(is_int_col(df,cols_lists[i])) :
                    try :
                        int(vals_list[j])
                    except :
                        opstat.set_status(False)
                        opstat.set_errorMsg(vals_list[j] + "is not a valid value for " + cols_lists[i] + " column")
                else :
                    try :
                        float(vals_list[j])
                    except :
                        opstat.set_status(False)
                        opstat.set_errorMsg(vals_list[j] + "is not a valid value for " + cols_lists[i] + " column")


def find_matching_rows(df_title,column_type,cols_lists,vals_lists,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : find rows in df matching the col names and values
    * 
    * parms :
    *   cols_list -   col names
    *   vals_list -   column values
    *   opstat    -   status object
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    print("\nfind_matching_rows",column_type,"\n",cols_lists,"\n",vals_lists)
    #return

    from dfcleanser.common.common_utils import is_int_col
    df  =   cfg.get_current_chapter_df(cfg.DataInspection_ID) 

    print("find_matching_rows df",str(len(df)))       
    # get the subset df
    
    clock = RunningClock()
    clock.start()
        
    import pandas as pd
    final_criteria  =   pd.Series()
    
    for i in range(len(cols_lists)) :
        
        vals_list   =   vals_lists[i]
        vals_list   =   vals_list.replace("[","")
        vals_list   =   vals_list.replace("]","")
        
        print("\n\nfind_matching_rows vals_list after replace",type(vals_list),vals_list,len(vals_list))
            
        vals_list   =   vals_list.split(",")   

        print("find_matching_rows vals_list after split ",i,type(vals_list),len(vals_list),vals_list,opstat.get_status())         
                
        col_vals_list     =   []
                    
        if(column_type == 0) :
            
            if(is_int_col(df,cols_lists[i])) : 
                try :
                    for j in range(len(vals_list)) :            
                        col_vals_list.append(int(vals_list[j]))
                except :
                    #print("int excx",j)
                    opstat.set_status(False)
            else :
                try :
                    for j in range(len(vals_list)) :            
                        col_vals_list.append(float(vals_list[j]))
                except :
                    #print("float excx",j)
                    opstat.set_status(False)
                                
        else :
            try :
                for j in range(len(vals_list)) :            
                    col_vals_list.append(str(vals_list[j]))
            except :
                opstat.set_status(False)
        
        print("find_matching_rows criteria",col_vals_list,type(col_vals_list),opstat.get_status(),len(final_criteria))  
        
        if(opstat.get_status()) :
            
            if(len(col_vals_list) > 0) :
            
                if(column_type == 0) :
                    
                    print("find_matching_rows cols_lists[i]",len(df),cols_lists[i],col_vals_list,opstat.get_status())
                        
                    try :
                        current_criteria    =   df[cols_lists[i]].isin(col_vals_list)
                        num_ccs   =  [i for i in current_criteria.index if current_criteria[i]]
                        print("num current_criteria trues",len(num_ccs))

                            
                    except :
                        opstat.set_status(False) 
                        opstat.set_errorMsg("failed to get current criteria subset " + cols_lists[i])
                            
                    if(opstat.get_status()) :
                        try :
                                
                            if(len(final_criteria) > 0) :
                                final_criteria      =   final_criteria & current_criteria
                            else :
                                final_criteria      =   current_criteria
                                
                            num_fcs   =  [i for i in final_criteria.index if final_criteria[i]]
                            print("num final_criteria trues",len(num_fcs))

                            
                        except :
                            opstat.set_status(False) 
                            opstat.set_errorMsg("failed to get final criteria subset " + cols_lists[i])
                         
                else :
                    
                    for k in range(len(col_vals_list)) :
                
                        current_criteria    =   df[cols_lists[i]].str.contains(col_vals_list[k])
                            
                        try :
                            if(len(final_criteria) > 0) :
                                final_criteria      =   final_criteria & current_criteria
                            else :
                                final_criteria      =   current_criteria
                        except :
                            opstat.set_status(False) 
                            opstat.set_errorMsg("failed to get final criteria subset " + cols_lists[i])
                    
            else :
                opstat.set_status(False) 
                opstat.set_errorMsg("no valid column_values entered for " + cols_lists[i])
                    
        else :
            opstat.set_status(False) 
            opstat.set_errorMsg("invalid column_values entered for " + cols_lists[i])
    
    #ccrit = 0                    
    #for q in range(len(final_criteria)) :
    #    if(final_criteria[q]) :
    #        ccrit = ccrit + 1
    #print("final final_criteria",ccrit,len(final_criteria))
    
    #try :
    #    total_trues = 0       
    #    for w in range(len(final_criteria))  :
    #        if(final_criteria[w]) : 
    #            total_trues = total_trues + 1
        
    #    print("total_trues",total_trues)
    #except :
    #    print("fuck total trues")
            
    
    clock.stop() 
    
    num_trues   =  [i for i in final_criteria.index if final_criteria[i]]
    print("num_trues",len(num_trues))
    
    if(len(num_trues) > 0) :
        
        search_df = df[final_criteria].copy()
        #print("search_df",len(search_df))
        search_df.reset_index(drop=True,inplace=True)
            
        from dfcleanser.common.cfg import dfc_dataframe,add_dfc_dataframe
            
        search_df_notes     =   "search subset from " + cfg.get_config_value(cfg.CURRENT_INSPECTION_DF)
        new_dfcdf           =   dfc_dataframe(df_title,search_df,search_df_notes)
        add_dfc_dataframe(new_dfcdf)
        
    return(len(num_trues))
            

def match_values_rows(inparm) :
    """
    * -------------------------------------------------------------------------- 
    * function : find rows in df matching the col names and values
    * 
    * parms :
    *   cols_list -   col names
    *   vals_list -   column values
    *   opstat    -   status object
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat  =   opStatus()
        
    print("match_values_rows",inparm)
    column_type     =   inparm[0]
        
    fparms          =   get_parms_for_input(inparm[1],diw.data_inspection_colsearch_idList)
        
    print("match_values_rows",fparms)
        
    if(len(fparms) > 0) :
            
        df_title        =   fparms[0]
            
        if(len(df_title) > 0) :
            
            cols_string     =   fparms[1]
            
            try :
                cols_list       =   cols_string.split(",")
                
                if(not (cols_list) is None) :
                    if(len(cols_list[0]) == 0) :
                        opstat.set_status(False)
                        opstat.set_errorMsg("No column names list is defined")
                else :
                    opstat.set_status(False)
                    opstat.set_errorMsg("No column names list is defined")
                    
            except :
                opstat.set_status(False)
                opstat.set_errorMsg("Invalid column names list is defined")
            
            print("match_values_rows - colslist ",type(cols_list),len(cols_list),cols_list)
            
            if(opstat.get_status()) :
                
                vals_lists  =   []
                
                for i in range(len(cols_list)) :
        
                    vals_list     =   fparms[i+2]
                    print("match_values_rows vals_list ",type(vals_list),len(vals_list),vals_list)
                
                    if(len(vals_list) > 0) :
                        vals_lists.append(vals_list)
                    else :
                        opstat.set_status(False)
                        opstat.set_errorMsg("Invalid column values list is defined")
                        
                if(opstat.get_status) :
                    
                    try :
                        print("match_values_rows vals_lists cols_lists \n",cols_list,"\n",vals_lists)
                        
                        if(len(cols_list)  == (len(vals_lists))) :
                            check_values_datatypes(cols_list,vals_lists,opstat)
                            #print("match_values_rows - opstat",opstat.get_status())
                            if(opstat.get_status) :
                                num_trues   =   find_matching_rows(df_title,column_type,cols_list,vals_lists,opstat)
                        else :
                            opstat.set_status(False)
                            opstat.set_errorMsg("Number Of Column Names does not match Number of Values")
                            
                    except :
                        opstat.set_status(False)
                        opstat.set_errorMsg("Invalid column values list is defined")
                        
                else :
                    opstat.set_status(False)
                    opstat.set_errorMsg("Invalid column values list is defined")
                    
            else :
                opstat.set_status(False)
                opstat.set_errorMsg("column values list is not defined")
                    
        else :
            opstat.set_status(False)
            opstat.set_errorMsg("no output dataframe title defined")
                
    else :
        opstat.set_status(False)
        opstat.set_errorMsg("column names list is not defined")
            
    from IPython.display import clear_output
    clear_output()
    
    cboxes  =   [False,False,True,False,False]
    diw.display_dfc_inspection_main(cboxes)
    
    if(opstat.get_status()) :
        
        cfg.set_config_value(cfg.CURRENT_INSPECTION_DF,df_title)
    
        print("\n")
        if(num_trues > 0) :
            display_status(str(num_trues) + " matches found in your df") 
        else :
            display_status("No matches found in your df")
        
    else :
        
        print("\n")
        msg     =   "Unable to get Rows Data Subset : " + opstat.get_errorMsg()
        opstat.set_errorMsg(msg)
        display_exception(opstat)
        
    display_inspect_rows()



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
    
    import math
    
    if(display) :
            
        clock = RunningClock()
        clock.start()

    try     :
        if(ttype == dim.BY_PERCENT) : 
            thold   =   math.floor(len(df.columns) * (float(threshold) * 0.01))
        else :
            thold   =   math.floor(float(threshold))
            
        nanslist    =   df.isnull().sum(axis=1).tolist() #< thold
        criteria    =   nanslist
        
        dropcount   =   0
        for i in range(len(nanslist)) :
            if(nanslist[i]) < thold :
                criteria[i]     =   True
            else :
                criteria[i]     =   False
                dropcount       =   dropcount + 1
                
        if(dropcount > 0) :
        
            df = df[criteria]
            cfg.set_dfc_dataframe_df(cfg.get_config_value(cfg.CURRENT_INSPECTION_DF),df)
        
    except Exception as e:
        opstat.store_exception("Error dropping nan rows\n ",e)
        display_exception(opstat)

    if(display) :
        clock.stop()
        
        #make scriptable
        add_to_script(["# Drop NAN Rows ",
                       "from dfcleanser.data_inspection.data_inspection_control import drop_nan_rows",
                       "drop_nan_rows(" + str(threshold) + ",False)"],opstat)
    
    return([dropcount,len(df)])


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
    import math
    
    if(display) :
            
        clock = RunningClock()
        clock.start()

    try     :
        
        if(ttype == dim.BY_PERCENT) : 
            thold   =   math.floor(len(df) * (float(threshold) * 0.01))
        else :
            thold   =   math.floor(float(threshold))
            
        df_cols         =   df.columns
        colswithnulls   =   df.isnull().sum()
        droplist        =   []
    
        for i in range(len(colswithnulls)) :
            if(colswithnulls[i] >= thold) :
                droplist.append(df_cols[i])

        if(len(droplist) > 0) :
            df.drop(droplist,axis=1,inplace=True)

    except Exception as e:
        opstat.store_exception("Error dropping nan cols\n ",e)

    if(display) :
        
        clock.stop()
        
        #make scriptable try catch
        add_to_script(["# Drop NAN Cols ",
                       "from dfcleanser.data_inspection.data_inspection_control import drop_nan_cols",
                       "drop_nan_cols(" + str(threshold) + ",False)"],opstat)

    return(len(droplist))


"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   general housekeeping functions
#------------------------------------------------------------------
#------------------------------------------------------------------
"""  

     
def clear_data_inspection_data() :
    
    drop_owner_tables(cfg.DataInspection_ID)
    from dfcleanser.common.html_widgets import delete_all_inputs
    delete_all_inputs(cfg.DataInspection_ID)
    clear_data_inspection_cfg_values()
    
    
def clear_data_inspection_cfg_values() :
    
    return
    
    #cfg.drop_config_value(cfg.CURRENT_INSPECTION_DF)
    



