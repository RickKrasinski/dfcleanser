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

    window.clear_cell_output(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID);
    window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_LIB, "process_sw_utilities", id));
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

function select_dict(key) {
    /**
     * data structures utility select dict.
     *
     * Parameters:
     *  key - dict to display
     */

    window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_LIB, "process_sw_utilities", "10, " + JSON.stringify(key)));
    window.scroll_to('DCListUtility');
}

function select_list(key) {
    /**
     * data structures utility select list.
     *
     * Parameters:
     *  key - dict to display
     */

    window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_LIB, "process_sw_utilities", "9, " + JSON.stringify(key)));
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

    console.log("get_geocode_form_id", id);

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

    var fparms = get_input_form_parms(get_geocode_form_id(gcid, gtype, gmode));
    var inputs = [gcid, gtype, gmode, fparms];

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
    console.log("process_batch_geocoder", fid, fparms);
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

    var formid = "";
    switch (fid) {
        case 5:
        case 6:
        case 7:
        case 8:
            formid = "geocodebulkproc";
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

    switch (fid) {
        case 0:
        case 1:
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", fid));
            window.scroll_to('DCDFSubsetUtility');
            break;
        case 2:
        case 3:
        case 4:
            if (fid == 3) { var inputs = window.get_input_form_parms("dcdfsubset"); } else {
                if (fid == 2) { var inputs = window.get_input_form_parms("dcdfsubset"); } else {
                    if (fid == 4) { var inputs = window.get_input_form_parms("dcdfsubsetsearch"); } else { var inputs = new Array(); }
                }
            }
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", (fid + ", " + inputs)));
            window.scroll_to('DCDFSubsetUtility');
            break;
        case 5:
            $('#gsrowrange').val("");
            $('#gscolnames').val("");
            $('#gsadddrop').val("");
            $('#subsetfname').val("");
            break;
        case 6:
            $('#gscolname').val("");
            $('#gscoloper').val("");
            $('#gscolvalue').val("");
            $('#gscolandor').val("");
            $('#gscolandor').val("");
            var parms = new Array();
            parms.push(1);
            parms.push("");
            window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "get_dfsubset_vals", JSON.stringify(parms)));
            break;

        case 7:
            var condcolname = $('#gscolname').val();
            var condcoloper = $('#gscoloper').val();
            if (condcoloper != null)
                if (condcoloper.length > 0) {
                    var condcoloperarray = condcoloper.split(",");
                }

            var condcolvals = $('#gscolvalue').val();
            if (condcolvals != null)
                if (condcolvals.length > 0) {
                    var condcolvalsarray = condcolvals.split("  ,  ");
                }

            var condcolandor = $('#gscolandor').val();
            var condcolandorarray = new Array();
            if (condcolandor != null)
                if (condcolandor.length > 0) {
                    condcolandorarray = condcolandor.split(",");
                }

            var cselectandor = $('#gsselandor').val();
            if (cselectandor != null)
                if (cselectandor.length == 0) {
                    cselectandor = " AND ";
                }

            var newcselectstring = "";
            var cselectstring = $('#gsselectstring').val();
            if (cselectstring != null)
                if (cselectstring.length > 0) {
                    newcselectstring = cselectstring + " " + cselectandor + " " + window.NEW_LINE;
                } else {
                    $('#gsselandor').val("AND");
                    newcselectstring = newcselectstring;
                }

            var newcondition = "( ";
            var i;
            for (i = 0; i < condcolvalsarray.length; i++) {
                newcondition = newcondition + "( " + "'" + condcolname + "'" + condcoloperarray[i] + condcolvalsarray[i] + " )";

                if (i < (condcolvalsarray.length - 1)) {
                    newcondition = newcondition + " " + condcolandorarray[i] + window.NEW_LINE;
                }
            }

            $('#gscolname').val("");
            $('#gscoloper').val("");
            $('#gscolvalue').val("");
            $('#gscolandor').val("");

            var parms = new Array();
            parms.push(condcolname);
            parms.push(newcondition);
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", fid + ", " + JSON.stringify(parms)));
            window.scroll_to('DCDFSubsetUtility');
            break;

        case 10:
        case 12:
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", fid));
            window.scroll_to('DCDFSubsetUtility');
            break;
        case 11:
        case 13:
            var inputs = window.get_input_form_parms("dcdfsubsetfilters")
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", fid + ", " + JSON.stringify(inputs)));
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

    var colnamefield = $('#gscolname');
    colnamefield.val(colname);
    $('#gscoloper').val("");
    $('#gscolvalue').val("");
    $('#gscolandor').val("");
    $('#gscolandor').val("");
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
function getgsval(uval) {
    var operfield = $('#gscoloper');
    if (operfield.val().length == 0) {
        operfield.val('==');
    } else {
        var newstr = operfield.val() + ",==";
        operfield.val(newstr);

        var andorfield = $('#gscolandor');
        if (andorfield.val().length == 0) {
            andorfield.val("or");
        } else {
            var newstr1 = andorfield.val() + ",or";
            andorfield.val(newstr1);
        }
    }

    var uvalfield = $('#gscolvalue');
    if (uvalfield.val().length == 0) {
        uvalfield.val("'" + uval + "'");
    } else {
        var newstr = uvalfield.val() + "  ,  " + "'" + uval + "'";
        uvalfield.val(newstr);
    }
}

