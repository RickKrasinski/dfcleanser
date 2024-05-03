"""
# DataExportControl
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:29:22 2017

@author: Rick
"""

import sys
this = sys.modules[__name__]


import inspect
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStackedWidget

from PyQt5.QtCore import QSize, Qt
from PyQt5 import uic


#import dfcleanser.common.cfg as cfg 

DEBUG_DATA_EXPORT               =   False
DEBUG_DATA_EXPORT_HISTORIES     =   False
DEBUG_DATA_EXPORT_FILE_TYPE     =   False
DEBUG_DATA_EXPORT_DETAILS       =   False
DEBUG_DATA_EXPORT_FORMS         =   False

DEBUG_DATA_EXPORT_CSV           =   False
DEBUG_DATA_EXPORT_EXCEL         =   False
DEBUG_DATA_EXPORT_JSON          =   False
DEBUG_DATA_EXPORT_HTML          =   False
DEBUG_DATA_EXPORT_SQLTABLE      =   False
DEBUG_DATA_EXPORT_CUSTOM        =   False


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


import dfcleanser.Qt.data_export.DataExportModel as DEM
from dfcleanser.common.common_utils import opStatus, get_parms_for_input


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                Data Import processing methods                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#



# -----------------------------------------------------------------#
# -                   Data Import format parms                    -#
# -----------------------------------------------------------------#

def process_export_form(formid, parms, parent) :
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
    
    if(DEBUG_DATA_EXPORT) :
        print("[process_export_form] formid : ",formid,"\n  ",parms)

    opstat  =   opStatus()   
    
    try :
        
        if( (formid == DEM.CSV_EXPORT)  or (formid == DEM.EXCEL_EXPORT) or 
            (formid == DEM.JSON_EXPORT) or (formid == DEM.HTML_EXPORT) or 
            (formid == DEM.XML_EXPORT)  or (formid == DEM.CUSTOM_EXPORT) )  :
    
            if (formid == DEM.CSV_EXPORT) :

                parmstitle  =   "Pandas CSV Export Parms"
                opstat      =   export_pandas_csv(parms)
                
                parmslist   =   DEM.pandas_export_csv_labelList[:6]
                parmslist.pop(1)
                parms.pop(1)

            elif (formid == DEM.EXCEL_EXPORT) :
                parmstitle  =   "Pandas Excel Export Parms"
                opstat      =   export_pandas_excel(parms)
                
                parmslist   =   DEM.pandas_export_excel_labelList[:7]
                parmslist.pop(1)
                parms.pop(1)
        
            elif (formid == DEM.JSON_EXPORT) : 
                parmstitle  =   "Pandas JSON Export Parms"
                opstat      =   export_pandas_json(parms)
                
                parmslist   =   DEM.pandas_export_json_labelList[:5]
                    
            elif (formid == DEM.XML_EXPORT) : 
                parmstitle  =   "Pandas XML Export Parms"
                opstat      =   export_pandas_xml(parms)
                
                parmslist   =   DEM.pandas_export_xml_labelList[:7]
 
            elif (formid == DEM.HTML_EXPORT) : 
                parmstitle  =   "Pandas HTML Export Parms"
                opstat      =   export_pandas_html(parms)
                
                parmslist   =   DEM.pandas_export_html_labelList[:6]

            elif (formid == DEM.CUSTOM_EXPORT) : 
                parmstitle  =   "Pandas Custom Export Parms"
                return_data      =   export_pandas_custom(parms)

                opstat              =   return_data[0]
                custom_file_path    =   return_data[1]
                
                parmslist   =   DEM.custom_export_labelList[:1]


        # -----------------------------------------------------#
        # -             SQL Import Functions                  -#
        # -----------------------------------------------------#
        
        elif (formid == DEM.SQLTABLE_EXPORT) : 
            opstat  =   export_sql_table(parms)
                
            # check if import was successful        
            if(opstat.get_status()) : 
                parent.display_export_status(formid, parms[1],parms[0] )
            else :
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception("dfcleanser Import","Export failed",opstat.get_exception())
        
        else :

            title       =   "dfcleanser error"
            status_msg  =   "[process_export_form] error : invalid form type"
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

    except Exception as e:

        title       =   "dfcleanser exception"
        status_msg  =   "[process_export_form] export error " + parmstitle
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,e)

    # check if import was successful        
    if(opstat.get_status()) : 

        if (formid == DEM.CUSTOM_EXPORT) : 
            parent.display_export_status(formid, custom_file_path, parms[0])
        else :
           parent.display_export_status(formid, parms[1],parms[0])

    else :

        if(opstat.get_exception() is None) :

            title       =   "dfcleanser exception : [build_export_from]"        
            status_msg  =   opstat.get_errorMsg()
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)
            opstat.set_status(False)


        else :

            title       =   "dfcleanser exception"        
            status_msg  =   "[process_export_form] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,opstat.get_exception())
            opstat.set_status(False)


    if(DEBUG_DATA_EXPORT) :
        print("[process_export_form] end : ",opstat.get_status())


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   process pandas export utility functions
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_export_addl_parms_dict(detid,addl_parms,opstat) :
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
    
    if(DEBUG_DATA_EXPORT_DETAILS) :
        print("[get_export_addl_parms_dict]",detid,"\n",addl_parms)
    
    try :
        
        if(len(addl_parms) > 0) :
            
            import json
    
            addl_parms_dict     =   json.loads(addl_parms)

            if(DEBUG_DATA_EXPORT_DETAILS) :
                print("[get_import_addl_parms_dict] addl_parms_dict : \n  ",addl_parms_dict)

            dkeys   =   list(addl_parms_dict.keys())
    
            for i in range(len(dkeys)) :
                
                new_dkey    =   dkeys[i].replace("'","")
                new_dkey    =   dkeys[i].replace('"',"")
                
                import  dfcleanser.Qt.data_export.DataExportModel as DEM
                new_dtype   =   DEM.get_export_addl_parm_dtype(detid,new_dkey)
                
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

        if(DEBUG_DATA_EXPORT_DETAILS) :
            print("[get_import_addl_parms_dict] exception  ")
            
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception("dfcleanser Export","Export failed",e)

        opstat.store_exception("Unable to parse adittional parms string." + addl_parms,e)

    if(opstat.get_status()) :
        return(addl_parms_dict)
    else :
        return(None)

