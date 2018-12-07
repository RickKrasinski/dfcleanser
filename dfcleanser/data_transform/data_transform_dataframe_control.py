"""
# data_transform_widgets 
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
import dfcleanser.data_transform.data_transform_dataframe_widgets as dftw

from dfcleanser.data_transform.data_transform_widgets import display_main_option

from dfcleanser.common.common_utils import (display_exception, display_status, 
                                            opStatus, single_quote, get_parms_for_input)

from dfcleanser.common.table_widgets import (dcTable)

from dfcleanser.common.display_utils import display_column_names

from dfcleanser.scripting.data_scripting_control import add_to_script

from IPython.display import clear_output

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    dataframe transform components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    dataframe transform functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    save the column names row
#--------------------------------------------------------------------------
"""
def save_column_names_row(fname):

    opstat = opStatus() 
    
    # see if save col names row 
    if(len(fname) > 0) :
                        
        colids = cfg.get_dfc_dataframe().columns.tolist()

        # save the index row as file
        try :
            with open(fname, 'w') as colid_file :
                json.dump(colids,colid_file)
        except Exception as e:
            opstat.store_exception("Unable to save column names file" + fname,e)
            colid_file.close()

    return(opstat)

"""
#--------------------------------------------------------------------------
#    save the column names row
#--------------------------------------------------------------------------
"""
def change_column_names(parms):

    opstat = opStatus() 
    
    fparms  =   get_parms_for_input(parms[1],dftw.df_change_row_transform_input_idList)
    fparms  =   fparms[0]
    fparms  =   fparms.lstrip('[')
    fparms  =   fparms.rstrip(']')
    fparms  =   fparms.replace(" ,  ",",")
    fparms  =   fparms.replace(" , ",",")
    fparms  =   fparms.replace(" ,",",")
    fparms  =   fparms.replace(", ",",")
    fparms  =   fparms.replace("'","")
    collist =   fparms.split(",")
    
    if(not (len(cfg.get_dfc_dataframe().columns) == len(collist)) ) :
        opstat.set_status(False)
        opstat.set_errorMsg("Number of column names does not match number of columns in dataframe")
    else :
    
        try :
            cfg.get_dfc_dataframe().columns = collist    
        except Exception as e:
            opstat.store_exception("Unable to change column names ",e)
        
    return(opstat)

"""
#--------------------------------------------------------------------------
#    add a column names row
#--------------------------------------------------------------------------
"""
def add_column_names_row(fname,colslist):
    
    opstat = opStatus() 

    colids = []
                    
    # see if get col names row 
    if(not(fname == "None")) :

        # save the index row as file
        try :
            with open(fname, 'r') as colid_file :
                colids = json.load(colid_file)
        except Exception as e:
            opstat.store_exception("Unable to open column names file" + fname,e)
            colid_file.close()
                            
    elif(not(colslist == "None")) :
        colids = colslist
    
    if(opstat.get_status())  :               
        try :
            cfg.get_dfc_dataframe().columns = colids
        except Exception as e: 
            opstat.store_exception("Unable to open column names file" + fname,e)
        
    return(opstat)

"""
#--------------------------------------------------------------------------
#    reset the row ids column
#--------------------------------------------------------------------------
"""
def reset_row_ids_column(startid):
    
    opstat = opStatus() 

    try :
        cfg.get_dfc_dataframe().index = range(startid,len(get_dfc_dataframe().index)+startid)
    except Exception as e:
        opstat.store_exception("Unable to reset row ids",e)

    return(opstat)

"""
#--------------------------------------------------------------------------
#    set a row ids column
#--------------------------------------------------------------------------
"""
def set_row_ids_column(colname):
    
    opstat = opStatus()
    
    try :
        cfg.get_dfc_dataframe().set_index(colname, inplace=True)
    except Exception as e: 
        opstat.store_exception("Unable to set row ids from : " + colname,e)

    return(opstat)

"""
#--------------------------------------------------------------------------
#    drop the row ids column
#--------------------------------------------------------------------------
"""
def drop_row_ids_column():
    
    opstat = opStatus()

    try :
        cfg.get_dfc_dataframe().reset_index(drop=True)
    except Exception as e: 
        opstat.store_exception("Unable to drop row ids column",e)

    return(opstat)

"""
#--------------------------------------------------------------------------
#    drop duplicate rows
#--------------------------------------------------------------------------
"""
def sort_row_ids_column(parms):
    
    print("sort_row_ids_column",parms)
    
    opstat = opStatus()

    return(opstat)



"""
#--------------------------------------------------------------------------
#    drop duplicate rows
#--------------------------------------------------------------------------
"""
def drop_duplicate_rows(colkeys):
    
    opstat = opStatus()

    try :
        if(len(colkeys) > 0) :
            cfg.get_dfc_dataframe().drop_duplicates(colkeys,inplace=True) 
        else :
            cfg.get_dfc_dataframe().drop_duplicates(inplace=True) 
    except Exception as e:
        opstat.store_exception("Unable to drop drop duplicate rows",e)

    return(opstat)


