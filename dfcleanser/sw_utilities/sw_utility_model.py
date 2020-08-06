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

from dfcleanser.common.html_widgets import (new_line)
from dfcleanser.common.common_utils import (display_exception, opStatus)
from dfcleanser.common.cfg import add_error_to_log



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

LOAD_DICT_OPTION            =   18
LOAD_LIST_OPTION            =   19

FUNCS_OPTION                =   11

MAINT_LIST_OPTION           =   12
UPDATE_LIST_OPTION          =   13

MAINT_DICT_OPTION           =   15
UPDATE_DICT_OPTION          =   16



DICT_ID         =   0
LIST_ID         =   1

ReservedDicts       =   ["ArcGIS_Categories","Canadian_Provinces_and_Territories","Country_Codes","Elipsoids","Language_Codes","State_Cities","State_Counties","State_County_Cities","strftime","US_States_and_Territories"]
ReservedLists       =   ["Google_Address_Components", "Google_Location_Types","US_Zipcodes"]


DATA_TYPE       =   0
FILE_TYPE       =   1


ReservedDictsType   =   [DATA_TYPE,DATA_TYPE,DATA_TYPE,DATA_TYPE,DATA_TYPE,FILE_TYPE,FILE_TYPE,FILE_TYPE,DATA_TYPE,DATA_TYPE]
ReservedListsType   =   [DATA_TYPE,DATA_TYPE]


Red             =   "#FAA78F"
Green           =   "#8FFAC0"
Yellow          =   "#FAFB95"


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   DictList class static helper functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
DFC_CREATED         =   0
USER_CREATED        =   1


"""
#--------------------------------------------------------------------------
#   Dict methods
#--------------------------------------------------------------------------
"""
def get_Dict(dictname,creator=DFC_CREATED) :
    return(dfcDataStructures.get_Item(DICT_ID,dictname,creator))
    
def add_Dict(dictname,newdict,creator,filename=None) :
   dfcDataStructures.add_Item(DICT_ID,dictname,creator,newdict,filename)

def delete_Dict(dictname,creator) :
    dfcDataStructures.delete_Item(DICT_ID,dictname,creator) 
    
def update_Dict(dictname,newdict,creator) :
    dfcDataStructures.update_Item(DICT_ID,dictname,creator,newdict) 
    
def get_dicts_names(creator) :
    return(dfcDataStructures.get_dict_names(creator))
    
def get_pretty_dict(indict,inkeys) :
    
    dicttext = "{" 
    for i in range(len(inkeys)) :
        dicttext = (dicttext + '"' + str(inkeys[i]) + '" : ' + '"' + str(indict.get(inkeys[i])) + '"')   
        if(i != (len(inkeys) -1)) :
            dicttext = (dicttext + "," + new_line)
        else :
            dicttext = (dicttext + "}")
        
    return(dicttext)

"""
#--------------------------------------------------------------------------
#   List methods
#--------------------------------------------------------------------------
"""
def get_List(listname,creator=DFC_CREATED) :
    return(dfcDataStructures.get_Item(LIST_ID,listname,creator))
    
def add_List(listname,newlist,creator,filename=None) :
    dfcDataStructures.add_Item(LIST_ID,listname,creator,newlist,filename)

def delete_List(listname,creator) :
    dfcDataStructures.delete_Item(LIST_ID,listname,creator) 

def update_List(listname,newlist,creator) :
    dfcDataStructures.update_Item(LIST_ID,listname,creator,newlist) 

def get_lists_names(creator) :
    return(dfcDataStructures.get_list_names(creator))
    

def get_Listlog() :
    return(dfcDataStructures.get_log(LIST_ID)) 

COMMON_DICTS_FILE_NAME      =   "\dfcleanserCommon_dictlog.json"
COMMON_LISTS_FILE_NAME      =   "\dfcleanserCommon_listlog.json"

