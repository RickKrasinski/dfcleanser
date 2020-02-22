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

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "transform_task_bar_callback", fid);

    switch (fid) {
        case -1:
            var inputs = new Array();
            inputs.push([4]);
            var inputParms = window.get_input_form_parms("datainspectdf");
            inputs.push(inputParms);

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

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "df_transform_task_bar_callback", optionId);

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

    dfc_log("df_process_cmd_callback" + optionId.toString())

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
        case 125:
            formid = "sortcolInput";
            break;
        case 127:
            formid = "remwhitetransformInput";
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
        window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", optionId + "," + inputs));
    }

    window.scroll_to('DCDataTransform');
}


function chcolname(cname) {
    /**
     * set column name.
     *
     * Parameters:
     *  cname          - column name
     */

    if (window.debug_detail_flag)
        console.log("chcolname", cname);

    $('#ccolname').val(cname);

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

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "cols_transform_tb_callback", fid);

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

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "data_transform_display_add_cols_callback", optionId);

    var inputs = new Array();
    var formid;
    var fparms;

    if (optionId == 412) {
        window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
        window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", 0));
        window.scroll_to('DCDataTransform');
        return;
    }
    switch (optionId) {
        case 402:
            formid = "addcoldfcfuncInput";

            fparms = get_input_form_parms("addcoldfcfuncInput");
            if (fparms.length < 10) {
                fparms = get_input_form_parms("addcoldfcdfcolInput");
                if (fparms.length < 10) {
                    fparms = get_input_form_parms("addcoldfcdfcolnumInput");
                    if (fparms.length < 10) {
                        fparms = get_input_form_parms("addcoldfcdfcolnumnumInput");
                        if (fparms.length < 10) {
                            formid = "addcoldfcdfnumnumInput";
                        } else
                            formid = "addcoldfcdfcolnumnumInput";
                    } else
                        formid = "addcoldfcdfcolnumInput";
                } else
                    formid = "addcoldfcdfcolInput";
            } else
                formid = "addcoldfcfuncInput";

            break;

        case 404:
            formid = "addcolcodefnInput";
            fparms = get_input_form_parms("addcolcodefnInput");

            if (fparms.length < 10) {
                formid = "addcolInput";
            } else formid = "addcolcodefnInput";
            break;

        default:
            formid = "addcolInput";
            break;
    }

    addvals = get_input_form_parms(formid);
    inputs.push(addvals);

    window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", optionId + "," + inputs));
    window.scroll_to('DCDataTransform');
}

