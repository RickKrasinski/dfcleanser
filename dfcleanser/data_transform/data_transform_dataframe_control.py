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

from dfcleanser.common.common_utils import (display_exception, display_status_note,
                                            opStatus, single_quote, get_parms_for_input)

from dfcleanser.common.table_widgets import (dcTable)

from dfcleanser.common.display_utils import display_column_names

from dfcleanser.scripting.data_scripting_control import add_to_script


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
#    process the dataframe transform options
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def process_df_transform(optionid,parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : process dataframe transform option
    * 
    * parms :
    *   optionid  -   transform option
    *   parms     -   transform parms
    *   display   -   display flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat  =   opStatus()
    
    #dftw.display_dataframe_transform_taskbar()
    
    if(optionid == dtm.PROCESS_SHOW_COLUMN_NAMES_ROW) :
        
        dftw.display_dataframe_col_names_taskbar()
        
        print("\n")
        col_names_table = dcTable("Column Names ","cnamesTable",cfg.DataTransform_ID)
        col_names_table.set_table_column_parms({"font":12})
        col_names_table.set_note("None")
        display_column_names(cfg.get_current_chapter_df(cfg.DataTransform_ID),col_names_table,None)  


    if(optionid == dtm.PROCESS_SAVE_COLUMN_NAMES_ROW) :
        
        [opstat, filename]  =   save_column_names_row(parms)
        
        dftw.display_dataframe_col_names_taskbar()

        if(opstat.get_status()) :
            display_status_note("Column Names Row Saved Successfully to : " + filename) 
            clear_dataframe_transform_cfg_values()
        else :
            display_exception(opstat)

        
    # add column names row
    elif(optionid == dtm.PROCESS_ADD_COLUMN_NAMES_ROW) :
    
        opstat     =   add_column_names_row(parms) 
        
        dftw.display_dataframe_col_names_taskbar()
        print("\n")
        
        if(opstat.get_status()) :

            clear_dataframe_transform_cfg_values()
            display_status_note("Column Names Row Added Successfully")
            
            col_names_table = dcTable("Column Names ","cnamesTable",cfg.DataTransform_ID)
            col_names_table.set_table_column_parms({"font":12})
            col_names_table.set_note("None")
            display_column_names(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),col_names_table,None)    
                
        else :
                    
            display_main_option([[0,0]])
            display_exception(opstat)

    
    elif(optionid == dtm.PROCESS_CHANGE_COLUMN_NAMES) :
        
        opstat = change_column_names(parms)
        
        dftw.display_dataframe_col_names_taskbar()
        print("\n")
        
        if(opstat.get_status()) :
                
            clear_dataframe_transform_cfg_values()
            display_status_note("Column Names Changed Successfully")
            
            col_names_table = dcTable("Column Names ","cnamesTable",cfg.DataTransform_ID)
            col_names_table.set_table_column_parms({"font":12})
            col_names_table.set_note("None")
            display_column_names(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),col_names_table,None)    
                
        else :
            display_exception(opstat)


    if(optionid == dtm.PROCESS_DROP_COLUMN_NAMES_ROW) :
        
        opstat      =   drop_column_names_row()
        
        dftw.display_dataframe_col_names_taskbar()
        print("\n")
            
        if(opstat.get_status()) :
            display_status_note("Column Names Row Dropped Successfully")
            clear_dataframe_transform_cfg_values()
        else :
            display_exception(opstat)

            
    if(optionid == dtm.PROCESS_WHITESPACE_COLUMN_NAMES) :
        
        opstat      =   remwhitespace_column_names_row(parms)
        
        dftw.display_dataframe_col_names_taskbar()
        print("\n")
            
        if(opstat.get_status()) :
            display_status_note("Column Names Whitespace Removed Successfully")
            clear_dataframe_transform_cfg_values()
        else :
            display_exception(opstat)
        
    
    elif(optionid == dtm.PROCESS_SET_DF_INDEX) :
        
        opstat = set_df_index(parms) 
        
        dftw.display_dataframe_indices_taskbar()
        print("\n")
                
        if(opstat.get_status()) :
            clear_dataframe_transform_cfg_values()
            display_status_note("df Index Set Successfully")
        else :
            display_exception(opstat)
            
        dftw.display_current_df_index(cfg.get_current_chapter_df(cfg.DataTransform_ID),
                                      cfg.get_current_chapter_dfc_df_title(cfg.DataTransform_ID))
        
        dftw.display_remote_df(cfg.DataTransform_ID)

                
    elif(optionid == dtm.PROCESS_RESET_DF_INDEX) :
        
        opstat = reset_df_index(parms)
        
        dftw.display_dataframe_indices_taskbar()
        print("\n")
            
        if(opstat.get_status()) :
            clear_dataframe_transform_cfg_values()
            display_status_note("df Index Reset Successfully")
        else :
            display_exception(opstat)
            
        dftw.display_current_df_index(cfg.get_current_chapter_df(cfg.DataTransform_ID),
                                      cfg.get_current_chapter_dfc_df_title(cfg.DataTransform_ID))
        
        dftw.display_remote_df(cfg.DataTransform_ID) 
            
    elif(optionid == dtm.PROCESS_APPEND_TO_INDEX) :
        
        opstat = append_to_df_index(parms)
        
        dftw.display_dataframe_indices_taskbar()
        print("\n")
            
        if(opstat.get_status()) :
            clear_dataframe_transform_cfg_values()
            display_status_note("df Index Appended to Successfully")
        else :
            dftw.display_dataframe_options([[4,0]])
            display_exception(opstat)
            
        dftw.display_current_df_index(cfg.get_current_chapter_df(cfg.DataTransform_ID),
                                      cfg.get_current_chapter_dfc_df_title(cfg.DataTransform_ID))
 
        dftw.display_remote_df(cfg.DataTransform_ID) 
            
    elif(optionid == dtm.PROCESS_SORT_DF_INDEX) :
        
        opstat = sort_df_index(parms)
        
        dftw.display_dataframe_indices_taskbar()
        print("\n")
            
        if(opstat.get_status()) :
            clear_dataframe_transform_cfg_values()
            display_status_note("Dataframe Sorted by index Successfully")
        else :
            display_exception(opstat)
        
        dftw.display_current_df_index(cfg.get_current_chapter_df(cfg.DataTransform_ID),
                                      cfg.get_current_chapter_dfc_df_title(cfg.DataTransform_ID))
        
        dftw.display_remote_df(cfg.DataTransform_ID) 

    # drop duplicate rows
    elif(optionid == dtm.PROCESS_SORT_COLUMN) :

        opstat = process_sort_by_column(parms,display)
        
        dftw.display_dataframe_transform_main()
        print("\n")
            
        if(opstat.get_status()) :
            clear_dataframe_transform_cfg_values()
            display_status_note(opstat.get_errorMsg())
        else :
            display_main_option([[0,0]])
            display_exception(opstat) 
            
    # drop duplicate rows
    elif(optionid == dtm.PROCESS_DROP_DUPLICATE_ROWS) :
        
        df = cfg.get_current_chapter_df(cfg.DataTransform_ID)
        
        start_rows  =   len(df)

        opstat = drop_duplicate_rows(parms,display)
        
        end_rows    =   len(df)
        
        dftw.display_dataframe_transform_main()
        print("\n")
            
        if(opstat.get_status()) :
            clear_dataframe_transform_cfg_values()
            display_status_note(str(start_rows-end_rows) + " Duplicate Rows Dropped Successfully")
        else :
            display_exception(opstat) 
    
    # return
    elif(optionid == dtm.DF_TRANSFORM_RETURN) :
        
        dftw.display_dataframe_transform_main()
        
    # help
    elif(optionid == dtm.DF_TRANSFORM_HELP) :
        print("help")




