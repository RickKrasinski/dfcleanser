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

import dfcleanser.common.cfg as cfg 
import dfcleanser.data_transform.data_transform_columns_widgets as dtcw
import dfcleanser.data_transform.data_transform_model as dtm
import dfcleanser.data_transform.data_transform_widgets as dtw


from dfcleanser.common.common_utils import (displayParms, single_quote, get_parms_for_input,
                                            display_exception, display_status, does_col_contain_nan, 
                                            opStatus, RunningClock, is_existing_column, is_numeric_col,
                                            get_datatype, get_datatype_str, is_int_col,
                                            get_col_uniques, get_datatype_id_from_str)

from dfcleanser.common.display_utils import (display_df_sizing_info)        

from IPython.display import clear_output

from dfcleanser.scripting.data_scripting_control import add_to_script


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    Column transform components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#    process column transform option
#--------------------------------------------------------------------------
"""
def process_column_option(parms) :
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
    
    dtcw.display_base_data_transform_columns_taskbar()
    
    if(type(parms) != str) :
        optionid    = parms[2]
        
    colname = cfg.get_config_value(cfg.DATA_TRANSFORM_COL_SELECTED_KEY)
        
    if(optionid == dtm.RENAME_COLUMN) :
        process_rename_column(colname,parms)
    elif(optionid == dtm.ADD_COLUMN) :
        process_add_column(parms)
    elif(optionid == dtm.DROP_COLUMN) :
        process_drop_column(colname,parms)
    elif(optionid == dtm.REORDER_COLUMNS) :
        process_reorder_columns(parms)
    elif(optionid == dtm.MAP_COLUMN) :
        process_map_transform(dtm.MAP_FROM_FILE,colname,parms)
    elif(optionid == dtm.MAP_COLUMN_VALUES) :
        process_map_transform(dtm.MAP_FROM_VALUES,colname,parms)
    elif(optionid == dtm.MAP_COLUMN_FUNCTION) :
        process_map_transform(dtm.MAP_FROM_FUNCTION,colname,parms)
    elif(optionid == dtm.DUMMIES_COLUMN) :
        process_dummy_transform(colname,parms)
    elif(optionid == dtm.CAT_COLUMN) :
        process_cat_transform(colname,parms)
    elif(optionid == dtm.SAVE_COLUMN) :
        process_save_column(colname,parms)
    elif(optionid == dtm.COPY_COLUMN) :
        process_copy_column(parms)
    elif(optionid == dtm.SORT_COLUMN) :
        process_sort_by_column(colname,parms)
    elif(optionid == dtm.APPLY_COLUMN) :
        process_apply_fn_to_column(parms)
    elif(optionid == dtm.DATATYPE_COLUMN) :
        process_datatype_column(colname,parms) 

        
def process_rename_column(colname,parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : rename column transform option
    * 
    * parms :
    *   colname -   cokumn name
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat = opStatus()
    
    fparms = get_parms_for_input(parms[3],dtcw.rename_column_input_idList)
    
    newname     =   fparms[0]
    inplace     =   fparms[1]
    if(inplace == "True") :
        inplace     =   True
    else :
        inplace     =   False
    
    if(not inplace) :    
        resultdf    =   fparms[2]
        if(len(resultdf) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No title specified for result df")
    else :
        resultdf    =   None

    if(opstat.get_status()) :
        
        namesdict = {}
        namesdict.update({colname:newname})
    
    
        df  =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
        try :
        
            if(inplace) :
                df.rename(columns=namesdict,axis=1,inplace=True)
            else :
                newdf           =   df.rename(columns=namesdict,axis=1)
                new_dfcnotes    =   "rename " + colname + " to " + newname
                new_dfcdf       =   cfg.dfc_dataframe(resultdf,newdf,new_dfcnotes)
                cfg.add_dfc_dataframe(new_dfcdf)
        
        except Exception as e:
            opstat.store_exception("Rename Column " + colname + "Error",e)
            display_exception(opstat)
        
        if(opstat.get_status()) :

            if(display) :
            
                #make scriptable
                add_to_script(["# Rename column " + colname + " to " + newname,
                               "from dfcleanser.data_transform.data_transform_columns_control import process_rename_column",
                               "process_rename_column(" + single_quote(colname) + "," + json.dumps(parms) + ",False)"],opstat)
            
                clear_output()
                dtcw.display_base_data_transform_columns_taskbar()
                display_status("Column " + colname + " renamed to " + newname + " successfully")
        

def add_column(dftitle,colname,colList,opstat,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : add column with column list
    * 
    * parms :
    *   dftitle -   dataframe title
    *   colname -   column name
    *   collist -   column values
    *   opstat  -   op status var
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    df = cfg.get_dfc_dataframe_df(dftitle) 
    
    if(is_existing_column(df,colname)) :
        opstat.set_status(False)
        opstat.set_errorMsg("Column to Add : "+colname + " already exists")
        return()
    
    try :
        namesdict = {}
        namesdict.update({"newcolname" : colname})
        
        df  =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
        #TODO inplace
        newdf   =   df.assign(newcolname=colList)
        newdf.rename(columns=namesdict,axis=1,inplace=True)
        
        #TODO assign newdf back to dftitle
        
    except Exception as e:
        opstat.store_exception("Add New Column Error",e)
        if(display) :
            display_exception(opstat)


def process_add_column(parms,display=True) :
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
    
    optionid        =   parms[0][2]
    #print("process_add_column",parms,optionid)

    opstat = opStatus()
   
    if(display) :
        clock = RunningClock()
        clock.start()
        
    # get column names from file
    if(optionid == dtm.PROCESS_ADD_FROM_FILE_OPTION) :
            
        fparms  =   get_parms_for_input(parms[1],dtcw.add_column_file_input_idList)
        print(fparms)

        newcolname      =   fparms[0]
        newcoldatatype  =   fparms[1]
        filename        =   fparms[2]
            
        if( (len(newcolname) < 1) ) :
            opstat.set_status(False)
            opstat.set_errorMsg("Unable to add new column - no name specified")
            display_exception(opstat)
            
        elif( (len(filename) < 1) ) :
            opstat.set_status(False)
            opstat.set_errorMsg("Unable to add column : file name invalid")
            display_exception(opstat)
                
        else :
            
            colList = []
            try :
                with open(filename, 'r') as col_list_file :
                    colList = json.load(col_list_file)
            except Exception as e:
                opstat.store_exception("Unable to load col list file : " + filename,e)
                display_exception(opstat)

            if( not (len(colList) == len(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF))) ) :
                opstat.set_status(False)
                opstat.set_errorMsg("Unable to add column : column list values not equal df column length")
                display_exception(opstat)

            else :
                add_column(cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF),newcolname,colList,opstat)
                
                if(not (opstat.get_status())) :
                    display_exception(opstat) 
                        
    # get column names from code    
    elif(optionid == dtm.PROCESS_ADD_FROM_CODE_OPTION) :
            
        fparms  =   get_parms_for_input(parms[1],dtcw.add_column_code_gf_input_idList)
        print(fparms)

        newcolname      =   fparms[0]
        newcoldatatype  =   fparms[1]
        modulename      =   fparms[2]
        functionname    =   fparms[3]
        code            =   fparms[4]
        code            =   code.replace('\\n','\n')
        
        print("newcolname",newcolname)
        print("newcoldatatype",newcoldatatype)
        print("modulename",modulename)
        print("functionname\n",functionname)
        print("code\n",code)
        
        if( (len(newcolname) < 1) ) :
            opstat.set_status(False)
            opstat.set_errorMsg("Unable to add new column - no name specified")
            display_exception(opstat)
            
        elif( (len(modulename) < 1) ) :
            opstat.set_status(False)
            opstat.set_errorMsg("Unable to add column : module name invalid")
            display_exception(opstat)
        
        elif( (len(functionname) < 1) ) :
            opstat.set_status(False)
            opstat.set_errorMsg("Unable to add column : function name invalid")
            display_exception(opstat)
        
        elif( (len(code) < 1) ) :
            opstat.set_status(False)
            opstat.set_errorMsg("Unable to add column : code invalid")
            display_exception(opstat)
                
        else :
            
            try :
                
                if(code.find("set_add_col_list(") < 0) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("User fn code does not call set_add_col_list")
                else :
                    exec(code)
                    
                    from dfcleanser.common.common_utils import get_add_col_list
                    add_column(cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF),newcolname,get_add_col_list(),opstat)
                    
               
            except Exception as e:
                opstat.store_exception("Unable to add new column column list from code error",e)
                display_exception(opstat)
                
    # get column names from dfc function    
    elif(optionid == dtm.PROCESS_ADD_FROM_DFC_FUNCS) :
                        
        fparms  =   get_parms_for_input(parms[1],dtcw.get_current_dfc_funcs_idlist())
        print(fparms)

        newcolname      =   fparms[0]
        newcoldatatype  =   fparms[1]
        dfcfuncname     =   fparms[2]
        functioncall    =   fparms[3]
        functiondesc    =   fparms[4]
            
        print("newcolname",newcolname)
        print("newcoldatatype",newcoldatatype)
        print("dfcfuncname",dfcfuncname)
        print("functioncall\n",functioncall)
        print("functiondesc\n",functiondesc)
            
        from dfcleanser.sw_utilities.sw_utility_genfunc_model import reservedfunctionsmodule, get_reserved_function_parms, get_reserved_function_parms_datatypes
        gfmodule    =   reservedfunctionsmodule
        print("gfmodule",gfmodule)
            
        kwargs      =   get_reserved_function_parms(dfcfuncname)
        kwdtypes    =   get_reserved_function_parms_datatypes(dfcfuncname)
        print("\nkwargs\n",kwargs)
        print("\nkwdtypes\n",kwdtypes)
            
        kwvals  =   []
        for i in range(len(kwargs)) :
            kwvals.append(fparms[i+5])
                
        print("kwvals",kwvals)

        code            =   fparms[4]
        code            =   code.replace('\\n','\n')
            
        code = parms[1][1]
        code = code.replace('\\n','\n')
        
        if( (len(newcolname) < 1) ) :
            opstat.set_status(False)
            opstat.set_errorMsg("Unable to add new column - no name specified")
            display_exception(opstat)
            
        elif( (len(dfcfuncname) < 1) ) :
            opstat.set_status(False)
            opstat.set_errorMsg("Unable to add column : dfcfunc name invalid")
            display_exception(opstat)
            
        else :
            
            for i in range(len(kwvals)) :
                
                if(opstat.get_status()) :
                    if(len(kwvals[i] < 1)) :
                        
                        opstat.set_status(False)
                        opstat.set_errorMsg("Unable to add column : function parm" + str(i) + " is not defined")
                        display_exception(opstat)
                        
                    else :
                        
                        if(kwdtypes[i] == int) :
                        
                            try :
                                kwvals[i]    =   int(kwvals[i])
                            except :
                                opstat.set_status(False)
                                opstat.set_errorMsg("Unable to add column : function parm" + str(i) + " is invalid type")
                                display_exception(opstat)

                        elif(kwdtypes[i] == float) :
                        
                            try :
                                kwvals[i]    =   float(kwvals[i])
                            except :
                                opstat.set_status(False)
                                opstat.set_errorMsg("Unable to add column : function parm" + str(i) + " is invalid type")
                                display_exception(opstat)
                        
        if(opstat.get_status()) :
            
            try :
                
                
                
                
                
                print("add column from df func")       
            except Exception as e:
                opstat.store_exception("Unable to add new column column list from code error",e)
                display_exception(opstat)
               
    # get column names from dfc function    
    elif(optionid == dtm.PROCESS_ADD_FROM_DF_OPTION) :
            
        fparms  =   get_parms_for_input(parms[1],dtcw.add_column_df_input_idList)
        print(fparms)
            
        outdftitle      =   fparms[0]
        newcolname      =   fparms[1]
        newcoldatatype  =   fparms[2]
        sourcedftitle   =   fparms[3]
        sourcecolname   =   fparms[4]
        fillnavalue     =   fparms[5]
            
        print("outdftitle",outdftitle)
        print("newcolname",newcolname)
        print("newcoldatatype",newcoldatatype)
        print("sourcedftitle",sourcedftitle)
        print("sourcecolname",sourcecolname)
        print("fillnavalue",fillnavalue)
        
        if( (len(outdftitle) < 1) ) :
            opstat.set_status(False)
            opstat.set_errorMsg("Unable to add new column - invalid output dataframe")
            display_exception(opstat)
        
        elif( (len(newcolname) < 1) ) :
            opstat.set_status(False)
            opstat.set_errorMsg("Unable to add new column - no name specified")
            display_exception(opstat)
            
        elif( (len(sourcedftitle) < 1) ) :
            opstat.set_status(False)
            opstat.set_errorMsg("Unable to add column : invalid source dataframe")
            display_exception(opstat)

        elif( (len(sourcecolname) < 1) ) :
            opstat.set_status(False)
            opstat.set_errorMsg("Unable to add column : invalid source column name")
            display_exception(opstat)

        else :
            
            try :
                print("add column from df ")       
            except Exception as e:
                opstat.store_exception("Unable to add new column column list from code error",e)
                display_exception(opstat)
                
                
    if(display) :
        clock.stop()    
            
    if(opstat.get_status()) :

        if(display) :
            
            #make scriptable
            add_to_script(["# Add new column " + newcolname,
                           "from dfcleanser.data_transform.data_transform_columns_control import process_add_column",
                           "process_add_column(" + json.dumps(parms) + ",False)"],opstat)

            clear_output()
            dtcw.display_base_data_transform_columns_taskbar()
            display_status("New Column " + newcolname + " Added Successfully")
            

def save_deleted_column(colname,fname,df) :
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
    
    opstat = opStatus()
    df  =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)  
    try :
        collist = df[colname].tolist()
        with open(fname, 'w') as col_list_file :
            json.dump(collist,col_list_file)
                    
    except Exception as e:
        opstat.store_exception("Unable to save column being dropped ",e)

    return(opstat)


def process_drop_column(colname,parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : drop column transform option
    * 
    * parms :
    *   colname -   cokumn name
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat = opStatus()
    
    fparms = get_parms_for_input(parms[3],dtcw.drop_column_input_idList)
    
    inplace     =   fparms[0]
    
    if(inplace == "True") :
        inplace     =   True
    else :
        inplace     =   False
    
    if(not inplace) :    
        resultdf    =   fparms[1]
        if(len(resultdf) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No title specified for result df")
    else :
        resultdf    =   None
        
    fname   =   fparms[2]
    
    if(len(fname) == 0) :
        fname   =   None

    if(opstat.get_status()) :
        
        df  =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
        
        if(not (fname is None))  :
        
            opstat = save_deleted_column(colname,fname,df)
        
            if(not opstat.get_status()) :
                display_exception(opstat)
            
        if(opstat.get_status()) :
        
            try :
            
                if(not(inplace)) :
                    newdf               =   df.drop([colname],axis=1)
                    new_dfcnotes        =   "drop " + colname
                    new_dfc_dataframe   =   cfg.dfc_dataframe(resultdf,newdf,new_dfcnotes)
                    cfg.add_dfc_dataframe(new_dfc_dataframe)
                else :
                    df.drop([colname],inplace=True,axis=1)
            
            except Exception as e:
                opstat.store_exception("Drop Columns Error",e)
                display_exception(opstat)
    
            if(opstat.get_status()) : 

                if(display) :
            
                    #make scriptable
                    add_to_script(["# drop column " + colname,
                                   "from dfcleanser.data_transform.data_transform_columns_control import process_drop_column",
                                   "process_drop_column(" + single_quote(colname) + "," + json.dumps(parms) + ",False)"],opstat)
            
                    clear_output()
                    dtcw.display_base_data_transform_columns_taskbar()
                    display_status("Column " + colname + " dropped Successfully")

 
def process_save_column(colname,parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : save column transform option
    * 
    * parms :
    *   colname -   cokumn name
    *   parms   -   associated parms
    *   display -   display results flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    opstat = opStatus()
    fparms = get_parms_for_input(parms[3],dtcw.save_column_input_idList)
    
    if(len(fparms) > 0) :
        fname = fparms[0]
    else :
        fname = None
        
    df  =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
    
    if(not (fname == None))  :
    
        try :
            collist = df[colname].tolist()
            with open(fname, 'w') as col_list_file :
                json.dump(collist,col_list_file)
                    
        except Exception as e:
            opstat.store_exception("Unable to save column being dropped ",e)
    
    if(opstat.get_status()) :
        
        if(display) :
            
            #make scriptable
            add_to_script(["# save column " + colname,
                           "from dfcleanser.data_transform.data_transform_columns_control import process_save_column",
                           "process_save_column(" + single_quote(colname) + "," + json.dumps(parms) + ",False)"],opstat)
            clear_output()
            dtcw.display_base_data_transform_columns_taskbar()
            display_status("Column " + colname + " Saved Successfully")

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
    fparms  =    get_parms_for_input(parms[3],dtcw.reorder_columns_input_idList)

    movecol         = fparms[0]
    moveaftercol    = fparms[1]
    
    df          =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
    df_cols     =   df.columns.tolist() 
    
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
        df[final_cols]       
        
    except Exception as e:
        opstat.store_exception("Reorder Columns Error",e)
        display_exception(opstat)

    if(opstat.get_status()) :
        
        if(display) :
            
            #make scriptable
            add_to_script(["# reorder columns ",
                           "from dfcleanser.data_transform.data_transform_columns_control import process_reorder_columns",
                           "process_reorder_columns(" + json.dumps(parms) + ",False)"],opstat)
            
            clear_output()
            dtcw.display_base_data_transform_columns_taskbar()
            display_status("Column " + movecol + " moved Successfully")

    
      
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
    
    fparms  =   get_parms_for_input(parms[3],dtcw.copy_columns_input_idList)

    copytocol      = fparms[0]
    copyfromcol    = fparms[1]

    try : 
        df = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
        df[copytocol] = df[copyfromcol]
        
    except Exception as e:
        opstat.store_exception("Reorder Columns Error",e)
        display_exception(opstat)

    if(opstat.get_status()) :
        
        if(display) :
            
            #make scriptable
            add_to_script(["# copy column ",
                           "from dfcleanser.data_transform.data_transform_columns_control_widgets import process_copy_column",
                           "process_copy_column(" + json.dumps(parms) + ",False)"],opstat)
            
            clear_output()
            dtcw.display_base_data_transform_columns_taskbar()
            display_status("Column " + copyfromcol + " copied to " + copytocol + " Successfully")


def process_sort_by_column(colname,parms,display=True) :
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

    fparms      =   get_parms_for_input(parms[3],dtcw.sort_column_input_idList)
    
    inplace     =   fparms[0]
    
    if(inplace == "True") :
        inplace     =   True
    else :
        inplace     =   False
    
    if(not inplace) :    
        resultdf    =   fparms[1]
        if(len(resultdf) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No title specified for result df")
    else :
        resultdf    =   None
        
    sortorder   =   fparms[2]
    if(sortorder == "True") :
        sortorder   =   True
    else :
        sortorder   =   False
    
    sortkind    =   fparms[3]
    naposition  =   fparms[4]
    resetrowids =   fparms[5]

    if(opstat.get_status()) :

        try : 
            df = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
            
            if(inplace) :
                df.sort_values(colname,axis=1,ascending=sortorder,inplace=True,kind=sortkind,na_position=naposition)
            else :
                newdf               =   df.sort_values(colname,axis=1,ascending=sortorder,inplace=False,kind=sortkind,na_position=naposition)
                new_dfcnotes        =   "sort by " + colname
                new_dfc_dataframe   =   cfg.dfc_dataframe(resultdf,newdf,new_dfcnotes)
                cfg.add_dfc_dataframe(new_dfc_dataframe)
        
            if(resetrowids) :
                from dfcleanser.data_transform.data_transform_dataframe_control import reset_df_index
                opstat = reset_df_index()
        
        except Exception as e:
            opstat.store_exception("Sort df By Column Error : "+colname,e)
            display_exception(opstat)
    
        if(opstat.get_status()) :
        
            if(display) :
            
                #make scriptable
                add_to_script(["# sort by column ",
                           "from dfcleanser.data_transform.data_transform_columns_control import process_sort_by_column",
                           "process_sort_by_column(" + json.dumps(parms) + ",False)"],opstat)
            
                clear_output()
                dtcw.display_base_data_transform_columns_taskbar()
                display_status("Column " + colname + " sorted successfully.")
    
    cfg.drop_config_value(dtcw.sort_column_input_id+"Parms")


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
    apply_id_list   =   dtcw.get_current_apply_fn_idList()
    
    fparms = get_parms_for_input(parms[3],apply_id_list)
    print("process_apply_fn_to_column",parms,fparms)

    dftoapply       =   fparms[0]
    coltoapply      =   fparms[1]
    fntoapply       =   fparms[2]
    fncode          =   fparms[3]
    
    print("dftoapply",dftoapply)
    print("fntoapply",fntoapply)
    print("fncode",fncode)
    
    from dfcleanser.sw_utilities.sw_utility_genfunc_model import get_apply_function_parms
    kwargs  =   get_apply_function_parms(fntoapply)
    
    print("kwargs",kwargs)
    
    kwargs_vals     =   []
    for i in range(len(kwargs)) :
        kwargs_vals.append(fparms[4+i]) 
        
    print("kwargs_vals",kwargs_vals) 
    
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
            #display_exception(opstat)
    
    if(opstat.get_status()) :
        
        if(display) :
            
            #make scriptable
            add_to_script(["# apply fn to column ",
                           "from dfcleanser.data_transform.data_transform_columns_control import process_apply_fn_to_column",
                           "process_apply_fn_to_column(" + json.dumps(parms) + ",False)"],opstat)
            
            clear_output()
            dtcw.display_base_data_transform_columns_taskbar()
            display_status("function applied to column " + coltoapply + " successfully.")
            
    else :
        
        display_exception(opstat)
    
    #et_dc_dataframe()[coltoapply].apply(fncode)
    cfg.drop_config_value(dtcw.apply_column_input_id+"Parms")


def convert_fill_na_value(dtid,nafillvalue,opstat) :
    """
    * -------------------------------------------------------------------------- 
    * function : convert the na fill value to correct type
    * 
    * parms :
    *   dtid        -   datatype id
    *   nafillvalue -   na fiull value
    *   opstat      -   op status var
    *
    * returns : 
    *  na fill value of correct format
    * --------------------------------------------------------
    """ 
    
    if( ((dtid >= 0) and (dtid <= 7)) or (dtid == 17) )  :  
        
        try :
            fillnavalue     =   int(nafillvalue) 
        except :                   
            opstat.set_status(False)
            opstat.set_errorMsg("invalid integer na fill value " + fillnavalue)
            
    elif( ((dtid >= 8) and (dtid <= 10)) or (dtid == 18) ) :
        
        try :
            fillnavalue     =   float(nafillvalue) 
        except :                   
            opstat.set_status(False)
            opstat.set_errorMsg("invalid float na fill value " + fillnavalue)
        
    elif( (dtid >= 15) and (dtid <= 16) ) :
        fillnavalue     =   nafillvalue
        
    elif( (dtid >= 11) and (dtid <= 14) ) :
        print("datetime component")        
        
    else :
        opstat.set_status(False)
        opstat.set_errorMsg("unknown datatype na fill value " + fillnavalue)
        

def process_datatype_column(colname,parms,display=True)  :
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

    opstat          =   opStatus()
    fillnaoption    =   parms[1]
    fillnavalue     =   None
    
    df          =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
    nans_flag   =   does_col_contain_nan(df,colname)
    
    nafillvalue     =   None
    nafillmethod    =   None    
    nafillinplace   =   None 
    nafilllimit     =   None 
    
    nadropanyall    =   "any" 
    nadropthreshold =   None    
    nadropinplace   =   False    
    
    if(nans_flag) :
        
        if(fillnaoption == dtm.FILL_NA__OPTION) :
            
            if(is_numeric_col(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),colname)) :
                
                fparms          =   get_parms_for_input(parms[2],dtcw.dt_data_type_fn_input_idList)
                datatype        =   fparms[0]
                fillnavalue     =   fparms[2]
                fillnamethod    =   fparms[3]
                fillnainplace   =   fparms[4]
                fillnalimit     =   fparms[5]
                
                if(fillnamethod.find("None") > -1) :
                    nafillmethod    =  fillnamethod
                else :
                    nafillmethod    =  None
                 
            else :
                
                fparms          =   get_parms_for_input(parms[2],dtcw.dt_nn_fn_data_type_input_idList)
                datatype        =   fparms[0]
                fillnavalue     =   fparms[2]
                fillnainplace   =   fparms[3]
                fillnalimit     =   fparms[4]
            
            if(len(fillnavalue) > 0) :
                nafillvalue    =   convert_fill_na_value(datatype,fillnavalue,opstat)
            else :
                nafillvalue    =   None
            
            if(fillnainplace == "True") :
                nafillinplace   =   True
            else :
                nafillinplace   =   False

            if(len(fillnalimit) > 0) :
                
                try :
                    nafilllimit     =   int(fillnalimit)    
                except :
                    opstat.set_status(False)
                    opstat.set_errorMsg("invalid limit value")
                    
            else :
                nafilllimit     =   None     
                
        else :
            
            fparms          =   get_parms_for_input(parms[2],dtcw.dt_data_type_dn_input_idList)
            datatype        =   fparms[0]
            dropnaanyall    =   fparms[2]
            dropnathreshold =   fparms[3]
            dropnainplace   =   fparms[4]

            if(len(dropnaanyall) > 0) :
                if(dropnaanyall == "all") :
                    nadropanyall   =   "all"
                else :
                    nadropanyall   =   "any"
            else :
                nadropanyall   =   "any" 
                
            if(len(dropnathreshold) > 0) :
                
                try :
                    nadropthreshold     =   int(dropnathreshold)    
                except :
                    opstat.set_status(False)
                    opstat.set_errorMsg("invalid drop threshold value")
                    
            else :
                nadropthreshold     =   None    
                
            if(dropnainplace == "True") :
                nadropinplace   =   True
            else :
                nadropinplace   =   False
            
    else :
        
        fparms          =   get_parms_for_input(parms[2],dtcw.dt_nonans_data_type_input_idList)
        datatype        =   fparms[0]
    
    datatype_id     =   get_datatype_id_from_str(datatype)

    print("process_datatype_column",colname,parms,fparms)

    # validate the input parms


       
    if(nans_flag) :
        if(not(fillnamethod is None)) :
            if(fillnamethod.find("None") < -1) :
                if(fillnamethod == "mean") :
                    if(is_numeric_col(df,colname)) :
                        fillnavalue     =   df[colname].mean() 
                    else :
                        opstat.set_status(False)
                        opstat.set_errorMsg("can not define a mean value for a non numeric column")
                        fillnavalue     =   None
                else :
                    if( (not (fillnamethod == "ffill")) and (not (fillnamethod == "bfill")) ) :
                        opstat.set_status(False)
                        opstat.set_errorMsg("invalid na fill method " + fillnamethod)
                        fillnamethod     =   None
            else :
                fillnamethod     =   None    
                        
    if(is_numeric_col(df,colname) and (nans_flag)) :

        try :
            if(is_int_col(df,colname)) :
                fillnavalue     =   int(fillnavalue) 
            else :
                fillnavalue     =   float(fillnavalue)    
        except :                   
            opstat.set_status(False)
            opstat.set_errorMsg("invalid na fill value " + fillnavalue)
    
    if(opstat.get_status()) :   
        
        if(nans_flag) :
        
            try :
                df[colname] = df[colname].fillna(fillnavalue,method=fillnamethod)#value=fillnavalue,method=fillnamethod,axis=None,inplace=True)    
            except :                    
                opstat.set_status(False)
                if(not (fillnamethod is None) ) :
                    opstat.set_errorMsg("fillna failure for column " + colname + " : method = " + fillnamethod + " : value = " + str(fillnavalue) + " : " + str(sys.exc_info()[0]))
                else :
                    opstat.set_errorMsg("fillna failure for column " + colname + " : value = " + str(fillnavalue) + " : " + str(sys.exc_info()[0]))

    if(opstat.get_status()) : 
        
        if( (datatype_id == 11) or 
            (datatype_id == 12) or
            (datatype_id == 13) or
            (datatype_id == 14) ) :
            
            convparms = [get_datatype_str(datatype_id),colname,fillnavalue]
            from dfcleanser.data_transform.data_transform_widgets import display_datetime_convert
            display_datetime_convert(convparms)
            return()

        try :
            df[colname] = df[colname].astype(get_datatype(datatype_id),copy=True)
        except :
            opstat.set_status(False)
            opstat.set_errorMsg("error changing data type ")
    
    if(opstat.get_status()) :
        
        print("\n")
        if(display) :
            display_status("Column [" + colname + "] datatype changed successfully to " + get_datatype_str(datatype_id))
            
            #print("new dtype",df[colname].dtype)
            
    else :
        display_exception(opstat)

 
def process_map_transform(mtype,colname,parms,display=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : mapping transform
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
    fparms  =   get_parms_for_input(parms[3],dtcw.transform_map_input_idList)

    mapDict         = None
    map_file_name   = fparms[0]
    if(len(map_file_name) == 0) :
        map_file_name = "None"
    
    nanFlag         = fparms[1]
    if(len(nanFlag) == 0) :
        nanFlag = "False"

    mapkeys = fparms[2].split(',')
    mapvals = fparms[3].split(',')
    
    for i in range(len(mapvals)) :
        try :
            if(fparms[i].find(".") is not -1) :
                fparms[i] = float(fparms[i])
            else :
                fparms[i] = int(fparms[i])
        except Exception :
            fparms[i] = str(fparms[i])    
     
    if(len(mapkeys) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("Mapping Keys are not defined")

    elif( (len(mapvals) == 0) ) :
        opstat.set_status(False)
        opstat.set_errorMsg("Mapping Values are not defined")

    elif( not (len(mapkeys) == len(mapvals)) ) : 
        opstat.set_status(False)
        opstat.set_errorMsg("Length of Mapping Values and Keys don't match")
    
    # check if mapping is in a file
    if(map_file_name != "None") :
        
        try :
            with open(map_file_name, 'r') as map_file :
                mapDict = json.loads(map_file)
        except Exception as e:
            opstat.store_exception("Error opening map file " + map_file_name,e)
            display_exception(opstat)
        
    else : 
        
        mapDict = {}
        
        if(len(mapkeys) == len(mapvals)) :
            for i in range(len(mapkeys)) :
                mapDict.update({mapkeys[i]:mapvals[i]})
        else :
            opstat.set_status(False)
    
    if(opstat.get_status()) : 
        
        handlenan = False
        if(nanFlag  == "True") :
            handlenan = None
        else :
            handlenan = 'ignore'
    
        opstat = make_col_categorical_from_map(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF), 
                                               colname, mapDict, handlenan)
        
        if(opstat.get_status()) :
            
            labellist = [dtcw.transform_map_input_labelList[:3]]
            valslist  = [map_file_name,nanFlag,
                         str(mapkeys),str(mapvals)]
  
            displayParms("Map Column " + colname + " Parms",labellist,valslist,cfg.DataTransform_ID)
            
            display_status("Column " + colname + " mapped successfully")
            
            if(display) :
                #make scriptable
                add_to_script(["# Make col map for " + colname,
                               "from dfcleanser.data_transform.data_transform_columns_control import process_map_transform",
                               "process_map_transform(" + single_quote(colname) + "," + json.dumps(parms) + ",False)"],opstat)
            
        else :
            display_exception(opstat)
            
    else :
        
        display_exception(opstat)
        print("\n")
        
    if(opstat.get_status()) :
        if(display) :
            dtw.display_column_transform_status(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),colname)


def process_dummy_transform(colname,parms,display=True) :
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
    fparms  =   get_parms_for_input(parms[3],dtcw.transform_dummy_input_idList)

    removecol = True
    if(len(fparms) > 0) :
        if(fparms[0] == "False") :
            removecol = False
    
    opstat = make_col_categorical_from_dummies(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),
                                               colname, removecol) 

    if(opstat.get_status()) :
        
        if(display) :
            #make scriptable
            add_to_script(["# Make dummies for " + colname,
                           "from dfcleanser.data_transform.data_transform_column_control import process_dummy_transform",
                           "process_dummy_transform(" + single_quote(colname) + "," + json.dumps(parms)  + ",False)"],opstat)
        
        if(display) :
            display_status("Column [" + colname + "] dummies created successfully")
        
        if(removecol) :
            if(display) :
                display_status("Column [" + colname + "] dropped successfully")
            
            cfg.drop_config_value(cfg.CLEANSING_COL_KEY)
            
        else :
            if(display) :
                print("\n")
            
    else :
        display_exception(opstat)
    
    if(display) :
        display_df_sizing_info(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF))
        print("\n")        

    if(opstat.get_status()) :
        if(display) :
            if(not removecol) :
                dtw.display_column_transform_status(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),
                                                     colname)


def process_cat_transform(colname,parms,display=True) :
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
    
    opstat  =   opStatus()
    fparms  =   get_parms_for_input(parms[3],dtcw.transform_category_input_idList)
    
    makecat = True
    if(len(fparms) > 0 ) :
        if(fparms[0] == "False") :
            makecat = False
            
    changedatatype = False
    if(len(fparms) > 1 ) :
        if(fparms[1] == "True") :
            changedatatype = True
    
    if((not (makecat)) and (not (changedatatype))) :
        opstat.set_status(False)
        opstat.set_errorMsg("Both parms are false : you must make catagorical or change datatye to category")
    
    else :
        if(makecat) :       
            opstat = make_col_categorical(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),colname) 
    
    if(opstat.get_status()) :
        
        if(changedatatype) :
            try :
                cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)[colname] = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)[colname].astype('category')
            except Exception as e:
                opstat.store_exception("Change to category datatype",e)
                display_exception(opstat)
    
    if(opstat.get_status()) :
        
        print("\n")
        if(display) :
            
            if(changedatatype) :
                display_status("Column [" + colname + "] categorized successfully and datatype changed to category")
            else : 
                display_status("Column [" + colname + "] categorized successfully")
            
    else :
        display_exception(opstat)

        
    if(display) :
        
        #make scriptable
        add_to_script(["# Make categories for " + colname,
                       "from dfcleanser.data_transform.data_transform_columns_control import process_cat_transform",
                       "process_cat_transform(" +  single_quote(colname) + "," + json.dumps(parms) + ",False)"],opstat)

        labellist = [dtcw.transform_category_input_labelList[0],dtcw.transform_category_input_labelList[1]]
        valuelist = [str(makecat),str(changedatatype)]
    
        displayParms("Column " + colname + " Category Transform Parms",labellist,valuelist,cfg.DataTransform_ID)
        
        dtw.display_column_transform_status(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),colname)


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
    import numpy as np
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
    
    import pandas as pd
    
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
            
    if(opstat.get_status()) :
        print("new df")
    
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

"""
#--------------------------------------------------------------------------
#    clear column transform working vars
#--------------------------------------------------------------------------
""" 
def clear_dataframe_columns_transform_cfg_values() :

    cfg.drop_config_value(dtcw.transform_map_input_id+"Parms")
    cfg.drop_config_value(dtcw.transform_map_input_id+"ParmsProtect")
    cfg.drop_config_value(dtcw.transform_dummy_input_id+"Parms")
    cfg.drop_config_value(dtcw.transform_dummy_input_id+"ParmsProtect")
    cfg.drop_config_value(dtcw.transform_category_input_id+"Parms")
    cfg.drop_config_value(dtcw.transform_category_input_id+"ParmsProtect")
    
    cfg.drop_config_value(dtcw.add_column_input_id+"Parms")
    cfg.drop_config_value(dtcw.add_column_input_id+"ParmsProtect")
    cfg.drop_config_value(dtcw.add_column_file_input_id+"Parms")
    cfg.drop_config_value(dtcw.add_column_file_input_id+"ParmsProtect")
    cfg.drop_config_value(dtcw.add_column_code_gf_input_id+"Parms")
    cfg.drop_config_value(dtcw.add_column_code_gf_input_id+"ParmsProtect")
    cfg.drop_config_value(dtcw.add_column_df_input_id+"Parms")
    cfg.drop_config_value(dtcw.add_column_df_input_id+"ParmsProtect")
    cfg.drop_config_value(dtcw.add_column_code_dfc_funcs_input_id+"Parms")
    cfg.drop_config_value(dtcw.add_column_code_dfc_funcs_input_id+"ParmsProtect")
    
    
    cfg.drop_config_value(dtcw.reorder_columns_input_id+"Parms")
    cfg.drop_config_value(dtcw.reorder_columns_input_id+"ParmsProtect")
    cfg.drop_config_value(dtcw.sort_column_input_id+"Parms")
    cfg.drop_config_value(dtcw.sort_column_input_id+"ParmsProtect")
    cfg.drop_config_value(dtcw.apply_column_lambda_input_id+"Parms")
    cfg.drop_config_value(dtcw.apply_column_lambda_input_id+"ParmsProtect")
    cfg.drop_config_value(dtcw.apply_column_lambda_parms_input_id+"Parms")
    cfg.drop_config_value(dtcw.apply_column_lambda_parms_input_id+"ParmsProtect")

    cfg.drop_config_value(dtcw.copy_columns_input_id+"Parms")
    cfg.drop_config_value(dtcw.copy_columns_input_id+"ParmsProtect")
    cfg.drop_config_value(dtcw.rename_column_input_id+"Parms")
    cfg.drop_config_value(dtcw.rename_column_input_id+"ParmsProtect")
    cfg.drop_config_value(dtcw.drop_column_input_id+"Parms")
    cfg.drop_config_value(dtcw.drop_column_input_id+"ParmsProtect")
    cfg.drop_config_value(dtcw.save_column_input_id+"Parms")
    cfg.drop_config_value(dtcw.save_column_input_id+"ParmsProtect")
    
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
    



    