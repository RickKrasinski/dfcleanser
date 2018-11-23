"""
# cfg 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

import json 
import os

"""
#--------------------------------------------------------------------------
#   local helper functions
#--------------------------------------------------------------------------
"""
def display_javascript_HTML(html) :
    from IPython.core.display import display 
    display(html)#, metadata=dict(isolated=True))


def run_javascript(jscript, errmsg, errtitle) :

    try :            
        from IPython.core.magics.display import Javascript
        display_javascript_HTML(Javascript(jscript))
    except :
        print(errmsg,jscript)
        
        
        

NOTEBOOK_TITLE          =   "NoteBookName"
NOTEBOOK_PATH           =   "NoteBookPath"
DFC_CELLS_LOADED        =   "dfCcellsLoaded"
DFC_CELLS_CBS           =   "dfCcellcbs"


DataCleansing_ID        =   "DataCleansing"
DataExport_ID           =   "DataExport"
DataImport_ID           =   "DataImport"
DataInspection_ID       =   "DataInspection"
DataScripting_ID        =   "DataScripting"
DataTransform_ID        =   "DataTransform"
SWUtilities_ID          =   "SWUtilities"
SWDFSubsetUtility_ID    =   "SWDFSubsetUtility"
SWGeocodeUtility_ID     =   "SWGeocodeUtility"
System_ID               =   "System"
DBUtils_ID              =   "DBUtils"
DumpUtils_ID            =   "DumpUtils"
Help_ID                 =   "Help"
GenFunction_ID          =   "GenFunction"
SWDFConcatUtility_ID    =   "SWDFConcatUtility"


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   DC Dataframe helper methods
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def is_dc_dataframe_loaded(title=None) :
    return(DCdf.is_dataframe_set(title)) 
   
def set_dc_dataframe(df,title=None) :
    DCdf.set_dataframe(df,title)
    
def get_dc_dataframe(title=None) :
    return(DCdf.get_dataframe(title))
    
def rename_default_dc_dataframe(title) :
    DCdf.name_default_dataframe(title)

def drop_dc_dataframe(title=None) :
    DCdf.drop_dataframe(title)


class DCDataframes :
    
    dcdataframes    =   {}
    default_df      =   ""

    def __init__(self):
        self.dcdataframes = {}
        #print("dc dataframe init")
        
    def set_dataframe(self,df,title=None) :
        if(title == None) :
            self.dcdataframes.update({"default" : df})
        else :
            self.dcdataframes.update({title : df})
        
    def get_dataframe(self,title=None) :
        if(title == None) :
            return(self.dcdataframes.get("default"))
        else :
            return(self.dcdataframes.get(title))
    
    def rename_default_dataframe(self,title) :
        if(title == None) :
            return(self.dcdataframes.get("default"))
        else :
            return(self.dcdataframes.get(title))
        
    def drop_dataframe(self,title=None) :
        if(title == None) :
            if(self.get_dataframe("default") is not None) :
                self.dcdataframes.pop("default")
        else :
            if(self.get_dataframe(title) is not None) :
                self.dcdataframes.pop(title)

    def is_dataframe_set(self,title=None) :
        if(title == None) :
            tdf = self.get_dataframe("default")
            if(type(tdf) != type(None)) :
                return(True)
            else :
                return(False)
        else :
            if(self.get_dataframe(title) == None) :
                return(False)
            else :
                return(True)

DCdf = DCDataframes()


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser config value keys
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

GLOBAL      =   False
LOCAL       =   True



"""
#--------------------------------------------------------------------------
#   DBUtils config value keys
#--------------------------------------------------------------------------
"""
CURRENT_DB_ID_KEY           =   "currentDBID"
CURRENT_DBLIB_ID_KEY        =   "currentDBLIBID"

"""
#--------------------------------------------------------------------------
#   Cleansing config value keys
#--------------------------------------------------------------------------
"""
UNIQUES_FLAG_KEY                        =   "columnUniquesDisplay"
UNIQUES_RANGE_KEY                       =   "columnUniquesRange"

OUTLIERS_FLAG_KEY                       =   "columnOutliersDisplay"
DATA_TYPES_FLAG_KEY                     =   "columnDataTypeChange"
ROUNDING_FLAG_KEY                       =   "roundcolumn"

CLEANSING_COL_KEY                       =   "datacleansingcolumn"
CLEANSING_ROW_KEY                       =   "datacleansingrow"

OBJ_TYPE_PARM_KEY                       =   "objtypeparm"
OBJ_DATA_TYPES_FLAG_KEY                 =   "colsDataTypeChange"
OBJ_ROUNDING_FLAG_KEY                   =   "colsroundcolumn"

GRAPHS_FLAG_KEY                         =   "graphcolumn"

"""
#--------------------------------------------------------------------------
#   Export config value keys
#--------------------------------------------------------------------------
"""
CURRENT_EXPORTED_FILE_NAME_KEY          =   "currentEXportedFileName"

"""
#--------------------------------------------------------------------------
#   Import config value keys
#--------------------------------------------------------------------------
"""
CURRENT_IMPORTED_DATA_SOURCE_KEY        =   "currentImportedDataSource"
CURRENT_SQL_IMPORT_ID_KEY               =   "currentSQLImportID"

MYSQL_IMPORT_PARMS_KEY                  =   "MySqlImportParms"
MSSQL_IMPORT_PARMS_KEY                  =   "MSSqlServerImportParms"
SQLITE_IMPORT_PARMS_KEY                 =   "SqliteImportParms"
POSTGRESQL_IMPORT_PARMS_KEY             =   "PostgresqlImportParms"
ORACLE_IMPORT_PARMS_KEY                 =   "OracleImportParms"
CUSTOM_IMPORT_PARMS_KEY                 =   "CustomImportParms"

"""
#--------------------------------------------------------------------------
#   Inspection config value keys
#--------------------------------------------------------------------------
"""
DATA_TYPES_CBOX_0_KEY                   =   "data_inspection_cb0"
NANS_CBOX_1_KEY                         =   "data_inspection_cb1"
ROWS_CBOX_2_KEY                         =   "data_inspection_cb2"
COLS_CBOX_3_KEY                         =   "data_inspection_cb3"
CATS_CBOX_4_KEY                         =   "data_inspection_cb4"

"""
#--------------------------------------------------------------------------
#   Transform config value keys
#--------------------------------------------------------------------------
"""
DATA_TRANSFORM_COL_SELECTED_KEY         =   "DT_ColumnsSelected"
MAP_TRANSFORM_COL_NAME_KEY              =   "DT_MapColumnName"
MOVE_COL_ID_KEY                         =   "MoveColumnId"
MOVE_AFTER_COL_ID_KEY                   =   "MoveAfterColumnId"
ADD_COL_COL_NAME_KEY                    =   "AddColumnColName"
ADD_COL_DATATYPE_ID_KEY                 =   "AddColumnDataType"
ADD_COL_CODE_KEY                        =   "AddColumnCode"
COPY_COL_TO_KEY                         =   "CopyColumnTo"
COPY_COL_FROM_KEY                       =   "CopyColumnFrom"

"""
#--------------------------------------------------------------------------
#   Scripting config value keys
#--------------------------------------------------------------------------
"""
SCRIPT_LOG_KEY                          =   "ScriptLog"
BACKUP_SCRIPT_LOG_KEY                   =   "BackupScriptLog"
SCRIPTING_FLAG_KEY                      =   "ScriptingFlag"

"""
#--------------------------------------------------------------------------
#   SW Utilities config value keys
#--------------------------------------------------------------------------
"""
CURRENT_GEOCODER_KEY                    =   "currentGeocoder"
ARCGIS_BATCH_MAX_BATCH_SIZE_KEY         =   "arcgisMaxBatchSize"
ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY   =   "arcgisSuggestedBatchSize"
BULK_GEOCODE_MODE_KEY                   =   "bulkGeocodeMode"

"""
#--------------------------------------------------------------------------
#   System config value keys
#--------------------------------------------------------------------------
"""
CORE_CBS_KEY                            =   "dfc_core_cbs"
UTILITIES_CBS_KEY                       =   "dfc_utilities_cbs"
SCRIPTING_CBS_KEY                       =   "dfc_scripting_cbs"
LAST_TASK_BAR_ID_KEY                    =   "lastsystemtaskbarid"
EULA_FLAG_KEY                           =   "EULARead"
SAVED_FILE_NAME_KEY                     =   "DCS_savedfilenname"
DFC_CURRENTLY_LOADED_KEY                =   "dfcleanserCurrentlyLoaded"
DFC_CHAPTERS_LOADED_KEY                 =   "dfcCurrentlyLoadedChapters"

"""
#--------------------------------------------------------------------------
#   working column name
#--------------------------------------------------------------------------
"""
CURRENT_COL_NAME    =   "currentColumnName"

def get_current_col_name() :
    return(get_config_value(CURRENT_COL_NAME))


GlobalKeys          =   [EULA_FLAG_KEY,ARCGIS_BATCH_MAX_BATCH_SIZE_KEY,ARCGIS_BATCH_SUGGESTED_BATCH_SIZE_KEY]
GlobalParmsKeys     =   ["geocoder"]





"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Dataframe Cleanser config data helper functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   dfcleanser notebook specific cfg values methods
#--------------------------------------------------------------------------
"""
def get_notebook_name() :
    run_javascript("window.getNotebookName();","Javascript Error","Unable to get notebook name")
