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

from dfcleanser.common.common_utils import (displayParms, single_quote, 
                                            display_exception, display_status, 
                                            opStatus, RunningClock, is_existing_column,
                                            get_col_uniques)

from dfcleanser.common.display_utils import (display_df_sizing_info)        

from IPython.display import clear_output

from dfcleanser.scripting.data_scripting_control import add_to_script

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    global list for column values
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
NewColumnValues = []

def get_NewColumnValues() :
    return()
def set_NewColumnValues(ncv) :
    global NewColumnValues
    NewColumnValues = ncv

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
    
    dtcw.display_data_transform_columns_taskbar()
    
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
        process_map_transform(colname,parms)
    elif(optionid == dtm.DUMMIES_COLUMN) :
        process_dummy_transform(colname,parms)
    elif(optionid == dtm.CAT_COLUMN) :
        process_cat_transform(colname,parms)
    elif(optionid == dtm.SAVE_COLUMN) :
        process_save_column(colname,parms)
    elif(optionid == dtm.COPY_COLUMN) :
        process_copy_column(parms)
    elif(optionid == dtm.SORT_COLUMN) :
        process_sort_by_column(parms)
    elif(optionid == dtm.APPLY_COLUMN) :
        process_apply_fn_to_column(parms)
        
"""
#--------------------------------------------------------------------------
#    rename column transform option
#--------------------------------------------------------------------------
"""
def process_rename_column(colname,parms,display=True) :
    
    fparms = dtcw.get_rename_column_inputs(parms)
    newname = fparms[0]
    
    namesdict = {}
    namesdict.update({colname:newname})
    
    opstat = opStatus()
    
    try :
        cfg.set_current_dfc_dataframe(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF).rename(columns=namesdict))
        
    except Exception as e:
        opstat.store_exception("Rename Column Error",e)
        display_exception(opstat)
        
    if(opstat.get_status()) :

        if(display) :
            
            #make scriptable
            add_to_script(["# Rename column " + colname + " to " + newname,
                           "from dfcleanser.data_transform.data_transform_columns_widgets import process_rename_column",
                           "process_rename_column(" + single_quote(colname) + "," + json.dumps(parms) + ",False)"],opstat)
            
            clear_output()
            dtcw.display_base_data_transform_columns_taskbar()
            display_status("Column " + colname + " renamed to " + newname + " successfully")
        

"""
#--------------------------------------------------------------------------
#    add column with column list 
#--------------------------------------------------------------------------
"""
def add_column(colname,colList,opstat,display=True) :
    
    if(is_existing_column(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),colname)) :
        opstat.set_status(False)
        opstat.set_errorMsg("Column to Add : "+colname + " already exists")
        return()
    
    try :
        namesdict = {}
        namesdict.update({"newcolname" : colname})

        cfg.set_current_dfc_dataframe(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF).assign(newcolname=colList))
        cfg.set_current_dfc_dataframe(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF).rename(columns=namesdict))
        
    except Exception as e:
        opstat.store_exception("Add New Column Error",e)
        if(display) :
            display_exception(opstat)


"""
#--------------------------------------------------------------------------
#    process add column option 
#--------------------------------------------------------------------------
"""    
def process_add_column(parms,display=True) :

    optionid        =   parms[0]

    opstat = opStatus()
    
    newcolname  =   parms[1][0]
        
    if(len(newcolname) < 1) :
        opstat.set_status(False)
        opstat.set_errorMsg("Unable to add new column - no name specified")
        display_exception(opstat)
        
    else :
        
        if(display) :
            clock = RunningClock()
            clock.start()
        
        # get column names from file
        if(optionid == dtm.PROCESS_FILE_OPTION) :

            filename    =   parms[1][1]
            
            if( (len(filename) < 1) ) :
                opstat.set_status(False)
                opstat.set_errorMsg("Unable to add column : file name invalid")
                display_exception(opstat)
                
            else :
                colList = []
                try :
                    with open(filename, 'r') as col_list_file :
                        colList = json.load(col_list_file)
                except Exception as e:
                    opstat.store_exception("Unable to load col list file",e)
                    display_exception(opstat)

                if( not (len(colList) == len(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF))) ) :
                    opstat.set_status(False)
                    opstat.set_errorMsg("Unable to add column : column list values not equal df column length")
                    display_exception(opstat)

                else :
                    add_column(newcolname,colList,opstat)
                
                    if(not (opstat.get_status())) :
                        display_exception(opstat) 
                        
        # get column names from code    
        elif(optionid == dtm.PROCESS_ADD_NEW_CODE_OPTION) :
            
            code = parms[1][1]
            code = code.replace('\\n','\n')
            
            try :
                exec(code)
                #print("NewColumnValues",len(NewColumnValues))
                add_column(newcolname,NewColumnValues,opstat)
               
            except Exception as e:
                opstat.store_exception("Unable to add new column column list from code error",e)
                display_exception(opstat)
                
        if(display) :
            clock.stop()    
            
    if(opstat.get_status()) :

        if(display) :
            
            #make scriptable
            add_to_script(["# Add new column " + newcolname,
                           "from dfcleanser.data_transform.data_transform_columns_widgets import process_add_column",
                           "process_add_column(" + json.dumps(parms) + ",False)"],opstat)

            clear_output()
            dtcw.display_base_data_transform_columns_taskbar()
            display_status("New Column " + newcolname + " Added Successfully")
            