"""
#--------------------------------------------------------------------------
#    process the dataframe transform options
#--------------------------------------------------------------------------
"""
def process_df_transform(parms,display=True) :
    
    print("process_df_transform",parms)

    opstat  =   opStatus()
    
    optionid    =   parms[0][0]
    funcid      =   parms[0][1]
    
    PROCESS_CMD                 =   0
    GET_DEFAULT_FILE_NAME       =   1
    
    dftw.display_dataframe_transform_taskbar()

    if(optionid == dftw.SAVE_COLUMN_NAMES_ROW) :
        
        # remove column names row
        if(funcid == PROCESS_CMD) :
            fparms      =   dftw.get_save_colnames_row_input_parms(parms[1])
            filename    =   fparms[0]
            
            if(len(filename) == 0) :
                filename = "datasets/" + cfg.get_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY)
                filename = filename.replace(".","_")
                filename = filename + "_column_names.json"
            
            opstat  =   save_column_names_row(filename)
            
            if(opstat.get_status()) :
                
                if(display) :
                    
                    #make scriptable
                    add_to_script(["# save column names row",
                                   "from dfcleanser.data_transform.data_transform_dataframe_widgets save_column_names_row",
                                   "save_column_names_row(" + str(filename) + ")"],opstat)
                
                clear_output()

                display_main_option([[0,0]])
                display_status("Column Names Row Saved Successfully to : " + filename)

                clear_dataframe_transform_cfg_values()
                
            else :
                clear_output()
                dftw.display_dataframe_options([[0,1]])
                display_exception(opstat)
                
        # use fefault file name
        elif(funcid == GET_DEFAULT_FILE_NAME) :
             
             # for remove column names row
             if(cfg.get_config_value(dftw.df_save_row_transform_input_id + "Parms") == None) :
            
                fname = ""
                fname = cfg.get_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY)
                if( not (fname == None)) :
                    fname = fname.replace('.','_')
                    fname = fname + "_column_names.json"

                    cfg.set_config_value(dftw.df_save_row_transform_input_id + "Parms",fname)

             dftw.display_save_colnames_row_input()
            
    # add column names row
    elif(optionid == dftw.ADD_COLUMN_NAMES_ROW) :
        
        # add column names row
        if(funcid == PROCESS_CMD) :
            
            fparms      =   dftw.get_add_colnames_row_input_parms(parms)
            filename    =   fparms[0]
            collist     =   fparms[1]
            
            if(len(filename) == 0) :
                filename = "None"
                
            if(len(collist) == 0 ) :
                collist = "None"
            else :
                collist = json.loads(collist)
                
            if( (not(filename == "None")) or (not(collist == "None"))) :
                
                opstat = add_column_names_row(filename,collist)
            
                if(opstat.get_status()) :
                    
                    if(display) :
                        
                        #make scriptable
                        add_to_script(["# Add Column Names Row",
                                       "from dfcleanser.data_transform.data_transform_dataframe_widgets add_column_names_row",
                                       "add_column_names_row(" + single_quote(filename) +"," + json.dumps(collist) + ")"],opstat)

                    clear_output()
                    display_main_option([[0,0]])
                    clear_dataframe_transform_cfg_values()
                    display_status("Column Names Row Added Successfully")
                
                else :
                    
                    clear_output()
                    dftw.display_dataframe_options([[1,0]])
                    display_exception(opstat)

            else :
                
                clear_output()
                dftw.display_dataframe_options([[1,0]])
                opstat.set_status(False)
                opstat.set_errormsg("Adding Column Names Row - No file name or column List defined")
                display_exception(opstat)
    
    elif(optionid == dftw.CHANGE_COLUMN_NAMES) :
        
        opstat = change_column_names(parms)
        
        if(opstat.get_status()) :
                 
            if(display) :
                #make scriptable
                add_to_script(["# change column names",
                               "from dfcleanser.data_transform.data_transform_dataframe_widgets change_column_names",
                               "change_column_names("+",False)"],opstat)
                
                clear_output()
                display_main_option([[0,0]])
                clear_dataframe_transform_cfg_values()
                print("\n")
                display_status("Column Names Changed Successfully")
                col_names_table = dcTable("Column Names ","cnamesTable",cfg.DataTransform_ID)
                col_names_table.set_note(" ")
                display_column_names(cfg.get_dfc_dataframe(),col_names_table,None)    
                
            else :
                
                clear_output()
                dftw.display_dataframe_options([[4,0]])
                display_exception(opstat)
                
    # reset row ids column
    elif(optionid == dftw.RESET_ROW_IDS) :
        
        # Remove Row Ids Column
        if(funcid == PROCESS_CMD) :
            
            fparms  =   dftw.get_reset_colnames_row_input_parms(parms[1])
            startid =   fparms[0]
            
            if(len(startid) > 0) :
                startid = int(startid)
            else :
                startid = 0

            opstat = reset_row_ids_column(startid)
            
            if(opstat.get_status()) :
                 
                if(display) :
                    #make scriptable
                    add_to_script(["# reset row ids column",
                                   "from dfcleanser.data_transform.data_transform_dataframe_widgets reset_row_ids_column",
                                   "reset_row_ids_column(" + str(startid) + ")"],opstat)

                clear_output()
                display_main_option([[0,0]])
                clear_dataframe_transform_cfg_values()
                display_status("Row Index Column Reset Successfully")
                
            else :
                
                clear_output()
                dftw.display_dataframe_options([[1,0]])
                display_exception(opstat)
            
    elif(optionid == dftw.SET_NEW_ROW_IDS_COL) :
        
        if(funcid == PROCESS_CMD) :
            
            fparms  =   dftw.get_set_colnames_row_input_parms(parms[1])
            colname =   fparms[0]
            
            if(len(colname) > 0) :
                
                opstat = set_row_ids_column(colname)      
                
                if(opstat.get_status()) :
                    
                    if(display) :
                        #make scriptable
                        add_to_script(["# set row ids column",
                                       "from dfcleanser.data_transform.data_transform_dataframe_widgets set_row_ids_column",
                                       "set_row_ids_column(" + single_quote(colname) + ")"],opstat)

                    clear_output()
                    display_main_option([[0,0]])
                    clear_dataframe_transform_cfg_values()
                    display_status("Row Index Column Set Successfully")
                
                else :
                
                    clear_output()
                    dftw.display_dataframe_options([[3,0]]) 
                    display_exception(opstat)
                
            else :
                
                clear_output()
                dftw.display_dataframe_options([[3,0]])
                opstat.set_status(False)
                opstat.set_errormsg("No Column Name Defined")
                display_exception(opstat)
        
    elif(optionid == dftw.DROP_ROW_IDS_COL) :
        
        # Remove Row Ids Column
        if(funcid == PROCESS_CMD) :
            
            opstat = drop_row_ids_column()
            
            if(opstat.get_status()) :
                 
                if(display) :
                    #make scriptable
                    add_to_script(["# set row ids column",
                                   "from dfcleanser.data_transform.data_transform_dataframe_widgets drop_row_ids_column",
                                   "drop_row_ids_column()"],opstat)
                
                clear_output()
                display_main_option([[0,0]])
                clear_dataframe_transform_cfg_values()
                
                display_status("Row Index Column Dropped Successfully")
                
            else :
                
                clear_output()
                dftw.display_dataframe_options([[4,0]])
                display_exception(opstat)
    
    elif(optionid == dftw.SORT_ROWS) :
        
        # Remove Row Ids Column
        if(funcid == PROCESS_CMD) :
            
            opstat = sort_row_ids_column(parms)
            
            if(opstat.get_status()) :
                 
                if(display) :
                    #make scriptable
                    add_to_script(["# set row ids column",
                                   "from dfcleanser.data_transform.data_transform_dataframe_widgets sort_row_ids_column",
                                   "sort_row_ids_column()"],opstat)
                
                clear_output()
                display_main_option([[0,0]])
                clear_dataframe_transform_cfg_values()
                
                display_status("Dataframe Sorted Successfully")
                
            else :
                
                clear_output()
                dftw.display_dataframe_options([[4,0]])
                display_exception(opstat)
            
    # drop duplicate rows
    elif(optionid == dftw.DROP_DUPLICATE_ROWS) :

        # drop duplicate rows
        if(funcid == PROCESS_CMD) :
            
            fparms  =   dftw.get_drop_duplicate_rows_input_parms(parms[1])
            collist =   fparms[0]
            
            opstat = drop_duplicate_rows(collist)
            
            if(opstat.get_status()) :
                 
                if(display) :
                    #make scriptable
                    add_to_script(["# drop duplicate rows",
                                   "from dfcleanser.data_transform.data_transform_dataframe_widgets drop_duplicate_rows",
                                   "drop_duplicate_rows("+ json.dumps(collist) + ")"],opstat)

                clear_output()
                display_main_option([[0,0]])
                clear_dataframe_transform_cfg_values()
                
                display_status("Duplicate Rows Dropped Successfully")
                
            else :
                
                clear_output()
                dftw.display_dataframe_options([[4,0]])                
                display_exception(opstat) 
    
    # return
    elif(optionid == dftw.DF_TRANSFORM_RETURN) :
        
        dftw.display_dataframe_transform_main()
        
    # help
    elif(optionid == dftw.DF_TRANSFORM_HELP) :
        print("help")

def clear_dataframe_transform_cfg_values() :
    
    cfg.drop_config_value(dftw.df_save_row_transform_input_id+"Parms")
    cfg.drop_config_value(dftw.df_add_row_transform_input_id+"Parms")
    cfg.drop_config_value(dftw.df_reset_col_transform_input_id+"Parms")
    cfg.drop_config_value(dftw.df_drop_dups_transform_input_id+"Parms")
    cfg.drop_config_value(dftw.df_change_row_transform_input_id+"Parms")    
    cfg.drop_config_value(dftw.df_sort_row_ids_transform_input_id+"Parms")
