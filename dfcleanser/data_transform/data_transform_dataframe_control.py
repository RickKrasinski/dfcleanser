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
import dfcleanser.data_transform.data_transform_model as dtm

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
                        
        colids = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF).columns.tolist()

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
    
    if(not (len(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF).columns) == len(collist)) ) :
        opstat.set_status(False)
        opstat.set_errorMsg("Number of column names does not match number of columns in dataframe")
    else :
    
        try :
            cfg.cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF).columns = collist    
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
            cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF).columns = colids
        except Exception as e: 
            opstat.store_exception("Unable to open column names file" + fname,e)
        
    return(opstat)

"""
#--------------------------------------------------------------------------
#    reset the row ids column
#--------------------------------------------------------------------------
"""
def reset_df_index(parms):
    
    opstat = opStatus() 
    
    fparms      =   get_parms_for_input(parms,dftw.df_reset_index_transform_input_idList)

    if(len(fparms[0]) == 0) :
        colnames = None
    else :
        colnames = fparms[0]
        
    if(fparms[1] == "True") :
        drop = True
    else :
        drop = False
            
    if(fparms[3] == "True") :
        inplace = True
    else :
        inplace = False
            
        if(len(fparms[4]) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("column names list is empty")
        else :
            resultdf    =   fparms[4]
                
 
    if(opstat.get_status()) :
        
        df = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)

        try : 
            
            if(inplace) :
                df.reset_index(colnames,drop=drop,inplace=True)
            else :
                newdf               =   df.reset_index(colnames,drop=drop,inplace=False)
                new_dfcnotes        =   "reset index " + colnames
                new_dfc_dataframe   =   cfg.dfc_dataframe(resultdf,newdf,new_dfcnotes)
                cfg.add_dfc_dataframe(new_dfc_dataframe)
        
        except Exception as e: 
            opstat.store_exception("Unable to reset df index : " + colnames,e)

    return(opstat)
    

