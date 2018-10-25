"""
# data_cleansing_control 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

from dfcleanser.scripting.data_scripting_control import add_to_script

import dfcleanser.common.cfg as cfg 
import dfcleanser.data_cleansing.data_cleansing_widgets as dcw
import dfcleanser.data_cleansing.data_cleansing_model as dcm

from dfcleanser.common.common_utils import (RunningClock, display_status, display_exception, 
                                            opStatus, single_quote, is_numeric_col, is_numeric_col_int)

from dfcleanser.common.html_widgets import (displayHeading)
from dfcleanser.common.table_widgets import (dcTable, drop_owner_tables)
from dfcleanser.common.display_utils import (display_df_describe) 

from IPython.display import clear_output



"""            
#------------------------------------------------------------------
#   main data cleansing processing
#
#   option  -   display option
#   parms   -   associated parms 
#
#------------------------------------------------------------------
"""
def display_data_cleansing(option,parms=None) :
    
    clear_output()
    
    if(not cfg.check_if_dc_init()) :
        dcw.display_no_data_heading()
        return
    
    # setup the button bar form
    dcw.display_data_cleansing_main_taskbar()
    
    if(cfg.is_dc_dataframe_loaded()) :
        
        cfg.set_config_value(cfg.DATA_TYPES_FLAG_KEY,False)

        if(option == dcm.MAIN_OPTION) :
            from dfcleanser.data_inspection.data_inspection_widgets import display_inspection_data
            display_inspection_data()
            clear_data_cleansing_data()
            
        elif(option == dcm.CHANGE_COLUMN_OPTION) :

            displayHeading("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Changing Column Values",4)
            clock = RunningClock()
            clock.start()
            
            opstat = change_unique_col_data(cfg.get_dc_dataframe(),parms)
            cfg.drop_config_value(cfg.UNIQUES_RANGE_KEY)
            
            clock.stop()
            
            if(opstat.get_status()) :
                display_status("Column " + cfg.get_config_value(cfg.CLEANSING_COL_KEY) + " values changed successfully")
            else :
                display_exception(opstat)                
            
            dcw.display_col_data()
            
        elif(option == dcm.FIND_COLUMN_OPTION) :
            cfg.set_config_value(cfg.UNIQUES_RANGE_KEY,parms)
            dcw.display_col_data()
            
        elif(option == dcm.DISPLAY_COLS_OPTION) :
            cfg.drop_config_value(cfg.OUTLIERS_FLAG_KEY)
            cfg.drop_config_value(cfg.UNIQUES_FLAG_KEY)
            cfg.drop_config_value(cfg.DATA_TYPES_FLAG_KEY)            
            cfg.drop_config_value(cfg.ROUNDING_FLAG_KEY)
            
            cfg.drop_config_value(cfg.CLEANSING_COL_KEY)
            cfg.drop_config_value(cfg.CLEANSING_ROW_KEY)
            cfg.drop_config_value(cfg.OBJ_TYPE_PARM_KEY)
            
            funcid = int(parms[0])
            
            if(funcid == 0) :
                
                displayHeading("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Numeric Columns",4)
                
                clock = RunningClock()
                clock.start()

                try :
                    num_col_names_table = dcTable("Numeric Column Names ",
                                                  "dcgendfdesc",
                                                  cfg.DataCleansing_ID)
                    
                    display_df_describe(cfg.get_dc_dataframe(),num_col_names_table)
                
                except Exception as e: 
                    opstat = opStatus()
                    opstat.store_exception("Unable to display numeric column names",e)
                    display_exception(opstat)

                clock.stop()

            elif(funcid == 1) :
                
                displayHeading("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Non Numeric Columns",4)
                
                clock = RunningClock()
                clock.start()

                try :
                    nn_col_names_table  = dcTable("Non Numeric Column Names ",
                                                  "dcnngendfdesc",
                                                  cfg.DataCleansing_ID)
                    
                    df_cols             =   cfg.get_dc_dataframe().columns.tolist()
                    df_cols.sort()
                    dcw.display_non_numeric_df_describe(cfg.get_dc_dataframe(),
                                                        nn_col_names_table,None,None) 
                    
                except Exception as e:
                    opstat = opStatus()
                    opstat.store_exception("Unable to display non numeric column names",e)
                    display_exception(opstat)

                clock.stop()
                    
            elif(funcid == 2) :
                cfg.set_config_value(cfg.CLEANSING_ROW_KEY,0)
                dcw.display_row_data(cfg.get_dc_dataframe(),0,0)
    
            elif(funcid == 3) :
                return()
                
            elif(funcid == 4) :
                displayHeading("Auto Cleanse",4)
            
        elif(option == dcm.DISPLAY_ROW_OPTION) :
            
            rowid = int(parms)
            cfg.set_config_value(cfg.CLEANSING_ROW_KEY,parms)
            dcw.display_row_data(cfg.get_dc_dataframe(),rowid,0)
            
        elif(option == dcm.GENERIC_COL_OPTION) :
            
            cfg.drop_config_value(cfg.OUTLIERS_FLAG_KEY)
            cfg.drop_config_value(cfg.UNIQUES_FLAG_KEY)
            cfg.drop_config_value(cfg.ROUNDING_FLAG_KEY)

            if(parms != None) :
                cfg.set_config_value(cfg.CLEANSING_COL_KEY,parms)

            dcw.display_col_data()
    
        elif(option == dcm.ALL_COL_OPTION) :
            
            cfg.drop_config_value(cfg.OUTLIERS_FLAG_KEY)
            cfg.set_config_value(cfg.UNIQUES_FLAG_KEY, True)
            dcw.display_numeric_col_data(cfg.get_dc_dataframe())

        elif(option == dcm.DROP_COL_OPTION ) : 
            
            opstat = drop_column(cfg.get_config_value(cfg.CLEANSING_COL_KEY))
            
            clear_output()
            
            # setup the button bar form
            dcw.display_data_cleansing_main_taskbar()
            
            if(opstat.get_status()) :
                display_status("Column " + cfg.get_config_value(cfg.CLEANSING_COL_KEY) + " dropped successfully")
                cfg.drop_config_value(cfg.CLEANSING_COL_KEY)
            else :
                display_exception(opstat)                
            
            display_inspection_data()

        elif(option == dcm.DROP_ROWS_OPTION ) : 
                
            displayHeading("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dropping Rows",4)
                
            clock = RunningClock()
            clock.start()
            
            opstat = drop_value_rows(cfg.get_dc_dataframe(),
                                     cfg.get_config_value(cfg.CLEANSING_COL_KEY),
                                     parms[1])
            
            clock.stop()
            
            if(opstat.get_status()) :
                display_status("Rows dropped successfully")
            else :
                display_exception(opstat)                
            
            dcw.display_col_data()

        elif(option == dcm.DROP_COL_NANS_OPTION ) :
            
            displayHeading("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dropping Column Nans",4)
                
            clock = RunningClock()
            clock.start()
            
            opstat = drop_col_nans(cfg.get_dc_dataframe(),cfg.get_config_value(cfg.CLEANSING_COL_KEY))
            
            clock.stop()
            
            if(opstat.get_status()) :
                display_status("Column nan rows dropped successfully")
            else :
                display_exception(opstat)                
            
            dcw.display_col_data()
            
        elif(option == dcm.DISPLAY_OUTLIERS_OPTION ) : 
            
            cfg.set_config_value(cfg.OUTLIERS_FLAG_KEY, True)
            dcw.display_numeric_col_data(cfg.get_dc_dataframe())
            
        elif(option ==  dcm.DISPLAY_ROUND_COLUMN_OPTION  ) : 
            
            cfg.set_config_value(cfg.ROUNDING_FLAG_KEY,True)
            dcw.display_col_data()
        
        elif(option ==  dcm.PROCESS_ROUND_COLUMN_OPTION  ) :
            
            displayHeading("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Rounding Column Data",4)
                
            clock = RunningClock()
            clock.start()
            
            opstat = round_column_data(cfg.get_dc_dataframe(),parms)
            
            clock.stop()
            
            if(opstat.get_status()) :
                display_status("Column " + cfg.get_config_value(cfg.CLEANSING_COL_KEY) + "rounded successfully")
                cfg.set_config_value(cfg.ROUNDING_FLAG_KEY,False)
            else :
                display_exception(opstat)                
            
            dcw.display_col_data()
            
        elif(option ==  dcm.DISPLAY_COL_CHANGE_OPTION  ) :
            
            cfg.set_config_value(cfg.ROUNDING_FLAG_KEY,False)
            dcw.display_col_data()
            
        elif(option ==  dcm.DISPLAY_OBJECTS_COLS_OPTION  ) :
            #deprecated
            print("DISPLAY_OBJECTS_COLS_OPTION")
            
        elif(option ==  dcm.REMOVE_WHITESPACE_OPTION  ) :
            
            displayHeading("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Removing Column Whitespace",4)
                
            clock = RunningClock()
            clock.start()
            
            opstat = remove_whitespace(cfg.get_dc_dataframe(),parms)
            
            clock.stop()
            
            if(opstat.get_status()) :
                display_status("Column " + cfg.get_config_value(cfg.CLEANSING_COL_KEY) + " whitespace removed successfully")
            else :
                display_exception(opstat)                
            
            dcw.display_col_data()

        elif(option ==  dcm.DISPLAY_GRAPHS_OPTION  ) :
            
            cfg.set_config_value(cfg.GRAPHS_FLAG_KEY,True)
            dcw.display_numeric_col_data(cfg.get_dc_dataframe())
            
        elif(option ==  dcm.DISPLAY_UNIQUES_OPTION  ) :
            
            cfg.set_config_value(cfg.UNIQUES_FLAG_KEY, True)
            dcw.display_numeric_col_data(cfg.get_dc_dataframe())
            
        elif(option ==  dcm.DISPLAY_NEW_ROW) :

            rowid = int(parms)
            cfg.set_config_value(cfg.CLEANSING_ROW_KEY,parms)
            cfg.set_config_value(cfg.CLEANSING_COL_KEY,0)
            dcw.display_row_data(cfg.get_dc_dataframe(),rowid,0)

        elif(option ==  dcm.UPDATE_ROW_COL) :
            
            colname     =   parms
            rowid       =   int(cfg.get_config_value(cfg.CLEANSING_ROW_KEY))
            
            column_names = list(cfg.get_dc_dataframe().columns.values)
            found = -1
            for i in range(len(column_names)) :
                if(column_names[i] == colname) :
                    found = i
            if(found > 0) :
                colid = found
            cfg.set_config_value(cfg.CLEANSING_COL_KEY,colid)
            
            chval = cfg.get_dc_dataframe().iloc[rowid,colid]

            cfg.set_config_value(dcw.change_row_values_input_id + "Parms",[chval,""])           
            dcw.display_row_data(cfg.get_dc_dataframe(),rowid,0)

        elif(option ==  dcm.PROCESS_ROW_COL) :
            
            func_id     =   parms[0]
            row_id      =   int(cfg.get_config_value(cfg.CLEANSING_ROW_KEY))
            
            cfg.drop_config_value(dcw.change_row_values_input_id + "Parms")           
            
            if(func_id == 0) :
                
                fparms      =   dcw.get_change_row_values_inputs(parms)
                new_value   =   fparms[1]
                
                col_id      =   int(cfg.get_config_value(cfg.CLEANSING_COL_KEY))
                
                if(is_numeric_col(cfg.get_dc_dataframe(), col_id)) :
                    if(is_numeric_col_int(cfg.get_dc_dataframe(), col_id)) :
                        new_value       =   int(new_value)
                    else :
                        new_value       =   float(new_value)
                
                if(len(new_value) > 0) :
                    cfg.get_dc_dataframe().iloc[row_id,col_id] = new_value

                dcw.display_row_data(cfg.get_dc_dataframe(),row_id,0)
                
            elif(func_id == 1) :
                drop_row(cfg.get_dc_dataframe(),row_id)
                dcw.display_row_data(cfg.get_dc_dataframe(),0,0)
                
    else :
        
        from dfcleanser.data_inspection.data_inspection_widgets import display_inspection_data
        display_inspection_data()

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    data cleansing process data functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
"""            
#------------------------------------------------------------------
#   drop a specific col  
#
#   colname         -   column to drop 
#   display         -   true  : add to script log : 
#                       false : running from script log 
#
#------------------------------------------------------------------
"""
def     drop_column(colname,display=True) :
    
    droplist    =   []
    droplist.append(colname)
    
    df = cfg.get_dc_dataframe()
    
    opstat = opStatus()
    
    try :
        df.drop(droplist,axis=1,inplace=True)
        
        if(display) :
            #make scriptable
            add_to_script(["# Drop Column " + colname,
                           "from data_cleansing_widgets drop_column",
                           "drop_column(" + single_quote(colname)  +")"],opstat)
        
    except Exception as e:
        opstat.store_exception("Unable to drop column " + cfg.get_config_value(cfg.CLEANSING_COL_KEY),e)
        
    return(opstat)


"""            
#------------------------------------------------------------------
#   drop rows for column value  
#
#   df              -   dataframe
#   colname         -   column to drop 
#   value           -   column value to match
#   display         -   true  : add to script log : 
#                       false : running from script log 
#
#------------------------------------------------------------------
"""   
def     drop_value_rows(df,colname,value,display=True) :
    
    opstat      =   opStatus()
    
    if(value == "nan") :

        df.dropna(subset=[colname],inplace=True)
        df.reset_index(inplace=True)
        
    else :
        
        droplist    =   []
        
        #TODO change using indexer
        dfcoldata = df[colname].tolist()
        isnumeric = is_numeric_col(df,colname)
    
        for i in range(len(dfcoldata)) :
            if(isnumeric) :
                if(str(dfcoldata[i]) == value) :
                    droplist.append(i)
            else :
                if(dfcoldata[i] == value) :
                    droplist.append(i)    

        if(len(droplist) > 0) :
        
            try :
                df.drop(droplist,axis=0,inplace=True)
                df.reset_index(inplace=True)
            
                if(display) :
                    #make scriptable
                    add_to_script(["# Drop Values ",
                                   "from dfcleanser.data_cleansing.data_cleansing_widgets import drop_value_rows",
                                   "drop_value_rows(get_dc_dataframe()," + single_quote(colname) + "," + str(value) +")"],opstat)

            except Exception as e:
                opstat.store_exception("Unable to drop row values ",e)

    return(opstat)


"""            
#------------------------------------------------------------------
#   drop column nans  
#
#   df              -   dataframe
#   colname         -   column to drop 
#
#------------------------------------------------------------------
"""   
def     drop_col_nans(df,colname) :

    opstat = opStatus()
    opstat = drop_value_rows(df,colname,"nan")

    return(opstat)

"""            
#------------------------------------------------------------------
#   drop a specific row  
#
#   df              -   dataframe
#   rowid           -   row to drop 
#   display         -   true  : add to script log : 
#                       false : running from script log 
#
#------------------------------------------------------------------
"""
def     drop_row(df,rowid,display=True) :

    opstat = opStatus()
    
    try :     
        df.drop(df.index[int(rowid)],inplace=True)
        
        if(display) :
            #make scriptable
            add_to_script(["# Drop Row " + str(rowid),
                           "from data_cleansing_widgets drop_row",
                           "drop_row(get_dc_dataframe()," + str(rowid) +")"],opstat)
        
    except Exception as e:
        opstat.store_exception("Unable to drop rowid  " + str(rowid),e)

    return(opstat)
 
"""            
#------------------------------------------------------------------
#   round a column  
#
#   df              -   dataframe
#   parms           -   list of parms
#                          parm[0]  colname
#                          parm[1]  number of decimals
#   display         -   true  : add to script log : 
#                       false : running from script log 
#
#------------------------------------------------------------------
"""   
def round_column_data(df,parms,display=True) :

    
    colname = parms[0]
    accuracy = int(parms[1])
    rounds = {colname: accuracy}
    
    opstat = opStatus()
    
    try :     

        df = df.round(rounds)
        cfg.set_dc_dataframe(df)
        
        if(display) :
            #make scriptable
            import json
            add_to_script(["# Round Column ",
                           "from data_cleansing_widgets round_column_data",
                           "round_column_data(get_dc_dataframe()," + json.dumps(parms) +")"],opstat)

    except Exception as e:
        opstat.store_exception("Unable to round  " + colname,e)

    return(opstat)

"""            
#------------------------------------------------------------------
#   remove leading and trailing blanks and tabs  
#
#   df              -   dataframe
#   colname         -   column name
#   display         -   true  : add to script log : 
#                       false : running from script log 
#------------------------------------------------------------------
""" 
def remove_whitespace(df,colname,display=True) :
    
    dfcolnames = df.columns.values.tolist()
    for i in range(len(dfcolnames)) :
        if(dfcolnames[i] == colname) :
            colindex = i
    
    opstat = opStatus()
    
    try :     

        for i in range(len(df)) :
        
            cvalue = str(df.iloc[i,colindex]) 
            nvalue = cvalue.strip()
            nvalue = nvalue.strip("\t")
            nvalue = cvalue.strip()
        
            if(len(cvalue) != len(nvalue)) :
                df.iloc[i,colindex] = nvalue 
                
        if(display) :       
            #make scriptable
            add_to_script(["# Remove Whitespace for " + colname,
                           "from data_cleansing_widgets remove_whitespace",
                           "remove_whitespace(get_dc_dataframe()," + single_quote(colname) +",False)"],opstat)
                
    except Exception as e:
        opstat.store_exception("Unable to remove whitespace from  " + colname,e)

    return(opstat)
                
"""            
#------------------------------------------------------------------
#   change unique vals for a column
#
#   df              -   dataframe
#   parms           -   associated col parms 
#   display         -   true  : add to script log : 
#                       false : running from script log 
#------------------------------------------------------------------
"""
def change_unique_col_data(df,parms,display=True) :

    opstat = opStatus()

    if(type(parms) != str) :

        colname     =   parms[0]
        changefrom  =   parms[1]
        changeto    =   parms[2]

        if(changefrom == 'nan') :

            try :
                if(is_numeric_col(df,colname)) :
                    if(is_numeric_col_int(df,colname)) :
                        toval       =   int(changeto)
                    else :
                        toval       =   float(changeto)
                else :
                    toval       =   changeto
                    
                df = df.fillna({colname : toval})
                cfg.set_dc_dataframe(df)
                
            except Exception as e :
                opstat.store_exception("Unable to change value for " + colname,e) 
                
        else :
            try     :
                if(is_numeric_col(df,colname)) :
                    if(is_numeric_col_int(df,colname)) :
                        fromval     =   int(changefrom)
                        toval       =   int(changeto)
                    else :
                        fromval     =   float(changefrom)
                        toval       =   float(changeto)
                else :
                    fromval     =   changefrom
                    toval       =   changeto   

                criteria        =   df[colname] == fromval    
                df[criteria]    =   toval
                cfg.set_dc_dataframe(df)
            except Exception as e :
                opstat.store_exception("Unable to change value for " + colname,e)            
        
    if(opstat.get_status()) :
        
        if(display) :
            #make scriptable
            add_to_script(["# Change Unique Column Data ",
                           "from dfcleanser.data_cleansing.data_cleansing_widgets import change_unique_col_data",
                           "from dfcleanser.common.cfg import get_dc_dataframe",
                           "change_unique_col_data(get_dc_dataframe()," + str(parms) +",False)"],opstat)

    return(opstat)  
   
   
"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   general housekeeping functions
#------------------------------------------------------------------
#------------------------------------------------------------------
""" 
def clear_data_cleansing_data() :
    
    drop_owner_tables(cfg.DataCleansing_ID)
    clear_data_cleansing_cfg_values()
    
def clear_data_cleansing_cfg_values() :
 
    cfg.drop_config_value(cfg.UNIQUES_FLAG_KEY)
    cfg.drop_config_value(cfg.UNIQUES_RANGE_KEY)
    cfg.drop_config_value(cfg.OUTLIERS_FLAG_KEY)
    cfg.drop_config_value(cfg.DATA_TYPES_FLAG_KEY)
    cfg.drop_config_value(cfg.ROUNDING_FLAG_KEY)
    cfg.drop_config_value(cfg.GRAPHS_FLAG_KEY)
    
    cfg.drop_config_value(cfg.CLEANSING_COL_KEY)
    cfg.drop_config_value(cfg.CLEANSING_ROW_KEY)
    
    cfg.drop_config_value(cfg.OBJ_TYPE_PARM_KEY)
    cfg.drop_config_value(cfg.OBJ_DATA_TYPES_FLAG_KEY)
    cfg.drop_config_value(cfg.OBJ_ROUNDING_FLAG_KEY)

    cfg.drop_config_value("changerowinputParms")
        

