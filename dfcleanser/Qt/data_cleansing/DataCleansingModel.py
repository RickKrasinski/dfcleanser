"""
# DataCleansingModel 
"""

# -*- coding: utf-8 -*-
"""
Created on Sept 13 22:29:22 2018

@author: Rick
"""
import sys
this = sys.modules[__name__]

from dfcleanser.common.common_utils import (opStatus)
from dfcleanser.common.cfg import (add_error_to_log, SEVERE_ERROR, set_config_value, get_config_value, CURRENT_IMPORTED_DATA_SOURCE_KEY)

DEBUG_DATA_CLEANSING            =   False



"""
#--------------------------------------------------------------------------
#    numeric columns change values input
#--------------------------------------------------------------------------
"""
change_values_input_title               =   "Change Data Value"
change_values_input_id                  =   "dcchangevalsinput"
change_values_input_idList              =   ["changecval",
                                             "changenval"
                                             ,None]

change_values_input_labelList           =   ["current_column_value",
                                             "new_Column_value",
                                             "Change Values"]

change_values_input_typeList            =   ["text","text","button"]

change_values_input_placeholderList     =   ["","",None]

change_values_input_reqList             =   [0,1]

"""
#--------------------------------------------------------------------------
#    non numeric columns change values input
#--------------------------------------------------------------------------
"""
nn_change_values_input_title            =   "Change Data Value"
nn_change_values_input_id               =   "dcnnchangevalsinput"
nn_change_values_input_idList           =   ["nnchangecval",
                                             "nnchangenval",
                                             None]

nn_change_values_input_labelList        =   ["current_column_value",
                                             "new_column_value",
                                             "Change Values"]

nn_change_values_input_typeList         =   ["text","text","button"]

nn_change_values_input_placeholderList  =   ["","",None]

nn_change_values_input_reqList          =   [0,1]


"""
#--------------------------------------------------------------------------
#    round column input text
#--------------------------------------------------------------------------
"""
col_round_input_title                   =   "Column Round"
col_round_input_id                      =   "columnroundinput"
col_round_input_idList                  =   ["columnround",None,None,None]

col_round_input_labelList               =   ["number_of_decimals",
                                             "Round</br>Column",
                                             "Return",
                                             "Help"]

col_round_input_typeList                =   ["text","button","button","button"]

col_round_input_placeholderList         =   ["",None,None,None]

col_round_input_reqList                 =   [0]


"""
#--------------------------------------------------------------------------
#    data transform remove whitespace input 
#--------------------------------------------------------------------------
"""
transform_remwhite_input_title          =   "Remove Whitespace"
transform_remwhite_input_id             =   "remwhitetransformInput"
transform_remwhite_input_idList         =   ["wschars",
                                             "leadtrailflag",
                                             None,None,None]

transform_remwhite_input_labelList      =   ["whitespace_chars",
                                             "remove_type_flag",
                                             "Remove</br>Whitspace",
                                             "Return","Help"]

transform_remwhite_input_typeList       =   ["select","select","button","button","button"]

transform_remwhite_input_placeholderList =  ["whitespace chars",
                                             "remove leading and trailing",
                                             None,None,None]

transform_remwhite_input_reqList        =   [0,1]


"""
#--------------------------------------------------------------------------
#   numeric fillna form
#--------------------------------------------------------------------------
"""
col_fillna_input_title                  =   "Change Data Type"
col_fillna_input_id                     =   "fillnainput"
col_fillna_input_idList                 =   ["fillvalue",
                                             "fillmethod",
                                             None,None,None]

col_fillna_input_labelList              =   ["fillna_value",
                                             "fillna_method",
                                             "Fill</br>Nans",
                                             "Return","Help"]

col_fillna_input_typeList               =   ["text","select",
                                             "button","button","button"]

col_fillna_input_placeholderList        =   ["fillna value",
                                             "fillna method",
                                              None,None,None]

col_fillna_input_reqList                =   [0,1]


"""
#--------------------------------------------------------------------------
#   non numeric fillna form
#--------------------------------------------------------------------------
"""
nn_col_fillna_input_title               =   "Fill Nans"
nn_col_fillna_input_id                  =   "nnfillna"
nn_col_fillna_input_idList              =   ["nnfillna_value",
                                              None,None,None]