def get_notebook_path() :
    run_javascript("window.getNotebookPath();","Javascript Error","Unable to get notebook path")
def get_notebook_location() :
    run_javascript("window.getNotebookLocation();","Javascript Error","Unable to get notebook location")


    
"""
#--------------------------------------------------------------------------
#   dfcleanser global config helper methods
#--------------------------------------------------------------------------
"""
#--------------------------------------------------------------------------
#   dfcleanser notebook specific cfg values methods
#--------------------------------------------------------------------------
def set_notebookName(nbname) :
    print("set_notebook_name",nbname)
    DataframeCleanserCfgData.set_notebookName(nbname)
def get_notebookName() :
    return(DataframeCleanserCfgData.get_notebookName())  
def set_notebookPath(nbpath) :
    print("set_notebook_path",nbpath)
    DataframeCleanserCfgData.set_notebookPath(nbpath)
def get_notebookPath() :
    return(DataframeCleanserCfgData.get_notebookPath())  

#--------------------------------------------------------------------------
#   dfcleanser generic cfg values methods
#--------------------------------------------------------------------------
def get_config_value(key, local=True) :
    return(DataframeCleanserCfgData.get_config_value(key,local))
def set_config_value(key, value, local=True) :
    DataframeCleanserCfgData.set_config_value(key,value,local)