function data_transform_add_cols_callback(optionId) {
    /**
     * columns transform taskbar callback.
     *
     * Parameters:
     *  optionId   - option id
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "data_transform_add_cols_callback", optionId);

    var inputs = new Array();
    var formid = "";

    switch (optionId) {
        case 401:
            formid = "addcolfileInput";
            break;
        case 403:
            formid = "addcolcodeInput";
            break;
        case 406:
            formid = "addcoldfcfuncInput";
            break;
        case 408:
            formid = "addcoldfSourceInput";
            break;
        case 420:
            formid = "maintainuserfnsInput";
            break;
        case 421:
            formid = "addcolcodefnInput";
            break;
        case 422:
            var fparms = get_input_form_parms("addcolcodefnInput");

            if (fparms.length < 10) {
                formid = "maintainuserfnsInput";
            } else formid = "addcolcodefnInput";
            break;
    }

    if (formid != "") {
        var importVals = get_input_form_parms(formid);
        inputs.push(importVals);
    }

    switch (optionId) {
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
        case 420: // delete user fns
        case 421: // maintain user fns
        case 422:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", optionId + "," + inputs));
            window.scroll_to('DCDataTransform');
            break;
        case 408: // add new column from df 

            formid = "addcoldfOutputInput";
            importVals = get_input_form_parms(formid);
            inputs.push(importVals);

            formid = "addcoldfInput";
            importVals = get_input_form_parms(formid);
            inputs.push(importVals);

            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", optionId + "," + JSON.stringify(inputs)));
            window.scroll_to('DCDataTransform');
            break;
        case 430:
        case 431:
            inputs.push(optionId);
            window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "clear_add_col_df", JSON.stringify(inputs)));
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

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "data_transform_add_cols_generic", funcid, gtid);

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

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "data_transform_process_cols_callback", optionId);

    if (optionId == 216) {
        window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", 0));
        window.scroll_to('DCDataTransform');
        return;
    }

    var inputs = new Array();

    var formid = "";

    switch (optionId) {
        case 214:
            formid = "applyfncolInput";
            break;
        case 215:
            formid = "applyldfccolInput";
            break;
        case 217:
            formid = "applyldfccolInput";
            break;
        case 218:
            formid = "applyfncolInput";
            break;
        case 250:
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
        case 257:
        case 258:
        case 259:
            formid = "maptransformInput";
            break;
        case 260:
            formid = "dummytransformInput";
            break;
        case 261:
            formid = "categorytransformInput";
            break;
        case 262:
            formid = "categorytransformexcludeInput";
            break;
        case 273:
            formid = "savecolindxInput";
            break;

    }

    // get the input values
    var formVals = get_input_form_parms(formid);
    inputs.push(formVals);

    window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", optionId + "," + inputs));
    window.clear_cell_output(window.CLEANSING_TASK_BAR_ID);
    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID, window.getJSPCode(window.CLEANSING_LIB, "display_data_cleansing", "0"));
    window.clear_cell_output(window.INSPECTION_TASK_BAR_ID);
    window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID, window.getJSPCode(window.INSPECTION_LIB, "display_data_inspection", "0"));
    window.scroll_to('DCDataTransform');

}

//----------------------------------------------------------------
// dynamic html for column transforms
//----------------------------------------------------------------
function add_df_col_df_change(selectid) {
    /**
     * column change for add col
     *
     * Parameters:
     *  selectid   - select form id
     * 
     */

    var selected_value = $("#" + selectid + " :selected").text();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "add_df_col_df_change", selected_value);

    var inputs = new Array();
    inputs.push(selectid);
    inputs.push(selected_value);

    window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "add_col_from_df_change_df", JSON.stringify(inputs)));
}

function change_user_func_value(selectid) {
    /**
     * column change for add col
     *
     * Parameters:
     *  selectid   - select form id
     * 
     */

    var selected_value = $("#" + selectid + " :selected").text();
    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "change_user_func_value", selected_value);

    var inputs = get_input_form_parms("maintainuserfnsInput");

    window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", 421 + "," + inputs));
    window.scroll_to('DCDataTransform');
}

function add_df_col_change_col(selectid) {
    /**
     * column change for add col
     *
     * Parameters:
     *  selectid   - select form id
     * 
     */

    var selected_value = $("#" + selectid + " :selected").val();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "add_df_col_change_col", selected_value);

    var inputs = new Array();

    if (selectid == "addcolsourceindex") {

        var current_sindex_list = $("#addcoldfsourceindexlist").val();

        if (current_sindex_list == "[]") {
            $("#addcoldfsourceindexlist").val("[" + selected_value + "]");
        } else {
            current_sindex_list = current_sindex_list.replace("]", ", ");
            current_sindex_list = current_sindex_list + selected_value + "]";
            $("#addcoldfsourceindexlist").val(current_sindex_list);
        }
    } else {

        var current_oindex_list = $("#addcoldfoutputindexlist").val();

        if (current_oindex_list == "[]") {
            $("#addcoldfoutputindexlist").val("[" + selected_value + "]");
        } else {
            current_oindex_list = current_oindex_list.replace("]", ", ");
            current_oindex_list = current_oindex_list + selected_value + "]";
            $("#addcoldfoutputindexlist").val(current_oindex_list);
        }
    }
}

function add_df_change_col_source(selectid) {
    /**
     * column change for add col
     *
     * Parameters:
     *  selectid   - select form id
     * 
     */

    var selected_value = $("#" + selectid + " :selected").text();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "add_df_change_col_source", selected_value);

    var inputs = new Array();
    inputs.push(selectid);

    var selected_df = $("#addcolsourcedftitle :selected").text();
    inputs.push(selected_df);

    inputs.push(selected_value);

    window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "change_add_col_df_source_col", JSON.stringify(inputs)));
}

