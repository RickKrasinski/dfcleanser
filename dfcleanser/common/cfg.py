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
#   dfcleanser sync jupyter with js 
#--------------------------------------------------------------------------
"""
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
#--------------------------------------------------------------------------
#   dfcleanser chapter onjects
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""


"""
#--------------------------------------------------------------------------
#   dfcleanser chapter ids
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
SWCensusUtility_ID      =   "SWCensusUtility"
System_ID               =   "System"


DBUtils_ID              =   "DBUtils"
DumpUtils_ID            =   "DumpUtils"
Help_ID                 =   "Help"
GenFunction_ID          =   "GenFunction"
SWDFCensusUtility_ID    =   "SWDFCensusUtility"


"""
#--------------------------------------------------------------------------
#    chapter current dataframe objects   
#--------------------------------------------------------------------------
"""
chapter_select_df_input_title             =   "Dataframe To Inspect"
chapter_select_df_input_id                =   "datainspectdf"
chapter_select_df_input_idList            =   ["didfdataframe"]

chapter_select_df_input_labelList         =   ["dataframe_to_inspect"]

chapter_select_df_input_typeList          =   ["select"]

chapter_select_df_input_placeholderList   =   ["dataframe to inspect"]

chapter_select_df_input_jsList            =   [None]

chapter_select_df_input_reqList           =   [0]

chapter_select_df_input_form              =   [chapter_select_df_input_id,
                                               chapter_select_df_input_idList,
                                               chapter_select_df_input_labelList,
                                               chapter_select_df_input_typeList,
                                               chapter_select_df_input_placeholderList,
                                               chapter_select_df_input_jsList,
                                               chapter_select_df_input_reqList]  



data_cleansing_df_input_id                =   "datacleansedf"
data_transform_df_input_id                =   "datatransformdf"
data_export_df_input_id                   =   "dataexportdf"
data_subset_df_input_id                   =   "datasubsetdf"



def update_chapter_df_select(chapterform) :
    """
    * ---------------------------------------------------------
    * function : change the df list in select forms
    * 
    * Parms :
    *  chapterform - chapter fomr to update
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------
    """
    
    df_forms    =   ["dfmgrform","datainspectdf","datacleansedf","datatransformdf","dataexportdf","datasubsetdf"]
    df_selects  =   ["dftitle","didfdataframe","dcdfdataframe","dtdfdataframe","dedfdataframe","dsdfdataframe"]
    
    
    for j in range(len(df_forms)) :
        if(chapterform == df_forms[j]) :
            df_index    =   j
        
    from dfcleanser.common.html_widgets import get_Input
    select_df_form      =   get_Input(df_forms[df_index])
        
    select_dicts        =   select_df_form[6]
    select_dfs_dict     =   select_dicts.get(df_selects[df_index])
    selected_df         =   select_dfs_dict.get("default")
        
    # get list to update chapter selects
    dftitles    =   get_dfc_dataframes_titles_list()
    dftitles.sort()
        
    if(selected_df == "") :
        selected_df = dftitles[0]

    new_df_dict         =   {"default":selected_df,"list":dftitles}
    select_dicts.update({df_selects[df_index]:new_df_dict})
    select_df_form[6]   =   select_dicts
        
    from dfcleanser.common.html_widgets import InputForm
    temp_form  =   InputForm(df_forms[df_index],
                             select_df_form[0],
                             select_df_form[1],
                             select_df_form[2],
                             select_df_form[3],
                             select_df_form[4],
                             select_df_form[5])
        
    temp_form.set_form_select_dict(select_dicts)
    
    from dfcleanser.common.common_utils import patch_html, run_jscript
        
    new_df_html         =   temp_form.get_select_html(df_selects[df_index],selected_df)
    new_df_html         =   patch_html(new_df_html)

    change_select_js = "$("
    change_select_js = change_select_js + "'#" + df_selects[df_index] + "').html('"
    change_select_js = change_select_js + new_df_html + "');"
    
    run_jscript(change_select_js,"fail update select : ")


