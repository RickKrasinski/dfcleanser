"""
# data_transform_columns_control 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

import json 
import numpy as np
import pandas as pd

import dfcleanser.common.cfg as cfg 
import dfcleanser.data_transform.data_transform_columns_widgets as dtcw
import dfcleanser.data_transform.data_transform_model as dtm
import dfcleanser.data_transform.data_transform_widgets as dtw


from dfcleanser.common.common_utils import (get_parms_for_input, display_exception, display_status_note, 
                                            opStatus, RunningClock, is_existing_column, is_numeric_col,
                                            is_column_in_df, get_col_uniques, display_generic_grid,
                                            does_dir_exist, get_datatype_from_dtype_str, get_converted_value,
                                            get_dtype_str_for_datatype, convert_df_cols_datatype, is_string_col, 
                                            is_categorical_col)

from dfcleanser.common.display_utils import (display_column_names) 

from dfcleanser.common.table_widgets import (dcTable)       

from IPython.display import clear_output

from dfcleanser.scripting.data_scripting_control import add_to_script


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    Column transform components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def display_cnames() :
    
    df              =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
        
    col_names_table =   dcTable("Column Names ","cnamesTable",cfg.DataTransform_ID)
    col_names_table.set_note("None")
    col_names_html  =   display_column_names(df,col_names_table,None,False)
    
    gridclasses     =   ["main"]
    gridhtmls       =   [col_names_html]
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("df-reorder-colnames-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("df-reorder-colnames-pop-up-wrapper",gridclasses,gridhtmls)
        

"""
#--------------------------------------------------------------------------
#    process column transform option
#--------------------------------------------------------------------------
"""

def display_category_status(colname) :
    
    opstat  =   opStatus()
            
    df  =   cfg.get_current_chapter_df(cfg.DataTransform_ID)

    #display_df_unique_column(df,cat_uniques_table,colname,sethrefs=False,display=True)
    from dfcleanser.data_cleansing.data_cleansing_widgets import get_unique_col_html
    get_unique_col_html(df,colname,opstat,False)

    from dfcleanser.data_cleansing.data_cleansing_widgets import display_col_stats
    colstats_html       =   display_col_stats(df,colname,display=False,full_size=True)

    gridclasses     =   ["dfc-main"]
    gridhtmls       =   [colstats_html]
    
    if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
        display_generic_grid("dfc-common-480px-single-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("dfc-common-480px-single-wrapper",gridclasses,gridhtmls,True)
        
    
def process_column_option(optionid,parms) :
    """
    * -------------------------------------------------------------------------- 
    * function : process column transform option
    * 
    * parms :
    *   parms   -   associated parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    #dtcw.display_base_data_transform_columns_taskbar()
    
    opstat      =   opStatus()
    
    colname = cfg.get_config_value(cfg.DATA_TRANSFORM_COL_SELECTED_KEY)
        
    if(optionid == dtm.PROCESS_RENAME_COLUMN) :
        
        opstat  =   process_rename_column(parms)
        
        dtcw.display_base_data_transform_columns_taskbar()
        print("\n")
        
        if(opstat.get_status()) :
            display_status_note(opstat.get_errorMsg())
            print("\n")
            display_cnames()
        else :
            display_exception(opstat)
        
    elif(optionid == dtm.PROCESS_DROP_COLUMN) :
        
        opstat  =   process_drop_column(parms)
        
        dtcw.display_base_data_transform_columns_taskbar()
        print("\n")
        
        if(opstat.get_status()) :
            display_status_note(opstat.get_errorMsg())
        else :
            display_exception(opstat)
        
    elif(optionid == dtm.PROCESS_REORDER_COLUMNS) :
        
        opstat  =   process_reorder_columns(parms)
        
        dtcw.display_base_data_transform_columns_taskbar()
        print("\n")
        
        if(opstat.get_status()) :
            display_status_note(opstat.get_errorMsg())
            print("\n")
            display_cnames()
        else :
            display_exception(opstat)

    elif(optionid == dtm.PROCESS_SAVE_COLUMN) :
         
        opstat  =   process_save_column(parms)
            
        dtcw.display_base_data_transform_columns_taskbar()
        
        if(opstat.get_status()) :
            display_status_note(opstat.get_errorMsg())
        else :
            display_exception(opstat)
    
    elif(optionid == dtm.PROCESS_SAVE_COLUMN_WITH_INDEX) :
         
        opstat  =   process_save_column(parms,withIndex=True)
        
        dtcw.display_base_data_transform_columns_taskbar()
        
        if(opstat.get_status()) :
            display_status_note(opstat.get_errorMsg())
        else :
            display_exception(opstat)
        
    elif(optionid == dtm.PROCESS_COPY_COLUMN) :
        
        opstat  =   process_copy_column(parms)
        
        dtcw.display_base_data_transform_columns_taskbar()
        print("\n")
        
        if(opstat.get_status()) :
            display_status_note(opstat.get_errorMsg())
        else :
            display_exception(opstat)
        
    elif(optionid == dtm.PROCESS_MAP_COLUMN) :
        
        opstat  =   process_map_transform(dtm.MAP_FROM_FILE,parms)
        
        dtcw.display_base_data_transform_columns_taskbar()
        print("\n")
        
        if(opstat.get_status()) :
            display_status_note(opstat.get_errorMsg())
        else :
            display_exception(opstat)
        
    elif(optionid == dtm.PROCESS_MAP_COLUMN_VALUES) :
        
        opstat  =   process_map_transform(dtm.MAP_FROM_VALUES,parms)
        
        dtcw.display_base_data_transform_columns_taskbar()
        print("\n")
        
        if(opstat.get_status()) :
            display_status_note(opstat.get_errorMsg())
        else :
            display_exception(opstat)
        
    elif(optionid == dtm.PROCESS_MAP_COLUMN_FUNCTION) :
        
        opstat  =   process_map_transform(dtm.MAP_FROM_FUNCTION,colname,parms)
        
        dtcw.display_base_data_transform_columns_taskbar()
        print("\n")
        
        if(opstat.get_status()) :
            display_status_note(opstat.get_errorMsg())
        else :
            display_exception(opstat)
        
    elif(optionid == dtm.PROCESS_DUMMIES_COLUMN) :
        
        opstat  =   process_dummy_transform(parms)
        
        dtcw.display_base_data_transform_columns_taskbar()
        print("\n")
        
        if(opstat.get_status()) :
            display_status_note(opstat.get_errorMsg())
            print("\n")
            display_cnames()
        else :
            display_exception(opstat)
        
    elif( (optionid == dtm.PROCESS_CAT_COLUMN) or 
          (optionid == dtm.PROCESS_CAT_COLUMN_EXCLUDE) ) :
        
        opstat  =   process_cat_transform(parms)
        
        dtcw.display_base_data_transform_columns_taskbar()
        
        if(opstat.get_status()) :
            display_status_note(opstat.get_errorMsg())
            display_category_status(parms[1][0])
        else :
            display_exception(opstat)
    
    elif(optionid == dtm.PROCESS_CHANGE_DATATYPE_COLUMNS) :
        
        opstat  =   process_datatype_column(parms)
        
        dtcw.display_base_data_transform_columns_taskbar()
        print("\n")
        
        if(opstat.get_status()) :
            display_status_note(opstat.get_errorMsg())
        else :
            display_exception(opstat)
        
    elif(optionid == dtm.PROCESS_APPLY_COLUMN) :
        
        opstat  =   process_apply_fn_to_column(parms)
        
        dtcw.display_base_data_transform_columns_taskbar()
        print("\n")
        
        if(opstat.get_status()) :
            display_status_note(opstat.get_errorMsg())
        else :
            display_exception(opstat)

    elif( (optionid == dtm.PROCESS_ADD_FROM_FILE_OPTION) or 
          (optionid == dtm.PROCESS_ADD_FROM_CODE_OPTION) or
          (optionid == dtm.PROCESS_ADD_FROM_DFC_FUNCS) or 
          (optionid == dtm.PROCESS_ADD_FROM_DF_OPTION) or 
          (optionid == dtm.PROCESS_ADD_FROM_FILE_WITH_INDEX_OPTION) ) :

        opstat  =   process_add_column(optionid,parms)
        
        print("\n")
        
        if(opstat.get_status()) :
            display_status_note(opstat.get_errorMsg())
        else :
            display_exception(opstat)

    elif(optionid == dtm.PROCESS_SAVE_USER_FUNC) :
        
        opstat  =   process_save_user_fn(parms)
        
        dtcw.display_base_data_transform_columns_taskbar()
        print("\n")
        
        if(opstat.get_status()) :
            display_status_note(opstat.get_errorMsg())
            dtcw.display_add_cols_option(dtm.DISPLAY_ADD_FROM_CODE_OPTION,parms,False)
        else :
            display_exception(opstat)

    elif(optionid == dtm.PROCESS_DELETE_USER_FUNC) :
        
        opstat  =   process_delete_user_fn(parms)
        
        dtcw.display_base_data_transform_columns_taskbar()
        print("\n")
        
        if(opstat.get_status()) :
            display_status_note(opstat.get_errorMsg())
            dtcw.display_add_cols_option(dtm.DISPLAY_MAINTAIN_USER_FUNC,None,False)
        else :
            display_exception(opstat)

        
