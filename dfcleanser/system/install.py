"""
# install 
"""
# -*- coding: utf-8 -*-

"""
Created on Sat Aug 25 10:29:48 2018

@author: Rick
"""

import sys
this = sys.modules[__name__]

import sys
import os.path

import dfcleanser.common.cfg as cfg

from dfcleanser.common.common_utils import (opStatus, display_exception, read_text_file)


def install_dfcleanser() :
    """
    * -------------------------------------------------------------------------- 
    * function : install dfcleanser package
    * 
    * parms :
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """

    install_dfc_custom()
    install_dfc_notebook_widgets()


def install_dfc_notebook_widgets() :
    """
    * -------------------------------------------------------------------------- 
    * function : install dfcleanser widgets
    * 
    * parms :
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """

    return()    
    

def uninstall_dfcleanser() :
    """
    * -------------------------------------------------------------------------- 
    * function : uninstall dfcleanser package
    * 
    * parms :
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """
    
    opstat  =   opStatus()  
    
    from jupyter_core.paths import jupyter_config_dir
    jupyter_dir = jupyter_config_dir()
    
    custom_js_path      =   os.path.join(jupyter_dir, 'custom', 'custom.js')
    custom_css_path     =   os.path.join(jupyter_dir, 'custom', 'custom.css')
    
    try : 
        # remove existing dfcleanser js scripts
        remove_existing_dfcleanser_js(custom_js_path)
        # remove existing dfcleanser js scripts
        remove_existing_dfcleanser_css(custom_css_path)
        
        print("* dfcleanser uninstalled successfully")
        print("* To complete the uninstall you must restart the Jupyter notebook server")
        
    except Exception as e:
        opstat.store_exception("uninstall dfcleanser " + custom_js_path + custom_css_path,e)
        display_exception(opstat)

    
"""
# -----------------------------------------------------------------------
# components for installing the dfcleanser into Jupyter notebook server 
# -----------------------------------------------------------------------
"""
dfc_js_files    =   ["js_utils.js", "data_cleansing.js", "data_export.js", "data_import.js", "data_inspection.js", 
                     "data_scripting.js", "data_transform.js", "sw_utilities.js", "system.js" ]
dfc_css_files   =   ["dfc_styles.css"]


js_require_text_preamble = ("\n\n// ---------------------------------------\n" +
                            "//     dfcleanser javascript functions    \n" +
                            "// ---------------------------------------\n")
js_require_text_postamble = ("\n// ----------------------------------------\n" +
                             "//   end dfcleanser javascript functions  \n" +
                             "// ----------------------------------------")

css_require_text_preamble = ("\n/*\n" +
                             "// --------------------------\n" +
                             "//       dfcleanser css      \n" +
                             "// --------------------------\n" +
                             "*/\n")
css_require_text_postamble = ("\n/*\n" +
                              "// --------------------------\n" +
                              "//      end dfcleanser css      \n" +
                              "// --------------------------\n" +
                              "*/")


def remove_existing_dfcleanser_js(custom_js_path) :
    """
    * -------------------------------------------------------------------------- 
    * function : remove the dfcleanser jasvascript from Jupyter custom.js
    * 
    * parms :
    *  custom_js_path   - path of custom js
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """
    
    opstat = opStatus()
    
    try :
    
        newfilecontents     =   ""
            
        # custom.js exists 
        # open file and see if dfcleanser is embedded
        with open(custom_js_path,'r') as jupyter_custom_js_file :
            filecontents = jupyter_custom_js_file.read()

            startdfc = filecontents.find(js_require_text_preamble)

            # if dfc js in file delete it
            if(startdfc > -1) :
                
                if(startdfc > 0) :
                    newfilecontents     =   filecontents[0:(startdfc)]
                    
                startpostamble      =   filecontents.find(js_require_text_postamble)
                enddfc              =   startpostamble + len(js_require_text_postamble)

                if(len(filecontents) > enddfc) :
                    newfilecontents = (newfilecontents + filecontents[enddfc:])
                
                jupyter_custom_js_file.close()
                
            else :
                newfilecontents     =  filecontents 
                jupyter_custom_js_file.close()

        if(len(newfilecontents) == 0) :
            newfilecontents = ""
            
        with open(custom_js_path,'w') as jupyter_custom_js_file :
            jupyter_custom_js_file.write(newfilecontents)
            jupyter_custom_js_file.close()
                
    except Exception as e:
        opstat.store_exception("remove dfcleanser js " + custom_js_path,e)
        display_exception(opstat)