"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    dataframe transform functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def save_column_names_row(parms,display=True):
    """
    * -------------------------------------------------------------------------- 
    * function : save column names row to a file
    * 
    * parms :
    *   parms     -   transform parms
    *   display   -   display flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat = opStatus() 
    
    try :
    
        fparms      =   get_parms_for_input(parms,dftw.df_save_row_transform_input_idList)
        filename    =   fparms[0]
            
        if(len(filename) == 0) :
            filename = "./" + cfg.get_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY)
            #filename = filename.replace(".","_")
            filename = filename + "_column_names.json"

        # see if save col names row 
        if(len(filename) > 0) :
                        
            colids = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF).columns.tolist()

            # save the index row as file
            with open(filename, 'w') as colid_file :
                json.dump(colids,colid_file)
                
            colid_file.close()
                
            if(display) :
                    
                #make scriptable
                add_to_script(["# save column names row",
                               "from dfcleanser.data_transform.data_transform_dataframe_control save_column_names_row",
                               "save_column_names_row(" + json.dumps(parms) + ",False)"],opstat)
                
    except Exception as e:
        opstat.store_exception("Unable to save column names file to : " + filename,e)

    return([opstat, filename])


def change_column_names(parms,display=True):
    """
    * -------------------------------------------------------------------------- 
    * function : change column names 
    * 
    * parms :
    *   parms     -   transform parms
    *   display   -   display flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat = opStatus() 
    
    try :
    
        fparms      =   get_parms_for_input(parms,dftw.df_change_row_transform_input_idList)
        ccolname    =   fparms[0]
        ncolname    =   fparms[1]
        
        if( (len(ccolname) < 1) or (len(ncolname) < 1) ) :
            opstat.set_status(False)
            if(len(ccolname) < 1) :
                opstat.set_errorMsg("current_column_name is invalid")
            else :
                opstat.set_errorMsg("current_column_name is invalid")
                
        else :
        
            collist     =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF).columns.tolist()
            
            try :
                found       =   collist.index(ccolname)
            except :
                opstat.set_status(False)
                opstat.set_errorMsg("current_column_name is not in df")
                
        if(opstat.get_status()) :
            
            collist[found]  =   ncolname
        
            cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF).columns = collist 
            
            if(display) :
                #make scriptable
                add_to_script(["# change column names",
                               "from dfcleanser.data_transform.data_transform_dataframe_control change_column_names",
                               "change_column_names(" + json.dumps(parms) + ",False)"],opstat)
            
    except Exception as e:
        opstat.store_exception("Unable to change column names ",e)
        
    return(opstat)


