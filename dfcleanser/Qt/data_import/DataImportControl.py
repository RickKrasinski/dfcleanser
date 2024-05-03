"""
# DataImportControl
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:29:22 2017

@author: Rick
"""

import sys
this = sys.modules[__name__]


import inspect
#from PyQt#5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QStackedWidget

from PyQt5.QtCore import Qt
#from PyQt5 import uic


#import dfcleanser.common.cfg as cfg 

DEBUG_DATA_IMPORT               =   False
DEBUG_DATA_IMPORT_HISTORIES     =   False
DEBUG_DATA_IMPORT_FILE_TYPE     =   False
DEBUG_DATA_IMPORT_DETAILS       =   False
DEBUG_DATA_IMPORT_FORMS         =   False
DEBUG_DATA_IMPORT_SAVE          =   False

DEBUG_DATA_IMPORT_CSV           =   False
DEBUG_DATA_IMPORT_FWF           =   False
DEBUG_DATA_IMPORT_EXCEL         =   False
DEBUG_DATA_IMPORT_JSON          =   False
DEBUG_DATA_IMPORT_HTML          =   False
DEBUG_DATA_IMPORT_SQLTABLE      =   False
DEBUG_DATA_IMPORT_SQLQUERY      =   False
DEBUG_DATA_IMPORT_CUSTOM        =   False


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -           general Data Inspection Housekeeping                -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

import logging
logger = logging.getLogger(__name__)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

# Set the exception hook to our wrapping function
sys.excepthook = except_hook

# Enables PyQt event loop in IPython
from dfcleanser.sw_utilities.dfc_qt_model import fix_ipython
fix_ipython()




# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                    Data Import methods                        -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


import dfcleanser.Qt.data_import.DataImportModel as DIM
from dfcleanser.common.common_utils import opStatus, get_parms_for_input


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                Data Import processing methods                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#



# -----------------------------------------------------------------#
# -                   Data Import format parms                    -#
# -----------------------------------------------------------------#

def process_import_form(formid, parms,parent) :
    """
    * -------------------------------------------------------
    * 
    * parms :
    *  formid   -   form id
    *  parms    -   import parms                      
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    if(1):#DEBUG_DATA_IMPORT) :
        print("[process_import_form] formid : ",formid,"\n  ",parms)

    print("[parent ",type(parent),type(parent.statusBar))
    opstat  =   opStatus()   
    
    try :
        
        if( (formid == DIM.CSV_IMPORT)  or (formid == DIM.EXCEL_IMPORT) or 
            (formid == DIM.JSON_IMPORT) or (formid == DIM.HTML_IMPORT) or 
            (formid == DIM.FWF_IMPORT)  or (formid == DIM.CUSTOM_IMPORT) or 
            (formid == DIM.XML_IMPORT)  or (formid == DIM.PDF_IMPORT))  :
    
            if (formid == DIM.CSV_IMPORT) :
                opstat      =   import_pandas_csv(parms,parent)
                
                parmstitle  =   "Pandas CSV Import Parms"
                parmslist   =   DIM.pandas_import_csv_labelList[:8]
                parmslist.pop(1)
                parms.pop(1)

            elif (formid == DIM.FWF_IMPORT) :
                opstat      =   import_pandas_fwf(parms,parent)
            
                parmstitle  =   "Pandas FWF Import Parms"
                parmslist   =   DIM.pandas_import_fwf_labelList[:9]
                parmslist.pop(1)
                parms.pop(1)
        
            elif (formid == DIM.EXCEL_IMPORT) :
                opstat      =   import_pandas_excel(parms,parent)
            
                parmstitle  =   "Pandas Excel Import Parms"
                parmslist   =   DIM.pandas_import_excel_labelList[:9]
                parmslist.pop(1)
                parms.pop(1)
        
            elif (formid == DIM.JSON_IMPORT) : 
                opstat      =   import_pandas_json(parms,parent)
            
                parmstitle  =   "Pandas JSON Import Parms"
                parmslist   =   DIM.pandas_import_json_labelList[:7]
        
            elif (formid == DIM.HTML_IMPORT) : 
                dfs         =   import_pandas_html(parms,parent,opstat)

                if(opstat.get_status()) :
                    parent.display_import_json_dfs(dfs)
            
            elif (formid == DIM.XML_IMPORT) : 
                opstat      =   import_pandas_xml(parms,parent)

                parmstitle  =   "Pandas XML Import Parms"
                parmslist   =   DIM.pandas_import_xml_labelList[:6]
                parmslist.pop(1)
                parms.pop(1)

            elif (formid == DIM.CUSTOM_IMPORT) : 
                (dispstats, opstat)     =   import_custom(parms)
                
                print("dispstats",dispstats)
            
                if(dispstats) :
                    
                    fparms      =   get_parms_for_input(parms,DIM.custom_import_idList)
                    parmstitle  =   "Custom Import Parms"
                    parmslist   =   DIM.custom_import_labelList[:3]
                    
                    print("fparms\n",fparms)
                        
                    fparms[2] = fparms[2].replace("\n","</br>")
                    fparms[2] = fparms[2].replace("\'",'"')
                    fparms[2] = fparms[2].replace('"',"'")
                    print("fparms\n",fparms)
                    
                    fparms[1] = ""
                    from dfcleanser.common.cfg import DataImport_ID
                    DIM.display_data_import_parms(parmstitle,parmslist,fparms,DataImport_ID,fparms[0],True)
                    
            elif (formid == DIM.IMPORT_MORE) : 
                (dispstats, opstat)     =   import_custom(parms,parent)
         
           
            if(not (formid == DIM.HTML_IMPORT)) :
            
                # check if import was successful        
                if(opstat.get_status()) : 
                    parent.display_import_status(formid, parms[0])
                else :
                    from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                    display_exception("dfcleanser Import","Import failed",opstat.get_exception())
    

        # -----------------------------------------------------#
        # -             SQL Import Functions                  -#
        # -----------------------------------------------------#
        
        elif (formid == DIM.SQLTABLE_IMPORT) : 
            opstat  =   import_sql_table(parms,parent)
                
            # check if import was successful        
            if(opstat.get_status()) : 
                parent.display_import_status(formid, parms[0])
            else :
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception("dfcleanser Import","Import failed",opstat.get_exception())
        
        elif (formid == DIM.SQLQUERY_IMPORT) :

            opstat  =   import_sql_query(parms,parent)
        
            # check if import was successful        
            if(opstat.get_status()) : 
                parent.display_import_status(formid, parms[0])
            else :
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception("dfcleanser Import","Import failed",opstat.get_exception())



        else :

            title       =   "dfcleanser error"
            status_msg  =   "[process_import_form] error : invalid form type"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

    except Exception as e:

        title       =   "dfcleanser exception"
        status_msg  =   "[process_import_form] error "
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,e)

    if(DEBUG_DATA_IMPORT) :
        print("[process_import_form] end : ",opstat.get_status())


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   process pandas import functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_import_addl_parms_dict(detid,addl_parms,opstat) :
    """
    * --------------------------------------------------------
    * function : get addl parms for dict 
    * parms :
    *   detid   -   type details
    *   parms   -   json parms dict
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    if(DEBUG_DATA_IMPORT_DETAILS) :
        print("[get_import_addl_parms_dict]",detid,"\n",addl_parms)
    
    try :
        
        if(len(addl_parms) > 0) :
            
            import json
    
            addl_parms_dict     =   json.loads(addl_parms)

            if(DEBUG_DATA_IMPORT_DETAILS) :
                print("[get_import_addl_parms_dict] addl_parms_dict : \n  ",addl_parms_dict)

            dkeys   =   list(addl_parms_dict.keys())
    
            for i in range(len(dkeys)) :
                
                new_dkey    =   dkeys[i].replace("'","")
                new_dkey    =   dkeys[i].replace('"',"")
                
                new_dtype   =   DIM.get_addl_parm_dtype(detid,new_dkey)
                
                if(addl_parms_dict.get(dkeys[i]) == "False") :
                    addl_parms_dict.update({new_dkey:False})
                elif(addl_parms_dict.get(dkeys[i]) == "True") :
                    addl_parms_dict.update({new_dkey:True})
                elif(addl_parms_dict.get(dkeys[i]) == "None") :
                    addl_parms_dict.update({new_dkey:None})
                else :
                    
                    if(new_dtype == int) :
                        try :
                            new_value   =   int(addl_parms_dict.get(dkeys[i]))
                        except :
                            new_value   =   None
                            
                    elif(new_dtype == str) :
                        new_value   =   str(addl_parms_dict.get(dkeys[i]))
                        
                    else :
                        new_value   =   None
                        
                    addl_parms_dict.update({new_dkey:new_value})
                    
        else :
            
            addl_parms_dict     =   None    
                
    except Exception as e:

        if(DEBUG_DATA_IMPORT_DETAILS) :
            print("[get_import_addl_parms_dict] exception  ")
            
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception

        display_exception("dfcleanser Import","Import failed",e)


        opstat.store_exception("Unable to parse adittional parms string." + addl_parms,e)

    if(opstat.get_status()) :
        return(addl_parms_dict)
    else :
        return(None)
    