def save_export_data(exportid,df_title,df,fparms,full_parms,addl_parms,methodTitle,file_path,exportFormId,opstat) :
    """
    * --------------------------------------------------------
    * function : save dtat for an export 
    * parms :
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    if(DEBUG_DATA_EXPORT):
        print("\n\n  [save_export_data] exportid ; dftitle : ",exportid,df_title)
        print("  [save_export_data] file_path : ",file_path)
        print("  [save_export_data] exportFormId : ",exportFormId)
        print("  [save_export_data] fparms : \n    ",fparms)
        print("  [save_export_data] full_parms : \n    ",full_parms)
        print("  [save_export_data] addl_parms : \n    ",addl_parms)

    try :

        import  dfcleanser.Qt.data_import.DataImportModel as DIM
        DIM.ExportHistory.add_to_history(exportid,file_path,fparms,addl_parms)#full_parms,addl_parms)

        if(DEBUG_DATA_EXPORT):
            print("  [save_export_data][" + methodTitle + "] Export History added : ",opstat.get_status())

    except Exception as e:
        opstat.store_exception("Unable to save export parms to history",e)
            
        title       =   "dfcleanser exception"       
        status_msg  =   "[" + methodTitle + "] error "
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,e)


    import dfcleanser.common.cfg as cfg

    if(opstat.get_status()) :
        
        if(len(fparms) > 0) :
            cfg.set_config_value(exportFormId + "Parms",fparms)
 
            if(DEBUG_DATA_EXPORT):#_DETAILS) :
                print("  [save_export_data][" + methodTitle + "] cfg parms stored : \n  ",cfg.get_config_value(exportFormId + "Parms"))

    if(DEBUG_DATA_EXPORT):
        print("  [save_export_data][" + methodTitle + "] end ")




# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                       Export Methods                          -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

import json
import pandas as pd

# -----------------------------------------------------------------#
# -                        Export CSV File                        -#
# -----------------------------------------------------------------#

def export_pandas_csv(fparms) : 
    
    if(DEBUG_DATA_EXPORT_CSV) :
        print("\n[export_pandas_csv]\n",fparms)
    
    opstat      =   opStatus()
    exportId    =   DEM.pandas_export_csv_id
    
    
    if(len(fparms) == 0) :
        
        opstat.set_status(False)
        opstat.set_errorMsg("No Export parameters defined")
        
    else :
        
        if(len(fparms[0]) == 0):
            
            opstat.set_status(False)
            opstat.set_errorMsg("No df_title defined")
            
        else :
            
            df_title    =   fparms[0]
            from dfcleanser.common.cfg import get_dfc_dataframe_df
            df  =   get_dfc_dataframe_df(df_title)
            
            if(len(fparms[1]) == 0):
                
                opstat.set_status(False)
                opstat.set_errorMsg("No file location defined")
                
            else :
                
                try :

                    if(DEBUG_DATA_EXPORT_CSV) :
                        print("[export_pandas_csv] df_title : ",df_title)
                
                    file_path   =   fparms[1]
                    file_path   =   file_path.replace("\\","/")
                    
                    pindex   =   3
                    if(len(fparms[pindex]) == 0):
                        csv_header   =   None
                    else :
                        if(fparms[pindex] == "False"):
                            csv_header   =   False
                        else :
                            csv_header   =   True
                                    
                    pindex   =   4
                    if(len(fparms[pindex]) == 0):
                        csv_index   =   None
                    else :
                        if(fparms[pindex] == "False"):
                            csv_index   =   False
                        else :
                            csv_index   =   True

                    pindex   =   5
                    csv_addl_parms  =   get_export_addl_parms_dict(DEM.CSV_EXPORT,fparms[5],opstat)

                    if(DEBUG_DATA_EXPORT_CSV) :
                        print("[export_pandas_csv] csv_addl_parms : ",csv_addl_parms)
                    
                except Exception as e:
                    opstat.store_exception("Invalid Import Parm " + DEM.pandas_export_csv_labelList[pindex] + " : " + fparms[pindex],e)

    if(opstat.get_status()) :
                    
        if(DEBUG_DATA_EXPORT_CSV) :
            print("[import_pandas_csv] parms loaded : ")

        #from dfcleanser.common.common_utils import RunningClock
        #from IPython.display import clear_output
        #clear_output()
        
        try :
            if(csv_addl_parms is None) :
                df.to_csv(file_path, header=csv_header, index=csv_index)
            else :
                df.to_csv(file_path, header=csv_header, index=csv_index, **csv_addl_parms)
        except Exception as e:
            opstat.store_exception("Unable to import csv file" + fparms[2],e)

            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception("dfcleanser Import","CSV Import failed",opstat.get_exception())

            
    if(opstat.get_status()) : 

        if(DEBUG_DATA_EXPORT_CSV) :
            print("[export_pandas_csv] csv exported : ")
        
        csv_full_parms  =   []
        csv_full_parms.append(df_title)
        if(csv_header) :
            csv_full_parms.append("True")
        else :
            csv_full_parms.append("False")
        if(csv_index) :
            csv_full_parms.append("True")
        else :
            csv_full_parms.append("False")
        # addl parms tag
        csv_full_parms.append("")

        save_export_data(DEM.CSV_EXPORT,df_title,df,fparms,csv_full_parms,csv_addl_parms,"export_pandas_csv",file_path,exportId,opstat) 


    return(opstat)



# -----------------------------------------------------------------#
# -                      Export EXCEL File                        -#
# -----------------------------------------------------------------#

def export_pandas_excel(fparms) : 

    import openpyxl
    
    if(DEBUG_DATA_EXPORT_EXCEL) :
        print("\n[export_pandas_excel]\n",fparms)

    exception_occurred  =   False
   
    opstat      =   opStatus()
    exportId    =   DEM.pandas_export_excel_id
    
    if(len(fparms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Export parameters defined")
    else :
        
        if(len(fparms[0]) == 0):
            opstat.set_status(False)
            opstat.set_errorMsg("No df_title defined")
        else :
            
            df_title    =   fparms[0]
            from dfcleanser.common.cfg import get_dfc_dataframe_df
            df  =   get_dfc_dataframe_df(df_title)
            
            if(len(fparms[1]) == 0):
                opstat.set_status(False)
                opstat.set_errorMsg("No excel_writer defined")
            else :
                
                try :

                    if(DEBUG_DATA_EXPORT_EXCEL) :
                        print("[export_pandas_excel] df_title : ",df_title)
                
                    excel_writer   =   fparms[1]
                    excel_writer   =   excel_writer.replace("\\","/")
                
                    pindex  =   3
                    if(len(fparms[pindex]) == 0):
                        excel_sheet   =   'Sheet1'
                    else :
                        excel_sheet   =   fparms[pindex]

                    pindex   =   4
                    if(len(fparms[pindex]) == 0):
                        excel_header   =   None
                    else :
                        if(fparms[pindex] == "False"):
                            excel_header   =   False
                        else :
                            excel_header   =   True
                                    
                    pindex   =   5
                    if(len(fparms[pindex]) == 0):
                        excel_index   =   None
                    else :
                        if(fparms[pindex] == "False"):
                            excel_index   =   False
                        else :
                            excel_index   =   True

                    excel_addl_parms  =   get_export_addl_parms_dict(DEM.EXCEL_EXPORT,fparms[6],opstat)
                    
                    if(DEBUG_DATA_EXPORT_EXCEL) :
                        print("[export_pandas_excel] excel_addl_parms : ",excel_addl_parms)
                
                except Exception as e:
                    opstat.store_exception("Invalid Wxport Parm " + DEM.pandas_export_excel_labelList[pindex] + " : " + fparms[pindex],e)
                    exception_occurred  =   True

    if(opstat.get_status()) :

        if(DEBUG_DATA_EXPORT_EXCEL) :
            print("[import_pandas_excel] parms loaded : ")

        #from dfcleanser.common.common_utils import RunningClock
        #from IPython.display import clear_output
        #clear_output()
        
        try :
            if(excel_addl_parms is None) :
                df.to_excel(excel_writer, sheet_name=excel_sheet, header=excel_header, index=excel_index)
            else :
                df.to_excel(excel_writer, sheet_name=excel_sheet, header=excel_header, index=excel_index, **excel_addl_parms)
        except Exception as e:

            title       =   "dfcleanser exception"        
            status_msg  =   "[export_pandas_excel] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)
            opstat.set_status(False)

        if(opstat.get_status()) : 

            if(DEBUG_DATA_EXPORT_EXCEL) :
                print("[export_pandas_excel] excel exported : ")
        
            excel_full_parms  =   []
            excel_full_parms.append(df_title)
            excel_full_parms.append(excel_writer)
            excel_full_parms.append(excel_sheet)
            if(excel_header) :
                excel_full_parms.append("True")
            else :
                excel_full_parms.append("False")
            if(excel_index) :
                excel_full_parms.append("True")
            else :
                excel_full_parms.append("False")
            # addl parms tag
            excel_full_parms.append("")

            save_export_data(DEM.EXCEL_EXPORT,df_title,df,fparms,excel_full_parms,excel_addl_parms,"import_pandas_excel",excel_writer,exportId,opstat) 

    if(not (opstat.get_status())) :

        title       =   "dfcleanser exception"       
        status_msg  =   "[export_pandas_excel] " + opstat.get_errorMsg()
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

    
    return(opstat)


# -----------------------------------------------------------------#
# -                       Export JSON File                        -#
# -----------------------------------------------------------------#
 
def export_pandas_json(fparms) : 
    
    if(DEBUG_DATA_EXPORT) :
        print("\n[import_pandas_json]\n",fparms)
    
    opstat      =   opStatus()
    exportId    =   DEM.pandas_export_json_id
    
    if(len(fparms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
    else :
        
        if(len(fparms[0]) == 0):
            opstat.set_status(False)
            opstat.set_errorMsg("No df_title defined")
        else :
            
            df_title    =   fparms[0]
            from dfcleanser.common.cfg import get_dfc_dataframe_df
            df  =   get_dfc_dataframe_df(df_title)
        
            if(len(fparms[1]) == 0):
                opstat.set_status(False)
                opstat.set_errorMsg("No file_path defined")
            else :
                
                try :

                    if(DEBUG_DATA_EXPORT) :
                        print("[import_pandas_json] df_title : ",df_title)
            
                    file_path   =   fparms[1]
                    file_path   =   file_path.replace("\\","/")
                
                    pindex  =   3
                    if(len(fparms[pindex]) == 0):
                        orient_parm   =   "'records'"
                    else :
                        orient_parm   =   fparms[pindex]

 
                    json_addl_parms  =   get_export_addl_parms_dict(DEM.JSON_EXPORT,fparms[4],opstat)
                    
                    if(DEBUG_DATA_EXPORT) :
                        print("[export_pandas_json] json_addl_parms : ",json_addl_parms)
                   
                except Exception as e:
                    opstat.store_exception("Invalid Import Parm " + DEM.pandas_export_json_labelList[pindex] + " : " + fparms[pindex],e)
            
    if(opstat.get_status()) :
        
        if(DEBUG_DATA_EXPORT) :
            print("[export_pandas_json] parms loaded : ")

        from dfcleanser.common.common_utils import RunningClock
        from IPython.display import clear_output
        clear_output()
        
        try :
            if(json_addl_parms is None) :
                df.to_json(file_path, orient=orient_parm)
            else :
                df.to_json(file_path, orient=orient_parm, **json_addl_parms)
        except Exception as e:
            opstat.store_exception("Unable to export json file" + fparms[2],e)

    if(opstat.get_status()) : 

        if(DEBUG_DATA_EXPORT) :
            print("[import_pandas_json] json imported : ")
        
        json_full_parms  =   []
        json_full_parms.append(df_title)
        json_full_parms.append(orient_parm)
        json_full_parms.append("")

        save_export_data(DEM.JSON_EXPORT,df_title,df,fparms,json_full_parms,json_addl_parms,"export_pandas_json",file_path,exportId,opstat) 


    return(opstat)

# -----------------------------------------------------------------#
# -                       Export JSON File                        -#
# -----------------------------------------------------------------#
 
def export_pandas_xml(fparms) : 
    
    if(DEBUG_DATA_EXPORT) :
        print("\n  [export_pandas_xml]\n",fparms)
    
    opstat      =   opStatus()
    exportId    =   DEM.pandas_export_json_id
    
    if(len(fparms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
    else :
        
        if(len(fparms[0]) == 0):
            opstat.set_status(False)
            opstat.set_errorMsg("No df_title defined")
        else :
            
            df_title    =   fparms[0]
            from dfcleanser.common.cfg import get_dfc_dataframe_df
            df  =   get_dfc_dataframe_df(df_title)
        
            if(len(fparms[1]) == 0):
                opstat.set_status(False)
                opstat.set_errorMsg("No file_path defined")
            else :
                
                try :

                    if(DEBUG_DATA_EXPORT) :
                        print("  [export_pandas_xml] df_title : ",df_title)
            
                    file_path   =   fparms[1]
                    file_path   =   file_path.replace("\\","/")
                
                    pindex  =   3
                    if(len(fparms[pindex]) == 0):
                        xindex   =   True
                    else :
                        if(fparms[pindex] == "True") :
                            xindex  =   True
                        else :
                            xindex  =   False

                    pindex  =   4
                    if(len(fparms[pindex]) == 0):
                        root_name   =   "data"
                    else :
                        root_name   =   fparms[pindex]

                    pindex  =   5
                    if(len(fparms[pindex]) == 0):
                        row_name   =   "row"
                    else :
                        row_name   =   fparms[pindex]

                    pindex  =   6
                    if(len(fparms[pindex]) == 0):
                        na_rep      =    None
                    else :
                        na_rep      =   fparms[pindex]

                    xml_addl_parms  =   get_export_addl_parms_dict(DEM.JSON_EXPORT,fparms[7],opstat)
                    
                    if(DEBUG_DATA_EXPORT) :
                        print("  [export_pandas_xml] xml_addl_parms : ",xml_addl_parms)
                   
                except Exception as e:
                    opstat.store_exception("Invalid Import Parm " + DEM.pandas_export_xml_labelList[pindex] + " : " + fparms[pindex],e)
            
    if(opstat.get_status()) :
        
        if(DEBUG_DATA_EXPORT) :
            print("  [export_pandas_xml] parms loaded : ")

        from dfcleanser.common.common_utils import RunningClock
        from IPython.display import clear_output
        clear_output()
        
        try :
            if(xml_addl_parms is None) :
                df.to_xml(file_path, index=xindex, root_name=root_name, row_name=row_name,na_rep=na_rep)
            else :
                df.to_xml(file_path, index=xindex, root_name=root_name, row_name=row_name,na_rep=na_rep, **xml_addl_parms)
        except Exception as e:

            title       =   "dfcleanser exception"       
            status_msg  =   "[export_pandas_xml] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.store_exception("Unable to export xml file" + fparms[2],e)

    if(opstat.get_status()) : 

        if(DEBUG_DATA_EXPORT) :
            print("[export_pandas_xml] xml exported : ")
        
        xml_full_parms  =   []
        xml_full_parms.append(df_title)
        xml_full_parms.append(xindex)
        xml_full_parms.append(root_name)
        xml_full_parms.append(row_name)
        xml_full_parms.append(na_rep)
        xml_full_parms.append("")

        save_export_data(DEM.XML_EXPORT,df_title,df,fparms,xml_full_parms,xml_addl_parms,"export_pandas_xml",file_path,exportId,opstat) 


    return(opstat)



# -----------------------------------------------------------------#
# -                      Export HTML page                         -#
# -----------------------------------------------------------------#
   
def export_pandas_html(fparms,opstat) : 

    if(DEBUG_DATA_EXPORT) :
        print("[export_pandas_html] : \n",fparms)   


    opstat      =   opStatus()
    exportId    =   DEM.pandas_export_json_id
    
    if(len(fparms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
    else :
        
        if(len(fparms[0]) == 0):
            opstat.set_status(False)
            opstat.set_errorMsg("No df_title defined")
        else :
            
            df_title    =   fparms[0]
            from dfcleanser.common.cfg import get_dfc_dataframe_df
            df  =   get_dfc_dataframe_df(df_title)
        
            if(len(fparms[1]) == 0):

                opstat.set_status(False)
                opstat.set_errorMsg("No file_path defined")

            else :
                
                try :

                    if(DEBUG_DATA_EXPORT) :
                        print("[import_pandas_json] df_title : ",df_title)
            
                    io   =   fparms[1]
                    io   =   io.replace("\\","/")
                
                    pindex  =   3
                    if(len(fparms[pindex]) == 0):
                        html_header   =   None
                    else :
                        if(fparms[pindex] == "False"):
                            html_header   =   False
                        else :
                            html_header   =   True
                                    
                    pindex   =   4
                    if(len(fparms[pindex]) == 0):
                        html_index   =   None
                    else :
                        if(fparms[pindex] == "False"):
                            html_index   =   False
                        else :
                            html_index   =   True
 
                    html_addl_parms  =   get_export_addl_parms_dict(DEM.HTML_EXPORT,fparms[5],opstat)
                    
                    if(DEBUG_DATA_EXPORT) :
                        print("[export_pandas_html] json_addl_parms : ",html_addl_parms)
                   
                except Exception as e:
                    opstat.store_exception("Invalid Import Parm " + DEM.pandas_export_json_labelList[pindex] + " : " + fparms[pindex],e)

    
    if(opstat.get_status()) : 

        from dfcleanser.common.common_utils import RunningClock
        from IPython.display import clear_output
        clear_output()

        try :
            if(html_addl_parms is None) :
                df.to_html(io, header=html_header, index=html_index)
            else :
                df.to_html(io, header=html_header, index=html_index, **html_addl_parms)
        except Exception as e:
            opstat.store_exception("Unable to export html file" + fparms[2],e)
            
    if(opstat.get_status()) : 

        if(DEBUG_DATA_EXPORT) :
            print("[import_pandas_json] json imported : ")
        
        html_full_parms  =   []
        html_full_parms.append(df_title)
        if(html_header) :
            html_full_parms.append("True")
        else :
            html_full_parms.append("False")
        if(html_index) :
            html_full_parms.append("True")
        else :
            html_full_parms.append("False")
        # addl parms tag
        html_full_parms.append("")

        save_export_data(DEM.HTML_EXPORT,df_title,df,fparms,html_full_parms,html_addl_parms,"export_pandas_html",io,exportId,opstat) 
    
    
    return(opstat)


# -----------------------------------------------------------------#
# -                        Export Custom                          -#
# -----------------------------------------------------------------#

def export_pandas_custom(fparms) : 

    if(DEBUG_DATA_EXPORT) :
        print("[export_pandas_custom] : \n",fparms)   
    
    opstat = opStatus() 
    exportId    =   DEM.custom_export_id 

    if(len(fparms) == 0) :
        opstat.set_status(False)
        opstat.set_errorMsg("No Import parameters defined")
        
    else :
        
        df_title    =   fparms[0]
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        df  =   get_dfc_dataframe_df(df_title)
      
        if(len(df_title) == 0) :
            opstat.set_status(False)
            opstat.set_errorMsg("No df title defined")
            
        else :

            if(len(fparms[1]) == 0):

                opstat.set_status(False)
                opstat.set_errorMsg("No custom code defined")

            else :

                from dfcleanser.common.common_utils import RunningClock
                from IPython.display import clear_output
                clear_output()
           
                code    =   fparms[1]
                code    =   code.replace("\\","\\\\")
            
                try :
                    exec(code)
                except Exception as e:
                    opstat.store_exception("Unable to import custom" + fparms[1],e)

    if(opstat.get_status()) : 
        
        if(DEBUG_DATA_EXPORT) :
            print("[import_pandas_custom] custom exported : ")
        
        custom_full_parms  =   []
        custom_full_parms.append(df_title)
        custom_full_parms.append(code)

        from dfcleanser.Qt.data_import.DataImportModel import ExportHistory
        df_titles   =   ExportHistory.get_df_titles_for_file_type(DEM.CUSTOM_EXPORT)

        if(not (df_titles is None)) :
            file_type_totals    =   len(df_titles)
        else :
            file_type_totals    =   0

        file_path   =   "Custom_file_path_" + str(file_type_totals)

        save_export_data(DEM.CUSTOM_EXPORT,df_title,df,fparms,custom_full_parms,None,"export_pandas_custom",file_path,exportId,opstat) 
    

    return([opstat,file_path])



# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                    SQL Export functions                       -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

def export_sql_table(fparms) :
                
    if(DEBUG_DATA_EXPORT) :
        print("  [export_sql_table] : \n    ",fparms)
    
    opstat      =   opStatus()
    exportId    =   DEM.pandas_export_sqltable_id 

    from dfcleanser.sw_utilities.db_utils import dfc_dbconnectors_table, EXPORT_FLAG
    current_selected_connector  =   dfc_dbconnectors_table.get_current_dbconnector(EXPORT_FLAG)

    if(DEBUG_DATA_EXPORT) :
        print("  [export_sql_table] : dbconnector : ] ",type(current_selected_connector))
        current_selected_connector.dump()

    if(len(fparms) == 0) :
        
        opstat.set_status(False)
        opstat.set_errorMsg("No Export parameters defined")
        
    else :
        
        if(len(fparms[0]) == 0):
            
            opstat.set_status(False)
            opstat.set_errorMsg("No 'df_title' defined")
            
        else :
            
            df_title    =   fparms[0]
            from dfcleanser.common.cfg import get_dfc_dataframe_df
            df  =   get_dfc_dataframe_df(df_title)
            
            try :
                
                pindex  =   1
                if( (fparms[pindex] is None) or (len(fparms[pindex]) == 0) ):
                    opstat.set_errorMsg("No 'table' defined")
                    opstat.set_status(False)
                else :
                    table_name   =   fparms[pindex]

                if(opstat.get_status()) :

                    pindex  =   2
                    if(len(fparms[pindex]) == 0):
                        schema   =   ""
                    else :
                        schema   =   fparms[pindex]
                
                    pindex  =   3    
                    if(len(fparms[pindex]) == 0):
                        if_exists   =   "fail"
                    else :
                        if_exists   =   fparms[pindex]

                    pindex  =   4
                    if(len(fparms[pindex]) == 0):
                        index   =   True
                    else :
                        if(fparms[pindex] == "True") :
                            index  =   True
                        else :
                            index  =   False

                    pindex  =   5    
                    if(len(fparms[pindex]) == 0):
                        index_label   =   None
                    else :
                        index_label   =   fparms[pindex]      

                    pindex  =   6    
                    if(len(fparms[pindex]) == 0):
                        chunksize   =   None
                    else :

                        try :
                            chunksize   =   int(fparms[pindex])  
                        except :
                            opstat.set_errorMsg("chunksize parm invalid format")
                            opstat.set_status(False)
                            chunksize     =   "Invalid"
                           
                    if(opstat.get_status()) :

                        print("pindex = 7")
                            
                        pindex  =   7
                        if(len(fparms[pindex]) == 0):
                            dtype   =   None
                        else :
                            dtype   =   fparms[pindex]

                        pindex  =   8    

                        print("fuck you")
                        if(len(fparms[pindex]) == 0):
                            sqlmethod   =   None
                        else :
                            if(fparms[pindex] == "None") :
                                sqlmethod  =   None
                            else :
                                sqlmethod  =   fparms[pindex]

                        print(sqlmethod)
                    
            except Exception as e:

                title       =   "dfcleanser exception"       
                status_msg  =   "[export_sql_table] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)
    
        if(DEBUG_DATA_EXPORT) :
            print("  [export_sql_table] : after parse parms : ] ",opstat.get_status())

        if(not(opstat.get_status())) :

            title       =   "dfcleanser error"
            status_msg  =   "[export_sql_table] error : " + opstat.get_errorMsg()
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg)

        else :

            import dfcleanser.sw_utilities.db_utils as dbu
            dbconDict   =   dbu.get_current_dbcondict(1)
        
            if(DEBUG_DATA_EXPORT) :
                print("  [export_sql_table] : dbconDict : \n  ",dbconDict)

            dbcon = dbu.dbConnector()
            dbcon.connect_to_db(dbu.SQLALCHEMY,opstat,dbconDict)

            #SQL_Server_ID   =  int(dbconDict.get("servertype")) 

            if(opstat.get_status()) :

                from dfcleanser.common.common_utils import RunningClock
                from IPython.display import clear_output
                clear_output()

                try :

                    dbconnector     =   dbcon.get_dbConnection()

                    df.to_sql(table_name, dbconnector, schema=schema,if_exists=if_exists, index=index, 
                              index_label=index_label, chunksize=chunksize,method=sqlmethod) 
                
                except Exception as e:

                    title       =   "dfcleanser exception"       
                    status_msg  =   "[export_sql_table] to_sql_table : error "
                    from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                    display_exception(title,status_msg,e)
                    opstat.set_status(False)
                
                if(opstat.get_status()) :

                    from PyQt5.QtWidgets import QMessageBox
                    dlg = QMessageBox()
                    dlg.setTextFormat(Qt.RichText)
                    dlg.setWindowTitle("Save Export To History")
                    dlg.setText("Save the current sql export to the export history log")
                    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                    dlg.setStyleSheet("QLabel{min-width: 350px;}")
            
                    button = dlg.exec()

                    if(button == QMessageBox.Yes) :


                        if(DEBUG_DATA_EXPORT) :
                            print("[export_pandas_sqltble] sqltable exported : ")
        
                        sql_full_parms  =   []
                        sql_full_parms.append(df_title)
                        sql_full_parms.append(table_name)
                        sql_full_parms.append(schema)
                        sql_full_parms.append(if_exists)
                        
                        if(index) :
                            sql_full_parms.append("True")
                        else :
                            sql_full_parms.append("False")

                        sql_full_parms.append(index_label)
                        sql_full_parms.append(str(chunksize))
                        sql_full_parms.append(str(dtype))
                        sql_full_parms.append(str(sqlmethod))

                        # addl parms tag
                        #sql_full_parms.append("")

                        save_export_data(DEM.SQLTABLE_EXPORT,df_title,df,fparms,sql_full_parms,None,"export_pandas_sqltable",table_name,exportId,opstat) 
    
             
    return(opstat)    


"""
* -------------------------------------------------------------------------- 
* --------------------------------------------------------------------------
*                         Export functions 
* -------------------------------------------------------------------------- 
* --------------------------------------------------------------------------
"""


