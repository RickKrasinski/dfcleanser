//
// 
// ------------------------------------------------------
// Data Cleansing Chapter javascript functions
// ------------------------------------------------------
//
// 

function get_dfs() {

    var inputParms1 = window.get_input_form_parms("datainspectdfinput");
    var inputs1 = new Array();
    inputs1.push(inputParms1);

    if (window.debug_flag)
        console.log("get_dfs", inputs1, inputParms1, inputParms1.length);

    var inputParms = window.get_input_form_parms("datacleansedfinput");
    var inputs = new Array();
    inputs.push(inputParms);

    if (window.debug_flag)
        console.log("get_dfs", inputs, inputParms, inputParms.length);

    var selected_value = $("#dcdfdataframe :selected").text();
    if (window.debug_flag)
        console.log("dfcleanser select ", selected_value);

    var selected_value = $("didfdataframe :selected").text();
    if (window.debug_flag)
        console.log("dfinspection select ", selected_value);


}

function cleansing_tb_callback(fid) {
    /**
     * data cleansing main taskbar callback.
     *
     * Parameters:
     *  fid - function id
     */
    var inputs = new Array();
    inputs.push(String(fid));

    switch (fid) {
        case 0:
        case 1:
        case 2:

            var inputParms1 = window.get_input_form_parms("datainspectdf");
            var inputs1 = new Array();
            inputs1.push(inputParms1);

            if (window.debug_flag)
                console.log("cleansing_tb_callback", inputs1, inputParms1, inputParms1.length);

            var inputParms = window.get_input_form_parms("datacleansedf");
            inputs.push(inputParms);

            if (window.debug_flag)
                console.log("cleansing_tb_callback", inputs, inputParms, inputParms.length);

            var inputParms1 = window.get_input_form_parms("datainspectdf");
            var inputs1 = new Array();
            inputs1.push(inputParms1);

            if (window.debug_flag)
                console.log("cleansing_tb_callback", inputs1, inputParms1, inputParms1.length);

            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "2" + "," + JSON.stringify(inputs)));
            window.scroll_to('DCDataCleansing');
            break;
        case 3:
            window.clear_cell_output(window.CLEANSING_TASK_BAR_ID);
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "0"));
            window.scroll_to('DCDataCleansing');
            break;
        case 55:
            window.clear_cell_output(window.CLEANSING_TASK_BAR_ID);
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "55"));
            window.scroll_to('DCDataCleansing');
            break;
        case 56:
            var inputs = window.get_input_form_parms("selectdfrowsinput");
            window.clear_cell_output(window.CLEANSING_TASK_BAR_ID);
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "56" + "," + inputs));
            window.scroll_to('DCDataCleansing');
            break;

    }
}

function chgval(val) {
    /**
     * data cleansing change value dhtml.
     *
     * Parameters:
     *  val - value to change to/from
     */

    var currentVal = document.getElementById('changecval').value;
    var newVal = document.getElementById('changenval').value;

    if (currentVal.length > 0) {
        if (newVal.length > 0) {
            $('#changecval').val(val);
            $('#changenval').val("");
        } else {
            $('#changenval').val(val);
        }
    } else {
        $('#changecval').val(val);
    }
}

function chgcat(val) {
    /**
     * data cleansing change category dhtml.
     *
     * Parameters:
     *  val - value to change to/from
     */

    var currentID = document.getElementById('changecatval');

    if (currentID != null) {
        $('#changecatval').val(val);
    } else {
        var currentID = document.getElementById('addcatname');

        if (currentID != null) {
            $('#addcatname').val("");
        } else {

            var currentID = document.getElementById('removecatname');

            if (currentID != null) {
                var currentVal = currentID.value;

                if (currentVal == "[]") $('#removecatname').val("[" + val + "]");
                else {
                    currentVal = currentVal.replace("]", "," + val + "]")
                    $('#removecatname').val(currentVal);
                }
            } else {
                var currentID = document.getElementById('remwhtspccatname');

                if (currentID != null) {
                    var currentVal = currentID.value;

                    if (currentVal == "[]") $('#remwhtspccatname').val("[" + val + "]");
                    else {
                        currentVal = currentVal.replace("]", "," + val + "]")
                        $('#remwhtspccatname').val(currentVal);
                    }
                } else {
                    var currentID = document.getElementById('reorderorderlist');

                    if (currentID != null) {
                        var currentVal = currentID.value;
                        if (currentVal == "[]")
                            $('#reorderorderlist').val("[" + val + "]");
                        else {
                            currentVal = currentVal.replace("]", "," + val + "]")
                            $('#reorderorderlist').val(currentVal);
                        }
                    }
                }
            }
        }
    }
}