def remove_existing_dfcleanser_css(custom_css_path) :
    """
    * -------------------------------------------------------------------------- 
    * function : remove the dfcleanser css from Jupyter custom.css
    * 
    * parms :
    *  custom_css_path   - path of custom css
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """
    
    opstat = opStatus()
    
    try :
    
        newfilecontents     =   ""
            
        # custom.js rxists 
        # open file and see if dfcleanser is embedded
        with open(custom_css_path,'r') as jupyter_custom_css_file :
            filecontents = jupyter_custom_css_file.read()

            startdfc = filecontents.find(css_require_text_preamble)

            # if dfc css in file delete it
            if(startdfc > -1) :
                
                if(startdfc > 0) :
                    newfilecontents     =   filecontents[0:(startdfc-1)]
                    
                startpostamble      =   filecontents.find(css_require_text_postamble) 
                enddfc              =   startpostamble + len(css_require_text_postamble)
                
                if(len(filecontents) > enddfc) :
                    newfilecontents = (newfilecontents + filecontents[enddfc:])
                        
                jupyter_custom_css_file.close()
                
            else :
                newfilecontents     =  filecontents
                jupyter_custom_css_file.close()    

        if(len(newfilecontents) == 0) :
            newfilecontents = ""
            
        with open(custom_css_path,'w') as jupyter_custom_css_file :
            jupyter_custom_css_file.write(newfilecontents)
            jupyter_custom_css_file.close()
                
    except Exception as e:
        opstat.store_exception("remove dfcleanser css " + custom_css_path,e)
        display_exception(opstat)


def install_dfc_custom_css() :
    """
    * -------------------------------------------------------------------------- 
    * function : install the dfcleanser css from Jupyter custom.css
    * 
    * parms :
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """
    
    opstat  =   opStatus()  
    
    # get the custpm.js and custom.css location
    from jupyter_core.paths import jupyter_config_dir
    jupyter_dir = jupyter_config_dir()
    
    """  
    # ----------------------------------------------------------------------------          
    # now find the custom.css file and append the dfc css files
    # ----------------------------------------------------------------------------          
    """ 
    
    custom_css_path     =   os.path.join(jupyter_dir, 'custom', 'custom.css')
    dfcleanser_css_path =   os.path.join(cfg.get_dfcleanser_location(),'static')

    dfcleanser_css   =   ""
    
    try : 

        # remove existing dfcleanser js scripts
        remove_existing_dfcleanser_css(custom_css_path)
        
        dfcleanser_css   =   (dfcleanser_css + css_require_text_preamble)
        
        for i in range(len(dfc_css_files)) :
            
            dfcleanser_css_file_name  =   os.path.join(dfcleanser_css_path,dfc_css_files[i])
            
            css_file_code = read_text_file(dfcleanser_css_file_name,opstat)
            if(opstat.get_status()) :
                dfcleanser_css   =   (dfcleanser_css + css_file_code)
        
        dfcleanser_css   =   (dfcleanser_css + css_require_text_postamble)

        if(len(dfcleanser_css) > 0) :
            with open(custom_css_path,'a') as jupyter_custom_css_file :
                jupyter_custom_css_file.write(dfcleanser_css)
            
    except Exception as e:
        opstat.store_exception("[writng custom css file]["+ custom_css_path +"]",e)
        display_exception(opstat)


def install_dfc_custom() :
    """
    * -------------------------------------------------------------------------- 
    * function : Install the dfcleanser js and css components in the 
    *            Jupyter custom.js and custom.css files
    * 
    * parms :
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """

    opstat  =   opStatus()  
    
    # get the custpm.js and custom.css location
    from jupyter_core.paths import jupyter_config_dir
    jupyter_dir = jupyter_config_dir()
    
    """  
    # ---------------------------------------------------------------------------          
    # now have empty dfc_dir dir go ahead and copy all dfc js files to directory
    # ---------------------------------------------------------------------------          
    """ 
  
    """  
    # ----------------------------------------------------------------------------          
    # now find the custom.js file and append the dfc javascript files
    # ----------------------------------------------------------------------------          
    """ 
    
    custom_js_path      =   os.path.join(jupyter_dir, 'custom', 'custom.js')
    dfcleanser_js_path  =   os.path.join(cfg.get_dfcleanser_location(), 'static')
    
    dfcleanser_js       =   ""
    
    #print("install_dfc_custom",custom_js_path)
    #print("install_dfc_custom",dfcleanser_js_path)
    
    try : 

        # remove existing dfcleanser js scripts
        remove_existing_dfcleanser_js(custom_js_path)
        
        dfcleanser_js   =   (dfcleanser_js + js_require_text_preamble)
        
        for i in range(len(dfc_js_files)) :
            
            dfcleanser_js_file_name  =   os.path.join(dfcleanser_js_path, dfc_js_files[i])
            #print("install_dfc_custom",dfcleanser_js_file_name)
            js_file_code = read_text_file(dfcleanser_js_file_name,opstat)
            if(opstat.get_status()) :
                dfcleanser_js   =   (dfcleanser_js + js_file_code)
        
        dfcleanser_js   =   (dfcleanser_js + js_require_text_postamble)

        if(len(dfcleanser_js) > 0) :
            with open(custom_js_path,'a') as jupyter_custom_js_file :
                jupyter_custom_js_file.write(dfcleanser_js)
            
    except Exception as e:
        opstat.store_exception("Error writng custom js file : " + custom_js_path,e)
        display_exception(opstat)
    
    print("* updated Jupyter common.js with dfcleanser scripts")

        
    """  
    # ----------------------------------------------------------------------------          
    # now find the custom.css file and append the dfc css files
    # ----------------------------------------------------------------------------          
    """ 
    
    install_dfc_custom_css()
        
    if(opstat.get_status()) :
        print("* updated Jupyter common.css with dfcleanser styles")
        print("* dfcleanser installed to Jupyter - restart Jupyter Server to use dfcleanser ")
        print("* after restart from dfcleanser.system.install run setup_dfcleanser() ")
        print("\n")
    else :
        print("* unable to install dfcleanser")
    

