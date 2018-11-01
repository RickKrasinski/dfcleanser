 

"use strict";

//
// 
// ------------------------------------------------------
// Dataframe Cleanser javascript utilities 
// ------------------------------------------------------
// 
//
window.debug_flag       = true;
window.debug_dev_flag   = false;

window.NEW_LINE = "\n";

//
// ---------------------------------------------------
// Dataframe Cleanser python libraries
// ---------------------------------------------------
//
window.SYSTEM_LIB               = "from dfcleanser.system.system_control import ";
window.COMMON_LIB               = "from dfcleanser.common.common_utils import ";
window.INSPECTION_LIB           = "from dfcleanser.data_inspection.data_inspection_control import ";
window.CLEANSING_LIB            = "from dfcleanser.data_cleansing.data_cleansing_control import ";
window.TRANSFORM_LIB            = "from dfcleanser.data_transform.data_transform_control import ";
window.IMPORT_LIB               = "from dfcleanser.data_import.data_import_control import ";
window.EXPORT_LIB               = "from dfcleanser.data_export.data_export_control import ";
window.SCRIPT_LIB               = "from dfcleanser.scripting.data_scripting_control import ";
window.SW_UTILS_LIB             = "from dfcleanser.sw_utilities.sw_utility_control import ";
window.GEN_FUNCTION_LIB         = "from dfcleanser.sw_utilities.sw_utility_genfunc_control import ";
window.SW_UTILS_GEOCODE_LIB     = "from dfcleanser.sw_utilities.sw_utility_geocode_control import ";
window.SW_UTILS_DFSUBSET_LIB    = "from dfcleanser.sw_utilities.sw_utility_dfsubset_control import ";
window.SW_UTILS_DFCONCAT_LIB    = "from dfcleanser.sw_utilities.sw_utility_dfconcat_control import ";
window.CFG_LIB                  = "from dfcleanser.common.cfg import ";
window.HELP_LIB                 = "from dfcleanser.common.help_utils import ";

window.OS_LIB                   = "from os import ";

//
// ---------------------------------------------------
// Dataframe Cleanser jupyter cell ids
// ---------------------------------------------------
//
window.DC_TITLE_ID                          = 0;
window.DC_SYSTEM_ID                         = 1;
window.DC_DATA_IMPORT_ID                    = 2;
window.DC_DATA_INSPECTION_ID                = 3;
window.DC_DATA_CLEANSING_ID                 = 4;
window.DC_DATA_TRANSFORM_ID                 = 5;
window.DC_DATA_EXPORT_ID                    = 6;
window.DC_SW_UTILITIES_ID                   = 7;
window.DC_DATASTRUCT_UTILITY_ID             = 8;
window.DC_GENFUNC_UTILITY_ID                = 9;
window.DC_GEOCODE_UTILITY_ID                = 10;
window.DC_DFSUBSET_UTILITY_ID               = 11;
window.DC_DFCONCAT_UTILITY_ID               = 12;
window.DC_SCRIPTING_ID                      = 13;
window.DC_DATA_SCRIPT_ID                    = 14;
window.DC_WORKING_ID                        = 15;

window.SYSTEM_TASK_BAR_ID                   = 16;
window.IMPORT_TASK_BAR_ID                   = 17;
window.IMPORT_CUSTOM_CODE_ID                = 18;
window.INSPECTION_TASK_BAR_ID               = 19;
window.CLEANSING_TASK_BAR_ID                = 20;
window.TRANSFORM_TASK_BAR_ID                = 21;
window.TRANSFORM_ADD_COLUMN_ID              = 22;
window.EXPORT_TASK_BAR_ID                   = 23;
window.EXPORT_CUSTOM_CODE_ID                = 24;
window.SW_UTILS_DATASTRUCT_TASK_BAR_ID      = 25;
window.SW_UTILS_GENFUNC_TASK_BAR_ID         = 26;
window.SW_UTILS_GENFUNC_CODECELL_ID         = 27;
window.SW_UTILS_GEOCODE_TASK_BAR_ID         = 28;
window.SW_UTILS_DFSUBSET_TASK_BAR_ID        = 29;
window.SW_UTILS_DFCONCAT_TASK_BAR_ID        = 30;
window.SCRIPT_TASK_BAR_ID                   = 31;
window.WORKING_CELL_ID                      = 32;

const DC_BLANK_LINE_ID                      = 1000;

