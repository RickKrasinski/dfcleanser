//
// 
// ------------------------------------------------------
// Data Cleansing Chapter javascript functions
// ------------------------------------------------------
//
// 

function cleansing_tb_callback(fid) {
    /**
     * save notebook callback.
     */
    var inputs = new Array();
    inputs.push(String(fid));

    switch (fid) {
        case 0:
        case 1:
        case 2:
            var inputParms = window.get_input_form_parms("datacleansedf");
            inputs.push(inputParms);
            console.log("cleansing_tb_callback", inputs);
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "2" + "," + JSON.stringify(inputs)));
            window.scroll_to('DCDataCleansing');
            break;
        case 3:
            window.clear_cell_output(window.CLEANSING_TASK_BAR_ID);
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "0"));
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

function change_uvals_callback() {
    /**
     * data cleansing change value callback.
     */

    var labels = get_input_form_labels("dcchangevalsinput");
    labels = JSON.parse(labels)

    console.log("change_uvals_callback", labels);
    //;console.log("change_uvals_callback", labels[0].indexOf("* New Value"), labels[1].indexOf("* New Value"));
    if ((labels[0].indexOf("* New_Value") < 0) &&
        (labels[1].indexOf("* New_Value") < 0)) {

        var currentVal = $('#changecval');
        var newVal = $('#changenval');

        var $label = $("label[for='" + currentVal.attr('id') + "']")
        $label.text("* Current_Value");
        var $label = $("label[for='" + newVal.attr('id') + "']")
        $label.text("* New_Value");

    } else {

        var colname = $("#ucolscolumnname");
        var currentVal = document.getElementById('changecval');
        var newVal = document.getElementById('changenval');

        var cval = "";
        var nval = "";
        var cname = "";

        if (currentVal.value.length > 0) { cval = currentVal.value; }
        if (newVal.value.length > 0) { nval = newVal.value; }

        if (window.has_Attribute(colname, "value")) {
            if (colname.attr('value').length > 0) {
                cname = colname.attr('value');
            }
        }

        var inputs = new Array();
        inputs.push(String(cname));
        inputs.push(String(cval));
        inputs.push(String(nval));

        window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "1" + "," + JSON.stringify(inputs)));
        window.scroll_to('DCDataCleansing');
    }
}

function find_uvals_callback() {
    /**
     * data cleansing find non numeric values callback.
     */

}

function find_uvals_callback() {
    /**
     * data cleansing find values callback.
     */

    var labels = get_input_form_labels("dcchangevalsinput");
    labels = JSON.parse(labels)

    if (labels[0].indexOf("* Min_Value") < 0) {

        var currentVal = $('#changecval');
        var newVal = $('#changenval');

        var $label = $("label[for='" + currentVal.attr('id') + "']")
        $label.text("* Min_Value");
        var $label = $("label[for='" + newVal.attr('id') + "']")
        $label.text("* Max_Value");

    } else {

        var colname = $("#ucolscolumnname");
        var currentVal = document.getElementById('changecval');
        var newVal = document.getElementById('changenval');
        var cval = "";
        var nval = "";
        var cname = "";

        if (currentVal.value.length > 0) { cval = currentVal.value; }
        if (newVal.value.length > 0) { nval = newVal.value; }
        if (window.has_Attribute(colname, "value")) {
            if (colname.attr('value').length > 0) { cname = colname.attr('value'); }
        }

        var inputs = new Array();
        inputs.push(String(cname));
        inputs.push(String(cval));
        inputs.push(String(nval));

        window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "20" + "," + JSON.stringify(inputs)));
        window.scroll_to('DCDataCleansing');
    }
}

function show_graphs_callback() {
    /**
     * data cleansing display graphs callback.
     */
    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "19"));
}

function show_uniques_callback() {
    /**
     * data cleansing display uniques callback.
     */
    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "22"));
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

function cleansing_task_bar_process_row_callback(option) {
    /**
     * process data cleansing row taskbar.
     *
     * Parameters:
     *   option - cleanse option
     */
    var inputs = new Array();
    inputs.push(String(option));
    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "12" + ", " + JSON.stringify(inputs)));

    if (option == 1) {
        window.clear_cell_output(window.INSPECTION_TASK_BAR_ID);
        window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID, window.getJSPCode(window.INSPECTION_LIB, "display_data_inspection", "0"));
        window.scroll_to('DCDataInspection');
    } else {
        if (option == 2) {
            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0" + ", " + "[[2]]"));
            window.scroll_to('DCDataTransform');
        } else {
            window.scroll_to('DCDataCleansing');
        }
    }
}


