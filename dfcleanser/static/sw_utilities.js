
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
    window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_LIB,"process_sw_utilities",id));
    window.scroll_to('DCListUtility');
}

function build_utility_clear_callback() {
    /**
    * data structures utility clear inputs.
    */
    window.clear_cell_output(SW_UTILS_DATASTRUCT_TASK_BAR_ID);
    window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_LIB,"process_sw_utilities","0"));
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
    if (id == 4) {iname = $("#listname").val()} 
    else {iname = $("#dictname").val()}
    window.clear_cell_output(SW_UTILS_DATASTRUCT_TASK_BAR_ID);
    window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_LIB,"process_sw_utilities",id + ", " + JSON.stringify(iname)));
}

function sw_utilities_list_add_callback() {
    /**
    * data structures utility add list.
    */
    var importVals = get_input_form_parms("buildlistparms");
    window.clear_cell_output(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID);
    window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_LIB,"process_sw_utilities",(3 + ", " + importVals)));
    window.scroll_to('DCListUtility');
}

function sw_utilities_dict_add_callback() {
    /**
    * data structures utility add dict.
    */
    var importVals = get_input_form_parms("builddictparms");
    window.clear_cell_output(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID);
    window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_LIB,"process_sw_utilities",(5 + ", " + importVals)));
    window.scroll_to('DCListUtility');
}

function select_dict(key) {
    /**
    * data structures utility select dict.
    *
    * Parameters:
    *  key - dict to display
    */
    window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_LIB,"process_sw_utilities","10, " + JSON.stringify(key)));
    window.scroll_to('DCListUtility');
}

function select_list(key) {
    /**
    * data structures utility select list.
    *
    * Parameters:
    *  key - dict to display
    */
    window.run_code_in_cell(window.SW_UTILS_DATASTRUCT_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_LIB,"process_sw_utilities","9, " + JSON.stringify(key)));
    window.scroll_to('DCListUtility');
}


// 
// ------------------------------------------------------
// Geocoding Utility functions 
// ------------------------------------------------------
//

function process_geomain_callback(fid) {
    /**
    * geocodong main taskbar callback.
    *
    * Parameters:
    *  fid - function id
    */
    switch (fid) {
        case 0:
        case 1:
        case 5:
        case 7:
        case 11:
            window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID, window.getJSPCode(window.SW_UTILS_GEOCODE_LIB,"display_geocode_utility",fid));
            window.scroll_to('DCGeocodeUtility');
            break;
        case 3:
        case 4:
            var inId = "";
            if (fid == 3) {inId = "addrconvertparmsid";} 
            else {inId = "coordconvertparmsid"; }
            var inputs = window.get_input_form_parms(inId);
            window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_GEOCODE_LIB,"display_geocode_utility", fid + "," + JSON.stringify(inputs)));
            window.scroll_to('DCGeocodeUtility');
            break;
    }
}

//
// Geocoding dhtml functions 
//
function acselcol(colid) {
    var inputId = $("#dfaddress");
    var addrtext = "";
    if (inputId.val().length > 0) {addrtext = inputId.val() + " + " + colid;} 
    else {addrtext = colid;}
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
    } 
    else {
        $('#addrconvertparmsid  :input').each(function() {
            $(this).prop('readonly', false);
            $(this).val('');
        });
    }
}
function add_df_column(colname) {
    var currentAddress = $("#dfaddress");
    var newAddress = "";
    if (currentAddress.val().length > 0) {newAddress = currentAddress.val() + " + " + colname;} 
    else {newAddress = colname;}
    currentAddress.val(newAddress);
}


function select_geocoder(gcid) {
    /**
    * select geocoder display.
    *
    * Parameters:
    *  gcid - geocoder id
    */
    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_GEOCODE_LIB,"display_geocode_utility","5, " + JSON.stringify(gcid)));
    window.scroll_to('DCGeocodeUtility');
}