def get_select_df_form(chapterid) :
    """
    * -------------------------------------------------------------------------- 
    * function : get select dataframe form
    * 
    * parms :
    *  chapterid    -   chapter id
    *
    * returns : form
    * --------------------------------------------------------
    """
    
    if(chapterid == DataCleansing_ID) :
        idlist      =   ["dcdfdataframe"]
        labellist   =   ["dataframe_to_cleanse"]
        formid      =   "datacleansedf"

    elif(chapterid == DataTransform_ID) :
        idlist      =   ["dtdfdataframe"]
        labellist   =   ["dataframe_to_transform"]
        formid      =   "datatransformdf"

    elif(chapterid == DataExport_ID) :
        idlist      =   ["dedfdataframe"]
        labellist   =   ["dataframe_to_export"]
        formid      =   "dataexportdf"
    
    elif(chapterid == SWDFSubsetUtility_ID) :
        idlist      =   ["dsdfdataframe"]
        labellist   =   ["dataframe_to_subset"]
        formid      =   "datasubsetdf"

    else :
        idlist      =   chapter_select_df_input_idList
        labellist   =   chapter_select_df_input_labelList
        formid      =   chapter_select_df_input_id
    
    from dfcleanser.common.html_widgets import InputForm
    select_df_form  =   InputForm(formid,
                                  idlist,
                                  labellist,
                                  chapter_select_df_input_typeList,
                                  chapter_select_df_input_placeholderList,
                                  chapter_select_df_input_jsList,
                                  chapter_select_df_input_reqList)
    
    df_list     =   get_dfc_dataframes_select_list(chapterid)

    if(not (df_list is None)) :
        dataframes      =   df_list
    else :
        dataframes      =   {'default': "", 'list': [""]}

    selectDicts     =   []
    selectDicts.append(dataframes)

    from dfcleanser.common.common_utils import get_select_defaults
    get_select_defaults(select_df_form,
                        formid,
                        idlist,
                        chapter_select_df_input_typeList,
                        selectDicts)
    
    select_df_form.set_shortForm(True)
    
    if(get_dfc_mode() == INLINE_MODE) :
        select_df_form.set_gridwidth(780)
    else :
        select_df_form.set_gridwidth(480)
    
    return(select_df_form)


def display_data_select_df(chapterid) :
    """
    * -------------------------------------------------------------------------- 
    * function : display select dataframe form
    * 
    * parms :
    *  chapterid    -   chapter id
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    select_df_form              =   get_select_df_form(chapterid)
    
    gridclasses     =   ["dfc-footer"]
    gridhtmls       =   [select_df_form.get_html()]
    
    from dfcleanser.common.common_utils import display_generic_grid   
    if(get_dfc_mode() == INLINE_MODE) :
        display_generic_grid("df-select-df-wrapper",gridclasses,gridhtmls)
    else :
        display_generic_grid("df-select-df-pop-up-wrapper",gridclasses,gridhtmls)


def display_no_dfs(chapterid) :
    """
    * -------------------------------------------------------------------------- 
    * function : display status fro no dfs
    * 
    * parms :
    *  chapterid    -   chapter id
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    if(chapterid == DataCleansing_ID) :         msg    =   "No dataframe imported to select for data cleansing"
    elif(chapterid == DataInspection_ID) :      msg    =   "No dataframe imported to select for data inspection"
    elif(chapterid == DataExport_ID) :          msg    =   "No dataframe imported to select for data export"
    elif(chapterid == DataTransform_ID) :       msg    =   "No dataframe imported to select for data transform"
    elif(chapterid == SWDFSubsetUtility_ID) :   msg    =   "No dataframe imported to select for subsets"
    
    from dfcleanser.common.common_utils import display_grid_status
    display_grid_status(msg)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#  dfc dataframe objects and methods