function select_reorder_cols(colid) {
    /**
     * column change for reorder col
     *
     * Parameters:
     *  selectid   - select form id
     * 
     */

    var movecol = $("#moveColumnname").val();
    var moveaftercol = $("#moveafterColumnname").val();

    if (movecol.length == 0) {
        $("#moveColumnname").val(colid);
        $("#moveafterColumnname").val("");
    } else {
        if (moveaftercol.length == 0) {
            $("#moveafterColumnname").val(colid);
        } else {
            $("#moveColumnname").val(colid);
            $("#moveafterColumnname").val("");
        }
    }
}

function change_dt_col_callback(selectid) {
    /**
     * column change datatype
     *
     * Parameters:
     *  selectid   - select form id
     * 
     */

    var selected_value = $("#" + selectid + " :selected").text();
    var inputs = new Array();
    inputs.push(selected_value);

    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "208" + "," + JSON.stringify(inputs)));
    window.scroll_to('DCDataTransform');
}

function change_na_option_callback(selectid) {
    /**
     * column change na option
     *
     * Parameters:
     *  selectid   - select form id
     * 
     */

    var colname = $("#dtcolname :selected").text();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "change_col_stats_callback", colname);

    var selected_value = $("#" + selectid + " :selected").text();
    var inputs = new Array();
    inputs.push(colname);
    inputs.push(selected_value);

    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "220" + "," + JSON.stringify(inputs)));
    window.scroll_to('DCDataTransform');
}

function change_apply_col_stats_callback(selectid) {
    /**
     * column change column stats
     *
     * Parameters:
     *  selectid   - select form id
     * 
     */

    var selected_values = $("#" + selectid).val();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "change_apply_col_stats_callback", selected_values);

    switch (selectid) {

        case "applycolname":
            var inputParms = window.get_input_form_parms("applyldfccolInput");
            var option = 214;
            break;

        case "applyfncolname":
            var inputParms = window.get_input_form_parms("applyfncolInput");
            var option = 215;
            break;

    }

    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", option + "," + inputParms));
    window.scroll_to('DCDataTransform');
}






function change_col_stats_callback(selectid) {
    /**
     * column change column stats
     *
     * Parameters:
     *  selectid   - select form id
     * 
     */

    var selected_values = $("#" + selectid).val();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "change_col_stats_callback", selectid, selected_values);

    var inputs = new Array();
    inputs.push(selectid);

    if ((selectid == "savecolname") ||
        (selectid == "saveColumnindexname") ||
        (selectid == "dropcolInputname")) {

        inputs.push(selected_values[selected_values.length - 1]);

        if (selectid == "savecolname") {

            var file_names = "[";

            for (i = 0; i < selected_values.length; i++) {
                var fname = selected_values[i].replace(/ /g, "_");
                fname = fname.replace(".", "_");
                file_names = file_names + "'" + fname + "'";

                if ((i + 1) != selected_values.length) {
                    file_names = file_names + ",";
                }
            }

            file_names = file_names + "]";

            $("#savefilename").val(file_names);
        } else {
            if (selectid == "dropcolInputname") {

                var saveflag = $("#dropsavedroppedflag").val();

                if (saveflag == "True") {

                    var file_names = "[";

                    for (i = 0; i < selected_values.length; i++) {
                        var fname = selected_values[i].replace(/ /g, "_");
                        fname = fname.replace(".", "_");
                        file_names = file_names + "'" + fname + "'";

                        if ((i + 1) != selected_values.length) {
                            file_names = file_names + ",";
                        }
                    }

                    file_names = file_names + "]";
                    $("#dropColumnfname").val(file_names);
                } else {
                    $("#dropColumnfname").val("");
                }
            }
        }
    } else {
        inputs.push(selected_values);
    }

    window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "change_col_stats", JSON.stringify(inputs)));
}

