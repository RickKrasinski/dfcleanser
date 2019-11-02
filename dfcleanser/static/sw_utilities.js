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

function select_dict(formid) {
    /**
     * data structures utility select dict.
     *
     * Parameters:
     *  formid - dict form
     */

    var inputs = new Array();
    var dictname = $("#dictname :selected").text();
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
    var listname = $("#listname :selected").text();
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

    console.log("get_subset_callback", fid);
    switch (fid) {
        case 0:
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", fid));
            window.scroll_to('DCDFSubsetUtility');
            break;
        case 1:
            var inputs = new Array();
            var inputParms = window.get_input_form_parms("datasubsetdf");
            inputs.push(inputParms);
            console.log("get_subset_callback", inputs);
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", "1" + "," + JSON.stringify(inputs)));
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
            $('#gsfilterselectstring').val("");
            //$('#gsselectstring').val("");
            var parms = new Array();
            parms.push(1);
            parms.push("");
            window.run_code_in_cell(window.WORKING_CELL_ID, window.getJSPCode(window.COMMON_LIB, "get_dfsubset_vals", JSON.stringify(parms)));
            break;

        case 7:

            var newcselectstring = $('#gsfilterselectstring').val();

            var parms = new Array();
            parms.push(newcselectstring);
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", fid + ", " + JSON.stringify(parms)));
            window.scroll_to('DCDFSubsetUtility');
            break;

        case 9:
            var inputs = window.get_input_form_parms("dcdfsubsetsearch");
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB, "display_dfsubset_utility", (fid + ", " + inputs)));
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

    if (window.debug_flag)
        console.log("set_filter_colname", colname);

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

    console.log("iscolnamedefined", filtersstring);

    if ((filtersstring.indexOf('df[') > -1))
        return (true);
    else
        return (false);
}

function isvaluedefined() {

    var filtersstring = getlastclause();

    console.log("isvaluedefined", filtersstring);

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
        //console.log("is value defined", filtersstring.charAt((operatoroffset + operatorlength + 1)));
        //console.log("is value defined", filtersstring.charAt((operatoroffset + operatorlength + 2)));
        if (filtersstring.charAt((operatoroffset + operatorlength + 1)) != ")") {
            return (true);
        }
    }

    return (false);

}

function isoperatordefined() {

    var filtersstring = getlastclause();

    console.log("isoperatordefined", filtersstring);

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

    console.log("getlastclause", filtersstring.val());

    console.log("getlastclause", filtersstring.val().indexOf('or'));
    console.log("getlastclause", filtersstring.val().indexOf('and'));


    if ((filtersstring.val().indexOf('or') < 0) &&
        (filtersstring.val().indexOf('and') < 0))
        return (filtersstring.val());
    else {

        var last_clause = filtersstring.val();

        console.log("getlastclause last_clause", last_clause);


        var max_loop = 10;
        var loop_count = 0;

        while ((loop_count < max_loop) &&
            ((last_clause.indexOf("or") > -1) ||
                (last_clause.indexOf("and") > -1))) {

            console.log("getlastclause loop", last_clause);

            loop_count = loop_count + 1;

            if (last_clause.indexOf("or") > -1)
                last_clause = last_clause.slice(last_clause.indexOf("or") + 3);
            else {
                last_clause = last_clause.slice(last_clause.indexOf("and") + 4);
                console.log("getlastclause and", last_clause);
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

            console.log("newfstring", newfstring, endisin);
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

            console.log("newfstring", newfstring, endisin);
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
            console.log(newfstring);
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

    console.log("generic_function_callback", fid);

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
    //var inputs = new Array();
    //inputs.push(6, genid);
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

            //inputs.push(datasetcbs);

            /*
            var subdatacbs = new Array();
            var subdatacount = [16, 12, 14, 17, 19, 9, 5, 5, 35, 11];

            var subdataID = $('#SubdataHeading').text();

            console.log("subdataID", subdataID);

            var subid = -1

            for (var i = 0; i < datasetids.length; i++) {
                if (subdataID == datasetids[i])
                    subid = i;
            }

            if (subid > -1) {

                for (var j = 1; j < subdatacount[subid] + 1; j++) {

                    ccb = "#CS" + datasetids[subid] + j.toString();
                    console.log("ccb", ccb)

                    var currentcb = $("#CS" + datasetids[subid] + j.toString()).prop("checked");

                    if (currentcb == true)
                        subdatacbs.push("True");
                    else
                        subdatacbs.push("False");
                }
            }

            inputs.push(subdatacbs);
            */

            window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", ("4, " + JSON.stringify(inputs))));
            break;

        case 24:
        case 25:

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

            var selected_values = $('#subdatacolnames').val();
            window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", (fid.toString() + " ," + JSON.stringify(selected_values))));
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

    var inputs = new Array();
    inputs.push(datasetid);
    inputs.push(subdataid);

    window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", ("13, " + JSON.stringify(inputs))));
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

    var inputs = new Array();
    inputs.push(datasetid);
    inputs.push(subdataid);

    window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", ("27, " + JSON.stringify(inputs))));
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

    var inputs = new Array();
    inputs.push(datasetid);
    inputs.push(subdataid);

    window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", ("22, " + JSON.stringify(inputs))));
    window.scroll_to('DCCensusUtility');
}

function get_configure_dataset_details(datasetid) {
    /**
     * census process command callback.
     *
     * Parameters:
     *  datasetid - dataset id
     */

    window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", ("21, " + JSON.stringify(datasetid))));
    window.scroll_to('DCCensusUtility');
}

function get_df_census_dataset_details(dtid, datasetid) {
    /**
     * census process command callback.
     *
     * Parameters:
     *  datasetid - dataset id
     */
    var inputs = new Array();
    inputs.push(dtid);
    inputs.push(datasetid);

    window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", ("7, " + JSON.stringify(inputs))));
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

    console.log("scroll_census_cols", inputs);

    window.run_code_in_cell(window.SW_UTILS_CENSUS_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_CENSUS_LIB, "display_census_utility", ("15, " + JSON.stringify(inputs))));
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

}