#
#   a dfc dataframe is an object that contains a descriptive, 
#   a pandas dataframe and descriptive notes
#
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   dfcleanser Dataframe helper methods
#--------------------------------------------------------------------------
"""

def is_a_dfc_dataframe_loaded() :
    """
    * ---------------------------------------------------------------------
    * function : chek if a dfc dataframe is loaed in memory for usage
    *
    * returns : 
    *  True if a dfc dataframe loaded else False
    * --------------------------------------------------------------------
    """
    return(dfc_dfs.is_a_dfc_dataframe_loaded()) 

"""
#--------------------------------------------------------------------------
#   dfcleanser dataframe attributes
#--------------------------------------------------------------------------
"""   
def get_dfc_dataframe(title) :
    """
    * ---------------------------------------------------------------------
    * function : get a dfc datframe object
    *
    * Parms : 
    *  title    :   dfc dataframe title
    * --------------------------------------------------------------------
    """
    return(dfc_dfs.get_dfc_dataframe(title))
    
def get_dfc_dataframe_df(title) :
    """
    * ---------------------------------------------------------------------
    * function : get a dfc datframe object dataframe attribute
    *
    * Parms : 
    *  title    :   dfc dataframe title
    * --------------------------------------------------------------------
    """
    return(dfc_dfs.get_dfc_dataframe(title).get_df())
    
def set_dfc_dataframe_df(title,df) :
    """
    * ---------------------------------------------------------------------
    * function : set a dfc datframe pandas dataframe attribute
    *
    * Parms : 
    *  title    :   dfc dataframe title
    * --------------------------------------------------------------------
    """
    dfc_dfs.get_dfc_dataframe(title).set_df(df) 

def get_dfc_dataframe_notes(title) :
    """
    * ---------------------------------------------------------------------
    * function : get a dfc datframe note attribute
    *
    * Parms : 
    *  title    :   dfc dataframe title
    * --------------------------------------------------------------------
    """
    return(dfc_dfs.get_dataframe_notes(title))
    
def set_dfc_dataframe_notes(title,notes) :
    """
    * ---------------------------------------------------------------------
    * function : set a dfc datframe note attribute
    *
    * Parms : 
    *  title    :   dfc dataframe title
    * --------------------------------------------------------------------
    """
    dfc_dfs.set_dataframe_notes(title,notes)

def append_dfc_dataframe_notes(title,notes) :
    """
    * ---------------------------------------------------------------------
    * function : append a note to the dfc dataframe notes
    *
    * Parms : 
    *  title    :   dfc dataframe title
    * --------------------------------------------------------------------
    """
    dfc_notes   =   get_dfc_dataframe_notes(title)
    dfc_notes   =   dfc_notes + "\n--------\n" + notes
    dfc_dfs.set_dataframe_notes(title,notes)


"""
* --------------------------------------
* dfcleanser dataframe object methods
* --------------------------------------
"""    
     
def rename_dfc_dataframe(oldtitle,newtitle) :
    """
    * ---------------------------------------------------------------------
    * function : rename a dfc datframe title attribute
    *
    * Parms : 
    *  title    :   dfc dataframe title
    * --------------------------------------------------------------------
    """
    dfc_dfs.rename_dataframe(oldtitle,newtitle)
     
def drop_dfc_dataframe(title) :
    """
    * ---------------------------------------------------------------------
    * function : drop a dfc datframe 
    *
    * Parms : 
    *  title    :   dfc dataframe title
    * --------------------------------------------------------------------
    """
    dfc_dfs.drop_dataframe(title)

def add_dfc_dataframe(dfcdf,update=True) :
    """
    * ---------------------------------------------------------------------
    * function : add a dfc dataframe object to available list
    * 
    * parms :
    *  dfcdf     - dfc_dataframe object
    *
    * returns : 
    *  N/A 
    * --------------------------------------------------------------------
    """
    
    # add the dataframe to dfc 
    dfc_dfs.add_dataframe(dfcdf)
    
    if(update) :
        change_select_js = "change_dataframes_to_select();"
    
        from dfcleanser.common.common_utils import run_jscript
        run_jscript(change_select_js,"fail update select : ")


def get_dfc_dataframes_titles_list() :
    """
    * ---------------------------------------------------------
    * class : get a python list of dfc dataframes titles 
    * 
    * returns : 
    *  list of dfc dataframe titles 
    * --------------------------------------------------------
    """
    return(dfc_dfs.get_dataframe_titles())


def get_dfc_dataframes_select_list(chapterid) :
    """
    * ---------------------------------------------------------
    * class : get the list of dfc dataframes for a select 
    * 
    * returns : 
    *  select list of dfc dataframe objects 
    * --------------------------------------------------------
    """
    
    df_select           =   {}
    df_select_titles    =   get_dfc_dataframes_titles_list()
    

    if(chapterid == DataInspection_ID)      :   default_df  =   get_config_value(CURRENT_INSPECTION_DF)
    elif(chapterid == DataCleansing_ID)     :   default_df  =   get_config_value(CURRENT_CLEANSE_DF)
    elif(chapterid == DataTransform_ID)     :   default_df  =   get_config_value(CURRENT_TRANSFORM_DF)
    elif(chapterid == DataExport_ID)        :   default_df  =   get_config_value(CURRENT_EXPORT_DF)
    elif(chapterid == SWDFSubsetUtility_ID) :   default_df  =   get_config_value(CURRENT_SUBSET_DF)
    else                                    :   default_df  =   None
   
    if(not (df_select_titles is None) ) :
        if(default_df is None) :
            df_select.update({"default": df_select_titles[0]})
        else :
            df_select.update({"default": default_df})
            
        df_select.update({"list":df_select_titles})
        return(df_select)
    else :
        return(None)



"""
#--------------------------------------------------------------------------
#   individual dfc dataframe object
#--------------------------------------------------------------------------
"""
class dfc_dataframe :
    """
    * ---------------------------------------------------------
    * class : dfc dataframe object
    * 
    * attributes :
    *  title     - dataframe title 
    *  df        - pandas dataframe object 
    *  notes     - dataframe descriptive notes 
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
#   dfc dataframes store
#--------------------------------------------------------------------------
"""
class dfc_dataframes :
    
    dcdataframes    =   []

    def __init__(self):
        self.dcdataframes   =   []
    

    def is_a_dfc_dataframe_loaded(self) :
        if(len(self.dcdataframes) > 0) :
            return(True)
        else :
            return(False)
        
    """
    * ------------------------------------
    * add or drop dfc dataframes 
    * ------------------------------------
    """        
    def add_dataframe(self,dfcdf) :
        for i in range(len(self.dcdataframes)) :
            if(self.dcdataframes[i].get_title() == dfcdf.get_title()) :
                self.drop_dataframe(dfcdf.get_title())    
        
        self.dcdataframes.append(dfcdf)
        
    def drop_dataframe(self,title) :
            
        dfindex     =   self.get_df_index(title)
        if(dfindex > -1) :
            del self.dcdataframes[dfindex]

    """
    * ------------------------------------
    * get dfc dataframe components
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
        dfc_index   =  self.get_df_index(title)
        if(dfc_index == -1) :
            return(None)
        else :
            return(self.dcdataframes[dfc_index])
    
    def get_dataframe_notes(self,title) :
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
    
    def set_dataframe_notes(self,title,notes) :
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
#   dfc dataframe factory object
#--------------------------------------------------------------------------
"""
dfc_dfs     =   dfc_dataframes()



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   dfcleanser config objects
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   dfc dataframe Chapters current dataframe config value
#--------------------------------------------------------------------------
"""
CURRENT_INSPECTION_DF                   =   "currentinspectiondf"
CURRENT_CLEANSE_DF                      =   "currentcleansedf"
CURRENT_TRANSFORM_DF                    =   "currenttransformdf"
CURRENT_EXPORT_DF                       =   "currentexportdf"
CURRENT_IMPORT_DF                       =   "currentimportdf"
CURRENT_GEOCODE_DF                      =   "currentgeocodedf"
CURRENT_SUBSET_DF                       =   "currentsubsetdf"


