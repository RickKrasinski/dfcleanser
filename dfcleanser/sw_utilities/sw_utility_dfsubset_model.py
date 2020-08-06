"""
# sw_utility_dfsubset_model 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""

import sys
this = sys.modules[__name__]


DISPLAY_MAIN                    =   0

DISPLAY_GET_SUBSET              =   1
PROCESS_GET_SUBSET              =   2

PROCESS_RUN_CRITERIA            =   5
CLEAR_FILTER_FORM               =   6

DISPLAY_SAVED_SUBSET            =   8

DISPLAY_SAVE_SUBSET             =   10
DISPLAY_SAVE_AND_GET_SUBSET     =   11

PROCESS_SAVE_SUBSET             =   12

PROCESS_SUBSET_SEQUENCE         =   13

INSPECT_DF                      =   14

OPEN_IN_EXCEL                   =   15

PROCESS_GET_NEXT_SUBSET         =   16
PROCESS_NEXT_CRITERIA           =   17
CLEAR_NEXT_FILTER_FORM          =   18

DISPLAY_NEW_STEP                =   19

PROCESS_SAVE_SAVED_SUBSET       =   20

DISPLAY_GET_REMOTE_SUBSET       =   21


starting_criteria_preamble      =   ("from dfcleanser.sw_utilities.sw_utility_dfsubset_model import get_current_subset_df\n" +
                                     "current_df         =     get_current_subset_df()\n\n")

starting_criteria               =   ("criteria                =   (current_df['State'] == 'CA')\n")

starting_criteria_postamble     =   ("next_subset_df   =   current_df[criteria]\n" + 
                                     "from dfcleanser.sw_utilities.sw_utility_dfsubset_model import set_current_subset_df\n" + 
                                     "set_current_subset_df(next_subset_df)\n")


DEBUG_SUBSET_MODEL  =   False

Current_Manual_Step             =   0
Current_Manual_Sequence         =   ""
    

"""
* ---------------------------------------------------------
* ---------------------------------------------------------
* dfc subset step class
* ---------------------------------------------------------
* ---------------------------------------------------------
"""

class dfc_subset_step :
    
    input_subset_df_title       =   ""
    col_names_list              =   []
    keep_drop_flag              =   True
    criteria                    =   ""
    output_subset_df_title      =   ""

    
    # full constructor
    def __init__(self,input_subset_df_title,drop_col_names_list,keep_drop_flag,criteria="",output_subset_df_title="") :

        self.input_subset_df_title          =   input_subset_df_title
        self.col_names_list                 =   drop_col_names_list
        self.keep_drop_flag                 =   keep_drop_flag
        self.criteria                       =   criteria
        self.output_subset_df_title         =   output_subset_df_title
        
        
    def get_input_subset_df_title(self) :
        return(self.input_subset_df_title)
        
    def get_col_names_list(self) :
        return(self.col_names_list)
        
    def get_keep_drop_flag(self) :
        return(self.keep_drop_flag)
        
    def get_criteria(self) :
        return(self.criteria)
       
    def get_output_subset_df_title(self) :
        return(self.output_subset_df_title)
        
    def set_input_subset_df_title(self,input_subset_df_title) :
        self.input_subset_df_title = input_subset_df_title
        
    def set_col_names_list(self,col_names_list) :
        self.col_names_list = col_names_list
        
    def set_keep_drop_flag(self,keep_drop_flag) :
        self.keep_drop_flag = keep_drop_flag
        
    def set_criteria(self,criteria) :
        self.criteria = criteria
       
    def set_output_subset_df_title(self,output_subset_df_title) :
        self.output_subset_df_title = output_subset_df_title


"""
* ---------------------------------------------------------
* ---------------------------------------------------------
* dfc subset sequence class
* ---------------------------------------------------------
* ---------------------------------------------------------
"""

class dfc_subset_sequence :

    input_df_title          =   ""
    sequence_title          =   ""
    sequence_steps          =   None
    output_csv              =   ""
    output_dfc_df_title     =   ""

    # full constructor
    def __init__(self,input_df_title="",sequence_title="",sequence_steps=None,output_csv="",output_dfc_df_title="") :

        self.input_df_title         =   input_df_title
        self.sequence_title         =   sequence_title
        self.sequence_steps         =   sequence_steps
        self.output_csv             =   output_csv
        self.output_dfc_df_title    =   output_dfc_df_title
        
    def get_total_sequence_steps(self) :
        if(self.sequence_steps is None) :
            return(0)
        else :
            return(len(self.sequence_steps))
        
    def get_sequence_step(self,stepid) :
        
        if(stepid > self.get_total_sequence_steps()) :
            return(None)
        else :
            if(stepid < 0) :
                return(None)
            else :
                return(self.sequence_steps[stepid])
                
    def add_step_to_sequence_steps(self,newstep) :
        if(self.sequence_steps is None) :
            self.sequence_steps     =   []
            
        self.sequence_steps.append(newstep)
        
    def get_input_df_title(self) :
        return(self.input_df_title)
        
    def get_sequence_title(self) :
        return(self.sequence_title)
    
    def set_sequence_title(self,title) :
        self.sequence_title = title
        
    def get_sequence_steps(self) :
        return(self.sequence_steps)
        
    def get_output_csv(self) :
        return(self.output_csv)
       
    def get_output_dfc_df_title(self) :
        return(self.output_dfc_df_title)
        
    
"""
* ---------------------------------------------------------
* ---------------------------------------------------------
* Current subset sequence, step and df being built
* ---------------------------------------------------------
* ---------------------------------------------------------
"""

def get_current_subset_sequence() :
    return(current_df_subset_data.get_current_subset_sequence())
    
def set_current_subset_sequence(sequence) :
    current_df_subset_data.set_current_subset_sequence(sequence)

def get_current_subset_df() :
    return(current_df_subset_data.get_current_df())
    
def set_current_subset_df(df) :
    current_df_subset_data.set_current_df(df)

def get_current_subset_step_id() :
    return(current_df_subset_data.get_current_subset_step_id())
    
def set_current_subset_step_id(step_id) :
    current_df_subset_data.set_current_subset_step_id(step_id)
    
def get_current_subset_step() :
    return(current_df_subset_data.get_current_subset_step())
    
def set_current_subset_step(step) :
    current_df_subset_data.set_current_subset_step(step)

def set_current_subset_step_col_names_list(col_names_list) :
    current_step    =   get_current_subset_step()
    current_step.set_col_names_list(col_names_list)

def set_current_subset_keep_drop_flag(keep_drop_flag) :
    current_step    =   get_current_subset_step()
    current_step.set_keep_drop_flag(keep_drop_flag)
    
def clear_current_subset_data() :
    current_df_subset_data.clear_current_subset_data()
    
        
class dfc_current_subset_data :    

    dfc_sequence        =   None
    dfc_subset_step_id  =   None
    dfc_subset_step     =   None
    df                  =   None    
        
    def __init__(self,sequence=None,step_id=None,step=None,df=None) :
        
        self.dfc_sequence       =   sequence
        self.dfc_subset_step_id =   step_id
        self.dfc_subset_step    =   step
        self.df                 =   df
    
    def get_current_subset_sequence(self) :
        return(self.dfc_sequence)
        
    def get_current_subset_step_id(self) :
        return(self.dfc_subset_step_id)
    
    def get_current_subset_step(self) :
        return(self.dfc_subset_step)
        
    def get_current_df(self) :
        return(self.df)
    
    def set_current_subset_sequence(self,subset_sequence) :
        self.dfc_sequence = subset_sequence
        
    def set_current_subset_step_id(self,subset_step_id) :
        self.dfc_subset_step_id = subset_step_id
        
    def set_current_subset_step(self,subset_step) :
        self.dfc_subset_step = subset_step
        
    
    def set_current_df(self,df) :
        self.df = df
        
    def clear_current_subset_data(self) :
        
        self.dfc_sequence        =   None
        self.dfc_subset_step_id  =   None
        self.dfc_subset_step     =   None
        self.df                  =   None  
        
        if(DEBUG_SUBSET_MODEL) :
            print("clear_current_subset_data")
            print("current_subset_sequence",self.get_current_subset_sequence())
            print("current_subset_step",self.get_current_subset_step())
            print("current_df",self.get_current_df())

current_df_subset_data  =   dfc_current_subset_data()



def dump_current_step() :
    
    current_step    =   get_current_subset_step()
    
    if(not (current_step is None)) :
    
        print("\ncurrent step \n")
        print("  input_subset_df_title      : ",current_step.get_input_subset_df_title())
        print("  col_names_list             : ",current_step.get_col_names_list())
        print("  keep_drop_flag             : ",current_step.get_keep_drop_flag())
        print("  criteria                   : ",current_step.get_criteria())
        print("  get_output_subset_df_title : ",current_step.get_output_subset_df_title())
        
    else :
        
        print(" \ncurrent step : None \n ")
        
        
def dump_current_sequence() :
    

    current_sequence    =   get_current_subset_sequence()
    
    if(not (current_sequence is None)) :
        print("\nCurrent Sequence \n")
    
        total_steps         =   current_sequence.get_total_sequence_steps()
    
        for i in range(total_steps) :
            current_step    =   current_sequence.get_sequence_step(i)
            print("step ",str(i)," : \n")
            print("  input_subset_df_title      : ",current_step.get_input_subset_df_title())
            print("  col_names_list             : ",current_step.get_col_names_list())
            print("  keep_drop_flag             : ",current_step.get_keep_drop_flag())
            print("  criteria                   : ",current_step.get_criteria())
            print("  get_output_subset_df_title : ",current_step.get_output_subset_df_title(),"\n")
            
    else :
        
        print(" \ncurrent sequence : None  \n")
        


"""
* ---------------------------------------------------------
* ---------------------------------------------------------
* Current subset sequences stored for later use
* ---------------------------------------------------------
* ---------------------------------------------------------
""" 


"""
* ---------------------------------------------------------
* ---------------------------------------------------------
* Current subset sequences storage class
* ---------------------------------------------------------
* ---------------------------------------------------------
"""

def get_subset_sequence(sequencetitle) :
    return(dfc_subset_sequences.get_sequence(sequencetitle))

def add_subset_sequence(sequence_title) :
    dfc_subset_sequences.add_sequence(sequence_title)
    
def get_sequences_list() :
    return(dfc_subset_sequences.get_list_of_sequences())    
        
def drop_subset_sequence(sequencetitle) :
    return(dfc_subset_sequences.get_sequence(sequencetitle))


   

class dfc_subset_sequences_store :

    dfc_subset_sequences_file_dir       =   ""
    dfc_subset_sequences_file_name      =   "" 
    dfc_subset_sequences_dict           =   {}
    
    
    
    @staticmethod
    def get_subset_sequence_dir_name() :
        
        import os
        
        from dfcleanser.common.cfg import get_notebookName, get_notebookPath
        
        nbdir   =   get_notebookPath()
        nbname  =   get_notebookName()
        
        if((nbdir is None)or(nbname is None)) :
            return(None)
        else :
            return(os.path.join(nbdir,nbname + "_files"))
    
    @staticmethod
    def get_subset_sequence_file_name() :

        import os
        
        seqdir  =   dfc_subset_sequences_store.get_subset_sequence_dir_name()   
        
        if(seqdir is None) :
            return(None)
        else :
            from dfcleanser.common.cfg import get_notebookName
            fname   =   get_notebookName() + "_subset_sequences.json"
            return(os.path.join(seqdir,fname)) 

    
    # full constructor
    def __init__(self) :
        
        self.load_dfc_subset_sequences()

    def load_dfc_subset_sequences(self) :

        self.dfc_subset_sequences_dict = self.unserialize_sequence_dict() 
        
        seq_keys    =   list(self.dfc_subset_sequences_dict.keys())
        for i in range(len(seq_keys)) :
            
            curseq  =   self.dfc_subset_sequences_dict.get(seq_keys[i])
            
            if(DEBUG_SUBSET_MODEL) :
            
                print("sequence  i : ",str(i)," ",seq_keys[i])
                print("   type                 : ",type(curseq))
                print("   sequence_title       : ",curseq.get_sequence_title())
                print("   total_sequence_steps : ",curseq.get_total_sequence_steps())
                print("   input_df_title       : ",curseq.get_input_df_title())
                print("   output_dfc_df_title  : ",curseq.get_output_dfc_df_title())


    def unserialize_sequence_dict(self) :
        
        dfc_subset_sequences_file   =   dfc_subset_sequences_store.get_subset_sequence_file_name() 
        
        from dfcleanser.common.common_utils import does_file_exist
        if(does_file_exist(dfc_subset_sequences_file)) :
    
            import json
        
            try :
        
                with open(dfc_subset_sequences_file, 'r') as dfc_subset_file :
                    
                    temp_dict = json.load(dfc_subset_file)
                    dfc_subset_file.close()
    
                new_subset_sequences_dict = {}
    
                for i in range(len(temp_dict)) :
                    
                    current_sequence = temp_dict[i]
                    current_attributes = current_sequence[0]
                    current_sequence_title = current_attributes[0]
                    current_sequence_total_steps = int(current_attributes[1])
                    
                    if(DEBUG_SUBSET_MODEL) :
                        print("current_sequence_title",current_sequence_title)
                        print("current_sequence_total_steps",current_sequence_total_steps)
                    
                    new_sequence  = dfc_subset_sequence()
                    new_sequence.set_sequence_title(current_sequence_title)
        
                    for j in range(current_sequence_total_steps) :
            
                        current_step = dfc_subset_step(current_sequence[j+1][0],
                                                       current_sequence[j+1][1],
                                                       current_sequence[j+1][2],
                                                       current_sequence[j+1][3],
                                                       current_sequence[j+1][4])
            
                        new_sequence.add_step_to_sequence_steps(current_step)
            
                    new_subset_sequences_dict.update({current_sequence_title : new_sequence})
                
                
            except :
                from dfcleanser.common.cfg import add_error_to_log
                add_error_to_log("[Load dfc subset sequences file Error] "  + str(sys.exc_info()[0].__name__))
                
        return(new_subset_sequences_dict)   
                
    
    def serialize_sequence_dict(self) :
        
        #sequence_titles     =   list(dfc_subset_sequences_dict.keys())
    
        sequences   =   self.get_list_of_sequences()
        
        serial_sequences        =   []

        for i in range(len(sequences)) :
            
            current_serial_sequence     =   []
            
            current_sequence    =   self.dfc_subset_sequences_dict.get(sequences[i])
            total_steps         =   current_sequence.get_total_sequence_steps()
    
            current_serial_sequence.append([str(sequences[i]),str(total_steps)])
            
            for j in range(total_steps) :
                
                current_step    =   current_sequence.get_sequence_step(j)
                
                current_serial_step   =   []
                
                current_serial_step.append(current_step.get_input_subset_df_title())
                current_serial_step.append(current_step.get_col_names_list())
                current_serial_step.append(current_step.get_keep_drop_flag())
                current_serial_step.append(current_step.get_criteria())
                current_serial_step.append(current_step.get_output_subset_df_title())
                
                current_serial_sequence.append(current_serial_step) 
                
            serial_sequences.append(current_serial_sequence)
            
        if(DEBUG_SUBSET_MODEL) :
            print("serial sequences dict\n",serial_sequences)
            
        return(serial_sequences)    

        
    def save_dfc_subset_sequences(self) :

        dfc_subset_sequences_file   =   dfc_subset_sequences_store.get_subset_sequence_file_name() 
        
        if(DEBUG_SUBSET_MODEL) :
            print("save_dfc_subset_sequences",dfc_subset_sequences_file)
            print(self.dfc_subset_sequences_dict)
        
        serial_dict     =   self.serialize_sequence_dict()
        
        try :
                    
            with open(dfc_subset_sequences_file, 'w') as  dfc_subset_file :
                
                import json
                
                json.dump(serial_dict,dfc_subset_file)
                dfc_subset_file.close()
                    
                    
        except :
            from dfcleanser.common.cfg import add_error_to_log
            add_error_to_log("[Save dfc subset sequences file Error] "  + str(sys.exc_info()[0].__name__))

            
    def get_list_of_sequences(self) :
        
        sequences   =   list(self.dfc_subset_sequences_dict.keys())
        sequences.sort()
        
        return(sequences)

    def get_sequence(self,sequencetitle) :
        
        return(self.dfc_subset_sequences_dict.get(sequencetitle,None))
        
    def add_sequence(self,sequencetitle) :
        
        #print("add_sequence",sequencetitle)
        current_sequence    =   get_current_subset_sequence() 
        
        if(DEBUG_SUBSET_MODEL) :
            print("add_sequence",type(current_sequence))
            dump_current_sequence()
            print("add_sequence",type(self.dfc_subset_sequences_dict))
        
        self.dfc_subset_sequences_dict.update({sequencetitle : current_sequence})

        self.save_dfc_subset_sequences()
        
    def drop_sequence(self,sequencetitle) :
        
        self.dfc_subset_sequences_dict.pop(sequencetitle,None)
    
        
dfc_subset_sequences    =   dfc_subset_sequences_store()        


