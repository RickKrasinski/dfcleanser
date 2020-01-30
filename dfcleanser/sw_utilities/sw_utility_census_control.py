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
                                            get_parms_for_input)

   
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
        
        swcw.display_load_census_data()
        
    elif(optionId == swcm.DISPLAY_CENSUS_DATA_DETAILS) :
        swcw.get_census_main_taskbar()
        datasetid   =   parms

        swcw.display_load_census_data(datasetid)
    
    elif(optionId == swcm.DISPLAY_CENSUS_SUBDATA_DETAILS) :
        swcw.get_census_main_taskbar()
        
        datasetid   =   parms[0]
        subdataid   =   int(parms[1])
        
        cfg.set_config_value(cfg.CENSUS_CURRENT_DATASET,datasetid)
        currentmode     =   cfg.get_config_value(cfg.CENSUS_CURRENT_MODE)
        
        if(currentmode  ==  "CONFIGURE") :
            swcw.display_load_census_data(datasetid,True,subdataid)
        else :
            swcw.display_load_census_data(datasetid,False,subdataid)
    
    elif(optionId == swcm.PROCESS_DOWNLOAD_CENSUS_DATA) :
        swcw.get_census_main_taskbar()
        
        downloadlists   =   parms
        cfg.set_config_value(cfg.CENSUS_DOWNLOAD_LISTS,downloadlists)

        swcw.display_download_census_confirmation(downloadlists)


    elif(optionId == swcm.VERIFY_DOWNLOAD_CENSUS_DATA) :
        swcw.get_census_main_taskbar()
        
        downloadlists   =   cfg.get_config_value(cfg.CENSUS_DOWNLOAD_LISTS)
        swcw.display_download_census_confirmation(downloadlists,True)


    elif(optionId == swcm.DISPLAY_DOWNLOADED_ZIP_FILES) :
        swcw.get_census_main_taskbar()
        
        downloadlists   =   cfg.get_config_value(cfg.CENSUS_DOWNLOAD_LISTS)
        swcw.display_process_downloaded_files(downloadlists)

    elif(optionId == swcm.DISPLAY_PROCESSED_ZIP_FILES) :
        swcw.get_census_main_taskbar()
         
        downloadlists   =   cfg.get_config_value(cfg.CENSUS_DOWNLOAD_LISTS)
        swcw.display_process_downloaded_files(downloadlists) 
        
    elif(optionId == swcm.PROCESS_DOWNLOADED_ZIP_FILES) :
        swcw.get_census_main_taskbar()
        
        downloadlists   =   cfg.get_config_value(cfg.CENSUS_DOWNLOAD_LISTS)
        zips_not_processed  =   get_zips_not_processed()
        
        if(any_zips_not_processed(zips_not_processed)) :
            unzip_dataset_files(zips_not_processed)
            
        process_note_html = swcw.process_notes_complete_html
            
        gridclasses     =   ["dfc-main"]
        gridhtmls       =   [process_note_html]
    
        display_generic_grid("dfcensus-note-wrapper",gridclasses,gridhtmls)
            

        cfg.drop_config_value(cfg.CENSUS_DOWNLOAD_LISTS)



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
        
        swcw.display_load_census_data(None,True)
        
    elif(optionId == swcm.DISPLAY_CONFIGURE_DATA_DETAILS) :
        swcw.get_census_main_taskbar()
        
        datasetid   =   parms
        cfg.set_config_value(cfg.CENSUS_CURRENT_DATASET,datasetid)

        swcw.display_load_census_data(datasetid,True)
    
    elif(optionId == swcm.DISPLAY_CONFIGURE_SUBDATA_DETAILS) :
        swcw.get_census_main_taskbar()
        
        datasetid   =   parms[0]
        subdataid   =   int(parms[1])
        
        cfg.set_config_value(cfg.CENSUS_CURRENT_DATASET,datasetid)
        swcw.display_load_census_data(datasetid,True,subdataid)
        
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
    #   common list commands
    #--------------------------------------------------------------------------
    #"""
        
    elif(optionId == swcm.DISPLAY_SCROLL_CENSUS_COL_NAMES) :
        swcw.get_census_main_taskbar()
        
        datasetid   =   parms[0]
        subdataid   =   int(parms[1])
        colnameid   =   int(parms[2])
        direction   =   int(parms[3])
        
        currentmode     =   cfg.get_config_value(cfg.CENSUS_CURRENT_MODE)
        if(currentmode  ==  "CONFIGURE") :
            swcw.display_load_census_data(datasetid,True,subdataid,colnameid,direction)
        else :
            swcw.display_load_census_data(datasetid,False,subdataid,colnameid,direction)



    #"""
    #--------------------------------------------------------------------------
    #   load datasets to memory commands
    #--------------------------------------------------------------------------
    #"""

    elif(optionId == swcm.DISPLAY_LOAD_CENSUS_DATA) :
        swcw.get_census_main_taskbar()
        swcw.display_load_datasets()
    
    elif(optionId == swcm.DISPLAY_LOAD_CENSUS_DATA_TO_DB) :
        swcw.get_census_main_taskbar()
        swcw.display_load_datasets(False)
        
    elif(optionId == swcm.PROCESS_LOAD_CENSUS_DATA_TO_DF) :
        swcw.get_census_main_taskbar()
        loadlist    =   parms
        load_census_datasets_to_df(loadlist)
        
    elif(optionId == swcm.DISPLAY_COLS_SUBDATA_DETAILS) :
        swcw.get_census_main_taskbar()
        cfg.set_config_value(cfg.CENSUS_CURRENT_DATASET,parms[0])
        cfg.set_config_value(cfg.CENSUS_CURRENT_GET_COLS_SUBDATA_ID,int(parms[1]))
        swcw.display_get_dataset_columns(parms[0],None,int(parms[1]))
        
    elif(optionId == swcm.PROCESS_COLS_SUBDATA_DETAILS) :
        swcw.get_census_main_taskbar()
        datasetid   =   cfg.get_config_value(cfg.CENSUS_CURRENT_DATASET)
        subdataid   =   int(cfg.get_config_value(cfg.CENSUS_CURRENT_GET_COLS_SUBDATA_ID))
        dsdtype     =   int(cfg.get_config_value(cfg.CENSUS_CURRENT_GET_COLS_DTYPE_ID))
        
        colslist    =   parms
        cfg.set_config_value(cfg.CENSUS_GET_COLS_COLUMNS_LIST_ID,colslist)
        
        swcw.display_get_census_columns(datasetid,dsdtype,subdataid,colslist)

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
            dtid    =   int(parms[0])
            dsid    =   parms[1]
            cfg.set_config_value(cfg.CENSUS_CURRENT_GET_COLS_DTYPE_ID,dtid)
            cfg.set_config_value(cfg.CENSUS_CURRENT_DATASET,dsid)
            
        swcw.display_get_dataset_columns(dsid,dtid)


    elif(optionId == swcm.PROCESS_GET_CENSUS_DATA) :
        swcw.get_census_main_taskbar()
        
        add_census_columns_to_df(parms)







    



        

