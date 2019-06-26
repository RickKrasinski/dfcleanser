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
    console.log("transform_task_bar_callback", fid);
    switch (fid) {
        case -1:
            var inputs = new Array();
            inputs.push([4]);
            var inputParms = window.get_input_form_parms("datainspectdf");
            inputs.push(inputParms);
            console.log("transform_task_bar_callback", inputs);

            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0" + "," + JSON.stringify(inputs)));
            break;
        case 1:
        case 2:
        case 3:
        case 4:
            var inputs = new Array();
            inputs.push([fid]);
            console.log("transform_task_bar_callback", inputs);

            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0" + "," + JSON.stringify(inputs)));
            break;
        case 5:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
            break;
    }
    window.scroll_to('DCDataTransform');
}

function dfscleansecol(colid) {
    /**
     * Data transform cleanse single column.
     *
     * Parameters:
     *  colid - column id
     */

    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "-1" + "," + JSON.stringify(colid)));
    window.scroll_to('DCDataCleansing');
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


function df_process_cmd_callback(optionId) {
    /**
     * dataframe transform process cmd callback.
     *
     * Parameters:
     *  optionId     - option id
     *  fId          - function id
     */

    var inputs = new Array();
    var formid = null;

    switch (optionId) {
        case 0:
            formid = "savecidrowtransform";
            break;
        case 1:
            formid = "addcidrowtransform";
            break;
        case 2:
            formid = "changecidrowtransform";
            break;
        case 3:
            formid = "setnewcoltransform";
            break;
        case 4:
            formid = "resetridcoltransform";
            break;
        case 5:
            formid = "dropridcoltransform";
            break;
        case 6:
            formid = "sortrowidcoltransform";
            break;
        case 7:
            formid = "dropdridcoltransform";
            break;
        case 8:
            var fparms = [0];
            var inputs = new Array();
            inputs.push(fparms);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0" + "," + JSON.stringify(inputs)));
            break;
    }

    if (formid != null) {
        // get the input values
        transformVals = get_input_form_parms(formid);
        inputs.push(transformVals);
    }
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "10" + "," + JSON.stringify(inputs)));

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
        case 13:
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
            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
            window.scroll_to('DCDataTransform');
            break;
        case 13: // add new column from file
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(inputs)));
            window.scroll_to('DCDataTransform');
            break;
        case 14:
            break;
        case 15: // add new column from code
            if (inputs.indexOf("# add column code") != -1) {
                inputs = inputs.replace("# add column code", "");
            }
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(inputs)));
            window.scroll_to('DCDataTransform');
            break;
        case 17: // add new column from code display gen functions
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

    console.log("data_transform_cols_callback", funcid, optionId);
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
            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
            window.scroll_to('DCDataTransform');
            break;
        case 4:
            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", 11 + "," + JSON.stringify("[0]")));
            break;
        case 8:
            var colname = $("#applyColumnname");
            var applyinputs = [];
            applyinputs.push([colname.val(), 36]);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(applyinputs)));
            window.scroll_to('DCDataTransform');
            break;

    }
}


function data_transform_apply_fn_callback(ftype, optionId) {
    /**
     * apply fn to column callback.
     *
     * Parameters:
     *  ftype      - form type
     *  optionId   - option id
     */

    var inputs = new Array();
    var fparms = null;

    if (ftype == 0)
        fparms = get_input_form_parms("applycolInput");
    else {
        if (ftype == 1)
            fparms = get_input_form_parms("applylcolInput");
        else
            fparms = get_input_form_parms("applydcolInput");
    }

    if ((ftype == 1) && (optionId == 8)) {
        var applyinputs = [];
        applyinputs.push([fparms[0], 37]);
        window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(applyinputs)));
    } else {
        inputs.push([ftype, optionId, fparms]);
        window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(fparms)));
    }
    window.scroll_to('DCDataTransform');

}

