
//
// 
// ------------------------------------------------------
// Data Import javascript functions
// ------------------------------------------------------
//
// 

function import_taskbar_callback(fid) {
    /**
    * Data Import main taskbar callback.
    *
    * Parameters:
    *  fid - function id
    */ 
    switch (fid) {
        case 0: window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"display_import_forms",1));   break;
        case 1: window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"display_import_forms",3));   break;
        case 2:
            window.delete_output_cell(window.IMPORT_CUSTOM_CODE_ID);
            window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"display_import_forms","0")); break;
    }
    window.scroll_to('DCDataImport');
}

function pandas_import_tb_select_callback(id) {
    /**
    * Pandas Import taskbar callbacks.
    *
    * Parameters:
    *  id - import type
    */ 
    window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"display_import_forms",2 + "," + id));
    window.scroll_to('DCDataImport');
}

function pandas_import_tb_return_callback() {
    /**
    * Pandas Import taskbar return.
    */ 
    window.delete_output_cell(window.window.IMPORT_CUSTOM_CODE_ID);
    window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"display_import_forms", 0));
    window.scroll_to('DCDataImport');
}

function pandas_details_import_callback(id) {
    /**
    * Pandas Details Import taskbar callback.
    *
    * Parameters:
    *  id - import type
    */ 
    var formid = "";
    switch (id) {
        case 0: formid = "importPandasCSV";     break;
        case 1: formid = "importPandasFWF";     break;
        case 2: formid = "importPandasExcel";   break;
        case 3: formid = "importPandasJSON";    break;
        case 4: formid = "importPandasHTML";    break;
    }

    // get the input values
    var importVals = get_input_form_parms(formid);
    window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"process_import_form",id + ", " + importVals));
    reset_dependents([false, true, true, true, true, true]);
    window.scroll_to('DCDataImport');
}

function pandas_details_clear_callback(id) {
    /**
    * Pandas Details Import clear inputs callback.
    *
    * Parameters:
    *  id - import type
    */ 
    window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"display_import_forms","2" + ", " + id));
    window.scroll_to('DCDataImport');
}

function pandas_details_return_callback() {
    /**
    * Pandas Details Import return callback.
    */ 
    window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"display_import_forms","1"));
    window.scroll_to('DCDataImport');
}

function pandas_sql_import_callback(itype, dbid) {
    /**
    * Pandas sql Import callbacks.
    *
    * Parameters:
    *  itype - import type
    *  dbid  - database id
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
    var importVals = get_input_form_parms(formid);
    if (itype == 0) {window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"display_pandas_import_sql_inputs","5,0" + "," + dbid + "," + importVals));} 
    else {window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"display_pandas_import_sql_inputs","6,0" + "," + dbid + "," + importVals));}
    window.scroll_to('DCDataImport');
}

function custom_import_callback(fid) {
    /**
    * Custom Import callbacks.
    *
    * Parameters:
    *  fid  - function id
    */
    
    switch (fid) {
        case 0:
            window.delete_output_cell(window.IMPORT_CUSTOM_CODE_ID);
            window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"display_import_forms",3));

            IPython.notebook.insert_cell_below('code');
            var cell = IPython.notebook.select_next().get_selected_cell();

            var code = "# custom import" + NEW_LINE +
                       "df = None" + NEW_LINE + NEW_LINE +
                       "from dfcleanser.common.cfg import set_dc_dataframe" + NEW_LINE +
                       "set_dc_dataframe(df)";

            window.run_code(cell, code);
            break;
        case 1:
            var inputs = new Array();
            inputs.push(fid)

            var parms = new Array();
            var ids = ["customImportCode"];
            var code = document.getElementById("customImportCode").value;
            if (code.indexOf("# custom import") != -1) {
                code = code.replace("# custom import\n", "");
            }

            parms.push(ids);
            parms.push([code]);
            inputs.push(JSON.stringify(parms));

            window.delete_output_cell(window.IMPORT_CUSTOM_CODE_ID);
            window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"process_import_form","7," + JSON.stringify(inputs)));
            break;
        case 2:
            var inputs = new Array();
            inputs.push(fid);

            var parms = new Array();
            var ids = ["customImportCode"];
            var custom_cell = window.get_cell_for_id(IMPORT_CUSTOM_CODE_ID);
            var custom_code = custom_cell.get_text();
            if (custom_code.indexOf("# custom import") != -1) {
                custom_code = custom_code.replace("# custom import\n", "");
            }

            parms.push(ids);
            parms.push([custom_code]);
            inputs.push(JSON.stringify(parms));

            window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"process_import_form","7," + JSON.stringify(inputs)));
            break;
        case 3:
            var inputs = new Array();
            inputs.push(fid);

            window.delete_output_cell(window.IMPORT_CUSTOM_CODE_ID);
            window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"process_import_form","7," + JSON.stringify(inputs)));
            break;
        case 4:

            window.delete_output_cell(window.IMPORT_CUSTOM_CODE_ID);
            window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"display_import_forms",0));
            break;
    }
    window.scroll_to('DCDataImport');
}

