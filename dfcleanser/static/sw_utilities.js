//
// 
// ------------------------------------------------------
// Software Utilities Chapter javascript functions
// ------------------------------------------------------
//
//

// 
// ------------------------------------------------------
// Data Structures Utility functions 
// ------------------------------------------------------
//

function build_utility_callback(id) {
    /**
     * data structures utility taskbar.
     *
     * Parameters:
     *  id - function id - list or dict
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     build_utility_callback", id);


    switch (id) {

        case 1:
        case 2:
        case 11:
        case 12:
        case 15:

            window.clear_cell_output(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID);
            window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_LIB, "process_sw_utilities", id));
            break;

        case 3: // add list
        case 4: // delete list
        case 7: // clear list
        case 13: // update list
        case 19: // load list

            var fparms = get_input_form_parms("maintlistparms");
            window.clear_cell_output(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID);
            window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_LIB, "process_sw_utilities", (id + ", " + fparms)));
            break;

        case 5: // add dict
        case 6: // delete dict
        case 8: // clear dict
        case 16: // update dict
        case 18: // load dict

            var fparms = get_input_form_parms("maintdictparms");
            window.clear_cell_output(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID);
            window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_LIB, "process_sw_utilities", (id + ", " + fparms)));
            break;
    }
    window.scroll_to('DCListUtility');
}



function build_utility_clear_callback() {
    /**
     * data structures utility clear inputs.
     */

    window.clear_cell_output(SW_UTILS_DATASTRUCT_TASK_BAR_ID);
    window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_LIB, "process_sw_utilities", "0"));
    window.scroll_to('DCListUtility');
}

function sw_utilities_delete_callback(id) {
    /**
     * data structures utility delete item.
     *
     * Parameters:
     *  id - function id - list or dict
     */

    var iname = ""
    if (id == 4) { iname = $("#listname").val() } else { iname = $("#dictname").val() }
    window.clear_cell_output(SW_UTILS_DATASTRUCT_TASK_BAR_ID);
    window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_LIB, "process_sw_utilities", id + ", " + JSON.stringify(iname)));
}

function sw_utilities_list_add_callback() {
    /**
     * data structures utility add list.
     */

    var importVals = get_input_form_parms("buildlistparms");
    window.clear_cell_output(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID);
    window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_LIB, "process_sw_utilities", (3 + ", " + importVals)));
    window.scroll_to('DCListUtility');
}

function sw_utilities_dict_add_callback() {
    /**
     * data structures utility add dict.
     */

    var importVals = get_input_form_parms("builddictparms");
    window.clear_cell_output(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID);
    window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_LIB, "process_sw_utilities", (5 + ", " + importVals)));
    window.scroll_to('DCListUtility');
}

function select_dict(formid) {
    /**
     * data structures utility select dict.
     *
     * Parameters:
     *  formid - dict form
     */

    var inputs = new Array();
    var dictname = $("#" + formid + " :selected").text();
    inputs.push(dictname);

    window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_LIB, "process_sw_utilities", "10, " + JSON.stringify(inputs)));
    window.scroll_to('DCListUtility');
}

function select_list(formid) {
    /**
     * data structures utility select list.
     *
     * Parameters:
     *  formid - list form
     */

    var inputs = new Array();
    var listname = $("#" + formid + " :selected").text();
    inputs.push(listname);

    window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_LIB, "process_sw_utilities", "9, " + JSON.stringify(inputs)));
    window.scroll_to('DCListUtility');
}


// 
// ------------------------------------------------------
// Geocoding Utility functions 
// ------------------------------------------------------
//

function process_geoutils_callback(fid) {
    /**
     * geocodong main taskbar callback.
     *
     * Parameters:
     *  fid - function id
     */

    var inputId = "";

    switch (fid) {
        case 40:
        case 41:
        case 43:
        case 45:
        case 47:
        case 49:
            window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", fid));
            window.scroll_to('DCGeocodeUtility');
            break;
        case 42:
            inputId = "addrdist";
            break;
        case 44:
            inputId = "addrdfdist";
            break;
        case 46:
            inputId = "addrcenter";
            break;
        case 48:
            inputId = "addrdfcenter";
            break;
        case 50:
            inputId = "bulktune";
            break;
        case 52:
            inputId = "addrdfcenterdist";
            break;
        case 53:
            inputId = "addrdfcenterdist";
            break;
        case 54:
            inputId = "addrdist";
            break;
        case 55:
            inputId = "addrdist";
            break;

    }

    if (inputId != "") {
        var inputs = window.get_input_form_parms(inputId);
        window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", fid + "," + JSON.stringify(inputs)));
        window.scroll_to('DCGeocodeUtility');
    }
}

//
// Geocoding dhtml functions 
//
function acselcol(colid) {
    var inputId = $("#dfaddress");
    var addrtext = "";
    if (inputId.val().length > 0) { addrtext = inputId.val() + " + " + colid; } else { addrtext = colid; }
    inputId.val(addrtext)
}

function accolsmove(action, formid) {
    var found_flag = false;
    if (action == 'skip') {
        $('#addrconvertparmsid  :input').each(function() {
            if (!found_flag) {
                if ($(this).prop('readonly') == false) {
                    $(this).prop('readonly', true);
                    found_flag = true;
                }
            }
        });
    } else {
        $('#addrconvertparmsid  :input').each(function() {
            $(this).prop('readonly', false);
            $(this).val('');
        });
    }
}

function add_df_column(colname) {
    var currentAddress = $("#dfaddress");
    var newAddress = "";
    if (currentAddress.val().length > 0) { newAddress = currentAddress.val() + " + " + colname; } else { newAddress = colname; }
    currentAddress.val(newAddress);
}


function select_geocoder(gcid) {
    /**
     * select geocoder display.
     *
     * Parameters:
     *  gcid - geocoder id
     */

    var id = -1;
    switch (gcid) {

        case ("ArcGIS"):
            id = 0;
            break;
        case ("Baidu"):
            id = 1;
            break;
        case ("Bing"):
            id = 2;
            break;
        case ("GoogleV3"):
            id = 7;
            break;
        case ("OpenMapQuest"):
            id = 9;
            break;
        case ("Nominatim"):
            id = 11;
            break;
    }

    var inputs = [id, 0, []];
    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", "3, " + JSON.stringify(inputs)));
    window.scroll_to('DCGeocodeUtility');
}

function select_bulk_geocoder(gcid) {
    /**
     * select geocoder display.
     *
     * Parameters:
     *  gcid - geocoder id
     */

    var id = -1;
    switch (gcid) {

        case ("ArcGIS"):
            id = 0;
            break;
        case ("Baidu"):
            id = 1;
            break;
        case ("Bing"):
            id = 2;
            break;
        case ("GoogleV3"):
            id = 7;
            break;
        case ("OpenMapQuest"):
            id = 9;
            break;
        case ("Nominatim"):
            id = 11;
            break;
    }

    var inputs = [id, 1, []];
    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", "3, " + JSON.stringify(inputs)));
    window.scroll_to('DCGeocodeUtility');
}