window.get_selected_value = function(selectid) {
    /**
     * get selected value
     *
     * Parameters:
     *  selectid   - select form id
     */

    var selected_value = $("#" + selectid + " :selected").text();
    console.log("get_selected_value", selectid, selected_value);

    var inputs = new Array();
    inputs.push(selectid);
    inputs.push(selected_value);
    window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "get_gen_func_values", JSON.stringify(inputs)));
};

function get_lambda_fn(selectid) {
    /**
     * get lambda fn
     *
     * Parameters:
     *  selectid   - select form id
     */

    var select_form_value = $("#" + selectid + " :selected").text();
    var df = $('#currentdf').val();
    var colname = $('#applylColumnname').val();

    var selected_value = "df[dfcolname] = ";
    selected_value = selected_value + select_form_value;

    console.log("get_selected_value", selectid, selected_value, colname);

    $('#fntoapply').val(selected_value);
}

function data_transform_apply_fn_callback(ftype, optionId) {
    /**
     * apply fn to column callback.
     *
     * Parameters:
     *  ftype      - form type
     *  optionId   - option id
     */

    var inputs = new Array();
    var fparms = null;

    if (ftype == 0)
        fparms = get_input_form_parms("applycolInput");
    else {
        if (ftype == 1)
            fparms = get_input_form_parms("applylcolInput");
        else
            fparms = get_input_form_parms("applydcolInput");
    }

    if ((ftype == 1) && (optionId == 8)) {
        var applyinputs = [];
        applyinputs.push([fparms[0], 37]);
        window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(applyinputs)));
    } else {
        inputs.push([ftype, optionId, fparms]);
        window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(fparms)));
    }
    window.scroll_to('DCDataTransform');

}

function process_cols_dropna_fillna_transform_callback(fid) {
    /**
     * Data Transform columns process cmd.
     *
     * Parameters:
     *  naoption  - na option
     *  fid       - function id
     *  numflag   - numflag
     */

    console.log("process_cols_dropna_fillna_transform_callback", fid);

    var inputs = new Array();

    switch (fid) {

        case 0:
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", fid));
            window.scroll_to('DCDataCleansing');
            break;
        case 5:
            fparms = get_input_form_parms("dtdndatatypeinput");
            inputs.push(fparms);
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", fid + "," + JSON.stringify(fparms)));
            window.scroll_to('DCDataCleansing');
            break;

        case 9:
            fparms = get_input_form_parms("dtfndatatypeinput");
            inputs.push(fparms);
            window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", fid + "," + JSON.stringify(fparms)));
            window.scroll_to('DCDataCleansing');
            break;
        default:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", fid));
            window.scroll_to('DCDataTransform');
    }


}

function process_cols_datatype_transform_callback(naoption, fid, numflag, dfcid) {
    /**
     * Data Transform columns process cmd.
     *
     * Parameters:
     *  naoption  - na option
     *  fid       - function id
     *  numflag   - numflag
     *  dfcid     - component id
     */

    console.log("process_cols_datatype_transform_callback", naoption, fid, numflag, dfcid);

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

            switch (dfcid) {
                case 'DataTransform':
                    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "44" + "," + JSON.stringify(inputs)));
                    window.scroll_to('DCDataTransform');
                    break;
                case 'DataCleansing':
                    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "11" + "," + JSON.stringify(inputs)));
                    window.scroll_to('DCDataCleansing');
                    break;
            }
            break;

        case 1:

            switch (dfcid) {
                case 'DataTransform':
                    window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
                    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
                    window.scroll_to('DCDataTransform');
                    break;
                case 'DataCleansing':
                    window.clear_cell_output(window.CLEANSING_TASK_BAR_ID);
                    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "0"));
                    window.scroll_to('DCDataCleansing');
                    break;
            }
    }
}