const MIN_CELL_ID = DC_TITLE_ID;
const MAX_CELL_ID = WORKING_CELL_ID;
const total_ids = ((MAX_CELL_ID - MIN_CELL_ID) + 1);

const WORKING_CELL = "# Working Cell "

window.empty_cell_id = null;

var dfc_cell_ids = ["PandasdfcleanserTitle","DCSystemTitle","DCDataImportTitle","DCDataInspectionTitle","DCDataCleansingTitle",
                    "DCDataTransformTitle","DCDataExportTitle","SWUtilities","DCListUtilityTitle","DCGenFunctionUtilityTitle",
                    "DCGeocodeUtilityTitle","DCDFSubsetUtilityTitle","DCDFConcatUtilityTitle","ScriptingMode","DCDataScriptingTitle","DCWorkingTitle",
                    "DCSystem","DCDataImport","DCDataImportCustom","DCDataInspection","DCDataCleansing","DCDataTransform",
                    "DCDataTransformAddCol","DCDataExport","DCDataExportCustom","DCListUtility","DCGenFunctionUtility",
                    "DCGenFunctionCodeCell","DCGeocodeUtility","DCDFSubsetUtility","DCDFConcatUtility","DCDataScripting","DCWorking"];

window.get_dfc_cellid_for_cell_id = function(cellid) {
    return(dfc_cell_ids[cellid]);
};

//
// ---------------------------------------------------
// dataframe cleanser initialization method
// ---------------------------------------------------
//
window.initialize_dc = function() {

    // get the current cells 
    var cells       =   IPython.notebook.get_cells();
    var cellText    =   "";
    var nbbcellId   =   null;

    window.run_code_in_cell(window.SYSTEM_TASK_BAR_ID,window.getJSPCode(window.SYSTEM_LIB,"display_system_environment","0"));
    window.delete_output_cell(window.IMPORT_CUSTOM_CODE_ID);
    window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"display_import_forms","0"));
    window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID,window.getJSPCode(window.INSPECTION_LIB,"display_data_inspection","0"));
    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID,window.getJSPCode(window.CLEANSING_LIB,"display_data_cleansing","0"));
    window.delete_output_cell(window.TRANSFORM_ADD_COLUMN_ID);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID,window.getJSPCode(window.TRANSFORM_LIB,"display_data_transform","0"));
    window.delete_output_cell(window.EXPORT_CUSTOM_CODE_ID);
    window.run_code_in_cell(window.EXPORT_TASK_BAR_ID,window.getJSPCode(window.EXPORT_LIB,"display_export_forms","0"));
    window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_LIB,"process_sw_utilities","0"));
    window.delete_output_cell(window.SW_UTILS_GENFUNC_CODECELL_ID);
    window.run_code_in_cell(window.SW_UTILS_GENFUNC_TASK_BAR_ID,window.getJSPCode(window.GEN_FUNCTION_LIB,"display_gen_function","0"));
    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_GEOCODE_LIB,"display_geocode_utility","0"));
    window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB,"display_dfsubset_utility","0"));
    window.run_code_in_cell(window.SW_UTILS_DFCONCAT_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFCONCAT_LIB, "display_dfconcat_utility", "0"));
    window.run_code_in_cell(window.SCRIPT_TASK_BAR_ID,window.getJSPCode(window.SCRIPT_LIB,"display_data_scripting","0"));
    
    var workingcell = get_cell_for_id(WORKING_CELL_ID);
    if(workingcell != null)
        workingcell.set_text(WORKING_CELL + "- please do not remove");
};

// -------------------------------------------------------
// get notebook cell object for the logical cell id
// ------------------------------------------------------
//      cellId - logical cell index
//      return : notebook cell object for logical id
// -------------------------------------------------------
window.get_cell_for_id = function(cellId) {
    // get the current cells 
    var cells = IPython.notebook.get_cells();
    var cell = null;

    // search through the cells 
    for (var i = 0; i < (IPython.notebook.ncells()); i++) {
        cell = cells[i];
        var cellIndex = IPython.notebook.find_cell_index(cell);

        // check that cell index is valid
        if (IPython.notebook.is_valid_cell_index(cellIndex)) {
            // get the cell metadata 
            var cell_mdata = cell.metadata;

            if (cell_mdata != undefined) {
                if ("dfcleanser_metadata" in cell_mdata) {
                    var dfc_cell_mdata = cell_mdata["dfcleanser_metadata"];
                    if ("dfc_cellid" in dfc_cell_mdata) {
                        var dfc_cell_id = dfc_cell_mdata["dfc_cellid"];
                        if (get_dfc_cellid_for_cell_id(cellId) == dfc_cell_id)
                            return (cell);
                    }
                }
            }
        }
        cell = null;
    }
    return (cell);
};

