"""
# DataTransformDataframeWidgets
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:29:22 2017

@author: Rick
"""

import sys
this = sys.modules[__name__]


# -----------------------------------------------------------------# 
# -----------------------------------------------------------------# 
# -         Data Transform Dataframes Column Names Row            -#
# -----------------------------------------------------------------# 
# -----------------------------------------------------------------#

def save_df_column_names_row(dftitle,filename):
    """
    * -------------------------------------------------------
    * function : save column names row to a file
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    from dfcleanser.common.common_utils import opStatus
    opstat      =   opStatus()

    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)

    if(df is None) :

        title       =   "dfcleanser exception"       
        status_msg  =   "[save_column_names_row] invalid df '" + dftitle + "' selected "
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        opstat.set_status(False)

    else :

        df_col_names    =   df.columns.tolist()
            
        if(len(filename) == 0) :
                
            from dfcleanser.common.cfg import DataframeCleansercfg
            import os
            nbdir       =   DataframeCleansercfg.get_notebookpath()
            nbname      =   DataframeCleansercfg.get_notebookname()
            file_path   =   os.path.join(nbdir,nbname + "_files")
            filename    =   os.path.join(file_path,dftitle + "_column_names.json")

        try :

            import json
                
            # write the column names row file
            with open(filename, 'w') as colid_file :
                json.dump(df_col_names,colid_file)
                colid_file.close()

            title       =   "dfcleanser status : [save_column_names_row]"        
            status_msg  =   "column names saved successfully"
            from dfcleanser.sw_utilities.dfc_qt_model import display_status_msg
            display_status_msg(title,status_msg)
            
        except Exception as e:

            title       =   "dfcleanser exception"       
            status_msg  =   "[save_column_names_row] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)

    return(opstat)


def add_column_names_row(dftitle,filename,colnames):
    """
    * ---------------------------------------------------------
    * function : add a column names row
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    from dfcleanser.common.common_utils import opStatus
    opstat = opStatus() 

    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)

    if(df is None) :

        title       =   "dfcleanser exception"       
        status_msg  =   "[add_column_names_row] invalid df '" + dftitle + "' selected "
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        opstat.set_status(False)

    else :

        if( (len(filename) == 0) and (len(colnames) == 0) ) :
                
            from dfcleanser.common.cfg import DataframeCleansercfg
            import os
            nbdir       =   DataframeCleansercfg.get_notebookpath()
            nbname      =   DataframeCleansercfg.get_notebookname()
            file_path   =   os.path.join(nbdir,nbname + "_files")
            filename    =   os.path.join(file_path,dftitle + "_column_names.json")

            try :

                import json

                # read the column names row file
                with open(filename, 'r') as colid_file :
                    new_col_names   =   json.load(colid_file)
                    colid_file.close()

                rename_names = new_col_names.strip('][').split(',')

            
            except Exception as e:

                title       =   "dfcleanser exception"       
                status_msg  =   "[add_column_names_row] error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

                opstat.set_status(False)

        else :

            if(len(filename) > 0) :

                try :

                    import json

                    # read the column names row file
                    with open(filename, 'r') as colid_file :
                        new_col_names   =   json.load(colid_file)
                        colid_file.close()

                    rename_names = new_col_names.strip('][').split(',')  

                except Exception as e:

                    title       =   "dfcleanser exception"       
                    status_msg  =   "[add_column_names_row] error "
                    from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                    display_exception(title,status_msg,e)

                    opstat.set_status(False)


            else :

                try :

                    import json 
                
                    rename_names   =   json.loads(colnames)

                except Exception as e:

                    title       =   "dfcleanser exception"       
                    status_msg  =   "[add_column_names_row] error "
                    from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                    display_exception(title,status_msg,e)

                    opstat.set_status(False)
                   
    if(opstat.get_status()) :

        df_col_names    =   df.columns.tolist()
        
        try : 
            
            namesdict = {}
            for i in range(len(df_col_names)) :
                namesdict.update({df_col_names[i]:rename_names[i]})
            
            df.rename(columns=namesdict,inplace=True)

            from dfcleanser.common.cfg import set_dfc_dtaframe_df
            set_dfc_dtaframe_df(dftitle,df)

        except Exception as e:

            title       =   "dfcleanser exception"       
            status_msg  =   "[add_column_names_row] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)
            
    return(opstat)