def add_column_names_row(parms,display=True):
    """
    * -------------------------------------------------------------------------- 
    * function : add a column names row
    * 
    * parms :
    *   parms     -   transform parms
    *   display   -   display flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat = opStatus() 
    
    try :

        fparms      =   get_parms_for_input(parms,dftw.df_add_row_transform_input_idList)
        filename    =   fparms[0]
        collist     =   fparms[1]
            
        if(len(filename) == 0) :
            filename = "None"
                
        if(len(collist) == 0 ) :
            collist = "None"
        else :
            collist =   collist.replace("'","")
            collist =   collist.split(",")
                
        if( (not(filename == "None")) or (not(collist == "None"))) :
            
            if(not(filename == "None")) :
                
                try :
                    
                    with open(filename, 'r') as colid_file :
                        colids = json.load(colid_file)
                        colid_file.close()
    
                except Exception as e: 
                    opstat.store_exception("Unable to open column names file" + filename,e)
                    
            else :
                
                colids = collist    
                
            cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF).columns = colids
                    
            if(display) :
                        
                #make scriptable
                add_to_script(["# Add Column Names Row",
                               "from dfcleanser.data_transform.data_transform_dataframe_control add_column_names_row",
                               "add_column_names_row(" + single_quote(filename) +"," + json.dumps(collist) + ",False)"],opstat)
    
        else :
            
            opstat.set_status(False)
            opstat.set_errorMsg("No Column List or filename defined")
    
    except Exception as e: 
        opstat.store_exception("Unable to add column names",e)
    
    return(opstat)


def drop_column_names_row(display=True):
    """
    * -------------------------------------------------------- 
    * function : drop the column names row
    * 
    * parms :
    *   parms     -   transform parms
    *   display   -   display flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat = opStatus() 
    
    try :
        
        df          =   cfg.get_current_chapter_df(cfg.DataTransform_ID)
    
        collist     =   df.columns.tolist()
        df.drop(labels=collist,axis=1,inplace=True)
        
        
            
        if(display) :
            #make scriptable
            add_to_script(["# change column names",
                           "from dfcleanser.data_transform.data_transform_dataframe_control change_column_names",
                           "drop_column_names(False)"],opstat)
            
    except Exception as e:
        opstat.store_exception("Unable to change column names ",e)
        
    return(opstat)


