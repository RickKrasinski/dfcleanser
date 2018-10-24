define([
    'base/js/namespace',
    'jquery',
    'base/js/utils',
    'base/js/dialog',
    './js_utils',
    './data_cleansing',
    './data_export',
    './data_import',
    './data_inspection',
    './data_scripting',
    './data_transform',
    './sw_utilities',
    './system'
], function(Jupyter, $, utils, dialog) {

    function toggle_dfcleanser() {
        window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSCode(window.SYSTEM_LIB, "toggle_dfcleanser"));
    }

    function load_button() {
        if (!Jupyter.toolbar) {
            $([Jupyter.events]).on("app_initialized.NotebookApp", place_button);
            return;
        }
        Jupyter.toolbar.add_buttons_group([{
            label: 'dfcleanser',
            icon: 'fa-database',
            callback: toggle_dfcleanser
        }])
    }

    function load_ipython_extension() {
        load_button();
    }

    return {
        load_ipython_extension: load_ipython_extension
    };

});