function get_geocode_form_id(gcid, gtype, gmode) {

    var id = ""

    if (gmode == 0) {
        switch (gtype) {

            case (0):

                switch (gcid) {
                    case 0:
                        id = "arcgisgeocoder";
                        break;
                    case 1:
                        id = "baidugeocoder";
                        break;
                    case 2:
                        id = "binggeocoder";
                        break;
                    case 7:
                        id = "googlegeocoder";
                        break;
                    case 9:
                        id = "mapquestgeocoder";
                        break;
                    case 11:
                        id = "nomingeocoder";
                        break;
                }
                break;

            case (1):

                switch (gcid) {
                    case 0:
                        id = "arcgisquery";
                        break;
                    case 1:
                        id = "baiduquery";
                        break;
                    case 2:
                        id = "bingquery";
                        break;
                    case 7:
                        id = "googlequery";
                        break;
                    case 9:
                        id = "mapquestquery";
                        break;
                    case 11:
                        id = "nominquery";
                        break;
                }
                break;

            case (2):

                switch (gcid) {
                    case 0:
                        id = "arcgisreverse";
                        break;
                    case 1:
                        id = "baidureverse";
                        break;
                    case 2:
                        id = "bingreverse";
                        break;
                    case 7:
                        id = "googlereverse";
                        break;
                    case 9:
                        id = "mapquestreverse";
                        break;
                    case 11:
                        id = "nominreverse";
                        break;
                }
                break;
        }
    } else {

        switch (gtype) {

            case (0):

                switch (gcid) {
                    case 0:
                        id = "arcgisbatchgeocoder";
                        break;
                    case 1:
                        id = "baidubulkgeocoder";
                        break;
                    case 2:
                        id = "bingbulkgeocoder";
                        break;
                    case 7:
                        id = "googlebulkgeocoder";
                        break;
                    case 9:
                        id = "mapquestbulkgeocoder";
                        break;
                    case 11:
                        id = "nominbulkgeocoder";
                        break;
                }
                break;

            case (1):

                switch (gcid) {
                    case 0:
                        id = "arcgisbatchquery";
                        break;
                    case 1:
                        id = "baidubulkquery";
                        break;
                    case 2:
                        id = "bingbulkquery";
                        break;
                    case 7:
                        id = "googlebulkquery";
                        break;
                }
                break;

            case (2):

                switch (gcid) {
                    case 1:
                        id = "baidubulkreverse";
                        break;
                    case 2:
                        id = "bingbulkreverse";
                        break;
                    case 7:
                        id = "googlebulkreverse";
                        break;
                }
                break;
        }
    }

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     get_geocode_form_id", gcid, gtype, gmode, id);

    return (id);
}

function process_geocoding_callback(gcid, gtype, gmode) {
    /**
     * geocoder inputs processing.
     *
     * Parameters:
     *  gcid  - geocoder id
     *  gtype - geocoding type
     *  gmode - geocoding mode
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     process_geocoding_callback", gcid, gtype, gmode);

    var fparms = get_input_form_parms(get_geocode_form_id(gcid, gtype, gmode));
    var inputs = [gcid, gtype, gmode, fparms];

    window.scroll_to('DCGeocodeUtility');
    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", "7" + ", " + JSON.stringify(inputs)));
    window.scroll_to('DCGeocodeUtility');
}

function display_geocoding_callback(gcid, gtype, gmode) {
    /**
     * geocoder inputs processing.
     *
     * Parameters:
     *  gcid  - geocoder id
     *  gtype - geocoding type
     *  gmode - geocoding mode
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     display_geocoding_callback", gcid, gtype, gmode);


    var fparms = get_input_form_parms(get_geocode_form_id(gcid, 0, gmode));
    var inputs = [gcid, gtype, gmode, fparms];

    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", "5" + ", " + JSON.stringify(inputs)));
    window.scroll_to('DCGeocodeUtility');
}

function test_geocoder(gid, gmode) {
    /**
     * test geocoder.
     *
     * Parameters:
     *  gid   - geocoder id
     *  gmode - geocode mode
     */

    var fparms = get_input_form_parms(get_geocode_form_id(gid, 0, gmode));
    var inputs = [gid, gmode, fparms];

    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", "4" + ", " + JSON.stringify(inputs)));
    window.scroll_to('DCGeocodeUtility');
}

function display_geocoders(gid, gmode) {
    /**
     * display geocoders.
     *
     * Parameters:
     *  gid   - geocoder id
     *  gmode - geocode mode
     */

    var inputs = [gid, gmode];
    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", "3" + ", " + JSON.stringify(inputs)));
    window.scroll_to('DCGeocodeUtility');
}

function clear_geocode_form(gid, gtype, gmode) {
    /**
     * clear a geocoder form.
     *
     * Parameters:
     *  gid   - geocoder id
     *  gtype - geocode type
     *  gmode - geocode mode
     */

    var inputs = [gid, gtype, gmode];
    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", "2" + ", " + JSON.stringify(inputs)));
    window.scroll_to('DCGeocodeUtility');
}

function geocode_return() {
    /**
     * clear a geocoder form.
     *
     */

    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", "0"));
    window.scroll_to('DCGeocodeUtility');
}

function get_geocoding_table(tableid, gcid, gtype, gmode) {
    /**
     * geocoder inputs processing.
     *
     * Parameters:
     *  tableid - table id id
     *  gcid    - geocoder id
     *  gtype   - geocoding type
     *  gmode   - geocoding mode
     */

    var fparms = get_input_form_parms(get_geocode_form_id(gcid, gtype, gmode));
    var inputs = [tableid, gcid, gtype, gmode, fparms];

    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", "6" + ", " + JSON.stringify(inputs)));
    window.scroll_to('DCGeocodeUtility');
}

function process_batch_geocoder(fid, geotype) {
    /**
     * geocoder bulk query processing.
     *
     * Parameters:
     *  fid- function id
     *  gcid - geocoder id
     */

    var fparms = get_input_form_parms("arcgisbatchgeocoder");

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     process_batch_geocoder", fid, fparms);

    var inputs = [fid, geotype, fparms];

    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", ("20, " + JSON.stringify(inputs))));
    window.scroll_to('DCGeocodeUtility');
}

function display_bulk_geocoding_results(fid) {
    /**
     * geocoder bulk reverse processing.
     *
     * Parameters:
     *  fid- function id
     */

    var inputs = [fid];

    if (fid == 3) {
        window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", ("30, " + JSON.stringify(inputs))));
        window.run_code_in_cell(window.EXPORT_TASK_BAR_ID, window.getJSPCode(window.EXPORT_LIB, "display_export_forms", "2,4"));
        window.scroll_to('DCDataExport');
    } else {
        window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", ("30, " + JSON.stringify(inputs))));
        window.scroll_to('DCGeocodeUtility');
    }
}

function process_bulk_geocoding_results(fid) {
    /**
     * geocoder bulk geocoding processing.
     *
     * Parameters:
     *  fid- function id
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     process_bulk_geocoding_results", fid);

    var formid = "";
    switch (fid) {
        case 5:
        case 6:
        case 8:
            formid = "geocodebulkproc";
            break;
        case 7:
            formid = "bulkcsvappend";
            break;
        case 10:
        case 11:
        case 12:
        case 13:
            formid = "reversebulkproc";
            break;
        case 15:
        case 16:
        case 17:
        case 18:
            formid = "bulkcsvexport";
            break;
        case 24:
            window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "open_as_excel", "1"));
            return;
            break;
        case 25:
            window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "open_as_excel", "2"));
            return;
            break;
        case 26:
        case 27:
        case 28:
            formid = "bulkerrorscsvexport";
            break;
        case 30:
            window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "open_as_excel", "3"));
            return;
            break;

    }

    if (formid != "") {
        var fparms = get_input_form_parms(formid);
    } else {
        fparms = [];
    }
    var inputs = [fid, fparms];

    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", ("30, " + JSON.stringify(inputs))));
    window.scroll_to('DCGeocodeUtility');
}

function controlbulkrun(fid) {
    /**
     * geocoder bulk run control.
     *
     * Parameters:
     *  fid- function id
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     controlbulkrun", fid);

    if (fid == 26) {
        window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "process_bulk_geocoding_run_cmd", fid));
        window.reset_dependents([false, true, false, false, false, false]);
        window.scroll_to('DCGeocodeUtility');
    } else {
        window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "process_bulk_geocoding_run_cmd", fid));
        window.reset_dependents([false, true, false, false, false, false]);
        window.scroll_to('DCGeocodeUtility');
    }
}

function set_bulk_progress_bar(barid, barvalue) {
    /**
     * set progress value
     *
     * Parameters:
     *  barid    - progress bar id
     *  barvalue - progress bar value
     */

    var progressbar = $("#" + barid);
    progressbar.text(barvalue.toString() + "%");
    progressbar.attr('aria-valuenow', barvalue).css('width', barvalue + "%");

}

