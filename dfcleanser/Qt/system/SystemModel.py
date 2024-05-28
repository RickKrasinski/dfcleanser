"""
# SystemModel 
"""

# -*- coding: utf-8 -*-
"""
Created on Sept 13 22:29:22 2018

@author: Rick
"""
import sys
this = sys.modules[__name__]

def is_debug_on(chapterid,flagvalue) :

    from dfcleanser.common.debug_utils import is_debug_set
    return(is_debug_set(chapterid,flagvalue))

def save_debug_flags() :

    from dfcleanser.common.debug_utils import save_debug_file
    save_debug_file()