def drop_column_names_row(dftitle):
    """
    * -------------------------------------------------------- 
    * function : drop the column names row
    * 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    from dfcleanser.common.common_utils import opStatus
    opstat      =   opStatus()

    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)

    if(df is None) :

        title       =   "dfcleanser exception"       
        status_msg  =   "[display_transform_columns] invalid df '" + dftitle + "' selected "
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        opstat.set_status(False)

    else :
    
        try :

            #df.drop(labels=None,axis=0,index=-1,inplace=True)
        
            collist     =   df.columns.tolist()
        
            for i in range(len(collist)) :
                df.rename(columns={collist[i]:"Column "+str(i)},inplace=True)

        except Exception as e:

            title       =   "dfcleanser exception"       
            status_msg  =   "[drop_column_names_row] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)
        
    return(opstat)

# -----------------------------------------------------------------# 
# -----------------------------------------------------------------# 
# -        Data Transform Dataframes Column Names Row end         -#
# -----------------------------------------------------------------# 
# -----------------------------------------------------------------#


# -----------------------------------------------------------------# 
# -----------------------------------------------------------------# 
# -                Data Transform Dataframes Index                -#
# -----------------------------------------------------------------# 
# -----------------------------------------------------------------#

def set_df_index(dftitle,index_columns,dropflag,verifyflag):
    """
    * ---------------------------------------------------------
    * function : set df indices
    * 
    * parms :
    *   parms     -   transform parms
    *   display   -   display flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """

    from dfcleanser.common.common_utils import opStatus
    opstat = opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)

    if(len(index_columns) == 0) :

        title       =   "dfcleanser error"       
        status_msg  =   "[set_df_index] no index columns "
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg,e)

        opstat.set_status(False)

    else :

        try :

            import json 
            index_cols  =   json.loads(index_columns)

        except Exception as e:

            title       =   "dfcleanser exception"       
            status_msg  =   "[set_df_index] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)

    if(opstat.get_status()) :
        
        if(dropflag == "True") :
            drop = True
        else :
            drop = False
            
        if(verifyflag == "True") :
            verify = True
        else :
            verify = False
                
        try : 
            
            df.set_index(index_cols,drop=drop,append=True,inplace=True,verify_integrity=verify)

            from dfcleanser.common.cfg import set_dfc_dataframe_df
            set_dfc_dataframe_df(dftitle,df)
        
        except Exception as e:
           
            title       =   "dfcleanser exception"       
            status_msg  =   "[set_df_index] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)

    return(opstat)


def reset_df_index(dftitle,columns_to_drop,drop_levels,reinsert_flag):
    """
    * -------------------------------------------------------------------------- 
    * function : reset df indices
    * 
    * parms :
    *   parms     -   transform parms
    *   display   -   display flag
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    from dfcleanser.common.common_utils import opStatus
    opstat = opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)
    
    if(len(columns_to_drop) == 0) :

        title       =   "dfcleanser error"       
        status_msg  =   "[reset_df_index] no index columns "
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg,e)

        opstat.set_status(False)

    else :

        try :

            import json 
            drop_cols  =   json.loads(columns_to_drop)

        except Exception as e:

            title       =   "dfcleanser exception"       
            status_msg  =   "[reset_df_index] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)

    if(opstat.get_status()) :
        
        if(reinsert_flag == "True") :
            reinsert = True
        else :
            reinsert = False
                
        try : 

            if(drop_levels[0] == "All") :
                df.reset_index(None,inplace=True)    
            else :
                df.reset_index(level=drop_levels,drop=drop_cols,inplace=True)

            from dfcleanser.common.cfg import set_dfc_dataframe_df
            set_dfc_dataframe_df(dftitle,df)
        
        except Exception as e:
           
            title       =   "dfcleanser exception"       
            status_msg  =   "[set_df_index] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)

    return(opstat)