function view_geocode_errors() {
    /**
     * view_geocode_errors
     *
     * Parameters:
     */

    var ids = new Array("didfdataframe");
    var inputs = new Array("Current_Geocoding_Error_Log_df");

    var parms = new Array();
    parms.push(ids);
    parms.push(inputs);
    fparms = JSON.stringify(parms);

    var inputcbs = new Array("False", "False", "True", "False", "False");
    cbs = JSON.stringify(inputcbs);

    var inputs = [fparms, cbs];
    window.clear_cell_output(window.INSPECTION_TASK_BAR_ID);
    window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID, window.getJSPCode(window.INSPECTION_LIB, "display_data_inspection", "1" + ", " + JSON.stringify(inputs)));
    window.scroll_to('DCDataInspection');
}

function report_geocode_run_error(cmd, msg) {
    /**
     * report a geocode run error
     *
     * Parameters:
     *  geocid  - geocoder id
     *  cmd     - run cmd
     *  msg     - error message
     */


    var parms = new Array();
    parms.push(cmd);
    parms.push(msg);

    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "process_bulk_geocoding_run_cmd", "31, " + JSON.stringify(parms)));
    window.scroll_to('DCGeocodeUtility');
}

function change_bulk_df(selectid) {
    /**
     * view_geocode_errors
     *
     * Parameters:
     */

    var dfname = $("#" + selectid).val();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     change_bulk_df", dfname);

    var parms = new Array();
    parms.push(dfname);

    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", "32, " + JSON.stringify(parms)));
    window.scroll_to('DCGeocodeUtility');
}

function change_bulk_reverse_df(selectid) {
    /**
     * view_geocode_errors
     *
     * Parameters:
     */

    var dfname = $("#" + selectid).val();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     change_bulk_reverse_df", dfname);

    var parms = new Array();
    parms.push(dfname);

    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", "33, " + JSON.stringify(parms)));
    window.scroll_to('DCGeocodeUtility');
}


// ------------------------------------------------------
// Geocoding dynamic html functions 
// ------------------------------------------------------
function bg_add_df_column(colid, addparms) {

    var coladdr = null;
    var colval = null;
    var parms = addparms.split(",");
    var geocid = parseInt(parms[0]);
    var geotype = parseInt(parms[1]);

    switch (geocid) {
        case 0:
            if (geotype == 1) {
                coladdr = $("#bagaddrcomps");
            }
            break;
        case 2:
            if (geotype == 1) {
                coladdr = $("#bbqaddress");
            } else {
                coladdr = $("#bbrcolumnname");
            }
            break;
        case 7:
            if (geotype == 1) {
                coladdr = $("#bgqaddress");
            } else {
                coladdr = $("#bgrcolumnname");
            }
            break;
    }

    if (coladdr.val() != null) {
        var colval = coladdr.val();
        var newcolval = ""
        if (geotype == 1) {
            if (colval.length > 0) { newcolval = colval + " + " + colid; } else { newcolval = colid; }
        } else {
            if (colval.length > 0) {
                var endlist = colval.indexOf("]");
                var collist = colval.slice(0, endlist);
                newcolval = collist + ", " + colid + "]";
            } else { newcolval = "[" + colid + "]"; }
        }

        coladdr.val(newcolval);
    }
}

function gb_select_language(lang) {
    var language = $("#bgqlanguage");
    language.val(lang);
}

function gb_select_region(region) {
    var reg = $("#bgqregion");
    reg.val(region);
}

function gb_select_country(region) {
    var reg = $("#baqsourcecountry");
    reg.val(region);
}

function gb_select_category(category) {
    var cat = $("#baqcategory");
    cat.val(category);
}

function gbr_google_add_addrcomp(addrcomp) {

    var acomps = $("#bgraddresscomponents");
    var colnames = $('#bgrcolumnnames');

    var aval = acomps.val();
    var cval = colnames.val();

    if (aval != undefined) {
        if (aval.length > 0) {

            var enddict = aval.indexOf("]");
            var alist = aval.slice(0, enddict);
            alist = alist + ", " + addrcomp + "]";

        } else {
            var alist = "[" + addrcomp + "]";
        }
    } else {
        var alist = "[" + addrcomp + "]";
    }

    acomps.val(alist.toString());
    colnames.val(alist.toString());
}

function gbr_add_location_type(loctype) {

    var ltype = $("#bgqloctypes");
    var loc = ltype.val();
    var llist = "";

    if (loc != undefined) {
        if (loc.length > 0) {
            var endlist = loc.indexOf("]");
            llist = loc.slice(0, endlist);
            llist = llist + "," + loctype + "]"
        } else {
            llist = "[" + loctype + "]";
        }
    } else {
        llist = "[" + loctype + "]";
    }
    ltype.val(llist);
}

function gbr_select_language(language) {

    var lang = $("#bgrlanguage");
    lang.val(language);
}

// 
// ------------------------------------------------------
// Dataframe Subset Utility functions 
// ------------------------------------------------------
//
function get_subset_callback(fid) {
    /**
     * df subset main taskbar callback.
     *
     * Parameters:
     *  fid- function id
     *  gcid - geocoder id
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     get_subset_callback", fid);

    switch (fid) {
        case 0:
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", fid));
            window.scroll_to('DCDFSubsetUtility');
            break;
        case 1:
            var inputs = new Array();
            var inputParms = window.get_input_form_parms("datasubsetdf");
            inputs.push(inputParms);
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", (fid + ", " + inputs)));
            window.scroll_to('DCDFSubsetUtility');
            break;
        case 2:
            var inputs = window.get_input_form_parms("dcdfsubset");
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", (fid + ", " + inputs)));
            window.scroll_to('DCDFSubsetUtility');
            break;
        case 5:
            var inputs = window.get_input_form_parms("dcdfsubsetsearch");
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", (fid + ", " + inputs)));
            window.scroll_to('DCDFSubsetUtility');
            break;
        case 6:
            $('#gsfilterselectstring').val("");
            break;
        case 8:
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", fid));
            window.scroll_to('DCDFSubsetUtility');
            break;
        case 10:
        case 11:
            var inputs = window.get_input_form_parms("dcrundfsubset");
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", (fid + ", " + inputs)));
            window.scroll_to('DCDFSubsetUtility');
            break;
        case 12:
            var inputs = window.get_input_form_parms("dcsavedfsubset");
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", (fid + ", " + inputs)));
            window.scroll_to('DCDFSubsetUtility');
            break;
        case 13:
            var inputs = window.get_input_form_parms("sequencesubset");
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", (fid + ", " + inputs)));
            window.scroll_to('DCDFSubsetUtility');
            break;
        case 14:
            var inputs = new Array();
            inputs.push("SWDFSubsetUtility");
            window.run_code_in_cell(window.INSPECTION_TASK_BAR_ID, window.getJSPCode(window.INSPECTION_LIB, "display_data_inspection", 21 + "," + JSON.stringify(inputs)));
            window.scroll_to('DCDataInspection');
            break;
        case 15:
            window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "open_as_excel", 4));
            break;
        case 16:
            var inputs = window.get_input_form_parms("dcdfmanualsubset");
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", (fid + ", " + inputs)));
            window.scroll_to('DCDFSubsetUtility');
            break;
        case 17:
            var inputs = window.get_input_form_parms("dcdfnextsearch");
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", (fid + ", " + inputs)));
            window.scroll_to('DCDFSubsetUtility');
            break;
        case 18:
            $('#gsnextselectstring').val("");
            break;
        case 19:
            var inputs = window.get_input_form_parms("dcsavesavedfsubset");
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", (fid + ", " + inputs)));
            window.scroll_to('DCDFSubsetUtility');
            break;
        case 20:
            var inputs = window.get_input_form_parms("dcsavesavedfsubset");
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", (fid + ", " + inputs)));
            window.scroll_to('DCDFSubsetUtility');
            break;


    }
}

function set_filter_colname(colname) {
    /**
     * df subset set filter callback.
     *
     * Parameters:
     *  colname - column name
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     set_filter_colname", colname);

    var colnamefield = $('#gscolname');
    colnamefield.val(colname);

    var filtersstring = $("#gsfilterselectstring");
    var colselstring = filtersstring.val() + "( df['" + colname + "'] )"
    filtersstring.val(colselstring);

    var filtersnote = $('#addfilternote');
    filtersnote.text("Select an operator for this filter.");

    var parms = new Array();
    parms.push(-1);
    parms.push(colname);
    window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "get_dfsubset_vals", JSON.stringify(parms)));
}

function select_filter(ftitle) {
    /**
     * df subset set filter callback.
     *
     * Parameters:
     *  colname - column name
     */

    var parms = new Array();
    parms.push(ftitle);
    window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", ("14" + ", " + JSON.stringify(parms))));
}