function process_category_column(colid) {
    /**
     * process category column cleanse.
     *
     * Parameters:
     *  colid - column id
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "process_category_column", colid);

    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "12" + "," + "'" + colid + "'"));
    window.scroll_to('DCDataCleansing');

}

function change_uvals_callback(optionid) {
    /**
     * change unique vals callback.
     *
     * Parameters:
     *  optionid - option id
     */

    var inputs = new Array();

    if (optionid == 0)
        var fparms = get_input_form_parms("dcchangevalsinput");
    else
        var fparms = get_input_form_parms("dcnnchangevalsinput");

    inputs.push(fparms);

    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "1" + "," + inputs));
    window.scroll_to('DCDataCleansing');
}


function find_nn_uvals_callback() {
    /**
     * data cleansing find non numeric values callback.
     */

    var inputs = new Array();

    var fparms = get_input_form_parms("dcnnfindvalsinput");

    inputs.push(fparms);

    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "29" + "," + inputs));
    window.scroll_to('DCDataCleansing');

}

function find_uvals_callback() {
    /**
     * data cleansing find numeric values callback.
     */

    var inputs = new Array();

    var fparms = get_input_form_parms("dcfindvalsinput");

    inputs.push(fparms);

    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "29" + "," + inputs));
    window.scroll_to('DCDataCleansing');
}

function show_graphs_callback() {
    /**
     * data cleansing display graphs callback.
     */
    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "19"));
    window.scroll_to('DCDataCleansing');
}

function show_details_callback() {
    /**
     * data cleansing display uniques callback.
     */
    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "22"));
    window.scroll_to('DCDataCleansing');
}

function show_uniques_callback() {
    /**
     * data cleansing display uniques callback.
     */
    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "29"));
    window.scroll_to('DCDataCleansing');
}

function show_outliers_callback() {
    /**
     * display col outliers.
     */
    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "20"));
    window.scroll_to('DCDataCleansing');
}

function cleansesrowtbInputIdcallback() {
    /**
     * data cleansing display row to clean.
     */
    var element = document.getElementById("cleansesrowtbInputId");
    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "3" + "," + JSON.stringify(element.value)));
    window.scroll_to('DCDataCleansing');
}

function process_cols_callback(fid) {
    /**
     * process column cleansing callback.
     *
     * Parameters:
     *  fid - function id
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "process_cols_callback", fid);

    var reset_inspection = true;

    switch (fid) {

        case 6:
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "6"));
            window.reset_dependents([true, true, false, true, true, false]);
            window.scroll_to('DCDataCleansing');
            reset_inspection = false;
            break;
        case 7:
            var inputs = new Array();

            var currentVal = document.getElementById('changecval');
            var cval = "";
            if (currentVal.value.length > 0) { cval = currentVal.value; }
            inputs.push(String(cval));
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "7" + "," + JSON.stringify(inputs)));
            window.scroll_to('DCDataCleansing');
            reset_inspection = false;
            break;
        case 13:
        case 15:
        case 16:
        case 35:
        case 36:
        case 37:
        case 38:
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", fid));
            window.scroll_to('DCDataCleansing');
            reset_inspection = false;
            break;
        case 40:
            var fparms = window.get_input_form_parms("dccatchangevalsinput");
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", fid + "," + fparms));
            window.scroll_to('DCDataCleansing');
            break;
        case 43:
        case 46:
        case 47:
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", fid));
            window.scroll_to('DCDataCleansing');
            break;
    }

    if (reset_inspection) window.reset_dependents([false, true, false, false, false, false]);
}

function process_cols_na_callback(fid) {
    /**
     * process column nan callback.
     *
     * Parameters:
     *  fid - function id
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "process_cols_na_callback", fid);

    switch (fid) {

        case 5:
        case 8:
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", fid));
            window.scroll_to('DCDataCleansing');
            break;
        case 41:

            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", fid));
            window.scroll_to('DCDataTransform');

            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "0"));

            break;
    }
}

function round_col_vals_callback() {
    /**
     * process rounding column.
     */

    var inputs = new Array();
    var fparms = get_input_form_parms("columnroundinput");
    inputs.push(fparms);

    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "14" + "," + inputs));
    window.scroll_to('DCDataCleansing');
}

function whitespace_vals_callback() {
    /**
     * process rounding column.
     */

    var inputs = new Array();
    var fparms = get_input_form_parms("remwhitetransformInput");
    inputs.push(fparms);

    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "17" + "," + inputs));
    window.scroll_to('DCDataCleansing');
}

function fillna_col_vals_callback() {
    /**
     * process fillna column.
     */

    var colname = document.getElementById("ucolscolumnname");
    var inputs = new Array();
    if (colname.value.length > 0) { inputs.push(String(colname.value)); }

    var parms = window.get_input_form_parms("colfillnainput");
    inputs.push(parms);

    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "28" + "," + JSON.stringify(inputs)));
    window.scroll_to('DCDataCleansing');

}

