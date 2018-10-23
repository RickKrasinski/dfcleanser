"""
# data_inspection_controller 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg
import dfcleanser.data_inspection.data_inspection_model as dim
import dfcleanser.data_inspection.data_inspection_widgets as diw

import dfcleanser.common.help_utils as dfchelp

from dfcleanser.common.table_widgets import drop_owner_tables, dcTable

from dfcleanser.common.html_widgets import displayHeading, display_composite_form

from dfcleanser.scripting.data_scripting_control import add_to_script

from dfcleanser.common.common_utils import (RunningClock, opStatus, display_exception)

from dfcleanser.common.display_utils import (get_df_datatypes_data, display_more_sample_rows,
                                             display_column_names, display_df_describe)

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    data inspection process data functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


def display_data_inspection(id, parms=None) :
    
    from IPython.display import clear_output
    clear_output()

    opstat  =   opStatus()  
      
    # setup the button bar form
    inspection_tbForm   =   diw.get_inspection_main_taskbar()

    # setup the checkbox form 
    current_checkboxes      =  []
    newrowId                =   0
    tableId                 =   ""
    
    # display the default insoection data
    if(id == dim.MAIN_OPTION) :
        current_checkboxes     =   [False, False, False, False, False] 
        clear_data_inspection_data()
        dfchelp.clear_help_text(dfchelp.INSPECT_HELP_BASE)
        
    # refresh the current insoection data     
    elif (id == dim.REFRESH_OPTION) : 
        
        # check if parms have checkbox flags
        if(not(parms==None)) :
            for i in range(len(parms)) :
                if(parms[i] == "True") :   
                    current_checkboxes.append(True)
                else :
                    current_checkboxes.append(False)
        
        # no checkbox parms so read from cfg file
        else :
            parms = []
            diw.get_inspection_check_form_parms(parms,current_checkboxes)           
                
    else :

        inparm = parms
        parms = []
        diw.get_inspection_check_form_parms(parms,current_checkboxes)           
        
    
    inspection_checkboxForm =   diw.get_main_checkbox_form(current_checkboxes) 
    display_composite_form([inspection_tbForm,inspection_checkboxForm])
    
    import matplotlib.pyplot as plt
    
    # parse the input parms
    if( (id == dim.DISPLAY_ROW_OPTION) or 
        (id == dim.DROP_ROWS_OPTION) or 
        (id == dim.DROP_COLS_OPTION) ) :
        
        if( id == dim.DISPLAY_ROW_OPTION ) :
            rowid = inparm
        else :
            
            thresholdType = inparm[0]
            
            if(id == dim.DROP_ROWS_OPTION) :
                fparms = diw.get_drop_rows_input_parms(inparm[1])
            else :
                fparms = diw.get_drop_cols_input_parms(inparm[1])
                
            threshold = int(fparms[0])
            
        parms = diw.get_drop_cbox_flags()
        parms = []
        
        if( id == dim.DISPLAY_ROW_OPTION ) :
            parms.append(rowid)
        
        if (id == dim.DROP_ROWS_OPTION) :
            
            drop_nan_rows(cfg.get_dc_dataframe(),threshold,thresholdType,opstat)
            
            if(not(opstat.get_status())) :
                display_exception(opstat)    
            
        if (id == dim.DROP_COLS_OPTION) :
            
            drop_nan_cols(cfg.get_dc_dataframe(),threshold,thresholdType,opstat) 
            
            if(not(opstat.get_status())) :
                display_exception(opstat)   
                
    if(opstat.get_status()) :
        diw.display_inspection_data()

    if( (id == dim.REFRESH_OPTION)   or (id == dim.DISPLAY_ROW_OPTION) or 
        (id == dim.DROP_ROWS_OPTION) or (id == dim.DROP_COLS_OPTION) ) :

        if(cfg.is_dc_dataframe_loaded()) :

            clock = RunningClock()
            clock.start()

            df_data_info = get_df_datatypes_data(cfg.get_dc_dataframe())

            clock.stop() 
            
            # if display data types
            if(parms[dim.INSPECT_DATATYPES] == "True") : 
                
                cfg.set_config_value(cfg.DATA_TYPES_CBOX_0_KEY,"True")
                
                displayHeading("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Data Types",2)
                print("\n")
                
                data_types_table = dcTable("Column Data Types",
                                           "datatypesTable",
                                           cfg.DataInspection_ID)

                diw.display_df_datatypes(data_types_table,df_data_info[0],df_data_info[1],df_data_info[2]) 
                
                print("\n")
                
                import matplotlib.pyplot as plt
                import numpy as np

                font =  {'fontsize': 14 }
                font2 = {'fontsize': 18 }
                
                objects = []
                for i in range(len(df_data_info[0])) :
                    ttype = str(df_data_info[0][i]) 
                    ttype = ttype.replace("datetime.","")
                    ttype = ttype.replace("datetime64[ns]","datetime")
                    ttype = ttype.replace("timedelta64[ns]","timedelta")
                    objects.append(ttype)    
                y_pos = np.arange(len(objects))
                
                plt.bar(y_pos, df_data_info[1], align='center', alpha=0.5, color='#428bca')
                plt.xticks(y_pos, objects,rotation='vertical')
                plt.ylabel('Type Counts',fontdict=font)
                plt.xlabel('Data Types',fontdict=font)
                plt.title('Column Data Types',fontdict=font2)
 
                plt.show()
                
                print("\n")
                
                display_composite_form([diw.get_inspection_dfschema_taskbar()])
                print("\n")
                
            # if display nan data
            if(parms[dim.INSPECT_NANS] == "True") : 
                
                cfg.set_config_value(cfg.NANS_CBOX_1_KEY,"True")
                    
                displayHeading("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NaNs",2)
                #print("\n")
                
                nans_rows_table = dcTable("Rows with most NaNs","nansrowTable",cfg.DataInspection_ID)
                nans_cols_table = dcTable("Columns with most NaNs","nansTable",cfg.DataInspection_ID)
                diw.display_null_data(cfg.get_dc_dataframe(),nans_rows_table,nans_cols_table,120)
            
            # if display sample row data
            if(parms[dim.INSPECT_ROWS] == "True") : 
                
                opstat = opStatus
                
                cfg.set_config_value(cfg.ROWS_CBOX_2_KEY,"True")
                print("\n")
                displayHeading("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Row Data",2)
                
                rows_table = dcTable("Start Row","DIsamplerows",cfg.DataInspection_ID)
        
                if(id == 2) :
                    opstat = diw.display_df_row_data(cfg.get_dc_dataframe(),rows_table,rowid,0)
                else : 
                    if(newrowId==0) :
                        opstat = diw.display_df_row_data(cfg.get_dc_dataframe(),rows_table,0,0)
                    else :
                        opstat = display_more_sample_rows(cfg.get_dc_dataframe(),tableId,1,newrowId)
            
                if(not opstat.get_status()) :
                    display_exception(opstat)
                    
            #if display column data
            if(parms[dim.INSPECT_COLS] == "True") : 
                
                cfg.set_config_value(cfg.COLS_CBOX_3_KEY,"True")
                print("\n")
                displayHeading("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Column Data",2)
                
                clock = RunningClock()
                clock.start()
                
                col_names_table = dcTable("Column Names ","cnamesTable",cfg.DataInspection_ID)
                display_column_names(cfg.get_dc_dataframe(),col_names_table,"scol")
                
                print("\n")
                num_col_names_table = dcTable("Numeric Column Names ","gendfdesc",cfg.DataInspection_ID)
                display_df_describe(cfg.get_dc_dataframe(),num_col_names_table)
                
                clock.stop()

            #if display categories data
            if(parms[dim.INSPECT_CATS] == "True") : 
                
                cfg.set_config_value(cfg.CATS_CBOX_4_KEY,"True")
                print("\n")
                displayHeading("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Categories",2)
                
                clock = RunningClock()
                clock.start()

                cattable = dcTable("Category Columns",
                                   "catcolsTable",
                                   cfg.DataInspection_ID)

                catcandidatetable = dcTable("Category Candidate Columns",
                                            "catcandcolsTable",
                                            cfg.DataInspection_ID)
                
                numcats, numcands = diw.display_df_categories(cfg.get_dc_dataframe(),cattable,catcandidatetable)
                
                clock.stop()


"""            
#------------------------------------------------------------------
#   drop rows with nans greater than threshold 
#
#   df        -   dataframe
#   threshold -   threshold 
#
#------------------------------------------------------------------
"""
def drop_nan_rows(df,threshold,ttype,opstat,display=True) :
    
    if(display) :
            
        clock = RunningClock()
        clock.start()
        

    try     :
        if(ttype == dim.BY_PERCENT) : 
            thold   =   len(df.columns) * (float(threshold) * 0.01)
        else :
            thold   =   float(threshold)
     
        criteria = df.isnull().sum(axis=1) < thold

        df = df[criteria]
        cfg.set_dc_dataframe(df)

    except Exception as e:
        opstat.store_exception("Error droppint nan rows\n ",e)

    if(display) :
        clock.stop()
        
        #make scriptable
        add_to_script(["# Drop NAN Rows ",
                       "from dfcleanser.data_inspection.data_inspection_widgets import drop_nan_rows",
                       "drop_nan_rows(" + str(threshold) + ",False)"],opstat)

"""            
#------------------------------------------------------------------
#   drop cols with nans greater than threshold 
#
#   df        -   dataframe
#   threshold -   threshold 
#
#------------------------------------------------------------------
"""
def drop_nan_cols(df,threshold,ttype,opstat,display=True) :
    
    if(display) :
            
        clock = RunningClock()
        clock.start()

    try     :
        
        if(ttype == dim.BY_PERCENT) : 
            thold   =   len(df) * (float(threshold) * 0.01)
        else :
            thold   =   float(threshold)

        df_cols         =   df.columns
        colswithnulls   =   df.isnull().sum()
        droplist        =   []
    
        for i in range(len(colswithnulls)) :
            if(colswithnulls[i] >= thold) :
                droplist.append(df_cols[i])

        if(len(droplist) > 0) :
            df.drop(droplist,axis=1,inplace=True)

    except Exception as e:
        opstat.store_exception("Error droppint nan rows\n ",e)

    if(display) :
        
        clock.stop()
        
        #make scriptable try catch
        add_to_script(["# Drop NAN Cols ",
                       "from dfcleanser.data_inspection.data_inspection_widgets import drop_nan_cols",
                       "drop_nan_cols(" + str(threshold) + ",False)"],opstat)

"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   general housekeeping functions
#------------------------------------------------------------------
#------------------------------------------------------------------
"""       
def clear_data_inspection_data() :
    
    drop_owner_tables(cfg.DataInspection_ID)
    clear_data_inspection_cfg_values()
    
def clear_data_inspection_cfg_values() :
    
    cfg.drop_config_value(cfg.DATA_TYPES_CBOX_0_KEY)
    cfg.drop_config_value(cfg.NANS_CBOX_1_KEY)
    cfg.drop_config_value(cfg.ROWS_CBOX_2_KEY)
    cfg.drop_config_value(cfg.COLS_CBOX_3_KEY)
    cfg.drop_config_value(cfg.CATS_CBOX_4_KEY)



