//
// 
// ------------------------------------------------------
// Data Transform Chapter javascript functions
// ------------------------------------------------------
//
// 

const PROCESS = 0
const RETURN = 1
    //const HELP = 2

function transform_task_bar_callback(fid) {
    /**
     * data transform main taskbar callback.
     *
     * Parameters:
     *  fid - function id
     */
    switch (fid) {
        case 0:
        case 1:
        case 2:
        case 3:
        case 4:
            var inputs = new Array();
            inputs.push([fid]);
            var inputParms = window.get_input_form_parms("datatransformdf");
            inputs.push(inputParms);
            console.log("transform_task_bar_callback", inputs);

            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0" + "," + JSON.stringify(inputs)));
            break;
        case 5:
            window.delete_output_cell(window.TRANSFORM_ADD_COLUMN_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
            break;
    }
    window.scroll_to('DCDataTransform');
}

// 
// ------------------------------------------------------
// Simple Dataframe Transform functions
// ------------------------------------------------------
// 

function df_transform_task_bar_callback(optionId) {
    /**
     * dataframe transform main taskbar callback.
     *
     * Parameters:
     *  optionId     - option id
     */

    switch (optionId) {
        case 7:
            window.delete_output_cell(window.TRANSFORM_GENERIC_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
            break;
        default:
            var fparms = [optionId];
            var inputs = new Array();
            inputs.push(fparms);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "9" + "," + JSON.stringify(inputs)));
            break;
    }
    window.scroll_to('DCDataTransform');
}

function df_process_cmd_callback(optionId, fid) {
    /**
     * dataframe transform process cmd callback.
     *
     * Parameters:
     *  optionId     - option id
     *  fId          - function id
     */
    var opcode = PROCESS;
    //if ((fid >= 30) && (fid < 40)) {
    //    opcode = HELP;
    //}
    switch (optionId) {
        case 0:
            if (fid == 2) { opcode = RETURN; }
            break;
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
            if (fid == 1) { opcode = RETURN; }
            break;
    }
    switch (opcode) {
        case PROCESS:
            var formid = "";
            var transformVals = "";
            var fparms = [optionId, fid];
            var inputs = new Array();
            inputs.push(fparms);
            switch (optionId) {
                case 0:
                    formid = "savecidrowtransform";
                    break;
                case 1:
                    formid = "addcidrowtransform";
                    break;
                case 2:
                    formid = "resetridcoltransform";
                    break;
                case 3:
                    formid = "setnewcoltransform";
                    break;
                case 4:
                    formid = "dtdroprowids";
                    break;
                case 5:
                    formid = "dropdridcoltransform";
                    break;
            }
            if (formid != "") {
                // get the input values
                transformVals = get_input_form_parms(formid);
                inputs.push(transformVals);
            }
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "10" + "," + JSON.stringify(inputs)));
            break;
        case RETURN:
            var fparms = [0];
            var inputs = new Array();
            inputs.push(fparms);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0" + "," + JSON.stringify(inputs)));
            break;
    }
    window.scroll_to('DCDataTransform');
}

//
//-------------------------------------------------------
// Columns Transform functions
//-------------------------------------------------------
//

function cols_transform_tb_callback(fid) {
    /**
     * columns transform taskbar callback.
     *
     * Parameters:
     *  fId          - function id
     */
    switch (fid) {
        case 0:
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
        case 6:
        case 7:
        case 8:
        case 11:
        case 12:
        case 14:
        case 15:
            var inputs = new Array();
            inputs.push([fid]);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(inputs)));
            break;
        case 9:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
            break;
    }
    if (fid != 5) window.scroll_to('DCDataTransform');
}