// -------------------------------------------------------
// get notebook cell object before the logical cell id
// ------------------------------------------------------
//      cellId - logical cell index
//      return : notebook cell object for logical id
// -------------------------------------------------------
window.get_cell_for_before_id = function(cellId) {

    console.log("get_cell_for_before_id",cellId);
    
    // get the current cells 
    var cells       = IPython.notebook.get_cells();
    var cell        = null;
    var prev_cell   = null;

    // search through the cells 
    for (var i = 0; i < (IPython.notebook.ncells()); i++) {
        cell = cells[i];
        var cellIndex = IPython.notebook.find_cell_index(cell);

        // check that cell index is valid
        if (IPython.notebook.is_valid_cell_index(cellIndex)) {
            // get the cell metadata 
            var cell_mdata = cell.metadata;
            console.log("get_cell_for_before_id["i,"]",cell_mdata);
            if (cell_mdata != undefined) {
                if ("dfcleanser_metadata" in cell_mdata) {
                    var dfc_cell_mdata = cell_mdata["dfcleanser_metadata"];
                    if ("dfc_cellid" in dfc_cell_mdata) {
                        var dfc_cell_id = dfc_cell_mdata["dfc_cellid"];
                        if (dfc_cell_id == cellId){
                            console.log("found prev_cell",prev_cell.metadata);
                            return (prev_cell);
                        }
                        else {
                            prev_cell = cell;
                            console.log("prev_cell",prev_cell.metadata);
                        }
                    }
                }
            }
        }
        cell = null;
    }
    console.log("end - get_cell_for_before_id",cellId);

    return (cell);
};

// -------------------------------------------------------
// set the cell pointed to by logical id 
// as the currently selected ipyhton cell with focus
// -------------------------------------------------------
window.select_cell = function(id) {
    var cell_to_select = window.get_cell_for_id(id);
    select_current_cell(cell_to_select);
};

window.select_before_cell = function(id) {
    var cell_to_select = window.get_cell_for_before_id(id);
    select_current_cell(cell_to_select);
};

// -------------------------------------------------------
// set the cell pointed to by logical id 
// as the currently selected ipyhton cell with focus
// -------------------------------------------------------
window.select_current_cell = function(cell_to_select) {
    var cellIndex = IPython.notebook.find_cell_index(cell_to_select);
    IPython.notebook.select(cellIndex, true);
    IPython.notebook.focus_cell();
    cell_to_select.select(true);
};

// -------------------------------------------------------
// set the cell based on metadata 
// -------------------------------------------------------
window.select_cell_from_metadata = function(metadata,offset=0) {
    var cells       =   IPython.notebook.get_cells();
    var cellIndex   =   null;
    
    for (var i=0; i < (IPython.notebook.ncells()); i++){
        var cell        =   cells[i];
        var cmdata      =   cell.metadata;
        var dfc_mdata   =   cmdata["dfcleanser_metadata"];

        if(dfc_mdata != undefined){    
            var dfc_cell_id     =   dfc_mdata["dfc_cellid"];
            
            if(dfc_cell_id == metadata){
                for (var j=0; j < offset; j++){
                    cell = cells[i+j+1];//IPython.notebook.select_next().get_selected_cell();
                    select_current_cell(cell);
                }
                select_current_cell(cell);
                return(cell);
            }
        }
    }
};

// -------------------------------------------------------
// set the cell based on text 
// -------------------------------------------------------
window.select_cell_from_text = function(text) {
    var cells   =   IPython.notebook.get_cells();
    
    for (var i=0; i < (IPython.notebook.ncells()); i++){
        var cell        =   cells[i];
        var ctext       =   cell.get_text();

        if(ctext != undefined) {
            if(containsSubstring(ctext,text)){
                var cellIndex   =   IPython.notebook.find_cell_index(cell);
                IPython.notebook.select(cellIndex, true);
                IPython.notebook.focus_cell();
                cell.select(true);
                return(true);
            }
        }
    }
    return(false);
};

//
// ---------------------------------------------------
// cell control functions 
// ---------------------------------------------------
//