"""
#--------------------------------------------------------------------------
#    save column being deleted 
#--------------------------------------------------------------------------
""" 
def save_deleted_column(colname,fname,df) :
    
    opstat = opStatus()
    
    try :
        collist = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)[colname].tolist()
        with open(fname, 'w') as col_list_file :
            json.dump(collist,col_list_file)
                    
    except Exception as e:
        opstat.store_exception("Unable to save column being dropped ",e)

    return(opstat)

"""
#--------------------------------------------------------------------------
#    drop column 
#--------------------------------------------------------------------------
"""     
def process_drop_column(colname,parms,display=True) :
    
    opstat = opStatus()
    fparms = dtcw.get_drop_column_inputs(parms)
    
    if(len(fparms) > 0) :
        fname = fparms[0]
    else :
        fname = None
        
    if(not (fname == None))  :
        
        opstat = save_deleted_column(colname,fname,cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF))
        
        if(not opstat.get_status()) :
            display_exception(opstat)
            
    if(opstat.get_status()) :
        
        try :
            tdf     =   cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF).drop([colname],axis=1)
            cfg.set_current_dfc_dataframe(tdf)
            
        except Exception as e:
            opstat.store_exception("Drop Columns Error",e)
            display_exception(opstat)
    
    if(opstat.get_status()) : 

        if(display) :
            
            #make scriptable
            add_to_script(["# drop column " + colname,
                           "from dfcleanser.data_transform.data_transform_columns_widgets import process_drop_column",
                           "process_drop_column(" + single_quote(colname) + "," + json.dumps(parms) + ",False)"],opstat)
            
            clear_output()
            dtcw.display_base_data_transform_columns_taskbar()
            display_status("Column " + colname + " dropped Successfully")

 
"""
#--------------------------------------------------------------------------
#    save column 
#--------------------------------------------------------------------------
""" 
def process_save_column(colname,parms,display=True) :
    
    opstat = opStatus()
    fparms = dtcw.get_save_column_inputs(parms)
    
    if(len(fparms) > 0) :
        fname = fparms[0]
    else :
        fname = None
        
    if(not (fname == None))  :
    
        try :
            collist = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)[colname].tolist()
            with open(fname, 'w') as col_list_file :
                json.dump(collist,col_list_file)
                    
        except Exception as e:
            opstat.store_exception("Unable to save column being dropped ",e)
    
    if(opstat.get_status()) :
        
        if(display) :
            
            #make scriptable
            add_to_script(["# save column " + colname,
                           "from dfcleanser.data_transform.data_transform_columns_widgets import process_save_column",
                           "process_save_column(" + single_quote(colname) + "," + json.dumps(parms) + ",False)"],opstat)
            clear_output()
            dtcw.display_base_data_transform_columns_taskbar()
            display_status("Column " + colname + " Saved Successfully")

    return(opstat)

    
"""
#--------------------------------------------------------------------------
#    reorder columns 
#--------------------------------------------------------------------------
"""      
def process_reorder_columns(parms,display=True) :
    
    opstat  =    opStatus()
    fparms  =    dtcw.get_reorder_column_inputs(parms)

    movecol         = fparms[0]
    moveaftercol    = fparms[1]

    df_cols     = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF).columns.tolist() 
    
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
        cfg.set_current_dfc_dataframe(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)[final_cols])       
        
    except Exception as e:
        opstat.store_exception("Reorder Columns Error",e)
        display_exception(opstat)

    if(opstat.get_status()) :
        
        if(display) :
            
            #make scriptable
            add_to_script(["# reorder columns ",
                           "from dfcleanser.data_transform.data_transform_columns_widgets import process_reorder_columns",
                           "process_reorder_columns(" + json.dumps(parms) + ",False)"],opstat)
            
            clear_output()
            dtcw.display_base_data_transform_columns_taskbar()
            display_status("Column " + movecol + " moved Successfully")

    