def append_to_df_index(dftitle,columns_to_append,drop_flag,verify_flag):
    """
    * --------------------------------------------
    * function : append column to df indices
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * -------------------------------------------
    """
    
    from dfcleanser.common.common_utils import opStatus
    opstat = opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)
    
    if(len(columns_to_drop) == 0) :

        title       =   "dfcleanser error"       
        status_msg  =   "[append_df_index] no index columns "
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg,e)

        opstat.set_status(False)

    else :

        try :

            import json 
            append_cols  =   json.loads(columns_to_append)

        except Exception as e:

            title       =   "dfcleanser exception"       
            status_msg  =   "[reset_df_index] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)
        
    if(opstat.get_status()) :

        
        if(drop_flag == "True") :
            drop = True
        else :
            drop = False
            
        if(verify_flag == "True") :
            verify = True
        else :
            verify = False
        
        try : 

            df.set_index(keys=columns_to_append,drop=drop,append=True,inplace=True,verify_integrity=verify)
            
            from dfcleanser.common.cfg import set_dfc_dataframe_df
            set_dfc_dataframe_df(dftitle,df)
        
        except Exception as e:
           
            title       =   "dfcleanser exception"       
            status_msg  =   "[set_df_index] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)
            
    return(opstat)


def sort_df_index(dftitle,ascending_flag,sort_kind,na_position):
    """
    * ------------------------------------
    * function : sort df indices
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * ------------------------------------
    """
    
    from dfcleanser.common.common_utils import opStatus
    opstat = opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)
    
    if(ascending_flag == "True") :
        ascending = True
    else :
        ascending = False

    try : 

        df.sort_index(axis=0,level="all",ascending=ascending,inplace=True,kind=sort_kind,na_position=na_position)
            
        from dfcleanser.common.cfg import set_dfc_dataframe_df
        set_dfc_dataframe_df(dftitle,df)
        
    except Exception as e:
           
        title       =   "dfcleanser exception"       
        status_msg  =   "[sort_df_index] error "
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,e)

        opstat.set_status(False)
                
    return(opstat)
   
# -----------------------------------------------------------------# 
# -----------------------------------------------------------------# 
# -               Data Transform Dataframes Index end             -#
# -----------------------------------------------------------------# 
# -----------------------------------------------------------------#


# -----------------------------------------------------------------# 
# -----------------------------------------------------------------# 
# -        Data Transform Dataframes Sort df by Column            -#
# -----------------------------------------------------------------# 
# -----------------------------------------------------------------#

def sort_df_column(dftitle,sort_column,ascending_flag,sort_kind,na_position):
    """
    * ------------------------------------
    * function : sort df indices
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * ------------------------------------
    """
    
    from dfcleanser.common.common_utils import opStatus
    opstat = opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)
    
    if(len(sort_column) == 0) :

        title       =   "dfcleanser error"       
        status_msg  =   "[append_df_index] no sort column "
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg,e)

        opstat.set_status(False)

    if(opstat.get_status()) :

        if(ascending_flag == "True") :
            ascending = True
        else :
            ascending = False

        try : 

            df.sort_values(axis=1,ascending=ascending,inplace=True,kind=sort_kind,na_position=na_position)
            
            from dfcleanser.common.cfg import set_dfc_dataframe_df
            set_dfc_dataframe_df(dftitle,df)
        
        except Exception as e:
           
            title       =   "dfcleanser exception"       
            status_msg  =   "[sort_df_column] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)
                
    return(opstat)

# -----------------------------------------------------------------# 
# -----------------------------------------------------------------# 
# -       Data Transform Dataframes Sort df by Column end         -#
# -----------------------------------------------------------------# 
# -----------------------------------------------------------------#

# -----------------------------------------------------------------# 
# -----------------------------------------------------------------# 
# -               Data Transform Datetime Utilities               -#
# -----------------------------------------------------------------# 
# -----------------------------------------------------------------#


