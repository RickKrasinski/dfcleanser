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
                                            display_generic_grid, does_file_exist,
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
        
        print("swcm.DISPLAY_DATASET_SUBDATA_DETAILS",parms)
        
        datasetid   =   parms[0]
        subdataid   =   int(parms[1])
        
        cfg.set_config_value(cfg.CENSUS_CURRENT_DATASET,datasetid)
        
        cmode       =   cfg.get_config_value(cfg.CENSUS_CURRENT_MODE)
        
        if(cmode == "LOAD") :
            swcw.display_downloaded_census_data(datasetid,subdataid)
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
        
        swcw.display_configure_verification_data(droplists)

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
    
        
    elif(optionId == swcm.MORE_COLS_SUBDATA_DETAILS) :
        swcw.get_census_main_taskbar()
        
        print("MORE_COLS_SUBDATA_DETAILS",parms)
        datasetid   =   cfg.get_config_value(cfg.CENSUS_CURRENT_DATASET)
        subdataid   =   int(cfg.get_config_value(cfg.CENSUS_CURRENT_GET_COLS_SUBDATA_ID))
        
        colslist    =   parms
        
        if(len(colslist) == 0) :
            cfg.drop_config_value(cfg.CENSUS_SELECTED_DATASET_ID)
            cfg.drop_config_value(cfg.CENSUS_SELECTED_SUBSET_ID)
        else :
            for i in range(len(colslist)) :
                colslist[i]     =   int(colslist[i])
        
        #datasets_cols_dict    =   cfg.get_config_value(cfg.CENSUS_CURRENT_GET_XXXX_SUBDATA_LISTS_ID)
        #if(datasets_cols_dict is None) :
        #    datasets_cols_dict      =   {}
            
        #old version dataset_cols_dict    =   cfg.get_config_value(cfg.CENSUS_CURRENT_GET_XXXX_SUBDATA_LISTS_ID)
        dataset_cols_dict    =   swcm.dfc_census_columns_selected.get_dfc_census_columns_selected_to_load_in_df()

        
        print("MORE_COLS_SUBDATA_DETAILS - dataset_cols_dict : start",dataset_cols_dict)
        
        if(dataset_cols_dict is None) :
            dataset_cols_dict     = {}
        
        subdata_cols_dict    =  dataset_cols_dict.get(datasetid)
        if(subdata_cols_dict is None) :
            subdata_cols_dict     = {}
        
        print("subdata_cols_dict",subdata_cols_dict)
        
        if(not (len(colslist) == 0)) :
        
            subdata_cols_dict.update({subdataid : colslist})
            dataset_cols_dict.update({datasetid : subdata_cols_dict})
            #datasets_cols_dict.update({datasetid : dataset_cols_dict})
            
            #old version cfg.set_config_value(cfg.CENSUS_CURRENT_GET_XXXX_SUBDATA_LISTS_ID,dataset_cols_dict)
            swcm.dfc_census_columns_selected.set_dfc_census_columns_selected_to_load_in_df(dataset_cols_dict)            
        
        excludes    =   list(subdata_cols_dict.keys())
        
        print("excludes",excludes)
        
        print("subdata_cols_dict",subdata_cols_dict)
        print("dataset_cols_dict",dataset_cols_dict)
        #print("datasets_cols_dict",datasets_cols_dict)
        
        #old version print("dataset_cols_dict : end",cfg.get_config_value(cfg.CENSUS_CURRENT_GET_XXXX_SUBDATA_LISTS_ID))
        print("dataset_cols_dict : end",swcm.dfc_census_columns_selected.get_dfc_census_columns_selected_to_load_in_df())
        
        swcw.display_get_dataset_columns(datasetid,excludes,None)
        
        
    elif(optionId == swcm.VERIFY_LOAD_CENSUS_TO_DFC_DFS) :
        
        print("VERIFY_LOAD_CENSUS_TO_DFC_DFS",parms)
        swcw.get_census_main_taskbar()

        cfg.set_config_value(cfg.CENSUS_CURRENT_MODE,"ADD_TO_DFS")
        
        droplists   =   parms
        cfg.set_config_value(cfg.CENSUS_DROP_DATASET_LISTS,droplists)
        
        swcw.display_load_to_df_verification_data(droplists)
        #display_load_to_df_verification_data(datasets_to_load_to_dfs)

    elif(optionId == swcm.PROCESS_LOAD_TO_DFC_DFS) :
        
        print("PROCESS_LOAD_TO_DFC_DFS",parms)
        swcw.get_census_main_taskbar()
        load_census_datasets_to_df(cfg.get_config_value(cfg.CENSUS_DROP_DATASET_LISTS))
        #print(cfg.get_config_value(cfg.CENSUS_DROP_DATASET_LISTS))
        
    elif(optionId == swcm.SHOW_SELECTED_COLUMNS) :
        swcw.get_census_main_taskbar()
         
        print("swcm.SHOW_SELECTED_COLUMNS",parms)
        swcw.display_dataset_columns_selected(parms)        

        
    elif(optionId == swcm.DISPLAY_INSERT_CENSUS_COLS) :
        swcw.get_census_main_taskbar()
        swcw.display_columns_to_insert(parms)
        
    elif(optionId == swcm.PROCESS_INSERT_CENSUS_COLS) :
        swcw.get_census_main_taskbar()
        process_insert_cols_to_df(parms)        
    

    elif(optionId == swcm.DISPLAY_EXPORT_CENSUS_DFS) :
        swcw.get_census_main_taskbar()
        print("DISPLAY_EXPORT_CENSUS_DFS")
        swcw.display_datasets_to_export()

    elif(optionId == swcm.PROCESS_EXPORT_CENSUS_DFS) :
        swcw.get_census_main_taskbar()
        print("PROCESS_EXPORT_CENSUS_DFS") 



    elif(optionId == swcm.DISPLAY_LOAD_CENSUS_DATA_TO_DB) :
        swcw.get_census_main_taskbar()
        swcw.display_datasets_to_load_to_db()

    elif(optionId == swcm.PROCESS_LOAD_CENSUS_DATA_TO_DB) :
        swcw.get_census_main_taskbar()
        print("PROCESS_LOAD_CENSUS_DATA_TO_DB") 
        
        

        
    #"""
    #--------------------------------------------------------------------------
    #   get datasets columns commands
    #--------------------------------------------------------------------------
    #"""
        
    elif(optionId == swcm.DISPLAY_GET_CENSUS_DATA) :
        swcw.get_census_main_taskbar()
        print("dm.DISPLAY_GET_CENSUS_DATA",parms)
        
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
            
        
        # old version dataset_cols_dict    =   cfg.get_config_value(cfg.CENSUS_CURRENT_GET_XXXX_SUBDATA_LISTS_ID)
        dataset_cols_dict    =   swcm.dfc_census_columns_selected.get_dfc_census_columns_selected_to_load_in_df()
        print("DISPLAY_GET_CENSUS_DATA - dataset_cols_dict : start",dataset_cols_dict)
        
        if(dataset_cols_dict is None) :
            excludes    =   None
        else :
        
            subdata_cols_dict    =  dataset_cols_dict.get(dsid)
            if(subdata_cols_dict is None) :
                excludes    =   None
            else :
                excludes    =   list(subdata_cols_dict.keys())
        
        print("excludes",excludes)
        
        swcw.display_get_dataset_columns(dsid,excludes,dtid)


    elif(optionId == swcm.DISPLAY_LOAD_CENSUS_TO_DFC_DFS) :
        swcw.get_census_main_taskbar()
        print("dm.DISPLAY_LOAD_CENSUS_TO_DFC_DFS",parms)

        swcw.display_datasets_loaded_to_dfs()






    



        

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
    
    print("load_census_datasets_to_df",datasets_to_load)
    
    
    load_datasets       =   []
    unload_datasets     =   []
    
    datasets_loaded_to_dfs  =   swcm.get_datasets_loaded_to_dfs()
    
    print("datasets_loaded_to_dfs",datasets_loaded_to_dfs)
    
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
        addnotes = ["Loading Selected datasets to dfs"]
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
    
        if(opstat.get_status()) :
            display_status("Selected datasets loaded successfully.")
        else :
            display_status("Not all selected datasets could be loaded successfully.")
            

    
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

    print("swcm.PROCESS_INSERT_CENSUS_COLS",parms)
    
    import os
    import pandas as pd
    
    opstat      =   opStatus()
    
    dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path    =   (dfc_census_path + "\\datasets\\")

    
    fparms      =   get_parms_for_input(parms,swcw.insert_cols_in_df_input_idList)
    
    index_type      =   fparms[0]
    insert_df       =   fparms[1]
    index_cols      =   fparms[3]
    nan_value       =   fparms[4]
    
    print("swcm.PROCESS_INSERT_CENSUS_COLS",index_type,insert_df,index_cols,nan_value)
    
    datasetid       =   cfg.get_config_value(cfg.CENSUS_SELECTED_DATASET_ID)
    subsetid        =   cfg.get_config_value(cfg.CENSUS_SELECTED_SUBSET_ID)

    print("swcm.PROCESS_INSERT_CENSUS_COLS : dataset - subset ",datasetid,subsetid)
    
    columns_list    =   swcm.dfc_census_columns_selected.get_columns_selected_to_load_in_df(datasetid,subsetid)
    
    print("swcm.PROCESS_INSERT_CENSUS_COLS : columns_list ",columns_list)
    
    df_titles           =   cfg.get_dfc_dataframes_titles_list()
    
    dataset_id_offset   =   swcm.get_datasetid_offset(datasetid)
    
    if(index_type == "[zipcode]") :
        df_title    =   swcm.census_data_dirs[dataset_id_offset] + "_zipcode_df"
        csv_title   =   swcm.census_data_dirs[dataset_id_offset] + "_zipcode.csv"
        col_names   =   ["Zip Code"]
    elif(index_type == "[city,state]") :
        df_title    =   swcm.census_data_dirs[dataset_id_offset] + "_cities_df"
        csv_title   =   swcm.census_data_dirs[dataset_id_offset] + "_cities.csv"
        col_names   =   ["State","City"]
    elif(index_type == "[county,state]") :
        df_title    =   swcm.census_data_dirs[dataset_id_offset] + "_counties_df"
        csv_title   =   swcm.census_data_dirs[dataset_id_offset] + "_counties.csv"
        col_names   =   ["State","County"]
    else :
        df_title    =   swcm.census_data_dirs[dataset_id_offset] + "_states_df"
        csv_title   =   swcm.census_data_dirs[dataset_id_offset] + "_states.csv"
        col_names   =   ["State"]
        
    if(not(df_title in df_titles )) :
        
        loadnotes =     ["Loading " + csv_title + " into " + df_title]
        display_notes(loadnotes,display=True)
        
        clock = RunningClock()
        clock.start()
    
        try :
            
            df1         =   pd.read_csv(dfc_census_path + csv_title)
            dfc_df1     =   cfg.dfc_dataframe(df_title,df1,df_title + " Census Dataset")
            cfg.add_dfc_dataframe(dfc_df1)
            
        except :
            opstat.set_status(False)
            opstat.set_errorMsg("Error : Loading " + csv_title + " into " + df_title)            
            
        clock.stop()
        
    if(opstat.get_status()) :
        
        loadnotes =     ["Loading " + csv_title + " into " + df_title]
        display_notes(loadnotes,display=True)
        
        clock = RunningClock()
        clock.start()
    
        try :
            
            df1         =   pd.read_csv(dfc_census_path + csv_title)
            dfc_df1     =   cfg.dfc_dataframe(df_title,df1,df_title + " Census Dataset")
            cfg.add_dfc_dataframe(dfc_df1)
            
        except :
            opstat.set_status(False)
            opstat.set_errorMsg("Error : Loading " + csv_title + " into " + df_title)            
            
        clock.stop()
        
        
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
    cfg.drop_config_value(cfg.CENSUS_GET_COLS_COLUMNS_LIST_ID)
    cfg.drop_config_value(cfg.CENSUS_ADD_DATASETS_LIST)
    cfg.drop_config_value(cfg.CENSUS_DROP_DATASETS_LIST)
    cfg.drop_config_value(cfg.CENSUS_CURRENT_GET_COLS_SUBDATA_LISTS_ID)


    return()

#https://raw.github.com/someguy/brilliant/master/somefile.txt