"""
#--------------------------------------------------------------------------
#    reorder columns 
#--------------------------------------------------------------------------
"""      
def process_copy_column(parms,display=True) :
    
    opstat  =   opStatus()
    fparms  =   dtcw.get_copy_column_inputs(parms)
    
    copytocol      = fparms[0]
    copyfromcol    = fparms[1]

    try : 
        df = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
        df[copytocol] = df[copyfromcol]
        cfg.set_current_dfc_dataframe(df)       
        
    except Exception as e:
        opstat.store_exception("Reorder Columns Error",e)
        display_exception(opstat)

    if(opstat.get_status()) :
        
        if(display) :
            
            #make scriptable
            add_to_script(["# copy column ",
                           "from dfcleanser.data_transform.data_transform_columns_widgets import process_copy_column",
                           "process_copy_column(" + json.dumps(parms) + ",False)"],opstat)
            
            clear_output()
            dtcw.display_base_data_transform_columns_taskbar()
            display_status("Column " + copyfromcol + " copied to " + copytocol + " Successfully")


"""
#--------------------------------------------------------------------------
#    sort by column 
#--------------------------------------------------------------------------
"""      
def process_sort_by_column(parms,display=True) :
    
    opstat  =   opStatus()

    fparms      =   dtcw.get_sort_by_column_inputs(parms)
    coltosort   =   fparms[0]
    sortorder   =   fparms[1]
    resetrowids =   fparms[2]
    print(coltosort,sortorder,resetrowids)

    try : 
        df = cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF)
        df.sort_values(coltosort,sortorder)
        
        if(resetrowids) :
            from dfcleanser.data_transform.data_transform_dataframe_control import reset_row_ids_column
            opstat = reset_row_ids_column()
        
    except Exception as e:
        opstat.store_exception("Sort df By Column Error : "+coltosort,e)
        display_exception(opstat)
    
    if(opstat.get_status()) :
        
        if(display) :
            
            #make scriptable
            add_to_script(["# sort by column ",
                           "from dfcleanser.data_transform.data_transform_columns_widgets import process_sort_by_column",
                           "process_sort_by_column(" + json.dumps(parms) + ",False)"],opstat)
            
            clear_output()
            dtcw.display_base_data_transform_columns_taskbar()
            display_status("Column " + coltosort + " sorted successfully.")
    
    cfg.drop_config_value(dtcw.sort_column_input_id+"Parms")

"""
#--------------------------------------------------------------------------
#    apply fn to column 
#--------------------------------------------------------------------------
"""      
def process_apply_fn_to_column(parms,display=True) :
    
    opstat  =   opStatus()
    
    fparms = dtcw.get_apply_fn_to_column_inputs(parms)

    coltoapply      =   fparms[0]
    lambdaflag      =   fparms[1]
    #fnname          =   fparms[2]
    fncode          =   fparms[3]
    
    try : 
    
        if(lambdaflag == "True") :
            # strip out any commentary or blank lines in func
            while(fncode.find("#") > -1) :
                comment = fncode.find("#")
                # find the end of the line
                eol = fncode.find("\n",comment)
                fncode = fncode[eol+1:]
            
            fncode = fncode.lstrip("\n")
            
            code    =   "get_dfc_dataframe().loc[:,[" + coltoapply + "]].apply(lambda colval : " + fncode + ", axis = 0)"
            exec(code)
        else :
            cfg.set_config_value(cfg.CURRENT_COL_NAME,coltoapply)
            code = fncode
            exec(code)
            cfg.drop_config_value(cfg.CURRENT_COL_NAME)
            
    except Exception as e:
        opstat.store_exception("Apply fn to Column Error : " + coltoapply + "\n   " + code,e)
        display_exception(opstat)
    
    if(opstat.get_status()) :
        
        if(display) :
            
            #make scriptable
            add_to_script(["# apply fn to column ",
                           "from dfcleanser.data_transform.data_transform_columns_widgets import process_apply_fn_to_column",
                           "process_apply_fn_to_column(" + json.dumps(parms) + ",False)"],opstat)
            
            clear_output()
            dtcw.display_base_data_transform_columns_taskbar()
            display_status("function applied to column " + coltoapply + " successfully.")
    
    #et_dc_dataframe()[coltoapply].apply(fncode)
    cfg.drop_config_value(dtcw.apply_column_input_id+"Parms")

    
"""
#--------------------------------------------------------------------------
#    mapping transform
#--------------------------------------------------------------------------
"""
def process_map_transform(colname,parms,display=True) :
    
    opstat  =   opStatus()
    fparms  =   dtcw.get_map_column_inputs(parms)

    mapDict         = None
    map_file_name   = fparms[0]
    if(len(map_file_name) == 0) :
        map_file_name = "None"
    
    nanFlag         = fparms[1]
    if(len(nanFlag) == 0) :
        nanFlag = "False"

    # TODO check type string must have ' '    
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
                               "from dfcleanser.data_transform.data_transform_columns_widgets import process_map_transform",
                               "from dfcleanser.common.cfg import get_dfc_dataframe",
                               "process_map_transform(get_dfc_dataframe()," + single_quote(colname) + "," + json.dumps(parms) + ",False)"],opstat)
            
        else :
            display_exception(opstat)
            
    else :
        
        display_exception(opstat)
        print("\n")
        
    if(opstat.get_status()) :
        if(display) :
            dtcw.display_column_transform_status(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),colname)

