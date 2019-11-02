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

GENFUNC_OPTION              =   11
SAVE_FUNCTION               =   12
DELETE_FUNCTION             =   13
CLEAR_FUNCTION              =   14
RETURN_FUNCTION             =   15

PROCESS_FUNCTION            =   16
SELECT_FUNCTION             =   17

DICT_ID         =   0
LIST_ID         =   1

ReservedDicts   =   ["strftime","Elipsoids","Country_Codes","Language_Codes","ArcGIS_Categories","US_States_and_Territories","Canadian_Provinces_and_Territories"]
ReservedLists   =   ["Google_Address_Components", "Google_Location_Types"]


FOR_ADD_COLUMNS                     =   0
FOR_APPLY_FN                        =   1
FOR_GEN_FUNC                        =   2

Red             =   "#FAA78F"
Green           =   "#8FFAC0"
Yellow          =   "#FAFB95"