USER_DICTS_FILE_NAME        =   "\dfcleanserUser_dictlog.json"
USER_LISTS_FILE_NAME        =   "\dfcleanserUser_listlog.json"



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser data strucrures storage class
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
class DataframeCleanserDataStructureStore :

    # full constructor
    def __init__(self) :
        
        # instance variables
        self.dictStore          =   {}
        self.listStore          =   {}
        
        self.userdictStore      =   {}
        self.userlistStore      =   {}

        self.load_datastructures_file(DICT_ID,DFC_CREATED)
        self.load_datastructures_file(LIST_ID,DFC_CREATED)
        
        self.load_datastructures_file(DICT_ID,USER_CREATED)
        self.load_datastructures_file(LIST_ID,USER_CREATED)
        

    def get_datastructures_file_name(self,dstype,creator) :
        
        if(dstype == DICT_ID) :
            if(creator == DFC_CREATED) :
                path = cfg.get_common_files_path() + COMMON_DICTS_FILE_NAME
            else :
                path = cfg.get_common_files_path() + USER_DICTS_FILE_NAME
                
            return(path)
            
        else :
            
            if(creator == DFC_CREATED) :
                path = cfg.get_common_files_path() + COMMON_LISTS_FILE_NAME
            else :
                path = cfg.get_common_files_path() + USER_LISTS_FILE_NAME
                
            return(path)

    def load_datastructures_file(self,dstype,creator) :

        try :
            with open(self.get_datastructures_file_name(dstype,creator), 'r') as datastructures_file :
                if(dstype == DICT_ID) :
                    if(creator == DFC_CREATED) :
                        self.dictStore = json.load(datastructures_file)
                    else :
                        self.userdictStore = json.load(datastructures_file) 
                else :
                    if(creator == DFC_CREATED) :
                        self.listStore = json.load(datastructures_file)
                    else :
                        self.userlistStore = json.load(datastructures_file)
                   
                datastructures_file.close()
                
        except Exception as e:
            
            if(dstype == DICT_ID) :
                
                if(creator == DFC_CREATED) :
                    self.dictStore          =   {}
                else :
                    self.userdictStore      =   {}
                    
            else :
                
                if(creator == DFC_CREATED) :
                    self.listStore          =   {}
                else :
                    self.userlistStore      =   {}

            opstat = opStatus()
            opstat.store_exception("Unable to load common file :  " + self.get_datastructures_file_name(dstype,creator),e)
            display_exception(opstat)
    
    def save_datastructures_file(self,dstype,creator) :
        
        try :
            with open(self.get_datastructures_file_name(dstype,creator), 'w') as datastructures_file :
                if(dstype == DICT_ID) :
                    if(creator == DFC_CREATED) :
                        json.dump(self.dictStore,datastructures_file)
                    else :
                        json.dump(self.userdictStore,datastructures_file)
                else :
                    if(creator == DFC_CREATED) :                    
                        json.dump(self.listStore,datastructures_file)
                    else :
                        json.dump(self.userlistStore,datastructures_file)
                    
                datastructures_file.close()
                
        except Exception as e:
            opstat = opStatus()
            opstat.store_exception("Unable to save file " + self.get_datastructures_file_name(dstype,creator),e)
            display_exception(opstat)


    def get_item_from_file(self,itemtype,itemname,creator) :
        
        import os
        
        #print("get_item_from_file",itemtype,itemname,creator)
        
        if(creator == DFC_CREATED) :
            
            if(itemtype == DICT_ID) :
                dsitem    =   self.dictStore.get(itemname,None)
            else :
                dsitem    =   self.listStore.get(itemname,None)
                
        else :
            
            if(itemtype == DICT_ID) :
                dsitem    =   self.userdictStore.get(itemname,None)
            else :
                dsitem    =   self.userlistStore.get(itemname,None)
            
        #print("dsitem",dsitem)                 
        if(not(dsitem is None)) :
        
            fname   =   os.path.join(cfg.get_common_files_path(),"datastructures")
            fname   =   os.path.join(fname,dsitem[1])
            #print("fname",fname)        
            if(not (fname is None)) :
            
                try :                
                    with open(fname, 'r') as ds_file :
                        ds = json.load(ds_file)
                        ds_file.close()
                    
                    return(ds)
                    
                except :
                    add_error_to_log("[Get Dict from File - no file name] " + itemname + str(sys.exc_info()[0].__name__))

                    return(None)  
                    
            else :
                add_error_to_log("[Dict not found] " + itemname)

                return(None)
                
        else :
            return(None)
            
            
    def get_dict_from_file(self,itemname,creator) :
        
        return(self.get_item_from_file(DICT_ID,itemname,creator))
    
        
    def get_list_from_file(self,itemname,creator) :
                        
        return(self.get_item_from_file(LIST_ID,itemname,creator))
        

    def get_Item(self,dstype,itemname,creator) :
        
        #print("get_Item",dstype,itemname,creator)

        if(dstype == DICT_ID) :
            
            if(creator == DFC_CREATED) : 
                
                if(self.dictStore == {}) :    self.load_datastructures_file(dstype,creator)  
                dictitem    =  self.dictStore.get(itemname,None)
                #print("dictitem",dictitem,type(dictitem))
                if(not (dictitem is None)) :
                    
                    if(dictitem[0] == DATA_TYPE) :
                        return(dictitem[1])
                    else :
                        return(self.get_dict_from_file(itemname,creator)) 
                        
                else :    
                    return(None)
                    
            else :
                
                if(self.userdictStore == {}) :    self.load_datastructures_file(dstype,creator) 
                dictitem    =  self.userdictStore.get(itemname,None)
                
                if(not (dictitem is None)) :
                    
                    if(dictitem[0] == DATA_TYPE) :
                        return(dictitem[1])
                    else :
                        return(self.get_dict_from_file(itemname,creator)) 
                        
                else :    
                    return(None)
                
        else :
            
            if(creator == DFC_CREATED) :    
                if(self.listStore == {}) :    self.load_datastructures_file(dstype,creator) 
                listitem    =  self.listStore.get(itemname,None)
                
                if(not (listitem is None)) :
                    
                    if(listitem[0] == DATA_TYPE) :
                        return(listitem[1])
                    else :
                        return(self.get_list_from_file(itemname,creator)) 

                else :    
                    return(None)
                
            else :
                
                if(self.userlistStore == {}) :    self.load_datastructures_file(dstype,creator) 
                listitem    =  self.userlistStore.get(itemname,None)
                
                if(not (listitem is None)) :
                    
                    if(listitem[0] == DATA_TYPE) :
                        return(listitem[1])
                    else :
                        return(self.get_list_from_file(itemname,creator)) 
                        
                else :    
                    return(None)
            
    def add_Item(self,dstype,name,creator,newitem,filename=None) :
        
        if(dstype == DICT_ID) : 
            if(creator == DFC_CREATED) :  
                if(filename is None) :
                    self.dictStore.update({name : [ DFC_CREATED, newitem]})
                else :
                    self.dictStore.update({name : [ DFC_CREATED, filename]})
            else :
                if(filename is None) :
                    self.userdictStore.update({name : [ USER_CREATED, newitem]})
                else :
                    self.userdictStore.update({name : [ USER_CREATED, filename]})
        else :
            if(creator == DFC_CREATED) : 
                if(filename is None) :
                    self.listStore.update({name : [ DFC_CREATED, newitem]})
                else :
                    self.listStore.update({name : [ DFC_CREATED, filename]})                    
            else :
                if(filename is None) :
                    self.userlistStore.update({name : [ USER_CREATED, newitem]})
                else :
                    self.userlistStore.update({name : [ USER_CREATED, filename]})
            
        self.save_datastructures_file(dstype,creator)


    def update_Item(self,dstype,name,creator,dsitem) :
        
        #print("update_Item",dstype,name,creator,"\n",dsitem)
        
        if(dstype == DICT_ID) : 
            if(creator == DFC_CREATED) :  
                add_error_to_log("Can not update DFC Dict : " + name)
                
            else :
                
                current_dict    =   self.userdictStore.get(name,None)
                if(not (current_dict is None)) :
                    if(current_dict[0] == DATA_TYPE) :
                        self.userdictStore.update({name : dsitem}) 
                    else :
                        
                        filename    =   current_dict[1]
                        
                        try :
                            
                            with open(filename, 'w') as dsdict_file :
                                json.dump(dsitem,dsdict_file)
                                dsdict_file.close()
                            
                        except :
                            add_error_to_log("Can not update DFC Dict : " + name)
                            
                else :
                    add_error_to_log("DFC Dict : " + name + " not in user dicts ")

                            
        else :
            
            if(creator == DFC_CREATED) : 
                add_error_to_log("Can not update DFC List : " + name)
                
            else :
                
                current_list    =   self.userlistStore.get(name,None)
                if(not (current_list is None)) :
                    if(current_list[0] == DATA_TYPE) :
                        self.userlistStore.update({name : dsitem}) 
                    else :
                        
                        filename    =   current_list[1]
                        
                        #print("filename",filename)
                        
                        try :
                            
                            with open(filename, 'w') as dslist_file :
                                json.dump(dsitem,dslist_file)
                                dslist_file.close()
                            
                        except :
                            add_error_to_log("Can not update DFC List : " + name)
                            
                else :
                    add_error_to_log("DFC List : " + name + " not in user lists ")
                
            
        self.save_datastructures_file(dstype,creator)


    def delete_Item(self,dstype,creator,name) :
        if(dstype == DICT_ID) :  
            if(creator == DFC_CREATED) :
                self.dictStore.pop(name,None)
            else :
                self.userdictStore.pop(name,None)
        else :
            if(creator == DFC_CREATED) :
                self.listStore.pop(name,None) 
            else :
                self. userlistStore.pop(name,None) 
            
        self.save_datastructures_file(dstype,creator)

    def get_dict_names(self,creator) :
        if(creator == DFC_CREATED) :
            return(ReservedDicts)
        else :
            names   =   self.userdictStore.keys()
            if(not (names is None)) :
                names   =   list(names)
                names.sort()
            
            if(len(names) > 0) :
                return(names)
            else :
                return(None)

    def get_list_names(self,creator) :
        if(creator == DFC_CREATED) :
            return(ReservedLists)
        else :
            names   =   self.userlistStore.keys()
            if(not (names is None)) :
                names   =   list(names)
                names.sort()
                
            if(len(names) > 0) :
                return(names)
            else :
                return(None)

    def get_log(self,id) :
        if(id == DICT_ID) : 
            if(self.dictlog == {}) :    self.load_Log_file(id)    
            return(self.dictlog) 
        else :
            if(self.listlog == {}) :    self.load_Log_file(id)    
            return(self.listlog) 
            

"""
* ----------------------------------------------------
# instantiation of the dict data object
* ----------------------------------------------------
"""    
dfcDataStructures    =   DataframeCleanserDataStructureStore()



