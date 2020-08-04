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
        drop_working_df()
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
                
            if(not (option == dim.DISPLAY_ROWS_OPTION)) :
                drop_working_df()
        
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
              (option == dim.DROP_COL_NANS_OPTION) ):
            
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
            display_inspect_rows()   

        elif(option == dim.DISPLAY_COL_GRAPHS) :
            display_inspect_graphs(parms)
        
        elif(option == dim.DISPLAY_COL_OUTLIERS) :
            display_inspect_outliers(parms[0])
            
        elif(option == dim.DISPLAY_SCROLL_TO_DF_ROW) :
            diw.display_scroll_to_row()
            
        elif(option == dim.PROCESS_SCROLL_TO_DF_ROW) :
            
            opstat      =   opStatus()
            
            df = cfg.get_current_chapter_df(cfg.DataInspection_ID)
            
            retparms    =   get_row_id_for_df(df,parms,diw.scroll_df_rows_input_idList,opstat)

            if(opstat.get_status()) :
                
                if(retparms[1] == 0) :
                    display_inspect_rows(retparms[0])  
                else :
                    display_inspect_rows(retparms[0])
                    
            else :
                
                diw.display_scroll_to_row()
                display_exception(opstat)
            
        elif(option == dim.SCROLL_DF_ROWS_DOWN) :
            
            new_row_id  =   cfg.get_config_value(cfg.CURRENT_SCROLL_ROW_KEY)
            
            if(new_row_id is None) :
                new_row_id  =   0
            else :
                new_row_id  =   new_row_id + 200
                
                df  =   cfg.get_current_chapter_df(cfg.DataInspection_ID)
                if(new_row_id > len(df)) :
                    new_row_id  =   cfg.get_config_value(cfg.CURRENT_SCROLL_ROW_KEY)    
            
            display_inspect_rows(new_row_id)   
            
        elif(option == dim.SCROLL_DF_ROWS_UP) :
            
            new_row_id  =   cfg.get_config_value(cfg.CURRENT_SCROLL_ROW_KEY)
            
            if(new_row_id is None) :
                new_row_id  =   0
            else :
                new_row_id  =   new_row_id - 200
                if(new_row_id < 0) :
                    new_row_id  =   0
            
            display_inspect_rows(new_row_id) 
            
        elif(option == dim.DISPLAY_DF_ROW) :
            
            print("dim.DISPLAY_DF_ROW")

        elif(option == dim.DISPLAY_DF_ROW_REMOTE) :
            
            chapterid   =   parms[0]
            #print("chapterId",chapterid)
            
            new_config_df   =   None
            
            if(chapterid == cfg.DataInspection_ID)      :   new_config_df  =   cfg.get_config_value(cfg.CURRENT_INSPECTION_DF)
            elif(chapterid == cfg.DataCleansing_ID)     :   new_config_df  =   cfg.get_config_value(cfg.CURRENT_CLEANSE_DF)
            elif(chapterid == cfg.DataTransform_ID)     :   new_config_df  =   cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF)
            elif(chapterid == cfg.DataExport_ID)        :   new_config_df  =   cfg.get_config_value(cfg.CURRENT_EXPORT_DF)
            elif(chapterid == cfg.DataImport_ID)        :   new_config_df  =   cfg.get_config_value(cfg.CURRENT_IMPORT_DF)
            elif(chapterid == cfg.SWGeocodeUtility_ID)  :   new_config_df  =   cfg.get_config_value(cfg.CURRENT_GEOCODE_DF)
            elif(chapterid == cfg.SWDFSubsetUtility_ID) :   new_config_df  =   cfg.get_config_value(cfg.CURRENT_SUBSET_DF)
            
            cfg.set_config_value(cfg.CURRENT_INSPECTION_DF,new_config_df)
            
            display_inspect_rows()
            
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

        print("\n")            
        
        from dfcleanser.data_transform.data_transform_dataframe_widgets import display_current_df_index
        display_current_df_index(cfg.get_current_chapter_df(cfg.DataInspection_ID),
                                 cfg.get_current_chapter_dfc_df_title(cfg.DataInspection_ID),0,True)
                
        row_stats_html      =   diw.display_row_stats(cfg.get_current_chapter_df(cfg.DataInspection_ID),
                                                      cfg.get_config_value(cfg.CURRENT_INSPECTION_DF),
                                                      False)
        
        sample_row_html     =   dim.display_df_rows(cfg.get_current_chapter_df(cfg.DataInspection_ID),rowid,200)
        
        rows_openexcel_tb   =   diw.get_inspection_openexcel_taskbar()
        rows_openexcel_tb.set_gridwidth(620)
        rows_openexcel_tb.set_customstyle({"font-size":13, "height":90, "width":120, "left-margin":10})
        rows_openexcel_html =   rows_openexcel_tb.get_html()
        rows_openexcel_html =   (rows_openexcel_html + "<br>")
        
        cfg.set_config_value(cfg.CURRENT_SCROLL_ROW_KEY,rowid)

        gridclasses     =   ["dfc-top","dfc-bottom","dfc-footer"]
        gridhtmls       =   [row_stats_html,sample_row_html,rows_openexcel_html]
                    
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

    from dfcleanser.common.common_utils import is_int_col
    df  =   cfg.get_current_chapter_df(cfg.DataInspection_ID) 

    clock = RunningClock()
    clock.start()
        
    import pandas as pd
    final_criteria  =   pd.Series()
    
    for i in range(len(cols_lists)) :
        
        vals_list   =   vals_lists[i]
        vals_list   =   vals_list.replace("[","")
        vals_list   =   vals_list.replace("]","")
        
        vals_list   =   vals_list.split(",")   

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
        
        if(opstat.get_status()) :
            
            if(len(col_vals_list) > 0) :
            
                if(column_type == 0) :
                    
                    try :
                        current_criteria    =   df[cols_lists[i]].isin(col_vals_list)
                        num_ccs   =  [i for i in current_criteria.index if current_criteria[i]]
                            
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
    
    clock.stop() 
    
    num_trues   =  [i for i in final_criteria.index if final_criteria[i]]
    
    if(len(num_trues) > 0) :
        
        search_df = df[final_criteria].copy()
        #print("search_df",len(search_df))
        search_df.reset_index(drop=True,inplace=True)
            
        from dfcleanser.common.cfg import dfc_dataframe,add_dfc_dataframe
            
        search_df_notes     =   "search subset from " + cfg.get_config_value(cfg.CURRENT_INSPECTION_DF)
        new_dfcdf           =   dfc_dataframe(df_title,search_df,search_df_notes)
        add_dfc_dataframe(new_dfcdf)
        
    return(len(num_trues))
            

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


