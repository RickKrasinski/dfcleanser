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

    var log_prefix = '[' + "dfcleanser" + ']';

    function load_buttons() {
        if (!Jupyter.toolbar) {
            $([Jupyter.notebook.events]).on("app_initialized.NotebookApp", place_button);
            return;
        }
        Jupyter.toolbar.add_buttons_group([{
            label: 'toggle',
            icon: 'fa-database',
            callback: toggle_dfcleanser
        }])
        
        Jupyter.toolbar.add_buttons_group([{
            label: 'reset',
            icon: 'fa-window-restore',
            callback: reset_dfcleanser
        }])
        
        Jupyter.notebook.events.on('notebook_renamed.Notebook',callback_notebook_renamed);
        Jupyter.notebook.events.on('app_initialized.NotebookApp',callback_app_initialized);
        Jupyter.notebook.events.on('notebook_loaded.Notebook',callback_notebook_loaded);
        
        // setup things to run on loading config/notebook
        //Jupyter.notebook.config.loaded
            //.then(function update_options_from_config () {
            //    $.extend(true, options, Jupyter.notebook.config.data[mod_name]);
            //}, function (reason) {
            //    console.warn(log_prefix, 'error loading config:', reason);
            //})
            //.then(function () {
            //    if (Jupyter.notebook._fully_loaded) {
            //        callback_notebook_loaded();
            //    }
            //    events.on('notebook_loaded.Notebook', callback_notebook_loaded);
            //}).catch(function (reason) {
            //    console.error(log_prefix, 'unhandled error:', reason);
            //});        

    }
    
    //var options = { // updated from server's config & nb metadata
    //    run_on_kernel_ready: true,
    //};
    
    function toggle_dfcleanser() {
        
        if(window.is_dfcleanser_loaded()){
            window.unload_dfcleanser();
        }
        else{
            window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSCode(window.SYSTEM_LIB, "load_dfCleanser"));
        }
        console.log(log_prefix + "toggle_dfcleanser");
    }

    function reset_dfcleanser() {
        window.initialize_dc();
        console.log(log_prefix + "reset_dfcleanser");
    }

    function callback_notebook_renamed(){
        console.log(log_prefix + "callback_notebook_renamed");
            
        // rename the config files
        window.run_code_in_cell(window.SYSTEM_TASK_BAR_ID,window.getJSPCode(window.SYSTEM_LIB,"display_system_environment","12"));
    }
       
    function callback_notebook_loaded() {
        console.log(log_prefix + "callback_notebook_loaded");
    }
    
    function callback_app_initialized() {
        
        console.log(log_prefix + "callback_app_initialized");    
        if(window.is_dfcleanser_loaded()){
        
            // reset the system chapter
            window.run_code_in_cell(window.SYSTEM_TASK_BAR_ID,window.getJSPCode(window.SYSTEM_LIB,"display_system_environment","0"));

            // reset working chapter
            var workingcell = get_cell_for_id(WORKING_CELL_ID);
            if(workingcell != null)
                workingcell.set_text(WORKING_CELL + "- please do not remove");
                window.delete_output_cell(window.WORKING_CELL_ID);
         }
        
        // set the notebook name and path
        window.getNotebookLocation();
                
        // set chapters loaded
        window.getdfCChaptersLoaded();
    
    }

    function load_ipython_extension() {
        load_buttons();
    }

    return {
        load_ipython_extension: load_ipython_extension
    };

});