window.get_dfc_func_value = function(selectid) {
    /**
     * get selected value
     *
     * Parameters:
     *  selectid   - select form id
     */

    switch (selectid) {

        case "addcolfuncs":
            var importVals = get_input_form_parms("addcoldfcfuncInput");
            break;

        case "addcolfuncsdfcol":
        case "addcoldftitledfcol":
            var importVals = get_input_form_parms("addcoldfcdfcolInput");
            break;

        case "addcolfuncsdfcolnum":
        case "addcoldftitledfcolnum":
            var importVals = get_input_form_parms("addcoldfcdfcolnumInput");
            break;

        case "addcolfuncsdfcolnumnum":
        case "addcoldftitledfcolnumnum":
            var importVals = get_input_form_parms("addcoldfcdfcolnumnumInput");
            break;

        case "addcolfuncsdfnumnum":
        case "addcoldftitledfnumnum":
            var importVals = get_input_form_parms("addcoldfcdfnumnumInput");
            break;
    }

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "get_dfc_func_value", selectid, importVals);

    var inputs = new Array();
    inputs.push(importVals);

    window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "405" + "," + inputs));
    window.scroll_to('DCDataTransform');

}

function get_apply_fn(selectid) {
    /**
     * get apply fn
     *
     * Parameters:
     *  selectid   - select form id
     */

    var select_form_value = $("#" + selectid + " :selected").text();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "get_apply_fn", select_form_value);

    var colname = $("#" + "applycolname" + " :selected").text();

    var parms = window.get_input_form_parms("applyldfccolInput");

    //var inputs = new Array();
    //inputs.push(colname);
    //inputs.push(select_form_value);

    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "219" + "," + parms));
    window.scroll_to('DCDataTransform');
}

function add_df_col_change_df(selectid) {
    /**
     * add col df change
     *
     * Parameters:
     *  selectid   - select form id
     * 
     */

    var dfname = $("#" + selectid + " :selected").text();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "add_df_col_change_df", dfname);

    var inputs = new Array();
    inputs.push(selectid);
    inputs.push(dfname);

    window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "get_add_df_col_change", JSON.stringify(inputs)));
}

function add_df_col_change_source_df(selectid) {
    /**
     * add col change source df
     *
     * Parameters:
     *  selectid   - select form id
     */

    var select_form_value = $("#" + selectid + " :selected").text();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "add_df_col_change_source_df", select_form_value);

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

    var inputs = new Array();

    var select_form_value = $("#" + selectid + " :selected").text();
    var colname = $("#" + "applycolname" + " :selected").text();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "change_apply_fn_col", select_form_value);

    inputs.push(colname);
    inputs.push(35);

    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify([inputs])));
    window.scroll_to('DCDataTransform');

}

function get_user_func_value(selectid) {
    /**
     * change the fn to add column
     *
     * Parameters:
     *  selectid   - select id
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "get_user_func_value");

    var inputs = new Array();
    var formVals = get_input_form_parms("addcolcodefnInput");

    inputs.push(formVals);

    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "423" + "," + inputs));
    window.scroll_to('DCDataTransform');

}

function process_cols_dropna_fillna_transform_callback(fid) {
    /**
     * columns process fillna dropna option.
     *
     * Parameters:
     *  fid       - function id
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "process_cols_dropna_fillna_transform_callback", fid);

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

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "process_transform_datatype_callback", naoption, fid);

    var inputs = new Array();
    var dtparms = null;

    switch (naoption) {
        case 0:
            var dtparms = window.get_input_form_parms("dtdndatatypeinput");
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

            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "222" + "," + dtparms));
            break;

        case 2:

            inputs.push(naoption);
            inputs.push(dtparms);

            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "270" + "," + JSON.stringify(inputs)));
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

function select_exclude_unique(uniqueid) {
    /**
     * col category exclude unique.
     *
     * Parameters:
     *  uniqueid  - boolean flag
     */

    var current_exclude = $("#excludeuniques").val();
    if (current_exclude == "[]")
        current_exclude = current_exclude.replace("]", uniqueid.toString() + "]");
    else
        current_exclude = current_exclude.replace("]", "," + uniqueid.toString() + "]");
    $("#excludeuniques").val(current_exclude);

}