def process_datetime_datatype_transform(dftitle,column_to_convert,NA_Threshold,error_method,format_string) :
    """
    * ---------------------------------------------------
    * function : convert column to datetime datatype
    * 
    * parms :
    *   parms     -   change parms
    *
    * returns : 
    *  N/A
    * ---------------------------------------------------
    """
    
    from dfcleanser.common.common_utils import opStatus
    opstat = opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)
    
    if(len(column_to_convert) == 0) :

        title       =   "dfcleanser error"       
        status_msg  =   "[process_datetime_datatype_transform] no convert column "
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg)

        opstat.set_status(False)

    if(opstat.get_status()) :
    
        if(len(NA_Threshold) == 0) :
            natthresh   =   None
        else :
            try :
                natthresh   =   float(natthresh)    
            except :

                title       =   "dfcleanser exception"       
                status_msg  =   "[process_datetime_datatype_transform] invalid NA Threshold "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

            opstat.set_status(False)
            
    if(opstat.get_status()) :
        
        from dfcleanser.Qt.data_transform.DataTransformDataframeModel import error_handlers

        cerrors     =   error_method
    
        if(cerrors.find(error_handlers[0]) > -1)    :  cerrors     =   error_handlers[0]
        elif(cerrors.find(error_handlers[1]) > -1)  :  cerrors     =   error_handlers[1]
        elif(cerrors.find(error_handlers[2]) > -1)  :  cerrors     =   error_handlers[2]
        else                                        :  cerrors     =   error_handlers[1]                                            
      
        import pandas as pd

        format_string     =   format_string.strip(" ")
        format_string     =   format_string.rstrip(" ") 
    
        try :
            
            if(not (natthresh is None)) :
        
                tdf_data    =   df[column_to_convert]
                tdf_dtype   =   df[column_to_convert].dtype
        
                tempdf      =   pd.DataFrame(data=tdf_data, dtype=tdf_dtype, columns = [column_to_convert])
        
                if(len(format_string) > 0) :
                    tempdf[column_to_convert] = pd.to_datetime(tempdf[column_to_convert], errors=cerrors, format=format_string)
                else :
                    tempdf[column_to_convert] = pd.to_datetime(tempdf[column_to_convert], errors=cerrors)
                
                total_nats  =   tempdf[column_to_convert].isnull().sum()
                
                if( (total_nats/len(tempdf)) < (natthresh * 0.01) ) :
                    df[column_to_convert]     =   tempdf[column_to_convert]
                    opstat.set_errorMsg("Column '" + column_to_convert +"' data type converted successfully to datetime64.")
                else :
                    df_nats     =   float("{0:.2f}".format((total_nats/len(tempdf)*100)))
                    opstat.set_errorMsg("Column '" + column_to_convert +"' data type not converted. " + "Convert NaTs " + str(df_nats) + "% exceeds threshold of " + str(natthresh) + "%.")
                    
            else :
                
                if(len(format_string) > 0) :
                    df[column_to_convert] = pd.to_datetime(df[column_to_convert], errors=cerrors, format=format_string)
                else :
                    df[column_to_convert] = pd.to_datetime(df[column_to_convert], errors=cerrors)
                    
            from dfcleanser.common.cfg import set_dfc_dataframe_df
            set_dfc_dataframe_df(dftitle,df)
            
        except Exception as e:

            title       =   "dfcleanser exception"       
            status_msg  =   "[process_datetime_datatype_transform] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)
         
    return(opstat)
    
    
