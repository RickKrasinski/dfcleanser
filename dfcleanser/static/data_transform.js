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
            var inputParms = window.get_input_form_parms("datatransformdf");
            inputs.push(inputParms);
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
        case 108:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
            break;
        default:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", optionId));
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

    var formid = null;

    switch (optionId) {
        case 110:
            formid = "savecolnamestransform";
            break;
        case 111:
            formid = "addcolnamestransform";
            break;
        case 112:
            formid = "changecolnamestransform";
            break;
        case 113:
            formid = "setnewindextransform";
            break;
        case 114:
            formid = "resetindextransform";
            break;
        case 115:
            formid = "appendindextransform";
            break;
        case 116:
            formid = "sortindextransform";
            break;
        case 117:
            formid = "dropduplicatetransform";
            break;
        case 108:
            var fparms = [0];
            var inputs = new Array();
            inputs.push(fparms);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0" + "," + JSON.stringify(inputs)));
            break;
    }

    var inputs = new Array();
    //inputs.push(optionId);

    if (formid != null) {
        // get the input values
        transformVals = get_input_form_parms(formid);
        inputs.push(transformVals);
    }
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", optionId + "," + JSON.stringify(inputs)));

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

    console.log("cols_transform_tb_callback", fid);

    switch (fid) {
        case 200:
        case 201:
        case 202:
        case 203:
        case 204:
        case 205:
        case 206:
        case 207:
        case 208:
        case 209:
        case 211:
        case 212:
        case 213:
        case 214:
        case 215:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", fid));
            break;
        case 210:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
            break;
        case 5:
        case 216:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
            break;
    }
    window.scroll_to('DCDataTransform');
}

function data_transform_display_add_cols_callback(optionId) {

    var inputs = new Array();

    if (optionId == 412) {
        window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
        window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", 0));
        window.scroll_to('DCDataTransform');
        return;
    }

    addvals = get_input_form_parms("addcolInput");
    inputs.push(addvals);

    window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", optionId + "," + JSON.stringify(inputs)));
    window.scroll_to('DCDataTransform');
}

function data_transform_add_cols_callback(optionId) {
    /**
     * columns transform taskbar callback.
     *
     * Parameters:
     *  optionId   - option id
     */

    console.log("data_transform_add_cols_callback", optionId);

    var inputs = new Array();
    var fparms = ["None", 2, optionId];
    inputs.push(fparms);

    var formid = "";
    switch (optionId) {
        case 100:
        case 102:
        case 104:
        case 107:
            formid = "addcolInput";
            break;
        case 101:
            formid = "addcolfileInput";
            break;
        case 103:
            formid = "addcolcodeInput";
            break;
        case 106:
            formid = "addcoldfcfuncInput";
            break;
        case 108:
            formid = "addcoldfInput";
            break;
    }

    if (formid != "") { var importVals = get_input_form_parms(formid); }

    inputs.push(importVals);

    switch (optionId) {
        case 400:
        case 402:
        case 404:
        case 407:
            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(inputs)));
            window.scroll_to('DCDataTransform');
            break;
        case 411:
            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", optionId));
            window.scroll_to('DCDataTransform');
            break;
        case 412:
            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
            window.scroll_to('DCDataTransform');
            break;
        case 401: // add new column from file
        case 403: // add new column from user code
        case 406: // add new column from dfc func
        case 408: // add new column from df
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", optionId + "," + JSON.stringify(inputs)));
            window.scroll_to('DCDataTransform');
            break;
            //case 14:
            //    break;
            //case 15: // add new column from code
            //    if (inputs.indexOf("# add column code") != -1) {
            //        inputs = inputs.replace("# add column code", "");
            //    }
            //    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(inputs)));
            //    window.scroll_to('DCDataTransform');
            //    break;
            //case 17: // add new column from code display gen functions
            //    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(inputs)));
            //    window.scroll_to('DCDataTransform');
            //    break;
            //case 21:
            //    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(inputs)));
            //    window.scroll_to('DCDataTransform');
            //    break;
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
function data_transform_process_cols_callback(optionId) {
    /**
     * Data Transform columns callback mapping, dummies and categorical.
     *
     * Parameters:
     *  funcid       - function id
     *   optionId    - option id
     */

    console.log("data_transform_process_cols_callback", optionId);

    if (optionId == 216) {
        window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", 0));
        window.scroll_to('DCDataTransform');
        return;
    }

    var inputs = new Array();

    var formid = "";

    switch (optionId) {
        case 259:
            formid = "renamecolInput";
            break;
        case 251:
            formid = "dropcolInput";
            break;
        case 252:
            formid = "savecolInput";
            break;
        case 253:
            formid = "reordercolInput";
            break;
        case 254:
            formid = "copycolInput";
            break;
        case 255:
            formid = "sortcolInput";
            break;
        case 256:
            formid = "applylfntocolInput";
            break;
        case 217:
        case 218:
        case 257:
            formid = "maptransformInput";
            break;
        case 258:
            formid = "dummytransformInput";
            break;
        case 259:
            formid = "categorytransformInput";
            break;
    }

    // get the input values
    var formVals = get_input_form_parms(formid);

    console.log("formVals", formid, formVals);
    inputs.push(formVals);

    window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", optionId + "," + JSON.stringify(inputs)));
    window.clear_cell_output(window.CLEANSING_TASK_BAR_ID);
    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "0"));
    window.clear_cell_output(window.INSPECTION_TASK_BAR_ID);
    window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID, window.getJSPCode(window.INSPECTION_LIB, "display_data_inspection", "0"));
    window.scroll_to('DCDataTransform');

}