"""
#--------------------------------------------------------------------------
#    set a row ids column
#--------------------------------------------------------------------------
"""
def set_df_index(parms):
    
    opstat = opStatus()
    
    fparms      =   get_parms_for_input(parms,dftw.df_set_index_transform_input_idList)

    colnames    =   fparms[0]
    
    if(len(colnames) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("column names list is empty")
        
    else :
        
        if(fparms[1] == "True") :
            drop = True
        else :
            drop = False
            
        if(fparms[2] == "True") :
            inplace = True
        else :
            inplace = False
            
        if(not inplace) :
            if(len(fparms[3]) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("result df name is empty")
            else :
                
                resultdf    =   fparms[3]
                
                if(fparms[4] == "True") :
                    verify = True
                else :
                    verify = False
 
    if(opstat.get_status()) :
        
        df = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)

        try : 
            
            if(inplace) :
                df.set_index(colnames,drop=drop,append=False,inplace=True,verify_integirty=verify)
            else :
                newdf               =   df.set_index(colnames,drop=drop,append=False,inplace=False,verify_integirty=verify)
                new_dfcnotes        =   "set index " + colnames
                new_dfc_dataframe   =   cfg.dfc_dataframe(resultdf,newdf,new_dfcnotes)
                cfg.add_dfc_dataframe(new_dfc_dataframe)
        
        except Exception as e: 
            opstat.store_exception("Unable to set row ids from : " + colnames,e)

    return(opstat)

"""
#--------------------------------------------------------------------------
#    drop the row ids column
#--------------------------------------------------------------------------
"""
def append_to_df_index(parms):
    
    opstat = opStatus()

    fparms      =   get_parms_for_input(parms,dftw.df_append_index_transform_input_idList)

    colnames    =   fparms[0]
    
    if(len(colnames) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("column names list is empty")
        
    else :
        
        if(fparms[1] == "True") :
            drop = True
        else :
            drop = False
        
        if(fparms[2] == "True") :
            inplace = True
        else :
            inplace = False
            
        if(not inplace) :
            if(len(fparms[3]) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("result df name is empty")
            else :
                
                resultdf    =   fparms[3]
                
    if(opstat.get_status()) :
        
        df = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)

        try : 
            
            if(inplace) :
                df.set_index(colnames,drop=drop,append=True,inplace=True)
            else :
                newdf               =   df.set_index(colnames,drop=drop,append=True,inplace=False)
                new_dfcnotes        =   "append to index " + colnames
                new_dfc_dataframe   =   cfg.dfc_dataframe(resultdf,newdf,new_dfcnotes)
                cfg.add_dfc_dataframe(new_dfc_dataframe)
        
        except Exception as e: 
            opstat.store_exception("Unable to append to df index : " + colnames,e)

    return(opstat)


"""
#--------------------------------------------------------------------------
#    drop duplicate rows
#--------------------------------------------------------------------------
"""
def sort_df_index(parms):
    
    opstat = opStatus()
    
    fparms      =   get_parms_for_input(parms,dftw.df_sort_index_transform_input_idList)

    colnames    =   fparms[0]
    
    if(len(colnames) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("column names list is empty")
        
    else :
        
        if(fparms[1] == "True") :
            ascending = True
        else :
            ascending = False
        
        if(fparms[2] == "True") :
            inplace = True
        else :
            inplace = False
            
        if(not inplace) :
            if(len(fparms[3]) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("result df name is empty")
            else :
                
                resultdf    =   fparms[3]
                kind        =   fparms[4]
                na_position =   fparms[5]
                
    if(opstat.get_status()) :
        
        df = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)

        try : 
            
            if(inplace) :
                df.set_index(colnames,level=None,ascending=ascending,inplace=True,kind=kind,na_position=na_position)
            else :
                newdf               =   df.set_index(colnames,level=None,ascending=ascending,inplace=False,kind=kind,na_position=na_position)
                new_dfcnotes        =   "sort index " + colnames
                new_dfc_dataframe   =   cfg.dfc_dataframe(resultdf,newdf,new_dfcnotes)
                cfg.add_dfc_dataframe(new_dfc_dataframe)
        
        except Exception as e: 
            opstat.store_exception("Unable to sort df index : " + colnames,e)

    return(opstat)


"""
#--------------------------------------------------------------------------
#    drop duplicate rows
#--------------------------------------------------------------------------
"""
def drop_duplicate_rows(parms):
    
    opstat = opStatus()
    
    fparms      =   get_parms_for_input(parms,dftw.df_drop_dups_transform_input_idList)

    colnames    =   fparms[0]
    
    if(len(colnames) == 0) :
        colnames    =   None
        
    if(fparms[1] == "drop") :
        drop = True
    else :
        drop = False
        
    keep        =   fparms[2]
    if(keep == "False") :
        keep    =   False
        
    if(fparms[3] == "True") :
        inplace = True
    else :
        inplace = False
            
    if(not inplace) :
        if(len(fparms[3]) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("result df name is empty")
        else :
            resultdf    =   fparms[4]
            
    df = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
            
    if(not (colnames is None)) :
        if(not drop) :
            fcolnames   =   []  
            colslist    =   df.columns.tolist()
            
            for i in range(len(colslist)) :
                if(not (colslist[i] in colnames)) :
                    fcolnames.append(colslist[i]) 
                    
            colnames    =   fcolnames
                
    if(opstat.get_status()) :
        
        try : 
            
            if(inplace) :
                df.drop_duplicates(colnames,keep=keep,inplace=True)
            else :
                newdf               =   df.drop_duplicates(colnames,keep=keep,inplace=False)
                new_dfcnotes        =   "drop duplicates " + colnames
                new_dfc_dataframe   =   cfg.dfc_dataframe(resultdf,newdf,new_dfcnotes)
                cfg.add_dfc_dataframe(new_dfc_dataframe)
        
        except Exception as e: 
            opstat.store_exception("Unable to sort df index : " + colnames,e)

    return(opstat)
 

"""
#--------------------------------------------------------------------------
#    process the dataframe transform options
#--------------------------------------------------------------------------
"""
def process_df_transform(optionid,parms,display=True) :
    
    opstat  =   opStatus()
    
    funcid      =   parms[0][1]
    
    #PROCESS_CMD                 =   0
    #GET_DEFAULT_FILE_NAME       =   1
    
    dftw.display_dataframe_transform_taskbar()

    if(optionid == dtm.PROCESS_SAVE_COLUMN_NAMES_ROW) :
        
        # remove column names row
        #if(funcid == PROCESS_CMD) :
        fparms      =   get_parms_for_input(parms,dftw.df_save_row_transform_input_idList)
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
                               "from dfcleanser.data_transform.data_transform_dataframe_control save_column_names_row",
                               "save_column_names_row(" + str(filename) + ")"],opstat)
                
            clear_output()

            display_main_option([[0,0]])
            display_status("Column Names Row Saved Successfully to : " + filename)

            clear_dataframe_transform_cfg_values()
                
        else :
            clear_output()
            dftw.display_dataframe_options([[0,1]])
            display_exception(opstat)
        
        """        
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

                funcid = parms[0][0]

            dftw.display_dataframe_options([[dtm.SAVE_COLUMN_NAMES_ROW]])
        """
            
    # add column names row
    elif(optionid == dtm.PROCESS_ADD_COLUMN_NAMES_ROW) :
        
        # add column names row
        #if(funcid == PROCESS_CMD) :
            
        fparms      =   get_parms_for_input(parms,dftw.df_add_row_transform_input_idList)
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
                                   "from dfcleanser.data_transform.data_transform_dataframe_control add_column_names_row",
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
            
    
    elif(optionid == dtm.PROCESS_CHANGE_COLUMN_NAMES) :
        
        opstat = change_column_names(parms)
        
        if(opstat.get_status()) :
                 
            if(display) :
                #make scriptable
                add_to_script(["# change column names",
                               "from dfcleanser.data_transform.data_transform_dataframe_control change_column_names",
                               "change_column_names("+",False)"],opstat)
                
                clear_output()
                display_main_option([[0,0]])
                clear_dataframe_transform_cfg_values()
                print("\n")
                display_status("Column Names Changed Successfully")
                col_names_table = dcTable("Column Names ","cnamesTable",cfg.DataTransform_ID)
                col_names_table.set_note(" ")
                display_column_names(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),col_names_table,None)    
                
            else :
                
                clear_output()
                dftw.display_dataframe_options([[4,0]])
                display_exception(opstat)

    
    elif(optionid == dtm.PROCESS_SET_DF_INDEX) :
        
        #if(funcid == PROCESS_CMD) :
            
        opstat = set_df_index(parms)      
                
        if(opstat.get_status()) :
                    
            if(display) :
                #make scriptable
                add_to_script(["# set df index",
                               "from dfcleanser.data_transform.data_transform_dataframe_control set_df_index",
                               "set_df_index(" + json.dumps(parms[1]) + ")"],opstat)

            clear_output()
            display_main_option([[0,0]])
            clear_dataframe_transform_cfg_values()
            display_status("df Index Set Successfully")
                
        else :
                
            clear_output()
            dftw.display_dataframe_options([[3,0]]) 
            display_exception(opstat)
                
                
    elif(optionid == dtm.PROCESS_RESET_DF_INDEX) :
        
        # Remove Row Ids Column
        #if(funcid == PROCESS_CMD) :
            
        opstat = reset_df_index(parms)
            
        if(opstat.get_status()) :
                 
            if(display) :
                #make scriptable
                add_to_script(["# reset df index",
                               "from dfcleanser.data_transform.data_transform_dataframe_control reset_df_index",
                               "reset_df_index(" + json.dumps(parms[1]) + ")"],opstat)

            clear_output()
            display_main_option([[0,0]])
            clear_dataframe_transform_cfg_values()
            display_status("df Index Reset Successfully")
                
        else :
                
            clear_output()
            dftw.display_dataframe_options([[1,0]])
            display_exception(opstat)

            
    elif(optionid == dtm.PROCESS_APPEND_TO_INDEX) :
        
        # Remove Row Ids Column
        #if(funcid == PROCESS_CMD) :
            
        opstat = append_to_df_index(parms)
            
        if(opstat.get_status()) :
                 
            if(display) :
                #make scriptable
                add_to_script(["# append to df index",
                               "from dfcleanser.data_transform.data_transform_dataframe_control append_to_df_index",
                               "append_to_df_index(" + json.dumps(parms[1]) + ")"],opstat)
                
            clear_output()
            display_main_option([[0,0]])
            clear_dataframe_transform_cfg_values()
                
            display_status("Row Index Column Dropped Successfully")
                
        else :
                
            clear_output()
            dftw.display_dataframe_options([[4,0]])
            display_exception(opstat)
 
    
    elif(optionid == dtm.PROCESS_SORT_DF_INDEX) :
        
        # Remove Row Ids Column
        #if(funcid == PROCESS_CMD) :
            
        opstat = sort_df_index(parms)
            
        if(opstat.get_status()) :
                 
            if(display) :
                #make scriptable
                add_to_script(["# set row ids column",
                               "from dfcleanser.data_transform.data_transform_dataframe_control sort_df_index",
                               "sort_df_index(" + json.dumps(parms[1]) + ")"],opstat)
                
            clear_output()
            display_main_option([[0,0]])
            clear_dataframe_transform_cfg_values()
                
            display_status("Dataframe Sorted Successfully")
                
        else :
                
            clear_output()
            dftw.display_dataframe_options([[4,0]])
            display_exception(opstat)

            
    # drop duplicate rows
    elif(optionid == dtm.PROCESS_DROP_DUPLICATE_ROWS) :

        # drop duplicate rows
        #if(funcid == PROCESS_CMD) :
            
        opstat = drop_duplicate_rows(parms)
            
        if(opstat.get_status()) :
                 
            if(display) :
                #make scriptable
                add_to_script(["# drop duplicate rows",
                               "from dfcleanser.data_transform.data_transform_dataframe_control drop_duplicate_rows",
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
    elif(optionid == dtm.DF_TRANSFORM_RETURN) :
        
        dftw.display_dataframe_transform_main()
        
    # help
    elif(optionid == dtm.DF_TRANSFORM_HELP) :
        print("help")

def clear_dataframe_transform_cfg_values() :
    
    cfg.drop_config_value(dftw.df_save_row_transform_input_id+"Parms")
    cfg.drop_config_value(dftw.df_add_row_transform_input_id+"Parms")
    cfg.drop_config_value(dftw.df_reset_index_transform_input_id+"Parms")
    cfg.drop_config_value(dftw.df_drop_dups_transform_input_id+"Parms")
    cfg.drop_config_value(dftw.df_change_row_transform_input_id+"Parms")    
    cfg.drop_config_value(dftw.df_sort_index_transform_input_id+"Parms")
    cfg.drop_config_value(dftw.df_set_index_transform_input_id+"Parms")    
    
    
    
    