def remwhitespace_column_names_row(parms,display=True):
    """
    * -------------------------------------------------------- 
    * function : drop the column names row
    * 
    * parms :
    *   parms     -   transform parms
    *   display   -   display flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat = opStatus() 
    #TODO  what the fuck   
    return(opstat)
    
    try :
        
        df          =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
    
        collist     =   df.columns.tolist()
        df.drop(labels=collist,axis=1,inplace=True)
        
        
            
        if(display) :
            #make scriptable
            add_to_script(["# change column names",
                           "from dfcleanser.data_transform.data_transform_dataframe_control change_column_names",
                           "drop_column_names(False)"],opstat)
            
    except Exception as e:
        opstat.store_exception("Unable to change column names ",e)
        
    return(opstat)




def reset_df_index(parms,display=True):
    """
    * -------------------------------------------------------------------------- 
    * function : reset df indices
    * 
    * parms :
    *   parms     -   transform parms
    *   display   -   display flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat = opStatus() 
    
    df = cfg.get_current_chapter_df(cfg.DataTransform_ID)
    
    fparms      =   get_parms_for_input(parms,dftw.df_reset_index_transform_input_idList)
    
    drop_levels     =   fparms[0]
    
    if(len(drop_levels) > 0) :
        
        drop_levels     =   drop_levels.lstrip("[")
        drop_levels     =   drop_levels.rstrip("]")
        drop_levels     =   drop_levels.split(",")
        
        if(drop_levels[0] == "All") :
            
            drop_levels     =   []
            
            index_columns   =   df.index.names
            if(len(index_columns) > 0) :
                for i in range(len(index_columns)) :
                    if( not (index_columns[i] is None) ) :
                        drop_levels.append(index_columns[i])
        
    else :
        
        drop_levels     =   None
        
    
    if(fparms[2] == "True") :
        drop  =   False
    else :
        drop  =   True
    
    if(opstat.get_status()) :

        try :
            
            df.reset_index(level=drop_levels,drop=drop,inplace=True)
                
            if(display) :
                #make scriptable
                add_to_script(["# reset df index",
                               "from dfcleanser.data_transform.data_transform_dataframe_control reset_df_index",
                               "reset_df_index(" + json.dumps(parms[1]) + ",False)"],opstat)
    
        except Exception as e: 
            opstat.store_exception("Unable to reset df index : ",e)

    return(opstat)
    

