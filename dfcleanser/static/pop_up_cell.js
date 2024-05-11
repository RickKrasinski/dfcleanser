define([
    'require',
    'jquery',
    'base/js/namespace',
    'base/js/events',
    'base/js/utils',
    'notebook/js/codecell',
    'notebook/js/outputarea',
], function(
    requirejs,
    $,
    Jupyter,
    events,
    utils,
    codecell,
    outputarea
) {
    "use strict";

    const DEBUG_POP_UP = false

    var CodeCell = codecell.CodeCell;

    var popup_height = 300;

    window.set_pop_up_height = function(height) {
        if (DEBUG_POP_UP)
            console.log("set_pop_up_height", height);

        popup_height = height;
    }

    var PopUp = null;

    var PopUpCodeCell = function(nb) {
        var popupcodecell = this;
        this.notebook = nb;
        this.kernel = nb.kernel;
        this.km = nb.keyboard_manager;
        this.collapsed = true;

        // setup the reset and minimize cell buttons
        this.element = $("<div id='dfcleanser-PopUpCodeCell'>");

        this.close_button = $("<i>").addClass("fa fa-window-close PopUpCodeCell-btn PopUpCodeCell-close");

        this.element.append(this.close_button);

        this.close_button.click(function() {

            var code = "from IPython.display import clear_output" + NEW_LINE;
            code = code + "clear_output()" + NEW_LINE;
            code = code + "from dfcleanser.common.common_utils import run_jscript" + NEW_LINE;
            code = code + "run_jscript('delete_popupcodecell('close_button_click');',' ');" + NEW_LINE;

            run_code_in_popupcodecell(code);
            popupcodecell.collapse();

        });

        // create the pop up working cell
        var cell = this.cell = new CodeCell(nb.kernel, {
            events: nb.events,
            config: nb.config,
            keyboard_manager: nb.keyboard_manager,
            notebook: nb,
            tooltip: nb.tooltip,
        });

        // add the dfcleanser cellid metadata
        var dfcellDict = { "dfc_cellid": "dfcPopUpCell" };
        var dfcleanserDict = { "dfcleanser_metadata": dfcellDict };
        var newcellDict = { "dfcleanser_metadata": dfcellDict, "trusted": true };
        cell.metadata = newcellDict;

        // do cell housekeeping
        cell.set_input_prompt();
        this.element.append($("<div/>").addClass('cell-wrapper').append(this.cell.element));
        cell.render();
        cell.refresh();
        this.collapse();

        // add me to the notebook
        $("body").append(this.element);
    };

    PopUpCodeCell.prototype.run_code_in_popup = function(code) {

        if (DEBUG_POP_UP)
            console.log("run_code_in_popup\n", code);

        this.cell.set_text(code);
        this.cell.execute();

        if (DEBUG_POP_UP)
            console.log("run_code_in_popup end");
    }

    PopUpCodeCell.prototype.clear_popup = function() {
        this.cell.set_text("");
        this.cell.execute();
    }

    PopUpCodeCell.prototype.run_popup = function() {
        this.cell.execute();
    }

    PopUpCodeCell.prototype.toggle = function() {
        if (this.collapsed) {
            this.expand();
        } else {
            this.collapse();
        }
        return false;
    };

    PopUpCodeCell.prototype.expand = function() {
        this.collapsed = false;
        var site_height = 300; /*$("#site").height();*/

        if (DEBUG_POP_UP)
            console.log("popup_height", popup_height);

        this.element.animate({
            height: popup_height,
            width: 840,
        }, 200);
        this.close_button.show();
        this.cell.element.show();
        this.cell.focus_editor();
        $("#notebook-container").css('margin-left', 0);
    };

    PopUpCodeCell.prototype.collapse = function() {
        this.collapsed = true;
        $("#notebook-container").css('margin-left', 'auto');
        this.element.animate({
            height: 0,
            width: 840,
            top: 20,
        }, 100);
        this.close_button.hide();

        this.cell.element.hide();
    };

    //
    // ---------------------------------------------------
    // PopUpCodeCell helper functions
    // ---------------------------------------------------
    //

    window.setup_popupcodecell = function() {
        if (DEBUG_POP_UP)
            console.log(log_prefix + "[Load]\n" + "     dfcleanser popupcodecell created");
        PopUp = new PopUpCodeCell(Jupyter.notebook);
    }

    window.get_popupcodecell = function() {
        return (PopUp.cell);
    }

    window.delete_popupcodecell = function(id) {
        if (DEBUG_POP_UP)
            console.log(log_prefix + "\n" + "     delete_popupcodecell", id);

        if (PopUp != null)
            PopUp.close_button.click();

        PopUp = null;
    }

    window.is_pop_up_visible = function() {
        if (PopUp.collapsed)
            return (false);
        else
            return (true);
    }

    window.toggle_popupcodecell = function() {
        if (DEBUG_POP_UP)
            console.log(log_prefix + "\n" + "     toggle_popupcodecell");
        PopUp.toggle();
    }

    window.run_code_in_popupcodecell = function(code) {
        if (DEBUG_POP_UP)
            console.log(log_prefix + "\n" + "     run_code_in_popupcodecell", code);

        if (PopUp.collapsed == false)
            PopUp.run_code_in_popup(code);
        else {
            PopUp.expand();
            PopUp.run_code_in_popup(code);
        }
    }

    window.reset_pop_up = function() {
        process_pop_up_cmd(6);
    }

    window.clear_pop_up = function() {
        process_pop_up_cmd(6);
    }

    window.shut_off_autoscroll = function() {
        if (DEBUG_POP_UP)
            console.log(log_prefix + "\n" + "     shut_off_autoscroll");

        outputarea.OutputArea.auto_scroll_threshold = -1;
    }


});