// -------------------------------------------------------
// delete the cell pointed to by logical id
// ------------------------------------------------------
//      id - logical cell to delete
// -------------------------------------------------------
window.delete_output_cell = function(id) {
    var cell_to_delete      =   null;
    var cell_to_return_to   =   null;
    cell_to_delete          =   window.get_cell_for_id(id);

    if (cell_to_delete != window.empty_cell_id) {
        select_cell(id);
        cell_to_return_to = IPython.notebook.select_next().get_selected_cell()
        IPython.notebook.delete_cell(IPython.notebook.find_cell_index(cell_to_delete));
    }
    IPython.notebook.select(cell_to_return_to);
};

// -------------------------------------------------------
// run code in specified cell
// ------------------------------------------------------
///      id      -   logical nbb cell id ro run in 
//      code    -   code to run in cell
// -------------------------------------------------------
window.run_code_in_cell = function(id, code) {
    var runCell = window.get_cell_for_id(id);
    var runCode = code;

    if (runCell != null) {
        if (id == window.WORKING_CELL_ID) {
            runCode = WORKING_CELL + "- please do not remove" + NEW_LINE + code;
            run_code(runCell, runCode);
        } else { run_code(runCell, runCode); }
    } else { if (window.debug_dev_flag) console.log("  [Cell to run in not found]", id, code, id); }
};

// -------------------------------------------------------
// insert a new cell below current cell and run code
// ------------------------------------------------------
//      id          -   logical nbb cell id to run below 
//      outputid    -   logical nbb cell id for new cell 
//      code        -   code to run in cell
// -------------------------------------------------------
window.insert_cell_and_run_code_in_output_cell = function(id, outputid, code) {
    window.delete_output_cell(outputid);
    window.select_cell(id);
    IPython.notebook.insert_cell_below('code');
    var cell = IPython.notebook.select_next().get_selected_cell();
    window.run_code(cell, code);
    if (window.debug_dev_flag) {console.log("\n    [insert_cell_and_run_code_in_output_cell][end]");}
};

// -------------------------------------------------------
// clear the output of a cell by the logical id
// ------------------------------------------------------
//      id          -   logical cell id to run below 
// -------------------------------------------------------
window.clear_cell_output = function(id) {
    var cell_to_clear = window.get_cell_for_id(id);
    if (cell_to_clear != window.empty_cell_id) { IPython.notebook.clear_output(IPython.notebook.find_cell_index(cell_to_clear)); } 
    else { if(window.debug_dev_flag) console.log("   [unable to clear cell for] : " + id.toString()); }
};

const   MARKDOWN    =   0
const   CODE        =   1

// -------------------------------------------------------
// add a dfcleanser cell to the notebook
// ------------------------------------------------------
//      ctype          -   cell type 
//      ctext          -   cell text
//      dfcid          -   cell metadata id 
// -------------------------------------------------------
window.add_dfc_cell = function(ctype, ctext, dfcid, afterid = -1) {
    if(window.debug_dev_flag) 
        console.log("\nadd_dfc_cell", ctype, ctext, dfcid, afterid);
       
    // if first cell to load find correct 
    // cell to start loading after
    if (afterid != -1) {
        select_cell(afterid);
    }
        
    if(ctype == CODE) {IPython.notebook.insert_cell_below('code');}
    else {IPython.notebook.insert_cell_below('markdown');}

    var cell_to_add = IPython.notebook.select_next().get_selected_cell();
    cell_to_add.set_text(ctext);
    
    // add the cellid metadata
    var dfcellDict          =   { "dfc_cellid": dfcid };
    var dfcleanserDict      =   { "dfcleanser_metadata": dfcellDict };
    var newcellDict         =   {"trusted":true, "dfcleanser_metadata": dfcellDict};
    cell_to_add.metadata    =   newcellDict;//dfcleanserDict;
    
    if (ctype == MARKDOWN) {cell_to_add.execute();}
    else {cell_to_add.execute();}
};

// -------------------------------------------------------
// find the number of dfcleanser cells
// -------------------------------------------------------
window.get_num_dfcleanser_cells = function(){

    var cells               =   IPython.notebook.get_cells();
    var total_dfc_cells     =   0;
    
    for (var i=0; i < (IPython.notebook.ncells()); i++){
        var cell        =   cells[i];
        var cmdata      =   cell.metadata;
        var dfc_mdata   =   cmdata["dfcleanser_metadata"];

        if(dfc_mdata != undefined){total_dfc_cells++;}
    }
    return(total_dfc_cells);
};