function data_transform_add_cols_callback(optionId) {
    /**
     * columns transform taskbar callback.
     *
     * Parameters:
     *  optionId   - option id
     */

    var inputs = new Array();
    var fparms = ["None", 2, optionId];
    inputs.push(fparms);

    var formid = "";
    switch (optionId) {
        case 0:
        case 1:
        case 2:
            formid = "addcolInput";
            break;
        case 13:
            formid = "addcolfileInput";
            break;
        case 14:
        case 15:
        case 16:
        case 17:
        case 21:
            formid = "addcolcodeInput";
            break;
    }

    if (formid != "") { var importVals = get_input_form_parms(formid); }
    if ((optionId == 16) || (optionId == 17)) {
        if (importVals.indexOf("# add column code") != -1) {
            importVals = importVals.replace("# add column code", "");
        }
    }

    inputs.push(importVals);
    switch (optionId) {
        case 0:
        case 1:
        case 2:
            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(inputs)));
            window.scroll_to('DCDataTransform');
            break;
        case 4:
        case 5:
            window.delete_output_cell(window.TRANSFORM_ADD_COLUMN_ID);
            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
            window.scroll_to('DCDataTransform');
            break;
        case 13: // add new column from file
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(inputs)));
            window.scroll_to('DCDataTransform');
            break;
        case 14:
            window.run_code_in_cell(window.SW_UTILS_GENFUNC_TASK_BAR_ID, window.getJSPCode(window.GEN_FUNCTION_LIB, "display_gen_function", "1"));
            window.scroll_to('DCGenFunctionUtility');
            break;
        case 15: // add new column from code
            if (inputs.indexOf("# add column code") != -1) {
                inputs = inputs.replace("# add column code", "");
            }
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(inputs)));
            window.scroll_to('DCDataTransform');
            break;
        case 21:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(inputs)));
            window.scroll_to('DCDataTransform');
            break;
    }

}

function data_transform_add_cols_generic(funcid, gtid) {
    /**
     * generic transform taskbar callback.
     *
     * Parameters:
     *  funcid       - function id
     *  gtid         - generic type id
     */
    var inputs = new Array();
    var fparms = ["None", 2, funcid];
    inputs.push(fparms);
    var dtvals = getradioValues("dtconvertdatatype");
    if (dtvals != null) { inputs.push(dtvals); }
    var importVals = get_input_form_parms("addcolcodeInput");
    inputs.push(importVals);
    inputs.push(gtid);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(inputs)));
}

//----------------------------------------------------------------
// Column Transform callbacks - mapping, dummies and categorical
//----------------------------------------------------------------
function data_transform_cols_callback(funcid, optionId) {
    /**
     * Data Transform columns callback mapping, dummies and categorical.
     *
     * Parameters:
     *  funcid       - function id
     *   optionId    - option id
     */
    var inputs = new Array();
    var element = document.getElementById("ucolscolumnname");
    if (element != null) { inputs.push(element.value); } else { inputs.push("None"); }
    inputs.push(funcid);
    inputs.push(optionId);

    switch (funcid) {
        case 0:
            var formid = "";
            switch (optionId) {
                case 1:
                    formid = "renamecolInput";
                    break;
                case 2:
                    formid = "addcolInput";
                    break;
                case 3:
                    formid = "dropcolInput";
                    break;
                case 4:
                    formid = "reordercolInput";
                    break;
                case 5:
                    formid = "maptransformInput";
                    break;
                case 6:
                    formid = "dummytransformInput";
                    break;
                case 7:
                    formid = "categorytransformInput";
                    break;
                case 11:
                    formid = "savecolInput";
                    break;
                case 12:
                    formid = "copycolInput";
                    break;
                case 14:
                    formid = "sortcolInput";
                    break;
                case 15:
                    formid = "applycolInput";
                    break;
            }

            // get the input values
            var importVals = get_input_form_parms(formid);
            inputs.push(importVals);

            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", 5 + "," + JSON.stringify(inputs)));
            window.clear_cell_output(window.CLEANSING_TASK_BAR_ID);
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "0"));
            window.clear_cell_output(window.INSPECTION_TASK_BAR_ID);
            window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID, window.getJSPCode(window.INSPECTION_LIB, "display_data_inspection", "0"));
            window.scroll_to('DCDataTransform');
            break;
        case 1:
            var colname = $("#applyColumnname");
            var applyinputs = [];
            applyinputs.push([colname.val(), 35]);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(applyinputs)));
            window.scroll_to('DCDataTransform');
            break;
        case 2:
            window.delete_output_cell(window.TRANSFORM_ADD_COLUMN_ID);
            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
            window.scroll_to('DCDataTransform');
            break;
        case 4:
            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", 11 + "," + JSON.stringify("[0]")));
            break;
    }
}