function set_ds_colname(colname) {
    console.log("set_ds_colname", colname);
    var colnamefield = $('#gscolnames');
    if (colnamefield.val().length == 0) {
        colnamefield.val(colname);
    } else {
        var newstr = colnamefield.val() + " ," + colname;
        colnamefield.val(newstr);

    }
}

function set_col_oper(operator) {
    var condcoloper = $('#gscoloper').val();
    if (condcoloper != null)
        if (condcoloper.length > 0) {

            var lastcomma = condcoloper.lastIndexOf(",");

            if (lastcomma == -1) {
                $('#gscoloper').val(operator);
            } else {
                $('#gscoloper').val(condcoloper.slice(0, lastcomma) + "," + operator);
            }
        } else {
            var colvals = $('#gscolvalue').val();
            if (colvals != null)
                if (colvals.length > 0)
                    $('#gscoloper').val(operator);
        }
}

function set_clause_oper(logical) {
    var condcolandor = $('#gscolandor').val();
    if (condcolandor != null)
        if (condcolandor.length > 0) {

            var lastcomma = condcolandor.lastIndexOf(",");

            var newcondcolandor = "";
            if (lastcomma == -1) {
                newcondcolandor = logical;
            } else {
                newcondcolandor = condcolandor.slice(0, lastcomma) + "," + logical;
            }

            $('#gscolandor').val(newcondcolandor);
        } else {
            var colvals = $('#gscolvalue').val();
            if (colvals != null)
                if (colvals.length > 0)
                    if (colvals.indexOf(",") > -1)
                        $('#gscolandor').val(logical);
        }
}

function set_filter_oper(logical) {
    var condselandor = $('#gsselandor').val();

    if (condselandor != null)
        if (condselandor.length > 0) {

            if (logical == "NOT") {
                if (condselandor.indexOf("NOT") == -1)
                    $('#gsselandor').val($('#gsselandor').val() + " NOT");
            } else {
                $('#gsselandor').val(logical);
            }
        } else {
            if (logical != "NOT") {
                $('#gsselandor').val(logical);
            }
        }
}

// 
// ------------------------------------------------------
// Generic Functions Utility methods 
// ------------------------------------------------------
//
function genfunction_task_bar_callback(fid) {
    /**
     * generic function main taskbar callback.
     *
     * Parameters:
     *  fid - function id
     */

    window.run_code_in_cell(window.SW_UTILS_GENFUNC_TASK_BAR_ID, window.getJSPCode(window.GEN_FUNCTION_LIB, "display_gen_function", fid));
    window.scroll_to('DCGenFunctionUtility');
}