def get_row_id_for_df(df,parms,idList,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : get a specific df row
    * 
    * parms :
    *   df        -   dataframe
    *   parms     -   row id parms
    *   idlist    -   threshold type
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    fparms  =   get_parms_for_input(parms,idList)
            
    row_id      =   fparms[0]
            
    index_cols  =   fparms[1]
    index_cols  =   index_cols.lstrip("[")
    index_cols  =   index_cols.rstrip("]")
    index_cols  =   index_cols.split(",")
            
    index_vals  =   fparms[2]
    index_vals  =   index_vals.lstrip("[")
    index_vals  =   index_vals.rstrip("]")
    index_vals  =   index_vals.split(",")
            
    if(len(row_id) > 0) :
                
        try :
                    
            row_id  =   int(row_id)
                    
            #df = cfg.get_current_chapter_df(cfg.DataInspection_ID)
                    
            if( (row_id > 0) and (row_id < len(df)) ) :
                        
                return([row_id,0])                         
                        
            else :
                        
                opstat.set_status(False)
                opstat.set_errorMsg("Row Id is oiut of range of df len : 0 - " + str(len(df)))
                    
        except :
                    
            opstat.set_status(False)
            opstat.set_errorMsg("Row Id is not valid numeric value : " + fparms[0])
            
    else :
                
        if(len(index_cols) > 0) :
                    
            index_names     =   []
            index_types     =   []
                    
                    #df              =   cfg.get_current_chapter_df(cfg.DataInspection_ID)
            index_columns   =   df.index.names
                    
            if(len(index_columns) > 0) :
                for i in range(len(index_columns)) :
                    if( not (index_columns[i] is None) ) :
                        index_names.append(index_columns[i])
                        index_types.append(df.index.get_level_values(i).dtype)

            if(len(index_names) == len(index_cols)) :
                            
                matched     =   True
                            
                for i in range(len(index_cols)) :
                    if(not (index_cols[i] == index_names[i])) :
                        matched = False
                              
                if(matched) :
                                
                    if(len(index_vals) > 0) :
                        
                        df_vals_converted   =   []
                                    
                        for i in range(len(index_vals)) :
                                        
                            from dfcleanser.common.common_utils import get_converted_value, get_dtype_str_for_datatype 
                            dtype_str               =   get_dtype_str_for_datatype(index_types[i])
                            df_vals_converted.append(get_converted_value(dtype_str,index_vals[i],opstat))
                                        
                            if(not opstat.get_status()) :
                                break;
                                        
                        if(opstat.get_status()) :
                         
                            try :
                                            
                                boolean_index   =   None
                                            
                                for i in range(len(index_names)) :
                                                
                                    if(i == 0) :
                                        boolean_index   =   df.index.get_level_values(index_names[i]) == df_vals_converted[i] 
                                    else :
                                        boolean_index   =   (boolean_index & (df.index.get_level_values(index_names[i]) == df_vals_converted[i]))
                                                    
                                result  = df.loc[boolean_index] 
                                                
                                row_id  =   df.index.get_loc(result.iloc[0].name) 
                                                                                        
                                return([row_id,1])
                                            
                            except :
                                            
                                opstat.set_status(False)
                                opstat.set_errorMsg("Unable to get df row with index values specified ")
                        
                        else :
                        
                            opstat.set_status(False)
                            opstat.set_errorMsg("No Index values specified ")
                    
                    else :
                                
                        opstat.set_status(False)
                        opstat.set_errorMsg("Index cols sequence does not match df Index")
                            
                else :
                            
                    opstat.set_status(False)
                    opstat.set_errorMsg("Number of Index cols specified incorrect")
                        
            else :
                    
                opstat.set_status(False)
                opstat.set_errorMsg("No Index specified for df")
                    
        else :
                    
            opstat.set_status(False)
            opstat.set_errorMsg("No Row Id or Index Columns specified ")
            
        if(not (opstat.get_status)) :

            if(len(row_id) > 0) :   
                return([None,0])
            else :
                return([None,1])


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

def drop_working_df() :
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df, drop_dfc_dataframe
    
    df = get_dfc_dataframe_df("dfc_subset_working_df")
    
    if(not (df is None)) :
        drop_dfc_dataframe("dfc_subset_working_df")    
        
    



