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
    
    gtfuncs = reservedfunctions
    gtfuncs.sort()
    return(gtfuncs)


"""
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
* generic functions utilities
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


def get_function_kwvals(ftitle,dftitle,dfcolname) :
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
 
    #print("get_function_kwvals",ftitle,dftitle,dfcolname)
    
    kwvals  =   None
    
    if(ftitle == "upperCase_df_column")                         :    kwvals  =   {"dftitle":dftitle,"dfcolname":dfcolname}
    if(ftitle == "normalize_df_column")                         :    kwvals  =   {"dftitle":dftitle,"dfcolname":dfcolname}
    if(ftitle == "get_trig_values_for_column")                  :    kwvals  =   {"dftitle":dftitle,"dfcolname":dfcolname,"trigfunc":"sin"}
    if(ftitle == "convert_df_column_to_degrees_or_radians")     :    kwvals  =   {"dftitle":dftitle,"dfcolname":dfcolname,"degrees":"True"}
    if(ftitle == "absolute_df_column")                          :    kwvals  =   {"dftitle":dftitle,"dfcolname":dfcolname}
    if(ftitle == "round_df_column")                             :    kwvals  =   {"dftitle":dftitle,"dfcolname":dfcolname}
    if(ftitle == "get_dist_from_center_df_column")              :    kwvals  =   {"dftitle":dftitle,"dfcolname":dfcolname,"units":"USER VALUE"}
    if(ftitle == "get_dist_from_point_df_column")               :    kwvals  =   {"dftitle":dftitle,"dfcolname":dfcolname,"point":"USER VALUE","units":"USER VALUE"}
    if(ftitle == "random_int_range")                            :    kwvals  =   {"dftitle":dftitle,"randomIntLower":"0","randomIntUpper":"0"}
    if(ftitle == "random_float_range")                          :    kwvals  =   {"dftitle":dftitle,"randomFloatLower":"0.0","randomFloatUpper":"0.0"}
        
    return(kwvals)


def get_function_return_datatype(ftitle) :
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
    
    
def get_function_kwval_parms_select(ftitle,parmid) :
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
 
    #print("get_function_kwvals",ftitle,parmid)
    
    select_dict  =   None
    
    if(parmid == "dftitle") :
        dataframes_loaded   =   cfg.get_dfc_dataframes_titles_list()
        current_df_name     =   cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF)
        select_dict         =   {"default":current_df_name,"list":dataframes_loaded}
        
    elif(parmid == "dfcolname") :
        current_df_name     =   cfg.get_config_value(cfg.CURRENT_TRANSFORM_DF)
        df                  =   cfg.get_dfc_dataframe_df(current_df_name)
        cols_list           =   df.columns.tolist()
        select_dict         =   {"default":cols_list[0],"list":cols_list}
        
    elif(ftitle == "get_trig_values_for_column") :
        if(parmid == "trigfunc") :        
            select_dict         =   {"default":'sin',"list":['sin','cos','tan','arcsin','arccos','arctan']}

    elif(ftitle == "convert_df_column_to_degrees_or_radians") :
        if(parmid == "degrees") :        
            select_dict         =   {"default":True,"list":[True,False]}
            
    elif(ftitle == "get_dist_from_center_df_column") :
        if(parmid == "units") :        
            select_dict         =   {"default":True,"list":[True,False]}
            
    elif(ftitle == "get_dist_from_point_df_column") :
        if(parmid == "units") :        
            select_dict         =   {"default":True,"list":[True,False]}
    
    return(select_dict)
    

def get_function_call(ftitle,fparms_dict) :
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
 
    print("get_function_call",ftitle,fparms_dict)
    funcparms       =   get_reserved_function_parms(ftitle)
    
    func_call       =   (ftitle + "(")

    for i in range(len(funcparms)) :
            
        if(funcparms[i] == "dftitle") :
            if(not (fparms_dict.get("dftitle",None) is None)) :
                func_call       =   (func_call + "'" + fparms_dict.get("dftitle",None) + "'")
            else :
                func_call       =   (func_call + "****")
        
        elif(funcparms[i] == "dfcolname") :
            if(not (fparms_dict.get("dfcolname",None) is None)) :
                func_call       =   (func_call + ",  '" + fparms_dict.get("dfcolname",None) + "'")
            else :
                func_call       =   (func_call + ",  ****")
        
        elif(funcparms[i] == "opstat") :
            func_call       =   (func_call + ",  opstat ")
        else :
            func_call       =   (func_call + ",  " + "****") 

        func_call       =   (func_call + ")") 
        
    return(func_call)





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


def get_df_function_source(ftitle,sourceOnly=True) :
    """
    * ------------------------------------------------------------------------
    * function : get the function help doc
    * 
    * parms :
    *  ftitle     - function 
    *  sourceOnly - source only flag
    *
    * returns : 
    *    function function code
    *
    * -------------------------------------------------------------------------
    """

    import inspect
    
    from dfcleanser.sw_utilities.sw_utility_genfunc_model import reservedfunctions

    if(ftitle == reservedfunctions[0])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import upperCase_df_column
        gfcode      =   inspect.getsource(upperCase_df_column)        
    elif(ftitle == reservedfunctions[1])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import normalize_df_column
        gfcode      =   inspect.getsource(normalize_df_column) 
    elif(ftitle == reservedfunctions[2])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import get_trig_values_for_column
        gfcode      =   inspect.getsource(get_trig_values_for_column) 
    elif(ftitle == reservedfunctions[3])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import convert_df_column_to_degrees_or_radians
        gfcode      =   inspect.getsource(convert_df_column_to_degrees_or_radians) 
    elif(ftitle == reservedfunctions[4])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import absolute_df_column
        gfcode      =   inspect.getsource(absolute_df_column) 
    elif(ftitle == reservedfunctions[5])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import round_df_column
        gfcode      =   inspect.getsource(round_df_column) 
    elif(ftitle == reservedfunctions[6])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import get_dist_from_center_df_column
        gfcode      =   inspect.getsource(get_dist_from_center_df_column) 
    elif(ftitle == reservedfunctions[7])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import get_dist_from_point_df_column
        gfcode      =   inspect.getsource(get_dist_from_point_df_column) 
    elif(ftitle == reservedfunctions[8])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import random_int_range
        gfcode      =   inspect.getsource(random_int_range) 
    elif(ftitle == reservedfunctions[9])  :   
        from dfcleanser.sw_utilities.sw_utility_genfunc_functions import random_float_range
        gfcode      =   inspect.getsource(random_float_range) 
        
    if(sourceOnly) :
        firstcomment    =   gfcode.find('"""')
        secondcomment   =   gfcode.find('"""',firstcomment + 3)
        
        newgfcode       =   gfcode[secondcomment+3:]
        newgfcode       =   newgfcode.lstrip("\n")
        newgfcode       =   newgfcode.lstrip("\n")

        return(str(newgfcode))
        
    else :
        return(gfcode)
        