def drop_config_value(key, local=True) :
    DataframeCleanserCfgData.drop_config_value(key,local)
def get_config_data() :
    return(DataframeCleanserCfgData.get_config_data())
def get_dfc_config_data() :
    return(DataframeCleanserCfgData.get_dfc_config_data())


"""
#--------------------------------------------------------------------------
#   dfcleanser config init functions
#--------------------------------------------------------------------------
"""
def get_chapters_loaded_cbs() :
    
    cellsList   =   get_config_value(DFC_CHAPTERS_LOADED_KEY)
    
    corecbs     =   [0,0,0,0,0]
    utilcbs     =   [0,0,0,0,0]
    scriptcbs   =   [0]

    if(not (cellsList == None)) :
        
        if(cellsList[1])     :   corecbs[0] = 1
        if(cellsList[3])     :   corecbs[1] = 1
        if(cellsList[4])     :   corecbs[2] = 1
        if(cellsList[5])     :   corecbs[3] = 1
        if(cellsList[7])     :   corecbs[4] = 1
    
        if(cellsList[9])     :   utilcbs[0] = 1
        if(cellsList[10])    :   utilcbs[1] = 1
        if(cellsList[12])    :   utilcbs[2] = 1
        if(cellsList[13])    :   utilcbs[3] = 1
        if(cellsList[14])    :   utilcbs[4] = 1
    
        if(cellsList[15])    :   scriptcbs[0] = 1

    return([corecbs,utilcbs,scriptcbs])
    

def set_chapters_loaded(cellsList) :
    
    print("set_chapters_loaded",cellsList)
    set_config_value(DFC_CHAPTERS_LOADED_KEY, cellsList)
    
    cblist  =   get_chapters_loaded_cbs()
    
    set_config_value(CORE_CBS_KEY,cblist[0])
    set_config_value(UTILITIES_CBS_KEY,cblist[1])
    set_config_value(SCRIPTING_CBS_KEY,cblist[2])
    set_config_value(DFC_CURRENTLY_LOADED_KEY,True)

def get_loaded_cells() :
    run_javascript("window.getdfCChaptersLoaded();","Javascript Error","Unable to get cells loaded")

def init_dc_data() :
    
    if(DataframeCleanserCfgData.get_notebookName() == None) :
        run_javascript("window.getNotebookName();","Javascript Error","Unable to get Notebook Name")
    if(DataframeCleanserCfgData.get_notebookPath() == None) :    
        run_javascript("window.getNotebookPath();","Javascript Error","Unable to get Notebook Path")
        
    get_loaded_cells()
    
def check_if_dc_init() :
    
    if( not(DataframeCleanserCfgData.get_notebookName() == None) ) :
        if( not(DataframeCleanserCfgData.get_notebookPath() == None) ) :  
            return(True)
    else :
        init_dc_data()
        return(False)



def get_common_files_path() :
    common_files_path = os.path.join(get_dfcleanser_location(),"files")
    return(common_files_path + "\\")   