def setup_dfcleanser() :
    """
    * -------------------------------------------------------------------------- 
    * function : setup dfcleanser
    * 
    * parms :
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """
    
    opstat  =   opStatus()
    
    from dfcleanser.system.load  import (add_dfc_cell, get_dfc_cells_text, DC_WORKING_TITLE, DC_WORKING, DC_SYSTEM, 
                                         MARKDOWN, CODE, DC_BLANK_LINE, DC_SYSTEM_TITLE, DC_PANDAS_TITLE) 
    from dfcleanser.common.common_utils import displayHTML, RunningClock
    
    from dfcleanser.common.common_utils import run_jscript
    celltext    =  "setup_dfcleanser" 
    jscript     =   ("select_cell_from_text(" +  "'" + celltext + "'" + ")")
    run_jscript(jscript,"Error setting dfc Cell") 
    
    # insert working cell 
    title_html = get_dfc_cells_text(DC_PANDAS_TITLE)
    displayHTML(title_html)

    # insert working cell 
    add_dfc_cell(MARKDOWN,DC_SYSTEM_TITLE)
    from dfcleanser.common.common_utils import get_dfc_cell_file
    cell_text = get_dfc_cell_file("SystemCodeCellAbbr",opstat)
    add_dfc_cell(CODE,DC_SYSTEM,cell_text)
    add_dfc_cell(MARKDOWN,DC_BLANK_LINE)
    
    # insert working cell 
    add_dfc_cell(MARKDOWN,DC_WORKING_TITLE)
    add_dfc_cell(CODE,DC_WORKING)
    add_dfc_cell(MARKDOWN,DC_BLANK_LINE)
    
    from dfcleanser.common.cfg import get_notebook_name, get_notebook_path
    get_notebook_name()
    get_notebook_path()
    
    clock = RunningClock()
    clock.start()
    
    from dfcleanser.data_cleansing.data_cleansing_control import clear_data_cleansing_data
    clear_data_cleansing_data()

    from dfcleanser.data_export.data_export_control import clear_data_export_data
    clear_data_export_data()

    from dfcleanser.data_import.data_import_control import clear_data_import_data
    clear_data_import_data()

    from dfcleanser.data_inspection.data_inspection_control import clear_data_inspection_data
    clear_data_inspection_data()

    from dfcleanser.data_transform.data_transform_control import clear_data_transform_data
    clear_data_transform_data()

    from dfcleanser.sw_utilities.genfunc_control import clear_gen_function_data
    clear_gen_function_data()

    from dfcleanser.scripting.data_scripting_control import clear_data_scripting_data
    clear_data_scripting_data()

    from dfcleanser.sw_utilities.sw_utility_geocode_control import clear_sw_utility_geocodedata
    clear_sw_utility_geocodedata()

    from dfcleanser.sw_utilities.sw_utility_dfsubset_control import clear_sw_utility_dfsubsetdata
    clear_sw_utility_dfsubsetdata()
    
    clock.stop()
    
    print("* dfcleanser modules found successfully")
    print("\n")
    print("* Please review the functions in the System Environment taskbar below.")
    print("* dfcleanser Chapters allows you to determine which dfcleanser modules to display upon dfcleanser load.")
    print("* Please read the EULA before doing anything in dfcleanser")
    print("* Once you are done with setup hit the Exit Setup button.")
    print("* To run dfcleanser within your notebook run load_dfcleanser from dfcleanser.system.load")
    print("\n")








   