// -------------------------------------------------------
// get the metadata for a dfc cell
// -------------------------------------------------------
//   cell - notebook cell
// -------------------------------------------------------
window.get_dfc_metadata = function(cell) {
    var cmdata      =   cell.metadata;
    var dfc_mdata   =   cmdata["dfcleanser_metadata"];
    if(dfc_mdata != undefined) return(dfc_mdata);
    else return(undefined);
}

// -------------------------------------------------------
// delete the dfc chapter
// ------------------------------------------------------
//   chaptertitle - dfc chapter to delete
// -------------------------------------------------------
window.delete_dfc_chapter = function(chaptertitle) {

    console.log("delete_dfc_chapter",chaptertitle);

    var cell_to_delete  =   null;
    var next_cell       =   null;
    cell_to_delete      =   select_cell_from_metadata(chaptertitle)
    
    // delete the title cell
    if (cell_to_delete != window.empty_cell_id) {
        select_current_cell(cell_to_delete);
        next_cell = IPython.notebook.select_next().get_selected_cell();
        IPython.notebook.delete_cell(IPython.notebook.find_cell_index(cell_to_delete));
    }
    
    // delete the help cell 
    cell_to_delete  =   next_cell;
    select_current_cell(cell_to_delete);
    next_cell       =   IPython.notebook.select_next().get_selected_cell();   
    
    var dfc_metadata    =   get_dfc_metadata(cell_to_delete);
       
    if( dfc_metadata != undefined){
        dfcid   =   dfc_metadata["dfc_cellid"];
        if(dfcid != undefined){
            if(containsSubstring(dfcid,"Help"))
                IPython.notebook.delete_cell(IPython.notebook.find_cell_index(cell_to_delete));            
            else 
                next_cell = cell_to_delete;
        }
    }
    
    // delete the code cell 
    cell_to_delete  =   next_cell;
    select_current_cell(cell_to_delete);
    next_cell       =   IPython.notebook.select_next().get_selected_cell();   
    var dfc_codetext    =   cell_to_delete.get_text();
       
    if(containsSubstring(dfc_codetext,"from dfcleanser."))
        IPython.notebook.delete_cell(IPython.notebook.find_cell_index(cell_to_delete));            
    else 
        next_cell = cell_to_delete; 
           
    // delete the blank line cell 
    cell_to_delete  =   next_cell;
    select_current_cell(cell_to_delete);
    next_cell       =   IPython.notebook.select_next().get_selected_cell();   
    
    dfc_metadata    =   get_dfc_metadata(cell_to_delete);
       
    if( dfc_metadata != undefined){
        var dfcid   =   dfc_metadata["dfc_cellid"];
        if(dfcid != undefined){
            if(containsSubstring(dfcid,"DCBlankline"))
                IPython.notebook.delete_cell(IPython.notebook.find_cell_index(cell_to_delete));            
        }
    }
    
    IPython.notebook.select(next_cell);
};

// -------------------------------------------------------
// delete dfcleanser cells
// -------------------------------------------------------
window.delete_dfcleanser_cells = function(){
    var cells       =   IPython.notebook.get_cells();
    var cell        =   window.empty_cell_id;
    
    // search through the cells 
    for (var i=0; i < (IPython.notebook.ncells()); i++){
        cell            =   cells[i];
        var cmdata      =   cell.metadata;
        var dfc_mdata   =   cmdata["dfcleanser_metadata"];

        if(dfc_mdata != undefined){
            var cellIndex   =   IPython.notebook.find_cell_index(cell);
            IPython.notebook.select(cellIndex, true);
            IPython.notebook.focus_cell();
            cell.select(true);
            IPython.notebook.delete_cell(cellIndex);
        } 
    }
};

window.WORKING_CODE_CELL           =   '# working cell- please do not remove';
window.WORKING_TITLE_CELL          =   '<div align="left" id="Restricted"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/Restricted.jpg" width="80" align="left"/></div><div><image width="10"></div><div><image width="10"><h2>&nbsp;&nbsp;&nbsp;Restricted</h2></div></div>';
window.WORKING_BLANK_LINE          =   '<br></br>';