def get_function_kwargs(module,fname,kwvals=None) :
    """
    * ------------------------------------------------------------------------
    * function : get the function keyord args
    * 
    * parms :
    *  module     - function module
    *  fname      - function name
    *
    * returns : 
    *    function heyword args
    *
    * -------------------------------------------------------------------------
    """
    
    #print("get_function_kwargs",module,fname,kwvals)
    
    help_text   =   get_function_help_doc(module,fname)
    
    if(len(help_text) > 0) :
    
        start_kwargs    =   help_text.find("(")    
        end_kwargs      =   help_text.find(")")
        
        kwargs  =   help_text[start_kwargs+1:end_kwargs]
        kwargs  =   kwargs.split(",")
        
        for i in range(len(kwargs)) :
            kwargs[i]   =   kwargs[i].lstrip(" ")
            kwargs[i]   =   kwargs[i].rstrip(" ")
            
            defval      =   kwargs[i].find("=")
            if(defval > -1) :
                kwargs[i]   =   kwargs[i][:defval] 
                
        from dfcleanser.common.html_widgets import new_line
        
        kwargs_text     =   "from " + module + " import " + fname + new_line
        kwargs_text     =   kwargs_text + fname + "("
        
        for i in range(len(kwargs)) :
            
            if(i == (len(kwargs)-1)) :
                endchar     =   ""
            else :
                endchar     =   ", "
            
            if(i>0) :
                kwargs_text     =   kwargs_text  + kwargs[i] + "="  
            
            if(not(kwvals is None)) :
                
                kwval   =   kwvals.get(kwargs[i],None)
                if(kwval is None) :
                    kwargs_text     =   kwargs_text  + " 'USER VALUE' " + endchar  
                else :
                    kwargs_text     =   kwargs_text  + str(kwval) + endchar  
            else :    
                kwargs_text     =   kwargs_text  + " 'USER VALUE' " + endchar
                
        kwargs_text     =   kwargs_text + ") "        
                
        return([kwargs,kwargs_text])
        
    else :
        
        return(None)


"""
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
* generic functions classes
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
"""

GENERIC_FUNCTIONS_FILE_NAME       =   "dfcleanserCommon_gfunclog.json"

"""
* -----------------------------------------------------------------------*
* generic function class
* -----------------------------------------------------------------------*
"""
class genericFunction :

    def __init__(self,fmodparm="",ftitleparm="",fcodeparm="") :
        
        self.fmodule     =   fmodparm
        self.ftitle      =   ftitleparm
        self.fcode       =   fcodeparm

    def get_func_module(self) :
        return(self.fmodule)
    def get_func_title(self) :
        return(self.ftitle)
    def get_func_code(self) :
        return(self.fcode)
        
    def set_func_module(self,module) :
        self.fmodule    =   module
    def set_func_title(self,title) :
        self.ftitle     =   title
    def set_func_code(self,code) :
        self.fcode      =   code

    def get_serial_func(self) :
        return([self.get_func_module(),
                self.get_func_title(),
                self.get_func_code(),
                self.get_func_kwargs()])

