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
            window.run_code_in_cell(window.SYSTEM_TASK_BAR_ID, window.getJSPCode(window.SYSTEM_LIB, "display_system_environment", fid));
            break;
        case 2:
            window.initialize_dc();
            window.run_code_in_cell(window.SYSTEM_TASK_BAR_ID, window.getJSPCode(window.SYSTEM_LIB, "display_system_environment", fid));
            window.set_code(window.SYSTEM_TASK_BAR_ID, window.getJSPCode(window.SYSTEM_LIB, "display_system_environment", 0));
            break;
        case 3:
            window.run_code_in_cell(window.SYSTEM_TASK_BAR_ID, window.getJSPCode(window.SYSTEM_LIB, "display_system_environment", fid));
            break;
        case 15:
            var inputs = new Array();
            var cbparms = window.getcheckboxValues("dfc_core_cb");
            if (cbparms != null) { inputs.push(cbparms); }
            cbparms = window.getcheckboxValues("dfc_utils_cb");
            if (cbparms != null) { inputs.push(cbparms); }
            cbparms = window.getcheckboxValues("dfc_script_cb");
            if (cbparms != null) { inputs.push(cbparms); }
            window.run_code_in_cell(window.SYSTEM_TASK_BAR_ID, window.getJSPCode(window.SYSTEM_LIB, "display_system_environment", "15, " + JSON.stringify(inputs)));
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

function dfmgr_callback(fid) {
    /**
     * process dataframe manager callback.
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     dfmgr_callback : fid ", fid);

    var inputs = new Array();
    inputs.push(fid);

    if (fid == 19)
        var inputparms = window.get_input_form_parms("dfmgraddform");
    else
        var inputparms = window.get_input_form_parms("dfmgrform");

    if (inputparms != null) {
        inputs.push(inputparms);
    }

    switch (fid) {

        case 19:
            //window.delete_output_cell(window.SYSTEM_TASK_BAR_ID);
            window.run_code_in_cell(window.SYSTEM_TASK_BAR_ID, window.getJSPCode(window.SYSTEM_LIB, "display_system_environment", "19, " + JSON.stringify(inputs)));
            window.scroll_to('DCSystem');
            break;

        case 5:
            //window.delete_output_cell(window.SYSTEM_TASK_BAR_ID);
            window.run_code_in_cell(window.SYSTEM_TASK_BAR_ID, window.getJSPCode(window.SYSTEM_LIB, "display_system_environment", "0"));
            window.scroll_to('DCSystem');
            break;

        case 7:
            console.log(log_prefix + "\n" + "     dfmgr_callback : fid : case 7");
            //window.delete_output_cell(window.SYSTEM_TASK_BAR_ID);
            window.run_code_in_cell(window.SYSTEM_TASK_BAR_ID, window.getJSPCode(window.SYSTEM_LIB, "display_system_environment", "7"));
            window.scroll_to('DCSystem');
            break;

        default:
            //window.delete_output_cell(window.SYSTEM_TASK_BAR_ID);
            window.run_code_in_cell(window.SYSTEM_TASK_BAR_ID, window.getJSPCode(window.SYSTEM_LIB, "display_system_environment", "18, " + JSON.stringify(inputs)));
            window.scroll_to('DCSystem');
            break;

    }

}


function select_new_df(dftitle) {

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     select_new_df : ", dftitle);

    var title = $('#dftitle');
    if (title != null) {
        var titleparm = title.val();
        var formparm = "dftitle";
    } else {
        var titleparm = $('#dftitleadd').val();
        var formparm = "dftitleadd";
    }

    var inputs = new Array();
    inputs.push(formparm);
    inputs.push(titleparm);

    window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "select_df", JSON.stringify(inputs)));
}


function add_new_dfc_df(dftitle, dfname, dfnotes) {

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     add_new_dfc_df : ", dftitle, dfname, dfnotes);

    var df_addcode = "from dfcleanser.common.cfg import dfc_dataframe, add_dfc_dataframe" + window.NEW_LINE;
    df_addcode = (df_addcode + "new_dfc_df = dfc_dataframe('" + dftitle + "', " + dfname + ", '" + dfnotes + "')" + window.NEW_LINE)
    df_addcode = (df_addcode + "add_dfc_dataframe(new_dfc_df)")
    window.run_code_in_cell(window.WORKING_CELL_ID, df_addcode);
}