// -------------------------------------------------------
// load dfcleanser cells from toolbar
// ------------------------------------------------------
window.load_dfcleanser_from_toolbar = function(){

    add_dfc_cell(MARKDOWN,window.WORKING_BLANK_LINE,'DCBlankline',-1);
    add_dfc_cell(MARKDOWN,window.WORKING_TITLE_CELL,'DCWorkingTitle',-1);
    add_dfc_cell(CODE,window.WORKING_CODE_CELL,'DCWorking',-1);
    add_dfc_cell(MARKDOWN,window.WORKING_BLANK_LINE,'DCBlankline',-1);

    window.getNotebookLocation();
    
    window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSCode(window.SYSTEM_LIB, "load_dfcleanser_from_toolbar"));
       
}    
    
   
// -------------------------------------------------------
// unload dfcleanser cells
// ------------------------------------------------------
window.unload_dfcleanser = function(){
    var     max_trys    =   3;
    var     ctry        =   0;
    
    while(ctry < max_trys){
        if(get_num_dfcleanser_cells() > 0){
            ctry++;
            delete_dfcleanser_cells();
        }
        else {ctry    =   max_trys;}    
    }
};

// -------------------------------------------------------
// run code in noteboook cell
// ------------------------------------------------------
//
//      cell          -   noteboook cell to run code in 
//      code          -   code to run in cell 
//
// -------------------------------------------------------
window.run_code = function(cell, code) {
    cell.set_text(code);
    cell.execute();
};

// -------------------------------------------------------
// set code cell content
// ------------------------------------------------------
//
//      cell          -   noteboook cell to run code in 
//      code          -   code to run in cell 
//
// -------------------------------------------------------
window.set_code = function(id, code) {
    var Cell = window.get_cell_for_id(id);
    Cell.set_text(code);
};

// -------------------------------------------------------
// reset dependent cells when code cell changes
// impact other chapters in notebook
// ------------------------------------------------------
//
//      deplist       -   list of chapters to update 
//
// -------------------------------------------------------
window.reset_dependents = function(deplist) {

    if (deplist[0]) {
        window.delete_output_cell(window.IMPORT_CUSTOM_CODE_ID);
        window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"display_import_forms","0"));
    }
    if (deplist[1]) {window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID,window.getJSPCode(window.INSPECTION_LIB,"display_data_inspection","0"));}
    if (deplist[2]) {window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID,window.getJSPCode(window.CLEANSING_LIB,"display_data_cleansing","0"));}
    if (deplist[3]) {window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID,window.getJSPCode(window.TRANSFORM_LIB,"display_data_transform","0"));}
    if (deplist[4]) {
        window.delete_output_cell(window.EXPORT_CUSTOM_CODE_ID);
        window.run_code_in_cell(window.EXPORT_TASK_BAR_ID,window.getJSPCode(window.EXPORT_LIB,"display_export_forms","0"));
    }
    if (deplist[5]) {window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB,"display_dfsubset_utility","0"));}
};

//
// ---------------------------------------------------
// ---------------------------------------------------
// common uility functions
// ---------------------------------------------------
// ---------------------------------------------------
//

//
// check if string contains a substring
//
function containsSubstring(instr, insubstr) {
    var flag = instr.indexOf(insubstr);
    if (flag == -1) return (false);
    else return (true);
}

//
//
// ---------------------------------------------------
// helper functions for running python methods from js
// ---------------------------------------------------
// 
//
window.getJCode = function(code) {
    return (code + NEW_LINE);
};
window.getJSCode = function(lib, call) {
    return (lib + call + NEW_LINE + call + "()");
};
window.getJSPCode = function(lib, call, parm) {
    return (lib + call + NEW_LINE + call + "(" + parm + ")");
};

//
// check if element has attribute
//
window.has_Attribute = function(elem, cattr) {
    var cattr = elem.attr(cattr);
    if (typeof cattr !== typeof undefined && cattr !== false) return (true);
    else return (false);
};

//
// scroll to a chapter in the notebook
//
window.scroll_to = function(anchor) {
    var element_to_scroll_to = document.getElementById(anchor);
    if(element_to_scroll_to != null) element_to_scroll_to.scrollIntoView();
};

//
//
// ---------------------------------------------------
// helper functions for getting form input data
// ---------------------------------------------------
// 
//

// 
// Common get values for checkboxes
// 
window.getcheckboxValues = function(id) {
    var formd = document.getElementById(id);

    if (formd == null) {
        if(window.debug_dev_flag) console.log("no checkbox ", id, " not found");
        return (null);
    }

    var inputs = new Array();
    $('#' + id + ' :input').each(function() {
        var type = $(this).attr("type");
        if (type == "checkbox")
            var id = $(this).attr("id");
        if ($(this).is(':checked')) {inputs.push("True");}
        else {inputs.push("False");}
    });
    return (JSON.stringify(inputs));
};

