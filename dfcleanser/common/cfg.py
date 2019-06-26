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


def run_javascript(jscript, errmsg) :

    try :            
        from IPython.core.magics.display import Javascript
        display_javascript_HTML(Javascript(jscript))
    except :
        print(errmsg,jscript)
        
def does_dir_exist(path) :
    if(os.path.exists(path)) :
        if(os.path.isdir(path)) :   
            return(True)
        else :
            return(False)
    
def make_dir(path) :
    try :
        os.mkdir(path)
        return()
    
    except FileExistsError:
        return()

def does_file_exist(path) :
    if(os.path.exists(path)) :
        if(os.path.isfile(path)) :   
            return(True)
        else :
            return(False)
"""
#--------------------------------------------------------------------------
#   dfcleanser common notebook file and path functions
#--------------------------------------------------------------------------
"""
def get_notebook_name() :
    return(DataframeCleanserCfgData.get_notebookname())
       
def get_notebook_path() :
    return(DataframeCleanserCfgData.get_notebookpath())
    
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
#--------------------------------------------------------------------------
#   dfcleanser component Ids
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
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
#   dfcleanser Dataframe objects
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   dfcleanser Dataframe helper methods
#--------------------------------------------------------------------------
"""
def is_a_dfc_dataframe_loaded() :
    return(DCdf.is_current_dataframe_set()) 
def get_dfc_dataframe_titles_list() :
    return(DCdf.get_dataframe_titles())
   

"""
* --------------------------------------
* dfcleanser dataframe methods
* --------------------------------------
"""    
def add_dfc_dataframe(dfcdf) :
    """
    * ---------------------------------------------------------------------
    * function : add a dataframe cleanser dataframe object to available list
    * 
    * parms :
    *  dfcdf     - dfc_dataframe object
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------------------
    """
    DCdf.add_dataframe(dfcdf)
    dftitles    =   get_dfc_dataframes_titles_list()
    dftitles.sort()
    
    for i in range(len(dftitles)) :
        dftitles[0] =   dftitles[0].replace('"',"'")
    
    dftitlesDict    =   {}
    
    for i in range(len(dftitles)) :
        dftitlesDict.update({dftitles[i] : dftitles[i]})    
    
    dftitlesStr     =   json.dumps(dftitlesDict)
    dftitlesStr =   dftitlesStr.replace('"',"'")
    script      =   "change_dataframes_to_select(" + dftitlesStr + ",'temp');"
    run_javascript(script, "get df titles error") 
 
    
def get_dfc_dataframe_object(title=None) :
    return(DCdf.get_dfc_dataframe(title))
def get_dfc_dataframe(title=None) :
    return(DCdf.get_dataframe(title))
def get_dfc_dataframe_notes(title=None) :
    return(DCdf.get_dataframe_notes(title))
def set_dfc_dataframe_notes(notes,title=None) :
     DCdf.set_dataframe_notes(notes,title)
def rename_dfc_dataframe(oldname,newname) :
     DCdf.rename_dataframe(oldname,newname)
def update_dfc_dataframe(title,df) :
    DCdf.update_dataframe(title,df)
def drop_dfc_dataframe(title=None) :
    DCdf.drop_dataframe(title)

"""
* --------------------------------------
* current dfcleanser dataframe methods
* --------------------------------------
"""
def set_current_dfc_dataframe(df) :
    DCdf.update_current_dataframe(df)
def set_current_dfc_dataframe_title(title) :
    DCdf.set_current_dataframe(title)
def get_current_dfc_dataframe_title() :
    return(DCdf.get_current_dataframe())
    
def get_dfc_dataframes_select_list() :
    
    df_select           =   {}
    df_select_default   =   get_current_dfc_dataframe_title()
    df_select.update({"default": df_select_default})
    df_select_titles    =   get_dfc_dataframe_titles_list()
            
    df_select.update({"list":df_select_titles})
    
    return(df_select)

def get_dfc_dataframes_titles_list() :
    return(DCdf.get_dataframe_titles())
    
def get_dfc_df(title) :
    return(DCdf.get_dfc_dataframe(title))    
    
"""
#--------------------------------------------------------------------------
#  dfcleanser Dataframe object
#--------------------------------------------------------------------------
"""
class dfc_dataframe :
    """
    * ---------------------------------------------------------
    * class : dataframe cleanser dataframe object
    * 
    * attributes :
    *  title     - datframe title : get_title()
    *  df        - pandas dataframe object : get_df()
    *  notes     - dataframe descriptive notes : get_notes()
    *
    * returns : 
    *  dataframe cleanser dataframe object 
    * --------------------------------------------------------
    """
    
    dfc_df    =   []
    
    def __init__(self,titleparm,dfparm,notesparm=""):
        self.dfc_df     =   [titleparm,dfparm,notesparm]
        
    def get_title(self)     : return(self.dfc_df[0])       
    def get_df(self)        : return(self.dfc_df[1])       
    def get_notes(self)     : return(self.dfc_df[2])       

    def set_title(self,title)   : self.dfc_df[0] = title       
    def set_df(self,df)         : self.dfc_df[1] = df     
    def set_notes(self,notes)   : self.dfc_df[2] = notes  
    
    

"""
#--------------------------------------------------------------------------
#   dfcleanser Dataframe factory
#--------------------------------------------------------------------------
"""
class DCDataframes :
    
    dcdataframes    =   []
    current_df      =   None

    def __init__(self):
        self.dcdataframes   =   []
        self.current_df     =   None
    
    """
    * --------------------------------------
    * current dfcleanser dataframes methods
    * --------------------------------------
    """
    def set_current_dataframe(self,title) :
        self.current_df     =  title 
    def get_current_dataframe(self) :
        return(self.current_df)
    def update_current_dataframe(self,df) :
        dfindex     =   self.get_df_index(self.current_df)
        if(dfindex > -1) :
            self.dcdataframes[dfindex].set_df(df)    
    def update_current_dataframe_notes(self,notes) :
        dfindex     =   self.get_df_index(self.current_df)
        if(dfindex > -1) :
            self.dcdataframes[dfindex].set_notes(notes)    
    def is_current_dataframe_set(self) :
        if(self.current_df == None) :
            return(False)
        else :
            dfindex     =   self.get_df_index(self.current_df)
            if(dfindex > -1) :
                return(True)
            else :
                self.current_df = None
                return(False)
    
    """
    * ------------------------------------
    * add or drop dfcleanser dataframes 
    * ------------------------------------
    """        
    def add_dataframe(self,dfcdf) :
        for i in range(len(self.dcdataframes)) :
            if(self.dcdataframes[i].get_title() == dfcdf.get_title()) :
                self.drop_dataframe(dfcdf.get_title())    
        
        self.dcdataframes.append(dfcdf)
        
    def drop_dataframe(self,title=None) :
        if(title == None) :
            if(self.current_df == None) :
                return()
            else :
                dfindex     =   self.get_df_index(self.current_df)
                if(dfindex > -1) :
                    del self.dcdataframes[dfindex]
                    self.current_df == None
        else :
            dfindex     =   self.get_df_index(title)
            if(dfindex > -1) :
                del self.dcdataframes[dfindex]
                if(self.current_df == title) :
                    self.current_df == None    

    """
    * ------------------------------------
    * get dfcleanser dataframe components
    * ------------------------------------
    """        
    def get_dataframe(self,title=None) :
        if(title == None) :
            dfindex     =   self.get_df_index(self.current_df)
        else :
            dfindex     =   self.get_df_index(title)
            
        if(dfindex > -1) :            
            return(self.dcdataframes[dfindex].get_df())
        else :
            return(None)
    
    def update_dataframe(self,title,df) :
        if(title == None) :
            dfindex     =   self.get_df_index(self.current_df)
        else :
            dfindex     =   self.get_df_index(title)
            
        if(dfindex > -1) :            
            return(self.dcdataframes[dfindex].set_df(df))
        else :
            print("no dataframe found for " + title)
                
    def get_dfc_dataframe(self,title) : 
        return(self.dcdataframes[self.get_df_index(title)])
    
    def get_dataframe_notes(self,title=None) :
        if(title == None) :
            dfindex     =   self.get_df_index(self.current_df)
            if(dfindex > -1) :            
                return(self.dcdataframes[dfindex].get_notes())
            else :
                return(None)
        else :
            dfindex     =   self.get_df_index(title)
            if(dfindex > -1) :            
                return(self.dcdataframes[dfindex].get_notes())
            else :
                return(None)
    
    def set_dataframe_notes(self,notes,title=None) :
        if(title == None) :
            dfindex     =   self.get_df_index(self.current_df)
            if(dfindex > -1) :            
                self.dcdataframes[dfindex].set_notes(notes)
        else :
            dfindex     =   self.get_df_index(title)
            if(dfindex > -1) :            
                self.dcdataframes[dfindex].set_notes(notes)

    def rename_dataframe(self,oldName,newName) :
        dfindex     =   self.get_df_index(oldName)
        if(dfindex > -1) :            
            self.dcdataframes[dfindex].set_title(newName)
            
            if(oldName == self.current_df) :
                self.current_df     =   newName
                
    def get_dataframe_titles(self) :
        
        if(len(self.dcdataframes) > 0) :
            titles  =   []
            for i in range(len(self.dcdataframes)) :
                titles.append(self.dcdataframes[i].get_title())
                
            return(titles)
        else :
            return(None)
            
    def get_df_index(self,title) :
        
        for i in range(len(self.dcdataframes)) :
            if(self.dcdataframes[i].get_title() == title) :
                return(i)
                
        return(-1)
        
        
"""
#--------------------------------------------------------------------------
#   global DC Dataframe factory object
#--------------------------------------------------------------------------
"""
DCdf = DCDataframes()

"""
#--------------------------------------------------------------------------
#   global DC Dataframe Chapters Current Dataframe
#--------------------------------------------------------------------------
"""
CURRENT_INSPECTION_DF                   =   "currentinspectiondf"
CURRENT_CLEANSE_DF                      =   "currentcleansedf"
CURRENT_TRANSFORM_DF                    =   "currenttransformdf"
CURRENT_EXPORT_DF                       =   "currentexportdf"

def get_current_chapter_df(chapterdfId) :

    if(is_a_dfc_dataframe_loaded()) : 
        
        saved_df    =   get_config_value(chapterdfId)
        
        if(saved_df is None) :
            drop_config_value(saved_df)
            return(get_dfc_dataframe())
        else :
            df  =   get_dfc_dataframe(saved_df)
            if(df is None) :
                drop_config_value(saved_df)
                return(get_dfc_dataframe())
            else :
                return(df)
    
    else :
        return(None)




"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser config objects
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_cfg_parm_from_input_list(formid,label,labellist) :
    """
    * ---------------------------------------------------------
    * function : get a parm from cfg parms list
    * 
    * parms :
    *  formid     - form id
    *  label      - label of parm to get
    *  labellist  - input form label list
    *
    * returns : 
    *  geocoder engine 
    * --------------------------------------------------------
    """

    parmslist   =   get_config_value(formid+"Parms")
    
    if(not (parmslist == None)) :
        
        for i in range(len(labellist)) :
            if(label == labellist[i]) :
                return(parmslist[i])
                
    return(None)




GLOBAL      =   False
LOCAL       =   True

        
"""
#--------------------------------------------------------------------------
#   Generic System config value keys
#--------------------------------------------------------------------------
"""
NOTEBOOK_TITLE          =   "NoteBookName"
NOTEBOOK_PATH           =   "NoteBookPath"
DFC_CELLS_LOADED        =   "dfCcellsLoaded"
DFC_CELLS_CBS           =   "dfCcellcbs"


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

CLEANSING_COL_KEY                       =   "datacleansingcolumn"
CLEANSING_ROW_KEY                       =   "datacleansingrow"

GRAPHS_FLAG_KEY                         =   "graphcolumn"

"""
#--------------------------------------------------------------------------
#   Export config value keys
#--------------------------------------------------------------------------
"""
CURRENT_EXPORTED_FILE_NAME_KEY          =   "currentExportedFileName"

"""
#--------------------------------------------------------------------------
#   Import config value keys
#--------------------------------------------------------------------------
"""
CURRENT_IMPORTED_DATA_SOURCE_KEY        =   "currentImportedDataSource"
CURRENT_SQL_IMPORT_ID_KEY               =   "currentSQLImportID"
CURRENT_IMPORT_START_TIME               =   "importStartTime"

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
CURRENT_GENERIC_FUNCTION                =   "currentGenFunction"
CURRENT_SUBSET_FILTERS                  =   "currentSubsetFilters"
CURRENT_SUBSET_FILTER                   =   "currentSubsetFilter"

"""
#--------------------------------------------------------------------------
#   System config value keys
#--------------------------------------------------------------------------
"""
UTILITIES_CBS_KEY                       =   "dfc_utilities_cbs"
EULA_FLAG_KEY                           =   "EULARead"
SAVED_FILE_NAME_KEY                     =   "DCS_savedfilenname"
DFC_CURRENTLY_LOADED_KEY                =   "dfcleanserCurrentlyLoaded"
DFC_CHAPTERS_LOADED_KEY                 =   "dfcCurrentlyLoadedChapters"
CURRENT_DF_DISPLAYED_KEY                =   "dfcCurrentSelecteddf"

"""
#--------------------------------------------------------------------------
#   working column name
#--------------------------------------------------------------------------
"""
CURRENT_COL_NAME    =   "currentColumnName"

def get_current_col_name() :
    return(get_config_value(CURRENT_COL_NAME))


GlobalKeys     =   [EULA_FLAG_KEY,"geocoder","GoogleV3_querykwargs",
                    "arcgisgeocoderParms","binggeocoderParms","mapquestgeocoderParms",
                    "nomingeocoderParms","googlegeocoderParms","baidu_geocoderParms",
                    "googlebulkgeocoderParms","arcgisbatchgeocoderParms",
                    "bingbulkgeocoderParms","baidubulkgeocoderParms",
                    "PostgresqldbconnectorParms","MySQLdbconnectorParms","SQLitedbconnectorParms",
                    "OracledbconnectorParms","MSSQLServerdbconnectorParms","customdbconnectorParms"]

def is_global_parm(key) :
    if(key in GlobalKeys) :
        return(True)
    else :
        return(False)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Dataframe Cleanser config data helper functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

#--------------------------------------------------------------------------
#   dfcleanser generic cfg values methods
#--------------------------------------------------------------------------
def get_config_value(key) :
    return(DataframeCleanserCfgData.get_config_value(key))
def set_config_value(key, value) :
    DataframeCleanserCfgData.set_config_value(key,value)
def drop_config_value(key) :
    DataframeCleanserCfgData.drop_config_value(key)

#--------------------------------------------------------------------------
#   dfcleanser generic cfg values methods for notebook copy 
#--------------------------------------------------------------------------
def get_config_data() :
    return(DataframeCleanserCfgData.get_config_data())
def get_dfc_config_data() :
    return(DataframeCleanserCfgData.get_dfc_config_data())
def get_current_notebook_name() :
    return(DataframeCleanserCfgData.get_notebookname())
def reset_cfg_data() :
    print("reset_cfg_data")
    DataframeCleanserCfgData.load_cfg_file()    

#--------------------------------------------------------------------------
#   dfcleanser sync jupyter with js 
#--------------------------------------------------------------------------
def sync_with_js(parms) :
    DataframeCleanserCfgData.sync_js(parms)    

def get_notebookname() :
    try :
        run_javascript("window.getNotebookName();","Unable to get notebook name")
    except :
        print("get_get_notebookname error")
        
def get_notebookpath() :
    try :
        run_javascript("window.getNotebookPath();","Unable to get notebook path")
    except :
        print("get_notebook_path error")

"""
#--------------------------------------------------------------------------
#   Dataframe Cleanser config class
#--------------------------------------------------------------------------
"""

class DataframeCleansercfg :
    
    # instance variables
    
    # notebook specific cfg file data
    cfg_data                =   {}
    # global dfcleanser cfg file data
    dfc_cfg_data            =   {}
    
    # default starting cfg data
    default_dfc_cfg_data    =   {"EULARead":"False"}
    
    notebookName            =   ""
    notebookPath            =   ""
    
    # notebook specific cfg file name
    cfgfilename             =   ""
    # global dfcleanser cfg file name
    dfccfgfilename          =   ""
    
    # Jupyter synced flag
    cfg_file_loaded         =   False
    
    
    # full constructor
    def __init__(self) :
 
        
        #print("fuck you")
        self.cfg_data               =   {"EULARead":"true"}
        self.dfc_cfg_data           =   {}
        self.default_dfc_cfg_data   =   {"EULARead":"False"}

        self.notebookName           =   ""
        self.notebookPath           =   ""
        self.cfgfilename            =   ""
        self.dfccfgfilename         =   ""
        self.cfg_file_loaded        =   False
    
    def init_cfg_file(self) :
        
        if( (self.notebookName == "") or (self.notebookPath == "") ) :
            self.cfgfilename = ""
            return()
        
        if(self.cfgfilename == "")  :
            # check if notebook specific dir exists
            cfgdir = os.path.join(self.notebookPath,self.notebookName+"_files")
            if(not (does_dir_exist(cfgdir))) :
                make_dir(cfgdir)
                
            self.cfgfilename = os.path.join(cfgdir,self.notebookName+"_config.json")
            if(not (does_file_exist(self.cfgfilename))) :

                with open(self.cfgfilename, 'w') as cfg_file :
                    json.dump(self.cfg_data,cfg_file)
                    cfg_file.close()
        else :
            return()
            
        
    def get_cfg_file_name(self) :
        
        if(self.cfgfilename == "") :
            self.init_cfg_file()
            return(self.cfgfilename)
        else :
            return(self.cfgfilename)    
            
    def load_cfg_file(self) :
        
        cfg_fname   =   self.get_cfg_file_name()
        
        if(cfg_fname == "") :
            return()
        
        try :
            if(len(self.cfgfilename) > 0) :
                with open(cfg_fname, 'r') as cfg_file :
                    self.cfg_data = json.load(cfg_file)
                    cfg_file.close()
                    
            self.cfg_file_loaded    =   True
                    
        except json.JSONDecodeError :
            
            from dfcleanser.common.common_utils import confirm_user,CORRUPTED_CFG_FILE_ID 
            confirm_user("Config File Corrupted : Use blank default file",CORRUPTED_CFG_FILE_ID)

            self.cfg_data   =   {}
            os.rename(self.cfgfilename,self.cfgfilename+"_corrupted")
                        
        except :
            if(len(self.get_notebookname()) > 0) :
                
                from dfcleanser.common.common_utils import confirm_user,NO_CFG_FILE_ID 
                confirm_user("Config File Not Found : Use blank default file",NO_CFG_FILE_ID)

                print("[load_config_file Error] " + "[" + cfg_fname + "] " + str(sys.exc_info()[0].__name__))
                
            else :
                from dfcleanser.common.common_utils import confirm_user,NO_CFG_FILE_ID
                confirm_user("Config File Not Found : Use blank default file",NO_CFG_FILE_ID)
        
    
    def save_cfg_file(self) :
        
        if(not(self.cfg_file_loaded)) :
            self.load_cfg_file()
    
        try :
            if(len(self.cfgfilename) > 0) :
                with open(self.get_cfg_file_name(), 'w') as cfg_file :
                    json.dump(self.cfg_data,cfg_file)
                    cfg_file.close()
        except :
            if(len(self.get_notebookname()) > 0) :
                print("[save_config_file Error] " + "[" + self.get_cfg_file_name() + "] " + str(sys.exc_info()[0].__name__))
            
    def get_config_data(self) :
        return(self.cfg_data)            
    
    def get_config_value(self,key) :
        
        if(not(is_global_parm(key))) :
            if(self.cfg_data.get(key) == None) :
                self.load_cfg_file()
                return(self.cfg_data.get(key))
            else :
                return(self.cfg_data.get(key))
        else :
            return(self.get_dfc_config_value(key))

    def set_config_value(self, key, value) :
        
        if(not(is_global_parm(key))) :
            try :
                self.cfg_data.update({key: value})
            except :
                print("[error set cfg value] ",key,self.cfg_data,str(sys.exc_info()[0].__name__))
                self.load_cfg_file()
        
            self.save_cfg_file()
            
        else :
            self.set_dfc_config_value(key, value)    
            
    def drop_config_value(self, key) :

        if(not(is_global_parm(key))) :
            try :
                self.cfg_data.pop(key,None)
            except :
                print("[error drop cfg value] ",key,self.cfg_data,str(sys.exc_info()[0].__name__))
                self.load_cfg_file()
        
            self.save_cfg_file() 
        else :
            self.drop_dfc_config_value(key)

    #---------------------------------------------------
    #   dfcleanser common values
    #---------------------------------------------------    
    def set_notebookname(self,nbname) :
        self.notebookName = nbname

    def set_notebookpath(self,nbpath) :
        self.notebookPath = nbpath
        self.init_cfg_file()
        self.init_dfc_cfg_file()
        
        if( (len(self.get_cfg_file_name()) > 0) and 
            (len(self.get_dfc_cfg_file_name()) > 0) and 
            (len(self.get_notebookname()) > 0) ) :
            log_text =  "log_jupyter_msg('dfcleanser synced : successfully');"
        else :
            log_text =  "log_jupyter_msg('dfcleanser not synced : successfully');"
            
        run_javascript(log_text,"errmsg")
        
        
    def get_notebookname(self) :
        return(self.notebookName) 
    def get_notebookpath(self) :
        return(self.notebookPath) 

        
    #---------------------------------------------------
    #   dfcleanser global cfg values 
    #---------------------------------------------------   
    def init_dfc_cfg_file(self) :
        if(self.dfccfgfilename == "")  :
            self.dfccfgfilename = get_common_files_path() + "dfcleanserCommon" + "_config.json"
            if(not (does_file_exist(self.dfccfgfilename))) :
                with open(self.cfgfilename, 'w') as cfg_file :
                    json.dump(self.default_dfc_cfg_data,cfg_file)
                    cfg_file.close()
            else :
                return()
        
    def get_dfc_cfg_file_name(self) :
        if(self.dfccfgfilename == "") :
            self.init_dfc_cfg_file()
            return(self.dfccfgfilename)
        else :
            return(self.dfccfgfilename)    
    
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
        else :
            return(self.dfc_cfg_data.get(key))
        
    def set_dfc_config_value(self, key, value) :
        try :
            self.dfc_cfg_data.update({key: value})
        except :
            print("[error set cfg value] ",key,self.cfg_data,str(sys.exc_info()[0].__name__))
            self.load_dfc_cfg_file()
        
        self.save_dfc_cfg_file()
    
    def drop_dfc_config_value(self, key) :
        try :
            self.dfc_cfg_data.pop(key,None)
        except :
            self.load_dfc_cfg_file()
        
        self.save_dfc_cfg_file()
        
    def sync_js(self,parms) :

        nbname  =   parms[0]
        self.set_notebookname(nbname)
        get_notebookpath()
        
"""
* ----------------------------------------------------
# static instantiation of the config data object
* ----------------------------------------------------
"""    
DataframeCleanserCfgData    =   DataframeCleansercfg()


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser cells functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def get_chapters_loaded_cbs() :
    
    cellsList   =   get_config_value(DFC_CHAPTERS_LOADED_KEY)

    utilcbs     =   [0,0,0,0]

    if(not (cellsList == None)) :
        
        if(cellsList[19])    :   utilcbs[0] = 1
        if(cellsList[20])    :   utilcbs[1] = 1
        if(cellsList[21])    :   utilcbs[2] = 1
        if(cellsList[22])    :   utilcbs[3] = 1

    return([utilcbs])
    

def set_chapters_loaded(cellsList) :
    
    set_config_value(DFC_CHAPTERS_LOADED_KEY, cellsList)
    
    cblist  =   get_chapters_loaded_cbs()
    
    set_config_value(UTILITIES_CBS_KEY,cblist[0])
    set_config_value(DFC_CURRENTLY_LOADED_KEY,"True")

def get_loaded_cells() :

    run_javascript("window.getdfcChaptersLoaded();",
                   "Unable to get cells loaded")

def check_if_dc_init() :
    
    if( not(DataframeCleanserCfgData.get_notebookname() == None) ) :
        if( not(DataframeCleanserCfgData.get_notebookpath() == None) ) :  
            return(True)
    else :
        return(False)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser common notebook and path functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
    
"""
#--------------------------------------------------------------------------
#   dfcleanser python config helper methods
#--------------------------------------------------------------------------
"""
def set_notebookName(nbname) :
    DataframeCleanserCfgData.set_notebookname(nbname)
def get_notebookName() :
    return(DataframeCleanserCfgData.get_notebookname())
    
def set_notebookPath(nbpath) :
    DataframeCleanserCfgData.set_notebookpath(nbpath)
def get_notebookPath() :
    return(DataframeCleanserCfgData.get_notebookpath())  

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
                except FileNotFoundError :
                    print("[create_notebook_dir_and_cfg_files : remove dir ] ",nbpath + "_files" + "\\" + notebookname,str(sys.exc_info()[0].__name__))
                except Exception :
                    print("[create_notebook_dir_and_cfg_files : remove dir ] ",nbpath + "_files" + "\\" + notebookname,str(sys.exc_info()[0].__name__))
                
                
        else :
            
            # notebook path and name not found so create them
            try :
                create_notebook_dir_and_cfg_files(notebookname,nbpath)
            except FileNotFoundError :
                print("[create_notebook_dir_and_cfg_files : remove dir ] ",nbpath + "_files" + "\\" + notebookname,str(sys.exc_info()[0].__name__))
            except Exception :
                print("[create_notebook_dir_and_cfg_files : remove dir ] ",nbpath + "_files" + "\\" + notebookname,str(sys.exc_info()[0].__name__))


"""
* ----------------------------------------------------
# dfcleanser mode - inline or popup
* ----------------------------------------------------
""" 

INLINE_MODE     =   0
POP_UP_MODE     =   1
     
def set_dfc_mode(mode) :
    dfcMode.set_mode(mode)

def get_dfc_mode() :   
    return(dfcMode.get_mode())

class dfc_mode :
    
    # instance variables
    mode                    =   INLINE_MODE
    
    # full constructor
    def __init__(self) :
        self.mode               =   INLINE_MODE
        
    def set_mode(self,inmode) :
        self.mode  =   inmode
        run_javascript("set_dfcmode(" + str(inmode) + ");","Unable to set mode")

    def get_mode(self) :
        return(self.mode)
   

dfcMode     =   dfc_mode()    