function generic_function_callback(fid) {
    /**
     * generic function process command callback.
     *
     * Parameters:
     *  fid - function id
     */

    console.log("generic_function_callback", fid);
    var inputs = new Array();
    switch (fid) {
        case 0:

            window.delete_output_cell(window.SW_UTILS_GENFUNC_CODECELL_ID);

            var tcell = window.get_cell_for_id(window.SW_UTILS_GENFUNC_TASK_BAR_ID);
            window.select_cell(SW_UTILS_GENFUNC_TASK_BAR_ID);

            IPython.notebook.insert_cell_below('code');
            var cell = IPython.notebook.select_next().get_selected_cell();

            var code = "def dfcleanser_generic_function(parm1, parm2) : " + window.NEW_LINE;
            code = code + '    """' + window.NEW_LINE;
            code = code + "    * ------------------------------------------------------------------------" + window.NEW_LINE;
            code = code + "    * function : description" + window.NEW_LINE;
            code = code + "    *" + window.NEW_LINE;
            code = code + "    * parms :" + window.NEW_LINE;
            code = code + "    *  parm1   - description" + window.NEW_LINE;
            code = code + "    *  parm2   - description" + window.NEW_LINE;
            code = code + "    *" + window.NEW_LINE;
            code = code + "    * returns :" + window.NEW_LINE;
            code = code + "    *     description" + window.NEW_LINE;
            code = code + "    *" + window.NEW_LINE;
            code = code + "    * Notes :" + window.NEW_LINE;
            code = code + "    *    dfcleanser generic function" + window.NEW_LINE;
            code = code + "    * -------------------------------------------------------------------------" + window.NEW_LINE;
            code = code + '    """' + window.NEW_LINE;
            cell.set_text(code);

            // add the cellid metadata
            var dfcellDict = { "dfc_cellid": "DCGenFunctionCodeCell" };
            //var dfcleanserDict = { "dfcleanser_metadata": dfcellDict };
            //var newcellDict = { "dfcleanser_metadata": dfcellDict, "scrolled": true, "trusted": true };
            cell.metadata = { "dfcleanser_metadata": dfcellDict, "scrolled": true, "trusted": true };

            inputs.push(0, [code])
            window.run_code_in_cell(window.SW_UTILS_GENFUNC_TASK_BAR_ID, window.getJSPCode(window.GEN_FUNCTION_LIB, "display_gen_function", "2" + "," + JSON.stringify(inputs)));

            break;

        case 1:
            var codecell = get_cell_for_id(window.SW_UTILS_GENFUNC_CODECELL_ID);
            window.select_cell(window.SW_UTILS_GENFUNC_CODECELL_ID);
            console.log("codecell", codecell)
            if (codecell != null) {
                var codecelltext = codecell.get_text();
                console.log("codecelltext", codecelltext)
            } else {
                var codecelltext = "";
            }

            window.delete_output_cell(window.SW_UTILS_GENFUNC_CODECELL_ID);

            var gtmodule = $('#gtmodule').val();
            if (gtmodule == null) gtmodule = "";
            var gttitle = $('#gttitle').val();
            if (gttitle == null) gttitle = "";

            inputs.push(fid, gtmodule, gttitle, codecelltext);
            window.run_code_in_cell(window.SW_UTILS_GENFUNC_TASK_BAR_ID, window.getJSPCode(window.GEN_FUNCTION_LIB, "display_gen_function", "2" + "," + JSON.stringify(inputs)));
            break;

        case 2:

            var fparms = get_input_form_parms("genfuncform");
            inputs.push(fid, fparms);
            window.run_code_in_cell(window.SW_UTILS_GENFUNC_TASK_BAR_ID, window.getJSPCode(window.GEN_FUNCTION_LIB, "display_gen_function", "2" + "," + JSON.stringify(inputs)));
            break;

        case 3:
        case 4:

            var gtmodule = $('#gtmodule').val();
            if (gtmodule == null) gtmodule = "";
            var gttitle = $('#gttitle').val();
            if (gttitle == null) gttitle = "";

            inputs.push(fid, gtmodule, gttitle);
            window.run_code_in_cell(window.SW_UTILS_GENFUNC_TASK_BAR_ID, window.getJSPCode(window.GEN_FUNCTION_LIB, "display_gen_function", "2" + "," + JSON.stringify(inputs)));
            break;

        case 5:
            window.delete_output_cell(window.SW_UTILS_GENFUNC_CODECELL_ID);
            window.run_code_in_cell(window.SW_UTILS_GENFUNC_TASK_BAR_ID, window.getJSPCode(window.GEN_FUNCTION_LIB, "display_gen_function", "0"));
            break;

        case 7:
            inputs.push(fid);
            window.run_code_in_cell(window.SW_UTILS_GENFUNC_TASK_BAR_ID, window.getJSPCode(window.GEN_FUNCTION_LIB, "display_gen_function", "2" + "," + JSON.stringify(inputs)));
            break;


    }
    window.scroll_to('DCGenFunctionUtility');
}