// 
// Common get values for radios
// 
window.getradioValues = function(id) {
    var formd = document.getElementById(id);

    if (formd == null) {
        if(window.debug_dev_flag) console.log("no radio ", id, " not found");
        return (null);
    }

    var inputs = new Array();
    var total_found = -1;
    var found_at = -1;

    $('#' + id + ' :input').each(function() {
        total_found = total_found + 1;
        var type = $(this).attr("type");
        if (type == "radio")
            var id = $(this).attr("id");
        if ($(this).is(':checked')) {
            found_at = total_found;
        }
    });
    inputs.push(found_at);
    return (JSON.stringify(found_at));
};

// 
// Common get value for dropdown
// 
window.getdropdownValues = function(id) {
    var formd = document.getElementById(id);

    if (formd == null) {
        return (null);
    }

    var inputs = new Array();
    var total_found = -1;
    var found_at = -1;

    $('#' + id + ' option').each(function() {
        total_found = total_found + 1;
        var sel = $(this).prop("selected");
        if (sel == true) {
            found_at = total_found;
        }
    });
    inputs.push(found_at);
    return (JSON.stringify(found_at));
};

// 
// Common get values for input forms
// 
window.get_input_form_parms = function(id) {

    var inputs = new Array();
    var ids = new Array();

    $('#' + id + ' :input').each(function() {
        var type = $(this).attr("type");
        if (type != "file") {
            if (String($(this).val()).length > 0) {
                inputs.push(String($(this).val()));
                ids.push(String($(this).attr("id")));
            }
        }
    });

    var parms = new Array();
    parms.push(ids);
    parms.push(inputs);

    return (JSON.stringify(parms));
};

// 
// Common get labels for input forms
// 
window.get_input_form_labels = function(id) {

    var inputs = new Array();
    $('#' + id + ' :input').each(function() {
        var $element = $(this)
        var $label = $("label[for='" + $element.attr('id') + "']")
        inputs.push(String($label.text()));
    });

    return (JSON.stringify(inputs));
};

//
// functions to request a full list of parms for an inout form
//
window.getfullparms = function(inputid) {
    var inputs = new Array();
    inputs.push(String(inputid));
    window.run_code_in_cell(window.WORKING_CELL_ID,window.getJSPCode(window.COMMON_LIB,"get_fullparms",JSON.stringify(inputs)));
}

//
// ---------------------------------------------------
// file selection directory - dirs restricted to local only
// Note : adhere to the browser security usage of fakepath
// ---------------------------------------------------
// 
window.onChangefileselect = function(inputid, fileid) {
    if (window.debug_flag) {
        console.log("[onChangefileselect]");
        console.log("  [inputid] [", inputid, "] ", inputid.value);
        console.log("  [inputid.id] [", inputid, "] ", inputid.id);
        console.log("  [fileid ] [", fileid, "] ", fileid.value);
    }

    if (inputid.id == "csvFileName")
        inputid.value = fileid.value.replace("C:\\fakepath\\", "datasets/");
    else
        if ((inputid.id == "startlistfile") || (inputid.id == "listfilename"))
            inputid.value = fileid.value.replace("C:\\fakepath\\", "lists/");
        else
            if ((inputid.id == "startdictfile") || (inputid.id == "dictfilename"))
                inputid.value = fileid.value.replace("C:\\fakepath\\", "dicts/");
            else
                inputid.value = fileid.value.replace("C:\\fakepath\\", "datasets/");
};

//
// ---------------------------------------------------
// common functions for jupyter to get notebook info 
// via javascript calls
// ---------------------------------------------------
//

//
// get the current notebook location
// 
window.getNotebookLocation = function() {
    window.getNotebookPath();
    window.getNotebookName();
};

//
// get the current notebook name
// 
window.getNotebookName = function() {
    var nbname = IPython.notebook.get_notebook_name();

    if (window.get_cell_for_id(window.WORKING_CELL_ID) == null) {
        window.add_dfc_cell(1, "# Temporary Working Cell", "DCWorking");
        window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.CFG_LIB, "set_notebookName", JSON.stringify(nbname)));
        window.delete_output_cell(window.WORKING_CELL_ID);
    } else {
        window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.CFG_LIB, "set_notebookName", JSON.stringify(nbname)));
    }
};

