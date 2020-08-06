"""
# sw_utility_census_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue June 6 16:00:00 2019

@author: Rick
"""

import sys
this = sys.modules[__name__]

import os
    
import dfcleanser.common.cfg as cfg

from dfcleanser.common.table_widgets import (drop_owner_tables)

import dfcleanser.sw_utilities.sw_utility_census_model as swcm
import dfcleanser.sw_utilities.sw_utility_census_widgets as swcw

from dfcleanser.common.common_utils import (opStatus, RunningClock, delete_a_file, 
                                            does_file_exist,
                                            display_notes,display_status,
                                            get_parms_for_input, display_exception)

   
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   main taskbar and route function
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


def display_census_utility(optionId,parms=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : main census routing function
    * 
    * parms :
    *  optionId   - display func id
    *  parms      - associated parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    from IPython.display import clear_output
    clear_output()
    
    from dfcleanser.common.html_widgets import define_inputs, are_owner_inputs_defined
    if(not (are_owner_inputs_defined(cfg.SWCensusUtility_ID)) ) :
        define_inputs(cfg.SWCensusUtility_ID,swcw.SWUtility_census_inputs)

    
    if(optionId == swcm.DISPLAY_MAIN) :
        swcw.get_census_main_taskbar()
        clear_sw_utility_census_data()

    #"""
    #--------------------------------------------------------------------------
    #   download and build commands
    #--------------------------------------------------------------------------
    #"""
        
    elif(optionId == swcm.DISPLAY_DOWNLOAD_CENSUS_DATA) :
        swcw.get_census_main_taskbar()
        cfg.set_config_value(cfg.CENSUS_CURRENT_MODE,"DOWNLOAD")
        
        swcw.display_downloaded_census_data()
        

    #"""
    #--------------------------------------------------------------------------
    #   configure commands
    #--------------------------------------------------------------------------
    #"""
    
    elif(optionId == swcm.DISPLAY_CONFIGURE_CENSUS_DATA) :
        swcw.get_census_main_taskbar()
        cfg.set_config_value(cfg.CENSUS_CURRENT_MODE,"CONFIGURE")
        
        cfg.drop_config_value(cfg.CENSUS_DROP_DATASET_LISTS)
        cfg.drop_config_value(cfg.CENSUS_DROP_SUBDATASET_LIST)
        cfg.drop_config_value(cfg.CENSUS_CURRENT_DATASET)
        
        swcw.display_configure_census_data(None,True)
        
    elif(optionId == swcm.DISPLAY_DATASET_DETAILS) :
        if(swcm.DEBUG_CENSUS) :
            print("swcm.DISPLAY_DATASET_DETAILS",parms)
            
        swcw.get_census_main_taskbar()
        
        datasetid   =   parms[0]
        subsetid    =   parms[1]
        caller      =   parms[2]
        
        cfg.set_config_value(cfg.CENSUS_CURRENT_DATASET,datasetid)

        if(caller == "0") :
            swcw.display_downloaded_census_data(datasetid)
            cfg.set_config_value(cfg.CENSUS_CURRENT_MODE,"LOAD")
            #swcw.display_download_census_data(datasetid,True)
        else :
            swcw.display_configure_census_data(datasetid,True)
            cfg.set_config_value(cfg.CENSUS_CURRENT_MODE,"CONFIGURE")

    
    elif(optionId == swcm.DISPLAY_DATASET_SUBDATA_DETAILS) :
        swcw.get_census_main_taskbar()
        
        if(swcm.DEBUG_CENSUS) :
            print("swcm.DISPLAY_DATASET_SUBDATA_DETAILS",parms)
        
        datasetid   =   parms[0]
        subdataid   =   int(parms[1])
        
        cfg.set_config_value(cfg.CENSUS_CURRENT_DATASET,datasetid)
        
        cmode       =   cfg.get_config_value(cfg.CENSUS_CURRENT_MODE)
        
        if(cmode == "LOAD") :
            swcw.display_downloaded_census_data(datasetid,subdataid,460)
        else :
            swcw.display_configure_census_data(datasetid,True,subdataid)

    elif(optionId == swcm.DISPLAY_SCROLL_CENSUS_COL_NAMES) :
        swcw.get_census_main_taskbar()
        
        datasetid   =   parms[0]
        subdataid   =   int(parms[1])
        colnameid   =   int(parms[2])
        direction   =   int(parms[3])
        
        currentmode     =   cfg.get_config_value(cfg.CENSUS_CURRENT_MODE)
        if(currentmode  ==  "CONFIGURE") :
            swcw.display_configure_census_data(datasetid,True,subdataid,colnameid,direction)
        else :
            swcw.display_downloaded_census_data(datasetid,subdataid,colnameid,direction)
        
    elif(optionId == swcm.PROCESS_CONFIGURE_CENSUS_DATA) :
        swcw.get_census_main_taskbar()
        cfg.set_config_value(cfg.CENSUS_CURRENT_MODE,"CONFIGURE")
        
        droplists   =   parms
        cfg.set_config_value(cfg.CENSUS_DROP_DATASET_LISTS,droplists)
        
        swcw.display_add_drop_datasets(droplists)

    elif(optionId == swcm.DROP_CENSUS_DATA) :
        swcw.get_census_main_taskbar()
        
        configure_census_data()        

            
    #"""
    #--------------------------------------------------------------------------
    #   load datasets to memory commands
    #--------------------------------------------------------------------------
    #"""

    elif(optionId == swcm.DISPLAY_LOAD_CENSUS_DATA) :
        swcw.get_census_main_taskbar()
        swcw.display_load_datasets()
    

    elif(optionId == swcm.VERIFY_LOAD_CENSUS_TO_DFC_DFS) :
        
        #if(swcm.DEBUG_CENSUS) :
        #    print("VERIFY_LOAD_CENSUS_TO_DFC_DFS : parms\n",parms)
            
        swcw.get_census_main_taskbar()

        cfg.set_config_value(cfg.CENSUS_CURRENT_MODE,"ADD_TO_DFS")
        
        droplists   =   parms
        cfg.set_config_value(cfg.CENSUS_DROP_DATASET_LISTS,droplists)
        
        swcw.display_load_to_df_verification_data(droplists)
        #display_load_to_df_verification_data(datasets_to_load_to_dfs)

    elif(optionId == swcm.PROCESS_LOAD_TO_DFC_DFS) :
        
        if(swcm.DEBUG_CENSUS) :
            print("PROCESS_LOAD_TO_DFC_DFS : parms\n",parms)
            
        swcw.get_census_main_taskbar()
        load_census_datasets_to_df(cfg.get_config_value(cfg.CENSUS_DROP_DATASET_LISTS))
        #print(cfg.get_config_value(cfg.CENSUS_DROP_DATASET_LISTS))
        
    elif(optionId == swcm.SHOW_SELECTED_COLUMNS) :
        swcw.get_census_main_taskbar()
        
        #if(swcm.DEBUG_CENSUS) : 
        #    print("swcm.SHOW_SELECTED_COLUMNS : parms\n",parms)
        
        datasetid               =   None
        datasetid_types         =   []
        
        if(len(parms) > 0) :
            datasets_to_insert_from =   parms
            
            for i in range(len(datasets_to_insert_from)) :
                for j in range(len(datasets_to_insert_from[0])) :
                    if(datasets_to_insert_from[i][j] == "True") :
                        datasetid   =   swcm.census_datasets[i]
                        datasetid   =   datasetid.replace("_"," ")
                        datasetid_types.append(j)

        else :
            datasetid               =   None
        
        if(datasetid is None) :
            
            cfg.drop_config_value(cfg.CENSUS_DATASET_TO_INSERT_FROM) 
            swcm.current_dataset_inserting_from.clear_current_df_to_insert_from()
            display_status("No dataset(s) selected to insert columns from.")
            
        else :
            
            cfg.set_config_value(cfg.CENSUS_DATASET_TO_INSERT_FROM,datasetid) 
            cfg.set_config_value(cfg.CENSUS_DATASET_TYPES_TO_INSERT_FROM,datasetid_types)
            
            swcm.current_dataset_inserting_from.clear_current_df_to_insert_from()
            swcm.current_dataset_inserting_from.set_datasetid(datasetid) 
            swcm.current_dataset_inserting_from.set_index_types(datasetid_types)
            
            swcw.display_select_dataset_columns_to_insert(datasetid,None)        

    elif(optionId == swcm.SHOW_DATASET_SUBSETS) :
        datasetid   =   swcm.current_dataset_inserting_from.get_datasetid() 
        
        swcm.current_dataset_inserting_from.dump()
        swcw.display_select_dataset_columns_to_insert(datasetid,None)  
        
    elif(optionId == swcm.DISPLAY_INSERT_CENSUS_COLS) :
        swcw.get_census_main_taskbar()
        swcw.display_columns_to_insert(parms)
        
    elif(optionId == swcm.PROCESS_INSERT_CENSUS_COLS) :
        swcw.get_census_main_taskbar()
        process_insert_cols_to_df(parms)        
    

    elif(optionId == swcm.DISPLAY_EXPORT_CENSUS_DFS) :
        swcw.get_census_main_taskbar()
        
        if(swcm.DEBUG_CENSUS) : 
            print("DISPLAY_EXPORT_CENSUS_DFS")
            
        swcw.display_datasets_to_export()

    elif(optionId == swcm.PROCESS_EXPORT_CENSUS_DFS) :
        swcw.get_census_main_taskbar()
        
        if(swcm.DEBUG_CENSUS) : 
            print("PROCESS_EXPORT_CENSUS_DFS") 

    elif(optionId == swcm.DISPLAY_LOAD_CENSUS_DATA_TO_DB) :
        swcw.get_census_main_taskbar()
        swcw.display_datasets_to_load_to_db()

    elif(optionId == swcm.PROCESS_LOAD_CENSUS_DATA_TO_DB) :
        swcw.get_census_main_taskbar()
        
        if(swcm.DEBUG_CENSUS) :
            print("PROCESS_LOAD_CENSUS_DATA_TO_DB") 
        
        

        
    #"""
    #--------------------------------------------------------------------------
    #   get datasets columns commands
    #--------------------------------------------------------------------------
    #"""
        
    elif(optionId == swcm.DISPLAY_CENSUS_DATASETS_FOR_INSERT) :
        swcw.get_census_main_taskbar()
        
        #if(swcm.DEBUG_CENSUS) :
        #    print("DISPLAY_CENSUS_DATASETS_FOR_INSERT : parms\n",parms)
        
        if(parms is None) :
            dtid    =   None
            dsid    =   None
        else :
            
            dsid    =   parms[0]
            if(parms[1] == "None") :
                dtid    =   None
            else :
                dtid    =   int(parms[1])
                cfg.set_config_value(cfg.CENSUS_CURRENT_GET_COLS_SUBDATA_ID,dtid)
            
            cfg.set_config_value(cfg.CENSUS_CURRENT_DATASET,dsid)

        
        swcw.display_get_datasets_in_memory()


    elif(optionId == swcm.DISPLAY_LOAD_CENSUS_TO_DFC_DFS) :
        swcw.get_census_main_taskbar()
        
        #if(swcm.DEBUG_CENSUS) :
        #    print("DISPLAY_LOAD_CENSUS_TO_DFC_DFS : parms\n",parms)

        swcw.display_datasets_loaded_to_dfs()


    elif(optionId == swcm.PROCESS_GET_COLS_SUBSET) :
        
        swcw.get_census_main_taskbar()
            
        datasetid   =   parms[0]
        keyid       =   parms[1]
        
        if(swcm.DEBUG_CENSUS) :
            print("PROCESS_GET_COLS_SUBSET : parms\n",parms)
            print("datasetid : ",datasetid," keyid : ",keyid)
            
        dsid                =   swcm.census_datasets[int(datasetid)]
        dsid                =   dsid.replace("_"," ")

        swcw.display_select_dataset_columns_to_insert(dsid,None) 
    
    
    elif(optionId == swcm.PROCESS_GET_COLS_LISTS) :
        
        swcw.get_census_main_taskbar()
                
        datasetid       =   parms[0]
        subdataid       =   int(parms[1])
    
        cfg.set_config_value(cfg.CENSUS_SELECTED_SUBSET_ID,subdataid)

        if(swcm.DEBUG_CENSUS) :
            print("PROCESS_GET_COLS_LISTS : parms\n",parms)

        swcw.display_select_dataset_columns_to_insert(datasetid,subdataid)#,datasets_in_memory)
        
    elif( (optionId == swcm.PROCESS_INSERT_COLS_GET)  or (optionId == swcm.PROCESS_INSERT_COLS_DROP) ):
        
        swcw.get_census_main_taskbar()
        
        if(swcm.DEBUG_CENSUS) :
            print("PROCESS_INSERT_COLS_GET : parms\n",parms)
            
        cols_to_get_list    =   parms[0]
        for i in range(len(cols_to_get_list)) :
            cols_to_get_list[i]     =   int(cols_to_get_list[i])
        
        cols_to_get_list.sort()
            
        if(optionId == swcm.PROCESS_INSERT_COLS_DROP) :
            
            if(not ((cols_to_get_list[0] == "All") or (cols_to_get_list[0] == -1) or (cols_to_get_list[0] == -2) )) :
            
                datasetid               =   swcm.current_dataset_inserting_from.get_datasetid()
                subdataid               =   swcm.current_dataset_inserting_from.get_subdatasetid()
            
                subdata_data            =   swcm.get_subset_data_lists(datasetid)
                subdatacols             =   subdata_data[swcm.SUBSET_COLUMNS]
            
                with_drop_cols_list     =   []
            
                for i in range(len(subdatacols[subdataid])) :
                
                    if(not (i in cols_to_get_list)) :
                        with_drop_cols_list.append(i) 
                    
                cols_to_get_list     =    with_drop_cols_list
        
        unique_cols_to_get_list    =   []
        for i in range(len(cols_to_get_list)) :
            if(not(cols_to_get_list[i] in unique_cols_to_get_list)) :
                unique_cols_to_get_list.append(cols_to_get_list[i])
                
        cols_to_get_list    =   unique_cols_to_get_list
        
        print("cols_to_get_list",cols_to_get_list)
        
        if(len(cols_to_get_list) == 1) :
            
            #print("cols_to_get_list",type(cols_to_get_list),type(cols_to_get_list[0]))
            
            if( (cols_to_get_list[0] == "All") or (cols_to_get_list[0] == -1) or (cols_to_get_list[0] == -2) ) :
                
                datasetid       =   swcm.current_dataset_inserting_from.get_datasetid()
                subdataid       =   swcm.current_dataset_inserting_from.get_subdatasetid()
                
                print("subdataid",subdataid)

                subdata_attrs   =   swcm.current_dataset_inserting_from.get_subdata_col_attributes(subdataid)
            
                if(cols_to_get_list[0] == -2) :
                    cols_to_get_list    =   "None"
                elif( (cols_to_get_list[0] == -1) or (cols_to_get_list[0] == "All") ) :
                    cols_to_get_list    =   "All"
                    
                subdata_attrs.set_column_insert_type(cols_to_get_list) 
                
                print("cols_to_get_list",cols_to_get_list,subdata_attrs.get_column_insert_type())
                subdata_attrs.set_columns_list([]) 
                subdata_attrs.set_column_attributes_dict([])
                swcw.display_select_dataset_columns_to_insert(datasetid,None)            
                #swcw.display_select_dataset_columns_to_insert(datasetid,None)            
                
        else :

            for i in range(len(cols_to_get_list)) :
                cols_to_get_list[i] =   int(cols_to_get_list[i]) 
                
            datasetid       =   swcm.current_dataset_inserting_from.get_datasetid()
            subdataid       =   swcm.current_dataset_inserting_from.get_subdatasetid()            
            
            subdata_attrs   =   swcm.current_dataset_inserting_from.get_subdata_col_attributes(subdataid)
            subdata_attrs.set_column_insert_type("List")
            subdata_attrs.set_columns_list(cols_to_get_list) 
            subdata_attrs.set_column_attributes_dict({})
            
            print("cols_to_get_list",subdataid,cols_to_get_list,subdata_attrs.get_column_insert_type())
            
            swcm.current_dataset_inserting_from.dump()
            
            swcw.display_columns_to_insert(datasetid, subdataid, cols_to_get_list)

    elif(optionId == swcm.PROCESS_INSERT_COLS_DROP) :
        
        swcw.get_census_main_taskbar()
        
        if(swcm.DEBUG_CENSUS) :
            print("PROCESS_INSERT_COLS_DROP : parms\n",parms)
                
    elif(optionId == swcm.DISPLAY_CHANGE_COL_FOR_ATTRS) :
        
        colname     =   parms[0]
        colid       =   parms[1]
        
        if(swcm.DEBUG_CENSUS) :
            print("DISPLAY_CHANGE_COL_FOR_ATTRS : ",colname,colid)
        
        datasetid               =   swcm.current_dataset_inserting_from.get_datasetid()
        
        subdataid               =   cfg.get_config_value(cfg.CENSUS_SELECTED_SUBSET_ID)
        if(subdataid is None) :
            subdataid   =   0
            
        subdata_col_attributes  =   swcm.current_dataset_inserting_from.get_subdata_col_attributes(subdataid)
        cols_list               =   subdata_col_attributes.get_columns_list() 

        swcw.display_columns_to_insert(datasetid, subdataid, cols_list, int(colid))
        
    elif(optionId == swcm.PROCESS_CHANGE_COL_FOR_ATTRS) :
        
        colname     =   parms[0]
        colid       =   parms[1]
        dtype       =   parms[2]
        nanvalue    =   parms[3]
        
        if(swcm.DEBUG_CENSUS) :
            print("PROCESS_CHANGE_COL_FOR_ATTRS : ",colname,colid,dtype,nanvalue)
            
        datasetid               =   swcm.current_dataset_inserting_from.get_datasetid()
        
        subdataid               =   cfg.get_config_value(cfg.CENSUS_SELECTED_SUBSET_ID)
        if(subdataid is None) :
            subdataid   =   0
            
        subdata_col_attributes  =   swcm.current_dataset_inserting_from.get_subdata_col_attributes(subdataid)
        cols_list               =   subdata_col_attributes.get_columns_list() 
            
        swcw.display_columns_to_insert(datasetid, subdataid, cols_list, int(colid))
            
    elif(optionId == swcm.DISPLAY_INSERT_COLS_TO_DF) :
        
        if(swcm.DEBUG_CENSUS) :
            print("DISPLAY_INSERT_COLS_TO_DF : \n",parms)
        
        datasetid   =   swcm.current_dataset_inserting_from.get_datasetid()    
        user_dfs    =   swcw.get_user_dfs(datasetid)
        
        if(len(user_dfs) > 0) :
            
            swcw.get_census_main_taskbar()
            
            swcw.display_columns_to_insert_dfs()
            
        else :
            
            datasetid   =   swcm.current_dataset_inserting_from.get_datasetid() 
        
            swcm.current_dataset_inserting_from.dump()
            swcw.display_select_dataset_columns_to_insert(datasetid,None)  
            
            display_status("No User df(s) visible to dfc")
            
    elif(optionId == swcm.DISPLAY_INSERT_COLS_TO_DF_CHANGE) :
            
        swcw.get_census_main_taskbar()
        
        if(swcm.DEBUG_CENSUS) :
            print("DISPLAY_INSERT_COLS_TO_DF_CHANGE : \n",parms)
    
        census_df_title     =   parms[0]        
        user_df_title       =   parms[1]
        dfkeys              =   parms[2]
        
        swcw.display_columns_to_insert_dfs(census_df_title,user_df_title,dfkeys)
        
        
"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   Census utility functions
#------------------------------------------------------------------
#------------------------------------------------------------------
""" 

def is_dataset_installed(datasetid) :
    """
    * -------------------------------------------------------------------------- 
    * function : check if a dataset is installed
    * 
    * parms :
    *   datasetid       -   dataset id
    *
    * returns : 
    *  True/False
    * --------------------------------------------------------
    """
    
    dfc_census_dataset_path     =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_dataset_path     =   (dfc_census_dataset_path + "\\datasets\\")
    
    ds_files    =   ["cities","counties","states","zipcode"]
    
    for i in range(len(ds_files)) : 
        #print(dfc_census_dataset_path + swcm.census_data_dirs[i] + "_" + ds_files[i] + ".csv")
        if(does_file_exist(dfc_census_dataset_path + swcm.census_data_dirs[datasetid] + "_" +  ds_files[i] + ".csv")) :
            return(True)
            
    return(False)


def get_subdata_name(dataset_offset,subdata_offset) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the subset name
    * 
    * parms :
    #   dataset_offset -   dataset list offset
    #   subdata_offset -   subdata list offset
    *
    * returns : 
    *  True/False
    * --------------------------------------------------------
    """

    subdata_name_list   =   swcm.subdata_lists[dataset_offset] 
    return(subdata_name_list[subdata_offset]) 
    
    
def get_offset_for_datasetid(datasetid) :
    """
    * -------------------------------------------------------------------------- 
    * function : get the offset for a datasetid
    * 
    * parms :
    *   datasetid -   dataset id
    *
    * returns : 
    *  offset 
    * --------------------------------------------------------
    """
    
    for i in range(len(swcm.census_datasets)) :
        dsid    =   swcm.census_datasets[i].replace("_","")
        if(dsid == datasetid) :
            return(i)
            
    return(None)


"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   Census zip file functions
#------------------------------------------------------------------
#------------------------------------------------------------------
"""

def get_and_save_zipfile(zip_file_name,out_file_name,out_path) :
    """
    * -------------------------------------------------------------------------- 
    * function : unzip a zip file and save to a location
    * 
    * parms :
    *   zip_file_name   -   name and path of the zip file
    *   out_file_name   -   output file name
    *   out_path        -   location to store unzipped file
    *
    * returns : 
    *  offset 
    * --------------------------------------------------------
    """
    
    if(swcm.DEBUG_CENSUS) :

        print("get_and_save_zipfile",zip_file_name)
        print("get_and_save_zipfile",out_file_name)
        print("get_and_save_zipfile",out_path)
    
    
    opstat  =   opStatus()
    
    from zipfile import ZipFile
    
    try :
        
        with ZipFile(zip_file_name, 'r') as zip:
            zip.extract(out_file_name,out_path)  
            
    except Exception as e:
        opstat.store_exception("zip and save ",e)
        display_exception(opstat)
        print(zip_file_name," not found")


def unzip_dataset_files(zipslist) :
    """
    * -------------------------------------------------------------------------- 
    * function : unzip a list of zip files
    * 
    * parms :
    *   zipslist   -   list of zip files
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """

    if(swcm.DEBUG_CENSUS) :
        print("unzip_dataset_files",zipslist)
    
    import os
    
    dfc_census_working_path     =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_working_path     =   (dfc_census_working_path + "\\working\\")
    
    dfc_census_dataset_path     =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_dataset_path     =   (dfc_census_dataset_path + "\\datasets\\")
    
    loadnotes = ["Getting csv files fromo zip files"]
    display_notes(loadnotes,display=True)
    
    clock = RunningClock()
    clock.start()
    
    for i in range(len(zipslist)) :
            
        for j in range(len(zipslist[i])) :
            
            outfilename     =   zipslist[i][j]
            zipfilename     =   dfc_census_working_path + swcm.census_data_dirs[i]+".zip"
            
            swcw.display_short_note("extracting " + outfilename) 

            get_and_save_zipfile(zipfilename,outfilename,dfc_census_dataset_path)

    clock.stop()
    
    display_status("Selected datasets extracted from zips successfully.")


def get_zips_to_process(filelist,downloadlists) :
    """
    * -------------------------------------------------------------------------- 
    * function : get a list of zips to process
    * 
    * parms :
    *   filelist        -   list of csv files
    *   downloadlists   -   list of downloaded files
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path    =   (dfc_census_path + "\\datasets\\")
    
    csvs_list   =   []
    
    for i in range(len(swcm.census_data_dirs)) :
        
        search_for_list     =   []
        
        if(downloadlists[i][4] == "True") :
            
            search_for_list.append(swcm.census_data_dirs[i]+"_zipcode.csv")
            search_for_list.append(swcm.census_data_dirs[i]+"_cities.csv")
            search_for_list.append(swcm.census_data_dirs[i]+"_counties.csv")
            search_for_list.append(swcm.census_data_dirs[i]+"_states.csv")
            
        else :
            
            for j in range(4) :
                
                if(downloadlists[i][j] == "True") :
                    if(j==0)    :   search_for_list.append(swcm.census_data_dirs[i]+"_zipcode.csv")
                    elif(j==1)  :   search_for_list.append(swcm.census_data_dirs[i]+"_cities.csv")
                    elif(j==2)  :   search_for_list.append(swcm.census_data_dirs[i]+"_counties.csv")
                    elif(j==3)  :   search_for_list.append(swcm.census_data_dirs[i]+"_states.csv")
    
        csvs_list.append(search_for_list)
    
    csvs_missing    =   []
    
    for i in range(len(csvs_list)) :
        
        if(len(csvs_list[i]) > 0) :
            
            files_missing   =   []
            
            for j in range(len(csvs_list[i])) :
                
                if(not (does_file_exist(dfc_census_path+csvs_list[i][j]))) :
                    files_missing.append(csvs_list[i][j])

            csvs_missing.append(files_missing)
            
    return(csvs_missing)
        

def any_zips_not_processed(zipslist) :
    """
    * -------------------------------------------------------------------------- 
    * function : see if any zips not processed
    * 
    * parms :
    *   zipslist   -   list of zip files need to be processed
    *
    * returns : 
    *  True/False 
    * --------------------------------------------------------
    """
    
    for i in range(len(zipslist)) :
        for j in range(len(zipslist[i])) :
            if(len(zipslist[i][j]) > 0) :
                return(True)
                
    return(False)
    

def get_zips_not_processed() :
    """
    * -------------------------------------------------------------------------- 
    * function : get a list of zips to process
    * 
    * parms :
    *
    * returns : 
    *  True/False 
    * --------------------------------------------------------
    """
    
    downloadlists   =   cfg.get_config_value(cfg.CENSUS_DOWNLOAD_LISTS)
    
    if(swcm.DEBUG_CENSUS) :
        print("get_zips_not_processed",downloadlists)
    
    dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path    =   (dfc_census_path + "\\datasets\\")
    
    csvs_list   =   []
    
    for i in range(len(swcm.census_data_dirs)) :
        
        search_for_list     =   []
        
        if(downloadlists[i][4] == "True") :
            
            search_for_list.append(swcm.census_data_dirs[i]+"_zipcode.csv")
            search_for_list.append(swcm.census_data_dirs[i]+"_cities.csv")
            search_for_list.append(swcm.census_data_dirs[i]+"_counties.csv")
            search_for_list.append(swcm.census_data_dirs[i]+"_states.csv")
            
        else :
            
            for j in range(4) :
                
                if(downloadlists[i][j] == "True") :
                    if(j==0)    :   search_for_list.append(swcm.census_data_dirs[i]+"_zipcode.csv")
                    elif(j==1)  :   search_for_list.append(swcm.census_data_dirs[i]+"_cities.csv")
                    elif(j==2)  :   search_for_list.append(swcm.census_data_dirs[i]+"_counties.csv")
                    elif(j==3)  :   search_for_list.append(swcm.census_data_dirs[i]+"_states.csv")
    
        csvs_list.append(search_for_list)
    
    csvs_missing    =   []
    
    for i in range(len(csvs_list)) :
        
        if(len(csvs_list[i]) > 0) :
            
            files_missing   =   []
            
            for j in range(len(csvs_list[i])) :
                
                if(not (does_file_exist(dfc_census_path+csvs_list[i][j]))) :
                    files_missing.append(csvs_list[i][j])

            csvs_missing.append(files_missing)
            
    return(csvs_missing)
        

"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   Census download functions
#------------------------------------------------------------------
#------------------------------------------------------------------
"""

def check_if_file_in_missing_files(missing_files,filename) :
    """
    * -------------------------------------------------------------------------- 
    * function : check if a file is missing in the list
    * 
    * parms :
    *   missing_files   -   list of files
    *   filename        -   file to look for
    *
    * returns : 
    *  True/False
    * --------------------------------------------------------
    """
    
    for i in range(len(missing_files))  :
        
        if(type(missing_files[i]) == list) :
            for j in range(len(missing_files[i])) :
                if(missing_files[i][j] == filename) :
                    return(True)
                    
        else :
            if(missing_files[i] == filename) :
                return(True)
                
    return(False)


def are_downloads_selected(downloadlists) :
    """
    * -------------------------------------------------------------------------- 
    * function : check if any downloads are selected
    * 
    * parms :
    *   downloadlists -   requested downloads
    *
    * returns : 
    *  True/False
    * --------------------------------------------------------
    """
    
    for i in range(len(downloadlists)) :
        for j in range(len(downloadlists[i])) :
            if(downloadlists[i][j] == 'True') :
                return(True)
                
    return(False)

    
    
def verify_downloads(downloadlists) :
    """
    * -------------------------------------------------------------------------- 
    * function : check if all zips selected are downloaded
    * 
    * parms :
    *   downloadlists -   requested downloads
    *
    * returns : 
    *  True/False
    * --------------------------------------------------------
    """

    dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path    =   (dfc_census_path + "\\working\\")
    
    files_to_check_for  =   []
    
    for i in range(len(downloadlists)) :
        
        chkflag     =   False
        for j in range(len(downloadlists[i])) :
            
            if(downloadlists[i][j] == "True") :
                chkflag     =   True
            
        if(chkflag) :
            files_to_check_for.append(swcm.zip_file_names[i][0])
                
    if(len(files_to_check_for) > 0) :
                
        files_missing       =   []
        files_to_process    =   []
                
        from dfcleanser.common.common_utils import does_file_exist
        
        #print("files_to_check_for",files_to_check_for)
    
        for i in range(len(files_to_check_for)) :
            
            if(does_file_exist(dfc_census_path + files_to_check_for[i])) :
                files_to_process.append(files_to_check_for[i])
            else :
                files_missing.append(files_to_check_for[i])
  
        return([files_missing,files_to_process])  
        
    else :
        
        return([None,None])
 

"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   Census configure functions
#------------------------------------------------------------------
#------------------------------------------------------------------
"""

def add_dataset(dsname) :
    
    if(swcm.DEBUG_CENSUS) :
        print("add_dataset",dsname)
    
    dfc_census_path     =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path     =   (dfc_census_path + "\\working\\")
    
    dfc_ds_census_path  =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_ds_census_path  =   (dfc_ds_census_path + "\\datasets\\")
    
    dsid    =   ""
    
    for i  in range(len(swcm.census_data_dirs)) :
        if(dsname.find(swcm.census_data_dirs[i]) > -1) :
            dsid    =   swcm.census_data_dirs[i]
            
    if(does_file_exist(dfc_ds_census_path + dsname) ) :
        add_note    =   dsname + " already exists"
    
    else :
        
        if(swcm.DEBUG_CENSUS) :
            print("add_dataset : zip file",dfc_census_path + dsid + ".zip")
            print("add_dataset : out path",dfc_ds_census_path)
        
        if(does_file_exist(dfc_census_path + dsid + ".zip") ) :
            
            try :
                zip_file_name   =   dfc_census_path + dsid + ".zip"
                get_and_save_zipfile(zip_file_name,dsname + ".csv",dfc_ds_census_path)
                add_note    =   "dataset " + dsname + " added successfully"
                
            except :
                add_note    =   "failed to extract " + dsname + "from " + dsname + ".zip"
                
            
        else :
            
            for i in range(len(swcm.census_data_dirs)) :
                if(dsname.find(swcm.census_data_dirs[i]) > -1) :
                    zip_name    =   swcm.census_data_dirs[i]
                    break
            
            add_note    =   zip_name + ".zip needs to be downloaded"
        
    return(add_note)        


def configure_census_data() :
    """
    #------------------------------------------------------------------
    #   configure the selected datasets
    #
    #
    #------------------------------------------------------------------
    """      
    
    import os
    
    opstat  =   opStatus()
    
    dfc_census_path     =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path     =   (dfc_census_path + "\\datasets\\")
    
    add_datasets        =   cfg.get_config_value(cfg.CENSUS_ADD_DATASETS_LIST)
    drop_datasets       =   cfg.get_config_value(cfg.CENSUS_DROP_DATASETS_LIST)
    
    if(swcm.DEBUG_CENSUS) :
        print("configure_census_data",add_datasets,drop_datasets)

    if(not (add_datasets) is None) :
    
        print("\n")
        addnotes = ["Adding Selected datasets"]
        display_notes(addnotes,display=True)

        clock = RunningClock()
        clock.start()
    
        for i in range(len(add_datasets)) :
            add_note    =   add_dataset(add_datasets[i])
            swcw.display_short_note(add_note)
            
            if(add_note.find(".zip needs to be downloaded") > -1) :
                opstat.set_status(False)
    
        clock.stop() 
    
        if(opstat.get_status()) :
            display_status("Selected datasets addeed successfully.")
        else :
            display_status("Not all selected datasets could be added successfully. Click on 'Download Census Data' to download missing zip files.")
            

    
    if(not (drop_datasets) is None) :
    
        dropnotes = ["Dropping Selected datasets"]
        display_notes(dropnotes,display=True)

        clock = RunningClock()
        clock.start()
    
        for i in range(len(drop_datasets)) :
            
            if(swcm.DEBUG_CENSUS) :
                print("drop",dfc_census_path + drop_datasets[i],does_file_exist(dfc_census_path + drop_datasets[i] + ".csv"))
        
            if(does_file_exist(dfc_census_path + drop_datasets[i] + ".csv") ) :
                #swcw.display_short_note("Dropping " + drop_datasets[i])         
                delete_a_file(dfc_census_path + drop_datasets[i] + ".csv",opstat)
                if(not opstat.get_status()) :
                    display_exception(opstat)
                drop_note    =   "dataset " + drop_datasets[i] + " dropped successfully"
                swcw.display_short_note(drop_note)

    
        clock.stop() 
    
        display_status("Selected datasets dropped successfully.")

    
"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   Census load datasets to df functions
#------------------------------------------------------------------
#------------------------------------------------------------------
"""  


  
def load_census_datasets_to_df(datasets_to_load) :
    """
    #------------------------------------------------------------------
    #   load datasets to dfs
    #
    #   datasets_to_load   -   datasets to load
    #
    #------------------------------------------------------------------
    """    
    
    import os
    import pandas as pd
    
    opstat  =   opStatus()
    
    dfc_census_path     =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path     =   (dfc_census_path + "\\datasets\\")
    
    #if(swcm.DEBUG_CENSUS) :
    #    print("load_census_datasets_to_df",datasets_to_load)
    
    
    load_datasets       =   []
    unload_datasets     =   []
    
    datasets_loaded_to_dfs  =   swcm.get_datasets_loaded_to_dfs()
    
    #if(swcm.DEBUG_CENSUS) :
    #    print("datasets_loaded_to_dfs",datasets_loaded_to_dfs)
    
    for i in range(len(datasets_to_load)) :
        
        for j in range(4) :
            
            if(datasets_to_load[i][j] == "True") :
                if(not (datasets_loaded_to_dfs[i][j])) :
                    load_datasets.append(swcm.census_data_dirs[i] + "_" + swcm.get_dataset_type_name(j))
            else :
                if(datasets_loaded_to_dfs[i][j]) :
                    unload_datasets.append(swcm.census_data_dirs[i] + "_" + swcm.get_dataset_type_name(j))

    if(len(load_datasets) > 0) :
    
        print("\n")
        addnotes = ["Loading Selected datasets to memory as dfc df(s)"]
        display_notes(addnotes,display=True)

        clock = RunningClock()
        clock.start()
    
        for i in range(len(load_datasets)) :
            
            try :
                df1         =   pd.read_csv(dfc_census_path + load_datasets[i] + ".csv")
                dfc_df1     =   cfg.dfc_dataframe(load_datasets[i] + "_df",df1,load_datasets[i] + " Census Dataset")
                cfg.add_dfc_dataframe(dfc_df1)
                
            except Exception as e :
                opstat.set_exception(e)
            
            if(opstat.get_status()) :
                add_note    =   "Dataset " + load_datasets[i] + " loaded to " + load_datasets[i] + "_df successfully"
                swcw.display_short_note(add_note)
            
            else :
                add_note    =   "Dataset " + load_datasets[i] + " not loaded successfully"
                swcw.display_short_note(add_note)
                display_exception(opstat)
    
        clock.stop() 
    
        #print("\n")
        if(opstat.get_status()) :
            display_status("Selected census datasets loaded successfully as dfc df(s).")
        else :
            display_status("Not all selected datasets could be loaded successfully.")
            
        #print("\n")
        swcw.display_get_cols_tb()
            

    
    if(len(unload_datasets) > 0) :
    
        dropnotes = ["Unloading Selected datasets from dfs"]
        display_notes(dropnotes,display=True)

        clock = RunningClock()
        clock.start()
    
        for i in range(len(unload_datasets)) :
            
            try :
                
                cfg.drop_dfc_dataframe(unload_datasets[i] + "_df")
            
            except Exception as e :
                opstat.set_exception(e)
            
            if(opstat.get_status()) :
                add_note    =   "Dataset df " + unload_datasets[i] + "_df unloaded successfully"
                swcw.display_short_note(add_note)
            
            else :
                add_note    =   "Dataset df" + unload_datasets[i] + "_df not unloaded successfully"
                swcw.display_short_note(add_note)
                display_exception(opstat)

    
        clock.stop() 
    
        if(opstat.get_status()) :
            display_status("Selected datasets unloaded successfully.")
        else :
            display_status("Not all selected datasets could be unloaded successfully.")


def get_out_col_names(in_col_names) :
    
    col_names_list  =   in_col_names.replace("\n",",")
    col_names_list  =   col_names_list.rstrip(",")
    col_names_list  =   col_names_list.split(",")
    
    return(col_names_list)

    
def get_na_fill_value(na_string) :
    
    import numpy
    
    if(na_string == 'nan') :
        na_value    =   numpy.NaN
    else :
        
        if(na_string.find("'") > -1) :
            na_value    =   na_string.replace("'","")
            
        else :
            
            if(na_string.find('"') > -1) :
                na_value    =   na_string.replace('"',"")
                
            else :
                
                try :
                    na_value    =   float(na_string)
                except :
                    na_value    =   numpy.NaN
                    
    return(na_value)

    
"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   Census insert dataset cols into user dfs
#------------------------------------------------------------------
#------------------------------------------------------------------
"""  
            
def add_census_col_to_df(census_df_title, user_df_title, census_col_name, census_df_index_cols, user_df_index_cols, nan_value, opstat) :

    if(swcm.DEBUG_CENSUS) :
        print("add_census_col_to_df\n",census_df_title, user_df_title, census_col_name, census_df_index_cols, user_df_index_cols)    
        
    try :

        user_df         =   cfg.get_dfc_dataframe_df(user_df_title) 
        census_df       =   cfg.get_dfc_dataframe_df(census_df_title)
        new_columns     =   census_df_index_cols.append(census_col_name)
        new_df          =   census_df[new_columns]
        
        join_df         =   user_df.join(new_df.set_index[census_df_index_cols], on=user_df_index_cols)
        
        # add new df name in parms
           
            
    except :
        opstat.set_status(False)
        opstat.set_errorMsg("Error : Adding " + census_col_name + " to " + user_df_title)            
    
    """

    dct = {'a':3, 'b':3,'c':5,'d':3}
    lst = ['c', 'd', 'a', 'b', 'd']
    
    #map(dct.get, lst)
    list(map(dct.get, lst))
    
    or 
    
    [dct[k] for k in lst]
    
    OR
    
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    k, v = zip(*d.items())
    print(k)                # ('a', 'c', 'b', 'd')
    print(v)                # (1, 3, 2, 4)
    
    """    
 
    

def process_insert_cols_to_df(parms) :
    
    opstat  =   opStatus()

    fparms      =   get_parms_for_input(parms,swcw.insert_cols_in_df_input_idList)
    
    census_df_title     =   fparms[0]
    user_df_title       =   fparms[2]
    index_cols          =   fparms[5]
    
    if(swcm.DEBUG_CENSUS) :
        print("swcm.PROCESS_INSERT_CENSUS_COLS",census_df_title,user_df_title,index_cols)
        
    census_df   =   cfg.get_dfc_dataframe_df(census_df_title)
    user_df     =   cfg.get_dfc_dataframe_df(user_df_title)
    
    
    if(census_df is None) :
        
        opstat.set_status(False)
        opstat.set_errorMsg("Error : census df " + census_df_title + " is invalid ")   

    else :

        if(user_df is None) :
            
            opstat.set_status(False)
            opstat.set_errorMsg("Error : user df " + user_df_title + " is invalid ")  
            
        else :
            
            if(len(index_cols) == 0) :
                
                opstat.set_status(False)
                opstat.set_errorMsg("user df Index columns are not defined ") 
                
            else :
                
                index_cols  =   index_cols.replace("[","")
                index_cols  =   index_cols.replace("]","")
                index_cols  =   index_cols.split(",")
            
                census_index_cols   =   swcm.get_index_keys_for_census_df(census_df_title)
                census_index_cols   =   census_index_cols.replace("[","")
                census_index_cols   =   census_index_cols.replace("]","")
                census_index_cols   =   census_index_cols.split(",")
                
                if(not (len(index_cols) == len(census_index_cols))) :
                
                    opstat.set_status(False)
                    opstat.set_errorMsg("number user df Index columns does not match census df index columns ") 
                    
                else :
                    
                    user_index_names    =   []
                    user_index_dtypes   =   []
                    
                    user_index_columns  =   user_df.index.names
    
                    if(len(user_index_columns) > 0) :
                        for i in range(len(user_index_columns)) :
                            if( not (user_index_columns[i] is None) ) :
                                user_index_names.append(user_index_columns[i])
                                user_index_dtypes.append(user_df.index.levels[i].dtype)
                    
                    index_cols_in_user_df_indices   =   True
                    
                    for i in range(len(index_cols)) :
                        
                        if(not (index_cols[i] in user_index_names)) :
                            
                            index_cols_in_user_df_indices   =   False
                            break
                        
                        else :
                            
                            if(len(census_index_cols) == 1) :
                                
                                from dfcleanser.common.common_utils import is_int_col
                                if(not (is_int_col(user_df,index_cols[i]))) :
                                    
                                    opstat.set_status(False)
                                    opstat.set_errorMsg("user df index column " + index_cols[i] + " is not int datatype")
                                    break;
                                
                            else :
                            
                                from dfcleanser.common.common_utils import is_string_col, is_object_col
                                if(not ( (is_string_col(user_df,index_cols[i])) or (is_object_col(user_df,index_cols[i])) ) ) :
                                    
                                    opstat.set_status(False)
                                    opstat.set_errorMsg("user df index column " + index_cols[i] + " is not string datatype")
                                    break;
                            
    if(opstat.get_status()) :
        
        loadnotes =     ["Loading " + census_df_title + " cols into " + user_df_title]
        display_notes(loadnotes,display=True)
    
        subdata_data        =   swcm.get_subset_data_lists(swcm.current_dataset_inserting_from.get_datasetid())
        subdatacols         =   subdata_data[swcm.SUBSET_COLUMNS]    
        subdatacolstext     =   subdata_data[swcm.SUBSET_COLUMN_NAMES]
        subdatacolsnans     =   subdata_data[swcm.SUBSET_COLUMN_NANS]

        print("subdatacolstext\n",subdatacolstext) 
    
        clock = RunningClock()
        clock.start()
    
        try :
        
            # calculate the columns to drop
            subdata_groups_attributes   =   swcm.current_dataset_inserting_from.get_subdata_group_cols_attributes()
        
            cols_to_drop  =   []
        
            for i in range(len(subdata_groups_attributes)) :
            
                subdata_col_names   =   subdatacols[i]
                subdata_column_attributes   =    swcm.current_dataset_inserting_from.get_subdata_col_attributes(i)
                
                if(subdata_column_attributes.get_column_insert_type() == "List") :
                
                    subata_get_cols_list    =   subdata_column_attributes.get_columns_list()
                
                    for j in range(len(subdata_col_names)) :
                    
                        if(not (subdata_col_names[j] in subata_get_cols_list)) :
                            cols_to_drop.append(subdata_col_names[j])  
                        
                elif(subdata_column_attributes.get_column_insert_type() == "None") :
                
                    for j in range(len(subdata_col_names)) :
                        cols_to_drop.append(subdata_col_names[j])    
                
            print("cols_to_drop",cols_to_drop)  
            
            # drop the columns from the census df
            working_df  =   census_df.drop(cols_to_drop,axis=1)
            
            # get unique values for index cols 
            unique_census_df_index_values   =   census_df.index.unique()
            unique_user_df_index_values     =   user_df.index.unique() 
            
            rows_to_drop    =   []
            
            for i in range(len(unique_census_df_index_values)) :
                
                if(not (unique_census_df_index_values[i] in unique_user_df_index_values)) :
                    rows_to_drop.append(unique_census_df_index_values[i])
                
            # drop rows from census df not in user_df
            working_df  =   working_df.drop(rows_to_drop)
            
            result_df   =   user_df.join(working_df, how="inner")
            
            # apply any col attribute changes to result df
            
            
            
        except :
            opstat.set_status(False)
            opstat.set_errorMsg("Error : Loading " + census_df_title + " cols into " + user_df_title)            
            
        clock.stop()
        
    if(opstat.get_status()) :
        
                
        print("all good")                
        
        
        
        
    else :
        display_exception(opstat)
 
    
        
"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   Census configuration cleanup
#------------------------------------------------------------------
#------------------------------------------------------------------
"""      
def clear_sw_utility_census_data() :
    
    drop_owner_tables(cfg.SWCensusUtility_ID)
    clear_sw_utility_census_cfg_values()
    from dfcleanser.common.html_widgets import delete_all_inputs
    delete_all_inputs(cfg.SWCensusUtility_ID)


def clear_sw_utility_census_cfg_values() :
    
    cfg.drop_config_value(cfg.CENSUS_DOWNLOAD_LISTS)
    cfg.drop_config_value(cfg.CENSUS_CURRENT_MODE)
    cfg.drop_config_value(cfg.CENSUS_DROP_DATASET_LISTS)
    cfg.drop_config_value(cfg.CENSUS_DROP_SUBDATASET_LIST)
    cfg.drop_config_value(cfg.CENSUS_CURRENT_DATASET)
    cfg.drop_config_value(cfg.CENSUS_CURRENT_GET_COLS_SUBDATA_ID)
    cfg.drop_config_value(cfg.CENSUS_ADD_DATASETS_LIST)
    cfg.drop_config_value(cfg.CENSUS_DROP_DATASETS_LIST)
    cfg.drop_config_value(cfg.CENSUS_CURRENT_GET_COLS_SUBDATA_LISTS_ID)


    return()

#https://raw.github.com/someguy/brilliant/master/somefile.txt