// --------------------------
// DF Subset dhtml functions 
// --------------------------

function iscolnamedefined() {

    var filtersstring = getlastclause();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     iscolnamedefined", filtersstring);

    if ((filtersstring.indexOf('df[') > -1))
        return (true);
    else
        return (false);
}

function isvaluedefined() {

    var filtersstring = getlastclause();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     isvaluedefined", filtersstring);

    var operatoroffset = 0;
    var operatorlength = 0;

    if (filtersstring.indexOf('==') > -1) {
        operatoroffset = filtersstring.indexOf('==');
        operatorlength = 2;
    } else {
        if (filtersstring.indexOf('!=') > -1) {
            operatoroffset = filtersstring.indexOf('!=');
            operatorlength = 2;
        } else {
            if (filtersstring.indexOf('<') > -1) {
                operatoroffset = filtersstring.indexOf('<');
                operatorlength = 1;
            } else {
                if (filtersstring.indexOf('<=') > -1) {
                    operatoroffset = filtersstring.indexOf('<=');
                    operatorlength = 2;
                } else {
                    if (filtersstring.indexOf('>') > -1) {
                        operatoroffset = filtersstring.indexOf('>');
                        operatorlength = 1;
                    } else {
                        if (filtersstring.indexOf('>=') > -1) {
                            operatoroffset = filtersstring.indexOf('>=');
                            operatorlength = 2;
                        } else {
                            if (filtersstring.indexOf('isin') > -1) {
                                operatoroffset = filtersstring.indexOf('isin');
                                operatorlength = 6;
                            }
                        }
                    }
                }
            }
        }
    }

    if (operatoroffset > 0) {
        if (filtersstring.charAt((operatoroffset + operatorlength + 1)) != ")") {
            return (true);
        }
    }

    return (false);

}

function isoperatordefined() {

    var filtersstring = getlastclause();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     isoperatordefined", filtersstring);

    if ((filtersstring.indexOf('==') > -1) ||
        (filtersstring.indexOf('!=') > -1) ||
        (filtersstring.indexOf('<') > -1) ||
        (filtersstring.indexOf('<=') > -1) ||
        (filtersstring.indexOf('>') > -1) ||
        (filtersstring.indexOf('>=') > -1) ||
        (filtersstring.indexOf('isin') > -1) ||
        (filtersstring.indexOf('isnull') > -1) ||
        (filtersstring.indexOf('notnull') > -1))
        return (true);
    else
        return (false);
}

function getlastclause() {

    var filtersstring = $("#gsfilterselectstring");

    //console.log("getlastclause", filtersstring.val());

    //console.log("getlastclause", filtersstring.val().indexOf('or'));
    //console.log("getlastclause", filtersstring.val().indexOf('and'));


    if ((filtersstring.val().indexOf('or') < 0) &&
        (filtersstring.val().indexOf('and') < 0))
        return (filtersstring.val());
    else {

        var last_clause = filtersstring.val();

        //console.log("getlastclause last_clause", last_clause);


        var max_loop = 10;
        var loop_count = 0;

        while ((loop_count < max_loop) &&
            ((last_clause.indexOf("or") > -1) ||
                (last_clause.indexOf("and") > -1))) {

            //console.log("getlastclause loop", last_clause);

            loop_count = loop_count + 1;

            if (last_clause.indexOf("or") > -1)
                last_clause = last_clause.slice(last_clause.indexOf("or") + 3);
            else {
                last_clause = last_clause.slice(last_clause.indexOf("and") + 4);
                //console.log("getlastclause and", last_clause);
            }
        }

        return (last_clause);
    }
}


function getgsval(uval) {

    if (window.debug_flag)
        console.log("getgsval", uval);

    var filtersstring = $("#gsfilterselectstring");

    if ((iscolnamedefined()) &&
        (isoperatordefined())) {

        if (filtersstring.val().indexOf('isin') > -1) {
            var endisin = filtersstring.val().indexOf("])");
            newfstring = filtersstring.val().slice(0, (endisin));

            //console.log("newfstring", newfstring, endisin);
            if (filtersstring.val().indexOf('[]') > -1)
                newfstring = newfstring + uval + "]) )";
            else
                newfstring = newfstring + ", " + uval + "]) )";
        } else {

            var endfstring = get_last_close_paren(filtersstring.val());

            var newfstring = filtersstring.val().slice(0, endfstring);
            if (isNaN(uval))
                newfstring = newfstring + "'" + uval + "'" + " )";
            else
                newfstring = newfstring + uval + " )";
        }

        filtersstring.val(newfstring);

        if (filtersstring.val().indexOf('isin') > -1) {
            display_inline_help($('#addfilternote'), "To add another 'Column Value' to the 'isin' list click on the value.\nTo add another list value from the keypad enter a comma first");
        } else {
            display_inline_help($('#addfilternote'), "To add another clause to the current filter hit the 'or' or 'and' buttons.\nTo add another filter and save the current filter hit 'Add Filter To Criteria'.\nHit 'Get Subset' to get a subset with current filters");
        }

    }

}

function set_ds_colname(colname) {

    if (window.debug_flag)
        console.log("set_ds_colname", colname);

    var colnamefield = $('#gscolnames');
    if (colnamefield.val().length == 0) {
        colnamefield.val(colname);
    } else {
        var newstr = colnamefield.val() + "," + colname;
        colnamefield.val(newstr);
    }
}

function get_last_close_paren(selstring) {

    var filtersstring = $("#gsfilterselectstring");
    var filterselect = filtersstring.val();

    if (filterselect.indexOf(")", 0) > -1) {

        var numchars = filterselect.length;

        for (i = (numchars - 1); i - 1; i > -1) {

            if (filterselect[i] == ")")
                return (i);
        }
        return (-1);

    } else {
        return (-1);
    }
}

function keypad(keyvalue) {
    /**
     * dynamic html keypad entry.
     *
     * Parameters:
     *  keyvalue - key value
     */

    if (window.debug_flag)
        console.log("keypad", keyvalue);

    var filtersstring = $("#gsfilterselectstring");

    if ((iscolnamedefined()) &&
        (isoperatordefined())) {

        var endfstring = get_last_close_paren(filtersstring.val());
        var newfstring = "";

        if (filtersstring.val().indexOf('isin') > -1) {
            var endisin = filtersstring.val().indexOf("])");
            newfstring = filtersstring.val().slice(0, (endisin));

            //console.log("newfstring", newfstring, endisin);
            if (keyvalue == ",")
                newfstring = newfstring + keyvalue + "]) )";
            else
                newfstring = newfstring + keyvalue + "]) )";
        } else {
            if (keyvalue == ",")
                newfstring = filtersstring.val();
            else {
                newfstring = filtersstring.val().slice(0, endfstring);
                newfstring = newfstring + keyvalue + ")";
            }
        }

        filtersstring.val(newfstring);
    }

    if (filtersstring.val().indexOf('isin') > -1) {
        display_inline_help($('#addfilternote'), "Add to current number via the keypad or end current number with ',' for a list value. \nIf finished adding values hit 'Add Filter To Criteria' to complete the filter.");
    } else {
        display_inline_help($('#addfilternote'), "Continue adding to the current number via the keypad. \nIf finished defining a value hit 'Add Filter To Criteria' to complete the filter.");
    }
}