"""
#--------------------------------------------------------------------------
#    dummies transform
#--------------------------------------------------------------------------
"""
def process_dummy_transform(colname,parms,display=True) :
    
    opstat  =   opStatus()
    fparms  =   dtcw.get_dummies_column_inputs(parms)

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
                           "from dfcleanser.data_transform.data_transform_column_widgets import process_dummy_transform",
                           "from dfcleanser.common.cfg import get_dfc_dataframe",
                           "process_dummy_transform(get_dfc_dataframe()," + single_quote(colname) + "," + json.dumps(parms)  + ",False)"],opstat)
        
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
                dtcw.display_column_transform_status(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),
                                                     colname)

    if(not opstat.get_status()) : 
        if(display) :
            if(not removecol) :
                dtcw.display_transform_cols_option([[colname,26]])

"""
#--------------------------------------------------------------------------
#    categorical transform
#--------------------------------------------------------------------------
"""
def process_cat_transform(colname,parms,display=True) :
    
    opstat  =   opStatus()
    fparms  =   dtcw.get_cat_column_inputs(parms)
    
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
                       "from dfcleanser.data_transform.data_transform_columns_widgets import process_cat_transform",
                       "from dfcleanser.common.cfg import get_dfc_dataframe",
                       "process_cat_transform(" +  single_quote(colname) + "," + json.dumps(parms) + ",False)"],opstat)

        labellist = [dtcw.transform_category_input_labelList[0],dtcw.transform_category_input_labelList[1]]
        valuelist = [str(makecat),str(changedatatype)]
    
        displayParms("Column " + colname + " Category Transform Parms",labellist,valuelist,cfg.DataTransform_ID)
        
        dtcw.display_column_transform_status(cfg.get_current_chapter_df(cfg.CURRENT_TRANSFORM_DF),colname)

    if(not opstat.get_status()) : 
        if(display) :
            dtcw.display_transform_cols_option([[colname,27]])
        



"""            
#------------------------------------------------------------------
#------------------------------------------------------------------
#
#   column Transform Methods
#
#------------------------------------------------------------------
#------------------------------------------------------------------
"""

"""            
#------------------------------------------------------------------
#   make a column ordinal in place using categories 
#
#   return : (NA) df is changed in place
#
#   df              -   dataframe
#   columnName      -   column name
#   reverse         -   reverse the order of the values befor categorize 
#
#------------------------------------------------------------------
"""
def make_col_categorical(df, columnName, reverse=None)  :   

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
    
"""            
#------------------------------------------------------------------
#   make a column categorical in place using dummies 
#
#   return : (NA) df is changed in place
#
#   df              -   dataframe
#   columnName      -   column name
#   removeCol       -   remove the original column 
#
#------------------------------------------------------------------
"""
def make_col_categorical_from_dummies(df, columnName, removeCol)  :   
    
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
        cfg.set_current_dfc_dataframe(df)
    
    return(opstat)

"""            
#------------------------------------------------------------------
#   make a column categorical in place using map 
#
#   return : (NA) df is changed in place
#
#   df              -   dataframe
#   columnName      -   column name
#   cmpa            -   column value map
#                       ( {'Man': 0, 'Woman': 1} )
#
#   handleNA        -   how to handle nas
#                       'ignore' - ignore errors
#                       None     - no handling at all 
#
#------------------------------------------------------------------
"""
def make_col_categorical_from_map(df, columnName, cmap, handleNA)  :   

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
    cfg.drop_config_value(dtcw.add_column_input_id+"Parms")
    cfg.drop_config_value(dtcw.add_column_input_id+"ParmsProtect")
    cfg.drop_config_value(dtcw.add_column_file_input_id+"Parms")
    cfg.drop_config_value(dtcw.add_column_file_input_id+"ParmsProtect")
    cfg.drop_config_value(dtcw.add_column_code_input_id+"Parms")
    cfg.drop_config_value(dtcw.add_column_code_input_id+"ParmsProtect")
    cfg.drop_config_value(dtcw.reorder_columns_input_id+"Parms")
    cfg.drop_config_value(dtcw.reorder_columns_input_id+"ParmsProtect")
    cfg.drop_config_value(dtcw.sort_column_input_id+"Parms")
    cfg.drop_config_value(dtcw.sort_column_input_id+"ParmsProtect")
    cfg.drop_config_value(dtcw.apply_column_input_id+"Parms")
    cfg.drop_config_value(dtcw.apply_column_input_id+"ParmsProtect")
    
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
    


    