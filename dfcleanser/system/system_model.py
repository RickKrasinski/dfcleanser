"""
# system_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]

Red     = "#FAA78F"
Green   = "#8FFAC0"
Yellow  = "#FAFB95"

READMEText =  """
README
"""

DISPLAY_MAIN                =   0
DISPLAY_CHAPTERS            =   1
RESET_CHAPTERS              =   2
DISPLAY_DATAFRAMES          =   3
DISPLAY_SYSTEM              =   4
DISPLAY_DFC_FILES           =   5
DISPLAY_ABOUT               =   6

PROCESS_DFC_FILES           =   10

DISPLAY_EULA                =   12
PROCESS_EULA                =   13

DISPLAY_README              =   14

PROCESS_CHAPTERS            =   15
DISPLAY_ABBR_MAIN           =   16

EXIT_SETUP                  =   17

PROCESS_DATAFRAME           =   18


CORE                        =   0
UTILITIES                   =   1
SCRIPTING                   =   2

COPY_FILES                  =   0
RENAME_FILES                =   1
DELETE_FILES                =   2

DROP_DATAFRAME              =   0
SET_DATAFRAME               =   1
UPDATE_DATAFRAME            =   2


