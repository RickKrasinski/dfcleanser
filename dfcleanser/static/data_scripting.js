//
// 
// ------------------------------------------------------
// Data Scripting javascript functions
// ------------------------------------------------------
//
//

function scripting_tb_callback(fid) {
    /**
     * scripting main taskbar callback.
     *
     * Parameters:
     *  fid - function id
     */
    var inputs = new Array();
    inputs.push(String(fid));

    switch (fid) {
        case 0:
        case 1:
        case 2:
        case 9:
        case 10:
            window.run_code_in_cell(window.SCRIPT_TASK_BAR_ID, window.getJSPCode(window.SCRIPT_LIB, "display_data_scripting", "0" + "," + JSON.stringify(inputs)));
            window.scroll_to('DCDataScripting');
            break;
        case 3:
            window.clear_cell_output(window.SCRIPT_TASK_BAR_ID);
            window.run_code_in_cell(window.SCRIPT_TASK_BAR_ID, window.getJSPCode(window.SCRIPT_LIB, "display_data_scripting", "0"));
            window.scroll_to('DCDataScripting');
            break;
    }
}

function process_script_callback(fid) {
    /**
     * scripting process callback.
     *
     * Parameters:
     *  fid - function id
     */
    switch (fid) {
        case 2:
            var inputs = new Array();
            inputs.push(String(fid));
            var importVals = window.get_input_form_parms("dcscripting");
            inputs.push(importVals);
            window.run_code_in_cell(window.SCRIPT_TASK_BAR_ID, window.getJSPCode(window.SCRIPT_LIB, "display_data_scripting", "0" + "," + JSON.stringify(inputs)));
            break;
        case 3:
            var inputs = new Array();
            inputs.push(String(3));
            window.run_code_in_cell(window.SCRIPT_TASK_BAR_ID, window.getJSPCode(window.SCRIPT_LIB, "display_data_scripting", "0" + "," + JSON.stringify(inputs)));
            window.scroll_to('DCDataScripting');
            break;
        case 4:
            var inputs = new Array();
            inputs.push(String(fid));
            var importVals = window.get_input_form_parms("dcscripting");
            inputs.push(importVals);
            window.run_code_in_cell(window.SCRIPT_TASK_BAR_ID, window.getJSPCode(window.SCRIPT_LIB, "display_data_scripting", "0" + "," + JSON.stringify(inputs)));
            window.scroll_to('DCDataScripting');
            break;
        case 5:
            window.clear_cell_output(window.SCRIPT_TASK_BAR_ID);
            window.run_code_in_cell(window.SCRIPT_TASK_BAR_ID, window.getJSPCode(window.SCRIPT_LIB, "display_data_scripting", "0"));
            window.scroll_to('DCDataScripting');
            break;
    }
}

function process_script_add_code_callback(fid) {
    /**
     * scripting process add_code callback.
     *
     * Parameters:
     *  fid - function id
     */
    switch (fid) {
        case 7:
            var inputs = new Array();
            inputs.push(String(fid));
            var importVals = window.get_input_form_parms("dcacscripting");
            inputs.push(importVals);
            window.run_code_in_cell(window.SCRIPT_TASK_BAR_ID, window.getJSPCode(window.SCRIPT_LIB, "display_data_scripting", "0" + "," + JSON.stringify(inputs)));
            window.scroll_to('DCDataScripting');
            break;
        case 8:
            window.clear_cell_output(window.SCRIPT_TASK_BAR_ID);
            window.run_code_in_cell(window.SCRIPT_TASK_BAR_ID, window.getJSPCode(window.SCRIPT_LIB, "display_data_scripting", "0"));
            window.scroll_to('DCDataScripting');
            break;

    }
}