function change_dt_col_callback(selectid) {
    var selected_value = $("#" + selectid + " :selected").text();
    var inputs = new Array();
    inputs.push(selected_value);

    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "208" + "," + JSON.stringify(inputs)));
    window.scroll_to('DCDataTransform');
}

function change_na_option_callback(selectid) {

    var colname = $("#dtcolname :selected").text();
    var selected_value = $("#" + selectid + " :selected").text();
    var inputs = new Array();
    inputs.push(colname);
    inputs.push(selected_value);

    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "220" + "," + JSON.stringify(inputs)));
    window.scroll_to('DCDataTransform');
}

//----------------------------------------------------------------
// dynamic html for column transforms
//----------------------------------------------------------------
function change_col_stats_callback(selectid) {

    var selected_value = $("#" + selectid + " :selected").text();
    var inputs = new Array();
    inputs.push(selectid);
    inputs.push(selected_value);

    window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "change_col_stats", JSON.stringify(inputs)));
}

window.get_dfc_func_value = function(selectid) {
    /**
     * get selected value
     *
     * Parameters:
     *  selectid   - select form id
     */

    console.log("get_dfc_func_value", selectid);

    var inputs = new Array();
    var fparms = ["None", 2, 105];
    inputs.push(fparms);

    var importVals = get_input_form_parms("addcoldfcfuncInput");
    inputs.push(importVals);

    var selected_value = $("#" + selectid + " :selected").text();

    inputs.push(selectid);
    inputs.push(selected_value);

    window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(inputs)));
    window.scroll_to('DCDataTransform');

}

function get_apply_fn(selectid) {
    /**
     * get lambda fn
     *
     * Parameters:
     *  selectid   - select form id
     */

    var select_form_value = $("#" + selectid + " :selected").text();
    var colname = $("#" + "applycolname" + " :selected").text();

    var inputs = new Array();
    inputs.push(colname);
    inputs.push(select_form_value);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "217" + "," + JSON.stringify(inputs)));
    window.scroll_to('DCDataTransform');
}

function add_df_col_change_df(selectid) {
    /**
     * get lambda fn
     *
     * Parameters:
     *  selectid   - select form id
     * 
     */

    var dfname = $("#" + selectid + " :selected").text();

    var inputs = new Array();
    inputs.push(selectid);
    inputs.push(dfname);

    window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "get_add_df_col_change", JSON.stringify(inputs)));
}

function add_df_col_change_source_df(selectid) {
    /**
     * get lambda fn
     *
     * Parameters:
     *  selectid   - select form id
     */

    var select_form_value = $("#" + selectid + " :selected").text();
    var dfname = $("#" + "addcoldftitle" + " :selected").text();

    var inputs = new Array();
    inputs.push(1);
    inputs.push(dfname);
    inputs.push(select_form_value);
    window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "get_add_df_col_change", JSON.stringify(inputs)));
}

function change_apply_fn_col(selectid) {
    /**
     * change the column to apply fn to
     *
     * Parameters:
     *  formid   - form id
     */

    console.log("change_apply_fn_col", selectid);
    var inputs = new Array();

    var select_form_value = $("#" + selectid + " :selected").text();
    var colname = $("#" + "applycolname" + " :selected").text();

    inputs.push(colname);
    inputs.push(35);

    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify([inputs])));
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