def get_notebook_files_path() :
    notebook_files_path = os.path.join(get_dfcleanser_location(),"files","notebooks")
    return(notebook_files_path + "\\")   


def get_dfcleanser_location()  :

    import os
    import dfcleanser
    ppath = os.path.abspath(dfcleanser.__file__)
    #print("dfc path",dcfpath)   

    initpyloc = ppath.find("__init__.py")
    if(initpyloc > 0) :
        ppath = ppath[:initpyloc]

    return(ppath)

"""
#--------------------------------------------------------------------------
#   Dataframe Cleanser config class
#--------------------------------------------------------------------------
"""

class DataframeCleansercfg :
    
    # instance variables
    cfg_data                =   {}
    dfc_cfg_data            =   {}
    default_dfc_cfg_data    =   {}

    notebook_pids           =   {}
    notebookcfg_data        =   {}

    # full constructor
    def __init__(self) :
        
        self.cfg_data               =   {"EULARead":"true"}
        self.dfc_cfg_data           =   {}
        self.default_dfc_cfg_data   =   {"EULARead":"true"}

        self.notebookName           =   ""
        self.notebookPath           =   ""
       
        get_notebook_path()
        get_notebook_name()
        
        self.load_dfc_cfg_file()        
        
    def get_cfg_file_name(self) :
        return(get_notebook_files_path() + self.get_notebookName() + "_config.json")

    def load_cfg_file(self) :

        try :
            if(len(self.get_notebookName()) > 0) :
                with open(self.get_cfg_file_name(), 'r') as cfg_file :
                    self.cfg_data = json.load(cfg_file)
                    cfg_file.close()
        except :
            if(len(self.get_notebookName()) > 0) :
                print("[load_config_file Error] " + "[" + self.get_cfg_file_name() + "]" + str(sys.exc_info()[0].__name__))
    
    def save_cfg_file(self) :
    
        try :
            if(len(self.get_notebookName()) > 0) :
                with open(self.get_cfg_file_name(), 'w') as cfg_file :
                    json.dump(self.cfg_data,cfg_file)
                    cfg_file.close()
        except :
            if(len(self.get_notebookName()) > 0) :
                print("[save_config_file Error] " + "[" + self.get_cfg_file_name() + "]" + str(sys.exc_info()[0].__name__))
            
    def get_config_data(self) :
        return(self.cfg_data)            
    
    def get_config_value(self,key,local) :
        
        if(local) :
            if(self.cfg_data.get(key) == None) :
                self.load_cfg_file()
                return(self.cfg_data.get(key))
            else :
                return(self.cfg_data.get(key))
        else :
            return(self.get_dfc_config_value(key))    
    
    def set_config_value(self, key, value, local) :
        
        if(local) :
            try :
                self.cfg_data.update({key: value})
            except :
                print("[error set cfg value] ",key,self.cfg_data,str(sys.exc_info()[0].__name__))
                self.load_cfg_file()
        
            self.save_cfg_file()
            
        else :
            self.set_dfc_config_value(key, value)    
            
    def drop_config_value(self, key, local) :
        
        if(local) :
            try :
                self.cfg_data.pop(key,None)
            except :
                print("[error drop cfg value] ",key,self.cfg_data,str(sys.exc_info()[0].__name__))
                self.load_cfg_file()
        
            self.save_cfg_file() 
        else :
            self.drop_dfc_config_value(key)

    #---------------------------------------------------
    #   dfcleanser high value parms
    #---------------------------------------------------    
    def set_notebookName(self,nbname) :
        if(len(self.notebookName) == 0) :
            self.notebookName = nbname
            self.load_cfg_file()
        else :
            self.notebookName = nbname
    def get_notebookName(self) :
        return(self.notebookName) 
    def set_notebookPath(self,nbpath) :
        self.notebookPath = nbpath
        print("self.notebookPath",self.notebookPath)
    def get_notebookPath(self) :
        return(self.notebookPath) 

        
    #---------------------------------------------------
    #   dfcleanser global cfg values 
    #---------------------------------------------------    
    def get_dfc_cfg_file_name(self) :
        return(get_common_files_path() + "dfcleanserCommon" + "_config.json")
        
    def load_dfc_cfg_file(self) :
        try :
            with open(self.get_dfc_cfg_file_name(), 'r') as dfc_cfg_file :
                self.dfc_cfg_data = json.load(dfc_cfg_file)
                dfc_cfg_file.close()
        except :
            print("[load_notebook_cfg] " + "[" + self.get_dfc_cfg_file_name() + "]" + str(sys.exc_info()[0].__name__))
    
    def save_dfc_cfg_file(self) :

        try :
            with open(self.get_dfc_cfg_file_name(), 'w') as dfc_cfg_file :
                json.dump(self.dfc_cfg_data,dfc_cfg_file)
                dfc_cfg_file.close()
        except :
            if(not (self.get_nb_cfg_file_name() == None) ) :
                print("[save_notebook_cfg] " + "[" + self.get_dfc_cfg_file_name() + "]" + str(sys.exc_info()[0].__name__))
    
    def get_dfc_config_data(self) :
        return(self.dfc_cfg_data)            

    def get_dfc_config_value(self ,key) :
        if(self.dfc_cfg_data.get(key) == None) :
            self.load_dfc_cfg_file()
        return(self.dfc_cfg_data.get(key))    
        
    def set_dfc_config_value(self, key, value) :
        self.dfc_cfg_data.update({key: value})
        self.save_dfc_cfg_file()
    
    def drop_dfc_config_value(self, key) :
        try :
            self.dfc_cfg_data.pop(key,None)
        except :
            self.load_dfc_cfg_file()
        
        self.save_dfc_cfg_file()

        