def get_current_chapter_df(chapterdfId) :

    if(is_a_dfc_dataframe_loaded()) : 
        
        saved_df    =   get_config_value(chapterdfId)
        
        if(saved_df is None) :
            drop_config_value(saved_df)
            return(None)
        else :
            df  =   get_dfc_dataframe_df(saved_df)
            if(df is None) :
                drop_config_value(saved_df)
                return(None)
            else :
                return(df)
    
    else :
        return(None)

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

DATA_TYPES_FLAG_KEY                     =   "columnDataTypeChange"

CLEANSING_COL_KEY                       =   "datacleansingcolumn"
CLEANSING_ROW_KEY                       =   "datacleansingrow"

"""
#--------------------------------------------------------------------------
#   Export config value keys
#--------------------------------------------------------------------------
"""
CURRENT_EXPORTED_FILE_NAME_KEY          =   "currentExportedFileName"
CURRENT_EXPORT_START_TIME               =   "exportStartTime"

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
COMPAT_COL_KEY                          =   "CompatColumn"

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
CENSUS_DOWNLOAD_LISTS                   =   "censusdownloadlists"
CENSUS_CURRENT_MODE                     =   "censuscurrentmode"
CENSUS_DROP_DATASET_LISTS               =   "censusdropdataset"
CENSUS_DROP_SUBDATASET_LIST             =   "censusdropsubdataset"
CENSUS_CURRENT_DATASET                  =   "censuscurrentdataset"
CENSUS_CURRENT_GET_COLS_SUBDATA_ID      =   "censuscurrentgetcolssubdataid"
CENSUS_CURRENT_GET_COLS_DTYPE_ID        =   "censuscurrentgetcolsdtypeid"
CENSUS_GET_COLS_COLUMNS_LIST_ID         =   "censusgetcolscolslist"
CENSUS_ADD_DATASETS_LIST                =   "censusadddatasets"
CENSUS_DROP_DATASETS_LIST               =   "censusdropdatasets"



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


"""
#--------------------------------------------------------------------------
#   global keys that should be stored at the dfcleanser level
#--------------------------------------------------------------------------
"""
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

    utilcbs     =   [0,0,0,0,0]

    if(not (cellsList == None)) :
        
        if(cellsList[20])    :   utilcbs[0] = 1
        if(cellsList[21])    :   utilcbs[1] = 1
        if(cellsList[22])    :   utilcbs[2] = 1
        if(cellsList[23])    :   utilcbs[3] = 1
        if(cellsList[24])    :   utilcbs[4] = 1

    return([utilcbs])
    

def set_chapters_loaded(cellsList) :
    
    set_config_value(DFC_CHAPTERS_LOADED_KEY, cellsList)
    
    cblist  =   get_chapters_loaded_cbs()
    
    set_config_value(UTILITIES_CBS_KEY,cblist[0])

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