def process_timedelta_datatype_transform(dftitle,column_to_convert,threshold,units,error_method) :
    """
    * -------------------------------------------------------------------------- 
    * function : convert column to datetime datatype
    * 
    * parms :
    *   parms     -   change parms
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    from dfcleanser.common.common_utils import opStatus
    opstat = opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)
    
    if(len(column_to_convert) == 0) :

        title       =   "dfcleanser error"       
        status_msg  =   "[process_timedelta_datatype_transform] no convert column "
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg,e)

        opstat.set_status(False)

    if(opstat.get_status()) :
    
        if(len(threshold) == 0) :
            natthresh   =   None
        else :
            try :
                natthresh   =   float(threshold)    
            except :

                title       =   "dfcleanser exception"       
                status_msg  =   "[process_timedelta_datatype_transform] invalid NA Threshold "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,e)

                opstat.set_status(False)

    if(opstat.get_status()) :
        
        from dfcleanser.Qt.data_transform.DataTransformDataframeModel import error_handlers

        cerrors     =   error_method
    
        if(cerrors.find(error_handlers[0]) > -1)    :  cerrors     =   error_handlers[0]
        elif(cerrors.find(error_handlers[1]) > -1)  :  cerrors     =   error_handlers[1]
        elif(cerrors.find(error_handlers[2]) > -1)  :  cerrors     =   error_handlers[2]
        else                                        :  cerrors     =   error_handlers[1]                                            
      
        import pandas as pd

        try :

            if(not (natthresh is None)) :
        
                tdf_data    =   df[column_to_convert]
                tdf_dtype   =   df[column_to_convert].dtype
        
                tempdf      =   pd.DataFrame(data=tdf_data, dtype=tdf_dtype, columns = [column_to_convert])
        
                tempdf[column_to_convert] = pd.to_timedelta(tempdf[column_to_convert], unit=units, errors=cerrors) 
                
                total_nats  =   tempdf[column_to_convert].isnull().sum()
                
                if( (total_nats/len(tempdf)) > (natthresh * 0.01) ) :
                
                    title       =   "dfcleanser error"       
                    status_msg  =   "[process_timedelta_datatype_transform] exceeded Threshold "
                    from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                    display_error_msg(title,status_msg)

                    opstat.set_status(False)

                else :
                    
                    df[column_to_convert]     =   tempdf[column_to_convert]   
        
            else :
        
                df[column_to_convert] = pd.to_timedelta(df[column_to_convert], unit=units, errors=cerrors)

            from dfcleanser.common.cfg import set_dfc_dataframe_df
            set_dfc_dataframe_df(dftitle,df)

                    
        except Exception as e:

            title       =   "dfcleanser exception"       
            status_msg  =   "[process_timedelta_datatype_transform] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)

    return(opstat)
    

def process_calculate_timedelta_transform(dftitle,column1_name,column2_name,new_column_name,new_col_datatype,new_column_units) :
    """
    * -----------------------------------------------
    * function : get datetime delta from columns
    * 
    * parms :
    *   parms     -   change parms
    *
    * returns : 
    *  N/A
    * -----------------------------------------------
    """
    
    from dfcleanser.common.common_utils import opStatus
    opstat = opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)
    
    if(len(column1_name) == 0) :

        title       =   "dfcleanser error"       
        status_msg  =   "[process_timedelta_datatype_transform] no column 1 "
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg,e)

        opstat.set_status(False)

    if(opstat.get_status()) :

        if(len(column2_name) == 0) :

            title       =   "dfcleanser error"       
            status_msg  =   "[process_timedelta_datatype_transform] no column 2 "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg,e)

            opstat.set_status(False)

    if(opstat.get_status()) :

        if(len(new_column_name) == 0) :

            title       =   "dfcleanser error"       
            status_msg  =   "[process_timedelta_datatype_transform] no new column "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg,e)

            opstat.set_status(False)

    if(opstat.get_status()) :

        import pandas as pd

        try :

            timedeltacol = df[column1_name] - df[column2_name]

            if(new_column_units == "Seconds")              :   timedeltacol = timedeltacol.apply(lambda x: x.total_seconds())
            elif(new_column_units == "MilliSeconds")       :   timedeltacol = timedeltacol.apply(lambda x: x.total_seconds() * 1000)
            elif(new_column_units == "MicroSeconds")       :   timedeltacol = timedeltacol.apply(lambda x: x.total_seconds() * 1000 * 1000)
            elif(new_column_units == "Minutes")            :   timedeltacol = timedeltacol.apply(lambda x: x.total_seconds() / 60)
            elif(new_column_units == "Hours")              :   timedeltacol = timedeltacol.apply(lambda x: x.total_seconds() / 3600)
            elif(new_column_units == "Days")               :   timedeltacol = timedeltacol.apply(lambda x: x.total_seconds() / (3600*24))

            from dfcleanser.sw_utilities.GenericFunctionsModel import add_column_to_df   
            df  =   add_column_to_df(df,new_col_datatype,timedeltacol,opstat)

            from dfcleanser.common.cfg import set_dfc_dataframe_df
            set_dfc_dataframe_df(dftitle,df)
                    
        except Exception as e:

            title       =   "dfcleanser exception"       
            status_msg  =   "[process_timedelta_datatype_transform] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)
            
    return(opstat)
        

def process_datetime_merge_split_transform(dftitle,action,column1,column2,column3,threshold,errorrtn,new_datatype=None) :
    """
    * -------------------------------------------------------
    * function : merge or split a datetime column
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
      
    import datetime

    from dfcleanser.common.common_utils import opStatus
    opstat = opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)
    
    if(len(column1) == 0) :

        title       =   "dfcleanser error"       
        status_msg  =   "[process_datetime_merge_split_transform] no column 1 "
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg,e)

        opstat.set_status(False)

    if(opstat.get_status()) :

        if(len(column2) == 0) :

            title       =   "dfcleanser error"       
            status_msg  =   "[process_datetime_merge_split_transform] no column 2 "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg,e)

            opstat.set_status(False)

    if(opstat.get_status()) :

        if(len(column3) == 0) :

            title       =   "dfcleanser error"       
            status_msg  =   "[process_datetime_merge_split_transform] no new column "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg,e)

            opstat.set_status(False)

    if(opstat.get_status()) :
    
        from dfcleanser.Qt.data_transform.DataTransformDataframeModel import SPLIT
        if(action == SPLIT) :

            print("split removed")
        

        else :
    
            datecolumn      =   column1
            timecolumn      =   column2
            datetimecolumn  =   column3
            coldtype        =   new_datatype
        
            from dfcleanser.common.common_utils import is_existing_column
            if(is_existing_column(df,datetimecolumn)) :

                title       =   "dfcleanser error"       
                status_msg  =   "process_datetime_merge_split_transform] datetime column exists"
                from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                display_error_msg(title,status_msg,e)

                opstat.set_status(False)

                if(opstat.get_status()) :
                    
                    from dfcleanser.common.common_utils import is_existing_column
                    if(not (is_existing_column(df,datecolumn))) :

                        title       =   "dfcleanser error"       
                        status_msg  =   "process_datetime_merge_split_transform] date column does not exist"
                        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                        display_error_msg(title,status_msg,e)

                        opstat.set_status(False)

                        if(opstat.get_status()) :                        

                            if(not (is_existing_column(df,timecolumn))) :

                                title       =   "dfcleanser error"       
                                status_msg  =   "process_datetime_merge_split_transform] time column does not exist"
                                from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                                display_error_msg(title,status_msg,e)

                                opstat.set_status(False)

            if(opstat.get_status()) :
    
                mergeddatetime  =   []
        
                try :

                    error_count     =   0
            
                    for i in range(len(df[datecolumn])) :

                        try :

                            mergeddatetime.append(datetime.datetime.combine(df[datecolumn][i],df[timecolumn][i]))

                        except Exception as e:

                            error_count     =   error_count  + 1

                            if(errorrtn == "raise exception and terminate") :
                
                                title       =   "dfcleanser exception"       
                                status_msg  =   "[merge datetime columns] error "
                                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                                display_exception(title,status_msg,e)

                                opstat.set_status(False)

                                break

                            elif(errorrtn == "coerce and set result to NaT") :
                                
                                import numpy as np
                                mergeddatetime.append(np.datetime64('NaT'))

                                if( (error_count/len(df)) > (threshold * 0.01) ) :

                                    title       =   "dfcleanser exception"       
                                    status_msg  =   "[merge datetime columns] over threshold"
                                    from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                                    display_exception(title,status_msg,e)

                                    opstat.set_status(False)

                                    break

                            else :

                                mergeddatetime.append(df[datecolumn][i])

                                if( (error_count/len(df)) > (threshold * 0.01) ) :

                                    title       =   "dfcleanser exception"       
                                    status_msg  =   "[merge datetime columns] over threshold"
                                    from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                                    display_exception(title,status_msg,e)

                                    opstat.set_status(False)

                                    break

                    if(opstat.get_status()) :

                        from dfcleanser.sw_utilities.GenericFunctionsModel import add_column_to_df
                        df  =   add_column_to_df(df,datetimecolumn,mergeddatetime,opstat)

                    if(opstat.get_status()) :

                        from dfcleanser.common.cfg import set_dfc_dataframe_df
                        set_dfc_dataframe_df(dftitle,df)
        
                # convert to .date or .time         
                except Exception as e:
                
                    title       =   "dfcleanser exception"       
                    status_msg  =   "[process_datetime_merge_transform] error "
                    from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                    display_exception(title,status_msg,e)

                    opstat.set_status(False)
                
                
    return(opstat)