function operpad(keyvalue) {
    /**
     * dynamic html operator keypad entry.
     *
     * Parameters:
     *  keyvalue - key value
     */

    if (window.debug_flag)
        console.log("operpad", keyvalue);

    if (!isoperatordefined()) {
        if ((keyvalue == '.isnull()') || (keyvalue == '.notnull()') || (keyvalue == '.isin()')) {

            var filtersstring = $("#gsfilterselectstring");
            var endfstring = get_last_close_paren(filtersstring.val());

            var newfstring = filtersstring.val().slice(0, (endfstring - 1));
            if (keyvalue == '.isin()')
                newfstring = newfstring + "isin([])" + " )";
            else
                newfstring = newfstring + keyvalue + " )";
            //console.log(newfstring);
            filtersstring.val(newfstring);

        } else {

            var filtersstring = $("#gsfilterselectstring");
            var endfstring = get_last_close_paren(filtersstring.val());
            var newfstring = filtersstring.val().slice(0, endfstring);
            var colname = $("#gscolname").val();

            if (endfstring > -1) {
                newfstring = newfstring + " " + keyvalue + " )";
                filtersstring.val(newfstring);
            }

            display_inline_help($('#addfilternote'), "Select a value from the Column Values table or enter one by hand using the numeric keypad.");
        }
    }
}


function logicpad(keyvalue) {
    /**
     * dynamic html operator keypad entry.
     *
     * Parameters:
     *  keyvalue - key value
     */

    if (window.debug_flag)
        console.log("operpad", keyvalue);

    if ((keyvalue == 'or') || (keyvalue == 'and')) {

        var filtersstring = $("#gsfilterselectstring");
        var newfstring = filtersstring.val();
        if ((iscolnamedefined()) && (isoperatordefined()) && (isvaluedefined())) {
            if (newfstring[(newfstring.length - 1)] == ")") {
                newfstring = newfstring + " " + keyvalue + " ";
                filtersstring.val(newfstring);
                get_subset_callback(9);
            }
        }
    } else {

        if (keyvalue == 'not') {

        } else {

            var filtersstring = $("#gsselectstring");
            if (filtersstring.val().length > 0) {
                var newfstring = filtersstring.val() + " " + keyvalue + " ";
                filtersstring.val(newfstring);

                display_inline_help($('#addfilternote'), "Select a column name to use as the value for the filter.");
            }
        }
    }
}


// 
// ------------------------------------------------------
// Generic Functions Utility methods 
// ------------------------------------------------------
//

function generic_function_callback(fid) {
    /**
     * generic function process command callback.
     *
     * Parameters:
     *  fid - function id
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     generic_function_callback", fid);

    switch (fid) {
        case 12:
        case 13:
            var inputs = new Array();
            inputs.push(fid);
            window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_LIB, "process_sw_utilities", "16" + "," + JSON.stringify(inputs)));
            break;
        case 14:
            $("#gtmodule").val("");
            $("#gttitle").val("");
            $("#gtcode").val("");
            break;
        case 15:
            window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_LIB, "process_sw_utilities", "0"));
            break;
    }
    window.scroll_to('DCListUtility');
}


function select_gen_function(genid) {
    /**
     * generic function select function callback.
     *
     * Parameters:
     *  genid - gen function id
     */

    var funcid = "'" + genid + "'";

    window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_LIB, "process_sw_utilities", "17," + funcid));
    window.scroll_to('DCListUtility');
}


// 
// ------------------------------------------------------
// Census Utility methods 
// ------------------------------------------------------
//

function get_census_callback(fid) {
    /**
     * census process command callback.
     *
     * Parameters:
     *  fid - function id
     */

    if (window.debug_flag)
        console.log("get_census_callback", fid);

    switch (fid) {

        case 0:
        case 1:
        case 3:
        case 5:
        case 6:
        case 7:
        case 17:
        case 18:
        case 19:
        case 20:
        case 21:
        case 23:
        case 32:
        case 33:
        case 35:
        case 37:

            window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", fid));
            break;

        case 2:

            var inputs = new Array();
            var datasetids = ["Economic", "Education", "Employment", "Health_Insurance", "Housing", "Immigration", "Internet", "Population", "Social", "Transportation"];
            var datacontentcbs = new Array();


            for (var i = 0; i < datasetids.length; i++) {
                for (var j = 1; j < 6; j++) {

                    var currentcb = $("#cb" + j.toString() + datasetids[i]).prop("checked");
                    if (currentcb == true)
                        datacontentcbs.push("True");
                    else
                        datacontentcbs.push("False");
                }

                inputs.push(datacontentcbs);
                datacontentcbs = new Array();
            }

            window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", ("2, " + JSON.stringify(inputs))));
            break;

        case 4:

            var inputs = new Array();
            var datasetids = ["Economic", "Education", "Employment", "Health_Insurance", "Housing", "Immigration", "Internet", "Population", "Social", "Transportation"];
            var datasetcbs = new Array();

            for (var i = 0; i < datasetids.length; i++) {
                for (var j = 1; j < 6; j++) {

                    var currentcb = $("#cb" + j.toString() + datasetids[i]).prop("checked");
                    if (currentcb == true)
                        datasetcbs.push("True");
                    else
                        datasetcbs.push("False");
                }

                inputs.push(datasetcbs);
                datasetcbs = new Array();
            }

            window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", ("4, " + JSON.stringify(inputs))));
            break;

        case 24:
        case 25:
        case 36:
            var inputs = new Array();
            var datasetids = ["Economic", "Education", "Employment", "Health_Insurance", "Housing", "Immigration", "Internet", "Population", "Social", "Transportation"];
            var datacontentcbs = new Array();

            for (var i = 0; i < datasetids.length; i++) {
                for (var j = 1; j < 5; j++) {

                    var currentcb = $("#cb" + j.toString() + datasetids[i]).prop("checked");
                    if (currentcb == true)
                        datacontentcbs.push("True");
                    else
                        datacontentcbs.push("False");
                }

                inputs.push(datacontentcbs);
                datacontentcbs = new Array();
            }

            window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", (fid.toString() + " ," + JSON.stringify(inputs))));
            break;

        case 28:
        case 29:

            var selected_values = $('#subdatacolnames').val();
            window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", (fid.toString() + " ," + JSON.stringify(selected_values))));
            break;

        case 30:

            var inputs = new Array();
            var datasetids = new Array("Economic", "Education", "Employment", "Health_Insurance", "Housing", "Immigration", "Internet", "Population", "Social", "Transportation");
            var keytypes = new Array("ZipCode", "City", "County", "State");
            var i, j;

            var datasetradios = new Array();

            for (i = 0; i < datasetids.length; i++) {
                for (j = 0; j < keytypes.length; j++) {

                    var currentradio = $("#radio" + datasetids[i] + keytypes[j]).prop("checked");
                    if (currentradio == true)
                        datasetradios.push("True");
                    else
                        datasetradios.push("False");
                }

                inputs.push(datasetradios);
                datasetradios = new Array();

            }

            window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", 30 + ", " + JSON.stringify(inputs)));

            break;

        case 34:
            var fparms = get_input_form_parms("insertcoldf");
            window.clear_cell_output(window.SW_UTILS_CENSUS_TASK_BAR_ID);
            window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", (fid.toString() + " ," + fparms)));
            break;

        case 44:
            var inputs = new Array();
            inputs.push($("#colstoinsert option:selected").text());
            inputs.push($("#colstoinsert").val());

            window.clear_cell_output(window.SW_UTILS_CENSUS_TASK_BAR_ID);
            window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", 30 + ", " + JSON.stringify(inputs)));
            break;

        case 46:
            var inputs = new Array();
            inputs.push($("#colstoinsert option:selected").text());
            inputs.push($("#colstoinsert").val());
            inputs.push($('#newcoldtype').val());
            inputs.push($('#newcolnanval').val());

            window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "change_dfc_census_col_attrs", JSON.stringify(inputs)));
            break;

        case 47:
            var inputs = new Array();
            window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", 47 + ", " + JSON.stringify(inputs)));
            break;

        case 48:
            var inputs = new Array();
            window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", 48 + ", " + JSON.stringify(inputs)));
            break;

    }

    window.scroll_to('DCCensusUtility');
}