"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   Census utility functions
#------------------------------------------------------------------
#------------------------------------------------------------------
""" 

def is_dataset_installed(datasetid) :
    
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
    #------------------------------------------------------------------
    #   get the subdata name
    #
    #   dataset_offset -   dataset list offset
    #   subdata_offset -   subdata list offset
    #
    #------------------------------------------------------------------
    """      

    subdata_name_list   =   swcm.subdata_lists[dataset_offset] 
    return(subdata_name_list[subdata_offset]) 
    
    
def get_offset_for_datasetid(datasetid) :
    """
    #------------------------------------------------------------------
    #   get the offset for a datasetid
    #
    #   datasetid -   dataset id
    #
    #------------------------------------------------------------------
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
    #------------------------------------------------------------------
    #   unzip a zip file and save to a location
    #
    #   zip_file_name   -   name and path of the zip file
    #   out_file_name   -   output file name
    #   out_path        -   location to store unzipped file
    #
    #------------------------------------------------------------------
    """      
    
    from zipfile import ZipFile
    
    try :
        
        with ZipFile(zip_file_name, 'r') as zip:
            zip.extract(out_file_name,out_path)  
            
    except :
        print(zip_file_name," not found")


def unzip_dataset_files(zipslist) :
    """
    #------------------------------------------------------------------
    #   unzip a list of zip files
    #
    #   zipslist   -   list of zip files
    #
    #------------------------------------------------------------------
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
    #------------------------------------------------------------------
    #   get a list of zips to process
    #
    #   filelist   -   list of csv files
    #
    #------------------------------------------------------------------
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
    #------------------------------------------------------------------
    #   see if any zips not processed
    #
    #   zipslist   -   list of zip files need to be processed
    #
    #------------------------------------------------------------------
    """      
    
    for i in range(len(zipslist)) :
        for j in range(len(zipslist[i])) :
            if(len(zipslist[i][j]) > 0) :
                return(True)
                
    return(False)
    