def save_import_data(importid,df_title,df,fparms,full_parms,addl_parms,methodTitle,file_path,importFormId,opstat) :
    """
    * --------------------------------------------------------
    * function : save imporet data 
    * parms :
    *   detid   -   type details
    *   parms   -   json parms dict
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    

    if(DEBUG_DATA_IMPORT_SAVE) :
        print("\n  [save_import_data] importid ; dftitle : ",importid,df_title)
        print("  [save_import_data] fparms : \n    ",fparms)
        print("  [save_import_data] full_parms : \n    ",full_parms)
        print("  [save_import_data] addl_parms : \n    ",addl_parms,"\n")

    try :
        DIM.ImportHistory.add_to_history(importid,df_title,full_parms,addl_parms)

        if(DEBUG_DATA_IMPORT_SAVE) :
            print("  [save_import_data][" + methodTitle + "] Import History added : ",opstat.get_status())

    except Exception as e:
        opstat.store_exception("Unable to save import parms to history",e)
            
        title       =   "dfcleanser exception"       
        status_msg  =   "[" + methodTitle + "] error "
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,e)


    import dfcleanser.common.cfg as cfg

    if(opstat.get_status()) :
        
        try :

            cfg.add_df_to_dfc(df_title,df,file_path," Import CSV File : " + file_path)
            
            if(DEBUG_DATA_IMPORT_SAVE) :
                print("[" + methodTitle + "] add_df_to_dfc : ")

            cfg.set_user_defined_df(df)

            if(DEBUG_DATA_IMPORT_SAVE) :
                print("[" + methodTitle + "] set_user_defined_df : ")

            cfg.set_config_value(cfg.CURRENT_IMPORT_DF,df_title)

            if(DEBUG_DATA_IMPORT_SAVE) :
                print("[" + methodTitle + "] df added : ")

        except Exception as e:
            opstat.store_exception("Unable to save import parms to history",e)
            
            title       =   "dfcleanser exception"       
            status_msg  =   "[" + methodTitle + "] save df error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

        
        if(len(fparms) > 0) :

            fparms[0]   =   df_title
            fparms[1]   =   df_title
            
            cfg_parms   =   []
            for i in range(len(fparms)) :
                if(i == 2) :
                    cfg_parms.append(file_path)  
                else :
                    cfg_parms.append(fparms[i])

            cfg.set_config_value(importFormId + "Parms",cfg_parms)
            cfg.set_config_value(cfg.CURRENT_EXPORTED_FILE_NAME_KEY,fparms[1],True)

            if(DEBUG_DATA_IMPORT_SAVE) :
                print("  [save_import_data][" + methodTitle + "] cfg parms stored : \n  ",cfg_parms)
                print("  [save_import_data][" + methodTitle + "] opstat : ",opstat.get_status())



import json
import pandas as pd

# -----------------------------------------------------------------#
# -                        Import CSV File                        -#
# -----------------------------------------------------------------#

def import_pandas_csv(fparms,parent) : 
    
    if(DEBUG_DATA_IMPORT_CSV) :
        print("\n[import_pandas_csv]\n",fparms)
    
    opstat      =   opStatus()
    importId    =   DIM.pandas_import_csv_id


    if(len(fparms) == 0) :
        
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
        
    else :
        
        if(len(fparms[0]) == 0):
            
            opstat.set_status(False)
            opstat.set_errorMsg("No df_title defined")
            
        else :
            
            df_title    =   fparms[0]
            
            if(len(fparms[2]) == 0):
                
                opstat.set_status(False)
                opstat.set_errorMsg("No file location defined")
                
            else :
                
                try :

                    if(DEBUG_DATA_IMPORT_CSV) :
                        print("[import_pandas_csv] df_title : ",df_title)
                
                    file_path   =   fparms[2]
                    file_path   =   file_path.replace("\\","/")
                    
                    pindex   =   3
                    if(len(fparms[pindex]) == 0):
                        csv_header   =   DIM.csv_import_parms_defaults[1]
                    else :
                        if(fparms[pindex] == DIM.csv_import_parms_defaults[1]):
                            csv_header   =   DIM.csv_import_parms_defaults[1]
                        else :
                            csv_header   =   int(fparms[pindex])
                                    
                    pindex   =   4
                    if(len(fparms[pindex]) == 0):
                        col_names   =   DIM.csv_import_parms_defaults[2]
                    else :
                        try :
                            col_names   =   json.loads(fparms[pindex])    
                        except :
                            col_names   =   DIM.csv_import_parms_defaults[2]
                    
                    pindex   =   5
                    if(len(fparms[pindex]) == 0):
                        csv_index_col   =   DIM.csv_import_parms_defaults[3]
                    else :
                        csv_index_col   =   int(fparms[pindex])

                    pindex   =   6
                    if(len(fparms[pindex]) == 0):
                        dtypes   =  DIM.csv_import_parms_defaults[4]
                    else :
                        try :
                            dtypes   =   json.loads(fparms[pindex])    
                        except :
                            dtypes   =   DIM.csv_import_parms_defaults[4]
                    
                    pindex   =   7
                    csv_addl_parms  =   get_import_addl_parms_dict(DIM.CSV_IMPORT,fparms[7],opstat)

                    if(DEBUG_DATA_IMPORT_CSV) :
                        print("[import_pandas_csv] csv_addl_parms : ",csv_addl_parms)
                    
                except Exception as e:
                    opstat.store_exception("Invalid Import Parm " + DIM.pandas_import_csv_labelList[pindex] + " : " + fparms[pindex],e)

    if(opstat.get_status()) :
                    
        if(DEBUG_DATA_IMPORT_CSV) :
            print("[import_pandas_csv] parms loaded : ")

        try :
            if(csv_addl_parms is None) :
                df = pd.read_csv(file_path, header=csv_header, names=col_names, index_col=csv_index_col, dtype=dtypes)
            else :
                df = pd.read_csv(file_path, header=csv_header, names=col_names, index_col=csv_index_col, dtype=dtypes, **csv_addl_parms)
        except Exception as e:
            opstat.store_exception("Unable to import csv file" + fparms[2],e)

            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception("dfcleanser Import","CSV Import failed",opstat.get_exception())

    print("[import_pandas_csv] : after csv import",opstat.get_status())        
    if(opstat.get_status()) : 

        if(DEBUG_DATA_IMPORT_CSV) :
            print("[import_pandas_csv] csv imported : ")
        
        csv_full_parms  =   []
        csv_full_parms.append(file_path)
        csv_full_parms.append(csv_header)
        csv_full_parms.append(col_names)
        csv_full_parms.append(csv_index_col)
        csv_full_parms.append(dtypes)

        save_import_data(DIM.CSV_IMPORT,df_title,df,fparms,csv_full_parms,csv_addl_parms,"import_pandas_csv",file_path,importId,opstat) 

    from dfcleanser.Qt.data_import.DataImportModel import get_text_for_import_type, CSV_IMPORT
    file_text   =   get_text_for_import_type(CSV_IMPORT)

    parent.statusbar.showMessage(file_text + " : Complete")

    return(opstat)

# -----------------------------------------------------------------#
# -                        Import FWF File                        -#
# -----------------------------------------------------------------#
    
def import_pandas_fwf(fparms,parent) : 
    
    if(DIM.DEBUG_IMPORT_FILE) :
        print("import_pandas_fwf : \n",fparms)   

    opstat      =   opStatus()
    importId    =   DIM.pandas_import_fwf_id 
    
    if(len(fparms) == 0) :
        
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
        
    else :
        
        if(len(fparms[0]) == 0):
            opstat.set_status(False)
            opstat.set_errorMsg("No df_title defined")
        else :
            
            df_title    =   fparms[0]
            
            if(len(fparms[2]) == 0):
                
                opstat.set_status(False)
                opstat.set_errorMsg("No file location defined")
                
            else :
                
                try :

                    pindex      =   2
                    file_path   =   fparms[2]
                    file_path   =   file_path.replace("\\","/")
                
                    pindex  =   3
                    if(len(fparms[pindex]) == 0):
                        fwf_colspecs   =   None
                    else :
                        fwf_colspecs   =   fparms[pindex]
                
                    pindex  =   4
                    if(len(fparms[pindex]) == 0):
                        fwf_widths   =   None
                    else :
                        try :
                            fwf_widths      =   json.loads(fparms[pindex])    
                        except :
                            fwf_widths      =   fparms[pindex]

                    pindex  =   5
                    if(len(fparms[pindex]) == 0):
                        fwf_infer_nrows     =   100
                    else :
                        fwf_infer_nrows     =   int(fparms[pindex])

                    pindex  =   6
                    if(len(fparms[pindex]) == 0):
                        fwf_kwds   =   None
                    else :
                        try :
                            fwf_kwds   =   json.loads(fparms[pindex])    
                        except :
                            fwf_kwds   =   None
                    
                    fwf_addl_parms  =   None

                    
                    if(DEBUG_DATA_IMPORT) :
                        print("[import_pandas_fwf] fwf_kwds : ",fwf_kwds)

                
                except Exception as e:
                    opstat.store_exception("Invalid Import Parm " + DIM.pandas_import_fwf_labelList[pindex] + " : " + fparms[pindex],e)

    if(opstat.get_status()) :

        if(DEBUG_DATA_IMPORT) :
            print("[import_pandas_fwf] parms loaded : ",file_path,fwf_colspecs,fwf_widths,fwf_infer_nrows)

        try :
            if(fwf_kwds is None) :
                if(fwf_colspecs is None) :
                    df = pd.read_fwf(file_path,widths=fwf_widths,infer_nrows=fwf_infer_nrows)
                else :
                    df = pd.read_fwf(file_path,colspecs=fwf_colspecs,widths=fwf_widths,infer_nrows=fwf_infer_nrows)
            else :
                if(fwf_colspecs is None) :
                    df = pd.read_fwf(file_path,widths=fwf_widths,infer_nrows=fwf_infer_nrows,**fwf_kwds) 
                else :
                    df = pd.read_fwf(file_path,colspecs=fwf_colspecs,widths=fwf_widths,infer_nrows=fwf_infer_nrows,**fwf_kwds)
        except Exception as e:
            opstat.store_exception("Unable to import fwf file : " + fparms[2],e)
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception("dfcleanser Import","FWF Import failed",opstat.get_exception())

    if(opstat.get_status()) : 

        if(DEBUG_DATA_IMPORT) :
            print("[import_pandas_fwf] fwf imported : ")
        
        fwf_full_parms  =   []
        fwf_full_parms.append(file_path)
        fwf_full_parms.append(fwf_colspecs)
        fwf_full_parms.append(fwf_widths)
        fwf_full_parms.append(fwf_infer_nrows)
        fwf_full_parms.append(fwf_kwds)

        save_import_data(DIM.FWF_IMPORT,df_title,df,fparms,fwf_full_parms,fwf_addl_parms,"import_pandas_fwf",file_path,importId,opstat) 
    
    from dfcleanser.Qt.data_import.DataImportModel import get_text_for_import_type, FWF_IMPORT
    file_text   =   get_text_for_import_type(FWF_IMPORT)
    parent.statusbar.showMessage(file_text + " : Complete")

    return(opstat)

# -----------------------------------------------------------------#
# -                      Import EXCEl File                        -#
# -----------------------------------------------------------------#

def import_pandas_excel(fparms,parent) : 
    
    if(DEBUG_DATA_IMPORT) :
        print("\n  [import_pandas_excel]\n",fparms)

    opstat      =   opStatus()
    importId    =   DIM.pandas_import_excel_id
    
    if(len(fparms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
    else :
        
        if(len(fparms[0]) == 0):
            opstat.set_status(False)
            opstat.set_errorMsg("No df_title defined")
        else :
            
            df_title    =   fparms[0]
            
            if(len(fparms[2]) == 0):
                opstat.set_status(False)
                opstat.set_errorMsg("No file location defined")
            else :
                
                try :

                    if(DEBUG_DATA_IMPORT) :
                        print("  [import_pandas_excel] df_title : ",df_title)
                
                    file_path   =   fparms[2]
                    file_path   =   file_path.replace("\\","/")
                
                    pindex  =   3
                    if(len(fparms[pindex]) == 0):
                        excel_sheet   =   DIM.excel_import_parms_defaults[1]
                    else :
                        excel_sheet   =   int(fparms[pindex])

                    pindex  =   4
                    if(len(fparms[pindex]) == 0):
                        excel_header   =   DIM.excel_import_parms_defaults[2]
                    else :
                        if(fparms[pindex] == DIM.excel_import_parms_defaults[2]):
                            excel_header   =   DIM.excel_import_parms_defaults[2]
                        else :
                            excel_header   =   int(fparms[pindex])
                    
                    pindex  =   5
                    if(len(fparms[pindex]) == 0):
                        col_names   =   DIM.excel_import_parms_defaults[3]
                    else :
                        try :
                            col_names   =   json.loads(fparms[pindex])    
                        except :
                            col_names   =   DIM.excel_import_parms_defaults[3]

                    pindex  =   6
                    if(len(fparms[pindex]) == 0):
                        excel_index_col   =   DIM.excel_import_parms_defaults[4]
                    else :
                        excel_index_col   =   int(fparms[pindex])

                    pindex  =   7
                    if(len(fparms[pindex]) == 0):
                        dtypes   =   DIM.excel_import_parms_defaults[5]
                    else :
                        try :
                            dtypes   =   json.loads(fparms[pindex])    
                        except :
                            dtypes   =   DIM.excel_import_parms_defaults[5]

                    excel_addl_parms  =   get_import_addl_parms_dict(DIM.EXCEL_IMPORT,fparms[8],opstat)
                    
                    if(DEBUG_DATA_IMPORT) :
                        print("  [import_pandas_excel] excel_addl_parms : ",excel_addl_parms)
                
                except Exception as e:

                    title       =   "dfcleanser exception"
                    status_msg  =   "[import_pandas_excel] Invalid Import Parm " + str(pindex)
                    from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                    display_exception(title,status_msg,e)

                    opstat.set_status(False)

                    #opstat.store_exception("Invalid Import Parm " + DIM.pandas_import_excel_labelList[pindex] + " : " + fparms[pindex],e)

    if(opstat.get_status()) :

        if(DEBUG_DATA_IMPORT) :
            print("  [import_pandas_excel] parms loaded : ")

        if(0):#try :
            from dfcleanser.common.common_utils import PyQtRunningClock
            ImportClock     =   PyQtRunningClock(parent.form.ClockLabel)
            ImportClock.runClock()
        #except Exception as e:
        #    print("clock fail")


        #print("runClock")
        
        try :
            if(excel_addl_parms is None) :
                df = pd.read_excel(file_path, sheet_name=excel_sheet, header=excel_header, names=col_names, index_col=excel_index_col, dtype=dtypes)
            else :
                df = pd.read_excel(file_path, sheet_name=excel_sheet, header=excel_header, names=col_names, index_col=excel_index_col, dtype=dtypes, **excel_addl_parms)
        except Exception as e:

            title       =   "dfcleanser exception"
            status_msg  =   "[import_pandas_excel] Invalid Import Parm "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)



            #opstat.store_exception("Unable to import excel file" + fparms[2],e)

    if(opstat.get_status()) : 

        if(DEBUG_DATA_IMPORT) :
            print("[import_pandas_excel] excel imported : ")
        
        excel_full_parms  =   []
        excel_full_parms.append(file_path)
        excel_full_parms.append(excel_sheet)
        excel_full_parms.append(excel_header)
        excel_full_parms.append(col_names)
        excel_full_parms.append(excel_index_col)
        excel_full_parms.append(dtypes)

        save_import_data(DIM.EXCEL_IMPORT,df_title,df,fparms,excel_full_parms,excel_addl_parms,"import_pandas_excel",file_path,importId,opstat) 

    from dfcleanser.Qt.data_import.DataImportModel import get_text_for_import_type, EXCEL_IMPORT
    file_text   =   get_text_for_import_type(EXCEL_IMPORT)
    parent.statusbar.showMessage(file_text + " : Complete")
    
    return(opstat)

# -----------------------------------------------------------------#
# -                       Import JSON File                        -#
# -----------------------------------------------------------------#
 
def import_pandas_json(fparms,parent) : 
    
    if(DEBUG_DATA_IMPORT) :
        print("\n[import_pandas_json]\n",fparms)
    
    opstat      =   opStatus()
    importId    =   DIM.pandas_import_json_id
    
    if(len(fparms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
    else :
        
        if(len(fparms[0]) == 0):
            opstat.set_status(False)
            opstat.set_errorMsg("No df_title defined")
        else :
            
            df_title    =   fparms[0]
        
            if(len(fparms[2]) == 0):
                opstat.set_status(False)
                opstat.set_errorMsg("No file_path defined")
            else :
                
                try :

                    if(DEBUG_DATA_IMPORT) :
                        print("[import_pandas_json] df_title : ",df_title)
            
                    file_path   =   fparms[2]
                    file_path   =   file_path.replace("\\","/")
                
                    pindex  =   3
                    if(len(fparms[pindex]) == 0):
                        orient_parm   =   DIM.json_import_parms_defaults[1]
                    else :
                        orient_parm   =   fparms[pindex]

                    pindex  =   4
                    if(len(fparms[pindex]) == 0):
                        typ_parm   =   DIM.json_import_parms_defaults[2]
                    else :
                        if(fparms[pindex] == DIM.json_import_parms_defaults[2]):
                            typ_parm   =   DIM.json_import_parms_defaults[2]
                        else :
                            typ_parm   =   fparms[pindex]
                    
                    pindex  =   5
                    if(len(fparms[pindex]) == 0):
                        dtypes   =   DIM.json_import_parms_defaults[3]
                    else :
                        try :
                            dtypes   =   json.loads(fparms[pindex])    
                        except :
                            dtypes   =   DIM.json_import_parms_defaults[3]

                    json_addl_parms  =   get_import_addl_parms_dict(DIM.JSON_IMPORT,fparms[6],opstat)
                    
                    if(DEBUG_DATA_IMPORT) :
                        print("[import_pandas_json] json_addl_parms : ",json_addl_parms)
                   
                except Exception as e:
                    opstat.store_exception("Invalid Import Parm " + DIM.pandas_import_json_labelList[pindex] + " : " + fparms[pindex],e)
            
    if(opstat.get_status()) :
        
        if(DEBUG_DATA_IMPORT) :
            print("[import_pandas_json] parms loaded : ")

        try :
            if(json_addl_parms is None) :
                df = pd.read_json(file_path, orient=orient_parm, typ=typ_parm, dtype=dtypes)
            else :
                df = pd.read_json(file_path, orient=orient_parm, typ=typ_parm, dtype=dtypes, **json_addl_parms)
        except Exception as e:
            opstat.store_exception("Unable to import json file" + fparms[2],e)

    if(opstat.get_status()) : 

        if(DEBUG_DATA_IMPORT) :
            print("[import_pandas_json] json imported : ")
        
        json_full_parms  =   []
        json_full_parms.append(file_path)
        json_full_parms.append(orient_parm)
        json_full_parms.append(typ_parm)
        json_full_parms.append(dtypes)

        save_import_data(DIM.JSON_IMPORT,df_title,df,fparms,json_full_parms,json_addl_parms,"import_pandas_json",file_path,importId,opstat) 

    from dfcleanser.Qt.data_import.DataImportModel import get_text_for_import_type, JSON_IMPORT
    file_text   =   get_text_for_import_type(JSON_IMPORT)
    parent.statusbar.showMessage(file_text + " : Complete")

    return(opstat)

# -----------------------------------------------------------------#
# -                       Import XML File                         -#
# -----------------------------------------------------------------#
 
def import_pandas_xml(fparms,parent) : 
    
    if(DEBUG_DATA_IMPORT) :
        print("\n[import_pandas_xml]\n",fparms)
    
    opstat      =   opStatus()
    importId    =   DIM.pandas_import_json_id
    
    if(len(fparms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
    else :
        
        if(len(fparms[0]) == 0):
            opstat.set_status(False)
            opstat.set_errorMsg("No df_title defined")
        else :
            
            df_title    =   fparms[0]
        
            if(len(fparms[2]) == 0):
                opstat.set_status(False)
                opstat.set_errorMsg("No file_path defined")
            else :
                
                try :

                    if(DEBUG_DATA_IMPORT) :
                        print("[import_pandas_xml] df_title : ",df_title)
            
                    file_path   =   fparms[2]
                    file_path   =   file_path.replace("\\","/")
                
                    pindex  =   3
                    if(len(fparms[pindex]) == 0):
                        xpath   =   "./*"
                    else :
                        xpath   =   fparms[pindex]
                    print("[import_pandas_xml] xpath : ",xpath)
                    pindex  =   4
                    if(len(fparms[pindex]) == 0):
                        namespaces   =   None
                    else :

                        try :

                            import json
                            namespaces  =   json.loads(fparms[pindex])

                        except Exception as e:

                            title       =   "dfcleanser exception"       
                            status_msg  =   "[import_pandas_xml] parse xml error "
                            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                            display_exception(title,status_msg,e)

                            opstat.set_status(False)

                    if(opstat.get_status()) :

                        pindex  =   5

                        if(fparms[pindex] == "False"):
                            elems_only   =   False
                        else :
                            elems_only   =   True

                        pindex  =   6
                        if(fparms[pindex] == "False"):
                            attrs_only   =   False
                        else :
                            attrs_only   =   True

                        xml_addl_parms  =   get_import_addl_parms_dict(DIM.XML_IMPORT,fparms[7],opstat)
                    
                        if(DEBUG_DATA_IMPORT) :
                            print("[import_pandas_xml] xml_addl_parms : ",xml_addl_parms)
                   
                except Exception as e:
                    opstat.store_exception("Invalid Import Parm " + DIM.pandas_import_xml_labelList[pindex] + " : " + fparms[pindex],e)
            
    if(opstat.get_status()) :
        
        if(DEBUG_DATA_IMPORT) :
            print("[import_pandas_xml] parms loaded : ")
            print("path",file_path)
            print("xpath",xpath)
            print("namespaces",namespaces)
            print("elems_only",elems_only)
            print("attrs_only",attrs_only)
            print("xml_addl_parms",xml_addl_parms)

        try :
            if(xml_addl_parms is None) :
                df = pd.read_xml(file_path, xpath=xpath, namespaces=namespaces, elems_only=elems_only, attrs_only=attrs_only)
            else :
                df = pd.read_xml(file_path, xpath=xpath, namespaces=namespaces, elems_only=elems_only, attrs_only=attrs_only, **xml_addl_parms)
        except Exception as e:
            opstat.store_exception("Unable to import xml file" + fparms[2],e)

            title       =   "dfcleanser exception"       
            status_msg  =   "[display_import_with_parms][Unable to import xml file] "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)


    if(opstat.get_status()) : 

        if(DEBUG_DATA_IMPORT) :
            print("[import_pandas_xml] xml imported : ")
        
        xml_full_parms  =   []
        xml_full_parms.append(file_path)
        xml_full_parms.append(xpath)
        try :

            import json
            nspaces     =   json.dumps(namespaces)

        except Exception as e:

            nspaces     =   "{}"

        xml_full_parms.append(nspaces)
        xml_full_parms.append(elems_only)
        xml_full_parms.append(attrs_only)

        save_import_data(DIM.XML_IMPORT,df_title,df,fparms,xml_full_parms,xml_addl_parms,"import_pandas_xml",file_path,importId,opstat) 

    from dfcleanser.Qt.data_import.DataImportModel import get_text_for_import_type, XML_IMPORT
    file_text   =   get_text_for_import_type(XML_IMPORT)
    parent.statusbar.showMessage(file_text + " : Complete")

    return(opstat)

# -----------------------------------------------------------------#
# -                       Import PDF File                         -#
# -----------------------------------------------------------------#
 
"""
def import_pandas_pdf(fparms) : 
    
    if(DEBUG_DATA_IMPORT) :
        print("\n[import_pandas_xml]\n",fparms)
    
    opstat      =   opStatus()
    importId    =   DIM.pandas_import_json_id
    
    if(len(fparms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
    else :
        
        if(len(fparms[0]) == 0):
            opstat.set_status(False)
            opstat.set_errorMsg("No df_title defined")
        else :
            
            df_title    =   fparms[0]
        
            if(len(fparms[2]) == 0):
                opstat.set_status(False)
                opstat.set_errorMsg("No file_path defined")
            else :
            
                file_path   =   fparms[2]
                file_path   =   file_path.replace("\\","/")

            pdf_addl_parms  =   None
            
    if(opstat.get_status()) :
        
        if(DEBUG_DATA_IMPORT) :
            print("[import_pandas_pdf] parms loaded : ")

        from dfcleanser.common.common_utils import RunningClock
        from IPython.display import clear_output
        clear_output()
        clock = RunningClock()
        clock.start()

        import tabula-py 
        
        try :
            dfs = tabula.read_pdf(file_path,pages="all")
        except Exception as e:
            opstat.store_exception("Unable to import pdf file" + fparms[2],e)

    if(opstat.get_status()) : 

        if(DEBUG_DATA_IMPORT) :
            print("[import_pandas_json] pdf imported : ")
        
        pdf_full_parms  =   []
        pdf_full_parms.append(file_path)

        save_import_data(DIM.XML_IMPORT,df_title,dfs,fparms,pdf_full_parms,pdf_addl_parms,"import_pandas_xml",file_path,importId,opstat) 

    if(not (clock is None)) :
        clock.stop()

    return(opstat)
"""
# -----------------------------------------------------------------#
# -                      Import HTML page                         -#
# -----------------------------------------------------------------#
   
def import_pandas_html(fparms,parent,opstat) : 

    if(DEBUG_DATA_IMPORT) :
        print("[import_pandas_html] : \n",fparms)   
    
    if(len(fparms) == 0) :
        
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
        
    else :
        
        if(len(fparms[0]) == 0):
            
            opstat.set_status(False)
            opstat.set_errorMsg("No 'html_url_title' defined")
            
        else :
            
            html_url    =   fparms[0]
            
            try :
                
                pindex  =   2
                if( (fparms[pindex] is None) or (len(fparms[pindex]) == 0) ):
                    match_parm   =   DIM.html_import_parms_defaults[0]
                else :
                    match_parm   =   fparms[pindex]

                pindex  =   3
                if(len(fparms[pindex]) == 0):
                    flavor_parm   =   DIM.html_import_parms_defaults[1]
                else :
                    flavor_parm   =   fparms[pindex]
                
                pindex  =   4    
                if(len(fparms[pindex]) == 0):
                    header_parm   =   DIM.html_import_parms_defaults[2]
                else :
                    try :
                        header_parm   =   int(fparms[pindex])    
                    except :
                        header_parm   =   DIM.html_import_parms_defaults[2]
                
                pindex  =   5
                if(len(fparms[pindex]) == 0) :
                    html_addl_parms     =   None 
                else :
                    html_addl_parms  =   get_import_addl_parms_dict(DIM.HTML_IMPORT,fparms[pindex],opstat)
                    
            except Exception as e:
                #opstat.store_exception("Invalid Import Parm " + DIM.pandas_import_html_labelList[pindex] + " : " + fparms[pindex],e)

                title       =   "dfcleanser exception"
                status_msg  =   "[import_pandas_html] invalid parm " + str(pindex)
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

                opstat.set_status(False)

    
    if(opstat.get_status()) : 

        if(DEBUG_DATA_IMPORT) :
             print("[import_pandas_html] : html_url",type(html_url),html_url)

        try :
            if(html_addl_parms is None) :
                dfs = pd.read_html(html_url,match=match_parm,flavor=flavor_parm,header=header_parm)
            else :
                dfs = pd.read_html(html_url,match=match_parm,flavor=flavor_parm,header=header_parm, **html_addl_parms)
        except Exception as e:

            #opstat.store_exception("Unable to import html file : " + html_url,e)

            title       =   "dfcleanser exception"
            status_msg  =   "[import_pandas_html] import fail "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)

    
    #from dfcleanser.Qt.data_import.DataImportModel import get_text_for_import_type,HTML_IMPORT
    #file_text   =   get_text_for_import_type(HTML_IMPORT)
    #parent.statusbar.showMessage(file_text + " : Complete")
            
    if(opstat.get_status()) : 

        if(DEBUG_DATA_IMPORT_DETAILS) :
             print("[import_pandas_html] : dfs \n",dfs)
        
        return(dfs)
    
    else :
        
        return(None)


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                    SQL Import functions                       -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -                        Import SQLRable                        -#
# -----------------------------------------------------------------#

def import_sql_table(fparms, parent) :
                
    if(DEBUG_DATA_IMPORT) :
        print("  [import_sql_table] fparms : \n    ",fparms)
    
    opstat  =   opStatus()

    from dfcleanser.sw_utilities.db_utils import dfc_dbconnectors_table, IMPORT_FLAG
    current_selected_connector  =   dfc_dbconnectors_table.get_current_dbconnector(IMPORT_FLAG)

    if(DEBUG_DATA_IMPORT) :
        print("  [import_sql_table] : dbconnector : ] ",type(current_selected_connector))
        current_selected_connector.dump()

    if(len(fparms) == 0) :
        
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
        
    else :
        
        if(len(fparms[0]) == 0):
            
            opstat.set_status(False)
            opstat.set_errorMsg("No 'df_title' defined")
            
        else :
            
            df_title    =   fparms[0]
            
            try :
                
                pindex  =   2
                if( (fparms[pindex] is None) or (len(fparms[pindex]) == 0) ):
                    opstat.set_errorMsg("No 'table' defined")
                    opstat.set_status(False)
                else :
                    table_name   =   fparms[pindex]

                if(opstat.get_status()) :

                    pindex  =   3
                    if(len(fparms[pindex]) == 0):
                        schema   =   DIM.sqlt_import_parms_defaults[1]
                    else :
                        schema   =   fparms[pindex]
                
                    pindex  =   4    
                    if(len(fparms[pindex]) == 0):
                        index_columns   =   DIM.sqlt_import_parms_defaults[2]
                    else :

                        try :

                            index_columns   =   fparms[pindex] 
                            index_columns   =   index_columns.replace("[","")
                            index_columns   =   index_columns.replace("]","")
                            index_columns   =   index_columns.split(",")

                        except :
                            opstat.set_errorMsg("index columns parm invalid format")
                            opstat.set_status(False)
                            index_columns     =   "Invalid"

                    if(opstat.get_status()) :

                        pindex  =   5
                        if(len(fparms[pindex]) == 0):
                            coerce   =   DIM.sqlt_import_parms_defaults[3]
                        else :
                            if(fparms[pindex] == "True") :
                                coerce  =   True
                            else :
                                coerce  =   False

                        pindex  =   6    
                        if(len(fparms[pindex]) == 0):
                            parse_dates   =   DIM.sqlt_import_parms_defaults[4]
                        else :

                            import json
                            try :
                                parse_dates   =   fparms[pindex] 
                                parse_dates   =   parse_dates.replace("[","")
                                parse_dates   =   parse_dates.replace("]","")
                                parse_dates   =   parse_dates.split(",")
                            except :
                                opstat.set_errorMsg("parse dates parm invalid format")
                                opstat.set_status(False)
                                parse_dates     =   "Invalid"

                        if(opstat.get_status()) :

                            pindex  =   7    
                            if(len(fparms[pindex]) == 0):
                                columns   =   DIM.sqlt_import_parms_defaults[5]
                            else :

                                import json
                                try :

                                    columns   =   fparms[pindex] 
                                    columns   =   columns.replace("[","")
                                    columns   =   columns.replace("]","")
                                    columns   =   columns.split(",")

                                except :
                                    opstat.set_errorMsg("columns parm not valid list")
                                    opstat.set_status(False)
                                    columns     =   "Invalid"
                           
                            if(opstat.get_status()) :

                                pindex  =   8    
                                if(len(fparms[pindex]) == 0):
                                    chunksize   =   DIM.sqlt_import_parms_defaults[6]
                                else :

                                    import json
                                    try :
                                        chunksize   =   int(fparms[pindex])  
                                    except :
                                        opstat.set_errorMsg("chunkize not a number")
                                        opstat.set_status(False)
                                        chunksize     =   "Invalid"
                    
            except Exception as e:

                title       =   "dfcleanser exception"       
                status_msg  =   "[import_sql_table] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)
    
        if(DEBUG_DATA_IMPORT) :
            print("  [import_sql_table] : after parse parms : ] ",opstat.get_status())

        if(not(opstat.get_status())) :

            title       =   "dfcleanser error"
            status_msg  =   "[import_sql_table] error : " + opstat.get_errorMsg()
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

        else :

            import dfcleanser.sw_utilities.db_utils as qdbu
            dbconDict   =   qdbu.get_current_dbcondict(0)
        
            if(DEBUG_DATA_IMPORT) :
                print("  [import_sql_table] : dbconDict : \n  ",dbconDict)

            dbcon = qdbu.dbConnector()
            dbcon.connect_to_db(qdbu.SQLALCHEMY,opstat,dbconDict)

            SQL_Server_ID   =  int(dbconDict.get("servertype")) 

            if(opstat.get_status()) :

                try :

                    dbconnector     =   dbcon.get_dbConnection()

                    if(SQL_Server_ID == qdbu.Oracle) :
                        df = pd.read_sql("select * from " + table_name,dbconnector)
                    else :

                        if(DEBUG_DATA_IMPORT) :
                            print("  [import_sql_table] : table_name : ",table_name)
                            print("  [import_sql_table] : schema : ",schema)
                            print("  [import_sql_table] : index_col : ",index_columns,type(index_columns))
                            print("  [import_sql_table] : coerce : ",coerce)
                            print("  [import_sql_table] : parse_dates : ",parse_dates,type(parse_dates))
                            print("  [import_sql_table] : columns : ",columns,type(columns))
                           

                        df = pd.read_sql_table(table_name, dbconnector, schema=schema, 
                                               index_col=index_columns, coerce_float=coerce, 
                                               parse_dates=parse_dates, columns=columns,
                                               chunksize=chunksize) 
                
                except Exception as e:

                    title       =   "dfcleanser exception"       
                    status_msg  =   "[import_sql_table] read_sql_table : error "
                    from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                    display_exception(title,status_msg,e)
                    opstat.set_status(False)
                
                if(opstat.get_status()) :

                    from PyQt5.QtWidgets import QMessageBox
                    dlg = QMessageBox()
                    dlg.setTextFormat(Qt.RichText)
                    dlg.setWindowTitle("Save Import To History")
                    dlg.setText("Save the current sql import to the import history log")
                    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                    dlg.setStyleSheet("QLabel{min-width: 350px;}")
            
                    button = dlg.exec()

                    if(button == QMessageBox.Yes) :

                        # add import to import history file
                        sql_import_parms        =   [table_name,schema,index_columns,coerce,parse_dates,columns,chunksize]
                    
                        if(DEBUG_DATA_IMPORT) :
                            print("  [import_sql_table] add history : ",df_title,"\n  ",sql_import_parms)
        
                        try :

                            from dfcleanser.Qt.data_import.DataImportModel import SQLTableImportData
                            current_SQL_Import      =   SQLTableImportData(dbconDict)
                            add_import_sqltable_to_import_history(df_title,sql_import_parms)

                        except Exception as e:

                            title       =   "dfcleanser exception"       
                            status_msg  =   "[import_sql_table] save import history error "
                            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                            display_exception(title,status_msg,e)
                            opstat.set_status(False)

                    if(opstat.get_status()) :

                        if(DEBUG_DATA_IMPORT) :
                            print("  [import_sql_table] adding df to dfc : ",df_title,"\n  ",sql_import_parms)

                        # add imported df to dfc dfs table
                        try :

                            from dfcleanser.common.cfg import  add_df_to_dfc, set_user_defined_df, set_config_value, CURRENT_IMPORT_DF
                            add_df_to_dfc(df_title,df,sql_import_parms[3],"SQL Table Import")
                            set_user_defined_df(df)
                            set_config_value(CURRENT_IMPORT_DF,df,sql_import_parms[2])

                        except Exception as e:

                            title       =   "dfcleanser exception"       
                            status_msg  =   "[import_sql_table] add df to dfcleanser error "
                            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                            display_exception(title,status_msg,e)
                            opstat.set_status(False)

        # set cfg values for new import
        if(opstat.get_status()) : 

            from dfcleanser.Qt.data_import.DataImportModel import pandas_import_sqltable_common_id
            from dfcleanser.common.cfg import  get_config_value
            current_SQL_Import.set_import_sqltable_cfg_values(df_title,sql_import_parms,pandas_import_sqltable_common_id + "Parms",opstat)
            
            if(DEBUG_DATA_IMPORT) :
                print("  [import_sql_table] : new_cfg_parms : ",get_config_value(pandas_import_sqltable_common_id + "Parms"),"\n")

    from dfcleanser.Qt.data_import.DataImportModel import get_text_for_import_type,SQLTABLE_IMPORT
    file_text   =   get_text_for_import_type(SQLTABLE_IMPORT)
    parent.statusbar.showMessage(file_text + " : Complete")

    return(opstat)    
 
    
def add_import_sqltable_to_import_history(dftitle,importparms) :
    """
    * -------------------------------------------------------------------------- 
    * function : add the sql table import to the import history table
    * 
    * parms :
    *  dftitle       -   pandas df title                     
    *  importparms   -   sql input form parms                      
    *
    * returns : N/A
    * -------------------------------------------------------
    """

    if(DEBUG_DATA_IMPORT) :
        print("  [add_import_sqltable_to_import_history] : dftitle : ",dftitle,"\n   importparms : \n   ",importparms)
    
    full_parms  =   [] 

    import dfcleanser.sw_utilities.db_utils as qdbu
    dbconDict   =   qdbu.get_current_dbcondict(0)

    full_parms.append(dbconDict.get("hostname"))
    full_parms.append(dbconDict.get("database"))

    for i in range(len(importparms)) :

        if(type(importparms[i]) is bool) :

            if(importparms[i]) :
                full_parms.append("True")
            else :
                full_parms.append("False")

        else :

            if(importparms[i] is None) :
                full_parms.append("")
            else :
                full_parms.append(str(importparms[i]))
    
    if(DEBUG_DATA_IMPORT) :
        print("  [add_import_sqltable_to_import_history] : full_parms : \n   ",full_parms)

    from dfcleanser.Qt.data_import.DataImportModel import ImportHistory, SQLTABLE_IMPORT
    ImportHistory.add_to_history(SQLTABLE_IMPORT,dftitle,full_parms,None)


def import_sql_query(fparms,parent,display=True) :
    """
    * --------------------------------------------------------
    * function : import from sql query into pandas dataframe 
    * 
    * parms :
    *  parms   -   sql input form parms                      
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    opstat  =   opStatus()
    
    if(DEBUG_DATA_IMPORT) :
        print("  [import_sql_query] fparms : \n    ",fparms)
    
    from dfcleanser.sw_utilities.db_utils import dfc_dbconnectors_table, IMPORT_FLAG
    current_selected_connector  =   dfc_dbconnectors_table.get_current_dbconnector(IMPORT_FLAG)

    if(DEBUG_DATA_IMPORT) :
        print("  [import_sql_query] : dbconnector : ] ",type(current_selected_connector))
        current_selected_connector.dump()

    if(len(fparms) == 0) :
        
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
        
    else :
        
        if(len(fparms[0]) == 0):
            
            opstat.set_status(False)
            opstat.set_errorMsg("No 'df_title' defined")
            
        else :
            
            df_title    =   fparms[0]
            
            if(len(fparms[1]) == 0):
                opstat.set_status(False)
                opstat.set_errorMsg("No sql query defined")

            else :

                sql_query_string    =  fparms[1] 

                if(len(fparms[3]) == 0):
                    tindex_col   =   DIM.sqlq_import_parms_defaults[1]
                else :
                    try :

                        str_index_col   =  fparms[3].replace("[","")
                        str_index_col   =  str_index_col.replace("[","") 
                        tindex_col      =  str_index_col.split(",") 

                    except Exception as e:

                        opstat.set_status(False)
            
                        title       =   "dfcleanser exception"       
                        status_msg  =   "[Unable to get index_col] error "
                        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                        display_exception(title,status_msg,e)

                if(opstat.get_status()) :                       

                    if(len(fparms[4]) == 0):
                        tcoerce_float   =   DIM.sqlq_import_parms_defaults[2]
                    else :
                        if(fparms[4] == "False") :
                            tcoerce_float   =   False
                        else :
                            tcoerce_float   =   True 

                    if(len(fparms[5]) == 0):
                        tsqlparms   =   DIM.sqlq_import_parms_defaults[3]
                    else :
                        try :

                            str_parsedates      =  fparms[5].replace("[","")
                            str_parsedates      =  str_parsedates.replace("[","") 
                            tsqlparms           =  str_parsedates.split(",")    

                        except Exception as e:

                            opstat.set_status(False)
            
                            title       =   "dfcleanser exception"       
                            status_msg  =   "[Unable to get query parms] error "
                            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                            display_exception(title,status_msg,e)

                    if(opstat.get_status()) :

                        if(len(fparms[6]) == 0):
                            tparsedates   =   DIM.sqlq_import_parms_defaults[3]
                        else :
                            try :

                                str_parsedates      =  fparms[6].replace("[","")
                                str_parsedates      =  str_parsedates.replace("[","") 
                                tparsedates         =  str_parsedates.split(",") 

                            except Exception as e:

                                opstat.set_status(False)
            
                                title       =   "dfcleanser exception"       
                                status_msg  =   "[Unable to get parse dates] error "
                                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                                display_exception(title,status_msg,e)

                        if(opstat.get_status()) :

                            if(len(fparms[7]) == 0):
                                tdates_formats   =   DIM.sqlt_import_parms_defaults[4]
                            else :
                                tdates_formats   =   fparms[7]

                            if(len(fparms[9]) == 0):
                                tchunksize   =   DIM.sqlq_import_parms_defaults[5]
                            else :
                                try :
                                    tchunksize   =   int(fparms[9])   
                                except :
                                    tchunksize   =   DIM.sqlq_import_parms_defaults[5]
                            
                                    opstat.set_status(False)
            
                                    title       =   "dfcleanser exception"       
                                    status_msg  =   "[Unable to get chunksize] error "
                                    from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                                    display_exception(title,status_msg,e)


        if(opstat.get_status()) :

            if(DEBUG_DATA_IMPORT) :   
                print("[import_pandas_sqlquery][parms]:")
                print("[import_pandas_sqlquery][sql_query_string]:",sql_query_string)
                print("[import_pandas_sqlquery][tindex_col]:",tindex_col)
                print("[import_pandas_sqlquery][tcoerce_float]:",tcoerce_float)
                print("[import_pandas_sqlquery][tsqlparms]:",tsqlparms)
                print("[import_pandas_sqlquery][tparsedates]:",tparsedates)
                print("[import_pandas_sqlquery][tdates_formats]:",tdates_formats)
                print("[import_pandas_sqlquery][tchunksize]:",tchunksize)

            from dfcleanser.common.common_utils import RunningClock
            #from IPython.display import clear_output
            #clear_output()
            
            import dfcleanser.sw_utilities.db_utils as qdbu
            dbconDict   =   qdbu.get_current_dbcondict(0)
        
            if(DEBUG_DATA_IMPORT) :
                print("  [import_sql_qwuery] : dbconDict : \n  ",dbconDict)

            dbcon = qdbu.dbConnector()
            dbcon.connect_to_db(qdbu.SQLALCHEMY,opstat,dbconDict)

            try :

                dbconnector     =   dbcon.get_dbConnection()

                df = pd.read_sql_query(str(sql_query_string),dbconnector,index_col=tindex_col,coerce_float=tcoerce_float,
                                       params=tsqlparms,parse_dates=tparsedates,chunksize=tchunksize)
            except Exception as e:
                opstat.store_exception("Unable to run sql query " + sql_query_string,e)


        if(opstat.get_status()) : 
        
            sqlq_full_parms  =   []
            sqlq_full_parms.append(df_title)
            sqlq_full_parms.append(sql_query_string)
            sqlq_full_parms.append(fparms[2])
            sqlq_full_parms.append(tindex_col)
            sqlq_full_parms.append(tcoerce_float)
            sqlq_full_parms.append(tsqlparms)
            sqlq_full_parms.append(tparsedates)
            sqlq_full_parms.append(fparms[7])
            sqlq_full_parms.append(tdates_formats)
            sqlq_full_parms.append(tchunksize)
            sqlq_full_parms.append(fparms[9])
        
            if(DIM.DEBUG_SQL_IMPORT) :   
                print("sqlq_full_parms",sqlq_full_parms)
                #print("sqlq_addl_parms",sqlq_addl_parms)
        
            try :
                DIM.ImportHistory.add_to_history(DIM.SQLQUERY_IMPORT,df_title,sqlq_full_parms,None)
            except Exception as e:
                opstat.store_exception("Unable to save import parms to history : for " + str(df_title),e)
        
            import dfcleanser.common.cfg as cfg
            cfg.add_df_to_dfc(df_title,df,sql_query_string,"SQL Qyery Import")
            cfg.set_user_defined_df(df)
            cfg.set_config_value(cfg.CURRENT_IMPORT_DF,df_title)
        
        
            if(len(fparms) > 0) :
                #sqlqueryparms[0]   =   df_title
                #sqlqueryparms[1]   =   df_title
                cfg.set_config_value(DIM.pandas_import_sqlquery_id + "Parms",fparms)
                cfg.set_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY,df_title,True)


    from dfcleanser.Qt.data_import.DataImportModel import get_text_for_import_type,SQLQUERY_IMPORT
    file_text   =   get_text_for_import_type(SQLQUERY_IMPORT)
    parent.statusbar.showMessage(file_text + " : Complete")

    return(opstat)    
 

"""
* -------------------------------------------------------------------------- 
* --------------------------------------------------------------------------
*                         Custom Import functions 
* -------------------------------------------------------------------------- 
* --------------------------------------------------------------------------
"""


def import_custom(parms,parent,display=True) :
    """
    * --------------------------------------------------------
    * function : import from custom into pandas dataframe 
    * 
    * parms :
    *  parms   -   associated import parms                      
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    if(DIM.DEBUG_SQL_IMPORT) :   
        print("import_custom",parms)

    functionid = DIM.PROCESS_CUSTOM_IMPORT#parms[0]
    
    opstat      =   opStatus()
    dispstats   =   False
    
    if(functionid == DIM.PROCESS_CUSTOM_IMPORT) :
        opstat      =   process_custom_import(parms,DIM.custom_import_id,display=True) 
        dispstats   =   True
        
    elif(functionid == DIM.CLEAR_CUSTOM_IMPORT) :
        cfg.drop_config_value(DIM.custom_import_id + "Parms")
        display_import_forms(DIM.IMPORT_CUSTOM_ONLY)
    

    return(dispstats, opstat)
    

def process_custom_import(parms,import_id,display=True) : 
    """
    * -------------------------------------------------------------------------- 
    * function : process custom import into pandas dataframe 
    * 
    * parms :
    *  fparms    -   associated import parms                      
    *  importId  -   associated import parms                      
    *  display   -   display flag                      
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    if(DIM.DEBUG_SQL_IMPORT) :   
        print("\nprocess_custom_import",parms) 
    
    opstat = opStatus() 
    
    if(len(parms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
        
    else :
        
        fparms      =   get_parms_for_input(parms,DIM.custom_import_idList)
        df_title    =   fparms[0]
        print("\nprocess_custom_import : fparms\n",fparms)
        
        if(len(df_title) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No df title defined")
            
        else :
            
            code    =   fparms[2]
            code    =   code.replace("\\","\\\\")
            
            try :
                exec(code)
            except Exception as e:
                opstat.store_exception("Unable to import custom" + fparms[1],e)

    if(opstat.get_status()) : 
        
        custom_full_parms  =   []
        custom_full_parms.append(code)
        
        custom_addl_parms   =   None
        
        try :
            DIM.ImportHistory.add_to_history(DIM.CUSTOM_IMPORT,df_title,custom_full_parms,custom_addl_parms)
        except Exception as e:
            opstat.store_exception("Unable to save import parms to history",e)

        cfg.set_config_value(cfg.CURRENT_IMPORT_DF,df_title)
        

        if(len(fparms) > 0) :
            cfg.set_config_value(import_id + "Parms","custom")
            cfg.set_config_value(cfg.CURRENT_IMPORTED_DATA_SOURCE_KEY,"custom",True)

    return(opstat)
   