function change_category_callback(selectid) {
    /**
     * col category change name
     *
     * Parameters:
     *  selectid  - select id
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "change_category_callback");

    if (selectid == "catexcludecolumnname") {
        var fparms = window.get_input_form_parms("categorytransformexcludeInput");
        window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
        window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "224, " + fparms));

    } else {
        var fparms = window.get_input_form_parms("categorytransformInput");
        window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
        window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "207, " + fparms));
    }
}


function exclude_uniques_callback(selectid) {
    /**
     * col category exclude uniques callback
     *
     * Parameters:
     *  selectid  - select id
     */

    var exflag = $("#" + selectid + " :selected").text();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "exclude_uniques_callback", exflag);

    if (exflag == "False") {
        var fparms = window.get_input_form_parms("categorytransformInput");
        window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
        window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "224, " + fparms));
    }
}

function col_checknum(colid) {
    /**
     * Check if column numeric.
     *
     * Parameters:
     *  colid - column id
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "col_checknum", colid);

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

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "select_applyfn_gen_function", genid);

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

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "select_addcol_gen_function", genid);

    var inputs = new Array();
    var fparms = ["None", 2, 16];
    inputs.push(fparms);
    inputs.push(genid);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "11" + "," + JSON.stringify(inputs)));
    window.scroll_to('DCDataTransform');
}

function get_gf_fn(genid) {
    /**
     * get gen func to display.
     *
     * Parameters:
     *  genid       - generic function id
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "get_gf_fn", genid);

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

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "single_col_categorical_callback", optionId);

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

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "display_map_inputs_callback", colId);

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

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "dtctcol", colid, option);

    if (option == 30) {
        var fparms = ["3", colid, option];
    } else {
        var fparms = [colid, option];
    }

    var inputs = new Array();
    inputs.push(fparms);

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

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "process_transform_check_compatability", fid);

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

            var inputs = new Array();
            var inputVals = get_input_form_parms("checkstrdtinput");
            inputs.push(inputVals);

            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "45" + "," + JSON.stringify(inputVals)));
            window.scroll_to('DCDataTransform');
            break;

        case 3:
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

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "process_datetime_format_transform_callback", fid);

    var inputs = new Array();

    switch (fid) {
        case 14:
        case 15:
            var fparms = window.get_input_form_parms("datetimeformatinput");
            inputs.push(fparms);
            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", fid + "," + inputs));
            break;
        case 17:
            var fparms = window.get_input_form_parms("timedeltaformatinput");
            inputs.push(fparms);
            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", fid + "," + inputs));
            break;
        case 23:
            var fparms = window.get_input_form_parms("timedeltaformatinput");
            inputs.push(fparms);
            window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", fid + "," + inputs));
            break;
        case 26:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", fid));
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

    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", optionId));
    window.scroll_to('DCDataTransform');
}

function change_convert_dtype_callback(selectid) {
    /**
     * change convert datetime column callback.
     *
     * Parameters:
     *  optionId  - option id
     */

    var selected_value = $("#" + selectid + " :selected").text();
    var newcolname = $("#dttdrescolname").val();
    var units = $("#dttdunits").val();

    if (selected_value == "timedelta") {
        $("#dttdunits").prop("disabled", true);
        units = "timedelta";
    } else {
        $("#dttdunits").prop("disabled", false);
    }

    var found = newcolname.indexOf("_timedelta");

    if (newcolname.indexOf("_timedelta") > -1) { newcolname = newcolname.replace("_timedelta", "_" + units); } else {
        if (newcolname.indexOf("_Days") > -1) { newcolname = newcolname.replace("_Days", "_" + units); } else {
            if (newcolname.indexOf("_Hours") > -1) { newcolname = newcolname.replace("_Hours", "_" + units); } else {
                if (newcolname.indexOf("_Minutes") > -1) { newcolname = newcolname.replace("_Minutes", "_" + units); } else {
                    if (newcolname.indexOf("_Seconds") > -1) { newcolname = newcolname.replace("_Seconds", "_" + units); } else {
                        if (newcolname.indexOf("_MilliSeconds") > -1) { newcolname = newcolname.replace("_MilliSeconds", "_" + units); } else {
                            if (newcolname.indexOf("_MicroSeconds") > -1) { newcolname = newcolname.replace("_MicroSeconds", "_" + units); }
                        }
                    }
                }
            }
        }
    }

    $("#dttdrescolname").val(newcolname);

}