function process_cols_datatype_transform_callback(fid) {
    /**
     * Data Transform columns process cmd.
     *
     * Parameters:
     *  fid       - function id
     */

    var inputs = new Array();
    var element = document.getElementById("ucolscolumnname");
    if (element != null) { inputs.push(element.value); } else { inputs.push("None"); }

    switch (fid) {
        case 0:
            inputs.push(fid);
            inputs.push(8);
            var dtvals = window.getradioValues("dtconvertdatatype");
            if (dtvals != null) { inputs.push(dtvals); }
            var fillna = window.get_input_form_parms("dtdatatypeinput");
            inputs.push(fillna);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "5" + "," + JSON.stringify(inputs)));
            window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID, window.getJSPCode(window.INSPECTION_LIB, "display_data_inspection", "0"));
            window.scroll_to('DCDataTransform');
            break;
        case 1:
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "4" + "," + JSON.stringify(inputs[0])));
            window.scroll_to('DCDataCleansing');
            break;
        case 2:
            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
            window.scroll_to('DCDataTransform');
            break;
    }
}

function select_applyfn_gen_function(genid) {
    /**
     * select gen func to display.
     *
     * Parameters:
     *  genid       - generic function id
     */

    var inputs = new Array();
    var fparms = ["None", 16, 19];
    inputs.push(fparms);
    inputs.push(genid);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(inputs)));
    window.scroll_to('DCDataTransform');
}

function select_addcol_gen_function(genid) {
    /**
     * select gen func to display.
     *
     * Parameters:
     *  genid       - generic function id
     */
    var inputs = new Array();
    var fparms = ["None", 2, 16];
    inputs.push(fparms);
    inputs.push(genid);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(inputs)));
    window.scroll_to('DCDataTransform');
}

function single_col_categorical_callback(optionId) {
    /**
     * transform column categorical callback.
     *
     * Parameters:
     *  optionId    - option id
     */

    window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);

    if (optionId < 5) {
        var element = document.getElementById("ucolscolumnname");
        window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", optionId + "," + JSON.stringify(element.value)));
    } else {
        if (optionId == 5) {
            window.delete_output_cell(window.TRANSFORM_GENERIC_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", 0));
        }
    }
    window.scroll_to('DCDataTransform');
}

function display_map_inputs_callback(colId) {
    /**
     * display map inputs callback.
     *
     * Parameters:
     *  optionId    - option id
     */
    var fparms = [5];
    var cparms = colId;
    var inputs = new Array();
    inputs.push(fparms);
    inputs.push(cparms);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "7" + "," + JSON.stringify(inputs)));
    window.scroll_to('DCDataTransform');
}

function dtctcol(colid, option) {
    /**
     * get column name.
     *
     * Parameters:
     *  colid    - column id
     *  option   - option
     */
    if (option == 30) { var fparms = ["3", colid, option]; } else { var fparms = [colid, option]; }
    var inputs = new Array();
    inputs.push(fparms);
    // return to main
    if (option == 4) {
        window.delete_output_cell(window.TRANSFORM_GENERIC_ID);
        window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
        window.scroll_to('DCDataTransform');
    } else {
        switch (option) {
            case 24:
                var FromCol = document.getElementById("moveColumnname").value;
                var AfterCol = document.getElementById("moveafterColumnname").value;
                if (FromCol.length > 0) {
                    if (AfterCol.length > 0) {
                        $('#moveColumnname').val(colid);
                        $('#moveafterColumnname').val("");
                        $('#cnamesTablenote').text("* Select a Column for moving " + colid + " after by clicking on Column Name above");
                    } else {
                        $('#moveafterColumnname').val(colid);
                    }
                } else {
                    $('#moveColumnname').val(colid);
                    $('#cnamesTablenote').text("* Select a Column for moving " + colid + " after by clicking on Column Name above");
                }
                break;
            case 30:
                window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "9" + "," + JSON.stringify(inputs)));
                window.scroll_to('DCDataTransform');
                break;
            case 32:
                var ToCol = document.getElementById("copyColumnname").value;
                var FromCol = document.getElementById("copyfromColumnname").value;
                if (ToCol.length > 0) {
                    if (FromCol.length > 0) {
                        $('#copyColumnname').val(colid);
                        $('#copyfromColumnname').val("");
                    } else {
                        $('#copyfromColumnname').val(colid);
                    }
                } else {
                    $('#copyColumnname').val(colid);
                }
                break;
            default:
                window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(inputs)));
                window.scroll_to('DCDataTransform');
                break;
        }
    }
}

//----------------------------------------------------------------
// dynamic html functions
//----------------------------------------------------------------
function dfrcol(colid) {
    var currentList = $("#transformcolslist");
    var newList = "";
    if (currentList.val().length > 0) { newList = currentList.val() + ", " + "'" + colid + "'"; } else { newList = "'" + colid + "'"; }
    currentList.val(newList);
}

