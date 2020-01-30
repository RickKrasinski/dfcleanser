"""
# sw_utility_genfunc_widgets
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


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#    generic functions components
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

DISPLAY_GENERIC_FUNCTION_TB         =   0
DISPLAY_GENERIC_FUNCTION            =   1
PROCESS_GENERIC_FUNCTION_OPTION     =   2

LOAD_FUNCTION                       =   0
SAVE_FUNCTION                       =   1
UPDATE_FUNCTION                     =   2
DISPLAY_FUNCTION                    =   3
DELETE_FUNCTION                     =   4
RETURN_FUNCTION                     =   5
SELECT_FUNCTION                     =   6
CLEAR_FUNCTION                      =   7

FOR_ADD_COLUMNS                     =   0
FOR_APPLY_FN                        =   1
FOR_GEN_FUNC                        =   2


applyfns                            =   ["np.sin","np.cos","np.tan","np.arcsin","np.arccos","np.arctan",
                                         "np.degrees","np.radians",
                                         "np.absolute","np.square","np.sqrt",
                                         "np.ceil","np.floor","np.rint",
                                         "np.reciprocal","np.positive","np.negative",
                                         "np.capitalize",
                                         "lambda x: x.upper()","lambda x: x.lower()","lambda x: x.round(ndigits)",
                                         "lambda x: x.strip(stripchar)","lambda x: x.lstrip(stripchar)","lambda x: x.rstrip(stripchar)",
                                         "lambda x: x.center(width,fillchar)","lambda x: x.ljust(width,fillchar)",
                                         "lambda x: x.rjust(width,fillchar)","lambda x: x.replace(old,new)",
                                         "lambda x: x.slice(start,stop)"]

reservedfunctions                   =   ["upperCase_df_column","normalize_df_column","get_trig_values_for_column",
                                         "convert_df_column_to_degrees_or_radians","absolute_df_column","round_df_column",
                                         "get_dist_from_center_df_column","get_dist_from_point_df_column","random_int_range",
                                         "random_float_range"]

reservedfunctionsmodule             =    "dfcleanser.sw_utilities.sw_utility_genfunc_functions"


Red     = "#FAA78F"
Green   = "#8FFAC0"
Yellow  = "#F5F7A5"


def get_genfunc_list() :
    """
    * ------------------------------------------------------------------------
    * function : get the list of dfc reserved functions
    * 
    * parms :
    *
    * returns : 
    *    function call
    *
    * -------------------------------------------------------------------------
    """
    
    gtfuncs = reservedfunctions
    gtfuncs.sort()
    return(gtfuncs)


"""
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
* generic apply to fn functions utilities
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
"""

def get_apply_function_return_datatype(ftitle) :
    """
    * ------------------------------------------------------------------------
    * function : get the function call for reserved functions
    * 
    * parms :
    *  ftitle      - reserved function title
    *  fparms_dict - function parms dict
    *
    * returns : 
    *    function call
    *
    * -------------------------------------------------------------------------
    """
    
    dtype  =   "str"
    
    if(ftitle.find("np.sin") > -1 )                 :   dtype  =   "float"
    elif(ftitle.find("np.cos") > -1 )               :   dtype  =   "float"
    elif(ftitle.find("np.tan") > -1 )               :   dtype  =   "float"
    elif(ftitle.find("np.arcsin") > -1 )            :   dtype  =   "float"
    elif(ftitle.find("np.arccos") > -1 )            :   dtype  =   "float"
    elif(ftitle.find("np.arctan") > -1 )            :   dtype  =   "float"
    elif(ftitle.find("np.degrees") > -1 )           :   dtype  =   "float"
    elif(ftitle.find("np.radians") > -1 )           :   dtype  =   "float"
    elif(ftitle.find("np.absolute") > -1 )          :   dtype  =   "numeric"
    elif(ftitle.find("np.square") > -1 )            :   dtype  =   "numeric"
    elif(ftitle.find("np.sqrt") > -1 )              :   dtype  =   "numeric"
    elif(ftitle.find("np.ceil") > -1 )              :   dtype  =   "numeric"
    elif(ftitle.find("np.floor") > -1 )             :   dtype  =   "numeric"
    elif(ftitle.find("np.rint") > -1 )              :   dtype  =   "int"
    elif(ftitle.find("np.reciprocal") > -1 )        :   dtype  =   "float"
    elif(ftitle.find("np.positive") > -1 )          :   dtype  =   "numeric"
    elif(ftitle.find("np.negative") > -1 )          :   dtype  =   "numeric"
    elif(ftitle.find("np.capitalize") > -1 )        :   dtype  =   "str"
    elif(ftitle.find("x.round") > -1 )              :   dtype  =   "numeric"
    elif(ftitle.find("x.strip") > -1 )              :   dtype  =   "str"
    elif(ftitle.find("x.lstrip") > -1 )             :   dtype  =   "str"
    elif(ftitle.find("x.rstrip") > -1 )             :   dtype  =   "str"
    elif(ftitle.find("x.center") > -1 )             :   dtype  =   "str"
    elif(ftitle.find("x.ljust") > -1 )              :   dtype  =   "str"
    elif(ftitle.find("x.rjust") > -1 )              :   dtype  =   "str"
    elif(ftitle.find("x.replace") > -1 )            :   dtype  =   "str"
    elif(ftitle.find("x.slice") > -1 )              :   dtype  =   "str"
        
    return(dtype)


def get_apply_function_parms_datatypes(ftitle) :
    """
    * ------------------------------------------------------------------------
    * function : get the function parms datatypes for apply functions
    * 
    * parms :
    *  ftitle     - reserved function title
    *
    * returns : 
    *    opstat function parms
    *
    * -------------------------------------------------------------------------
    """
    fparms  =   None
    
    if(ftitle.find("x.round") > -1 )                            :   fparms  =   [int]
    elif(ftitle.find("x.strip") > -1 )                          :   fparms  =   [str]
    elif(ftitle.find("x.lstrip") > -1 )                         :   fparms  =   [str]
    elif(ftitle.find("x.rstrip") > -1 )                         :   fparms  =   [str]
    elif(ftitle.find("x.center") > -1 )                         :   fparms  =   [int,str]
    elif(ftitle.find("x.ljust") > -1 )                          :   fparms  =   [int,str]
    elif(ftitle.find("x.rjust") > -1 )                          :   fparms  =   [int,str]
    elif(ftitle.find("x.replace") > -1 )                        :   fparms  =   [str,str]
    elif(ftitle.find("x.slice") > -1 )                          :   fparms  =   [int,int]
    
    return(fparms)


def get_apply_function_parms(ftitle) :
    """
    * ------------------------------------------------------------------------
    * function : get the function parms for apply functions
    * 
    * parms :
    *  ftitle     - reserved function title
    *
    * returns : 
    *    opstat function parms
    *
    * -------------------------------------------------------------------------
    """
    fparms  =   None
    
    if(ftitle.find("x.round") > -1 )                            :   fparms  =   ["ndigits"]
    elif(ftitle.find("x.strip") > -1 )                          :   fparms  =   ["stripchar"]
    elif(ftitle.find("x.lstrip") > -1 )                         :   fparms  =   ["stripchar"]
    elif(ftitle.find("x.rstrip") > -1 )                         :   fparms  =   ["stripchar"]
    elif(ftitle.find("x.center") > -1 )                         :   fparms  =   ["width","fillchar"]
    elif(ftitle.find("x.ljust") > -1 )                          :   fparms  =   ["width","fillchar"]
    elif(ftitle.find("x.rjust") > -1 )                          :   fparms  =   ["width","fillchar"]
    elif(ftitle.find("x.replace") > -1 )                        :   fparms  =   ["old","new"]
    elif(ftitle.find("x.slice") > -1 )                          :   fparms  =   ["start","stop"]
    
    return(fparms)


"""
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
* generic add column from reserved functions utilities
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
"""
def get_reserved_function_parms_datatypes(ftitle) :
    """
    * ------------------------------------------------------------------------
    * function : get the function parms for reserved functions
    * 
    * parms :
    *  ftitle     - reserved function title
    *
    * returns : 
    *    opstat function parms
    *
    * -------------------------------------------------------------------------
    """
    fparms  =   None
    
    if(ftitle == "upperCase_df_column")                         :   fparms  =   [str,str]
    elif(ftitle == "normalize_df_column")                       :   fparms  =   [str,str]
    elif(ftitle == "get_trig_values_for_column")                :   fparms  =   [str,str,str]
    elif(ftitle == "convert_df_column_to_degrees_or_radians")   :   fparms  =   [str,str,float]
    elif(ftitle == "absolute_df_column")                        :   fparms  =   [str,str]
    elif(ftitle == "round_df_column")                           :   fparms  =   [str,str,int]
    elif(ftitle == "get_dist_from_center_df_column")            :   fparms  =   [str,str,int]
    elif(ftitle == "get_dist_from_point_df_column")             :   fparms  =   [str,str,float,int]
    elif(ftitle == "random_int_range")                          :   fparms  =   [str,int,int]
    elif(ftitle == "random_float_range")                        :   fparms  =   [str,float,float]
    
    return(fparms)


def get_reserved_function_parms(ftitle) :
    """
    * ------------------------------------------------------------------------
    * function : get the function parms for reserved functions
    * 
    * parms :
    *  ftitle     - reserved function title
    *
    * returns : 
    *    opstat function parms
    *
    * -------------------------------------------------------------------------
    """
    fparms  =   None
    
    if(ftitle == "upperCase_df_column")                         :   fparms  =   "dftitle,dfcolname"
    elif(ftitle == "normalize_df_column")                       :   fparms  =   "dftitle,dfcolname"
    elif(ftitle == "get_trig_values_for_column")                :   fparms  =   "dftitle,dfcolname,trigfunc"
    elif(ftitle == "convert_df_column_to_degrees_or_radians")   :   fparms  =   "dftitle,dfcolname,degrees"
    elif(ftitle == "absolute_df_column")                        :   fparms  =   "dftitle,dfcolname"
    elif(ftitle == "round_df_column")                           :   fparms  =   "dftitle,dfcolname,decimals"
    elif(ftitle == "get_dist_from_center_df_column")            :   fparms  =   "dftitle,dfcolname,units"
    elif(ftitle == "get_dist_from_point_df_column")             :   fparms  =   "dftitle,dfcolname,point,units"
    elif(ftitle == "random_int_range")                          :   fparms  =   "dftitle,randomIntLower,randomIntUpper"
    elif(ftitle == "random_float_range")                        :   fparms  =   "dftitle,randomFloatLower,randomFloatUpper"
    
    if(not(fparms is None)) :
        fparms  =   fparms.split(",")
    
    return(fparms)


def get_reserved_function_return_datatype(ftitle) :
    """
    * ------------------------------------------------------------------------
    * function : get the function call for reserved functions
    * 
    * parms :
    *  ftitle      - reserved function title
    *  fparms_dict - function parms dict
    *
    * returns : 
    *    function call
    *
    * -------------------------------------------------------------------------
    """
    
    dtype  =   "str"
    
    if(ftitle == "upperCase_df_column")                         :    dtype   =  "str"
    if(ftitle == "normalize_df_column")                         :    dtype   =  "float"
    if(ftitle == "get_trig_values_for_column")                  :    dtype   =  "float"
    if(ftitle == "convert_df_column_to_degrees_or_radians")     :    dtype   =  "float"
    if(ftitle == "absolute_df_column")                          :    dtype   =  "float"
    if(ftitle == "round_df_column")                             :    dtype   =  "float"
    if(ftitle == "get_dist_from_center_df_column")              :    dtype   =  "float"
    if(ftitle == "get_dist_from_point_df_column")               :    dtype   =  "float"
    if(ftitle == "random_int_range")                            :    dtype   =  "int"
    if(ftitle == "random_float_range")                          :    dtype   =  "float"
        
    return(dtype)
    

DF_COL                  =   0
DF_COL_NUM              =   1
DF_COL_NUM_NUM          =   2
DF_NUM_NUM              =   3


def get_reserved_function_form_type(ftitle) :
    """
    * ------------------------------------------------------------------------
    * function : get the function form type
    * 
    * parms :
    *  ftitle     - reserved function title
    *
    * returns : 
    *    opstat function parms
    *
    * -------------------------------------------------------------------------
    """
    
    if(ftitle == "upperCase_df_column")                         :   return(DF_COL)
    elif(ftitle == "normalize_df_column")                       :   return(DF_COL)
    elif(ftitle == "get_trig_values_for_column")                :   return(DF_COL_NUM)
    elif(ftitle == "convert_df_column_to_degrees_or_radians")   :   return(DF_COL_NUM)
    elif(ftitle == "absolute_df_column")                        :   return(DF_COL)
    elif(ftitle == "round_df_column")                           :   return(DF_COL_NUM)
    elif(ftitle == "get_dist_from_center_df_column")            :   return(DF_COL_NUM)
    elif(ftitle == "get_dist_from_point_df_column")             :   return(DF_COL_NUM_NUM)
    elif(ftitle == "random_int_range")                          :   return(DF_NUM_NUM)
    elif(ftitle == "random_float_range")                        :   return(DF_NUM_NUM)
    
    return(None)


def get_function_help_doc(module,fname) :
    """
    * ------------------------------------------------------------------------
    * function : get the function help doc
    * 
    * parms :
    *  module     - python module
    *  fname      - function name
    *
    * returns : 
    *    function function help
    *
    * -------------------------------------------------------------------------
    """
    
    temp_file   =   "temp_help_file"
    
    import contextlib

    try :
        
        with open(temp_file, 'w') as f:
            with contextlib.redirect_stdout(f):
                help(module + "." + fname)
            
        f.close()
    
        with open(temp_file,'r') as h:
            textdata = h.read()

        h.close()
        
    except :
        textdata    =   ""
    
    if(len(textdata) > 0) :
        import os
        os.remove(temp_file)
    
        start_help  =   textdata.find(fname + "(")
    
        return(textdata[start_help:])
    else :
        return("")


"""
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
* generic functions classes
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
"""

GENERIC_USER_FUNCTIONS_FILE_NAME       =   "dfcleanserCommon_gfunclog.json"

DFC_FUNCTION            =   0
USER_FUNCTION           =   1


"""
* -----------------------------------------------------------------------*
* Generic Functions helper functions
* -----------------------------------------------------------------------*
"""

"""
* -----------------------------------------------------------------------*
* dfc defined functions
* -----------------------------------------------------------------------*
"""
def get_generic_function_desc(ftitle) :
    
    if(ftitle in reservedfunctions) :
        module_name   =   "dfcleanser.sw_utilities.sw_utility_genfunc_functions"
        return(get_function_help_doc(module_name,ftitle))
    else :
        return(None)

def get_total_generic_functions() :
    return(len(reservedfunctions))

def get_generic_functions_names_list() :
    func_list   =   []
    for i in range(len(reservedfunctions)) :
        func_list.append(reservedfunctions[i])
    
    return(func_list.sort())


"""
* -----------------------------------------------------------------------*
* User defined functions
* -----------------------------------------------------------------------*
"""

def add_generic_user_function(ftitle,fmodule,fcode) :
    GenericUserFunctions.add_function(ftitle,fmodule,fcode)

def get_generic_user_function(ftitle) :
    if(not (ftitle in reservedfunctions)) :
        return(GenericUserFunctions.get_function(ftitle))
    
def get_generic_user_function_desc(ftitle) :
    
    if(ftitle in reservedfunctions) :
        module_name   =   "dfcleanser.sw_utilities.sw_utility_genfunc_functions"
        return(get_function_help_doc(module_name,ftitle))
    else :
        return(None)

def delete_generic_user_function(ftitle) :
    GenericUserFunctions.delete_function(ftitle)

def get_total_generic_user_functions() :
    return(GenericUserFunctions.get_total_functions())

def get_generic_user_functions_names_list() :

    user_funcs  =   GenericUserFunctions.get_function_list()
    user_funcs.sort()
    return(user_funcs)
    
    

"""
* -----------------------------------------------------------------------*
* generic transforms storage class
* -----------------------------------------------------------------------*
"""
class genericUserFunctionsStore :

    def __init__(self) :

        # instance variables
        self.genericfunctionDict    =   {}
        self.load_generic_functions_file()
    
    def get_functions_file_name(self) :
        
        import os
        return(os.path.join(cfg.get_common_files_path(),GENERIC_USER_FUNCTIONS_FILE_NAME))
    
    def load_generic_functions_file(self) :
        
        fname   =    self.get_functions_file_name() 
        if(not (fname == None)) :
        
            try :
                with open(fname, 'r') as gen_func_file :
                    self.genericfunctionDict = json.load(gen_func_file)#serial_gen_func_dict = json.load(gen_func_file)
                    gen_func_file.close()
               
            except FileNotFoundError :
                print("[file not found error load gen_func file ...]",str(sys.exc_info()[0]))
                self.genericfunctionDict = {}
            except :
                print("[error load gen_func file ...]",str(sys.exc_info()[0]))
                self.genericfunctionDict = {}
    
    def save_generic_functions_file(self) :
        
        fname   =    self.get_functions_file_name() 
        if(not (fname == None)) :
            
            if(len(self.genericfunctionDict) > 0) :
    
                try :
            
                    with open(fname, 'w') as gen_func_file :
                        json.dump(self.genericfunctionDict,gen_func_file)
                        gen_func_file.close()
                
                except :
                    print("[save_generic_functions_file error] : " + str(sys.exc_info()[0]))
                        
            else :
                    
                import os 
                os.remove(self.get_functions_file_name())
            
    def add_function(self,ftitle,fmodule,fcode) :
        self.genericfunctionDict.update({ftitle:[fmodule,fcode]})
        self.save_generic_functions_file()
            
    def get_total_functions(self) :
        if(self.genericfunctionDict == {}) :
            self.load_generic_functions_file()    
        return(len(self.genericfunctionDict))
    
    def get_function_list(self) :
        return(list(self.genericfunctionDict.keys()))
        
    def delete_function(self,title) :
        try :
            del self.genericfunctionDict[title]
        except :
            print("key not found")
            
        self.save_generic_functions_file()
        
    def get_function_code(self,title) :
        
        funccomps   =   self.genericfunctionDict.get(title,None)
        if(not (funccomps is None)) :
            return(funccomps[1])
        else  :
            return(None)
        
        
    def get_function(self,functionTitle) :
        if(self.genericfunctionDict == {}) :
            self.load_generic_functions_file() 
            
        return(self.genericfunctionDict.get(functionTitle,None))

"""
# -----------------------------------------------------------------
#                   static gewneric function store
# -----------------------------------------------------------------
"""        
GenericUserFunctions   =   genericUserFunctionsStore()
    
 