function process_geocoder_callback(fid, gcid) {
    /**
    * geocoder inputs processing.
    *
    * Parameters:
    *  fid- function id
    *  gcid - geocoder id
    */
    switch (fid) {
        case 0:
        case 1:
        case 2:
            var id = ""
            switch (gcid) {
                case 0:     id = "arcgisgeocoder";  break;
                case 2:     id = "binggeocoder";    break;
                case 3:     id = "databcgeocoder";  break;
                case 4:     id = "dotusgeocoder";   break;
                case 7:     id = "googlegeocoder";  break;
                case 9:     id = "mapquestgeocoder";break;
                case 11:    id = "nomingeocoder";   break;
                case 12:    id = "yahoogeocoder";   break;
            }

            var fparms = get_input_form_parms(id);
            var inputs = [fid, gcid, fparms];
            var cmd = 0;
            if (fid == 0) cmd = 6;
            else cmd = fid;
            window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_GEOCODE_LIB,"display_geocode_utility",cmd + ", " + JSON.stringify(inputs)));
            break;
        case 3:
            var inputs = [fid,gcid];
            window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_GEOCODE_LIB,"display_geocode_utility", "6, " + JSON.stringify(inputs)));
            break;
        case 4:
            window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_GEOCODE_LIB,"display_geocode_utility","0"));
            break;
    }
    window.scroll_to('DCGeocodeUtility');
}

function process_query_callback(fid, gcid) {
    /**
    * geocoder query processing.
    *
    * Parameters:
    *  fid- function id
    *  gcid - geocoder id
    */
    switch (fid) {
        case 0:
        case 1:
        case 2:
        case 3:
        case 6:
        case 7:
            var id = ""
            switch (gcid) {
                case 0:     id = "arcgisquery";     break;
                case 2:     id = "bingquery";       break;
                case 3:     id = "databcquery";     break;
                case 4:     id = "dotusquery";      break;
                case 7:     id = "googlequery";     break;
                case 9:     id = "mapquestquery";   break;
                case 11:    id = "nominquery";      break;
                case 12:    id = "yahooquery";      break;
            }

            var cmd = fid;
            switch (fid) {
                case 0: cmd = 3;    break;
                case 1: cmd = 2;    break;
                case 2: cmd = 5;    break;
                case 3: cmd = 21;   break;
                case 6: cmd = 1;    break;
                case 7: cmd = 13;   break;
            }

            var fparms = [];
            if (fid < 2)
                fparms = get_input_form_parms(id);
            else {
                if (fid == 7)
                    fparms = get_input_form_parms(id + "DF");
            }

            if(fid == 3)
                var inputs = [0, gcid];
            else
                var inputs = [fid, gcid, fparms];
                
            window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_GEOCODE_LIB,"display_geocode_utility",cmd + ", " + JSON.stringify(inputs)));
            break;
        case 4:
            window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_GEOCODE_LIB,"display_geocode_utility", "0"));
            break;
    }
    window.scroll_to('DCGeocodeUtility');
}

function process_reverse_callback(fid, gcid) {
    /**
    * geocoder reverse processing.
    *
    * Parameters:
    *  fid- function id
    *  gcid - geocoder id
    */
    switch (fid) {
        case 0:
        case 1:
        case 2:
        case 3:
        case 8:
        case 9:
            var id = ""
            switch (gcid) {
                case 0:     id = "arcgisreverse";   break;
                case 2:     id = "bingreverse";     break;
                case 3:     id = "databcreverse";   break;
                case 4:     id = "dotusreverse";    break;
                case 7:     id = "googlereverse";   break;
                case 9:     id = "mapquestreverse"; break;
                case 11:    id = "nominreverse";    break;
                case 12:    id = "yahooreverse";    break;
            }

            var cmd = fid;
            switch (fid) {
                case 0: cmd = 4;    break;
                case 1: cmd = 12;   break;
                case 2: cmd = 5;    break;
                case 3: cmd = 2;    break;
                case 8: cmd = 2;    break;
                case 9: cmd = 14;   break;
            }

            var fparms = [];
            if (fid < 2)
                fparms = get_input_form_parms(id);
            else {
                if (fid == 9)
                    fparms = get_input_form_parms(id + "DF");
            }

            var inputs = [fid, gcid, fparms];
            window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_GEOCODE_LIB,"display_geocode_utility",cmd + ", " + JSON.stringify(inputs)));
            break;
        case 4:
            window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_GEOCODE_LIB,"display_geocode_utility","0"));
            break;
    }
    window.scroll_to('DCGeocodeUtility');
}

