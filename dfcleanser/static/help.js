//
//
// ---------------------------------------------------
// common help functions
// ---------------------------------------------------
//
//

window.gethelpinputid = function(helpid) {

    var inputid = null;

    switch (helpid) {
        case 100:
            inputid = 'SystemHelphelpbackid';
            break;
        case 200:
            inputid = 'ImportHelphelpbackid';
            break;
        case 300:
            inputid = 'InspectionHelphelpbackid';
            break;
        case 400:
            inputid = 'CleansingHelphelpbackid';
            break;
        case 500:
            inputid = 'TransformHelphelpbackid';
            break;
        case 600:
            inputid = 'ExportHelphelpbackid';
            break;
        case 700:
            inputid = 'ScriptingHelphelpbackid';
            break;
        case 800:
            inputid = 'DCListUtilityHelphelpbackid';
            break;
        case 900:
            inputid = 'DCGenFunctionUtilityHelphelpbackid';
            break;
        case 1000:
            inputid = 'DCGeocodeUtilityHelphelpbackid';
            break;
        case 1100:
            inputid = 'DCDFSubsetUtilityHelphelpbackid';
            break;
        case 1200:
            inputid = 'DCDFSubsetUtilityHelphelpbackid';
            break;
        default:
            inputid = '';
            break;
    }

    if (inputid != null) {
        var inputval = $('#' + inputid);
        if (inputval != null) { return (inputval.val()); } else { return (null); }
    } else { return (null); }
};

window.displayhelp = function(helpid) {

    var help_id = parseInt(helpid, 10);

    if ((help_id > 99) & (help_id < 1220)) {
        var remainder = help_id % 100;

        if (remainder == 0) {
            if (gethelpinputid(helpid) == null) {
                var url = "https://rickkrasinski.github.io/dfcleanser/html/help/" + helpid + ".html";
                window.open(url);
            } else { self.close(); }
        } else {
            var url = "https://rickkrasinski.github.io/dfcleanser/html/help/" + helpid + ".html";
            window.open(url, "_self");
        }
    }
};