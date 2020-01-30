"""
# sw_utility_model 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

import dfcleanser.common.cfg as cfg
import json



MAIN_OPTION                 =   0
LIST_OPTION                 =   1
DICT_OPTION                 =   2
ADD_LIST_OPTION             =   3
DELETE_LIST_OPTION          =   4
ADD_DICT_OPTION             =   5
DELETE_DICT_OPTION          =   6
CLEAR_LIST_OPTION           =   7
CLEAR_DICT_OPTION           =   8
SELECT_LIST_OPTION          =   9
SELECT_DICT_OPTION          =   10

FUNCS_OPTION                =   11

MAINT_LIST_OPTION           =   12
UPDATE_LIST_OPTION          =   13

MAINT_DICT_OPTION           =   15
UPDATE_DICT_OPTION          =   16



DICT_ID         =   0
LIST_ID         =   1

ReservedDicts   =   ["strftime","Elipsoids","Country_Codes","Language_Codes","ArcGIS_Categories","US_States_and_Territories","Canadian_Provinces_and_Territories"]
ReservedLists   =   ["Google_Address_Components", "Google_Location_Types"]


Red             =   "#FAA78F"
Green           =   "#8FFAC0"
Yellow          =   "#FAFB95"


USER_LISTS_FILE_NAME   =   "dfc_user_lists.json"

"""
* -----------------------------------------------------------------------*
* user lists storage class
* -----------------------------------------------------------------------*
"""
class userListsStore :

    def __init__(self) :

        # instance variables
        self.userListsDict    =   {}
        self.load_user_lists_file()
    
    def get_user_lists_file_name(self) :
        
        import os
        return(os.path.join(cfg.get_common_files_path(),USER_LISTS_FILE_NAME))
    
    def load_user_lists_file(self) :
        
        fname   =    self.get_user_lists_file_name() 
        if(not (fname == None)) :
        
            try :
                with open(fname, 'r') as user_lists_file :
                    self.userListsDict = json.load(user_lists_file)#serial_gen_func_dict = json.load(gen_func_file)
                    user_lists_file.close()
               
            except FileNotFoundError :
                print("[file not found error load gen_func file ...]",str(sys.exc_info()[0]))
                self.genericfunctionDict = {}
            except :
                print("[error load gen_func file ...]",str(sys.exc_info()[0]))
                self.genericfunctionDict = {}
    
    def save_user_lists_file(self) :
        
        fname   =    self.get_user_lists_file_name() 
        if(not (fname == None)) :
            
            if(len(self.userListsDict) > 0) :
    
                try :
            
                    with open(fname, 'w') as user_lists_file :
                        json.dump(self.userListsDict,user_lists_file)
                        user_lists_file.close()
                
                except :
                    print("[save_generic_functions_file error] : " + str(sys.exc_info()[0]))
                        
            else :
                    
                import os 
                os.remove(self.get_functions_file_name())
            
    def add_list(self,listname,userlist) :
        self.userListsDict.update({listname:userlist})
        self.save_user_lists_file()
            
    def get_total_user_lists(self) :
        if(self.userListsDict == {}) :
            self.load_user_lists_file()    
        return(len(self.userListsDict))
    
    def get_user_lists_list(self) :
        return(list(self.userListsDict.keys()))
        
    def delete_user_list(self,listtitle) :
        try :
            del self.userListsDict[listtitle]
        except :
            print("key not found")
            
            
        self.save_user_lists_file()
        
    def get_user_list(self,listtitle) :
        return(self.userListsDict.get(listtitle))
        
        

"""
# -----------------------------------------------------------------
#                   static gewneric function store
# -----------------------------------------------------------------
"""        
UserLists   =   userListsStore()
    
 