def process_rename_column(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : rename column transform option
    * 
    * parms :
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat = opStatus()
        
    df  =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
    
    fparms = get_parms_for_input(parms,dtcw.rename_column_input_idList)
    
    newname     =   fparms[0]
    
    if(len(newname) < 1) :
        opstat.set_status(False)
        opstat.set_errorMsg("new_column_name is invalid")
        
    else :
        
        colname     =   fparms[1]
        if(not (is_column_in_df(df,colname))) :
            opstat.set_status(False)
            opstat.set_errorMsg("column_name is not in df")
            
    if(opstat.get_status()) :
        
        namesdict = {}
        namesdict.update({colname:newname})
    
        try :
        
            df.rename(columns=namesdict,inplace=True)
                
            if(display) :
                
                #make scriptable
                add_to_script(["# Rename column " + colname + " to " + newname,
                               "from dfcleanser.data_transform.data_transform_columns_control import process_rename_column",
                               "process_rename_column(" + json.dumps(parms) + ",False)"],opstat)
    
            opstat.set_errorMsg("Column '" + colname + "' renamed to '" + newname + "' successfully")
        
        except Exception as e:
            opstat.store_exception("Rename Column " + colname + " : Error",e)
    
    return(opstat)  


def save_deleted_column(colname,dftitle,fdir,ftype,fname=None) :
    """
    * -------------------------------------------------------------------------- 
    * function : save column being deleted to a file
    * 
    * parms :
    *   colname   -   column name
    *   fname     -   filename
    *   df        -   dataframe
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    import os
    
    opstat = opStatus()
    
    df  =   cfg.get_dfc_dataframe_df(dftitle)
    
    if(fname == None) :
        save_file_path  =   os.path.join(fdir,dftitle + "_" + colname + "." + ftype)
    else :
        fname   =   fname.lstrip("'")
        fname   =   fname.rstrip("'")
        save_file_path  =   os.path.join(fdir,fname + "." + ftype)
        
    save_file_path  =   save_file_path.replace(" ","_")
    
    try :
        
        collist = df[colname].tolist()
        
        if(ftype == "json") :
            with open(save_file_path, 'w') as col_list_file :
                json.dump(collist,col_list_file)
                
        else :
            
            newdf   =   pd.DataFrame(collist,columns=[colname])
            newdf.to_csv(save_file_path)

                    
    except Exception as e:
        opstat.store_exception("Unable to save column " + colname,e)

    return(opstat)
 

def process_drop_column(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : drop column transform option
    * 
    * parms :
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat = opStatus()
        
    df  =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
    
    fparms = get_parms_for_input(parms,dtcw.drop_column_input_idList)
    
    colnames    =   fparms[0]
    colnames    =   colnames.split(",")
    
    for i in range(len(colnames)) :
    
        if(not (is_column_in_df(df,colnames[i]))) :
            opstat.set_status(False)
            opstat.set_errorMsg("column_name is not in df")
            break;
            
    if(opstat.get_status()) :
        
        saveCols    =   fparms[1]
        if(saveCols == "True") :
            saveCols    =   True
        else :
            saveCols    =   False
            
        if(saveCols) :
            
            save_file_names     =   fparms[2]
            save_file_names     =   save_file_names.split(",")
            
            if(not(len(colnames) == len(save_file_names))) :
                opstat.set_status(False)
                opstat.set_errorMsg("Invalid file save names")
            
            if(opstat.get_status()) :
                
                fdir                =   fparms[3]
    
                if(len(fdir) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("col(s)_to_drop_save_file(s)_dir '" + fdir + "' not a valid dir")
                else :
                    if(not (does_dir_exist(fdir))) :
                        opstat.set_status(False)
                        opstat.set_errorMsg("col(s)_to_drop_save_file(s)_dir '" + fdir + "' not a valid dir")
                        
                if(opstat.get_status()) :
                    
                    ftype   =  fparms[4] 

    if(opstat.get_status()) :
        
        if(saveCols) :
        
            if(not (fdir is None))  :
                for i in range(len(colnames)) :
                    opstat = save_deleted_column(colnames[i],cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF),fdir,ftype)
                    if(not(opstat.get_status())) :
                        break
        
        if(opstat.get_status()) :
        
            try :
                
                for i in range(len(colnames)) :
                    
                    df.drop([colnames[i]],inplace=True,axis=1)
                    
                if(display) :
            
                    #make scriptable
                    add_to_script(["# drop columns " + str(colnames),
                                   "from dfcleanser.data_transform.data_transform_columns_control import process_drop_column",
                                   "process_drop_column(" + json.dumps(parms) + ",False)"],opstat)
    
                opstat.set_errorMsg("Columns '" + str(colnames) + "' dropped Successfully")
                    
            
            except Exception as e:
                opstat.store_exception("Drop Columns Error",e)

    return(opstat)


def process_reorder_columns(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : reorder column transform option
    * 
    * parms :
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat  =    opStatus()
    
    df          =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
    df_cols     =   df.columns.tolist() 
    
    fparms  =    get_parms_for_input(parms,dtcw.reorder_columns_input_idList)

    movecol         = fparms[0]
    if(not (is_column_in_df(df,movecol))) :
        opstat.set_status(False)
        opstat.set_errorMsg("column_to_move is not in df")
    else :
        
        moveaftercol    = fparms[2]
        if(not (is_column_in_df(df,moveaftercol))) :
            opstat.set_status(False)
            opstat.set_errorMsg("column_to_move_after is not in df")
    
    if(opstat.get_status())  :
        
        new_cols = []
    
        # drop the move column from list
        for i in range(len(df_cols)) :
            if(not (df_cols[i] == movecol)) :
                new_cols.append(df_cols[i])
            
        final_cols = []
        for i in range(len(new_cols)) :
            final_cols.append(new_cols[i])
            if(new_cols[i] == moveaftercol) :
                final_cols.append(movecol) 
    
        try : 
            
            df  =   df[final_cols]  

            cfg.set_dfc_dataframe_df(cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF),df) 
            
            df  =   cfg.get_dfc_dataframe_df(cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF))

            if(display) :
            
                #make scriptable
                add_to_script(["# reorder columns ",
                               "from dfcleanser.data_transform.data_transform_columns_control import process_reorder_columns",
                               "process_reorder_columns(" + json.dumps(parms) + ",False)"],opstat)
    
            opstat.set_errorMsg("Column '" + movecol + "' moved after '" + moveaftercol + "'Successfully")
            
        except Exception as e:
            opstat.store_exception("Reorder Columns Error",e)

    return(opstat)


def process_save_column(parms,withIndex=False,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : save column transform option
    * 
    * parms :
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat = opStatus()
    
    df  =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
    
    if(not (withIndex)) :
        fparms = get_parms_for_input(parms,dtcw.save_column_input_idList)
    else :
        fparms = get_parms_for_input(parms,dtcw.save_colind_input_idList)
    
    if(len(fparms) > 0) :

        colnames    =   fparms[0]
        colnames    =   colnames.lstrip("[")
        colnames    =   colnames.rstrip("]")
        colnames    =   colnames.split(",")
    
        for i in range(len(colnames)) :
    
            if(not (is_column_in_df(df,colnames[i]))) :
                opstat.set_status(False)
                opstat.set_errorMsg("column_name " + colnames[i] + " is not in df")
                break;
            
        if(opstat.get_status()) :
            
            fname   =   fparms[2]
            
            if(len(fname) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("file name is not defined")
            
            else :
                
                ftype   =  fparms[3] 
                
                if(opstat.get_status()) :
                
                    if(withIndex) :
                    
                        withindexflag   =   fparms[4]
                    
                        if(withindexflag == "True") :
                            withindexflag   =   True
                        else :
                            withindexflag   =   False
                        
                    else :
                        withindexflag   =   False
        
    else :
        opstat.set_status(False)
        opstat.set_errorMsg("no parameters defined for save")
    
    if(opstat.get_status())  :
    
        try :
            
            if(not (withindexflag)) :
                save_index  =   False
            else :
                save_index  =   True
                
            try :
                    
                if(ftype == "json") :
                    
                    cols            =   list(df.columns)
                    cols_to_drop    =   []
                    
                    for i in range(len(cols)) :
                        if(not (cols[i] in colnames) ) :
                            cols_to_drop.append(cols[i])
                            
                    temp_df     =   df.drop(cols_to_drop,axis=1)
                    
                    temp_df.to_json(fname)
                    
                elif(ftype == "excel") :
                    
                    df.to_excel(fname,columns=colnames,header=True,index=save_index)
                    
                else :
                    
                    df.to_csv(fname,columns=colnames,header=True,index=save_index)
                        
            except Exception as e:
                opstat.store_exception("Unable to save column(s) ",e)
                
            if(opstat.get_status()) :
                
                if(display) :
            
                    #make scriptable
                    add_to_script(["# save columns " + str(colnames),
                                   "from dfcleanser.data_transform.data_transform_columns_control import process_save_column",
                                   "process_save_column(" + json.dumps(parms) + ",False)"],opstat)
                        
            opstat.set_errorMsg("Columns " + str(colnames) + " saved Successfully")
            
            if(not (withindexflag)) :
                cfg.set_config_value(dtw.save_column_input_id+"Parms",["","",fname,""])
            else :
                cfg.set_config_value(dtw.save_colind_input_id+"Parms",["","",fname,"",""])
                    
        except Exception as e:
            opstat.store_exception("Unable to save column ",e)
    
    return(opstat)

    
def process_copy_column(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : copy column transform option
    * 
    * parms :
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
 
    opstat  =   opStatus()
    
    fparms  =   get_parms_for_input(parms,dtcw.copy_columns_input_idList)
    
    copyfromcol     =   fparms[0]
    copytocol       =   fparms[1]
    newcol          =   fparms[2]
        
    df = cfg.get_current_chapter_df(cfg.DataTransform_ID)
    
    if(len(newcol) > 0) :
        if(is_column_in_df(df,newcol)) :
            opstat.set_status(False) 
            opstat.set_errorMsg("new column name is already in df")
            
    else :
        if(copyfromcol == copytocol) :
            opstat.set_status(False) 
            opstat.set_errorMsg("copy to column name is same as copy from column name")
        
    if(opstat.get_status()) :
    
        try : 
        
            if(len(newcol) > 0) :
                df[copytocol] = df[copyfromcol]
            else :
                add_column_to_df(df,newcol,df[copyfromcol].tolist(),opstat,display) 
                
            cfg.set_dfc_dataframe_df(cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF),df) 
            
            if(display) :
            
                #make scriptable
                add_to_script(["# copy column ",
                               "from dfcleanser.data_transform.data_transform_columns_control_widgets import process_copy_column",
                               "process_copy_column(" + json.dumps(parms) + ",False)"],opstat)
        
            opstat.set_errorMsg("Column '" + copyfromcol + "' copied to '" + copytocol + "' Successfully")
        
        except Exception as e:
            opstat.store_exception("Copy Column Error",e)
        
        
    return(opstat)

"""
#--------------------------------------------------------------------------
#    Mapping, Dummies and Category helper functions
#--------------------------------------------------------------------------
"""


def make_col_categorical(df, columnName, reverse=None)  :   
    """
    * -------------------------------------------------------------------------- 
    * function : make a column ordinal in place using categories
    * 
    * parms :
    *   df              -   dataframe
    *   columnName      -   column name
    *   reverse         -   reverse the order of the values befor categorize
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """ 

    opstat = opStatus()

    ccats = get_col_uniques(df, columnName)
    
    nanfound = -1

    for i in range(len(ccats)) :

        if(type(ccats[i]) == float) :       
            if(np.isnan(ccats[i])) :
                nanfound = i

    if(nanfound == -1) :
        
        try :
            if (reverse == None) :
                ccats.sort()
            else :
                ccats.sort(reverse=True)
    
            df[columnName] = df[columnName].astype("category",
              categories=ccats
              ).cat.codes
          
        except Exception as e:
            opstat.store_exception("[Categories error] for Column " + columnName,e)
            
    else : 
        opstat.set_status(False)
        opstat.set_errorMsg("[Categories error] for Column " + columnName + " : NaN found in column")
        

    return(opstat)
    

def make_col_categorical_from_dummies(df, columnName, removeCol)  : 
    """
    * -------------------------------------------------------------------------- 
    * function : make a column categorical in place using dummies
    * 
    * parms :
    *   df              -   dataframe
    *   columnName      -   column name
    *   removeCol       -   remove the original column
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """ 
    
    opstat = opStatus()
    
    y = df[[columnName]]
    
    try :
        caty = pd.get_dummies(y)
        df = pd.concat([df, caty], axis=1)
    except Exception as e:
        opstat.store_exception("column concat error : " + columnName,e)
    
    if( (removeCol) and (opstat.get_status()) ): 
        try :
            df.drop(columnName, axis = 1, inplace = True) 
        except Exception as e: 
            opstat.store_exception("column drop error : " + columnName,e)
            
    return(opstat)


def make_col_categorical_from_map(df, columnName, cmap, handleNA)  :   
    """
    * -------------------------------------------------------------------------- 
    * function : make a column categorical in place using map
    * 
    * parms :
    *   df              -   dataframe
    *   columnName      -   column name
    *   cmpa            -   column value map
    *                       ( {'Man': 0, 'Woman': 1} )
    *
    *   handleNA        -   how to handle nas
    *                       'ignore' - ignore errors
    *                       None     - no handling at all 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """ 

    collist = df[columnName]
    
    opstat = opStatus()
    
    if( (handleNA == None) or (handleNA == 'ignore') ) : 
        try :
            df[columnName] = collist.map(cmap,handleNA)
        except Exception as e: 
            opstat.store_exception("column mapping error : " + columnName,e)
            
    else:
        opstat.set_status(False)
        opstat.set_errorMsg("handlena value not supported : " + columnName)

    return(opstat)


def process_map_transform(mtype,parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : mapping transform
    * 
    * parms :
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """ 
    
    opstat  =   opStatus()
        
    df      =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
    
    fparms  =   get_parms_for_input(parms,dtcw.transform_map_input_idList)

    map_colname     =   fparms[0]
    map_keys        =   fparms[1]
    map_values      =   fparms[2]
    map_fn          =   fparms[3]
    map_file_name   =   fparms[4]
    map_vals_dtype  =   fparms[5]
    handle_nan      =   fparms[6]
    

    if(mtype == dtm.MAP_FROM_VALUES) :
        
        mapkeys = map_keys.split(',')
        mapvals = map_values.split(',')
        
        if(not (len(mapkeys) == len(mapvals)) ) :
            opstat.set_status(False)
            opstat.set_errorMsg("Number of 'mapping_keys' does not match number of 'mapping_values'")
            
    if(mtype == dtm.MAP_FROM_FILE) :
        
        mapkeys = df[map_colname].unique().tolist()
        mapkeys.sort()
            
        if(len(map_file_name) > 0) : 
            
            try :
                
                with open(map_file_name, 'r') as map_file :
                    mapvals = json.loads(map_file)
                map_file.close()
                
                if(not (len(mapkeys) == len(mapvals)) ) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("Number of 'mapping_keys' does not match number of 'mapping_values'")
                
            except Exception as e:
                opstat.store_exception("Error opening mapping_values_file : " + map_file_name,e)
                
        else :
            opstat.set_status(False)
            opstat.set_errorMsg("Invalid mapping_values_list_file_name")
            
    if(mtype == dtm.MAP_FROM_FUNCTION) :
        
        if(len(map_fn) < 1) :
            
            opstat.set_status(False)
            opstat.set_errorMsg("Invalid mapping_values_function")
        
        else :
            
            if(map_fn.find("mapvals") < 0) :
                
                opstat.set_status(False)
                opstat.set_errorMsg("mapping_values_function does not return mapvals object")
            
            else :
            
                mapkeys     =    df[map_colname].unique().tolist()
                mapkeys.sort()
                mapvals     =   []
        
                try :
                    exec(map_fn) 
                except Exception as e:
                    opstat.store_exception("Error running mapping_values_function : ",e)
                
                if(not (len(mapkeys) == len(mapvals)) ) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("Number of 'mapping_keys' does not match number of 'mapping_values'")
            
    if(opstat.get_status()) :
    
        mapDict         =   {}
        
        coldtype        =   df[map_colname].dtype
        coldtype_str    =   get_dtype_str_for_datatype(coldtype) 
        
        for i in range(len(mapkeys)) :
            
            map_key     =   get_converted_value(coldtype_str,mapkeys[i],opstat)
            map_value   =   get_converted_value(map_vals_dtype,mapvals[i],opstat)
            
            if(opstat.get_status()) :
                mapDict.update({map_key:map_value})
            else :
                break;
            
    if(opstat.get_status()) : 
        
        if(handle_nan == "True") :
            nanFlag     =   True
        else :
            nanFlag     =   False
        
        handlenan = False
        if(nanFlag  == "True") :
            handlenan = None
        else :
            handlenan = 'ignore'
    
        opstat = make_col_categorical_from_map(cfg.get_current_chapter_df(cfg.DataTransform_ID), 
                                               map_colname, mapDict, handlenan)
        
        if(opstat.get_status()) :
            
            opstat.set_errorMsg("Column " + map_colname + " mapped successfully")
            
            if(display) :
                #make scriptable
                add_to_script(["# Make col map for " + map_colname,
                               "from dfcleanser.data_transform.data_transform_columns_control import process_map_transform",
                               "process_map_transform(" + json.dumps(parms) + ",False)"],opstat)
            
    return(opstat)


def process_dummy_transform(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : dummies transform
    * 
    * parms :
    *   colname -   associated parms
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """ 
    
    opstat  =   opStatus()
    df      =   cfg.get_current_chapter_df(cfg.DataTransform_ID)

    fparms  =   get_parms_for_input(parms,dtcw.transform_dummy_input_idList)
    
    colname     =   fparms[0]
    removecol   =   fparms[1]
    
    opstat = make_col_categorical_from_dummies(cfg.get_current_chapter_df(cfg.DataTransform_ID),
                                               colname, removecol) 

    if(opstat.get_status()) :
        
        if(display) :
            #make scriptable
            add_to_script(["# Make dummies for " + colname,
                           "from dfcleanser.data_transform.data_transform_column_control import process_dummy_transform",
                           "process_dummy_transform(" + json.dumps(parms)  + ",False)"],opstat)
        
        opstat.set_errorMsg("Column [" + colname + "] dummies created successfully")
        
        if(removecol == "True") :
            
            df.drop([colname],inplace=True,axis=1)            
            cfg.drop_config_value(cfg.CLEANSING_COL_KEY)
            

    return(opstat)


def process_cat_transform(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : categorical transform
    * 
    * parms :
    *   colname -   associated parms
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """ 
    
    opstat          =   opStatus()
    df              =   cfg.get_current_chapter_df(cfg.DataTransform_ID)

    if("catcolumncompleteuniques" in parms[0]) :
        
        fparms          =   get_parms_for_input(parms,dtcw.transform_category_input_idList)
    
        colname         =   fparms[0]
        orderflag       =   fparms[1]
        alluniques      =   fparms[2]
        
    else :
        
        fparms          =   get_parms_for_input(parms,dtcw.transform_cat_exclude_input_idList)
        
        colname         =   fparms[0]
        orderflag       =   fparms[1]
        excludeuniques  =   fparms[2]
        
        alluniques      =   "False"
        
    if(is_categorical_col(df,colname)) :
        opstat.set_status(False)
        opstat.set_errorMsg("column " + colname + " is already a categorical column")
        
    if(opstat.get_status()) :
    
        if(orderflag == "True") :
            orderflag     =   True
        else :
            orderflag     =   False
    
        if(alluniques == "True") :
            alluniques     =   True
        else :
            alluniques     =   False
            
        coluniques  =   df[colname].unique().tolist()
        colcats     =   []

        if(not (alluniques)) :
            
            excludeuniques  =   excludeuniques.lstrip("[")            
            excludeuniques  =   excludeuniques.rstrip("]") 
            
            if(excludeuniques.find(",") > -1) :
                excludeuniques  =   excludeuniques.split(",")
            else :
                excludeuniques  =   [excludeuniques]

        if(not(is_string_col(df,colname))) :
            for i in range(len(coluniques)) :
                if(not(coluniques[i].isnull())) :
                    if(alluniques) :
                        colcats.append(coluniques[i])
                    else :
                        if(not (coluniques[i] in excludeuniques)) :
                            colcats.append(coluniques[i])    
                        
        else :
            for i in range(len(coluniques)) :
                if(type(coluniques[i]) == str) :
                    if(alluniques) :
                        colcats.append(coluniques[i])
                    else :
                        if(not (coluniques[i] in excludeuniques)) :
                            colcats.append(coluniques[i])    

        try :
            
            cattype     =   pd.CategoricalDtype(categories = colcats,ordered=orderflag)
            df[colname] =   df[colname].astype(cattype)
            cfg.set_dfc_dataframe_df(cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF),df)
                    
        except Exception as e:
            opstat.store_exception("column category error : " + colname,e)
        
    
    if(opstat.get_status()) :
        
        opstat.set_errorMsg("Column [" + colname + "] set to category successfully")
            
        #make scriptable
        add_to_script(["# Make categories for " + colname,
                       "from dfcleanser.data_transform.data_transform_columns_control import process_cat_transform",
                       "process_cat_transform(" + json.dumps(parms) + ",False)"],opstat)
            
    return(opstat)


def process_datatype_column(parms,display=True)  :
    """
    * -------------------------------------------------------------------------- 
    * function : change column datatype
    * 
    * parms :
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """ 

    opstat      =   opStatus()
    
    df          =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
    
    naoption    =   parms[0]
    
    colname         =   None
    datatype        =   None
    
    nafillvalue     =   None
    nafillmethod    =   None    
    nafilllimit     =   None 
    
    nadropanyall    =   "any" 
    nadropthreshold =   None    
            
    if(naoption     ==  dtm.DROP_NA_OPTION) :
        fparms  =   get_parms_for_input(parms[1],dtcw.dt_drop_nans_data_type_input_idList)
        
        colname         =   fparms[0]
        datatype        =   fparms[1]
        nadropanyall    =   fparms[3]
        
        if(len(nadropanyall) == 0) :
            nadropanyall   =   "any" 

        nadropthreshold =   fparms[4]
                    
        if(len(nadropthreshold) > 0) :
                
            try :
                nadropthreshold     =   int(nadropthreshold)    
            except :
                opstat.set_status(False)
                opstat.set_errorMsg("invalid drop threshold value")
                    
        else :
            nadropthreshold     =   None    

        
    elif(naoption     ==  dtm.FILL_NA_OPTION) :
        fparms  =   get_parms_for_input(parms[1],dtcw.dt_nans_data_type_input_idList)
        
        colname         =   fparms[0]
        datatype        =   fparms[1]
        nafillvalue     =   fparms[3]
        
        nafillvalue    =   get_converted_value(datatype,nafillvalue,opstat)
            
        if(opstat.get_status()) :

            nafillmethod    =   fparms[4]
            
            if(len(nafillmethod) > 0) :

                if(nafillmethod == "mean") :
                    if(is_numeric_col(df,colname)) :
                        nafillvalue     =   df[colname].mean() 
                    else :
                        opstat.set_status(False)
                        opstat.set_errorMsg("can not define a mean value for a non numeric column")
                        nafillvalue     =   None
            else :
                nafillmethod     =   None    
            
            if(opstat.get_status()) :
            
                nafilllimit     =   fparms[5]
        
                if(len(nafilllimit) > 0) :
                
                    try :
                        nafilllimit     =   int(nafilllimit)    
                    except :
                        opstat.set_status(False)
                        opstat.set_errorMsg("invalid fillna limit value")
                    
                else :
                    nafilllimit     =   None     
        
    else :
        
        fparms  =   get_parms_for_input(parms[1],dtcw.dt_data_type_input_idList)
        
        colname         =   fparms[0]
        datatype        =   fparms[1]
    
    if(opstat.get_status()) :   
        
        if(naoption     ==  dtm.FILL_NA_OPTION) :
        
            try :
                if(nafillvalue is None) :
                    df[colname].fillna(method=nafillmethod,inplace=True,limit=nafilllimit) 
                else :
                    df[colname].fillna(nafillvalue,inplace=True,limit=nafilllimit) 
                    
            except Exception as e:
                
                if(not (nafillmethod is None) ) :
                    opstat.store_exception("fillna failure for column " + colname + " : method = " + nafillmethod + " : value = " + str(nafillvalue),e)
                else :
                    opstat.store_exception("fillna failure for column " + colname + " : value = " + str(nafillvalue),e)
                    
        elif(naoption     ==  dtm.DROP_NA_OPTION) :
            
            try :
                if(nadropthreshold is None) :
                    df[colname].dropna(how=nadropanyall,inplace=True) 
                else :
                    df[colname].dropna(thresh=nadropthreshold,inplace=True) 
            except Exception as e:
                opstat.store_exception("dropna failure for column " + colname,e)
                
    if(opstat.get_status()) : 
        
        try :
            df[colname] = df[colname].astype(get_datatype_from_dtype_str(datatype),copy=False)
        except Exception as e:
            opstat.store_exception("Error changing datatype for column " + colname + " to " + datatype,e)
    
    if(opstat.get_status()) :
        
        #make scriptable
        add_to_script(["# change column datatype for " + colname,
                       "from dfcleanser.data_transform.data_transform_columns_control import process_datatype_column",
                       "process_datatype_column(" + json.dumps(parms) + ",False)"],opstat)

        if(display) :
            opstat.set_errorMsg("Column '" + colname + "' datatype changed successfully to " + datatype)
            
    return(opstat)


def process_apply_fn_to_column(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : apply fn to column transform option
    * 
    * parms :
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat  =   opStatus()
    
    if(display) :
        clock = RunningClock()
        clock.start()
    
    apply_id_list   =   dtcw.get_current_apply_fn_idList()
    
    fparms = get_parms_for_input(parms,apply_id_list)

    dftoapply       =   fparms[0]
    coltoapply      =   fparms[1]
    fntoapply       =   fparms[2]
    fncode          =   fparms[3]
    
    from dfcleanser.sw_utilities.sw_utility_genfunc_model import get_apply_function_parms
    kwargs  =   get_apply_function_parms(fntoapply)
    
    kwargs_vals     =   []
    for i in range(len(kwargs)) :
        kwargs_vals.append(fparms[4+i]) 
        
    if(len(dftoapply) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No dataframe to aply fn to defined")
    
    elif(cfg.get_dfc_dataframe(dftoapply) is None) :
        opstat.set_status(False)
        opstat.set_errorMsg("Dataframe to aply fn to is invalid")
    
    elif(len(coltoapply) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No column to aply fn to defined")
    
    else :
        
        from dfcleanser.common.common_utils import is_column_in_df
        if(not (is_column_in_df(cfg.get_dfc_dataframe_df(dftoapply),coltoapply)) ) :
            opstat.set_status(False)
            opstat.set_errorMsg("Column " + coltoapply + " not found in " + dftoapply)
        elif(len(fncode) > 0) :
            
            for i in range(len(kwargs_vals)) :
                if(len(kwargs_vals[i]) == 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg(kwargs[i] + " fn parm is not defined")
    
    # good input parms        
    if(opstat.get_status()) :
    
        try : 
            
            code    =   ""
            code    =   (code + "import dfcleanser.common.cfg as cfg\n")
            fncode  =   fncode.replace("df","cfg.get_dfc_dataframe_df('" + dftoapply +"')")
            
            if(len(fntoapply) > 0) :
                
                if(fncode.find("np.") > -1) :
                    code    =   (code + "import numpy as np\n")
            
                from dfcleanser.sw_utilities.sw_utility_genfunc_model import get_apply_function_parms_datatypes
                kwarg_types     =   get_apply_function_parms_datatypes(fntoapply)
            
                for i in range(len(kwarg_types)) :
                    try :
                        if(kwarg_types[i] == int) :
                            kwargval    =   int(kwargs_vals[i])
                        elif(kwarg_types[i] == float) :
                            kwargval    =   float(kwargs_vals[i])
                        else :
                            kwargval    =   str("'"+kwargs_vals[i]+"'")
                        
                    except :
                        opstat.set_status(False)
                        opstat.set_errorMsg(kwargs[i] + " is invalid data_type")
                    
                    fncode  =   fncode.replace(kwargs[i],kwargval)
                    
            
            code    =   (code + fncode) 
            
            exec(code)
            
        except Exception as e:
            opstat.store_exception("Apply fn to Column Error : " + coltoapply + "\n   " + code,e)
    
    if(opstat.get_status()) :
        
        opstat.set_errorMsg("function applied successfully to column " + coltoapply)
        
        if(display) :
            
            #make scriptable
            add_to_script(["# apply fn to column ",
                           "from dfcleanser.data_transform.data_transform_columns_control import process_apply_fn_to_column",
                           "process_apply_fn_to_column(" + json.dumps(parms) + ",False)"],opstat)
            
            clear_output()
            dtcw.display_base_data_transform_columns_taskbar()
            display_status_note("function applied to column " + coltoapply + " successfully.")
            
    
    #et_dc_dataframe()[coltoapply].apply(fncode)
    cfg.drop_config_value(dtcw.apply_column_input_id+"Parms")
    
    if(display) :
        clock.stop()  
    
    return(opstat)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    ADD COLUMN transform methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def process_save_user_fn(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : save user func
    * 
    * parms :
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """ 
    
    opstat          =   opStatus()
    
    if("userfntitle" in parms[0]) :
        fparms          =   get_parms_for_input(parms,dtcw.maintain_user_fns_input_idList)
        
        newfmodule          =   fparms[2]
        newftitle           =   fparms[1]
        newfcode            =   fparms[3]
        
    else :
    
        fparms          =   get_parms_for_input(parms,dtcw.add_column_code_user_fns_input_idList)
            
        newfmodule          =   fparms[4]
        newftitle           =   fparms[5]
        newfcode            =   fparms[6]
        
    if(len(newfmodule) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("'function_module' is not defined")
    else :
        if(len(newftitle) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("'function_name' is not defined")
        else :
            if(len(newfcode) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("'function_code' is not defined")
                
    if(opstat.get_status()) :
        
        from dfcleanser.sw_utilities.sw_utility_genfunc_model import add_generic_user_function
        
        try :
            add_generic_user_function(newftitle,newfmodule,newfcode)
            opstat.set_errorMsg("User fn [" + newftitle + "] saved sucessfully")
        except Exception as e:
            opstat.store_exception("Unable to save user function " + newftitle,e)
    
    if(opstat.get_status()) :
        
        #make scriptable
        add_to_script(["# Save user fn " + newftitle,
                       "from dfcleanser.data_transform.data_transform_columns_control import process_save_user_fn",
                       "process_save_user_fn(" + json.dumps(parms) + ",False)"],opstat)
            
    return(opstat)      


def process_delete_user_fn(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : delete user func
    * 
    * parms :
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """ 
    
    opstat          =   opStatus()
    
    fparms          =   get_parms_for_input(parms,dtcw.maintain_user_fns_input_idList)
    
    ftitle          =   fparms[0]
    
    if(len(ftitle) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("'function_title' is not defined")
                
    if(opstat.get_status()) :
        
        from dfcleanser.sw_utilities.sw_utility_genfunc_model import delete_generic_user_function
        
        try :
            delete_generic_user_function(ftitle)
            opstat.set_errorMsg("User fn [" + ftitle + "] deleted sucessfully")
        except Exception as e:
            opstat.store_exception("Unable to delete user function ",e)
    
    if(opstat.get_status()) :
        
        #make scriptable
        add_to_script(["# Delete user fn " + ftitle,
                       "from dfcleanser.data_transform.data_transform_columns_control import process_delete_user_fn",
                       "process_delete_user_fn(" + json.dumps(parms) + ",False)"],opstat)
            
    return(opstat)      


def add_column_to_df(df,colname,colList,opstat,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : add column with column list
    * 
    * parms :
    *   df      -   dataframe title
    *   colname -   column name
    *   collist -   column values
    *   opstat  -   op status var
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    if(is_existing_column(df,colname)) :
        opstat.set_status(False)
        opstat.set_errorMsg("Column to Add : '" + colname + "' already exists")
        return()
    
    try :
        namesdict = {}
        namesdict.update({"newcolname" : colname})
        
        df   =   df.assign(newcolname=colList)
        df.rename(columns=namesdict,inplace=True)
        
    except Exception as e:
        opstat.store_exception("Add New Column Error",e)
    
    return(df)




def process_add_column(optionid,parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : process add column option
    * 
    * parms :
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    dtw.display_main_option(None)
    
    opstat = opStatus()
    
    if(display) :
        clock = RunningClock()
        clock.start()
        
    # get column names from file
    if(optionid == dtm.PROCESS_ADD_FROM_FILE_OPTION) :
        opstat  =   add_column_from_file(parms,display=True) 
                       
    # get column names from file
    elif(optionid == dtm.PROCESS_ADD_FROM_FILE_WITH_INDEX_OPTION) :
        opstat  =   add_column_from_indexed_file(parms)
                
    # get column names from code    
    elif(optionid == dtm.PROCESS_ADD_FROM_CODE_OPTION) :
        opstat  =   add_column_from_user_code(parms)
            
    # get column names from dfc function    
    elif(optionid == dtm.PROCESS_ADD_FROM_DFC_FUNCS) :
        opstat  =   add_column_from_dfc_fn(parms)
                        
    # get column names from dfc function    
    elif(optionid == dtm.PROCESS_ADD_FROM_DF_OPTION) :
        opstat  =   add_column_from_df(parms)
            
    if(display) :
        clock.stop()  
        
    return(opstat)


def add_column_from_file(parms,display=True) :
    """
    * -------------------------------------------------------- 
    * function : process add column from file 
    * 
    * parms :
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat  =   opStatus()
    
    df      =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
  
    fparms  =   get_parms_for_input(parms,dtcw.add_column_file_input_idList)

    newcolname      =   fparms[0]
    addcoldftitle   =   fparms[1]
    newcoldatatype  =   fparms[2]
    filename        =   fparms[3]
    nafillvalue     =   fparms[4] 
          
    if( (len(newcolname) < 1) ) :
        opstat.set_status(False)
        opstat.set_errorMsg("Unable to add new column from file : no column name specified")
            
    elif( (len(filename) < 1) ) :
        opstat.set_status(False)
        opstat.set_errorMsg("Unable to add column from file : file name invalid")
                
    else :
        
        colList = []
        
        try :
            with open(filename, 'r') as col_list_file :
                colList = json.load(col_list_file)
            col_list_file.close()
        except Exception as e:
            opstat.store_exception("Unable to load col list file : " + filename,e)
            
        if(opstat.get_status()) :
            
            df  =   cfg.get_dataframe(addcoldftitle)
                
            if( not (len(colList) == len(df)) ) :
                opstat.set_status(False)
                opstat.set_errorMsg("Unable to add column : length of column list values not equal to df column length")

            else :
                
                df = add_column_to_df(df,newcolname,colList,opstat)
                cfg.set_dfc_dataframe_df(addcoldftitle,df)
                df      =   cfg.get_dataframe(addcoldftitle)
                
                if(opstat.get_status()) :
                    
                    try :
                        df[newcolname].fillna(nafillvalue,inplace=True) 
                    except Exception as e:
                        opstat.store_exception("fillna failure for column " + newcolname + " :  value = " + str(nafillvalue),e)
    
                    if(opstat.get_status()) : 
        
                        try :
                            df[newcolname] = df[newcolname].astype(get_datatype_from_dtype_str(newcoldatatype),copy=False)
                        except Exception as e:
                            opstat.store_exception("Error changing datatype for column " + newcolname + " to " + newcoldatatype,e)
                            
    if(opstat.get_status()) :
        opstat.set_errorMsg("Column '" + newcolname + "' added successfully from '" + filename + "'")

    return(opstat)


def add_column_from_indexed_file(parms,display=True) :
    """
    * -------------------------------------------------------- 
    * function : process add column from file with index
    * 
    * parms :
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat  =   opStatus()
    
    df      =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
    
    fparms  =   get_parms_for_input(parms,dtcw.add_colind_file_input_idList)

    newcolname      =   fparms[0]
    newcoldatatype  =   fparms[1]
    filename        =   fparms[2]
    nafillvalue     =   fparms[3] 
    indexmap        =   fparms[4]
          
    if( (len(newcolname) < 1) ) :
        opstat.set_status(False)
        opstat.set_errorMsg("Unable to add new column from file : no column name specified")
            
    elif( (len(filename) < 1) ) :
        opstat.set_status(False)
        opstat.set_errorMsg("Unable to add column from file : file name invalid")
                
    else :
            
        colDict = {}
            
        try :
            
            with open(filename, 'r') as col_dict_file :
                colDict = json.load(col_dict_file)
            col_dict_file.close()
            
        except Exception as e:
            opstat.store_exception("Unable to load col dict file : " + filename,e)

        if(opstat.get_status()) :
                
            # get column list based on index to map
                
            filecolnameindexList    =   colDict.get("filecolnameindex")
            fileindexList           =   colDict.get("fileindexList")
            filecolvaluesList       =   colDict.get("filecolvaluesList")
                
            fileindexmap            =   json.load(indexmap)
                
            dfindex     =   []
                
            for i in range(len(filecolnameindexList)) :
                    
                dfcolname   =   fileindexmap.get(filecolnameindexList[i],None)
                if(not (dfcolname is None)) :
                    dfindex.append(dfcolname)
                        
            if(len(dfindex) == 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("No matching map index")
                    
            else :
                    
                badcolfound     =   False
                    
                for i in range(len(dfindex)) :
                    if(not (is_column_in_df(df,dfindex[i]))) :
                        badcolfound     =   True
                            
                if(badcolfound) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("Bad column in matching map index")
                        
                if(opstat.get_status()) :
                        
                    dfcolslist      =   df.columns.tolist()
                    dfindexoffsets  =   []
                        
                    for i in range(len(dfcolslist)) :
                        for j in range(len(dfindex)) :
                                
                            if(dfcolslist[i] == dfindex[j]) :
                                dfindexoffsets.append(i)
    
    # IF GOT GOOD COLUMN LIST TO ADD                    
    if(opstat.get_status())  :   

        colslist    =   []                    
                    
        for i in range(len(df)) :
                
            indexvals       =   df.iloc[i,dfindexoffsets]
                
            try :
                filevalsindex   =   fileindexList.index(indexvals)
                colslist.append(filecolvaluesList[filevalsindex])
            except :
                colslist.append(nafillvalue)
                    
        if(opstat.get_status()) :
                    
            df  =   add_column_to_df(df,newcolname,colslist,opstat)
            cfg.set_dfc_dataframe_df(cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF),df)
            df  =   cfg.get_current_chapter_df(cfg.DataTransform_ID) 
            
            if(opstat.get_status()) :
                    
                try :
                    df[newcolname].fillna(nafillvalue,inplace=True) 
                except Exception as e:
                    opstat.store_exception("fillna failure for column " + newcolname + " :  value = " + str(nafillvalue),e)
    
                if(opstat.get_status()) : 
                        
                    try :
                        df[newcolname] = df[newcolname].astype(get_datatype_from_dtype_str(newcoldatatype),copy=False)
                    except Exception as e:
                        opstat.store_exception("Error changing datatype for column " + newcolname + " to " + newcoldatatype,e)
    
    if(opstat.get_status()) :
        opstat.set_errorMsg("Column " + newcolname + " added successfully from " + filename)
    
    return(opstat)



def add_column_from_user_code(parms,display=True) :
    """
    * -------------------------------------------------------- 
    * function : process add column from user code
    * 
    * parms :
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat  =   opStatus()

    fparms  =   get_parms_for_input(parms,dtcw.add_column_code_user_fns_input_idList)
            
    newcolname      =   fparms[0]
    newdftitle      =   fparms[1]
    newdatatype     =   fparms[2]
    ftitle          =   fparms[3]
    fmodule         =   fparms[4]
    fname           =   fparms[5]
    fcode           =   fparms[6]

    if( (len(newcolname) < 1) ) :
        opstat.set_status(False)
        opstat.set_errorMsg("Unable to add new column - no name specified")
            
    elif( (len(fmodule) < 1) ) :
        opstat.set_status(False)
        opstat.set_errorMsg("Unable to add column : module name invalid")
        
    elif( (len(fname) < 1) ) :
        opstat.set_status(False)
        opstat.set_errorMsg("Unable to add column : function name invalid")
        
    elif( (len(fcode) < 1) ) :
        opstat.set_status(False)
        opstat.set_errorMsg("Unable to add column : code invalid")
                
    else :
        
        df      =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
            
        try :
                
            if(fcode.find("set_add_col_list(") < 0) :
                opstat.set_status(False)
                opstat.set_errorMsg("User fn code does not call set_add_col_list")
            else :
                exec(fcode)
                    
                from dfcleanser.common.common_utils import get_add_col_list
                df = add_column_to_df(df,newcolname,get_add_col_list(),opstat)
                cfg.set_dfc_dataframe_df(cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF),df)
               
        except Exception as e:
            opstat.store_exception("Unable to add new column column list from code error",e)
    
    if(opstat.get_status()) :
        opstat.set_errorMsg("Column " + newcolname + " added successfully from user code")

    return(opstat)


def add_column_from_dfc_fn(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : process add column from a dfc function
    * 
    * parms :
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat  =   opStatus()
            
    fparms  =   get_parms_for_input(parms,dtcw.get_current_dfc_funcs_idlist())

    newcolname      =   fparms[0]
    newcoldatatype  =   fparms[1]
    dfcfuncname     =   fparms[2]
    functioncall    =   fparms[3]
    functiondesc    =   fparms[4]
            
    from dfcleanser.sw_utilities.sw_utility_genfunc_model import reservedfunctionsmodule, get_reserved_function_parms, get_reserved_function_parms_datatypes
    gfmodule    =   reservedfunctionsmodule
    print("gfmodule",gfmodule)
            
    kwargs      =   get_reserved_function_parms(dfcfuncname)
    kwdtypes    =   get_reserved_function_parms_datatypes(dfcfuncname)
            
    kwvals  =   []
    for i in range(len(kwargs)) :
        kwvals.append(fparms[i+5])
                
    code            =   fparms[4]
    code            =   code.replace('\\n','\n')
            
    code = parms[1][1]
    code = code.replace('\\n','\n')
        
    if( (len(newcolname) < 1) ) :
        opstat.set_status(False)
        opstat.set_errorMsg("Unable to add new column - no name specified")
            
    elif( (len(dfcfuncname) < 1) ) :
        opstat.set_status(False)
        opstat.set_errorMsg("Unable to add column : dfcfunc name invalid")
            
    else :
        
        # setup function parms
        for i in range(len(kwvals)) :
                
            if(opstat.get_status()) :
                if(len(kwvals[i] < 1)) :
                        
                    opstat.set_status(False)
                    opstat.set_errorMsg("Unable to add column : function parm" + str(i) + " is not defined")
                        
                else :
                        
                    if(kwdtypes[i] == int) :
                        
                        try :
                            kwvals[i]    =   int(kwvals[i])
                        except :
                            opstat.set_status(False)
                            opstat.set_errorMsg("Unable to add column : function parm" + str(i) + " is invalid type")

                    elif(kwdtypes[i] == float) :
                        
                        try :
                            kwvals[i]    =   float(kwvals[i])
                        except :
                            opstat.set_status(False)
                            opstat.set_errorMsg("Unable to add column : function parm" + str(i) + " is invalid type")
                        
    if(opstat.get_status()) :
            
        try :
                
                
            #TODO                
                
                
            print("add column from df func")       
        except Exception as e:
            opstat.store_exception("Unable to add new column column list from code error",e)
            display_exception(opstat)
    
    if(opstat.get_status()) :
        opstat.set_errorMsg("Column " + newcolname + " added successfully from dfc function")
            
    return(opstat)


def add_column_from_df(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : process add column from a df
    * 
    * parms :
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat  =   opStatus()
            
    sourceparms     =   parms[0]
    sourceparms     =   json.loads(sourceparms)
    sourcefparms    =   get_parms_for_input(sourceparms,dtcw.add_column_source_df_input_idList)
         
    outputparms     =   parms[1]
    outputparms     =   json.loads(outputparms)
    outputfparms    =   get_parms_for_input(outputparms,dtcw.add_column_output_df_input_idList)
        
    addparms        =   parms[2]
    addparms        =   json.loads(addparms)
    addfparms       =   get_parms_for_input(addparms,dtcw.add_column_df_input_idList)
        
    sourcedftitle       =   sourcefparms[0]
    sourcecolname       =   sourcefparms[1]
        
    outputdftitle       =   outputfparms[0]
    newcolname          =   outputfparms[1]
    newcoldatatype      =   outputfparms[2]
        
    sourceindexcolnames =   addfparms[0]
    sourceindexcolnames =   json.loads(sourceindexcolnames)
    outputindexcolnames =   addfparms[1]
    outputindexcolnames =   json.loads(outputindexcolnames)
    fillnavalue         =   addfparms[2]
        
    if((len(outputdftitle) < 1)) :
        opstat.set_status(False)
        opstat.set_errorMsg("Unable to add new column - invalid 'output_dataframe_title' dataframe")
        
    elif((len(newcolname) < 1)) :
        opstat.set_status(False)
        opstat.set_errorMsg("Unable to add new column - 'output_new_column_name' not specified")
            
    elif((len(sourcedftitle) < 1)) :
        opstat.set_status(False)
        opstat.set_errorMsg("Unable to add column : invalid 'source_dataframe_title' dataframe")

    elif((len(sourcecolname) < 1)) :
        opstat.set_status(False)
        opstat.set_errorMsg("Unable to add column : invalid 'source_column_name_to_retrieve' column name")
        
    elif(outputdftitle ==  sourcedftitle) :
        opstat.set_status(False)
        opstat.set_errorMsg("Unable to add column : 'source_dataframe_title' can not equal 'output_dataframe_title'")
            
    elif(cfg.get_dfc_dataframe(sourcedftitle) is None) :
        opstat.set_status(False)
        opstat.set_errorMsg("Unable to add column : 'source_dataframe_title' is not a loaded dfc df")
            
    elif(cfg.get_dfc_dataframe(outputdftitle) is None) :
        opstat.set_status(False)
        opstat.set_errorMsg("Unable to add column : 'output_dataframe_title' is not a loaded dfc df")
            
    elif(not (len(sourceindexcolnames) == len(outputindexcolnames))) :
        opstat.set_status(False)
        opstat.set_errorMsg("Unable to add column : len of 'source_dataframe_match_list' does not equal len of 'output_dataframe_match_list'")
            
    else :
            
        if(fillnavalue == "") :
            fillnavalue = np.NaN
        else :
            fillnavalue     =   get_converted_value(newcoldatatype,fillnavalue,opstat)
            
    if(opstat.get_status()) :
            
        try :
            
            source_df               =   cfg.get_dfc_dataframe_df(sourcedftitle)  
            sourcegetcols           =   sourceindexcolnames.append(sourcecolname)
            source_working_df       =   source_df[sourcegetcols]
                
            output_df               =   cfg.get_dfc_dataframe_df(outputdftitle)  
            output_df.set_index(outputindexcolnames,drop=True,append=False,inplace=True,verify_integrity=False)
                
            for i in range(len(sourceindexcolnames)) :
                    
                out_uniques         =   output_df[outputindexcolnames[i]] .unique()
                criteria            =   source_working_df[sourceindexcolnames[i]].isin(out_uniques)
                source_working_df   =   source_working_df[criteria]
                    
            source_working_df.set_index(sourceindexcolnames,drop=True,append=False,inplace=True,verify_integrity=False)
                
            new_column_list_values  =   []
                
            for i in range(len(output_df)) :
                    
                try :
                    new_column_list_values.append(source_working_df.loc[output_df[outputindexcolnames],[sourcecolname]])
                except :
                    new_column_list_values.append(fillnavalue)
                
            # now add col uaing bew_column_list
            output_df   =   add_column_to_df
            cfg.set_dfc_dataframe_df(outputdftitle,output_df) 
            output_df   =   cfg.get_dfc_dataframe_df(outputdftitle)  
            
            if(opstat.get_status()) :
                    
                opstat = convert_df_cols_datatype(output_df,[newcolname],newcoldatatype,fillnavalue)
                
                if(display) :
            
                    #make scriptable
                    add_to_script(["# Add new column " + newcolname,
                                   "from dfcleanser.data_transform.data_transform_columns_control import add_column_from_df",
                                   "add_column_from_df(" + json.dumps(parms) + ",False)"],opstat)

                    clear_output()
                    dtcw.display_base_data_transform_columns_taskbar()
                    display_status_note("New Column " + newcolname + " Added Successfully")
                
                
        except Exception as e:
            opstat.store_exception("Unable to add new column column list from code error",e)
    
    if(opstat.get_status()) :
        opstat.set_errorMsg("Column " + newcolname + " added successfully from df")
            
    return(opstat)

"""
#--------------------------------------------------------------------------
#    clear column transform working vars
#--------------------------------------------------------------------------
""" 
def clear_dataframe_columns_transform_cfg_values() :

    cfg.drop_config_value(cfg.ADD_COL_CODE_KEY)
    cfg.drop_config_value(cfg.COPY_COL_TO_KEY)
    cfg.drop_config_value(cfg.COPY_COL_FROM_KEY)
    cfg.drop_config_value(cfg.DATA_TRANSFORM_COL_SELECTED_KEY)
    cfg.drop_config_value(cfg.MAP_TRANSFORM_COL_NAME_KEY)
    cfg.drop_config_value(cfg.MOVE_AFTER_COL_ID_KEY)
    cfg.drop_config_value(cfg.ADD_COL_COL_NAME_KEY)
    cfg.drop_config_value(cfg.ADD_COL_DATATYPE_ID_KEY)
    cfg.drop_config_value(cfg.ADD_COL_CODE_KEY)                               
    cfg.drop_config_value(cfg.COPY_COL_TO_KEY)
    cfg.drop_config_value(cfg.COPY_COL_FROM_KEY)
    cfg.drop_config_value(cfg.COMPAT_COL_KEY)
    



    