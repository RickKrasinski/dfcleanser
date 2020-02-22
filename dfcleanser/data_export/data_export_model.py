"""
# data_export_model 
"""

# -*- coding: utf-8 -*-
"""
Created on Sept 13 22:29:22 2018

@author: Rick
"""
import sys
this = sys.modules[__name__]

EXPORT_TB_ONLY                          =   0
EXPORT_PANDAS_TB_ONLY                   =   1
EXPORT_PANDAS_TB_PLUS_DETAILS           =   2
EXPORT_CUSTOM_ONLY                      =   3

EXPORT_DF_FROM_CENSUS                   =   4
EXPORT_TO_DB_FROM_CENSUS                =   5

CSV_EXPORT                              =   0
EXCEL_EXPORT                            =   1
JSON_EXPORT                             =   2
HTML_EXPORT                             =   3
SQLTABLE_EXPORT                         =   4
CUSTOM_EXPORT                           =   5