function process_addr_dist(fid) {
    /**
    * geocoder address processing.
    *
    * Parameters:
    *  fid- function id
    */
    switch (fid) {
        case 8:
        case 10:
            var fparms = get_input_form_parms("addrdist");
            window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_GEOCODE_LIB,"display_geocode_utility",fid + ", " + JSON.stringify(fparms)));
            break;
        case 0:
        case 5:
        case 7:
        case 9:
            window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_GEOCODE_LIB,"display_geocode_utility",fid));
            break;
    }
    window.scroll_to('DCGeocodeUtility');
}

function process_batch_geocoder(fid,geotype) {
    /**
    * geocoder bulk query processing.
    *
    * Parameters:
    *  fid- function id
    *  gcid - geocoder id
    */
    
    var fparms = get_input_form_parms("arcgisbatchgeocoder");     
    console.log("process_batch_geocoder",fid,fparms);
    var inputs = [fid, geotype, fparms];
    
    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_GEOCODE_LIB,"display_geocode_utility",("20, " + JSON.stringify(inputs))));
    window.scroll_to('DCGeocodeUtility');
}

function process_bulk_query(fid,gcid) {
    /**
    * geocoder bulk query processing.
    *
    * Parameters:
    *  fid- function id
    *  gcid - geocoder id
    */
    
    var formid = "";
    switch (gcid) {
        case 0: formid = "arcgisbatchquery";       break;
        case 7: formid = "googlebulkquery";      break;
    }
    var fparms = get_input_form_parms(formid);     
    console.log("process_bulk_query",formid,fparms);
    var inputs = [fid, gcid, 0, fparms];
    
    window.run_code_in_cell(window.SW_UTILS_GEOCODE_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_GEOCODE_LIB,"display_geocode_utility",("13, " + JSON.stringify(inputs))));
    window.scroll_to('DCGeocodeUtility');
}

// ------------------------------------------------------
// dynamic html functions 
// ------------------------------------------------------
function gb_google_add_df_column(colid){
    var addr = $("#bgqaddress");
    var addrtext = "";
    if (addr.val().length > 0) {addrtext = addr.val() + " + " + colid;} 
    else {addrtext = colid;}
    addr.val(addrtext);
}
function gb_arcgis_add_df_column(colid){
    var addr = $("#baqaddress");
    var addrtext = "";
    if (addr.val().length > 0) {addrtext = addr.val() + " + " + colid;} 
    else {addrtext = colid;}
    addr.val(addrtext);
}
function gb_select_language(lang){
    var language = $("#bgqlanguage");
    language.val(lang);
}
function gb_select_region(region){
    var reg = $("#bgqregion");
    reg.val(region);
}
function gb_select_country(region){
    var reg = $("#baqsourcecountry");
    reg.val(region);
}
function gb_select_category(category){
    var cat = $("#baqcategory");
    cat.val(category);
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
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB,"display_dfsubset_utility",fid));
            window.scroll_to('DCDFSubsetUtility');
            break;
        case 2:
        case 3:
        case 4:
            if (fid == 3) {var inputs = window.get_input_form_parms("dcdfsubset");}
            else{
                if (fid == 2) {var inputs = window.get_input_form_parms("dcdfsubset");}
                else{
                    if (fid == 4) {var inputs = window.get_input_form_parms("dcdfsubsetsearch");}
                    else {var inputs = new Array();}
                }
            }
            window.run_code_in_cell(window.SW_UTILS_DFSUBSET_TASK_BAR_ID,window.getJSPCode(window.SW_UTILS_DFSUBSET_LIB,"display_dfsubset_utility",(fid + ", " + inputs)));
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
            window.run_code_in_cell(window.WORKING_CELL_ID,window.getJSPCode(window.COMMON_LIB,"get_dfsubset_vals",JSON.stringify(parms)));
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

            newcselectstring = newcselectstring + newcondition + " ) ";
            $('#gsselectstring').val(newcselectstring);
            $('#gscolname').val("");
            $('#gscoloper').val("");
            $('#gscolvalue').val("");
            $('#gscolandor').val("");

            var parms = new Array();
            parms.push(1);
            parms.push("");
            window.run_code_in_cell(window.WORKING_CELL_ID,window.getJSPCode(window.COMMON_LIB,"get_dfsubset_vals",JSON.stringify(parms)));
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
    window.run_code_in_cell(window.WORKING_CELL_ID,window.getJSPCode(window.COMMON_LIB,"get_dfsubset_vals",JSON.stringify(parms)));
}