nn_col_fillna_input_labelList           =   ["fillna_value",
                                              "Fill</br>Nans",
                                              "Return","Help"]

nn_col_fillna_input_typeList            =   ["text",
                                             "button","button","button"]

nn_col_fillna_input_placeholderList     =   ["fillna value",
                                              None,None,None]

nn_col_fillna_input_reqList             =   [0]



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    categorical form widgets
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""



"""
#--------------------------------------------------------------------------
#    category forms
#--------------------------------------------------------------------------
"""

rename_category_input_title             =   "Change Data Value"
rename_category_input_id                =   "catcleanserenameinput"
rename_category_input_idList            =   ["changecatval",
                                             "changencatval",
                                             None,None]

rename_category_input_labelList         =   ["current_category_name",
                                             "new_category_name",
                                             "Rename</br>Category","Return"]

rename_category_input_typeList          =   ["select","text","button","button"]

rename_category_input_placeholderList   =   ["current category","new category",None,None]

rename_category_input_reqList           =   [0,1]


"""
#--------------------------------------------------------------------------
#    add category form   
#--------------------------------------------------------------------------
"""
add_category_input_title                  =   ""
add_category_input_id                     =   "catcleanseaddnameinput"
add_category_input_idList                 =   ["addcatname",
                                               None,None,None]

add_category_input_labelList              =   ["new_category_name",
                                               "Add</br>New</br>Category",
                                               "Return","Hekp"]

add_category_input_typeList               =   ["text","button","button","button"]

add_category_input_placeholderList        =   ["new category name",None,None,None]

add_category_input_reqList                =   [0]

from dfcleanser.common.html_widgets import maketextarea

"""
#--------------------------------------------------------------------------
#    dataframe drop duplicate rows inputs
#--------------------------------------------------------------------------
"""
df_drop_dups_transform_input_title          =   "Drop Duplicate Rows"
df_drop_dups_transform_input_id             =   "dropduplicatetransform"
df_drop_dups_transform_input_idList         =   ["colssubset",
                                                 "dropduplicatedrop",
                                                 "dropduplicatekeep",
                                                 None,None,None]

df_drop_dups_transform_input_labelList      =   ["columns_subset",
                                                 "columns_for_duplicate_match",
                                                 "keep_duplicates_flag",
                                                 "Drop Duplicate</br>Rows",
                                                 "Return","Help"]

df_drop_dups_transform_input_typeList       =   [maketextarea(2),"select","select",
                                                 "button","button","button"]

df_drop_dups_transform_input_placeholderList =  ["susbset of columns to use for compare ",
                                                 "drop or keep column_drop_keys_list (default : keep ) ",
                                                 "which duplicates to drop (default : False ) ",
                                                 None,None,None]

df_drop_dups_transform_input_reqList        =   [0,1,2]






DEBUG_USER_FNS      =   True










"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Dataframe Cleanser userfn history class
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

class userfnParms() :
    
    # full constructor
    def __init__(self,fnname,fndesc,fncode) :
        
        if(DEBUG_USER_FNS) :
            print("[userfnParms] : init",fnname,fndesc,"\n  ",fncode)
        
        self.fn_name            =   fnname
        self.fn_description     =   fndesc
        self.fn_code            =   fncode
        
      
    def get_fn_name(self) :
        return(self.fn_name)
    
    def get_fn_description(self) :
        return(self.fn_description)

    def get_fn_code(self) :
        return(self.fn_code)