function col_checknum(colid) {
    /**
     * Check if column numeric.
     *
     * Parameters:
     *  colid - column id
     */

    console.log("col_checknum", colid);

    var inputs = new Array();
    inputs.push(colid);

    var datatype_select = document.getElementById(colid + "colselId");
    if (datatype_select == null)
        inputs.push("-1");
    else
        inputs.push(datatype_select.value);

    var sample_select = document.getElementById(colid + "samplesizeid");
    if (sample_select == null)
        inputs.push("-1");
    else
        inputs.push(sample_select.value);

    window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "45" + ", " + JSON.stringify(inputs)));
    window.scroll_to('DCDataTransform');
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

function get_gf_fn(genid) {

    var inputs = new Array();
    inputs.push([36]);
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
    var current_columns = currentcolname.val();

    console.log("dfsnriccol", colid, current_columns);
    if (current_columns == null) console.log("dfsnriccol null");
    if (current_columns.length == 0) {
        current_columns = "[" + colid + "]";
    } else {
        current_columns = current_columns.replace("]", ",");
        current_columns = current_columns + colid + "]";
    }

    currentcolname.val(current_columns);

    //var fparms = [9];
    //var inputs = new Array();
    //inputs.push(fparms);
    //inputs.push(colid);
    //window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "9" + "," + JSON.stringify(inputs)));
}

function dtdcrcol(colid) {
    var currentList = $("#dtddrcolumnids");
    var current_columns = currentList.val();

    if (current_columns.length == 0) {
        current_columns = "[" + colid + "]";
    } else {
        current_columns = current_columns.replace("]", ",");
        current_columns = current_columns + colid + "]";
    }

    currentList.val(current_columns);
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
            var inputs = new Array();
            inputs.push(0);
            inputs.push(3);
            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "13" + "," + JSON.stringify(inputs)));
            break;
        case 2:
            var formatstring = $("#formatstring");
            formatstring.val("");
            break;
        case 3:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
            break;
        case 4:
            var inputs = new Array();
            inputs.push(0);
            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "13" + "," + JSON.stringify(inputs)));
            break;

    }
    window.scroll_to('DCDataTransform');
}

function dt_datetime_transform_task_bar_callback(optionId) {
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
        case 6:
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
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
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
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
            break;
    }
    window.scroll_to('DCDataTransform');
}

function process_datetime_components_callback(optionId) {
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
            inputs.push(optionId);
            var formatVals = get_input_form_parms("datetimecompinput");
            inputs.push(formatVals);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "21" + "," + JSON.stringify(inputs)));
            break;
        case 1:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
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

function get_comp_col(colid) {

    var cname = $("#dtcdatetimecolname");
    cname.val(colid);
}

function select_datetime_dt(dtid) {
    var dttype = $("#dtdatatype");
    if (dtid == 0) dttype.val("datetime.datetime");
    if (dtid == 1) dttype.val("datetime.date");
    if (dtid == 2) dttype.val("datetime.time");
    if (dtid == 3) dttype.val("datetime.timedelta");
}


function dtselect_dropna_change(dropid) {

    var selected_value = $("#" + dropid + " :selected").text();
    console.log("dtselect_dropna_change", dropid, selected_value);

    var inputs = new Array();
    inputs.push(selected_value);

    window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "38" + ", " + JSON.stringify(inputs)));
    window.scroll_to('DCDataTransform');

}

function dtcselect_dropna_change(dropid) {

    var selected_value = $("#" + dropid + " :selected").text();
    console.log("dtcselect_dropna_change", dropid, selected_value);

    var inputs = new Array();
    inputs.push(selected_value);

    window.clear_cell_output(window.CLEANSING_TASK_BAR_ID);
    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "28" + ", " + JSON.stringify(inputs)));
    window.scroll_to('DCDataCleansing');

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

    var fillnaopt = $("[id = 'dfillnasel" + colid + "'] :selected").val();
    //console.log("fillnaopt", fillnaopt);
    inputs.push(fillnaopt);

    window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "17" + ", " + JSON.stringify(inputs)));
    window.scroll_to('DCDataTransform');
}