//
// get the current notebook path
// 
window.getNotebookPath = function() {
    var code = "dcpath = %pwd" + NEW_LINE;
    code = code + "from dfcleanser.common.cfg import set_notebookPath" + NEW_LINE;
    code = code + "set_notebookPath(dcpath)";
    if (window.get_cell_for_id(window.WORKING_CELL_ID) == null) {
        window.add_dfc_cell(1, "# Temporary Working Cell", "DCWorking");
        window.run_code_in_cell(window.WORKING_CELL_ID, code);
        window.delete_output_cell(window.WORKING_CELL_ID);
    } else {
        window.run_code_in_cell(window.WORKING_CELL_ID, code);
    }
};

window.is_dfcleanser_loaded = function(){
    
    var cells = IPython.notebook.get_cells();

    // search through the cells 
    for (var i = 0; i < (IPython.notebook.ncells()); i++) {

        var cell = cells[i];
        var cmdata = cell.metadata;
        var dfc_mdata = cmdata["dfcleanser_metadata"];

        if (dfc_mdata != undefined) {return(true);}
    }

    return(false);
};

//
// set which dfc cells just got loaded
// 
window.getdfCChaptersLoaded = function() {

    var cells = IPython.notebook.get_cells();
    var cell = window.empty_cell_id;
    var cellsloaded = [];

    // search through the cells 
    for (var i = 0; i < (IPython.notebook.ncells()); i++) {

        cell = cells[i];
        var cmdata = cell.metadata;
        var dfc_mdata = cmdata["dfcleanser_metadata"];

        if (dfc_mdata != undefined) {
            if (dfc_mdata["dfc_cellid"] != "DCBlankline")
                cellsloaded.push(dfc_mdata["dfc_cellid"]);
        }
    }

    var chaptersloaded = [];

    for (var i = 16; i < dfc_cell_ids.length; i++) {

        var found = 0;
        for (var j = 0; j < cellsloaded.length; j++) {
            if (cellsloaded[j] == dfc_cell_ids[i])
                found = 1;
        }
        chaptersloaded.push(found);
    }

    window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.CFG_LIB, "set_chapters_loaded", JSON.stringify(chaptersloaded)));
};


//
//
// -----------------------------------------------------
// functions for scrolling tables in dataframe cleanser
// -----------------------------------------------------
// 
//
window.scrollSampleRow = function(tableid, direction) {
    var inputs = new Array();
    inputs.push(String(tableid));
    inputs.push(String(direction));
    window.run_code_in_cell(window.WORKING_CELL_ID,window.getJSPCode(window.COMMON_LIB,"scroll_sample_rows",JSON.stringify(inputs)));
};
window.scrollSingleRow = function(tableid, direction) {
    var inputs = new Array();
    inputs.push(String(tableid));
    inputs.push(String(direction));
    window.run_code_in_cell(window.WORKING_CELL_ID,window.getJSPCode(window.COMMON_LIB,"scroll_single_row",JSON.stringify(inputs)));
};
window.scrollTable = function(tableid, direction) {
    var inputs = new Array();

    if (tableid == "dfschemaTable") {
        inputs.push([3, direction])
        window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0" + "," + JSON.stringify(inputs)));
        window.scroll_to('DCDataTransform');
        return;
    }

    inputs.push(String(tableid));
    inputs.push(String(direction));
    window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "scroll_table", JSON.stringify(inputs)));
};

//
// display a sample row for a table
//
function getSampleRow(tableid) {
    var element = document.getElementById(tableid + "InputId");

    if (element.value.length > 0) {
        var fparms = [tableid, element.value];
        var inputs = new Array();
        inputs.push(fparms);
        window.run_code_in_cell(window.WORKING_CELL_ID,window.getJSPCode(window.COMMON_LIB,"get_sample_row",JSON.stringify(inputs)));
    }
}

//
//
// ---------------------------------------------------
// common help functions
// ---------------------------------------------------
//
//

//
// display help section by dfc hrlp id
//
window.displayhelp = function(helpid) {

    var url     =   "https://rickkrasinski.github.io/dfcleanser/html/help/dfcleanser_help#dfc_" + String(helpid);
    window.open(url);
}

//
// display help by url
//
window.display_help_url = function(url) {
    window.run_code_in_cell(window.WORKING_CELL_ID,window.getJSPCode(window.COMMON_LIB,"display_url",JSON.stringify(url)));
    return true;
};