class UserfnsHistory :
    
    # instance variables
    
    # notebook specific import history data
    notebook_history            =   {}
    default_history             =   {}
    history_file_loaded         =   False
    history_type                =   None
    
    
    """
    #--------------------------------------------------------------------------
    #   Dataframe Cleanser config initialization methods
    #--------------------------------------------------------------------------
    """
    
    # full constructor
    def __init__(self,history_type) :
        
        self.user_fns_dict              =   None
        self.history_file_loaded        =   False
        self.load_history_file()



    """
    #--------------------------------------------------------------------------
    #   Dataframe Cleanser import history files methods
    #--------------------------------------------------------------------------
    """
    
    def get_history_dir_name(self,history_type) :
        
        import os
        
        import dfcleanser.common.cfg as cfg
        return(str(cfg.get_dfcleanser_location()+"files"))
    
    def get_history_file_name(self) :
        
        #import os
        
        from dfcleanser.common.cfg import DataframeCleansercfg, get_dfcleanser_location
        
        cfgdir      =   DataframeCleansercfg.get_cfg_dir_name()
        nbname      =   DataframeCleansercfg.get_notebookname()
        file_loc    =   str(get_dfcleanser_location()+"files")
        return("dfcleanserCommon_userfns_history.json") 

    def get_history_full_file_name(self,history_type) :
        
        import os
        
        cfgdir  =   self.get_history_dir_name()
        fname   =   self.get_history_file_name()
        return(os.path.join(cfgdir,fname)) 


    def load_history_file(self) :
        
        import json

        if(DEBUG_USER_FNS) :
            print("\n[load_history_file] : self.history_file_loaded  ",self.history_file_loaded )

        history_data             =   []
        
        history_dir_name         =   self.get_history_dir_name(self.history_type)
        history_file_name        =   self.get_history_file_name(self.history_type)
        history_full_file_name   =   self.get_history_full_file_name(self.history_type)
        
        if(DEBUG_USER_FNS) :
            print("load_history_file",history_dir_name,"\n",history_file_name,"\n",history_full_file_name)
        
        if(not (history_dir_name is None)) :
            
            from dfcleanser.common.common_utils import does_dir_exist, make_dir
            if(not (does_dir_exist(history_dir_name))) :
                make_dir(history_dir_name)
            
            from dfcleanser.common.common_utils import does_file_exist
            if(DEBUG_USER_FNS) :
                print("[load_history_file] : does_file_exist ",does_file_exist(history_full_file_name))
            
            if(not (does_file_exist(history_full_file_name))) :
                
                if(DEBUG_USER_FNSS) :
                    print("load_history_file - file not found\n",history_full_file_name)
                    print("load_history_file - file not found : history type",self.history_type)
 
                self.history_file_loaded    =   False    
                self.notebook_history       =   {}
                
                if(DEBUG_USER_FNS) :
                    print("load_history_file - file not found : history length ",len(self.notebook_history))
                    self.dump_history()
            
            # import history file does exist
            else :
                
                if(DEBUG_USER_FNS) :
                    print("[load_history_file]  - file found\n  ",history_full_file_name)
                
                try :

                    with open(history_full_file_name,'r') as  history_file :
                            
                        history_data = json.load(history_file)
                        history_file.close()

                    if(DEBUG_USER_FNS) :
                        print("[load_history_file]  - history_data  ",type(history_data),len(history_data))
                    
                    self._parse_history_file_to_dict(history_data)
                    self.history_file_loaded = True
                    
                    if(DEBUG_USER_FNS) :
                        print("[load_history_file]  - self.history_file_loaded  ",self.history_file_loaded)
                        
                except :
                        
                    from dfcleanser.common.cfg import add_error_to_log, SEVERE_ERROR
                    add_error_to_log("[Load history file Error - for json decode error] "  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)
                    
        if(DEBUG_USER_FNS) :
            print("[load_history_file] - complete : ",self.history_file_loaded)

    def save_history_file(self) :
        
        import json
        
        history_data     =   []
        
        history_dir_name     =   self.get_history_dir_name(self.history_type)
        history_file_name    =   self.get_history_full_file_name(self.history_type)
            
        from dfcleanser.common.common_utils import does_dir_exist, make_dir
        if(not (does_dir_exist(history_dir_name))) :
            make_dir(history_dir_name)
            
        history_data     =   self._parse_history_dict_to_list()  
            
        if(DEBUG_USER_FNS) :
            print("\nhistory_data")
            for i in range(len(history_data)) :
                print("history",history_data[i])
            
        try :
                    
            with open(history_file_name, 'w') as  history_file :
                json.dump(history_data,history_file)
                history_file.close()
                    
            if(DEBUG_USER_FNS) :
                print("import history file saved ok")
                            
        except :
            from dfcleanser.common.cfg import add_error_to_log, SEVERE_ERROR
            add_error_to_log("[Save dfc cfg file Error] "  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)


    def _parse_history_file_to_dict(self,history_file) :
        """
        * -------------------------------------------------------- 
        * function : convert the import history file into a dict
        * 
        * parms :
        *  history_file     -   history_file to convert                     
        *
        * returns : N/A
        * --------------------------------------------------------
        """
        
        total_entries    =   len(history_file)
        
        if(DEBUG_USER_FNS) :
            print("\n[parse_history_file_to_dict]  ",self.history_type,type(history_file),total_entries,"\n")
            for i in range(total_entries) :
                print("    [",i,"] ",history_file[i])
        
        try :
       
            for i in range(total_entries) :
            
                fname       =   history_file[i][0]
                fdesc       =   history_file[i][1]
                fcode       =   history_file[i][2]
            
                history_entry    =   userfnParms(fname,fdesc,fcode)
            
                self._add_entry_to_history_dict(history_entry)

        except Exception as e:
            from dfcleanser.common.cfg import add_error_to_log, SEVERE_ERROR
            add_error_to_log("[_parse_history_file_to_dict Error - for json decode error] "  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)
            
            title       =   "dfcleanser exception"
            status_msg  =   "[parse import/export file] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)


    
    def _add_entry_to_history_dict(self,history_entry) :
        """
        * -------------------------------------------------------- 
        * function : add an import history entry to the dict
        * 
        * parms :
        *  history_file     -   history_file to convert                     
        *
        * returns : N/A
        * --------------------------------------------------------
        """
        
        opstat  =   opStatus()
        
        try :
            
            if(self.user_fns_dict is None) :
        
                if(DEBUG_USER_FNS) :
                    print("\nadd_entry_to_history_dict - no import_type_dict")
                    print("add_entry_to_import_history_dict - history_entry.get_df_title()",history_entry.get_fn_name())
                
                self.user_fns_dict  =   {}
                self.user_fns_dict.update({ history_entry.get_fn_name() : history_entry})
            
            else :
            
                self.user_fns_dict.update({ history_entry.get_fn_name() : df_titles_dict })
            
        except Exception as e:

            opstat.set_status(False)

            title       =   "dfcleanser exception"
            status_msg  =   "[add_entry_to_history_dict] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            add_error_to_log("[add_entry_to_history_dict] "  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)


 

    def _parse_history_dict_to_list(self) :
        """
        * -------------------------------------------------------- 
        * function : convert the import history dict to a list 
        * 
        * parms :
        *
        * returns : N/A
        * --------------------------------------------------------
        """
        
        opstat  =   opStatus()
        
        if(DEBUG_IMPORT_HISTORY_DETAILS) :
            print("\n\nparse_history_dict_to_list")
            self.dump_history()
        
        try :
        
            history_data_list    =   []
        
            history_types    =   list(self.notebook_history.keys())
            history_types.sort()
        
            if(DEBUG_IMPORT_HISTORY_DETAILS) :
                print("\nparse_history_dict_to_list - history types",history_types)
        
            for i in range(len(history_types)) :
                df_titles_dict  =   self.notebook_history.get(history_types[i])
            
                if(DEBUG_IMPORT_HISTORY_DETAILS) :
                    print("\nparse_history_dict_to_list - history_type : ",history_types[i])
                    print("    df_titles_dict",len(df_titles_dict))
            
            
                df_titles    =   list(df_titles_dict.keys())
                df_titles.sort()
            
                if(DEBUG_IMPORT_HISTORY_DETAILS) :
                    print("\nparse_history_dict_to_list - df_titles",len(df_titles)," : ",df_titles)

                for j in range(len(df_titles)) :
                
                    history_entry        =   df_titles_dict.get(df_titles[j])
                
                    if(DEBUG_IMPORT_HISTORY_DETAILS) :
                        print("\nparse_history_dict_to_list - import_entry[",j,"]",type(history_entry),history_entry)
                
                    history_entry_list   =   []
                
                    history_entry_list.append(history_entry.get_file_type())
                    history_entry_list.append(history_entry.get_df_title())
                    history_entry_list.append(history_entry.get_full_parms())
                
                    history_entry_addl_parms_dict    =  history_entry.get_addl_parms() 
                
                    if(not (history_entry_addl_parms_dict is None)) :
                    
                        addl_parms_keys    =   list(history_entry_addl_parms_dict.keys())
                        addl_parms_keys.sort()
                
                        addl_parms_keys_list    =   []
                        addl_parms_vals_list    =   []
                
                        for k in range(len(addl_parms_keys)) :
                    
                            addl_parms_keys_list.append(addl_parms_keys[k])
                            addl_parms_vals_list.append(history_entry_addl_parms_dict.get(addl_parms_keys[k]))
                
                    else :
                    
                        addl_parms_keys_list    =   []
                        addl_parms_vals_list    =   []
                    
                    history_entry_list.append(addl_parms_keys_list)
                    history_entry_list.append(addl_parms_vals_list)
                    
                    history_data_list.append(history_entry_list)
                
            return(history_data_list)
    
        except Exception as e:

            opstat.set_status(False)

            title       =   "dfcleanser exception"
            status_msg  =   "[parse_history_dict_to_list] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)
            
            add_error_to_log("[parse_history_dict_to_list] "  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)


    """
    #--------------------------------------------------------------------------
    #   Dataframe Cleanser import history entry methods
    #--------------------------------------------------------------------------
    """

    def get_df_titles_for_file_type(self,fileType) :
        """
        * -------------------------------------------------------- 
        * function : get all import df titles for a file type 
        * 
        * parms :
        *  fileType     -   type of import                     
        *
        * returns : N/A
        * --------------------------------------------------------
        """
        
        if(DEBUG_IMPORT_HISTORY_DETAILS) :
            print("\n[get_df_titles_for_file_type] : fileType : self.history_file_loaded",fileType,self.history_file_loaded)
            print("[get_df_titles_for_file_type ]: file name ",self.get_history_full_file_name(self.history_type))
            
        if(not (self.history_file_loaded)) :
            self.load_history_file()    
        
        df_titles_dict  =   self.notebook_history.get(fileType)
        
        if(DEBUG_IMPORT_HISTORY_DETAILS) :
            print("\ndf_titles_dict : ",fileType,"\n",df_titles_dict)
        
        if(not (df_titles_dict is None)) :
            
            df_titles_list  =   list(df_titles_dict.keys())
            
            if(DEBUG_IMPORT_HISTORY_DETAILS) :
                print("\ndf_titles_list",df_titles_list)
                self.dump_history()
            
            if(not (df_titles_list is None)) :
                df_titles_list.sort()
                return(df_titles_list)
            else :
                return(None)
            
        else :
            
            return(None)
        
    def add_to_history(self,filetype,dfTitle,fullParms,addlParms) :
        """
        * -------------------------------------------------------- 
        * function : add a new import to history table
        * 
        * parms :
        *  fileType     -   type of history IMPORT or EXPORT                    
        *  dfTitle      -   dataframe title                   
        *  fullParms    -   import full parms                    
        *  addlParms    -   additional prms                   
        *
        * returns : N/A
        * --------------------------------------------------------
        """
       
        opstat  =   opStatus()
        
        if(DEBUG_IMPORT_HISTORY_DETAILS) :
            print("\n  [add_to_history] : filetype : dftitle : ",filetype,dfTitle)
            self.dump_history()    
        
        try :
            
            new_entry    =   DataframeCleanserHistoryParms(self.history_type,filetype,dfTitle,fullParms,addlParms)
        
            if(DEBUG_IMPORT_HISTORY_DETAILS) :
                print("  [add_to_history] : df : ",dfTitle," history type : ",self.history_type," filetype : ",filetype,"\n fullparms : ",fullParms,"\n addlparms : ",addlParms)
                print("  [add_to_history] - new_entry - dump")
                new_entry.dump()
            
            df_titles_dict  =   self.notebook_history.get(filetype)
        
            if(DEBUG_IMPORT_HISTORY_DETAILS) :
                print("  [add_to_history] : df_titles_dict\n",df_titles_dict)

            if(df_titles_dict is None) :
            
                new_type_dict    =   {}
                new_type_dict.update({dfTitle : new_entry})
                
                if(DEBUG_IMPORT_HISTORY_DETAILS) :
                    print("\nadd_to_history : new_type_dict",new_type_dict,filetype)
            
                self.notebook_history.update({filetype : new_type_dict})
            
            else :
            
                if(DEBUG_IMPORT_HISTORY_DETAILS) :
                    print("  [add_to_history] - df_titles_dict : ",type(df_titles_dict),len(df_titles_dict))
            
                df_titles_dict.update({dfTitle : new_entry})    
            
                if(DEBUG_IMPORT_HISTORY_DETAILS) :
                    print("  [add_to_history] - df_titles_dict : ",type(df_titles_dict),len(df_titles_dict),"\n dict : ",df_titles_dict)

                self.notebook_history.update({filetype : df_titles_dict})
        
            self.save_history_file() 
        
        except Exception as e:

            opstat.set_status(False)

            title       =   "dfcleanser exception"
            status_msg  =   "[add_to_history] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            add_error_to_log("[add_to_history] "  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)


        if(DEBUG_IMPORT_HISTORY_DETAILS) :
            print("  [add_import_to_history] - new_history : ")
            self.dump_history()

    def delete_from_history(self,filetype,dfTitle) :
        """
        * -------------------------------------------------------- 
        * function : adelete import from history table
        * 
        * parms :
        *  fileType     -   type of history IMPORT or EXPORT                    
        *  dfTitle      -   dataframe title                   
        *
        * returns : N/A
        * --------------------------------------------------------
        """
       
        opstat  =   opStatus()
        
        if(DEBUG_IMPORT_HISTORY) :
            print("\ndelete_from_history\n",filetype,"\n",dfTitle)
            
        df_titles_dict  =   self.notebook_history.get(filetype)
        
        if(not (df_titles_dict is None) ) :
            
            try :
                
                df_titles_dict.pop(dfTitle)
                self.save_history_file() 
                
            except Exception as e:

                opstat.set_status(False)

                title       =   "dfcleanser exception"
                status_msg  =   "[delete_from_history] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)
            
                add_error_to_log("[delete_from_history] "  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)

        
    def get_df_title_entry(self,fileType,dfTitle) :
        """
        * -------------------------------------------------------------------- 
        * function : get the import history entry for a file type and dftitle
        * 
        * parms :
        *  fileType     -   type of history IMPORT or EXPORT                    
        *  dfTitle      -   dataframe title                   
        *
        * returns : N/A
        * -------------------------------------------------------------------
        """
        
        if(DEBUG_IMPORT_HISTORY_DETAILS):
            print("    [get_df_title_entry] : filetype : ",fileType," dftitle : ",dfTitle)
        
        if(not (self.history_file_loaded)) :
            self.load_history_file()    
        
        df_titles_dict  =   self.notebook_history.get(fileType)
        
        if(DEBUG_IMPORT_HISTORY_DETAILS):
            dict_keys = list(df_titles_dict.keys())
            print("    [get_df_title_entry] : dftitles dict keys : \n   ",dict_keys)

        if(df_titles_dict is None) :
            return(None)
        else :
            
            if( (DEBUG_IMPORT_HISTORY_DETAILS) ):
                print("    [get_df_title_entry] : dfTitle len : ",len(dfTitle),dfTitle)

            df_title_dict   =   df_titles_dict.get(dfTitle)
            if(DEBUG_IMPORT_HISTORY_DETAILS) :
                print("    [get_df_title_entry] : df_title_dict : ",type(df_title_dict))
                if(not (df_title_dict is None)) :
                    df_title_dict.dump()
            
            return(df_title_dict)
             
    def dump_history(self) :
        """
        * -------------------------------------------------------------------- 
        * function : dump the history table
        * 
        * parms :
        *
        * returns : N/A
        * -------------------------------------------------------------------
        """
        
        hkeys   =   list(self.notebook_history.keys())
        
        print("\nhkeys",hkeys)
        
        for i in range(len(hkeys)) :
            print("\nfile type : ",hkeys[i])
            ftdict  =   self.notebook_history.get(hkeys[i])
            ftkeys  =   list(ftdict.keys())
            
            for j in range(len(ftkeys)) :
                print("\ndftitle : ",ftkeys[j])
                ftdict.get(ftkeys[j]).dump()