function get_census_dataset_details(datasetid) {
    /**
     * census process command callback.
     *
     * Parameters:
     *  datasetid - dataset id
     */

    window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", ("11, " + JSON.stringify(datasetid))));
    window.scroll_to('DCCensusUtility');
}

function get_census_subData_details(datasetid, subdataid) {
    /**
     * census process command callback.
     *
     * Parameters:
     *  datasetid - dataset id
     *  subdataid - subset id
     */

    if (window.debug_flag)
        console.log("get_census_subData_details", datasetid, subdataid);


    var inputs = new Array();
    inputs.push(datasetid);
    inputs.push(subdataid);

    window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", ("22, " + JSON.stringify(inputs))));
    window.scroll_to('DCCensusUtility');
}

function get_load_cols_subData_details(datasetid, subdataid) {
    /**
     * census process command callback.
     *
     * Parameters:
     *  datasetid - dataset id
     *  subdataid - subset id
     */

    if (window.debug_flag)
        console.log("get_load_cols_subData_details", datasetid, subdataid);

    var inputs = new Array();

    inputs.push(datasetid);
    inputs.push(subdataid);

    window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", ("7, " + JSON.stringify(inputs))));
    window.scroll_to('DCCensusUtility');
}

function get_configure_subData_details(datasetid, subdataid) {
    /**
     * census process command callback.
     *
     * Parameters:
     *  datasetid - dataset id
     *  subdataid - subset id
     */

    if (window.debug_flag)
        console.log("get_configure_subData_details", datasetid, subdataid);

    var inputs = new Array();
    inputs.push(datasetid);
    inputs.push(subdataid);

    window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", ("22, " + JSON.stringify(inputs))));
    window.scroll_to('DCCensusUtility');
}

function get_configure_dataset_details(dtid, datasetid) {
    /**
     * census process command callback.
     *
     * Parameters:
     *  datasetid - dataset id
     */

    if (window.debug_flag)
        console.log("get_configure_dataset_details", dtid, datasetid);

    var inputs = new Array();
    inputs.push(datasetid);
    inputs.push(dtid);
    inputs.push("1");

    window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", ("21, " + JSON.stringify(inputs))));
    window.scroll_to('DCCensusUtility');
}


get_df_census_dataset_details

function get_df_census_dataset_details(dtid, datasetid) {
    /**
     * census process command callback.
     *
     * Parameters:
     *  datasetid - dataset id
     */

    if (window.debug_flag)
        console.log("get_df_census_dataset_details", dtid, datasetid);

    var inputs = new Array();
    inputs.push(datasetid);
    inputs.push(dtid);
    inputs.push("0");


    window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", ("21, " + JSON.stringify(inputs))));
    window.scroll_to('DCCensusUtility');
}

function scroll_census_cols(datasetid, subdataid, colnameid, direction) {
    /**
     * census process command callback.
     *
     * Parameters:
     *  datasetid - dataset id
     *  subdataid - subset id
     *  colnameid - subset id
     *  direction - direction
     */

    var inputs = new Array();
    inputs.push(datasetid);
    inputs.push(subdataid);
    inputs.push(colnameid);
    inputs.push(direction);

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     scroll_census_cols", inputs);

    window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", ("15, " + JSON.stringify(inputs))));
    window.scroll_to('DCCensusUtility');
}

function get_select_cols_subData_details(datasetid, subdataid) {
    /**
     * census process command callback.
     *
     * Parameters:
     *  datasetid - dataset id
     *  subdataid - subset id
     */

    var inputs = new Array();
    inputs.push(datasetid);
    inputs.push(subdataid);

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     get_select_cols_subData_details", inputs);

    window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", ("30, " + JSON.stringify(inputs))));
    window.scroll_to('DCCensusUtility');
}

function set_census_cbs(cbid) {
    /**
     * census process checkbox callback.
     *
     * Parameters:
     *  cbid - checkbox id
     */

    var idnum = 0;
    var datasetid = "";
    var i = 0;

    if (cbid.indexOf("cb1") > -1) idnum = 1;
    else if (cbid.indexOf("cb2") > -1) idnum = 2;
    else if (cbid.indexOf("cb3") > -1) idnum = 3;
    else if (cbid.indexOf("cb4") > -1) idnum = 4;
    else if (cbid.indexOf("cb5") > -1) idnum = 5;
    else if (cbid.indexOf("cb6") > -1) idnum = 6;
    else idnum = 0;

    if (cbid.indexOf("Economic") > -1) datasetid = "Economic";
    else if (cbid.indexOf("Education") > -1) datasetid = "Education";
    else if (cbid.indexOf("Employment") > -1) datasetid = "Employment";
    else if (cbid.indexOf("Health_Insurance") > -1) datasetid = "Health_Insurance";
    else if (cbid.indexOf("Housing") > -1) datasetid = "Housing";
    else if (cbid.indexOf("Immigration") > -1) datasetid = "Immigration";
    else if (cbid.indexOf("Internet") > -1) datasetid = "Internet";
    else if (cbid.indexOf("Population") > -1) datasetid = "Population";
    else if (cbid.indexOf("Social") > -1) datasetid = "Social";
    else if (cbid.indexOf("Transportation") > -1) datasetid = "Transportation";
    else datasetid = ""

    if ($("#" + cbid).prop("checked") == true) {
        if (idnum == 6) {
            for (i = 1; i < 6; i++) {
                $("#cb" + i.toString() + datasetid).prop("checked", false);
            }
        } else {
            $("#cb6" + datasetid).prop("checked", false);
        }
    }
}

function get_census_cols(dtid) {

    var fparms;

    switch (dtid) {

        case 0:
            fparms = get_input_form_parms("dcdfcensusgetcolsinput");
            break;
        case 1:
            fparms = get_input_form_parms("dcdfcensusgetcolscityinput");
            break;
        case 2:
            fparms = get_input_form_parms("dcdfcensusgetcolscountyinput");
            break;
        case 3:
            fparms = get_input_form_parms("dcdfcensusgetcolsstatesinput");
            break;
    }

    window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", ("8, " + JSON.stringify(fparms))));
    window.scroll_to('DCCensusUtility');
}

function change_get_center_pt_col(selectid) {
    /**
     * change get center pt source
     *
     * Parameters:
     *  selectid   - select form id
     * 
     */

    var colname = $("#" + selectid).val();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "change_get_center_pt_col", selectid, colname);

    var collist = $("#collist").val();

    if (collist.length == 0) {
        $("#collist").val(colname);
    } else {
        if (collist.indexOf("[") > -1) {
            $("#collist").val(colname);
        } else {
            collist = "[" + $("#collist").val() + ", " + colname + "]";
            $("#collist").val(collist);
        }
    }
}