def get_zips_not_processed() :
    """
    #------------------------------------------------------------------
    #   get a list of zips to process
    #
    #   filelist   -   list of csv files
    #
    #------------------------------------------------------------------
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
    #------------------------------------------------------------------
    #   get a list of file parts
    #
    #   missing_files -   multi level list of file names
    #   filename      -   file that is searched for
    #
    #------------------------------------------------------------------
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
    #------------------------------------------------------------------
    #   check if any downloads are selected
    #
    #   downloadlists -   requested downloads
    #
    #------------------------------------------------------------------
    """      
    
    for i in range(len(downloadlists)) :
        for j in range(len(downloadlists[i])) :
            if(downloadlists[i][j] == 'True') :
                return(True)
                
    return(False)

    
    
def verify_downloads(downloadlists) :
    """
    #------------------------------------------------------------------
    #   check if all zips selected are downloaded
    #
    #   downloadlists -   requested downloads
    #
    #------------------------------------------------------------------
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
    
    dfc_census_path     =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path     =   (dfc_census_path + "\\working\\")
    
    dfc_ds_census_path  =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_ds_census_path  =   (dfc_census_path + "\\datasets\\")
    
    dsid    =   ""
    
    for i  in range(len(swcm.census_data_dirs)) :
        if(dsname.find(swcm.census_data_dirs[i]) > -1) :
            dsid    =   swcm.census_data_dirs[i]
            
    if(does_file_exist(dfc_ds_census_path + dsname) ) :
        add_note    =   dsname + " already exists"
    
    else :
        
        if(does_file_exist(dfc_census_path + dsid + ".zip") ) :
            
            try :
                zip_file_name   =   dfc_census_path + dsid + ".zip"
                get_and_save_zipfile(zip_file_name,dsname,dfc_ds_census_path)
                add_note    =   "dataset " + dsname + " added successfully"
                
            except :
                add_note    =   "failed to extract " + dsname + "from " + dsname + ".zip"
                
            
        else :
            add_note    =   dsname + ".zip needs to be downloaded"
        
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
    
        clock.stop() 
    
        display_status("Selected datasets addeed successfully.")

    
    if(not (drop_datasets) is None) :
    
        dropnotes = ["Dropping Selected datasets"]
        display_notes(dropnotes,display=True)

        clock = RunningClock()
        clock.start()
    
        for i in range(len(drop_datasets)) :
        
            if(does_file_exist(dfc_census_path + drop_datasets[i]) ) :
                swcw.display_short_note("Dropping " + drop_datasets[i])         
                delete_a_file(dfc_census_path + drop_datasets[i],opstat)
    
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
    #print("load_census_datasets_to_df\n",datasets_to_load)
    
    import os
    
    import pandas as pd
    
    dfc_census_path    =   os.path.join(cfg.get_dfcleanser_location(),"files","census")
    dfc_census_path    =   (dfc_census_path + "\\datasets\\")
    
    print("\n")
    loadnotes = ["Loading Selected datasets"]
    display_notes(loadnotes,display=True)

    clock = RunningClock()
    clock.start()

    for i in range(len(datasets_to_load)) :
        for j in range(len(datasets_to_load[i])) :
            
            #print("datasets_to_load[i][j]",datasets_to_load[i][j])
            
            if(datasets_to_load[i][j] == "True") :
                
                if(j==0)        :   dftype  =   "zipcode"
                elif(j==1)      :   dftype  =   "cities"
                elif(j==2)      :   dftype  =   "counties"
                elif(j==3)      :   dftype  =   "states"
               
                df_name     =   swcm.census_data_dirs[i] + "_" + dftype
                
                swcw.display_short_note("loading " + df_name + " to " + df_name + "_df") 
                
                df1         =   pd.read_csv(dfc_census_path + df_name + ".csv")
                dfc_df1     =   cfg.dfc_dataframe(df_name + "_df",df1,df_name + " Census Dataset")
                cfg.add_dfc_dataframe(dfc_df1)
                
    
    clock.stop()
    
    display_status("Selected datasets loaded to df(s) successfully.")


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

            
def add_census_col_to_df(i,dtid,dsid,output_df,key_values,out_col_names,na_value,dfc_col_names) :
    
    print("add_census_col_to_df\n",i,dtid,dsid,"\n",output_df,"\n",key_values,"\n",out_col_names,"\n",na_value,type(na_value),"\n",dfc_col_names)    
        
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
 
    
def add_census_columns_to_df(inputParms) :
    """
    #------------------------------------------------------------------
    #   add census columns to dataframe to dfs
    #
    #   datasets_to_load   -   datasets to load
    #
    #------------------------------------------------------------------
    """      
    #print("load_census_datasets_to_df\n",datasets_to_load)
    
    
    colslist    =   cfg.get_config_value(cfg.CENSUS_GET_COLS_COLUMNS_LIST_ID)
    
    dtid        =   cfg.get_config_value(cfg.CENSUS_CURRENT_GET_COLS_DTYPE_ID)
    dsid        =   cfg.get_config_value(cfg.CENSUS_CURRENT_DATASET)
    subid       =   cfg.get_config_value(cfg.CENSUS_CURRENT_GET_COLS_SUBDATA_ID)
    
    if(dtid == 0)       :   idlist  =   swcw.get_census_cols_input_idList
    elif(dtid == 1)     :   idlist  =   swcw.get_city_census_cols_input_idList
    elif(dtid == 2)     :   idlist  =   swcw.get_county_census_cols_input_idList
    elif(dtid == 3)     :   idlist  =   swcw.get_states_census_cols_input_idList
    
    fparms      =   get_parms_for_input(inputParms,idlist)
    
    if(dtid == 0) :
        output_df       =   fparms[0]
        zipcode_col     =   fparms[1]
        key_values      =   [zipcode_col]
        out_col_names   =   get_out_col_names(fparms[2])
        na_value        =   get_na_fill_value(fparms[3])
        
    elif( (dtid == 1) or (dtid == 2) ):
        output_df       =   fparms[0]
        city_col        =   fparms[1]
        state_col       =   fparms[2]
        key_values      =   [city_col,state_col]
        out_col_names   =   get_out_col_names(fparms[3])
        na_value        =   get_na_fill_value(fparms[4])
    
    elif(dtid == 3) :
        output_df       =   fparms[0]
        state_col       =   fparms[1]
        key_values      =   [state_col]
        out_col_names   =   get_out_col_names(fparms[2])
        na_value        =   get_na_fill_value(fparms[3])
        
    else :
        output_df       =   None
        key_values      =   None
        out_col_names   =   None
        na_value        =   None
        
    dfc_col_names_list  =   swcm.get_subdata_colnames(dsid,subid) 
    
    dfc_col_names   =   []
    for i in range(len(colslist)) :
        cindex   =   int(colslist[i])
        dfc_col_names.append(dfc_col_names_list[cindex])
        
        
    loadnotes = ["Inserting Selected census column into dataset " + output_df]
    display_notes(loadnotes,display=True)

    clock = RunningClock()
    clock.start()
        
    for i in range(len(out_col_names)) :
        
        swcw.display_short_note("adding " + dfc_col_names[i] + " column to " + output_df) 

        add_census_col_to_df(i,dtid,dsid,output_df,key_values,out_col_names,na_value,dfc_col_names)
        
    clock.stop()
    
    display_status("Selected census columns added to df successfully.")
    
        
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
    cfg.drop_config_value(cfg.CENSUS_CURRENT_GET_COLS_DTYPE_ID)
    cfg.drop_config_value(cfg.CENSUS_GET_COLS_COLUMNS_LIST_ID)
    cfg.drop_config_value(cfg.CENSUS_ADD_DATASETS_LIST)
    cfg.drop_config_value(cfg.CENSUS_DROP_DATASETS_LIST)


    return()

#https://raw.github.com/someguy/brilliant/master/somefile.txt