function delete_genfunc_test_code_cell() {
    /**
     * delete generic function test code cell.
     *
     */
    window.delete_output_cell(window.SW_UTILS_GENFUNC_CODECELL_ID);
    window.scroll_to('DCGenFunctionUtility');
}

function load_genfunc_test_code_cell(cellcode) {
    /**
     * delete generic function test code cell.
     *
     */
    var generic_cell = window.get_cell_for_id(SW_UTILS_GENFUNC_CODECELL_ID);
    generic_cell.set_text(cellcode);
    window.scroll_to('DCGenFunctionUtility');
}

function select_gen_function(genid) {
    /**
     * generic function select function callback.
     *
     * Parameters:
     *  genid - gen function id
     */
    var inputs = new Array();
    inputs.push(6, genid);
    window.run_code_in_cell(window.SW_UTILS_GENFUNC_TASK_BAR_ID, window.getJSPCode(window.GEN_FUNCTION_LIB, "display_gen_function", "2," + JSON.stringify(inputs)));
    window.scroll_to('DCGenFunctionUtility');
}

// 
// ------------------------------------------------------
// Dataframe Concat Utility functions 
// ------------------------------------------------------
//
function process_concat_callback(fid) {
    /**
     * process dataframe concat callback.
     *
     * Parameters:
     *  fid - function id
     */
    switch (fid) {
        case 0:
        case 1:
            window.run_code_in_cell(window.SW_UTILS_DFCONCAT_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFCONCAT_LIB, "display_dfconcat_utility", fid));
            break;
        case 2:
        case 3:
            var formid = "";
            if (fid == 2) {
                formid = "concatinput";
            } else {
                formid = "fconcatinput";
            }
            var fparms = get_input_form_parms(formid);
            window.run_code_in_cell(window.SW_UTILS_DFCONCAT_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFCONCAT_LIB, "display_dfconcat_utility", fid + ", " + JSON.stringify(fparms)));
            break;
    }
    window.scroll_to('DCDFConcatUtility');
}

function select_concat_df(sid) {
    /**
     * process dataframe select callback.
     *
     * Parameters:
     *  sid - select id
     */

    var parms = new Array();
    if (sid == "dataframe1title")
        var seldf = $('#dataframe1title').val();
    else
        var seldf = $('#dataframe2title').val();

    var df1 = $('#dataframe1title').val();
    var df2 = $('#dataframe2title').val();
    parms.push(seldf, df1, df2);

    window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "get_select_concat_df_vals", JSON.stringify(parms)));

}

function set_concat_direction(direction) {
    /**
     * process dataframe concat direction.
     *
     * Parameters:
     *  direction - to dataframe
     */

    if (direction == "df2") {
        var dfselected = $('#dataframe2title').val();
    } else {
        var dfselected = $('#dataframe1title').val();
    }

    $('#dftoconcatto').val(dfselected);
}