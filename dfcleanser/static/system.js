
//
// 
// ------------------------------------------------------
// System Environment Chapter javascript functions
// ------------------------------------------------------
//
// 

function process_system_tb_callback(fid) {
    /**
    * main system taskbar callback.
    *
    * Parameters:
    *  fid
    *      System Environment function id
    */
    switch (fid) {
        case 0:
        case 1:
        case 4:
        case 5:
        case 6:
        case 12:
        case 13:
        case 14:
        case 16:
        case 17:
            window.run_code_in_cell(window.SYSTEM_TASK_BAR_ID,window.getJSPCode(window.SYSTEM_LIB,"display_system_environment",fid));
            break;
        case 2:
            window.initialize_dc();
            window.run_code_in_cell(window.SYSTEM_TASK_BAR_ID,window.getJSPCode(window.SYSTEM_LIB,"display_system_environment",fid));
            window.set_code(window.SYSTEM_TASK_BAR_ID,window.getJSPCode(window.SYSTEM_LIB,"display_system_environment",0));
            break;
        case 3:
            window.run_code_in_cell(window.SYSTEM_TASK_BAR_ID,window.getJSPCode(window.SYSTEM_LIB,"display_system_environment",fid));
            break;
        case 15:
            var inputs = new Array();
            var cbparms = window.getcheckboxValues("dfc_core_cb");
            if (cbparms != null) {inputs.push(cbparms);}
            cbparms = window.getcheckboxValues("dfc_utils_cb");
            if (cbparms != null) {inputs.push(cbparms);}
            cbparms = window.getcheckboxValues("dfc_script_cb");
            if (cbparms != null) {inputs.push(cbparms);}
            window.run_code_in_cell(window.SYSTEM_TASK_BAR_ID,window.getJSPCode(window.SYSTEM_LIB,"display_system_environment","15, " + JSON.stringify(inputs)));
            break;
    }
    window.scroll_to('DCSystem');
}

function process_notebook_files_callback(fid) {
    /**
     * process dfc files callback.
     */
    var inputs = new Array();
    inputs.push(fid);
    var inputparms = window.get_input_form_parms("dfcfiles");
    if (inputparms != null) {
        inputs.push(inputparms);
    }
    window.run_code_in_cell(window.SYSTEM_TASK_BAR_ID, window.getJSPCode(window.SYSTEM_LIB, "display_system_environment", "10, " + JSON.stringify(inputs)));
}

//----------------------------------------------------------------
// dynamic html functions
//----------------------------------------------------------------
function select_dfc_nb(dfcnbname){
    var currentcolname = $("#nbname");
    currentcolname.val(dfcnbname);

}

function dfmgr_callback(fid) {
    /**
     * process dataframe manager callback.
     */
    var inputs = new Array();
    inputs.push(fid);
    var inputparms = window.get_input_form_parms("dfmgrform");
    if (inputparms != null) {
        inputs.push(inputparms);
    }
    window.run_code_in_cell(window.SYSTEM_TASK_BAR_ID, window.getJSPCode(window.SYSTEM_LIB, "display_system_environment", "18, " + JSON.stringify(inputs)));
}

//----------------------------------------------------------------
// dynamic html functions
//----------------------------------------------------------------
function select_datframe(dfcdftitle){
    var inputs = new Array();
    inputs.push(dfcdftitle);
    window.run_code_in_cell(window.SYSTEM_TASK_BAR_ID, window.getJSPCode(window.SYSTEM_LIB, "display_system_environment", "3, " + JSON.stringify(inputs)));
}