function process_cols_callback(fid) {

    var element = document.getElementById("ucolscolumnname");

    switch (fid) {

        case 6:
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "6" + "," + JSON.stringify(element.value)));
            window.reset_dependents([true, true, false, true, true, false]);
            window.scroll_to('DCDataCleansing');
            break;

        case 7:
            var inputs = new Array();
            inputs.push(String(element.value));

            var currentVal = document.getElementById('changecval');
            var cval = "";
            if (currentVal.value.length > 0) { cval = currentVal.value; }
            inputs.push(String(cval));
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "7" + "," + JSON.stringify(inputs)));
            window.scroll_to('DCDataCleansing');
            break;

        case 15:
            var inputs = new Array();
            inputs.push(String(element.value));

            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "15" + "," + JSON.stringify(inputs)));
            window.scroll_to('DCDataCleansing');
            break;

        case 13:
        case 16:
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", fid + "," + JSON.stringify(element.value)));
            window.scroll_to('DCDataCleansing');
            break;

        case 26:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "1" + "," + JSON.stringify(element.value)));
            window.scroll_to('DCDataTransform');
            break;
    }
}

function process_cols_na_callback(fid) {

    console.log("process_cols_na_callback", fid);

    switch (fid) {

        case 4:
        case 8:
        case 10:
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", fid));
            window.scroll_to('DCDataCleansing');
            break;
        case 39:
        case 40:
        case 41:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", fid));
            window.scroll_to('DCDataTransform');
            break;
    }
}

function round_col_vals_callback() {
    /**
     * process rounding column.
     */
    var colname = document.getElementById("ucolscolumnname");
    var accuracy = document.getElementById("columnround");
    var inputs = new Array();

    if (colname.value.length > 0) { inputs.push(String(colname.value)); }
    if (accuracy.value.length > 0) { inputs.push(String(accuracy.value)); }

    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "14" + "," + JSON.stringify(inputs)));
    window.scroll_to('DCDataCleansing');
}

function whitespace_vals_callback() {
    /**
     * process rounding column.
     */

    console.log("whitespace_vals_callback");

    var flag = $('#leadtrailflag').val();

    var inputs = new Array();
    inputs.push(flag);

    console.log("whitespace_vals_callback", inputs);

    var cbs = new Array();

    if ($('#HTabcbId').is(":checked")) cbs.push("true");
    else cbs.push("false");
    if ($('#LfeedcbId').is(":checked")) cbs.push("true");
    else cbs.push("false");
    if ($('#FfeedcbId').is(":checked")) cbs.push("true");
    else cbs.push("false");
    if ($('#CReturncbId').is(":checked")) cbs.push("true");
    else cbs.push("false");
    if ($('#BspacecbId').is(":checked")) cbs.push("true");
    else cbs.push("false");
    if ($('#VTabcbId').is(":checked")) cbs.push("true");
    else cbs.push("false");

    inputs.push(cbs);

    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "17" + "," + JSON.stringify(inputs)));
    window.scroll_to('DCDataCleansing');
}

function fillna_col_vals_callback() {

    var colname = document.getElementById("ucolscolumnname");
    var inputs = new Array();
    if (colname.value.length > 0) { inputs.push(String(colname.value)); }

    var parms = window.get_input_form_parms("colfillnainput");
    inputs.push(parms);

    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "28" + "," + JSON.stringify(inputs)));
    window.scroll_to('DCDataCleansing');

}

//function nncol(col) {
/**
 * Data Cleansing display selected non numeric column.
 *
 * Parameters:
 *   col - column name
 */
//    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "4" + "," + JSON.stringify(col)));
//    window.scroll_to('DCDataCleansing');
//}

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

function getSingleRow(tableid, rowid) {
    /**
     * get a single row to display - called from button key.
     *
     * Parameters:
     *  tableid - table identifier
     *  rowid - row id
     */
    var element = document.getElementById("dcdisrowInputId");
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
    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "23" + ", " + JSON.stringify(colid)));
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
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "24" + ", " + JSON.stringify(parms)));
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