function change_get_center_pt(selectid) {
    /**
     * change get center pt source
     *
     * Parameters:
     *  selectid   - select form id
     * 
     */

    var center_pt_source = $("#" + selectid).val();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "change_get_center_pt", selectid, center_pt_source);

    if (center_pt_source == "True") {
        $("#addrcol").prop("disabled", false);
        $("#collist").prop("disabled", false);
        $("#centerpt").prop("disabled", true);

    } else {
        $("#addrcol").prop("disabled", true);
        $("#collist").prop("disabled", true);
        $("#centerpt").prop("disabled", false);
        $("#centerpt").prop("readonly", false);
    }
}

function export_census_to_db(dfid) {
    /**
     * export a census df to a db
     *
     * Parameters:
     *  dfid   - dataframe id
     * 
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "export_census_to_db", dfid);

}

function export_census_to_df(dfid) {
    /**
     * export a census df to a destination
     *
     * Parameters:
     *  dfid   - dataframe id
     * 
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "export_census_to_df", dfid);

}

function select_new_insert_df(selectid) {
    /**
     * select a new df to insert cols into
     *
     * Parameters:
     *  dfid   - dataframe id
     * 
     */

    var dftitle = $("#" + selectid).val();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "select_new_insert_df", dftitle);

    window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", ("33, " + JSON.stringify(dftitle))));
    window.scroll_to('DCCensusUtility');
}

function select_new_insert_df_index_type(selid) {
    /**
     * select a new col to use as index
     *
     * Parameters:
     *  dfid   - dataframe id
     * 
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "select_new_insert_df_index_type", selid);

    $("#censusindexcols").val("");

}

function select_new_insert_df_col(selectid) {
    /**
     * select a new col to use as index
     *
     * Parameters:
     *  dfid   - dataframe id
     * 
     */

    var itype = $("#censusindextype").val();
    var index = 0;

    var icols = $("#censusindexcols").val();

    var colname = $("#" + selectid).val();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "select_new_insert_df_col", colname, itype, icols);

    switch (itype) {

        case "[zipcode]":
            index = 0;
            break;
        case "[city,state]":
            index = 1;
            break;
        case "[county,state]":
            index = 2;
            break;
        default:
            index = 3;
            break;
    }

    if ((index == 0) || (index == 3)) {
        $("#censusindexcols").val("[" + colname + "]");
    } else {

        if (icols.indexOf("[") > -1) {
            if (icols.indexOf(",]") > -1) {
                icols = icols.replace(",]", "," + colname + "]")
                $("#censusindexcols").val(icols);
            } else {
                $("#censusindexcols").val("[" + colname + ",]");
            }
        } else {
            $("#censusindexcols").val("[" + colname + ",]");
        }
    }
}


function export_df_from_census(datasetid) {

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "export_df_from_census", datasetid);

    window.run_code_in_cell(window.EXPORT_TASK_BAR_ID, window.getJSPCode(window.EXPORT_LIB, "process_export_form", ("4" + ", " + JSON.stringify(datasetid))));
    window.scroll_to('DCDataExport');

}

function export_to_db_from_census(datasetid) {

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "export_to_db_from_census", datasetid);

    window.run_code_in_cell(window.EXPORT_TASK_BAR_ID, window.getJSPCode(window.EXPORT_LIB, "process_export_form", ("5" + ", " + JSON.stringify(datasetid))));
    window.scroll_to('DCDataExport');

}

function get_df_dist_from_cols(selectid) {

    var dftitle = $("#" + selectid).val();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "get_df_dist_from_cols", selectid, dftitle);

    var fparms = get_input_form_parms("addrdfdist");

    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", "56" + ", " + fparms));
    window.scroll_to('DCGeocodeUtility');

}

function get_df_dist_to_cols(selectid) {

    var dftitle = $("#" + selectid).val();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "get_df_dist_to_cols", selectid, dftitle);

    var fparms = get_input_form_parms("addrdfdist");

    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", "56" + ", " + fparms));
    window.scroll_to('DCGeocodeUtility');

}

function change_coords_columns(currentColumns, colname) {

    if (window.debug_flag)
        console.log("currentColumns", currentColumns.val(), colname);

    if (currentColumns.val().indexOf('[') < 0) {
        newColumns = "[" + colname + "]";
        currentColumns.val(newColumns);
    } else {
        if (window.debug_flag)
            console.log("currentColumns yes [", currentColumns.val());

        if (currentColumns.val().indexOf(',') < 0) {
            if (window.debug_flag)
                console.log("currentColumns no ,", currentColumns.val());
            newColumns = currentColumns.val();
            newColumns = newColumns.replace("]", "," + colname + "]")
            if (window.debug_flag)
                console.log("newColumns ", newColumns);
            currentColumns.val(newColumns);
        } else {
            newColumns = "[" + colname + "]";
            currentColumns.val(newColumns);
        }
    }
}

function select_from_df_dist_col(selectid) {

    var colname = $("#" + selectid).val();
    var currentColumns = $('#fromlatlngcolumns');

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "select_from_df_dist_col", selectid, colname);

    change_coords_columns(currentColumns, colname);
}

function select_to_df_dist_col(selectid) {

    var colname = $("#" + selectid).val();
    var currentColumns = $('#tolatlngcolumns');

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "select_to_df_dist_col", selectid, colname);

    change_coords_columns(currentColumns, colname);
}

function select_to_coord_type(selectid) {

    var colname = $("#" + selectid).val();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "select_to_coord_type", selectid, colname);

    var fparms = get_input_form_parms("addrdfdist");

    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", "56" + ", " + fparms));
    window.scroll_to('DCGeocodeUtility');

}

function get_df_center_cols(selectid) {

    var dftitle = $("#" + selectid).val();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "get_df_center_cols", selectid, dftitle);

    var fparms = get_input_form_parms("addrcenter");

    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", "57" + ", " + fparms));
    window.scroll_to('DCGeocodeUtility');

}

function change_df_lat_lng_columns(colname, currentColumns) {

    if (currentColumns.val().indexOf('[') < 0) {
        newColumns = "[" + colname + "]";
        currentColumns.val(newColumns);
    } else {
        if (currentColumns.val().indexOf(',') < 0) {
            newColumns = currentColumns.val();
            newColumns = newColumns.replace("]", "," + colname + "]")
            currentColumns.val(newColumns);
        } else {
            newColumns = "[" + colname + "]";
            currentColumns.val(newColumns);
        }
    }
}


function select_df_center_col(selectid) {

    var colname = $("#" + selectid).val();
    var currentColumns = $('#centerdflatlng');

    change_df_lat_lng_columns(colname, currentColumns);

}

function get_df_center_dist_cols(selectid) {

    var dftitle = $("#" + selectid).val();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "get_df_center_dist_cols", selectid, dftitle);

    var fparms = get_input_form_parms("addrdfcenterdist");

    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", "58" + ", " + fparms));
    window.scroll_to('DCGeocodeUtility');

}

function select_df_center_dist_col(selectid) {

    var colname = $("#" + selectid).val();
    var currentColumns = $('#addrdfcenterptlatlngs');

    change_df_lat_lng_columns(colname, currentColumns);
}

function get_df_center_dist_coords_cols(selectid) {

    var dftitle = $("#" + selectid).val();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "get_df_center_dist_coords_cols", selectid, dftitle);

    var fparms = get_input_form_parms("addrdfcenterdist");

    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", "58" + ", " + fparms));
    window.scroll_to('DCGeocodeUtility');

}

function select_df_center_dist_coords_col(selectid) {

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "select_df_center_dist_coords_col", selectid);

    var colname = $("#" + selectid).val();
    var currentColumns = $('#addrdfdistlatlngs');

    change_df_lat_lng_columns(colname, currentColumns);
}

function exit_bulk_geocoding() {

    if (window.confirm("Exitting Bulk Geocoder results in loss of all current data. Exit?")) {
        window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB, "display_geocode_utility", 25));
        window.reset_dependents([false, true, false, false, false, false]);
        window.scroll_to('DCGeocodeUtility');
    }
}

function show_geopy_exceptions() {

    geopy_url = "https://geopy.readthedocs.io/en/stable/#exceptions";

    window.open(geopy_url);

}