function process_transform_datatype_callback(naoption, fid) {
    /**
     * Data Transform columns process cmd.
     *
     * Parameters:
     *  naoption  - na option : none fill drop
     *  fid       - function id : show uniques compat process return
     */

    console.log("process_transform_datatype_callback", naoption, fid);

    var inputs = new Array();
    //var element = document.getElementById("ucolscolumnname");
    //if (element != null) { inputs.push(element.value); } else { inputs.push("None"); }

    //var dtype = $("#dtdatatype :selected").text();
    //inputs.push(dtype);

    var dtparms = null;

    switch (naoption) {
        case 0:
            var dtparms = window.get_input_form_parms("dtdndatatypeinputt");
            break;
        case 1:
            var dtparms = window.get_input_form_parms("dtfndatatypeinput");
            break;
        case 2:
            var dtparms = window.get_input_form_parms("dtdatatypeinput");
            break;
    }


    switch (fid) {
        case 0:

            inputs.push(naoption);
            inputs.push(dtparms);

            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "221" + "," + JSON.stringify(inputs)));

            break;

        case 1:

            inputs.push(naoption);
            inputs.push(dtparms);

            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "222" + "," + JSON.stringify(inputs)));
            break;

        case 2:

            inputs.push(naoption);
            inputs.push(dtparms);

            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "262" + "," + JSON.stringify(inputs)));
            break;

        case 3:

            inputs.push(naoption);
            inputs.push(dtparms);

            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));

            break;
    }
    window.scroll_to('DCDataTransform');

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

function process_transform_check_compatability(fid) {
    /**
     * get check compatability.
     *
     * Parameters:
     *  fid    - function id
     */

    switch (fid) {

        case 0:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "223"));
            window.scroll_to('DCDataTransform');
            break;

        case 1:

            var inputs = new Array();
            var inputVals = get_input_form_parms("checkdtinput");
            inputs.push(inputVals);

            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "45" + "," + JSON.stringify(inputVals)));
            window.scroll_to('DCDataTransform');
            break;

        case 2:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "0"));
            window.scroll_to('DCDataTransform');
            break;

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

function setindexcol(colid) {
    var currentcolname = $("#newindex_colid");
    var current_columns = currentcolname.val();

    console.log("setindexcol", colid, current_columns);
    if (current_columns != null) {
        if (current_columns.length == 0) {
            current_columns = "[" + colid + "]";
        } else {
            current_columns = current_columns.replace("]", ",");
            current_columns = current_columns + colid + "]";
        }
    }

    currentcolname.val(current_columns);
}

function appendindexcol(colid) {
    var currentcolname = $("#appendindex_colid");
    var current_columns = currentcolname.val();

    console.log("appendindexcol", colid, current_columns);
    if (current_columns != null) {
        if (current_columns.length == 0) {
            current_columns = "[" + colid + "]";
        } else {
            current_columns = current_columns.replace("]", ",");
            current_columns = current_columns + colid + "]";
        }
    }

    currentcolname.val(current_columns);
}

function dropduplicatescol(colid) {
    var currentList = $("#dropduplicate_colids");
    var current_columns = currentList.val();

    console.log("dropduplicatescol", colid, current_columns);
    if (current_columns != null) {
        if (current_columns.length == 0) {
            current_columns = "[" + colid + "]";
        } else {
            current_columns = current_columns.replace("]", ",");
            current_columns = current_columns + colid + "]";
        }
    }

    currentList.val(current_columns);
}

function setformat(fstring) {
    var formatstring = $("#dtformatstring");
    formatstring.val(fstring);
}

function change_col_for_check_callback(selectid) {

    var selected_value = $("#" + selectid + " :selected").text();
    var inputs = new Array();
    inputs.push(selected_value);

    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "222" + "," + JSON.stringify(inputs)));
    window.scroll_to('DCDataTransform');

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
 * df schema dynamic html
 --------------------------------------
*/

function dfsch_changedt(colid) {
    /**
     * Data Inspection change datatype.
     *
     * Parameters:
     *  colid - column id
     */

    var inputs = new Array();
    inputs.push(colid);

    window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "208" + ", " + JSON.stringify(inputs)));
    window.scroll_to('DCDataTransform');
}

dfsch_chkcompat

function dfsch_chkcompat(colid) {
    /**
     * Data Inspection check compatability.
     *
     * Parameters:
     *  colid - column id
     */

    var inputs = new Array();
    inputs.push(colid);

    window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "222" + ", " + JSON.stringify(inputs)));
    window.scroll_to('DCDataTransform');
}