def process_get_datetime_component(dftitle,column,comp_column,component) :
    """
    * --------------------------------------------------------
    * function : get the datatime component into a column
    * 
    * parms :
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    from dfcleanser.common.common_utils import opStatus
    opstat = opStatus()
    
    from dfcleanser.common.cfg import get_dfc_dataframe_df 
    df      =   get_dfc_dataframe_df(dftitle)
    
    if(len(column) == 0) :

        title       =   "dfcleanser error"       
        status_msg  =   "[process_datetime_merge_split_transform] no column "
        from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
        display_error_msg(title,status_msg,e)

        opstat.set_status(False)

    if(opstat.get_status()) :

        if(len(comp_column) == 0) :

            title       =   "dfcleanser error"       
            status_msg  =   "[process_datetime_merge_split_transform] no new column "
            from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
            display_error_msg(title,status_msg,e)

            opstat.set_status(False)

    if(opstat.get_status()) :

        comptype        =   component   

        try :

            import pandas as pd
            didx    =  pd.DatetimeIndex(df[column]) 
        
            if(comptype == "date")              :   colvalslist     =   didx.date
            elif(comptype == "year")            :   colvalslist     =   didx.year
            elif(comptype == "quarter")         :   colvalslist     =   didx.quarter
            elif(comptype == "month")           :   colvalslist     =   didx.month
            elif(comptype == "week")            :   colvalslist     =   didx.week
            elif(comptype == "week of year")    :   colvalslist     =   didx.weekofyear
            elif(comptype == "day")             :   colvalslist     =   didx.day
            elif(comptype == "day of year")     :   colvalslist     =   didx.dayofyear
            elif(comptype == "day of week")     :   colvalslist     =   didx.dayofweek
            elif(comptype == "time")            :   colvalslist     =   didx.time
            elif(comptype == "hour")            :   colvalslist     =   didx.hour
            elif(comptype == "minute")          :   colvalslist     =   didx.minute
            elif(comptype == "second")          :   colvalslist     =   didx.second
            elif(comptype == "microsecond")     :   colvalslist     =   didx.microsecond
            elif(comptype == "nanosecond")      :   colvalslist     =   didx.nanosecond
            else :
                    
                title       =   "dfcleanser error"       
                status_msg  =   "[process_get_datetime_componen] invalid comp "
                from dfcleanser.sw_utilities.dfc_qt_model import display_error_msg
                display_error_msg(title,status_msg,e)

                opstat.set_status(False)

            if(opstat.get_status()) :
                
                from dfcleanser.sw_utilities.GenericFunctionsModel import add_column_to_df 
                df  =   add_column_to_df(df,comp_column,colvalslist,opstat)

                if(opstat.get_status()) :

                    from dfcleanser.common.cfg import set_dfc_dataframe_df
                    set_dfc_dataframe_df(dftitle,df)

        except Exception as e:
        
            title       =   "dfcleanser exception"       
            status_msg  =   "[process_get_datetime_componen] error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_status(False)

    return(opstat)
    

# -----------------------------------------------------------------# 
# -----------------------------------------------------------------# 
# -            Data Transform Datetime Utilities end              -#
# -----------------------------------------------------------------# 
# -----------------------------------------------------------------#