function change_convert_units_callback(selectid) {
    /**
     * change convert datetime column callback.
     *
     * Parameters:
     *  selectid  - select id
     */

    var units = $("#" + selectid + " :selected").text();
    var colname = $("#dttdrescolname").val();

    if (colname.indexOf("_Days") > -1) { colname = colname.replace("_Days", "_" + units); } else {
        if (colname.indexOf("_Hours") > -1) { colname = colname.replace("_Hours", "_" + units); } else {
            if (colname.indexOf("_Minutes") > -1) { colname = colname.replace("_Minutes", "_" + units); } else {
                if (colname.indexOf("_Seconds") > -1) { colname = colname.replace("_Seconds", "_" + units); } else {
                    if (colname.indexOf("_MilliSeconds") > -1) { colname = colname.replace("_MilliSeconds", "_" + units); } else {
                        if (colname.indexOf("_MicroSeconds") > -1) { colname = colname.replace("_MicroSeconds", "_" + units); }
                    }
                }
            }
        }
    }

    $("#dttdrescolname").val(colname);

}


function change_component_callback(selectid) {
    /**
     * change component change callback.
     *
     * Parameters:
     *  selectid  - select id
     */

    var component = $("#dtccomptype :selected").text();
    var colname = $("#dtcdatetimecolname :selected").text();

    if (component == "week of year") component = "week_of_year"
    else
    if (component == "day of year") component = "day_of_year"
    else
    if (component == "day of week") component = "day_of_week"

    $("#dtcresultcolname").val(colname + "_" + component);

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

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "process_datetime_tdelta_callback", optionId);

    switch (optionId) {
        case 22:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", optionId + "," + inputs));
            break;
        case 23:
            var inputs = new Array();
            var formatVals = get_input_form_parms("datetimetdeltainput");
            inputs.push(formatVals);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", optionId + "," + inputs));
            break;
        case 26:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", optionId));
            break;
    }
    window.scroll_to('DCDataTransform');
}

function process_datetime_merge_split_callback(optionId) {
    /**
     * process merge split command.
     *
     * Parameters:
     *  optionId  - option
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "process_datetime_merge_split_callback", optionId);

    switch (optionId) {
        case 19:
            var inputs = new Array();
            var fparms = get_input_form_parms("datetimetmergeinput");
            inputs.push(fparms);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", optionId + "," + inputs));
            break;
        case 21:
            var inputs = new Array();
            var fparms = get_input_form_parms("datetimetsplitinput");
            inputs.push(fparms);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", optionId + "," + inputs));
            break;
        case 18:
        case 20:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", optionId));
            break;
        case 26:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", optionId));
            break;
    }
    window.scroll_to('DCDataTransform');
}

function process_datetime_components_callback(optionId) {
    /**
     * process datetime components.
     *
     * Parameters:
     *  optionId  - option
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "process_datetime_components_callback", optionId);

    switch (optionId) {
        case 25:
            var inputs = new Array();
            var fparms = get_input_form_parms("datetimecompinput");
            inputs.push(fparms);
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", optionId + "," + inputs));
            break;
        case 26:
            window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", optionId));
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
    /**
     * process dropna change.
     *
     * Parameters:
     *  dropid  - drop type
     */

    var selected_value = $("#" + dropid + " :selected").text();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "dtselect_dropna_change", selected_value);

    var inputs = new Array();
    inputs.push(selected_value);

    window.clear_cell_output(window.TRANSFORM_TASK_BAR_ID);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID, window.getJSPCode(window.TRANSFORM_LIB, "display_data_transform", "38" + ", " + JSON.stringify(inputs)));
    window.scroll_to('DCDataTransform');

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