function srowcol(colid) {
    var currentList = $("#rowfilterscolslist");
    var newList = "";
    if (currentList.val().length > 0) { newList = currentList.val() + ", " + "'" + colid + "'"; } else { newList = "'" + colid + "'"; }
    currentList.val(newList);
}

function dtscol(colid) {
    var currentcolname = $("#remridcolname");
    currentcolname.val(colid);
}

function dfsnriccol(colid) {
    var currentcolname = $("#setnewcolid");
    currentcolname.val(colid);

    var fparms = [9];
    var inputs = new Array();
    inputs.push(fparms);
    inputs.push(colid);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "9" + "," + JSON.stringify(inputs)));
}

function dtdcrcol(colid) {
    var currentList = $("#dtddrcolumnids");
    var newList = "";
    if (currentList.val().length > 0) { newList = currentList.val() + ", " + "'" + colid + "'"; } else { newList = "'" + colid + "'"; }
    currentList.val(newList);
}

function setformat(fstring) {
    var formatstring = $("#dtformatstring");
    formatstring.val(fstring);
}

//
//-------------------------------------------------------
// datetime Transform functions
//-------------------------------------------------------
//

function process_datetime_format_transform_callback(fid) {
    /**
     * process data teim taskbar callback.
     *
     * Parameters:
     *  fid    - function id
     */
    switch (fid) {
        case 0:
            var inputs = new Array();
            var element = document.getElementById("ucolscolumnname");
            if (element != null) { inputs.push(element.value); } else { inputs.push("None"); }
            inputs.push(fid);
            inputs.push(13);
            var formatVals = get_input_form_parms("datetimeformatinput");
            inputs.push(formatVals);
            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "14" + "," + JSON.stringify(inputs)));
            break;
        case 1:
            window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "get_datetime_formats", "0"));
            break;
        case 2:
            var formatstring = $("#formatstring");
            formatstring.val("");
            break;
        case 3:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
            break;
    }
    window.scroll_to('DCDataTransform');
}

function dt_transform_task_bar_callback(optionId) {
    /**
     * process datetime taskbar callback.
     *
     * Parameters:
     *  optionId  - option id
     */

    switch (optionId) {
        case 0:
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
            var inputs = new Array();
            inputs.push(optionId);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "13" + "," + JSON.stringify(inputs)));
            break;
    }
    window.scroll_to('DCDataTransform');
}

function get_datetime_col(colname) {
    /**
     * get datetime column.
     *
     * Parameters:
     *  colname  - column name
     */

    var cname = $("#dtcolname");
    cname.val(colname);
    window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "get_column_samples", JSON.stringify(colname)));
}

/* dhtml datetime */
function select_datetime_format(format) {
    var formatstring = $("#dtformatstring");
    formatstring.val(format);
}

function process_datetime_tdelta_callback(optionId) {
    /**
     * process get deltatime command.
     *
     * Parameters:
     *  colname  - column name
     */
    switch (optionId) {
        case 0:
            var inputs = new Array();
            inputs.push(optionId);
            var unitsValue = getradioValues("timedeltaselect");
            inputs.push(unitsValue);
            var formatVals = get_input_form_parms("datetimetdeltainput");
            inputs.push(formatVals);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "15" + "," + JSON.stringify(inputs)));
            break;
        case 1:
            var cname = $("#dttdcolname");
            cname.val("");
            cname = $("#dttdcolname1");
            cname.val("");
            cname = $("#dttdrescolname");
            cname.val("");
            break;
        case 2:
            var inputs = new Array();
            inputs.push([3]);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0" + "," + JSON.stringify(inputs)));
            break;
    }
    window.scroll_to('DCDataTransform');
}

function process_datetime_merge_split_callback(optionId, funcid) {
    /**
     * process merge split command.
     *
     * Parameters:
     *  optionId  - option
     *  funcid    - function id
     */
    switch (optionId) {
        case 0:
            var inputs = new Array();
            inputs.push(optionId, funcid);
            var formid = "";
            if (funcid == 0) formid = "datetimetsplitinput";
            else formid = "datetimetmergeinput";
            var formatVals = get_input_form_parms(formid);
            inputs.push(formatVals);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "16" + "," + JSON.stringify(inputs)));
            break;
        case 1:
            if (funcid == 0) {
                var cname = $("#dtsdatetimecolname");
                cname.val("");
                cname = $("#dtsdatecolname");
                cname.val("");
                cname = $("#dtstimecolname");
                cname.val("");
            } else {
                var cname = $("#dtmdatecolname");
                cname.val("");
                cname = $("#dtmtimecolname");
                cname.val("");
                cname = $("#dtmdatetimecolname");
                cname.val("");
            }
            break;
        case 2:
            var inputs = new Array();
            inputs.push([3]);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0" + "," + JSON.stringify(inputs)));
            break;
    }
    window.scroll_to('DCDataTransform');
}