function process_cat_function_callback(fid) {
    /**
     * process category function.
     *
     * Parameters:
     *  fid - function id
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "process_cols_na_callback", fid);

    switch (fid) {

        case 41:
            var parms = window.get_input_form_parms("addcatinput");
            break;
        case 42:
            var parms = window.get_input_form_parms("removecatinput");
            break;
            //case 43:
            //    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "43"));
            //    window.scroll_to('DCDataCleansing');
            //    window.reset_dependents([false, true, false, false, false, false]);
            //   return;
            //break;
        case 44:
            var parms = window.get_input_form_parms("removewscatinput");
            break;
        case 45:
            var parms = window.get_input_form_parms("reordercatinput");
            break;

    }

    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", fid + "," + parms));
    window.scroll_to('DCDataCleansing');
    window.reset_dependents([false, true, false, false, false, false]);

}

//
// ----------------------------------------------------
// Row Cleansing Methods 
// ----------------------------------------------------
//
function dcdisrowInputIdcallback() {
    /**
     * Data Cleansing display row based on current row id.
     */
    var element = document.getElementById("dcdisrowInputId");
    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "3" + "," + JSON.stringify(element.value)));
    window.scroll_to('DCDataCleansing');
}

function getSingleRow() {
    /**
     * get a single row to display - called from button key.
     *
     */
    var element = document.getElementById("DCsinglerowInputId");
    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "3" + "," + JSON.stringify(element.value)));
    window.scroll_to('DCDataCleansing');
}

function chrowval(colid) {
    /**
     * display change row value input form.
     *
     * Parameters:
     *  colid - column id in current row
     */
    window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "change_current_row_value", JSON.stringify(colid)));
}

function change_rowvals_callback(fid) {
    /**
     * change row values callback.
     *
     * Parameters:
     *  fid - function id
     */
    var inputs = window.get_input_form_parms("changerowinput");
    var parms = new Array();
    parms.push(fid);
    parms.push(inputs);

    switch (fid) {
        case 0:
        case 1:
        case 2:
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "25" + ", " + JSON.stringify(parms)));
            break;
    }
    window.scroll_to('DCDataCleansing');
}

function getsrow(rowid) {
    /**
     * Data Cleansing get a single row.
     *
     * Parameters:
     *  rowid - row id
     */
    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "22" + ", " + rowid));
    window.scroll_to('DCDataCleansing');
}


function process_cleanse_datatype_callback(naoption, fid, numflag, dfcid) {
    /**
     * Data Transform columns process cmd.
     *
     * Parameters:
     *  naoption  - na option
     *  fid       - function id
     *  numflag   - numflag
     *  dfcid     - component id
     */

    if (window.debug_flag)
        console.log("process_cleanse_datatype_callback", naoption, fid, numflag);

    var inputs = new Array();
    var element = document.getElementById("ucolscolumnname");
    if (element != null) { inputs.push(element.value); } else { inputs.push("None"); }

    var dtype = $("#dtdatatype :selected").text();
    inputs.push(dtype);

    switch (fid) {
        case 0:

            inputs.push(naoption);

            switch (naoption) {
                case 0:
                    var dropnaparms = window.get_input_form_parms("dtdndatatypeinput");
                    inputs.push(dropnaparms);
                    break;
                case 1:
                    if (numflag == 1) {
                        var fillnaparms = window.get_input_form_parms("dtfndatatypeinput");
                        inputs.push(fillnaparms);
                    } else {
                        var fillnaparms = window.get_input_form_parms("dtnnfndatatypeinput");
                        inputs.push(fillnaparms);
                    }
                    break;
            }

            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "11" + "," + JSON.stringify(inputs)));
            window.scroll_to('DCDataCleansing');

            break;

        case 1:

            window.clear_cell_output(window.CLEANSING_TASK_BAR_ID);
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "0"));
            window.scroll_to('DCDataCleansing');
            break;
    }
}

function nn_check_compatability(fid, colname) {
    /**
     * Check column for alpha or numeric.
     *
     * Parameters:
     *  fid       - function id
     *  colname   - column name
     */

    if (window.debug_flag)
        console.log("nn_check_compatability", fid, colname);

    var inputs = new Array();
    inputs.push(colname);

    window.clear_cell_output(window.CLEANSING_TASK_BAR_ID);

    if (fid == 0)
        window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "30" + "," + JSON.stringify(inputs)));
    else
        window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "32" + "," + JSON.stringify(inputs)));

    window.scroll_to('DCDataCleansing');


}

function process_nn_check_compatability(fid) {
    /**
     * Check column for alpha or numeric.
     *
     * Parameters:
     *  fid       - function id
     *  colname   - column name
     */

    if (window.debug_flag)
        console.log("nn_check_compatability", fid);

    window.clear_cell_output(window.CLEANSING_TASK_BAR_ID);

    if (fid == 0)
        window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "31"));
    else
        window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "33"));

    window.scroll_to('DCDataCleansing');


}

function change_cleanse_na_opt(selectid) {
    /**
     * Change na option.
     *
     * Parameters:
     *  fid       - function id
     *  colname   - column name
     */

    var naoption = $("#" + selectid).val();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "change_cleanse_na_opt", selectid, naoption);

    if (naoption == "fillna")
        window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "8"));
    else
        window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "19"));

    window.scroll_to('DCDataCleansing');


}

function change_drop_cols(selectid) {
    add_select_val(selectid, "dropduplicatecolids");
}