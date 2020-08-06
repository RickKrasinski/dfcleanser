"""
# sw_utility_dfsubset_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""

import sys
this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg
import dfcleanser.sw_utilities.sw_utility_dfsubset_model as swsm
import dfcleanser.sw_utilities.sw_utility_dfsubset_widgets as swsw


from dfcleanser.common.table_widgets import drop_owner_tables
#from dfcleanser.common.html_widgets import new_line

from dfcleanser.common.common_utils import (display_exception, display_status, opStatus, get_parms_for_input, RunningClock)


DEBUG_SUBSET     =   False
    

   
"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   main taskbar and route function
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_subset_df() :
    return(cfg.get_current_chapter_df(cfg.SWDFSubsetUtility_ID))


def get_current_subset_df(parms) :
    
    fparms          =   get_parms_for_input(parms[0],["dsdfdataframe"])
    if(len(fparms) > 0) :
        selected_df     =   fparms[0]
            
            
        if(not (len(selected_df) == 0) ) :
            cfg.set_config_value(cfg.CURRENT_SUBSET_DF,selected_df)


def drop_add_cols(col_names,col_action,df) :
    """
    * ---------------------------------------------------------
    * function : main geocode process function
    * 
    * parms :
    *  col_names    - column names list
    *  col_action   - keep or drop flag
    *  df           - df to drop columns from
    *
    * returns : 
    *  df with new columns
    * --------------------------------------------------------
    """
    
    if(len(col_names) > 0) :
        
        new_subset_df       =   df.copy()   
        dfcolnames          =   list(new_subset_df.columns)
        
        action_colnames     =   col_names.lstrip("[")
        action_colnames     =   action_colnames.rstrip("]")
        action_colnames     =   action_colnames.split(",")
        
        drop_col_list   =   []
        if(col_action == "Keep") :
            
            for i in range(len(dfcolnames)) :
                if(not (dfcolnames[i] in action_colnames)) :
                    drop_col_list.append(dfcolnames[i])
                    
        else :
            drop_col_list   =   action_colnames
           
        new_subset_df.drop(drop_col_list, axis=1, inplace=True)   
        
    else :
        
        new_subset_df   =   df.copy()  

    return(new_subset_df)        


def display_dfsubset_utility(optionId,parms=None) :
    """
    * ---------------------------------------------------------
    * function : main subset utility control
    * 
    * parms :
    *  optionId     - function to run
    *  parms        - parms to ryn function
    *
    * returns : 
    *  NA
    * --------------------------------------------------------
    """
    
    if(cfg.is_a_dfc_dataframe_loaded()) :
        
        from IPython.display import clear_output
        clear_output()
        
        from dfcleanser.common.html_widgets import define_inputs, are_owner_inputs_defined
        if(not (are_owner_inputs_defined(cfg.SWDFSubsetUtility_ID)) ) :
            define_inputs(cfg.SWDFSubsetUtility_ID,swsw.SWUtility_subset_inputs)
    
        if(optionId == swsm.DISPLAY_MAIN) :
            
            swsw.get_dfsubset_main_taskbar()
            clear_sw_utility_dfsubsetdata()
            
            cfg.display_data_select_df(cfg.SWDFSubsetUtility_ID)
            swsm.clear_current_subset_data() 
            
        elif(optionId == swsm.DISPLAY_GET_SUBSET) :
            
            swsm.clear_current_subset_data()
            
            if(DEBUG_SUBSET) :
                swsm.set_current_subset_sequence(swsm.dfc_subset_sequence())
                print("\ncurrent_subset_sequence\n")
                print("input_df_title",swsm.get_current_subset_sequence().get_input_df_title()) 
                print("get_sequence_title",swsm.get_current_subset_sequence().get_sequence_title()) 
                print("get_sequence_steps",swsm.get_current_subset_sequence().get_sequence_steps()) 
                if(not (swsm.get_current_subset_sequence().get_sequence_steps() is None)) :
                    print("get_total_sequence_steps",swsm.get_current_subset_sequence().get_total_sequence_steps())
                    print("get_output_csv",swsm.get_current_subset_sequence().get_output_csv()) 
                    print("get_output_dfc_df_title",swsm.get_current_subset_sequence().get_output_dfc_df_title()) 
            
            
            swsw.display_df_subset_setup()
            
            
            if(DEBUG_SUBSET) :
                print("DISPLAY_GET_SUBSET",parms)
                print("DISPLAY_GET_SUBSET : clear data")
                print(swsm.get_current_subset_sequence())
                print(swsm.get_current_subset_df())
                print(swsm.get_current_subset_step())
                print("new_sequence")
                swsm.dump_current_step()
                swsm.dump_current_sequence()
            
        
        elif(optionId == swsm.PROCESS_GET_SUBSET) :
            
            current_step        =   swsm.get_current_subset_step()
            
            if(not (current_step is None)) :
                current_sequence    =   swsm.get_current_subset_sequence()
                current_sequence.add_step_to_sequence_steps(current_step) 
            
            fparms              =   get_parms_for_input(parms,swsw.get_subset_input_idList)
            
            if(len(fparms) > 0) :
        
                df_title            =   fparms[0]
                df                  =   cfg.get_dfc_dataframe_df(df_title)
                col_names           =   fparms[1]
                col_action          =   fparms[3]
        
            new_subset_df           =   drop_add_cols(col_names,col_action,df)
            new_subset_df_title     =   df_title
    
            new_subset_step     =   swsm.dfc_subset_step(new_subset_df_title,col_names,col_action)
            swsm.set_current_subset_step(new_subset_step)
            swsm.set_current_subset_df(new_subset_df)
            
            swsw.display_df_criteria(new_subset_df_title,new_subset_df) 
            
            if(DEBUG_SUBSET) :
                print("\nPROCESS_GET_SUBSET\n  ",parms,"\n  ",fparms)
                swsm.dump_current_step()
                swsm.dump_current_sequence()

            
        elif(optionId == swsm.DISPLAY_SAVED_SUBSET) :
            
            swsw.display_saved_subset_sequences() 

            if(DEBUG_SUBSET) :
                print("\nDISPLAY_SAVED_SUBSET",parms)
            
            
        elif(optionId == swsm.PROCESS_RUN_CRITERIA) :
            
            opstat  =   opStatus()
            
            
            fparms  =   get_parms_for_input(parms,swsw.get_subset_criteria_input_idList)
            
            subset_title    =   fparms[0]
            
            if(len(subset_title) == 0) :
                
                current_sequence    =   swsm.get_current_subset_sequence()
                total_steps         =   current_sequence.get_total_sequence_steps()
                current_step        =   swsm.get_current_subset_step()
                subset_title        =   current_step.get_input_subset_df_title() + "_subset_" + str(total_steps+1)
                
            criteria        =   fparms[2]
            
            if(len(criteria) > 0) :
                
                try :
                    
                    clock   =   RunningClock()
                    clock.start()
                    
                    final_criteria  =   (swsm.starting_criteria_preamble + criteria + swsm.starting_criteria_postamble)
        
                    exec(final_criteria)
                    
                    current_step    =   swsm.get_current_subset_step()
                    current_step.set_criteria(criteria)
                    current_step.set_output_subset_df_title(subset_title)
                    
                    clock.stop()
                    
                except Exception as e:
                    opstat.store_exception("Error running df_criteria " + criteria,e)
                    
                    clock.stop()
            
            
            if(opstat.get_status()) :
                swsw.display_process_subset() 
            else :
                display_exception(opstat)

            if(DEBUG_SUBSET) :
                print("PROCESS_RUN_CRITERIA : End")
                swsm.dump_current_step()
                swsm.dump_current_sequence()
            
        elif(optionId ==  swsm.DISPLAY_SAVE_SUBSET) :
            
            fparms              =   get_parms_for_input(parms,swsw.get_subset_run_input_idList)
            
            current_sequence    =   swsm.get_current_subset_sequence()
            current_step        =   swsm.get_current_subset_step()
            current_sequence.add_step_to_sequence_steps(current_step)
    
            if(len(fparms) > 0) :
        
                df_title            =   fparms[0]
                df                  =   swsm.get_current_subset_df()
                col_names           =   fparms[1]
                col_action          =   fparms[3]
 
            new_subset_df   =   drop_add_cols(col_names,col_action,df)
            
            swsw.display_save_subset(df_title,new_subset_df) 
            
            if(DEBUG_SUBSET) :
                print("DISPLAY_SAVE_SUBSET",parms,fparms)
                swsm.dump_current_step()
                swsm.dump_current_sequence()
            
 
            
        elif(optionId ==  swsm.DISPLAY_SAVE_AND_GET_SUBSET) :
            
            fparms              =   get_parms_for_input(parms,swsw.get_subset_run_input_idList)
            
            current_sequence    =   swsm.get_current_subset_sequence()
            current_step        =   swsm.get_current_subset_step()
            current_sequence.add_step_to_sequence_steps(current_step)
    
            if(len(fparms) > 0) :
        
                df_title            =   fparms[0]
                col_names           =   fparms[1]
                col_action          =   fparms[3]
        
            new_subset_step     =   swsm.dfc_subset_step(df_title,col_names,col_action)
            df                  =   swsm.get_current_subset_df()

            new_subset_df       =   drop_add_cols(col_names,col_action,df)
            swsm.set_current_subset_df(new_subset_df)
            swsm.set_current_subset_step(new_subset_step)
            
            swsw.display_df_criteria(df_title,new_subset_df)

            if(DEBUG_SUBSET) :
                print("PROCESS_SAVE_AND_GET_SUBSET",parms,fparms)
                swsm.dump_current_step()
                swsm.dump_current_sequence()

            
        elif(optionId ==  swsm.PROCESS_SAVE_SUBSET) :
            
            save_subset_run(parms,0)
            
        elif(optionId ==  swsm.PROCESS_SUBSET_SEQUENCE) :
            
            opstat  =   opStatus()
                        
            fparms      =   get_parms_for_input(parms,swsw.get_subset_sequences_input_idList)
            
            sequence    =   fparms[0]
            run_option  =   fparms[1]
            
            saved_sequence  =   swsm.get_subset_sequence(sequence)
            first_step      =   saved_sequence.get_sequence_step(0)
            
            df_title        =   first_step.get_input_subset_df_title()
            df              =   cfg.get_dfc_dataframe_df(df_title)
            
            if(df is None) :
                
                swsw.get_dfsubset_main_taskbar()
                cfg.display_data_select_df(cfg.SWDFSubsetUtility_ID)
                
                opstat.set_status(False)
                opstat.set_errorMsg("subset sequence starting df '" + df_title + "' is not currently loaded in dfc")
                display_exception(opstat)
            
            else :
                
                if(run_option == "Auto Run") :
                    
                    total_steps     =   saved_sequence.get_total_sequence_steps()
                    swsm.set_current_subset_df(df)
                    
                    for i in range(total_steps) :
                        
                        current_step        =   saved_sequence.get_sequence_step(i)
                        current_columns     =   current_step.get_col_names_list()
                        columns_action      =   current_step.get_keep_drop_flag()
                        criteria            =   current_step.get_criteria()
                        output_df_title     =   current_step.get_output_subset_df_title()
                        
                        current_df          =   swsm.get_current_subset_df()   
                        
                        if(len(current_columns) > 0) :
                            
                            colnames        =   list(current_df.columns)
                            drop_columns    =   []
                            
                            for i in range(len(colnames)) :
                                
                                if(columns_action == "Keep") :
                                    if(not (colnames[i] in current_columns)) :
                                        drop_columns.append(colnames[i])
                                else :
                                    if(colnames[i] in current_columns) :
                                        drop_columns.append(colnames[i])  
                                        
                            if(len(drop_columns) > 0 ) :
                                
                                try :
                                    current_df.drop(drop_columns, axis=1, inplace=True)   
                                except :
                                    opstat.set_status(False)
                                    opstat.set_errorMsg("Unable to drop columns from subset dataframe")
                        
                        swsm.set_current_subset_df(current_df)
                        
                        try :
                            
                            current_df         =     swsm.get_current_subset_df()
                            exec(criteria + swsm.starting_criteria_postamble)
                            current_df         =     swsm.get_current_subset_df()
                            
                        except Exception as e:
                            opstat.store_exception("Error running subset sequence '" + sequence + "'",e)

                    swsw.display_save_subset(output_df_title,swsm.get_current_subset_df(),True)    
                    
                else :
                
                    total_steps     =   saved_sequence.get_total_sequence_steps()
                    swsm.set_current_subset_df(df)
                    
                    current_step        =   saved_sequence.get_sequence_step(0)
                    current_df_title    =   current_step.get_input_subset_df_title()
                    current_columns     =   current_step.get_col_names_list()
                    columns_action      =   current_step.get_keep_drop_flag()
                    
                    swsw.display_manual_df_subset_setup(saved_sequence.get_sequence_title(),current_df_title,current_columns,columns_action,0)
                    
                    swsm.set_current_subset_step_id(0)
                    
                    swsm.set_current_subset_sequence(saved_sequence)

                     
        elif(optionId ==  swsm.PROCESS_GET_NEXT_SUBSET) :
            
            fparms      =   get_parms_for_input(parms,swsw.get_manual_input_idList) 
            
            collist     =   fparms[1]
            collist     =   collist.lstrip("[")
            collist     =   collist.rstrip("]")
            collist     =   collist.split(",")
            
            keep_drop   =   fparms[3]
            
            saved_sequence      =   swsm.get_current_subset_sequence()
            
            total_steps     =   saved_sequence.get_total_sequence_steps()
            current_step_id =   swsm.get_current_subset_step_id()
            
            if(current_step_id < total_steps) :
                current_step        =   saved_sequence.get_sequence_step(swsm.get_current_subset_step_id())
            else :
                swsm.set_current_subset_step_col_names_list(collist)
                swsm.set_current_subset_keep_drop_flag(keep_drop)
                current_step        =   swsm.get_current_subset_step()
                
            swsm.dump_current_step() 
            
            swsm.set_current_subset_step(current_step)
            
            current_df_title    =   current_step.get_input_subset_df_title()

            current_df          =   swsm.get_current_subset_df()
            current_columns     =   current_step.get_col_names_list()
            columns_action      =   current_step.get_keep_drop_flag()
            criteria            =   current_step.get_criteria()
            output_df_title     =   current_step.get_output_subset_df_title()
            
            if(len(current_columns) > 0) :
                            
                colnames        =   list(current_df.columns)
                drop_columns    =   []
                            
                for i in range(len(colnames)) :
                                
                    if(columns_action == "Keep") :
                        if(not (colnames[i] in current_columns)) :
                            drop_columns.append(colnames[i])
                    else :
                        if(colnames[i] in current_columns) :
                            drop_columns.append(colnames[i])  
                                        
                if(len(drop_columns) > 0 ) :
                                
                    try :
                        current_df.drop(drop_columns, axis=1, inplace=True)   
                    except :
                        opstat.set_status(False)
                        opstat.set_errorMsg("Unable to drop columns from subset dataframe")
                        
            
            swsw.display_next_criteria(current_df_title,current_df,criteria,output_df_title)
            
            
        elif(optionId ==  swsm.PROCESS_NEXT_CRITERIA) :
            
            opstat  =   opStatus()
            
            fparms      =   get_parms_for_input(parms,swsw.get_next_criteria_input_idList)  
            
            output_df_title     =   fparms[0]
            criteria            =   fparms[2]
            
            current_sequence    =   swsm.get_subset_sequence(sequence)
            sequence_title      =   current_sequence.get_sequence_title()
            
            try :
                            
                current_df         =     swsm.get_current_subset_df()
                exec(criteria + swsm.starting_criteria_postamble)
                current_df         =     swsm.get_current_subset_df()
                            
            except Exception as e:
                
                opstat.store_exception("Error running subset sequence '" + sequence_title + "'",e)
                
                current_df_title    =   current_step.get_input_subset_df_title()
                current_df          =   swsm.get_current_subset_df()
                criteria            =   current_step.get_criteria()
                output_df_title     =   current_step.get_output_subset_df_title()
                
                swsw.display_next_criteria(current_df_title,current_df,criteria,output_df_title)                
                
                display_exception(opstat)
                
            if(opstat.get_status()) :
                
                
                swsm.set_current_subset_df(current_df)
                swsm.set_current_subset_step_id(swsm.get_current_subset_step_id() + 1)
                
                if(swsm.get_current_subset_step_id() >= swsm.get_current_subset_sequence().get_total_sequence_steps()) :
                    
                    swsw.display_sequence_save_subset(output_df_title,swsm.get_current_subset_df()) 

                else :
                    
                    current_step        =   swsm.get_current_subset_sequence().get_sequence_step(swsm.get_current_subset_step_id())
                    current_df_title    =   current_step.get_input_subset_df_title()
                    current_columns     =   current_step.get_col_names_list()
                    columns_action      =   current_step.get_keep_drop_flag()
                    
                    swsw.display_manual_df_subset_setup(swsm.get_current_subset_sequence().get_sequence_title(),current_df_title,current_columns,columns_action,swsm.get_current_subset_step_id())
                    
        elif(optionId ==  swsm.DISPLAY_NEW_STEP) :  
                
            current_sequence    =   swsm.get_current_subset_sequence()
            sequence_title      =   current_sequence.get_sequence_title()
            
            current_step        =   swsm.get_current_subset_step()
            df_title            =   current_step.get_output_subset_df_title()
            current_df          =   swsm.get_current_subset_df()
            current_columns     =   []
            current_action      =   "Keep"
            criteria            =   swsm.starting_criteria
            output_df_title     =   ""
            
            current_step        =   swsm.dfc_subset_step(df_title,current_columns,current_action,criteria,output_df_title)
            swsm.set_current_subset_step(current_step)
            
            swsw.display_manual_df_subset_setup(sequence_title,df_title,current_columns,current_action,swsm.get_current_subset_step_id())
            #swsw.display_next_criteria(df_title,current_df,criteria,output_df_title)
                
        elif(optionId ==  swsm.PROCESS_SAVE_SAVED_SUBSET ) :   

            save_subset_run(parms,1)
        
        elif(optionId ==  swsm.DISPLAY_GET_REMOTE_SUBSET) :  
            
            chapterid   =   parms[0]
            
            new_config_df   =   None
            
            if(chapterid == cfg.DataInspection_ID)      :   new_config_df  =   cfg.get_config_value(cfg.CURRENT_INSPECTION_DF)
            elif(chapterid == cfg.DataCleansing_ID)     :   new_config_df  =   cfg.get_config_value(cfg.CURRENT_CLEANSE_DF)
            elif(chapterid == cfg.DataTransform_ID)     :   new_config_df  =   cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF)
            elif(chapterid == cfg.DataExport_ID)        :   new_config_df  =   cfg.get_config_value(cfg.CURRENT_EXPORT_DF)
            elif(chapterid == cfg.DataImport_ID)        :   new_config_df  =   cfg.get_config_value(cfg.CURRENT_IMPORT_DF)
            elif(chapterid == cfg.SWGeocodeUtility_ID)  :   new_config_df  =   cfg.get_config_value(cfg.CURRENT_GEOCODE_DF)
            elif(chapterid == cfg.SWDFSubsetUtility_ID) :   new_config_df  =   cfg.get_config_value(cfg.CURRENT_SUBSET_DF)
            
            cfg.set_config_value(cfg.CURRENT_SUBSET_DF,new_config_df)
            
            swsm.clear_current_subset_data()
            swsw.display_df_subset_setup()
            
    else :
        
        swsw.get_dfsubset_main_taskbar()
        
        cfg.drop_config_value(cfg.CURRENT_SUBSET_DF)
        clear_sw_utility_dfsubsetdata()
        
        cfg.display_data_select_df(cfg.SWDFSubsetUtility_ID)
            
        if(not(optionId == swsm.DISPLAY_MAIN)) :
            cfg.display_no_dfs(cfg.SWDFSubsetUtility_ID)

        
def save_subset_run(parms,saveid) :  

    opstat  =   opStatus()
       
    if(saveid == 0) :     
        fparms              =   get_parms_for_input(parms,swsw.get_subset_save_input_idList)
    else :
        fparms              =   get_parms_for_input(parms,swsw.get_saved_save_input_idList)
        
            
    dfc_df_title        =   fparms[0]
    csv_file_name       =   fparms[1]
    save_subset_name    =   fparms[2]
    
    if(saveid == 1) :
        
        drop_original   =   fparms[3]
        
        if(drop_original == "False") :
            drop_original   =   False
        else :
            drop_original   =   True
            
    else :
        
        drop_original   =   False
            
    if(len(dfc_df_title) > 0) :

        try :
                    
            new_dfc_df  =   cfg.dfc_dataframe(dfc_df_title,swsm.get_current_subset_df(),
                                              "df from dataframe subset utility")
            cfg.add_dfc_dataframe(new_dfc_df)
    
        except Exception as e:
            opstat.store_exception("Error saving subset df as dfc df " + dfc_df_title,e)
            
        if(len(csv_file_name) > 0) : 
                   
            try :
                    
                swsm.get_current_subset_df().to_csv(csv_file_name,index=False)
                    
            except Exception as e:
                opstat.store_exception("Error saving subset df as csv file " + csv_file_name,e)
                    
        if(len(save_subset_name) > 0) : 
                   
            try :
                    
                swsm.add_subset_sequence(save_subset_name)
                    
            except Exception as e:
                opstat.store_exception("Error saving subset sequence " + save_subset_name,e)
                
        if(drop_original) :
            
            current_sequence    =   swsm.get_current_subset_sequence()
            sequence_title      =   current_sequence.get_sequence_title()
            swsm.drop_subset_sequence(sequence_title)
            
            
        swsw.get_dfsubset_main_taskbar()
        cfg.display_data_select_df(cfg.SWDFSubsetUtility_ID)
            
        print("\n")
            
        if(opstat.get_status()) :
                
            status_msg  =   ""
                
            if(len(dfc_df_title) > 0)       :   status_msg  =   status_msg + ("Final Subset df saved as dfc df : " + dfc_df_title + "<br><br>")
            if(len(csv_file_name) > 0)      :   status_msg  =   status_msg + ("Final Subset df saved as excel file : " + csv_file_name + "<br><br>")
            if(len(save_subset_name) > 0)   :   status_msg  =   status_msg + ("Subset sequence saved as : " + save_subset_name + "<br>")
            if(drop_original)               :   status_msg  =   status_msg + ("Original Subset sequence dropped : " + sequence_title + "<br>")
                
            if(len(status_msg) > 0) :
                display_status(status_msg)
                
        else :
            display_exception(opstat)

        swsm.clear_current_subset_data()
            
        if(DEBUG_SUBSET) :
            print("PROCESS_SAVE_SUBSET",parms,fparms)
            print("dfc_df_title",dfc_df_title)
            print("csv_file_name",csv_file_name)
            print("save_subset_name",save_subset_name)
            swsm.dump_current_step()
            swsm.dump_current_sequence()

     

"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#   subset housekeeping functions
#------------------------------------------------------------------
#------------------------------------------------------------------
""" 
def clear_sw_utility_dfsubsetdata() :
    
    drop_owner_tables(cfg.SWDFSubsetUtility_ID)
    from dfcleanser.common.html_widgets import delete_all_inputs
    delete_all_inputs(cfg.SWDFSubsetUtility_ID)
    clear_sw_utility_dfsubset_cfg_values()


def clear_sw_utility_dfsubset_cfg_values() :
 
    cfg.drop_config_value(swsw.get_subset_input_id+"Parms")
    cfg.drop_config_value(swsw.get_subset_criteria_input_id+"Parms")
    
    from dfcleanser.data_inspection.data_inspection_control import drop_working_df
    drop_working_df() 
    
    swsm.Current_Manual_Step            =   0
    swsm.Current_Manual_Sequence        =   ""
    
    return()




    
    
    
    
    
    
    
    
    
    
    
    