/* ------------------------------
 * dhtml functions
 * -------------------------------
 */
function get_deltat_col(colid) {
    var cname = $("#dttdcolname");
    if (cname.val().length > 0) {
        cname = $("#dttdcolname1");
        if (cname.val().length > 0) {
            cname = $("#dttdrescolname");
            if (cname.val().length > 0) {
                cname = $("#dttdcolname");
                cname.val(colid);
                cname = $("#dttdcolname1");
                cname.val("");
                cname = $("#dttdrescolname");
                cname.val("");
            } else {
                cname.val(colid);
            }
        } else {
            cname.val(colid);
        }
    } else {
        cname.val(colid);
    }
}

function get_split_col(colid) {

    var cname = $("#dtsdatetimecolname");

    if (cname.val().length > 0) {
        cname = $("#dtsdatecolname");
        if (cname.val().length > 0) {
            cname = $("#dtstimecolname");
            if (cname.val().length > 0) {
                cname = $("#dtsdatetimecolname");
                cname.val(colid);
                cname = $("#dtsdatecolname");
                cname.val("");
                cname = $("#dtstimecolname");
                cname.val("");
            } else {
                cname.val(colid);
            }
        } else {
            cname.val(colid);
        }
    } else {
        cname.val(colid);
    }
}

function get_merge_col(colid) {

    var cname = $("#dtmdatecolname");

    if (cname.val().length > 0) {
        cname = $("#dtmtimecolname");
        if (cname.val().length > 0) {
            cname = $("#dtmdatecolname");
            cname.val(colid);
            cname = $("#dtmtimecolname");
            cname.val(colid);
        } else {
            cname.val(colid);
        }
    } else {
        cname.val(colid);
    }
}

function select_datetime_dt(dtid) {
    var dttype = $("#dtdatatype");
    if (dtid == 0) dttype.val("datetime.datetime");
    if (dtid == 1) dttype.val("datetime.date");
    if (dtid == 2) dttype.val("datetime.time");
    if (dtid == 3) dttype.val("datetime.timedelta");
}

/*
 -----------------------------------------------
 -----------------------------------------------
 * Dataframe Schema callbacks
 -----------------------------------------------
 -----------------------------------------------
*/

/*
 --------------------------------------
 * dynamic html
 --------------------------------------
*/
function dfsch_fillnaselect(id) {
    $("#" + id).attr('disabled', false);
}

function dfsch_dropnaselect(id) {
    /**
     * Data Inspection drop nan dhtml.
     *
     * Parameters:
     *  id - threshold type
     */
    $("#" + id).attr('disabled', true);
    var col_id = id.slice("dfschinput".length);
    $("#dfschinput" + col_id).val("");
}

function dfsch_changedt(colid) {
    /**
     * Data Inspection change datatype.
     *
     * Parameters:
     *  colid - column id
     */

    var inputs = new Array();
    inputs.push(colid);

    var datatype_select = document.getElementById('dfschsel' + colid);
    if (datatype_select == null)
        inputs.push("-1");
    else
        inputs.push(datatype_select.value);

    var fillna_option = document.getElementById('fillna' + colid);
    if (fillna_option.checked)
        inputs.push("fillna");
    else {
        var dropna_option = document.getElementById('dropna' + colid);
        if (dropna_option.checked)
            inputs.push("dropna");
        else
            inputs.push("None");
    }

    var nafill = document.getElementById('dfschinput' + colid);
    if (nafill == null)
        inputs.push("");
    else
        inputs.push(nafill.value);

    window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "17" + ", " + JSON.stringify(inputs)));
    window.scroll_to('DCDataTransform');
}

/*
 -----------------------------------------------
 * Dataframe Concatenation callbacks
 -----------------------------------------------
*/
function process_concat_transform_callback(fid) {
    switch (fid) {
        case 0:
            var inputs = new Array();
            inputs.push(fid);
            var concatVals = get_input_form_parms("concatinput");
            inputs.push(concatVals);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "18" + "," + JSON.stringify(inputs)));
            break;
        case 1:
            var inputs = new Array();
            inputs.push([4]);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0" + "," + JSON.stringify(inputs)));
            break;
        case 2:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
            break;
    }
}