"""
* -----------------------------------------------------------------------*
* helper functions
* -----------------------------------------------------------------------*
"""

def add_generic_function(genfunc) :
    GenericFunctions.add_function(genfunc)

def get_generic_function(ftitle) :
    if(not (ftitle in reservedfunctions)) :
        return(GenericFunctions.get_function(ftitle))
    
def get_generic_function_desc(ftitle) :
    
    if(ftitle in reservedfunctions) :
        #from dfcleanser.sw_utilities.sw_utility_genfunc_functions import get_function_help_doc
        module_name   =   "dfcleanser.sw_utilities.sw_utility_genfunc_functions"
        return(get_function_help_doc(module_name,ftitle))
        
    else :
        return(ftitle)

def delete_generic_function(title) :
    GenericFunctions.delete_function(title)

def get_total_generic_functions() :
    print("get_total_generic_functions")
    total_funcs     =   len(reservedfunctions)
    total_funcs     =   total_funcs + GenericFunctions.get_total_functions()
    return(total_funcs)

def get_generic_functions_names_list() :
    print("get_generic_functions_names_list")
    func_list   =   []
    for i in range(len(reservedfunctions)) :
        func_list.append(reservedfunctions[i])
        
    user_funcs  =   GenericFunctions.get_function_list()
    for i in range(len(user_funcs)) :
        func_list.append(user_funcs[i])
    
    return(func_list)

"""
* -----------------------------------------------------------------------*
* generic transforms storage class
* -----------------------------------------------------------------------*
"""
class genericFunctionsStore :

    def __init__(self) :

        # instance variables
        self.genericfunctionDict    =   {}
        self.load_generic_functions_file()
    
    def get_functions_file_name(self) :
        import os
        return(os.path.join(cfg.get_common_files_path(),GENERIC_FUNCTIONS_FILE_NAME))
    
    def load_generic_functions_file(self) :
        
        fname   =    self.get_functions_file_name() 
        if(not (fname == None)) :
        
            try :
                serial_gen_func_dict    =   {}
                
                with open(fname, 'r') as gen_func_file :
                    serial_gen_func_dict = json.load(gen_func_file)
                    gen_func_file.close()
               
                if(len(serial_gen_func_dict) > 0) :
                    gf_keys         =   list(serial_gen_func_dict)
                    
                    for i in range(len(gf_keys)) :
                        gen_func_list   =   serial_gen_func_dict.get(gf_keys[i])
                        new_gf          =   genericFunction(gen_func_list[0],
                                                            gen_func_list[1],
                                                            gen_func_list[2],
                                                            gen_func_list[3])
                    
                    self.genericfunctionDict.update({gf_keys[i] : new_gf}) 
                    
            except FileNotFoundError :
                self.genericfunctionDict = {}
            except :
                #print("[error load gen_func file ...]",str(sys.exc_info()[0]))
                self.genericfunctionDict = {}
    
    def save_generic_functions_file(self) :
        
        fname   =    self.get_functions_file_name() 
        if(not (fname == None)) :
            
            gf_keys         =   list(self.genericfunctionDict.keys())

            serial_gen_func_dict   =   {}
            
            if(len(gf_keys) > 0) :
                for i in range(len(gf_keys)) : 
                    serial_func     =   self.genericfunctionDict.get(gf_keys[i]).get_serial_func()
                    serial_gen_func_dict.update({gf_keys[i] : serial_func})
    
                if(len(gf_keys) > 0) :
                    try :
            
                        with open(fname, 'w') as gen_func_file :
                            json.dump(serial_gen_func_dict,gen_func_file)
                            gen_func_file.close()
                
                    except :
                        print("[save_generic_functions_file error] : " + str(sys.exc_info()[0]))
                        
            else :
                    
                import os 
                os.remove(self.get_functions_file_name())
            
    def add_function(self,function) :
        
        title   =   function.get_func_title()
        self.genericfunctionDict.update({title:function})
        self.save_generic_functions_file()
            
    def get_total_functions(self) :
        if(self.genericfunctionDict == {}) :
            self.load_generic_functions_file()    
        return(len(self.genericfunctionDict))
    
    def get_function_list(self) :
        return(list(self.genericfunctionDict.keys()))
        
    def delete_function(self,title) :
        print("delete_function",title,len(self.genericfunctionDict))
        try :
            del self.genericfunctionDict[title]
        except :
            print("key not found"
                  )
        print("delete_function",title,len(self.genericfunctionDict))
        self.save_generic_functions_file()
        
    def get_function(self,functionTitle) :
        if(self.genericfunctionDict == {}) :
            self.load_generic_functions_file()    
        
        return(self.genericfunctionDict.get(functionTitle,None))

"""
# -----------------------------------------------------------------
#                   static gewneric function store
# -----------------------------------------------------------------
"""        
GenericFunctions   =   genericFunctionsStore()
    
 
