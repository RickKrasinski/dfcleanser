
//
// 
// ------------------------------------------------------
// Data Export Chapter javascript functions
// ------------------------------------------------------
//
// 

function export_taskbar_callback(fid) {
    /**
    * Data Export main taskbar.
    *
    * Parameters:
    *  fid - function id
    */
    switch (fid) {
        case 0: window.run_code_in_cell(window.EXPORT_TASK_BAR_ID,window.getJSPCode(window.EXPORT_LIB,"display_export_forms",1));   break;
        case 1: window.run_code_in_cell(window.EXPORT_TASK_BAR_ID,window.getJSPCode(window.EXPORT_LIB,"display_export_forms",3));   break;
        case 2:
            window.delete_output_cell(window.EXPORT_CUSTOM_CODE_ID);
            window.run_code_in_cell(window.EXPORT_TASK_BAR_ID,window.getJSPCode(window.EXPORT_LIB,"display_export_forms","0"));
            break;
    }
    window.scroll_to('DCDataExport');
}

function pandas_export_tb_select_callback(id) {
    /**
    * Pandas Export main taskbar.
    *
    * Parameters:
    *  id - import type
    */
    window.run_code_in_cell(window.EXPORT_TASK_BAR_ID,window.getJSPCode(window.EXPORT_LIB,"display_export_forms",(2 + "," + id)));
    window.scroll_to('DCDataExport');
}

function pandas_export_tb_return_callback() {
    /**
    * Pandas Export return callback.
    */
    window.delete_output_cell(window.EXPORT_CUSTOM_CODE_ID);
    window.run_code_in_cell(window.EXPORT_TASK_BAR_ID,window.getJSPCode(window.EXPORT_LIB,"display_export_forms","0"));
    window.scroll_to('DCDataExport');
}

function pandas_details_export_callback(id) {
    /**
    * Pandas Export display details.
    *
    * Parameters:
    *  id - import type
    */
    var formid = "";
    switch (id) {
        case 0: formid = "exportPandasCSV";         break;
        case 1: formid = "exportPandasExcel";       break;
        case 2: formid = "exportPandasJSON";        break;
        case 3: formid = "exportPandasHTML";        break;
        case 4: formid = "exportPandasSQLTable";    break;
    }
    var importVals = get_input_form_parms(formid);
    window.run_code_in_cell(window.EXPORT_TASK_BAR_ID,window.getJSPCode(window.EXPORT_LIB,"process_export_form",(id + ", " + importVals)));
    window.scroll_to('DCDataExport');
}

function pandas_details_export_clear_callback(id) {
    /**
    * Pandas Export details clear.
    *
    * Parameters:
    *  id - import type
    */
    window.run_code_in_cell(window.EXPORT_TASK_BAR_ID,window.getJSPCode(window.EXPORT_LIB,"display_export_forms","2" + ", " + id));
    window.scroll_to('DCDataExport');
}

function pandas_details_export_return_callback() {
    /**
    * Pandas Export details return.
    */
    window.delete_output_cell(window.window.EXPORT_CUSTOM_CODE_ID);
    window.run_code_in_cell(window.EXPORT_TASK_BAR_ID,window.getJSPCode(window.EXPORT_LIB,"display_export_forms","1"));
    window.scroll_to('DCDataExport');
}

function pandas_details_export_help_callback(id) {
    /**
    * Pandas Export details help.
    *
    * Parameters:
    *  id - import type
    */
    var command = window.getJSPCode(window.EXPORT_LIB,"handle_pandas_details_export_click_help",id);
    var kernel = IPython.notebook.kernel;
    kernel.execute(command);
}

