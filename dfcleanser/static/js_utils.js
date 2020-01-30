 "use strict";

 //
 // 
 // ------------------------------------------------------
 // Dataframe Cleanser javascript utilities 
 // ------------------------------------------------------
 // 
 //
 window.debug_flag = true;
 window.debug_detail_flag = false;


 window.BASIC_DEBUG = 0
 window.DETAIL_DEBUG = 1

 window.log_prefix = '[' + "dfcleanser" + ']';


 window.dfc_log = function(message, type = BASIC_DEBUG) {

     if (type == BASIC_DEBUG) {
         if (window.debug_flag)
             console.log(log_prefix + "\n    " + message);
     } else {
         if (window.debug_detail_flag)
             console.log(log_prefix + "\n    " + message);
     }
 };


 window.NEW_LINE = "\n";

 //
 // ---------------------------------------------------
 // Dataframe Cleanser python libraries
 // ---------------------------------------------------
 //
 window.SYSTEM_LIB = "from dfcleanser.system.system_control import ";
 window.COMMON_LIB = "from dfcleanser.common.common_utils import ";
 window.INSPECTION_LIB = "from dfcleanser.data_inspection.data_inspection_control import ";
 window.CLEANSING_LIB = "from dfcleanser.data_cleansing.data_cleansing_control import ";
 window.TRANSFORM_LIB = "from dfcleanser.data_transform.data_transform_control import ";
 window.IMPORT_LIB = "from dfcleanser.data_import.data_import_control import ";
 window.EXPORT_LIB = "from dfcleanser.data_export.data_export_control import ";
 window.SCRIPT_LIB = "from dfcleanser.scripting.data_scripting_control import ";
 window.SW_UTILS_LIB = "from dfcleanser.sw_utilities.sw_utility_control import ";
 window.SW_UTILS_GEOCODE_LIB = "from dfcleanser.sw_utilities.sw_utility_geocode_control import ";
 window.SW_UTILS_DFSUBSET_LIB = "from dfcleanser.sw_utilities.sw_utility_dfsubset_control import ";
 window.SW_UTILS_CENSUS_LIB = "from dfcleanser.sw_utilities.sw_utility_census_control import ";
 window.CFG_LIB = "from dfcleanser.common.cfg import ";
 window.HELP_LIB = "from dfcleanser.common.help_utils import ";

 window.OS_LIB = "from os import ";

 //
 // ---------------------------------------------------
 // Dataframe Cleanser jupyter cell ids
 // ---------------------------------------------------
 //
 window.DC_TITLE_ID = 0;
 window.DC_SYSTEM_ID = 1;
 window.DC_DATA_IMPORT_ID = 2;
 window.DC_DATA_INSPECTION_ID = 3;
 window.DC_DATA_CLEANSING_ID = 4;
 window.DC_DATA_TRANSFORM_ID = 5;
 window.DC_DATA_EXPORT_ID = 6;
 window.DC_SW_UTILITIES_ID = 7;
 window.DC_DATASTRUCT_UTILITY_ID = 8;
 window.DC_GEOCODE_UTILITY_ID = 9;
 window.DC_DFSUBSET_UTILITY_ID = 10;
 window.DC_CENSUS_ID = 11;
 window.DC_DATA_SCRIPT_ID = 12;
 window.DC_WORKING_ID = 13;

 window.SYSTEM_TASK_BAR_ID = 14;
 window.IMPORT_TASK_BAR_ID = 15;
 window.INSPECTION_TASK_BAR_ID = 16;
 window.CLEANSING_TASK_BAR_ID = 17;
 window.TRANSFORM_TASK_BAR_ID = 18;
 window.EXPORT_TASK_BAR_ID = 19;
 window.SW_UTILS_DATASTRUCT_TASK_BAR_ID = 20;
 window.SW_UTILS_GEOCODE_TASK_BAR_ID = 21;
 window.SW_UTILS_DFSUBSET_TASK_BAR_ID = 22;
 window.SW_UTILS_CENSUS_TASK_BAR_ID = 23;
 window.SCRIPT_TASK_BAR_ID = 24;
 window.WORKING_CELL_ID = 25;

 window.POPUP_CELL_ID = 26;

 const DC_BLANK_LINE_ID = 1000;

 const MIN_CELL_ID = DC_TITLE_ID;
 const MAX_CELL_ID = WORKING_CELL_ID;
 const total_ids = ((MAX_CELL_ID - MIN_CELL_ID) + 1);

 const WORKING_CELL = "# Working Cell ";

 window.empty_cell_id = null;




 var dfc_cell_ids = ["PandasdfcleanserTitle", "DCSystemTitle", "DCDataImportTitle", "DCDataInspectionTitle", "DCDataCleansingTitle",
     "DCDataTransformTitle", "DCDataExportTitle", "SWUtilities", "DCListUtilityTitle", "DCGeocodeUtilityTitle",
     "DCDFSubsetUtilityTitle", "DCDFCensusUtilityTitle", "DCDataScriptingTitle", "DCWorkingTitle",
     "DCSystem", "DCDataImport", "DCDataInspection", "DCDataCleansing", "DCDataTransform", "DCDataExport", "DCListUtility",
     "DCGeocodeUtility", "DCDFSubsetUtility", "DCCensusUtility", "DCDataScripting", "DCWorking", "dfcPopUpCell"
 ];

 var dfc_loaded_flagged = false;

 window.WORKING_CODE_CELL = '# working cell- please do not remove';
 window.WORKING_TITLE_CELL = '<div align="left" id="Restricted"/><div><img src="https://rickkrasinski.github.io/dfcleanser/graphics/Restricted.jpg" width="80" align="left"/></div><div><image width="10"></div><div><image width="10"><h2>&nbsp;&nbsp;&nbsp;Restricted</h2></div></div>';
 window.WORKING_BLANK_LINE = '<br></br>';

 //
 // ---------------------------------------------------
 // ---------------------------------------------------
 //               cell control functions 
 // ---------------------------------------------------
 // ---------------------------------------------------
 //

 /*
  *
  *  get dfc cell pointed to by dfc id 
  * 
  *  @function get_dfc_cellid_for_cell_id 
  * 
  *     @param : cellId - cell id to select
  * 
  */

 window.reset_chapter = function(cellid) {

     console.log("reset_chapter", cellid);
     switch (cellid) {

         case 0:
             window.clear_cell_output(window.SYSTEM_TASK_BAR_ID);
             window.run_code_in_cell(window.SYSTEM_TASK_BAR_ID, window.getJSPCode(window.SYSTEM_LIB, "display_system_environment", 0));
             window.scroll_to('DCSystem');

     }
     return (dfc_cell_ids[cellid]);
 };


 //
 // ---------------------------------------------------
 // ---------------------------------------------------
 //               cell control functions 
 // ---------------------------------------------------
 // ---------------------------------------------------
 //

 /*
  *
  *  get dfc cell pointed to by dfc id 
  * 
  *  @function get_dfc_cellid_for_cell_id 
  * 
  *     @param : cellId - cell id to select
  * 
  */

 window.get_dfc_cellid_for_cell_id = function(cellid) {
     return (dfc_cell_ids[cellid]);
 };

 /*
  *
  *  get cell pointed to by logical id 
  * 
  *  @function get_cell_for_id
  * 
  *    @param : cellId - cell id to select
  * 
  */
 window.get_cell_for_id = function(cellId) {
     // get the current cells 
     var cells = IPython.notebook.get_cells();
     var cell = null;

     if (cellId == POPUP_CELL_ID) {
         return (get_popupcodecell());
     }

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

 /*
  *
  *  get cell before cell pointed to by logical id 
  * 
  *  @function get_cell_for_before_id
  * 
  *    @param : cellId - cell id to select
  * 
  */
 window.get_cell_for_before_id = function(cellId) {

     // get the current cells 
     var cells = IPython.notebook.get_cells();
     var cell = null;
     var prev_cell = null;

     // search through the cells 
     for (var i = 0; i < (IPython.notebook.ncells()); i++) {
         cell = cells[i];
         var cellIndex = IPython.notebook.find_cell_index(cell);

         // check that cell index is valid
         if (IPython.notebook.is_valid_cell_index(cellIndex)) {
             // get the cell metadata 
             var cell_mdata = cell.metadata;

             if ((cell_mdata != undefined) && ("dfcleanser_metadata" in cell_mdata)) {
                 var dfc_cell_mdata = cell_mdata["dfcleanser_metadata"];
                 if ("dfc_cellid" in dfc_cell_mdata) {
                     var dfc_cell_id = dfc_cell_mdata["dfc_cellid"];
                     if (dfc_cell_id == cellId) {
                         return (prev_cell);
                     } else prev_cell = cell;
                 } else prev_cell = cell;
             } else prev_cell = cell;
         } else cell = null;
     }

     return (cell);
 };

 /*
  *
  *  select cell pointed to by logical id 
  * 
  *  @function select_cell
  * 
  *    @param : id - cell id to select
  * 
  */
 window.select_cell = function(id) {
     var cell_to_select = window.get_cell_for_id(id);
     select_current_cell(cell_to_select);
 };


 /*
  *
  *  selectthe cell before cell pointed to by logical id 
  * 
  *  @function select_before_cell
  * 
  *    @param : id - cell id to select
  * 
  */
 window.select_before_cell = function(id) {

     if (window.debug_detail_flag)
         console.log("select_before_cell", id);

     var cell_to_select = window.get_cell_for_before_id(id);
     select_current_cell(cell_to_select);
 };

 /*
  *
  *  set the cell pointed to by logical id 
  *  as the currently selected ipyhton cell with focus
  * 
  *  @function select_current_cell
  * 
  *  @param : cell_to_select - cell to focus
  * 
  */
 window.select_current_cell = function(cell_to_select) {
     var cellIndex = IPython.notebook.find_cell_index(cell_to_select);
     IPython.notebook.select(cellIndex, true);
     IPython.notebook.focus_cell();
     cell_to_select.select(true);
 };

 /*
  *
  *  select cell from its metadata
  * 
  *  @function select_cell_from_metadata
  * 
  *  @param : metadata - cell metadata to search for
  * 
  */
 window.select_cell_from_metadata = function(metadata, offset = 0) {

     if (window.debug_detail_flag)
         console.log(log_prefix + "\n" + "     select_cell_from_metadata", metadata, offset);

     var cells = IPython.notebook.get_cells();
     var cellIndex = null;

     for (var i = 0; i < (IPython.notebook.ncells()); i++) {
         var cell = cells[i];
         var cmdata = cell.metadata;
         var dfc_mdata = cmdata["dfcleanser_metadata"];

         if (dfc_mdata != undefined) {
             var dfc_cell_id = dfc_mdata["dfc_cellid"];

             if (dfc_cell_id == metadata) {
                 for (var j = 0; j < offset; j++) {
                     cell = cells[i + j + 1]; //IPython.notebook.select_next().get_selected_cell();
                     select_current_cell(cell);
                 }
                 select_current_cell(cell);
                 return (cell);
             }
         }
     }
 };

 /*
  *
  *  set the cell based on text
  * 
  *  @function select_cell_from_text
  * 
  *  @param : text - cell text to search for
  * 
  */
 window.select_cell_from_text = function(text) {
     var cells = IPython.notebook.get_cells();

     for (var i = 0; i < (IPython.notebook.ncells()); i++) {
         var cell = cells[i];
         var ctext = cell.get_text();

         if (ctext != undefined) {
             if (containsSubstring(ctext, text)) {
                 var cellIndex = IPython.notebook.find_cell_index(cell);
                 IPython.notebook.select(cellIndex, true);
                 IPython.notebook.focus_cell();
                 cell.select(true);
                 if (window.debug_detail_flag)
                     console.log(log_prefix + "\n" + "     select_cell_from_text", text, cellIndex);
                 return (true);
             }
         }
     }
     if (window.debug_detail_flag)
         console.log(log_prefix + "\n" + "     select_cell_from_text not found", text);

     return (false);
 };

 /*
  *
  *  delete the dfcleanser cell by id.
  * 
  *  @function delete_output_cell
  * 
  *  @param : id - cell id
  * 
  */
 window.delete_output_cell = function(id) {

     if (get_dfc_mode() == 1)
         return;

     var cell_to_delete = null;
     var cell_to_return_to = null;
     cell_to_delete = window.get_cell_for_id(id);

     if (cell_to_delete != window.empty_cell_id) {
         select_cell(id);
         cell_to_return_to = IPython.notebook.select_next().get_selected_cell()
         IPython.notebook.delete_cell(IPython.notebook.find_cell_index(cell_to_delete));
     }
     IPython.notebook.select(cell_to_return_to);
 };

 /*
  *
  *  run code in the dfcleanser cell
  * 
  *  @function run_code_in_cell
  * 
  *   @param : id   - cell id
  *   @param : code - python code to run
  * 
  */
 window.run_code_in_cell = function(id, code) {

     if (window.debug_detail_flag)
         console.log("run_code_in_cell", id, code, WORKING_CELL_ID, POPUP_CELL_ID, get_dfc_mode());

     var runCell = null;

     if (get_dfc_mode() == 1) {
         if (id == WORKING_CELL_ID)
             runCell = window.get_cell_for_id(id);
         else {
             if ((id == SW_UTILS_DATASTRUCT_TASK_BAR_ID) || (id == SW_UTILS_GEOCODE_TASK_BAR_ID) ||
                 (id == SW_UTILS_DFSUBSET_TASK_BAR_ID) || (id == SW_UTILS_CENSUS_TASK_BAR_ID) || (id == SCRIPT_TASK_BAR_ID))
                 runCell = window.get_cell_for_id(id);
             else
                 runCell = get_popupcodecell();
         }
     } else {
         runCell = window.get_cell_for_id(id);
     }

     var runCode = code;

     if (id == POPUP_CELL_ID)
         if (window.debug_detail_flag)
             console.log("run_code_in_cell", runCell, runCode);

     if (runCell != null) {
         if (id == window.WORKING_CELL_ID) {
             runCode = WORKING_CELL + "- please do not remove" + NEW_LINE + code;
             if (window.debug_detail_flag)
                 console.log(log_prefix + "\n" + "     run_code_in_cell : ", runCode);
             run_code(runCell, runCode);
         } else { run_code(runCell, runCode); }
     } else {
         if (window.debug_detail_flag)
             console.log(log_prefix + "\n" + "     Cell to run in not found", id, code);
     }
 };

 /*
  *
  *  run code in the dfcleanser cell
  * 
  *  @function insert_cell_and_run_code_in_output_cell
  * 
  *   @param : id         - cell id
  *   @param : outputid   - cell id for new cell
  *   @param : code       - python code to run
  * 
  */
 window.insert_cell_and_run_code_in_output_cell = function(id, outputid, code) {
     window.delete_output_cell(outputid);
     window.select_cell(id);
     IPython.notebook.insert_cell_below('code');
     var cell = IPython.notebook.select_next().get_selected_cell();
     window.run_code(cell, code);

     if (window.debug_detail_flag) {
         console.log(log_prefix + "\n" + "     insert_cell_and_run_code_in_output_cell", id, outputid, code);
     }
 };

 /*
  *
  *  clear cell output in the dfcleanser cell
  * 
  *  @function clear_cell_output
  * 
  *   @param : id         - cell id
  * 
  */
 window.clear_cell_output = function(id) {

     if (get_dfc_mode() == 1)
         var cell_to_clear = get_popupcodecell();
     else
         var cell_to_clear = window.get_cell_for_id(id);

     if (cell_to_clear != window.empty_cell_id) {
         IPython.notebook.clear_output(IPython.notebook.find_cell_index(cell_to_clear));
     } else {
         if (window.debug_detail_flag)
             console.log(log_prefix + "\n" + "     clear_cell_output : fail", id);
     }
 };

 /*
  *
  *  run code in noteboook cell
  * 
  *  @function run_code
  * 
  *   @param : cell          -   noteboook cell to run code in
  *   @param : code          -   code to run in cell
  * 
  */
 window.run_code = function(cell, code) {
     cell.set_text(code);
     cell.execute();
 };

 /*
  *
  *  set code cell content
  * 
  *  @function set_code
  * 
  *   @param : id          -   noteboook cell to run code in
  *   @param : code        -   code to run in cell
  * 
  */
 window.set_code = function(id, code) {
     var Cell = window.get_cell_for_id(id);
     Cell.set_text(code);
 };

 /*
  *
  *  reset dependent cells when code cell changes
  *  impact other chapters in notebook
  * 
  *  @function reset_dependents
  * 
  *   @param : deplist     -   dependent list
  * 
  */
 window.reset_dependents = function(deplist) {

     if (window.debug_flag)
         console.log(log_prefix + "\n" + "     reset_dependents");

     if (get_dfc_mode() == 1)
         return;

     if (deplist[0]) {
         window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "display_import_forms", "0"));
     }
     if (deplist[1]) { window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID, window.getJSPCode(window.INSPECTION_LIB, "display_data_inspection", "0")); }
     if (deplist[2]) { window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "0")); }
     if (deplist[3]) { window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0")); }
     if (deplist[4]) {
         window.run_code_in_cell(window.EXPORT_TASK_BAR_ID, window.getJSPCode(window.EXPORT_LIB, "display_export_forms", "0"));
     }
     if (deplist[5]) { window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", "0")); }
 };


 function process_pop_up_cmd(chid) {
     /**
      * pop up main task bar calls.
      *
      * Parameters:
      *  fid
      *      System Environment function id
      */

     //if (window.debug_detail_flag)
     console.log(log_prefix + "\n" + "     process_pop_up_cmd", chid);

     var code = null;

     switch (chid) {
         case 0:
             code = "from dfcleanser.system.system_control import display_system_environment" + window.NEW_LINE;
             code = code + "display_system_environment(0)";
             break;
         case 1:
             code = "from dfcleanser.data_import.data_import_control import display_import_forms" + window.NEW_LINE;
             code = code + "display_import_forms(0)";
             break;
         case 2:
             code = "from dfcleanser.data_inspection.data_inspection_control import display_data_inspection" + window.NEW_LINE;
             code = code + "display_data_inspection(0)";
             break;
         case 3:
             code = "from dfcleanser.data_cleansing.data_cleansing_control import display_data_cleansing" + window.NEW_LINE;
             code = code + "display_data_cleansing(0)";
             break;
         case 4:
             code = "from dfcleanser.data_transform.data_transform_control import display_data_transform" + window.NEW_LINE;
             code = code + "display_data_transform(0)";
             break;
         case 5:
             code = "from dfcleanser.data_export.data_export_control import display_export_forms" + window.NEW_LINE;
             code = code + "display_export_forms(0)";
             break;
         case 6:
             if (get_dfc_mode() == 0) {
                 initialize_dc();
                 return;
             } else {
                 code = "from dfcleanser.system.load import load_pop_up_startup" + NEW_LINE;
                 code = code + "load_pop_up_startup()";
             }
             break;
     }

     window.delete_output_cell(window.POPUP_CELL_ID);
     var cell = get_cell_for_id(window.POPUP_CELL_ID);
     run_code(cell, code);

     window.shut_off_autoscroll();

 }

 //
 // ---------------------------------------------------
 // end cell control functions 
 // ---------------------------------------------------
 //

 window.set_textarea = function(formid, istring) {
     var mstring = istring.replace(/dfc_new_line/g, '\n');
     $("#" + formid).val(mstring);
 };

 window.set_dfcnotes = function(notes) {
     var mstring = notes.replace(/dfc_new_line/g, '\n');
     $("#" + formid).val(mstring);
 };

 /* 
 // -------------------------------------------------------
 // -------------------------------------------------------
 //         dfcleanser load and unload functions
 // ------------------------------------------------------
 // -------------------------------------------------------
 */

 var dfc_mode = 0;

 window.get_dfc_mode = function() {
     return (dfc_mode);
 };

 /*
  *
  *  Load the dfcleanser utility in inline mode
  *  @function initialize_dc
  * 
  */
 window.initialize_dc = function() {
     if (window.debug_flag)
         console.log(log_prefix + "\n" + "     initialize_dc");

     // get the current cells 
     var cells = IPython.notebook.get_cells();
     var cellText = "";
     var nbbcellId = null;

     var workingcell = get_cell_for_id(WORKING_CELL_ID);
     if (workingcell != null)
         window.sync_notebook();

     window.run_code_in_cell(window.SYSTEM_TASK_BAR_ID, window.getJSPCode(window.SYSTEM_LIB, "display_system_environment", "0"));
     window.run_code_in_cell(window.IMPORT_TASK_BAR_ID, window.getJSPCode(window.IMPORT_LIB, "display_import_forms", "0"));
     window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID, window.getJSPCode(window.INSPECTION_LIB, "display_data_inspection", "0"));
     window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "0"));
     window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
     window.run_code_in_cell(window.EXPORT_TASK_BAR_ID, window.getJSPCode(window.EXPORT_LIB, "display_export_forms", "0"));
     window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_LIB, "process_sw_utilities", "0"));
     window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", "0"));
     window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", "0"));
     window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", "0"));
     window.run_code_in_cell(window.SCRIPT_TASK_BAR_ID, window.getJSPCode(window.SCRIPT_LIB, "display_data_scripting", "0"));

     if (workingcell != null)
         workingcell.set_text(WORKING_CELL + "- please do not remove");

     window.shut_off_autoscroll();
 };

 /*
  *
  *  Load the dfcleanser utility from the toolbar icon.
  *  @function load_dfcleanser_from_toolbar
  * 
  *  @param : dfcmode
  *      0 - load inline
  *      1 - load as pop up
  */
 window.load_dfcleanser_from_toolbar = function(dfcmode) {
     if (window.debug_flag)
         console.log(log_prefix + "\n" + "     load_dfcleanser_from_toolbar", dfcmode);

     if (dfcmode == 1) {
         var cells = IPython.notebook.get_cells();

         var cell = cells[(IPython.notebook.ncells() - 1)];
         var cellIndex = IPython.notebook.find_cell_index(cell);
         IPython.notebook.select(cellIndex, true);
         IPython.notebook.focus_cell();
         cell.select(true);
     }

     add_dfc_cell(MARKDOWN, window.WORKING_BLANK_LINE, 'DCBlankline', -1);
     add_dfc_cell(MARKDOWN, window.WORKING_TITLE_CELL, 'DCWorkingTitle', -1);
     add_dfc_cell(CODE, window.WORKING_CODE_CELL, 'DCWorking', -1);
     add_dfc_cell(MARKDOWN, window.WORKING_BLANK_LINE, 'DCBlankline', -1);

     window.shut_off_autoscroll();

     var nbname = IPython.notebook.get_notebook_name();
     window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.SYSTEM_LIB, "load_dfcleanser_from_toolbar", JSON.stringify([nbname, dfc_mode])));
 }

 /*
  *
  *  UnLoad the dfcleanser utility 
  *  @function unload_dfcleanser
  * 
  */
 window.unload_dfcleanser = function() {

     if (window.debug_flag)
         console.log(log_prefix + "\n" + "     unload_dfcleanser");

     window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSCode(window.SYSTEM_LIB, "unload_dfCleanser"));
 };


 window.complete_unload_dfcleanser = function() {

     if (window.debug_flag)
         console.log(log_prefix + "\n" + "     complete_unload_dfcleanser");

     var max_trys = 5;
     var ctry = 0;

     if (get_dfc_mode() == 1)
         delete_popupcodecell();

     while (ctry < max_trys) {
         if (get_num_dfcleanser_cells() > 0) {
             if (window.debug_detail_flag)
                 console.log(log_prefix + "\n" + "     unload_dfcleanser", ctry, get_num_dfcleanser_cells());
             ctry++;
             delete_dfcleanser_cells();
         } else { ctry = max_trys; }
     }
     if (window.debug_flag)
         console.log(log_prefix + "\n" + "     dfcleanser unloaded");
 };

 /*
  *
  *  preload the dfcleanser utility before loading cells
  *  @function preloaddfcleanser
  * 
  */
 window.preloaddfcleanser = function() {
     if (debug_flag)
         console.log(log_prefix + "\n" + "     preloaddfcleanser");

     var code = "dcpath = %pwd" + NEW_LINE;
     code = code + "from dfcleanser.common.cfg import set_notebookPath" + NEW_LINE;
     code = code + "set_notebookPath(dcpath)" + NEW_LINE;
     code = code + "from dfcleanser.system.load import load_dfcleanser_cells" + NEW_LINE;
     code = code + "load_dfcleanser_cells()";

     if (window.get_cell_for_id(window.WORKING_CELL_ID) == null) {
         window.add_dfc_cell(1, "# Temporary Working Cell", "DCWorking");
         window.run_code_in_cell(window.WORKING_CELL_ID, code);
         window.delete_output_cell(window.WORKING_CELL_ID);
     } else {
         window.run_code_in_cell(window.WORKING_CELL_ID, code);
     }
 };

 /*
  *
  *  load the dfcleanser utility as a pop up
  *  @function loaddfcleanserpopup
  * 
  */
 window.loaddfcleanserpopup = function() {
     if (debug_flag)
         console.log(log_prefix + "\n" + "     loaddfcleanserpopup");

     window.setup_popupcodecell();
     window.toggle_popupcodecell();

     var code = "from dfcleanser.system.load import load_pop_up_startup" + NEW_LINE;
     code = code + "load_pop_up_startup()";

     window.run_code_in_cell(window.POPUP_CELL_ID, code);

 };

 /*
  *
  *  check if dfcleanser is currently loaded
  *  @function is_dfcleanser_loaded
  * 
  */
 window.is_dfcleanser_loaded = function() {

     var cells = IPython.notebook.get_cells();

     // search through the cells 
     for (var i = 0; i < (IPython.notebook.ncells()); i++) {

         var cell = cells[i];
         var cmdata = cell.metadata;
         var dfc_mdata = cmdata["dfcleanser_metadata"];

         if (dfc_mdata != undefined) { return (true); }
     }

     return (false);
 };

 const MARKDOWN = 0
 const CODE = 1

 /*
  *
  *  add a dfcleanser cell to the notebook
  * 
  *  @function add_dfc_cell
  * 
  *   @param : ctype    - cell type
  *   @param : ctext    - cell text
  *   @param : dfcid    - dfcleanser metadata id
  * 
  */
 window.add_dfc_cell = function(ctype, ctext, dfcid, afterid = -1) {
     if (window.debug_detail_flag)
         console.log(log_prefix + "\n" + "     add_dfc_cell", ctype, ctext, dfcid, afterid);

     // if first cell to load find correct 
     // cell to start loading after
     if (afterid != -1) {
         select_cell(afterid);
     }

     if (ctype == CODE) { IPython.notebook.insert_cell_below('code'); } else { IPython.notebook.insert_cell_below('markdown'); }

     var cell_to_add = IPython.notebook.select_next().get_selected_cell();
     cell_to_add.set_text(ctext);

     // add the cellid metadata
     var dfcellDict = { "dfc_cellid": dfcid };
     var dfcleanserDict = { "dfcleanser_metadata": dfcellDict };
     var newcellDict = { "trusted": true, "scrolled": false, "dfcleanser_metadata": dfcellDict };
     cell_to_add.metadata = newcellDict; //dfcleanserDict;

     if (ctype == MARKDOWN) { cell_to_add.execute(); } else { cell_to_add.execute(); }
 };

 /*
  *
  *  find the number of dfcleanser cells
  * 
  *  @function get_num_dfcleanser_cells
  * 
  */
 window.get_num_dfcleanser_cells = function() {

     var cells = IPython.notebook.get_cells();
     var total_dfc_cells = 0;

     for (var i = 0; i < (IPython.notebook.ncells()); i++) {
         var cell = cells[i];
         var cmdata = cell.metadata;
         var dfc_mdata = cmdata["dfcleanser_metadata"];

         if (dfc_mdata != undefined) { total_dfc_cells++; }
     }
     return (total_dfc_cells);
 };

 /*
  *
  *  get the metadata for a dfc cell
  * 
  *  @function get_dfc_metadata
  * 
  *   @param : cell    - cell to get metadata from
  * 
  */
 window.get_dfc_metadata = function(cell) {
     var cmdata = cell.metadata;
     var dfc_mdata = cmdata["dfcleanser_metadata"];
     if (dfc_mdata != undefined) return (dfc_mdata);
     else return (undefined);
 }

 /*
  *
  *  delete the dfc cell
  * 
  *  @function delete_dfc_cell
  * 
  *   @param : cell_to_delete    - cell to delete
  * 
  */

 window.delete_dfc_cell = function(cell_to_delete) {
     if (window.debug_detail_flag)
         console.log(log_prefix + "\n" + "     delete_dfc_cell", cell_to_delete);

     var cellid = select_cell_from_metadata(cell_to_delete);
     IPython.notebook.delete_cell(IPython.notebook.find_cell_index(cellid));
 }

 /*
  *
  *  delete the dfc chapter cells
  * 
  *  @function delete_dfc_chapter
  * 
  *   @param : chaptertitle    - chapter cells to delete
  * 
  */
 window.delete_dfc_chapter = function(chaptertitle) {

     if (window.debug_detail_flag)
         console.log(log_prefix + "\n" + "     delete_dfc_chapter", chaptertitle);

     var cell_to_delete = null;
     var next_cell = null;
     cell_to_delete = select_cell_from_metadata(chaptertitle)

     // delete the title cell
     if (cell_to_delete != window.empty_cell_id) {
         select_current_cell(cell_to_delete);
         next_cell = IPython.notebook.select_next().get_selected_cell();
         IPython.notebook.delete_cell(IPython.notebook.find_cell_index(cell_to_delete));
     }

     if (window.debug_detail_flag)
         console.log(log_prefix + "\n" + "     delete_dfc_chapter : delete title", cell_to_delete);

     // delete the code cell 
     cell_to_delete = next_cell;
     select_current_cell(cell_to_delete);
     next_cell = IPython.notebook.select_next().get_selected_cell();
     var dfc_codetext = cell_to_delete.get_text();

     if (containsSubstring(dfc_codetext, "from dfcleanser."))
         IPython.notebook.delete_cell(IPython.notebook.find_cell_index(cell_to_delete));
     else
         next_cell = cell_to_delete;

     // delete the blank line cell 
     cell_to_delete = next_cell;
     select_current_cell(cell_to_delete);
     next_cell = IPython.notebook.select_next().get_selected_cell();

     var dfc_metadata = get_dfc_metadata(cell_to_delete);

     if (dfc_metadata != undefined) {
         var dfcid = dfc_metadata["dfc_cellid"];
         if (dfcid != undefined) {
             if (containsSubstring(dfcid, "DCBlankline"))
                 IPython.notebook.delete_cell(IPython.notebook.find_cell_index(cell_to_delete));
         }
     }

     IPython.notebook.select(next_cell);
 };

 /*
  *
  *  delete all dfc cells
  * 
  *  @function delete_dfcleanser_cells
  * 
  */
 window.delete_dfcleanser_cells = function() {

     if (window.debug_detail_flag)
         console.log(log_prefix + "\n" + "     delete_dfcleanser_cells");

     var cells = IPython.notebook.get_cells();
     var cell = window.empty_cell_id;

     // search through the cells 
     for (var i = 0; i < (IPython.notebook.ncells()); i++) {
         cell = cells[i];
         var cmdata = cell.metadata;
         var dfc_mdata = cmdata["dfcleanser_metadata"];

         if (dfc_mdata != undefined) {
             var cellIndex = IPython.notebook.find_cell_index(cell);
             IPython.notebook.select(cellIndex, true);
             IPython.notebook.focus_cell();
             cell.select(true);
             IPython.notebook.delete_cell(cellIndex);
         }
     }
 };

 /* 
  // -------------------------------------------------------
  // end dfcleanser load and unload functions
  // ------------------------------------------------------
  */


 //
 // ---------------------------------------------------
 // ---------------------------------------------------
 //           common uility functions
 // ---------------------------------------------------
 // ---------------------------------------------------
 //

 window.handlecbcheck = function(cb) {
     if (windows.debug_flag)
         console.log("handlecbcheck", cb);
 };



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
 // -----------------------------------------------------
 // helper functions for running python methods from js
 // -----------------------------------------------------
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
     if (element_to_scroll_to != null) element_to_scroll_to.scrollIntoView();
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
         if (window.debug_detail_flag)
             console.log("no checkbox ", id, " not found");
         return (null);
     }

     var inputs = new Array();
     $('#' + id + ' :input').each(function() {
         var type = $(this).attr("type");
         if (type == "checkbox")
             var id = $(this).attr("id");
         if ($(this).is(':checked')) { inputs.push("True"); } else { inputs.push("False"); }
     });
     return (JSON.stringify(inputs));
 };

 // 
 // Common get values for radios
 // 
 window.getradioValues = function(id) {
     var formd = document.getElementById(id);

     if (formd == null) {
         if (window.debug_detail_flag)
             console.log("no radio ", id, " not found");
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
 // function to request a full list of parms for an inout form
 //
 window.getfullparms = function(inputid) {

     switch (inputid) {

         case "arcgisgeocoder":
         case "googlegeocoder":
         case "binggeocoder":
         case "baidugeocoder":
         case "mapquestgeocoder":
         case "nomingeocoder":
         case "arcgisquery":
         case "googlequery":
         case "bingquery":
         case "databcquery":
         case "mapquestquery":
         case "nominquery":
         case "arcgisreverse":
         case "bingreverse":
         case "nominreverse":
         case "googlereverse":
         case "arcgisbatchgeocoder":
         case "baidubulkgeocoder":
         case "googlebulkgeocoder":
         case "bingbulkgeocoder":
         case "mapquestbulkgeocoder":
         case "nominbulkgeocoder":
         case "arcgisbatchquery":
         case "bingbulkquery":
         case "mapquestbulkquery":
         case "nominatimbulkquery":
         case "googlebulkreverse":

             var inputs = new Array();
             inputs.push(String(inputid));
             window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", "12" + ", " + JSON.stringify(inputs)));
             break;

         case "googlebulkquery":

             var inputs = new Array();
             inputs.push(String(inputid));

             var tableid = $('#gegdfltypesTable');

             if (window.debug_detail_flag)
                 console.log("tableid", tableid);
             if (tableid == null)
                 inputs.push(String(0));
             else
                 inputs.push(String(6));

             window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", "12" + ", " + JSON.stringify(inputs)));
             break;

         default:
             var inputs = new Array();
             inputs.push(String(inputid));
             window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "get_fullparms", JSON.stringify(inputs)));
             break;
     }
 };

 window.set_select_select = function(selectid, option) {

 };

 window.set_select_disable = function(selectid, option) {
     if (option == "Enable") {
         $('#' + selectid).removeAttr('disabled');
     } else {
         $('#' + selectid).attr('disabled', 'disabled');
     }
 };

 //
 // ----------------------------------------------------------
 // file selection directory - dirs restricted to local only
 // Note : adhere to the browser security usage of fakepath
 // ---------------------------------------------------------
 // 
 window.onChangefileselect = function(inputid, fileid) {

     var input = document.getElementById(inputid);
     var file = document.getElementById(fileid);

     if (window.debug_detail_flag)
         console.log("onChangefileselect", input, file);

     if (inputid == "addcolumnfilename") input.value = file.value.replace("C:\\fakepath\\", "");
     else input.value = file.value.replace("C:\\fakepath\\", "datasets/");
 };

 //
 // ---------------------------------------------------------
 // ---------------------------------------------------------
 // common functions for jupyter to javascript coordination
 // ---------------------------------------------------------
 // ---------------------------------------------------------
 //

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
     if (window.debug_flag)
         console.log(log_prefix + "\n" + "     getNotebookPath");

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


 //
 // set which dfc cells just got loaded
 // 
 window.getdfcChaptersLoaded = function() {

     console.log("getdfcChaptersLoaded");

     var cells = IPython.notebook.get_cells();
     var cell = window.empty_cell_id;
     var cellsloaded = [];

     for (var j = 0; j < dfc_cell_ids.length; j++)
         cellsloaded.push(0);

     // search through the cells 
     for (var i = 0; i < (IPython.notebook.ncells()); i++) {

         cell = cells[i];
         var cmdata = cell.metadata;
         var dfc_mdata = cmdata["dfcleanser_metadata"];

         if (dfc_mdata != undefined) {
             if (dfc_mdata["dfc_cellid"] != "DCBlankline")
                 for (var k = 0; k < dfc_cell_ids.length; k++) {
                     if (dfc_mdata["dfc_cellid"] == dfc_cell_ids[k])
                         cellsloaded[k] = 1;
                 }
         }
     }

     if (window.debug_flag)
         console.log(log_prefix + "\n" + "     cellsloaded", cellsloaded);

     window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.CFG_LIB, "set_chapters_loaded", JSON.stringify(cellsloaded)));
 };

 //
 // set dfc mode
 //
 window.set_dfcmode = function(dfcmode) {
     if (window.debug)
         console.log('\n[' + "dfcleanser" + ']' + "\n" + "     set_dfcmode ", dfcmode, "\n");

     dfc_mode = dfcmode;
 };


 //
 // -----------------------------------------------------
 // functions for scrolling tables in dataframe cleanser
 // -----------------------------------------------------
 //

 window.scrollSampleRow = function(tableid, direction) {

     var inputs = new Array();
     inputs.push(String(tableid));
     inputs.push(String(direction));
     window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "scroll_sample_rows", JSON.stringify(inputs)));
 };

 window.scrollSingleRow = function(tableid, direction) {

     var inputs = new Array();
     inputs.push(String(tableid));
     inputs.push(String(direction));
     window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "scroll_single_row", JSON.stringify(inputs)));
 };

 window.scrollTable = function(tableid, direction) {

     if (window.debug_flag)
         console.log(log_prefix + "\n" + "     " + "scrollTable", tableid, direction);

     var inputs = new Array();

     if (tableid == "dfschemaTable") {
         inputs.push([4, direction])
         window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0" + "," + JSON.stringify(inputs)));
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
         window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "get_sample_row", JSON.stringify(inputs)));
     }
 }

 //
 // ---------------------------------------------------
 //            common help functions
 // ---------------------------------------------------
 //

 //
 // display help section by dfc help id
 //
 window.displayhelp = function(helpid) {

     var url = "https://rickkrasinski.github.io/dfcleanser/html/help/dfcleanser_help#dfc_" + String(helpid);
     window.open(url);
 };

 //
 // display help by url
 //
 window.display_help_url = function(url) {
     window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "display_url", JSON.stringify(url)));
     return true;
 };

 //
 // display inline help 
 //
 window.display_inline_help = function(noteid, txtmsg) {
     var noteobj = noteid.text(txtmsg);
     noteobj.html(noteobj.html().replace(/\n/g, '<br/>'));
     noteid.css('color', '#67a1f3');
 };

 //
 // sync with Jupyter
 //
 window.sync_notebook = function() {

     var nbname = IPython.notebook.get_notebook_name();
     var inputs = new Array();
     inputs.push(nbname);
     window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.CFG_LIB, "sync_with_js", JSON.stringify(inputs)));
 };

 //
 // log Jupyter message
 //
 window.log_jupyter_msg = function(message) {
     console.log(log_prefix + "\n" + "     " + message);
 };

 $(document).ready(function() {

     if (!dfc_loaded_flagged) {
         window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "dfc_document_loaded", 0));
         console.log("document ready");
     }
     $("div").click(function() {
         //window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "dfc_document_loaded", 0));
     });
 });