function display_zipcode(fid) {
    /**
     * display zipcodes.
     *
     * Parameters:
     *  fid  - function id
     */

    var inputs = [fid];
    window.run_code_in_cell(window.SW_UTILS_ZIPCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_ZIPCODE_LIB, "display_zipcode_utility", fid));
    window.scroll_to('DCZipcodeUtility');
}


function process_zipcode(fid) {
    /**
     * display zipcodes.
     *
     * Parameters:
     *  fid  - function id
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "process_zipcode", fid);

    formid = null;

    switch (fid) {

        case 7:
            formid = "zipcodeattrs";
            break;
        case 8:
            formid = "zipcodecities";
            break;
        case 9:
            formid = "statecounties";
            break;
        case 10:
            formid = "countycities";
            break;
        case 11:
            formid = "statecities";
            break;

    }

    var fparms = get_input_form_parms(formid);

    window.run_code_in_cell(window.SW_UTILS_ZIPCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_ZIPCODE_LIB, "display_zipcode_utility", fid + ", " + fparms));
    window.scroll_to('DCZipcodeUtility');
}


function change_state_for_counties(selectid) {
    /**
     * display zipcodes.
     *
     * Parameters:
     *  fid  - function id
     */

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "change_state_for_counties", selectid);

    var state = $("#" + selectid).val();
    var fparms = get_input_form_parms("countycities");

    window.run_code_in_cell(window.SW_UTILS_ZIPCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_ZIPCODE_LIB, "display_zipcode_utility", 5 + ", " + fparms));
    window.scroll_to('DCZipcodeUtility');

}


function change_subset_cols(selectid) {
    add_select_val(selectid, "gscolnames");
}


function change_run_subset_cols(selectid) {
    add_select_val(selectid, "runcolnames");
}


function change_insert_col_dtype(selectid) {
    add_select_val(selectid, "coltoinsertdtype");
}

var select_subdata_cols = new Array();

function set_select_subdata_cols(col_vals) {
    select_subdata_cols = col_vals;

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "set_select_subdata_cols", select_subdata_cols);

}

function change_subset_col_names_lists(selectid) {


    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "change_subset_col_names_lists : selectid", selectid);

    var colname = $("#" + selectid + " option:selected").text();
    var colval = $("#" + selectid).val();
    var currentColumns = $("#censuscolssellist");
    var currentnames = currentColumns.val();

    if (window.debug_flag) {
        console.log(log_prefix + "\n" + "     " + "change_subset_col_names_lists : colname ", colname);
        console.log(log_prefix + "\n" + "     " + "change_subset_col_names_lists : colval ", colval);
        console.log(log_prefix + "\n" + "     " + "change_subset_col_names_lists : currentColumns ", currentColumns);
        console.log(log_prefix + "\n" + "     " + "change_subset_col_names_lists : currentnames ", currentnames);
    }

    if (colval == -2) {
        var newColumns = "None";
        currentColumns.val(newColumns);
        select_subdata_cols = new Array();
        select_subdata_cols.push(-2);
    } else {
        if (colval == -1) {
            var newColumns = "All";
            currentColumns.val(newColumns);
            select_subdata_cols = new Array();
            select_subdata_cols.push(-1);
        } else {
            if ((currentnames == "All") || (currentnames == "None")) {
                currentColumns.val(colname);
                select_subdata_cols = new Array();
            } else {
                currentColumns.val(currentnames + "\n" + colname);
            }
            select_subdata_cols.push(colval);
        }
    }

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "change_subset_col_names_lists : select_subdata_cols", select_subdata_cols);

}

function get_subset_col_names_callback(fid) {

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "get_subset_col_names_callback", fid, select_subdata_cols);

    var inputs = new Array();

    var colname = $("#censuscolssellist").val();

    if (select_subdata_cols.length > 0) {
        inputs.push(select_subdata_cols);
        select_subdata_cols = new Array();
    } else {
        var cols = $("#censuscolssellist").val();
        inputs.push(cols);
    }

    window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", fid + ", " + JSON.stringify(inputs)));
    window.scroll_to('DCCensusUtility');

}



function get_census_dataset_columns(datasetid, keyid) {

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "get_census_dataset_columns", datasetid, keyid);

    var inputs = new Array();
    inputs.push(datasetid);
    inputs.push(keyid);

    window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", "38, " + JSON.stringify(inputs)));
    window.scroll_to('DCCensusUtility');

}

function get_census_cols_details(datasetid, subsetid) {

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "get_census_cols_details", datasetid, subsetid);

    var inputs = new Array();
    inputs.push(datasetid);
    inputs.push(subsetid);

    window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", "40, " + JSON.stringify(inputs)));
    window.scroll_to('DCCensusUtility');

}

function select_dataset_radio(datasetid) {

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "select_dataset_radio", datasetid);


    var datasetids = new Array("Economic", "Education", "Employment", "Health_Insurance", "Housing", "Immigration", "Internet", "Population", "Social", "Transportation");
    var keytypes = new Array("ZipCode", "City", "County", "State");

    var i, j;

    for (i = 0; i < datasetids.length; i++) {
        if (!(datasetids[i] == datasetid)) {
            for (j = 0; j < keytypes.length; j++) {
                $("#radio" + datasetids[i] + keytypes[j]).prop("checked", false);
            }
        }
    }
}

function change_subset_col_selected_attrs(selectid) {

    var colname = $("#" + selectid + " option:selected").text();
    var colval = $("#" + selectid).val();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "change_subset_col_selected_attrs", selectid, colname, colval);

    var inputs = new Array();
    inputs.push(colname);
    inputs.push(colval);

    window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "change_selected_dfc_census_col", JSON.stringify(inputs)));

}

function change_census_df(selectid) {

    var dfname = $("#" + selectid + " option:selected").text();
    var df_list = $("#censusdfstoload").val();
    var df_keys = $("#userdfsindexkeys").val();
    userdfsindexkeys

    var inputs = new Array();
    inputs.push(df_list);
    inputs.push(dfname);
    inputs.push(df_keys);
    //inputs.push(colval);

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "change_census_df", selectid, inputs);

    window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "change_census_df_to_insert_from", JSON.stringify(inputs)));

}

function change_user_df(selectid) {

    var census_df_name = $("#censusdfstoload").val();
    var dfname = $("#" + selectid + " option:selected").text();
    var dfkeys = $("#userdfsindexkeys").val();

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "change_user_df", selectid, census_df_name, dfname);

    var inputs = new Array();
    inputs.push(census_df_name);
    inputs.push(dfname);
    inputs.push(dfkeys);

    window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", "49, " + JSON.stringify(inputs)));
    window.scroll_to('DCCensusUtility');


}

function change_user_df_col(selectid) {

    var colname = $("#" + selectid + " option:selected").text();
    var current_keys = $("#userdfsindexkeys").val();
    current_keys = current_keys.replace("[", "");
    current_keys = current_keys.replace("]", "");

    if (window.debug_flag)
        console.log(log_prefix + "\n" + "     " + "change_user_df_col", selectid, colname, current_keys);

    var firstkey = "";
    var secondkey = "";

    var commaloc = current_keys.indexOf(",");
    if (commaloc > -1) {
        firstkey = current_keys.substr(0, commaloc);
        secondkey = current_keys.substr(commaloc + 1, current_keys.length);
    } else {
        firstkey = current_keys
        secondkey = ""
    }

    if (firstkey.indexOf("key col") > -1) {
        firstkey = colname;
    } else {

        if (secondkey.indexOf("key col") > -1) {
            secondkey = colname;
        } else {
            firstkey = colname;
        }
    }

    var new_keys = "[" + firstkey;
    if (secondkey.length > 0) {
        new_keys = new_keys + "," + secondkey;
    }
    new_keys = new_keys + "]"

    $("#userdfsindexkeys").val(new_keys);


}