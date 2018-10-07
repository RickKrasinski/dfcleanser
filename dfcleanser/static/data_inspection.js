
//
// 
// ------------------------------------------------------
// Data Inspection Chapter javascript functions
// ------------------------------------------------------
//
//  

function inspection_task_bar_callback(fid) {
    /**
    * Data inspection taskbar callback.
    *
    * Parameters:
    *  fid - function id
    */
    switch (fid) {
        case 0:
            var inspectionParms = window.getcheckboxValues('inspection_cb');
            window.clear_cell_output(window.INSPECTION_TASK_BAR_ID);
            window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID,window.getJSPCode(window.INSPECTION_LIB,"display_data_inspection","1" + ", " + inspectionParms));
            break;
        case 1: window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID,window.getJSPCode(window.INSPECTION_LIB,"display_data_inspection","0")); break;
    }
}

function srow(rowid) {
    /**
    * Data Inspection select a row to display.
    *
    * Parameters:
    *  rowid - row id
    */
    var goodrowid = true;
    try {
        if (rowid.length > 0) {
            goodrowid = false;
            var nrow = parseInt(rowid);
            if (nrow === parseInt(nrow, 10))
                goodrowid = true;
        }
    } catch (e) {}
    if (goodrowid) {
        window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID,window.getJSPCode(window.CLEANSING_LIB,"display_data_cleansing","3" + "," + JSON.stringify(rowid)));
        window.scroll_to('DCDataCleansing');
    }
}

function display_objects_callback(id) {
    /* Data Inspection deprecated.
     * @param:
     *  rowid - row id
     */
    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID,window.getJSPCode(window.CLEANSING_LIB,"display_data_cleansing","16," + id));
    window.scroll_to('DCDataCleansing');
}

function ucol(colid) {
    /**
    * Data Inspection display unique columns values.
    *
    * Parameters:
    *  colid - column id
    */
    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID,window.getJSPCode(window.CLEANSING_LIB,"display_data_cleansing","1" + "," + JSON.stringify(colid)));
    window.scroll_to('DCDataCleansing');
}

function ncol(colid) {
    /**
    * Data Inspection display numeric columns.
    *
    * Parameters:
    *  colid - column id
    */
    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID,window.getJSPCode(window.CLEANSING_LIB,"display_data_cleansing","4" + "," + JSON.stringify(colid)));
    window.scroll_to('DCDataCleansing');
}

function scol(colid) {
    /**
    * Data Inspection display single column.
    *
    * Parameters:
    *  colid - column id
    */
    window.run_code_in_cell(window.CLEANSING_TASK_BAR_ID,window.getJSPCode(window.CLEANSING_LIB,"display_data_cleansing","4" + "," + JSON.stringify(colid)));
    window.scroll_to('DCDataCleansing');
}

function scatcol(colid) {
    /**
    * Data Inspection display cat columns.
    *
    * Parameters:
    *  colid - column id
    */
    var fparms = [colid, 27];
    var inputs = new Array();
    inputs.push(fparms);
    window.run_code_in_cell(window.TRANSFORM_TASK_BAR_ID,window.getJSPCode(window.TRANSFORM_LIB,"display_data_transform","11" + "," + JSON.stringify(inputs)));
    window.scroll_to('DCDataTransform');
}

function disrowInputIdcallback() {
    /**
    * Data Inspection display rows 
    */
    var element = document.getElementById("disrowInputId");
    window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID,window.getJSPCode(window.INSPECTION_LIB,"display_data_inspection","2" + "," + JSON.stringify(element.value)));
    window.scroll_to('DCDataInspection');
}

function dc_drop_rows_callback(valtype) {
    /**
    * Data Inspection drop nan rows.
    *
    * Parameters:
    *  valtype - threshold type
    */
    var parms = new Array();
    parms.push(valtype);
    var inputs = window.get_input_form_parms("droprowsinput");
    parms.push(inputs);
    window.clear_cell_output(window.INSPECTION_TASK_BAR_ID);
    window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID,window.getJSPCode(window.INSPECTION_LIB,"display_data_inspection","3" + ", " + JSON.stringify(parms)));
    window.scroll_to('DCDataInspection');
}

function dc_drop_cols_callback(valtype) {
    /**
    * Data Inspection drop nan cols.
    *
    * Parameters:
    *  valtype - threshold type
    */
    var parms = new Array();
    parms.push(valtype);
    var inputs = window.get_input_form_parms("dropcolsinput");
    parms.push(inputs);
    window.clear_cell_output(window.INSPECTION_TASK_BAR_ID);
    window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID,window.getJSPCode(window.INSPECTION_LIB,"display_data_inspection","4" + ", " + JSON.stringify(parms)));
    window.scroll_to('DCDataInspection');
}