//
// -------------------------------------
// Custom Export callbacks
// -------------------------------------
//
function custom_export_callback(fid) {
    /**
    * Custom Export callback.
    *
    * Parameters:
    *  fid - function id
    */
    switch (fid) {
        case 0:
            window.delete_output_cell(window.EXPORT_CUSTOM_CODE_ID);
            window.run_code_in_cell(window.EXPORT_TASK_BAR_ID,window.getJSPCode(window.EXPORT_LIB,"display_export_forms",3));
            window.select_cell(EXPORT_TASK_BAR_ID);
            IPython.notebook.insert_cell_below('code');
            var cell = IPython.notebook.select_next().get_selected_cell();
            var code =  "# custom export" + NEW_LINE +
                        "from dfcleanser.common.cfg import get_dfc_dataframe" + NEW_LINE +
                        "df = get_dfc_dataframe()" + NEW_LINE + NEW_LINE;
            window.run_code(cell, code);
            break;
        case 1:
            var inputs = new Array();
            inputs.push(1)
            var code = document.getElementById("customExportCode").value;
            if (code.indexOf("# custom export") != -1) {
                code = code.replace("# custom export\n", "");
            }
            inputs.push(String(code));
            window.delete_output_cell(window.EXPORT_CUSTOM_CODE_ID);
            window.run_code_in_cell(window.EXPORT_TASK_BAR_ID, window.getJSPCode(window.EXPORT_LIB,"process_export_form","5," + JSON.stringify(inputs)));
            break;
        case 2:
            var inputs = new Array();
            inputs.push(2)
            var custom_cell = window.get_cell_for_id(EXPORT_CUSTOM_CODE_ID);
            var custom_code = custom_cell.get_text();
            if (custom_code.indexOf("# custom export") != -1) {
                custom_code = custom_code.replace("# custom export\n", "");
            }
            inputs.push(String(custom_code));
            window.run_code_in_cell(window.EXPORT_TASK_BAR_ID,window.getJSPCode(window.EXPORT_LIB,"process_export_form","5," + JSON.stringify(inputs)));
            break;
        case 3:
            var inputs = new Array();
            inputs.push(3);
            window.delete_output_cell(window.EXPORT_CUSTOM_CODE_ID);
            window.run_code_in_cell(window.EXPORT_TASK_BAR_ID,window.getJSPCode(window.EXPORT_LIB,"process_export_form", "5," + JSON.stringify(inputs)));
            break;
        case 4:
            window.delete_output_cell(window.EXPORT_CUSTOM_CODE_ID);
            window.run_code_in_cell(window.EXPORT_TASK_BAR_ID,window.getJSPCode(window.EXPORT_LIB, "display_export_forms",0));
            break;
        case 5:
            var inputs = new Array();
            inputs.push(5);
            window.delete_output_cell(window.EXPORT_CUSTOM_CODE_ID);
            window.run_code_in_cell(window.EXPORT_TASK_BAR_ID,window.getJSPCode(window.EXPORT_LIB, "process_export_form","5," + JSON.stringify(inputs)));
            break;
    }
    window.scroll_to('DCDataExport');
}


function pandas_details_export_test_con_callback(dbid, driverid) {
    /**
    * Export db connector test.
    *
    * Parameters:
    *  dbid     - database id
    *  driverid - database driver id
    */
     
    var sqlinputparms = null;
    switch (dbid) {
        case 0: sqlinputparms = window.get_input_form_parms("MySQLdbconnector");        break;
        case 1: sqlinputparms = window.get_input_form_parms("MSSQLServerdbconnector");  break;
        case 2: sqlinputparms = window.get_input_form_parms("SQLitedbconnector");       break;
        case 3:sqlinputparms = window.get_input_form_parms("Postgresqldbconnector");    break;
        case 4:sqlinputparms = window.get_input_form_parms("Oracledbconnector");        break;
    }
    if (sqlinputparms != null) {
        window.run_code_in_cell(window.EXPORT_TASK_BAR_ID,window.getJSPCode(window.EXPORT_LIB,"test_export_sql_db_connector",driverid + ", " + sqlinputparms));
    }
    window.scroll_to('DCDataExport');
}


function pandas_sql_export_callback(dbid) {
    /**
    * Export sql export display callback.
    *
    * Parameters:
    *  dbid     - database id
    */
    var formid = "";
    switch (dbid) {
        case 0: formid = "MySQLdbconnector";        break;
        case 1: formid = "MSSQLServerdbconnector";  break;
        case 2: formid = "SQLitedbconnector";       break;
        case 3: formid = "Postgresqldbconnector";   break;
        case 4: formid = "Oracledbconnector";       break;
        case 5: formid = "Customdbconnector";       break;
    }
    // get the input values
    var connectVals = get_input_form_parms(formid);
    var inputs = new Array();
    window.run_code_in_cell(window.EXPORT_TASK_BAR_ID,window.getJSPCode(window.EXPORT_LIB,"display_pandas_export_sql_inputs",("2," + dbid + "," + connectVals + "," + JSON.stringify(inputs))));
    window.scroll_to('DCDataExport');
}

function pandas_export_sql_callback(fid) {
    /**
    * Export sql export process callback.
    *
    * Parameters:
    *  dbid     - database id
    */
    var inputParms = window.get_input_form_parms("exportPandasSQLTable");
    switch (fid) {
        case 0:
        case 1:
            var connectVals = new Array();
            window.run_code_in_cell(window.EXPORT_TASK_BAR_ID,window.getJSPCode(window.EXPORT_LIB,"display_pandas_export_sql_inputs",(fid + ", -1, " + JSON.stringify(connectVals) + ", " + inputParms)));
            break;
        case 2: window.run_code_in_cell(window.EXPORT_TASK_BAR_ID,window.getJSPCode(window.EXPORT_LIB,"export_sql_table",inputParms)); break;
    }
    window.reset_dependents([false, true, true, true, false, false]);
    window.scroll_to('DCDataExport');
}

//
// -------------------------------------
// Custom Export DHTML callbacks
// -------------------------------------
//
function select_export_table(tablename) {
    var table_name = $("#exportsqltableName");
    table_name.val(tablename);
}

function select_export_column(columnname) {
    var column = $("#exportsqltableindexlabel");
    if (column.val() == "") {
        console.log("empty")
        column.val("[" + columnname + "]");
    } else {
        var slen = column.val().length;
        var newstring = column.val().substr(0, slen - 1) + ", " + columnname + "]";
        column.val(newstring);
    }
}