//
// DF Subset dhtml functions 
//
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
// Generic Functions Utility functions 
// ------------------------------------------------------
//
function genfunction_task_bar_callback(fid) {
    /**
    * generic function main taskbar callback.
    *
    * Parameters:
    *  fid - function id
    */
    window.run_code_in_cell(window.SW_UTILS_GENFUNC_TASK_BAR_ID,window.getJSPCode(window.GEN_FUNCTION_LIB,"display_gen_function",fid));
    window.scroll_to('DCGenFunctionUtility');
}

function generic_function_callback(fid) {
    /**
    * generic function process command callback.
    *
    * Parameters:
    *  fid - function id
    */

    var inputs = new Array();
    switch (fid) {
        case 0:
            inputs.push(0)
            window.delete_output_cell(window.SW_UTILS_GENFUNC_CODECELL_ID);
            window.run_code_in_cell(window.SW_UTILS_GENFUNC_TASK_BAR_ID,window.getJSPCode(window.GEN_FUNCTION_LIB,"display_gen_function","2," + JSON.stringify(inputs)));

            IPython.notebook.insert_cell_below('code');
            var cell = IPython.notebook.select_next().get_selected_cell();

            var code = "# generic function" + NEW_LINE +
                '# function title' + NEW_LINE +
                "from dfcleanser.common.cfg import get_dc_dataframe" + NEW_LINE +
                "df = get_dc_dataframe()" + NEW_LINE + NEW_LINE;

            window.run_code(cell, code);
            break;
        case 1:
            var generic_cell = window.get_cell_for_id(SW_UTILS_GENFUNC_CODECELL_ID);

            if (generic_cell != null) {
                var generic_code = generic_cell.get_text();
                var c_line_start = generic_code.indexOf("#");
                var c_code = generic_code.slice(c_line_start + 1, generic_code.length)
                c_line_start = c_code.indexOf("#");
                c_code = c_code.slice(c_line_start, generic_code.length)
                var c_line_end = c_code.indexOf("\n");
                c_code = c_code.slice(2, c_line_end);
                var title = $('#gttitle');
                title.val(c_code);
                var code = $('#gtcode');
                code.val(generic_code);
            }
            break;
        case 2:
        case 3:
        case 4:
            var fparms = get_input_form_parms("genfuncform");
            if ((fid == 2) || (fid == 4)) {
                var gfuncfound = fparms.search("# generic function");
                if (fparms.indexOf("# generic function") != -1) {
                    fparms = fparms.replace("# generic function", "");
                    var tfound = fparms.search("#");
                    fparms = fparms.slice(0, (tfound - 2)) + fparms.slice(tfound, fparms.length);
                }
            }

            inputs.push(fid, fparms);
            window.delete_output_cell(window.SW_UTILS_GENFUNC_CODECELL_ID);
            window.run_code_in_cell(window.SW_UTILS_GENFUNC_TASK_BAR_ID,window.getJSPCode(window.GEN_FUNCTION_LIB,"display_gen_function","2," + JSON.stringify(inputs)));
            break;
        case 5:
            var title = $('#gttitle');
            title.val("");

            var code = $('#gtcode');
            var newcode = "# generic function" + NEW_LINE +
                '# function title' + NEW_LINE +
                "from dfcleanser.common.cfg import get_dc_dataframe" + NEW_LINE +
                "df = get_dc_dataframe()" + NEW_LINE + NEW_LINE;
            code.val(newcode);

            window.delete_output_cell(window.DC_GEN_FUNCTION_ID);
            break;

        case 6:
            window.delete_output_cell(window.SW_UTILS_GENFUNC_CODECELL_ID);
            window.run_code_in_cell(window.SW_UTILS_GENFUNC_TASK_BAR_ID,window.getJSPCode(window.GEN_FUNCTION_LIB,"display_gen_function","0"));
            break;
    }
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
    inputs.push(1, genid);
    window.run_code_in_cell(window.SW_UTILS_GENFUNC_TASK_BAR_ID,window.getJSPCode(window.GEN_FUNCTION_LIB,"display_gen_function","2," + JSON.stringify(inputs)));
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