function pandas_details_test_con_callback(sqlid, dbid, driverid) {
    /**
    * test db connection callbacks.
    *
    * Parameters:
    *  sqlid    - table or query
    *  dbid     - database id
    *  driverid - database driver id
    */
    var sqlinputparms = null;
    var sqlform = 0

    switch (dbid) {
        case 0: sqlinputparms = window.get_input_form_parms("MySQLdbconnector");        break;
        case 1: sqlinputparms = window.get_input_form_parms("MSSQLServerdbconnector");  break;
        case 2: sqlinputparms = window.get_input_form_parms("SQLitedbconnector");       break;
        case 3: sqlinputparms = window.get_input_form_parms("Postgresqldbconnector");   break;
        case 4: sqlinputparms = window.get_input_form_parms("Oracledbconnector");       break;
        case 5: sqlinputparms = window.get_input_form_parms("customdbconnector");       break;
    }
    
    if (sqlid == 0) {
        sqlform = 5;
    } else {
        sqlform = 6;
    }

    if (sqlinputparms != null) {
        window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"test_import_sql_db_connector",sqlform + ", " + driverid + ", " + sqlinputparms));
    }
}

function pandas_details_get_tables_callback() {
    /**
    * get db tables callback.
    */
    var sqlinputparms = [];
    sqlinputparms = window.get_input_form_parms("importPandasSQLCommonTable");
    window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"get_tables",sqlinputparms));
    window.scroll_to('DCDataImport');
}

function pandas_details_get_columns_callback() {
    /**
    * get db columns callback.
    */
    var sqlinputparms = [];
    sqlinputparms = window.get_input_form_parms("importPandasSQLCommonTable");
    window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"get_columns",sqlinputparms));
}

function pandas_details_get_strftime_callback() {
    /**
    * get format time list callback.
    */
    var sqlinputparms = [];
    sqlinputparms = window.get_input_form_parms("importPandasSQLCommonTable");
    window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"get_datetimeformats",sqlinputparms));
    window.scroll_to('DCDataImport');
}

function select_db(dblibid) {
    /**
    * test db connection callbacks.
    *
    * Parameters:
    *  dblibid - database library is
    */
    window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"display_sql_details_forms","5," + JSON.stringify(dblibid)));
    window.scroll_to('DCDataImport');
}

function select_custom() {
    /**
    * select custom callback.
    */
    window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"display_sql_details_forms","5," + JSON.stringify("custom")));
    window.scroll_to('DCDataImport');
}

function select_table(tablename) {
    /**
    * select table DHTML callback.
    *
    * Parameters:
    *  tablename - table name
    */
    var table_name = $("#sqltablecommontableName");
    table_name.val(tablename);
}

function select_column(columnname) {
    /**
    * select column callback.
    *
    * Parameters:
    *  columnname - column name
    */
    var column = $("#sqltablecommoncolumns");
    if (column.val() == "") {
        console.log("empty")
        column.val("[" + columnname + "]");
    } else {
        var slen = column.val().length;
        var newstring = column.val().substr(0, slen - 1) + ", " + columnname + "]";
        column.val(newstring);
    }
}

function pandas_import_sql_callback(fid) {
    /**
    * select column callback.
    *
    * Parameters:
    *  fid - function id
    */
    switch (fid) {
        case 0:
            var inputParms = window.get_input_form_parms("importPandasSQLCommonTable");
            window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"import_sql_table",inputParms));
            break;
        case 5:
            var inputParms = window.get_input_form_parms("importPandasSQLCustomTable");
            window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"import_sql_table",inputParms));
            break;
        default:
            var inputParms = window.get_input_form_parms("importPandasSQLQuery");
            window.run_code_in_cell(window.IMPORT_TASK_BAR_ID,window.getJSPCode(window.IMPORT_LIB,"import_sql_query",inputParms));
            break;
    }
    window.reset_dependents([false, true, true, true, true, false]);
    window.scroll_to('DCDataImport');
}