def set_df_index(parms,display=True):
    """
    * -------------------------------------------------------------------------- 
    * function : set df indices
    * 
    * parms :
    *   parms     -   transform parms
    *   display   -   display flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    opstat = opStatus()
    
    fparms      =   get_parms_for_input(parms,dftw.df_set_index_transform_input_idList)

    colnames    =   fparms[0]
    
    if(len(colnames) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("column names list is empty")
        
    else :
        
        colnames    =   colnames.lstrip("[")
        colnames    =   colnames.rstrip("]")
        colnames    =   colnames.split(",")
        
        if(fparms[2] == "True") :
            drop = True
        else :
            drop = False
            
        if(opstat.get_status()) :
                
            if(fparms[3] == "True") :
                verify = True
            else :
                verify = False
                
    if(opstat.get_status()) :

        try : 
            
            df = cfg.get_current_chapter_df(cfg.DataTransform_ID)
            
            df.set_index(colnames,drop=drop,append=True,inplace=True,verify_integrity=verify)
            
            cfg.set_dfc_dataframe_df(cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF),df)
            
            if(display) :
                #make scriptable
                add_to_script(["# set df index",
                               "from dfcleanser.data_transform.data_transform_dataframe_control set_df_index",
                               "set_df_index(" + json.dumps(parms[1]) + ",False)"],opstat)

        
        except Exception as e: 
            opstat.store_exception("Unable to set index of column(s) : " + str(colnames),e)

    return(opstat)


def append_to_df_index(parms,display=True):
    """
    * -------------------------------------------------------------------------- 
    * function : append column to df indices
    * 
    * parms :
    *   parms     -   transform parms
    *   display   -   display flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat = opStatus()

    fparms      =   get_parms_for_input(parms,dftw.df_append_index_transform_input_idList)

    colnames    =   fparms[0]
    colnames    =   colnames.lstrip("[")
    colnames    =   colnames.rstrip("]")
    colnames    =   colnames.split(",")
    
    if(len(colnames) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("column names list is empty")
        
    else :
        
        df = cfg.get_current_chapter_df(cfg.DataTransform_ID)
        
        if(fparms[2] == "True") :
            drop = True
        else :
            drop = False
            
        if(fparms[3] == "True") :
            verify = True
        else :
            verify = False
    
        try :
            
            """
            df.reset_index(drop=False,inplace=True)
                
            cnames        =   list(df.columns)
            levels_to_drop  =   []
            
            for i in range(len(cnames)) :
                if(cnames[i].find("level_") > -1) :
                    levels_to_drop.append(cnames[i])
            
            if(len(levels_to_drop) > 0) :
                df.drop(levels_to_drop,axis=1,inplace=True)
            """
            
            df.set_index(keys=colnames,drop=drop,append=True,inplace=True,verify_integrity=verify)
                
            if(display) :
                #make scriptable
                add_to_script(["# append to df index",
                               "from dfcleanser.data_transform.data_transform_dataframe_control append_to_df_index",
                               "append_to_df_index(" + json.dumps(parms[1]) + ",False)"],opstat)
        
        except Exception as e: 
            opstat.store_exception("Unable to append to df index : " + colnames,e)

    return(opstat)


def sort_df_index(parms,display=True):
    """
    * -------------------------------------------------------------------------- 
    * function : sort df indices
    * 
    * parms :
    *   parms     -   transform parms
    *   display   -   display flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat = opStatus()
    
    fparms      =   get_parms_for_input(parms,dftw.df_sort_index_transform_input_idList)
    
    levels      =   fparms[0]
    
    if(len(levels) > 0) :
        
        levels      =   levels.lstrip("[")
        levels      =   levels.rstrip("]")
        levels      =   levels.split(",")
        
    else :
        
        levels      =   None

    if(fparms[2] == "True") :
        ascending = True
    else :
        ascending = False
        
    kind        =   fparms[3]
    na_position =   fparms[4]
                
    if(opstat.get_status()) :

        try : 
            
            df = cfg.get_current_chapter_df(cfg.DataTransform_ID)
            df.sort_index(axis=0,level=levels,ascending=ascending,inplace=True,kind=kind,na_position=na_position)
                
            if(display) :
                #make scriptable
                add_to_script(["# set row ids column",
                               "from dfcleanser.data_transform.data_transform_dataframe_control sort_df_index",
                               "sort_df_index(" + json.dumps(parms[1]) + ",False)"],opstat)
        
        except Exception as e: 
            opstat.store_exception("Unable to sort df index : ",e)

    return(opstat)
   
      
def process_sort_by_column(parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : sort by column transform option
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

    fparms      =   get_parms_for_input(parms,dftw.sort_column_input_idList)
    
    colname     =   fparms[0]
        
    sortorder   =   fparms[1]
    if(sortorder == "True") :
        sortorder   =   True
    else :
        sortorder   =   False
    
    sortkind    =   fparms[2]
    sortkind    =   sortkind.lstrip("'")
    sortkind    =   sortkind.rstrip("'")    
    naposition  =   fparms[3]
    naposition  =   naposition.lstrip("'")
    naposition  =   naposition.rstrip("'")    

    resetrowids =   fparms[4]
    if(resetrowids == "True") :
        resetrowids     =   True
    else :
        resetrowids     =   False

    if(opstat.get_status()) :

        try : 
            
            df = cfg.get_current_chapter_df(cfg.DataTransform_ID)
            df.sort_values(colname,axis=0,ascending=sortorder,inplace=True,kind=sortkind,na_position=naposition)
        
            if(resetrowids) :
                from dfcleanser.data_transform.data_transform_dataframe_control import reset_df_index
                opstat = reset_df_index()
            
            if(display) :
            
                #make scriptable
                add_to_script(["# sort by column ",
                               "from dfcleanser.data_transform.data_transform_columns_control import process_sort_by_column",
                               "process_sort_by_column(" + json.dumps(parms) + ",False)"],opstat)
                
                opstat.set_errorMsg("df sorted by column '" + colname + "' successfully.")
        
        except Exception as e:
            opstat.store_exception("Sort df By Column Error : "+colname,e)
    
    cfg.drop_config_value(dftw.sort_column_input_id+"Parms")
    
    return(opstat)



def drop_duplicate_rows(parms,display=True):
    """
    * -------------------------------------------------------------------------- 
    * function : drop df duplicate rows
    * 
    * parms :
    *   parms     -   transform parms
    *   display   -   display flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat = opStatus()
    
    fparms      =   get_parms_for_input(parms,dftw.df_drop_dups_transform_input_idList)

    colnames    =   fparms[0]
    
    if(len(colnames) == 0) :
        colnames    =   None
        
    if(fparms[2] == "Drop") :
        drop = True
    else :
        drop = False
    
    keep        =   fparms[3]
    if(keep == "False") :
        keep    =   False
       
        
    df = cfg.get_current_chapter_df(cfg.DataTransform_ID)
            
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
            
            df.drop_duplicates(colnames,keep=keep,inplace=True)
                
            if(display) :
                #make scriptable
                add_to_script(["# drop duplicate rows",
                               "from dfcleanser.data_transform.data_transform_dataframe_control drop_duplicate_rows",
                               "drop_duplicate_rows("+ json.dumps(parms) + ",False)"],opstat)
        
        except Exception as e: 
            opstat.store_exception("Unable to drop duplicate rows : " + colnames,e)

    return(opstat)
 


def clear_dataframe_transform_cfg_values() :
    """
    * -------------------------------------------------------------------------- 
    * function : clear dataframe config data
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    
    
    
    