"""
* ----------------------------------------------------
# instantiation of the config data object
* ----------------------------------------------------
"""    
DataframeCleanserCfgData    =   DataframeCleansercfg()











def create_notebook_dir_and_cfg_files(notebookname,nbpath) :
    
    # create the proper dir
    os.chdir(os.path.join(nbpath))
    os.makedirs("./" + notebookname + "_files" + "/")
    os.chdir(nbpath + "/" + notebookname + "_files")
                
    # create the notebook specific files
    fname = notebookname + "_config.json"
    initcfg = {NOTEBOOK_TITLE : notebookname}
                
    with open(fname,'w') as dfc_cfg_file :
        json.dump(initcfg,dfc_cfg_file)
        dfc_cfg_file.close()
                
    fname = notebookname + "_scriptlog.json"
    initslog = {NOTEBOOK_TITLE : notebookname}
                
    with open(fname,'w') as dfc_script_file :
        json.dump(initslog,dfc_script_file)
        dfc_script_file.close()
    
    

def check_notebook_dir_and_cfg_files(notebookname) :
    
    nbpath  =  get_notebook_path()
    
    if(not(nbpath == None)) :

        if(os.path.exists(nbpath + "/" + notebookname + "_files")) :
            if(os.path.isdir(nbpath + "/" + notebookname + "_files")) :
                
                # if no config file create one
                if(not(os.path.exists(nbpath + "/" + notebookname + "_files" + "/" + notebookname + "_config.json"))) : 
                    # create the initial config file 
                    fname = notebookname + "_config.json"
                    initcfg = {NOTEBOOK_TITLE : notebookname}
                    
                    with open(fname,'w') as dfc_cfg_file :
                        json.dump(initcfg,dfc_cfg_file)
                        dfc_cfg_file.close()
                
                # if no scriptlog file create one
                if(not(os.path.exists(nbpath + "/" + notebookname + "_files" + "/" + notebookname + "_scriptlog.json"))) : 
                    # create the initial config file 
                    fname = notebookname + "_scriptlog.json"
                    initslog = {NOTEBOOK_TITLE : notebookname}
                    
                    with open(fname,'w') as dfc_script_file :
                        json.dump(initslog,dfc_script_file)
                        dfc_script_file.close()
                
            else :
                # delete it if it is a file and not a dir
                try :
                    os.remove(nbpath + "/" + notebookname)
                    
                    import win32api
                    win32api.MessageBox(None,"remove cfg dir file","remove",1)

                    create_notebook_dir_and_cfg_files(notebookname,nbpath)
                except FileNotFoundError as e:
                    print("[create_notebook_dir_and_cfg_files : remove dir ] ",nbpath + "_files" + "\\" + notebookname,str(sys.exc_info()[0].__name__))
                except Exception as e:
                    print("[create_notebook_dir_and_cfg_files : remove dir ] ",nbpath + "_files" + "\\" + notebookname,str(sys.exc_info()[0].__name__))
                
                
        else :
            
            # notebook path and name not found so create them
            try :
                create_notebook_dir_and_cfg_files(notebookname,nbpath)
            except FileNotFoundError as e:
                print("[create_notebook_dir_and_cfg_files : remove dir ] ",nbpath + "_files" + "\\" + notebookname,str(sys.exc_info()[0].__name__))
            except Exception as e:
                print("[create_notebook_dir_and_cfg_files : remove dir ] ",nbpath + "_files" + "\\" + notebookname,str(sys.exc_info()[0].__name__))


    
    
    
    

    
