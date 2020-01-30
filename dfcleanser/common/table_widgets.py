"""
# dfc_common_table_widgets 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sept 13 22:29:22 2017

@author: Rick
"""
import sys
this = sys.modules[__name__]


def addattribute(name,value) :
    """
    * -------------------------------------------------------------------------- 
    * function : add attribute
    * 
    * parms :
    *   namw        -   attribute name
    *   value       -   attribute value 
    *
    * returns : 
    *  html attribute
    * --------------------------------------------------------
    """
    attribute = ""
    attribute = attribute + " " + name + "=" + '"' + str(value) + '"'
    return(attribute)


def addstyleattribute(name,value) :
    """
    * -------------------------------------------------------------------------- 
    * function : add style attribute
    * 
    * parms :
    *   namw        -   style attribute name
    *   value       -   style attribute value 
    *
    * returns : 
    *  html style attribute
    * --------------------------------------------------------
    """
    
    styleattribute = ""
    styleattribute = styleattribute + " " + name + ":" + value + "; "
    return(styleattribute)


def strip_leading_blanks(instr) :
    """
    * -------------------------------------------------------------------------- 
    * function : stripleading blanks
    * 
    * parms :
    *   instr  - input string
    *
    * returns : 
    *  stripped string
    * --------------------------------------------------------
    """
    
    outstr = instr.replace("&nbsp;","")
    return(outstr)


new_line =   """
"""

debugTables     =   False

maxRowElement   =   14


"""
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
* Common Table defs 
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
"""
SCROLL_DOWN         =   0
SCROLL_UP           =   1

SCROLL_RIGHT        =   2
SCROLL_LEFT         =   3

SCROLL_NONE         =   -1

SIMPLE              =   -1

ROW_MAJOR           =   0
COLUMN_MAJOR        =   1
ROW_COL_MAJOR       =   2



"""
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
* dcTable Repository elements 
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
"""

"""
* -----------------------------------------------------------------------*
* dcTable Repository helper functions
* -----------------------------------------------------------------------*
"""
def get_table_value(tableid) :
    return(dc_table_config.get_table(tableid))
    
def set_table_value(tableid, table) :
    dc_table_config.set_table(tableid,table)
        
def drop_table_value(tableid) :
    dc_table_config.drop_table(tableid)

def drop_owner_tables(ownerid) :
    dc_table_config.drop_owner_table(ownerid)
    
def dump_table_values() :
    dc_table_config.dump_table_cfg_data()


"""
* -----------------------------------------------------------------------*
* dcTable Repository class 
* -----------------------------------------------------------------------*
*   class to store table ids that can be deleted when appropriate and
*   looked up and redisplayed when necessary
* -----------------------------------------------------------------------*
"""
class dcTable_cfg :

    # full constructor
    def __init__(self) :
        
        # instance variables

        # minimum init attributes
        self.dc_table_data   =   {}

    def set_table(self,tableidParm,tableParm) :
        self.dc_table_data.update({tableidParm: tableParm})
        
    def get_table(self,tableidParm) :
        try :
            return(self.dc_table_data.get(tableidParm))
        except :
            print("[error set dc_table_data cfg value]",tableidParm,str(sys.exc_info()[0]))
            
        
    def drop_table(self,tableidParm) :
        try :
            self.dc_table_data.pop(tableidParm,None)
        except :
            print("[error drop dc_table_data cfg value]",tableidParm,self.dc_table_data,str(sys.exc_info()[0]))
        
    def drop_owner_table(self,owneridParm) :
        keys = list(self.dc_table_data.keys())
        for i in range(len(keys)) :
            if(self.dc_table_data.get(keys[i]).get_owner() == owneridParm) :
                self.drop_table(self.dc_table_data.get(keys[i]).get_tableid())
        
    def dump_table_cfg_data(self) :
        print("Table Configuration Data")
        print(self.dc_table_data)

"""
* -----------------------------------------------------------------------*
* dcTable repository data store
* -----------------------------------------------------------------------*
"""
dc_table_config    =   dcTable_cfg()


"""
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
* dcTable elements 
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
"""

"""
* -----------------------------------------------------------------------*
* Common dcTable html elements
* -----------------------------------------------------------------------*
"""
table_form_start = """
<div class='dc-form-div'"""
table_form_end = """</div>
"""

table_container_start = """
<div class='container dc-table-container'"""

table_container_middle = """
    <div class="panel panel-primary" """
        
table_container_end = """
    </div>
"""
table_container_end1 = """</div>
"""

table_nd_container_end = """
        </div>
"""
table_nd_container_end1 = """
    </div>
"""

table_header_start = """
            <div class="panel-heading dc-table-panel-heading">
"""
small_table_header_start = """
            <div class="panel-heading clearfix dc-small-table-panel-heading" style="height:38px; font-size:11px;" """
small_table_with_arrows_header_start = """
            <div class="panel-heading clearfix dc-small-table-panel-heading" style="height:48px; font-size:11px;" """
small_table_no_header_start = """
            <div class="panel-heading clearfix dc-small-table-noheader-panel-heading" style=" margin-bottom:0px; background-color:white;" """

table_header_end = """            </div>
            <div>"""

table_input_group_start = """                <div class="input-group">
"""
table_input_group_end = """                </div>
"""

table_title_div_start = """                    <div class="input-group-btn">"""
table_title_div_end   = """                    </div>
"""

table_title_short_div_start = """                    <div class="input-group-btn" >                
"""
table_title_short_div_end   = """                    </div>
"""

table_title_div_start = """                    <div class='input-group-btn'>
"""
table_title_div_end = """                    </div>
"""

table_title_start = """                      <p class="dc-table-title pull-left" """
table_title_end = """</p>
"""

table_more_div_start = """                    <div class="input-group-btn" """
table_more_div_start1 = """ style="padding-right:0px; text-align:right">
"""
table_more_short_div_start1 = """ style="padding-right:25px; text-align:right;">
"""

table_short_more_div_start = """                    <div class="input-group-btn" style="padding-right:0px; padding-left:2%;" >
"""

table_more_div_end = """                    </div>
"""

table_next_start = """                        <button class="btn btn-primary" """
search_table_next_start = """                        <button class="btn btn-primary" """
table_next_end   = """>
                            <img src='https://rickkrasinski.github.io/dfcleanser/graphics/rightarrow.png' """
table_next_final_end   = """ height="20px" width="20px"></img>
                        </button>
"""

table_prev_start = """                        <button class="btn btn-primary" """
search_table_prev_start = """                        <button class="btn btn-primary" id="morePrev" """
table_prev_end   = """>
                            <img src='https://rickkrasinski.github.io/dfcleanser/graphics/leftarrow.png' """
table_prev_final_end   = """ height="20px" width="20px"></img>
                        </button>
"""

table_down_start = """                        <button class="btn btn-primary" """
search_table_down_start = """                        <button class="btn btn-primary" """
table_down_end   = """>
                            <img src='https://rickkrasinski.github.io/dfcleanser/graphics/downarrow.png' """
table_down_final_end   = """ height="20px" width="20px"></img>
                        </button>
"""

table_up_start = """                        <button class="btn btn-primary" """
search_up_down_start = """                        <button class="btn btn-primary" """
table_up_end   = """>
                            <img src='https://rickkrasinski.github.io/dfcleanser/graphics/uparrow.png' """
table_up_final_end   = """ height="20px" width="20px"></img>
                        </button>
"""

table_short_next_start = """                        <button class="btn btn-primary" """
table_short_next_end   = """>+</button>
"""

table_short_prev_start        = """                        <button class="btn btn-primary" """
table_short_prev_end          = """>-</button>
"""

table_short_button_end = """                        </button>
"""

table_note_start = """        <div class="table-note">
            <p> """
table_note_end   = """        </div>"""                     

table_note_color_start = """<span style='background-color:"""
              
table_start = """
        <div>
             <table class="table dc-table" style="border:0px;" """
table_start11 = """
        <div>
             <table class="table dc-table11" """
table_start12 = """
        <div>
             <table class="table dc-table12" align="center" """
table_start13 = """
        <div>
             <table class="table dc-table13" """
             
table_end = """
             </table>
        </div>"""

table_head_start = """                <thead>
"""
table_head_end = """
                </thead>"""

table_head_row_start = """                    <tr  class="dcrowhead" """
table_color_head_row_start = """                    <tr  class="dcrowhead" """

table_head_row_end = """                    </tr>"""

table_body_start = """
                <tbody>
"""
table_body_end = """                </tbody>"""

table_body_row_start = """                    <tr class="dc-describe-table-body-row">
"""
table_body_row_start12 = """                    <tr class="dc-describe-table-body-row12">
"""

table_body_row_href_start = """                    <tr class="dc-describe-table-body-row ">
"""

table_body_row_end = """
                    </tr>
"""

element_close = ">"

col_cb_div_start = """                            <div class="btn-grp">"""
col_cb_div_end = """
                            </div>"""

col_cb_input_start = """                                <input type="checkbox" style="height:20px;" """
col_cb_input_end = """ checked ></input>"""

col_cb_td_end = """                        </td>"""

table_button_div_start = """                              <div class="input-group-btn dc-table-input-group-btn">
"""
table_button_div_end   = """                              </div>
                        </td>"""

table_button_start = """                                 <button class="btn btn-primary dc-table-button" """
table_button_end   = """</button>
"""


"""
* -----------------------------------------------------------------------*
* Table title panel row html
* -----------------------------------------------------------------------*
"""

plain_title_row = """
        <div style="margin-bottom: -20px;">
            <table class="table dc-table" id="XXXXHeaderTable">
                <tbody>
                    <tr style="height:XXXXheight; font-family: Arial; font-weight:bold; color:white; background-color:#3281B8;">
                        <td class="dccolleft" style="font-size:XXXXfont-size;">XXXXTitle</td>
                    </tr>
                </tbody>
            </table>
        </div>
"""


scroll_button = """                                <button class="btn btn-primary" OnClick="XXXXScrollCallback">
                                    <img src='https://rickkrasinski.github.io/dfcleanser/graphics/XXXXimage.png' id="XXXXimageId" height="XXXXArrowSize" width="XXXXArrowSize" style="float:right"></img>
                                </button>
"""

scroll_col_start = """
                        <td class="dccolright" >
                            <div class="input-group-btn" style="text-align:right">
"""

scroll_col_end = """                            </div>
                        </td>"""


scroll_title_row = """
        <div style="margin-bottom: -20px;">
            <table class="table dc-table" id="XXXXHeaderTable" style="background-color:#3281B8;">
                <tbody style="background-color:#3281B8;">
                    <tr style="height:XXXXheight; font-family: Arial; font-weight:bold; color:white; background-color:#3281B8;">
                        <td class="dccolleft" width="xxxxTitleWidth%" style="font-size:XXXXfont-size;">XXXXTitle</td>
"""
                            
scroll_title_row_end = """
                    </tr>
                </tbody>
            </table>
        </div>
"""


search_col = """                        <td class="dccolright" width="xxxxInputWidth%">
                            <div class="input-group-btn">
                                <input type="text" class='form-control dc-form-search-more-input' size="14" style=' height:30px;  width:120px; ' id="XXXXsid" placeholder="XXXXtextid" </input>
                            </div>
                        </td>

                        <td class="dccolleft" width="xxxxIconWidth%" >
                            <div class="input-group-btn" style="text-align:left">
                                <button class='btn btn-primary' title="Get Row" OnClick="XXXXonclick">
                                    <i class='glyphicon glyphicon-search' id="dcdisrowsearchglyph" style="float:left"></i>
                                </button>
                            </div>
                        </td>
"""


"""
* -----------------------------------------------------------------------*
*    basic dcTable variants 
* -----------------------------------------------------------------------*
"""

        
"""
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
*    row major table methods
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
"""

def get_row_major_table(table,direction,displayTable=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : A row_major_table is a single table that displays a subset of rows at a time
    * 
    * parms :
    *   table           -   dcTable object
    *   direction       -   direction to scroll in 
    *   displayTable    -   display the html flag  
    *
    * returns : 
    *  html table
    * --------------------------------------------------------
    """

    if(not(displayTable)) :
        
        if(direction == SCROLL_UP) :
            numinlasttable = table.get_lastrowdisplayed() % table.get_rowspertable()
            if(numinlasttable > 0) :
                rowstart = table.get_lastrowdisplayed() - (numinlasttable+table.get_rowspertable())
            else :
                rowstart = table.get_lastrowdisplayed() - (2*table.get_rowspertable())
                
            if(rowstart < 0) :
                rowstart = -1
            
            table.set_lastrowdisplayed(rowstart)
        else :
            if( table.get_lastrowdisplayed() == len(table.get_rowList()) ) :
                table.set_lastrowdisplayed(-1)    

        table_HTML = table.get_html(False)

        return(table_HTML)
        
    else :
        table.display_table() 
        

"""
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
*    column major table methods
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
"""

"""
* -----------------------------------------------------------------------*
*    column major refresh styles methods
* -----------------------------------------------------------------------*
"""
def refresh_dfschema_buttons() :
    """
    * -------------------------------------------------------------------------- 
    * function : refresh df_schema table css
    * 
    * parms :
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """

    from dfcleanser.common.common_utils import run_jscript
    
    for j in range(2) :
        
        if(j==0)    :   colid    =   "dtcol"
        else        :   colid    =   "cccol"
        
        for i in range(7) :
    
            change_table_js = '$("#' + colid + str(i) + '").css("background-color","#67a1f3");'
            run_jscript(change_table_js,"fail scroll_table parms : "+ '#dfschemacontainer')
                    
            change_table_js = '$("#' + colid + str(i) + '").css("font-size","10px");'
            run_jscript(change_table_js,"fail scroll_table parms : "+ '#dfschemacontainer')
                    
            change_table_js = '$("#' + colid + str(i) + '").css("height","50px");'
            run_jscript(change_table_js,"fail scroll_table parms : "+ '#dfschemacontainer')

            change_table_js = '$("#' + colid + str(i) + '").css("color","white");'
            run_jscript(change_table_js,"fail scroll_table parms : "+ '#dfschemacontainer')

            change_table_js = '$("#' + colid + str(i) + '").css("width","90px");'
            run_jscript(change_table_js,"fail scroll_table parms : "+ '#dfschemacontainer')
            
            change_table_js = '$("#' + colid + str(i) + '").css("margin-left","15px");'
            run_jscript(change_table_js,"fail scroll_table parms : "+ '#dfschemacontainer')


def refresh_chknum_buttons() :
    """
    * -------------------------------------------------------------------------- 
    * function : refresh df_schema table css
    * 
    * parms :
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """

    from dfcleanser.common.common_utils import run_jscript
    
    for j in range(2) :
        
        if(j==0)    :   colid    =   "cancol"
        else        :   colid    =   "cncol"
        
        for i in range(7) :
    
            change_table_js = '$("#' + colid + str(i) + '").css("background-color","#67a1f3");'
            run_jscript(change_table_js,"fail scroll_table parms : "+ '#dfschemacontainer')
                    
            change_table_js = '$("#' + colid + str(i) + '").css("font-size","10px");'
            run_jscript(change_table_js,"fail scroll_table parms : "+ '#dfschemacontainer')
                    
            change_table_js = '$("#' + colid + str(i) + '").css("height","50px");'
            run_jscript(change_table_js,"fail scroll_table parms : "+ '#dfschemacontainer')

            change_table_js = '$("#' + colid + str(i) + '").css("color","white");'
            run_jscript(change_table_js,"fail scroll_table parms : "+ '#dfschemacontainer')

            change_table_js = '$("#' + colid + str(i) + '").css("width","90px");'
            run_jscript(change_table_js,"fail scroll_table parms : "+ '#dfschemacontainer')
            
            if(j == 0) :
                change_table_js = '$("#' + colid + str(i) + '").css("margin-left","15px");'
            else :
                change_table_js = '$("#' + colid + str(i) + '").css("margin-left","11px");'
                
            run_jscript(change_table_js,"fail scroll_table parms : "+ '#dfschemacontainer')


"""
* -----------------------------------------------------------------------*
*    common column major table methods
* -----------------------------------------------------------------------*
"""

def set_col_major_table_scroll(table,direction) :
    """
    * -------------------------------------------------------------------------- 
    * function : set the column major scroll values
    * 
    * parms :
    *   table           -   dcTable object
    *   direction       -   direction left or right
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """

    if( not(direction is None) ) :
        if(direction == SCROLL_RIGHT) :
            if((table.get_lastcoldisplayed() + 1) >= table.get_maxcolumns()) :
                table.set_lastcoldisplayed(0)
        else :
            
            if( (table.get_tableid() == "dcgendfdesc") or (table.get_tableid() == "dcnngendfdesc") ):
                
                from dfcleanser.common.common_utils import is_numeric_col
                import dfcleanser.common.cfg as cfg
                
                start_col   =   0
                nums_found  =   0
                
                df          =   cfg.get_current_chapter_df(cfg.DataCleansing_ID)
                df_cols     =   df.columns.tolist()

                print("set_col_major_table_scroll ",table.get_lastcoldisplayed())
                
                for i in range(table.get_lastcoldisplayed(),-1,-1) :
                    
                    print("set_col_major_table_scroll : ",i,nums_found)
                    
                    
                    if(nums_found < (2 * table.get_colsperrow())) :
                        
                        col_found   =   False
                        
                        if(table.get_tableid() == "dcgendfdesc") :
                            if(is_numeric_col(df,df_cols[i-1])) :  
                                col_found   =   True
                        else :
                            if( not(is_numeric_col(df,df_cols[i-1]))) :  
                                col_found   =   True
                        
                        if(col_found) :
                            
                            nums_found  =   nums_found + 1
                            if(nums_found == (2 * table.get_colsperrow())) :
                                start_col   =   i
                                #print("    start_col set ",i,nums_found,start_col)
                                break;
                
            else :
                start_col   =   table.get_lastcoldisplayed()-(table.get_colsperrow())
                if(start_col < 0) :
                    start_col   =   0
            
            table.set_lastcoldisplayed(start_col)
            
    else :
        
        start_col   =   table.get_lastcoldisplayed()-(table.get_colsperrow())
        
        if(start_col < 0) :
            start_col   =   0
                
        table.set_lastcoldisplayed(start_col)


def update_col_major_html(table,table_html) :
    """
    * -------------------------------------------------------------------------- 
    * function : scroll a col majot table
    * 
    * parms :
    *   table           -   dcTable object
    *   table_html      -   table html
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """
    
    start_html      =   table_html.find('<div class="panel panel-primary"  style=border:0px;>')
    end_html        =   len(table_html) - (len("</div>") + 1)
    col_major_html  =   table_html[start_html:end_html]
        
    from dfcleanser.common.common_utils import patch_html
    new_table_html = patch_html(col_major_html)
        
    change_table_js = "$("
    change_table_js = change_table_js + "'#" + table.get_tableid() + "container').html('"
    change_table_js = change_table_js + new_table_html + "');"
        
    #print(new_table_html)
            
    from dfcleanser.common.common_utils import run_jscript
    run_jscript(change_table_js,"fail scroll_table : " + table.get_tableid())
        
    from dfcleanser.common.common_utils import refresh_scroll_buttons
    refresh_scroll_buttons(table.get_tableid())  


def scroll_col_major_table(table,direction) :
    """
    * -------------------------------------------------------------------------- 
    * function : scroll a col majot table
    * 
    * parms :
    *   table           -   dcTable object
    *   direction       -   direction left or right
    *
    * returns : 
    *  N?A
    * --------------------------------------------------------
    """
    #print("scroll_col_major_table",direction,table.get_lastcoldisplayed())
    
    set_col_major_table_scroll(table,direction)
        
    if(table.get_tableid() == "dfschema") :
        
        from dfcleanser.data_transform.data_transform_widgets import update_df_schema_table 
        df_schema_html  =   update_df_schema_table(table,direction,False)
        
        update_col_major_html(table,df_schema_html)
        
        refresh_dfschema_buttons()

    elif(table.get_tableid() == "dcgendfdesc") :
        
        from dfcleanser.common.display_utils import update_df_describe
        df_describe_html  =   update_df_describe(table,direction,False)
        
        update_col_major_html(table,df_describe_html)
        
    elif(table.get_tableid() == "dcnngendfdesc") :
        
        from dfcleanser.common.display_utils import update_df_nn_describe
        df_nn_describe_html  =   update_df_nn_describe(table,direction,False)
        
        update_col_major_html(table,df_nn_describe_html)
        
        refresh_chknum_buttons()


def get_col_major_table(table,displayTable=True) :
    """
    * -------------------------------------------------------------------------- 
    * function : A col_major_table is a single table that displays a subset of cols at a time
    * 
    * parms :
    *   table           -   dcTable object
    *   displayTable    -   display the html flag  
    *
    * returns : 
    *  html table
    * --------------------------------------------------------
    """

    if(not(displayTable)) :
        
        table_HTML = table.get_html(False)
        return(table_HTML)
        
    else :
        
        table.display_table() 





"""
* -----------------------------------------------------------------------*
* class for defining dataframe cleanser html based tables 
* -----------------------------------------------------------------------*
"""


class dcTable :
    
    """
    * -------------------------------------------------------------------------- 
    * Class Description : class for defining html tables for display
    * 
    * attributes :
    *   title               -   table title
    *   tableid             -   html id for table
    *   owner               -   owner id to drop or build tables
    *   headerList          -   list of <th> fields
    *   rowList             -   list of <tr> fields
    *   widthList           -   list of column widths in percents
    *   alignList           -   list of column alignmments ("Center", "Left", "Right")
    *   refList             -   list of <th> OnClick callbacks
    *   hhrefList           -   list of <tr> OnClick callbacks
    *   refParm             -   list of <tr> OnClick callback parms
    *   buttonList          -   list of <tr> buttons
    *   hiddensList         -   list of hidden elements associated with table
    *
    *   tabletype           -   table type (ROW_MAJOR, COLUMN_MAJOR) 
    *   colsperrow          -   number of columns per row
    *   rowspertable        -   number of rows per table
    *   lastrowdisplayed    -   last row displayed in ROW_MAJOR table
    *
    *   searchable          -   flag to make table searchable
    *   searchtext          -   text for search box
    *   searchcallback      -   search callback function
    *
    *   color               -   flag to make table colored
    *   colorList           -   list of colors for each column 
    *
    *   border              -   flag to draw border
    *
    *   small               -   flag to make table small
    *   smallwidth          -   small table width in percent
    *   smallmargin         -   small table left margin
    *   smallfsize          -   small table font size
    *
    *   shortrow            -   flag to draw border
    *   note                -   note below table
    *   notecolor           -   note below table
    *   checkLength         -   flag to check <th> and <tr> lengths and use popover
    *   firstcolpadding     -   list of left padding for first column in rows
    *
    * --------------------------------------------------------

    """
    
    # full constructor
    def __init__(self,    
                 title           =   "",
                 tableid         =   "",
                 owner           =   "",
                 headerList      =   None,
                 rowList         =   None,
                 widthList       =   None,
                 alignList       =   None) :

        
        # instance variables

        # minimum init attributes
        self.title           =   title
        self.tableid         =   tableid
        self.owner           =   owner
        
        # minimum table data attributes
        self.headerList      =   headerList
        self.rowList         =   rowList
        self.widthList       =   widthList
        self.alignList       =   alignList
        
        # reference attribures
        self.refList         =   None
        self.hhrefList       =   None

        self.refIndex        =   -1
        self.refParm         =   None
        self.buttonList      =   None

        # hidden vars attribures
        self.hiddensList     =   None
        
        self.tabletype       =   -1
        
        # attributes for table sizing     
        self.colsperrow      =   0
        self.rowspertable    =   0
        self.maxtables       =   0
        
        # attributes for row major table scrolling  
        self.lastrowdisplayed = -1

        # attributes for col major table scrolling  
        self.lastcoldisplayed  = -1
        self.maxcolumns        = -1
        self.colscrollcallback = None

        # attributes for search table     
        self.searchable      =   False
        self.searchParms     =   None 
        self.searchRow       =   0
        self.searchCol       =   0 
        
        # attributes for color table     
        self.color           =   False
        self.colorList       =   None
        
        self.border          =   True
        
        # attributes for small table     
        self.small           =   False
        self.smallwidth      =   99
        self.smallmargin     =   0
        self.smallfsize      =   12
        self.smallheader     =   True
        
        self.shortrow        =   True

        self.note            =   ""
        self.notecolor       =   None
        
        self.checkLength     =   True
        self.textLength      =   maxRowElement
        
        self.table_title_parms      =   None  
        self.table_header_parms     =   None    
        self.table_column_parms     =   None 
        
        # add the table to internal dict for later retrieval    
        if(get_table_value(self.tableid)==None) :
            set_table_value(self.tableid,self)
        else :
            drop_table_value(self.tableid)
            set_table_value(self.tableid,self)
        
    # class setters
    """
    # table identifier attributes
    """
    def set_title(self,titleParm) :
        self.title = titleParm
    def set_tableid(self,tableidParm) :
        self.tableid = tableidParm
    def set_owner(self,ownerParm) :
        self.owner = ownerParm

    """
    # table content attributes
    """
    def set_headerList(self,headerListParm) :
        self.headerList = headerListParm
    def set_rowList(self,rowListParm) :
        self.rowList = rowListParm
    def set_widthList(self,widthListParm) :
        self.widthList = widthListParm
    def set_alignList(self,alignListParm) :
        self.alignList = alignListParm
    def set_refList(self,refListParm) :
        self.refList = refListParm
    def set_refIndex(self,refIndexParm) :
        self.refIndex = refIndexParm
    def set_hhrefList(self,hhrefListParm) :
        self.hhrefList = hhrefListParm
    def set_refParm(self,refParmParm) :
        self.refParm = refParmParm
    def set_buttonList(self,buttonListParm) :
        self.buttonList = buttonListParm
    def set_hiddensList(self,hiddensListParm) :
        self.hiddensList = hiddensListParm

    """
    # table type attributes
    """
    def set_tabletype(self,tabletypeParm) :
        self.tabletype        =   tabletypeParm
          
    # attributes for table sizing     
    def set_colsperrow(self,colsperrowParm) :
        self.colsperrow        =   colsperrowParm
    def set_rowspertable(self,rowspertableParm) :
        self.rowspertable        =   rowspertableParm
    def set_maxtables(self,maxtablesParm) :
        self.maxtables        =   maxtablesParm

    # attributes for row major table 
    def set_lastrowdisplayed(self,lastrowdisplayedParm) :
        self.lastrowdisplayed         =   lastrowdisplayedParm
       
    # attributes for row major table 
    def set_lastcoldisplayed(self,lastcoldisplayedParm) :
        self.lastcoldisplayed         =   lastcoldisplayedParm
    def set_maxcolumns(self,maxcolumnsParm) :
        self.maxcolumns         =   maxcolumnsParm
    def set_colscrollcallback(self,callbackparm) :
        self.colscrollcallback        =   callbackparm 
        
    """
    # search table attributes
    """
    def set_searchable(self,searchableParm) :
        self.searchable = searchableParm
    def set_searchParms(self,searchParms) :
        self.searchParms = searchParms
    def set_searchRow(self,rowParm) :
        self.searchRow = rowParm
    def set_searchCol(self,colParm) :
        self.searchCol = colParm

    """
    * color table attributes
    """
    def set_color(self,colorParm) :
        self.color           =   colorParm
    def set_colorList(self,colorListParm) :
        self.colorList       =   colorListParm
    def set_border(self,borderParm) :
        self.border          =   borderParm
        
    """
    * small table attributes
    """
    def set_small(self,smallParm) :
        self.small           =   smallParm
    def set_smallwidth(self,smallwidthParm) :
        self.smallwidth       =   smallwidthParm
    def set_smallmargin(self,smallmarginParm) :
        self.smallmargin       =   smallmarginParm
    def set_smallheader(self,smallheaderParm) :
        self.smallheader       =   smallheaderParm
    
    """
    * shorten elements with popover table attributes
    """
    def set_shortrow(self,shortrowParm) :
        self.shortrow        =   shortrowParm
    
    """
    * attach note to table attributes
    """
    def set_note(self,noteParm) :
        self.note           =   noteParm
    def set_notecolor(self,notecolorParm) :
        self.notecolor      =   notecolorParm

    """
    * shorten elements with popover table attributes
    """
    def set_checkLength(self,checkLengthParm) :
        self.checkLength    =   checkLengthParm
    def set_textLength(self,textLengthParm) :
        self.textLength    =   textLengthParm
        
    def set_html_only(self,html_onlyParm) :    
        self.html_only       =   html_onlyParm
        
    def set_table_title_parms(self,table_title_parms_in) :        
        self.table_title_parms      =   table_title_parms_in 
    def set_table_header_parms(self,table_header_parms_in) :        
        self.table_header_parms     =   table_header_parms_in 
    def set_table_column_parms(self,table_column_parms_in) :  
        self.table_column_parms     =   table_column_parms_in
        
    # class getters    
    def get_title(self) :
        return(self.title)
    def get_tableid(self) :
        return(self.tableid)
    def get_owner(self) :
        return(self.owner)
        
    def get_headerList(self) :
        return(self.headerList)
    def get_rowList(self) :
        return(self.rowList)
    def get_widthList(self) :
        return(self.widthList)
    def get_alignList(self) :
        return(self.alignList)
    
    def get_refList(self) :
        return(self.refList)
    def get_refIndex(self) :
        return(self.refIndex)
    def get_hhrefList(self) :
        return(self.hhrefList)
    def get_refParm(self) :
        return(self.refParm)
    def get_buttonList(self) :
        return(self.buttonList)

    def get_hiddensList(self) :
        return(self.hiddensList)

    def get_tabletype(self) :
        return(self.tabletype)
        
    def get_colsperrow(self) :
        return(self.colsperrow)
    def get_rowspertable(self) :
        return(self.rowspertable)
    def get_maxtables(self) :
        return(self.maxtables)
    
    # attributes for row major table 
    def get_lastrowdisplayed(self) :
        return(self.lastrowdisplayed)
        
    # attributes for col major table 
    def get_lastcoldisplayed(self) :
        return(self.lastcoldisplayed)
    def get_maxcolumns(self) :
        return(self.maxcolumns)
    def get_colscrollcallback(self) :
        return(self.colscrollcallback) 

    # attributes for search table     
    def get_searchable(self) :
        return(self.searchable)
    def get_searchParms(self) :
        return(self.searchParms)
    def get_searchRow(self) :
        return(self.searchRow)
    def get_searchCol(self) :
        return(self.searchCol)
   
    # attributes for color table     
    def get_color(self) :
        return(self.color)
    def get_colorList(self) :
        return(self.colorList)
    def get_border(self) :
        return(self.border)
        
    # attributes for small table
    def get_small(self) :
        return(self.small)
    def get_smallwidth(self) :
        return(self.smallwidth)
    def get_smallmargin(self) :
        return(self.smallmargin)
    def get_smallheader(self) :
        return(self.smallheader)
    
    def get_shortrow(self) :
        return(self.shortrow) 
        
    def get_note(self) :
        return(self.note)
    def get_notecolor(self) :
        return(self.notecolor)
    
    def get_checkLength(self) :
        return(self.checkLength)
    def get_textLength(self) :
        return(self.textLength)
    
    def get_firstcolpadding(self) :
        return(self.firstcolpadding)
    def set_firstcolpadding(self,setParm) :
        self.firstcolpadding = setParm

    def get_table_title_parms(self) :        
        return(self.table_title_parms) 
    def get_table_header_parms(self) :        
        return(self.table_header_parms) 
    def get_table_column_parms(self) :        
        return(self.table_column_parms)
        
    def get_table_title_parm(self,title_parm_id) :
        try :
            return(self.get_table_title_parms(self)[title_parm_id])
        except :
            return(None)

    def get_table_header_parm(self,header_parm_id) :
        try :
            return(self.get_table_header_parms(self)[header_parm_id])
        except :
            return(None)

    def get_table_column_parm(self,column_parm_id) :
        try :
            parm    =   self.get_table_column_parms().get(column_parm_id,None)
            return(parm)
        except :
            return(None)
           

    def get_html(self,fulltable=True) :
        
        tableHTML = ""
    
        if(self.get_searchable()) :
            tableHTML = (tableHTML + self.get_search_table_header(fulltable))
        else :
            tableHTML = (tableHTML + self.get_non_search_table_header(self.get_table_scrolls(),fulltable))
            
        fsize   =   self.get_table_column_parm("font")
        if(fsize is None) :
            tableHTML = (tableHTML + table_start)
        elif(fsize == 11) :
            tableHTML = (tableHTML + table_start11)
        elif(fsize == 12) :
            tableHTML = (tableHTML + table_start12)
        elif(fsize == 13) :
            tableHTML = (tableHTML + table_start13)
        else :
            tableHTML = (tableHTML + table_start)
    
        if(self.get_tableid() != None) :
            tableHTML = (tableHTML + addattribute("id",self.get_tableid()))

        tableHTML = (tableHTML + element_close)

        """
        /*************************
        /* Table Header
        /*************************
        """

        foundHeader = False
        for i in range(len(self.get_headerList())) :
            if( (self.get_headerList()[i] != None) and (len(self.get_headerList()[i]) > 0) ) :
                foundHeader = True

        if(foundHeader) :
        
            tableHTML = (tableHTML + new_line + table_head_start)
            if(self.get_color()) :
                tableHTML = (tableHTML + table_color_head_row_start + addattribute("id",self.get_tableid() + "_thr") + ">" + new_line)
            else :
                tableHTML = (tableHTML + table_head_row_start + addattribute("id",self.get_tableid() + "_thr") + ">" + new_line)
    
            try :

                for i in range(len(self.get_headerList())) :
                    if(self.get_hhrefList() == None) :

                        tableHTML = (tableHTML + self.add_table_head_column(self.get_headerList()[i],
                                                                            self.get_widthList()[i],
                                                                            self.get_alignList()[i]))
            
                    elif( (self.get_hhrefList()[i] == None) or (len(self.get_headerList()[i]) == 0) ) :

                        tableHTML = (tableHTML + self.add_table_head_column(self.get_headerList()[i],
                                                                            self.get_widthList()[i],
                                                                            self.get_alignList()[i]))
                    
                    else : 

                        tableHTML = (tableHTML + self.add_table_head_column(self.get_headerList()[i],
                                                                            self.get_widthList()[i],
                                                                            self.get_alignList()[i],
                                                                            self.get_hhrefList()[i]) )
                    
                    if(i != (len(self.get_headerList())) - 1) : #table.get_colsperrow()-1)):#len(table.get_headerList()) - 1) ) :
                        tableHTML = (tableHTML + new_line)
                        
            except Exception as e:
                
                print("Header Error i = ",i)
                self.dump()
                from dfcleanser.common.common_utils import opStatus,display_exception
                opstat  =   opStatus()
                
                opstat.store_exception("table header",e)
                opstat.set_status(False)
                display_exception(opstat)

            
            tableHTML = (tableHTML + new_line + table_head_row_end)
            tableHTML = (tableHTML + table_head_end)

        """
        /*************************
        /* Table Body
        /*************************
        """
            
        tableHTML = (tableHTML + table_body_start)

        startrowIndex   =   0
        rowcount        =   0
    
        startrowIndex, rowcount = self.get_row_indices()
        
        for i in range(startrowIndex, (startrowIndex + rowcount)) :
        
            if(self.get_refList() == None) :
                tableHTML = (tableHTML + self.add_table_body_row(i,
                                                                 self.get_rowList()[i],
                                                                 self.get_refList()))
            else :
                if(type(self.get_refList()[0]) == list) :
                    tableHTML = (tableHTML + self.add_table_body_row(i,
                                                                     self.get_rowList()[i],
                                                                     self.get_refList()[i])) 
                else :
                    tableHTML = (tableHTML + self.add_table_body_row(i,
                                                                     self.get_rowList()[i],
                                                                     self.get_refList()))

        tableHTML = (tableHTML + table_body_end)
        tableHTML = (tableHTML + table_end)
    
        if(fulltable) :
            tableHTML = (tableHTML + table_container_end)
        
            if(len(self.get_note()) > 0 ) :
                
                tableHTML = (tableHTML + table_note_start)
                #tableHTML = (tableHTML + addattribute("id",self.get_tableid()+"note") + ">" + new_line)

                if(not (self.get_notecolor() is None)) :
                    tableHTML = (tableHTML + table_note_color_start)
                    tableHTML = (tableHTML + str(self.get_notecolor()) + "'>")
                    tableHTML = (tableHTML + self.get_note() + "</span></p>" + new_line)
                else :
                    tableHTML = (tableHTML + self.get_note() + "</p>" + new_line)
                    
                tableHTML = (tableHTML + table_note_end)
            
            tableHTML = (tableHTML + table_container_end1)
        
        else :
            tableHTML = (tableHTML + table_nd_container_end)
        
            if(len(self.get_note()) > 0 ) :
                
                tableHTML = (tableHTML + table_note_start)

                if(not (self.get_notecolor() is None)) :
                    tableHTML = (tableHTML + table_note_color_start)
                    tableHTML = (tableHTML + str(self.get_notecolor()) + "'>")
                    tableHTML = (tableHTML + self.get_note() + "</span></p>" + new_line)
                else :
                    tableHTML = (tableHTML + self.get_note() + "</p>" + new_line)
                    
                tableHTML = (tableHTML + table_note_end)
            
            tableHTML = (tableHTML + table_nd_container_end1)
            
        if(fulltable) :
            tableHTML = (tableHTML + table_form_end)
        #else :
        #    tableHTML = (tableHTML + table_form_end)
        
        if(self.get_tabletype() == ROW_MAJOR) :
            self.set_lastrowdisplayed(startrowIndex + rowcount) 

        if(debugTables) :   
            print("\n\nTable HTML\n",tableHTML)
        
        """
        /*************************
        /* Table dump and display
        /*************************
        """
        
        #debug 
        if(not(self.get_title() is None))  :  
            if( ("#Column Values" in self.get_title()) or 
               (self.get_title() == "#Numeric Column Stats") or 
               ("#Column Names" in self.get_title()) ) :  
                self.dump()
                print(tableHTML)
        
        from dfcleanser.common.common_utils import DUMP_HTML
        if(DUMP_HTML) :
            if(not(self.get_tableid() == "dfschema")) :
                print(tableHTML)
            else :
                Html_file= open("dfschema_file","w")
                Html_file.write(tableHTML)
                Html_file.close()
            
        return(tableHTML)

    def display_table(self) :
        tableHTML = self.get_html(True)
        from dfcleanser.common.common_utils import (displayHTML)
        displayHTML(tableHTML)
        
    def dump(self) :
        print("\nTable Dump : ",self.get_tableid(),"\n")
        print(" Title       : ",self.get_title())
        print(" Owner       : ",self.get_owner())
        print(" tabletype   : ",self.get_tabletype())
        if(self.get_headerList() == None) :
            print(" Header      : None")
        else :
            print("\n Headers     : ",self.get_headerList())
            
        if(self.get_rowList() == None) :
            print(" Rows      : None")
        else :
            print(" Rows        :  [",len(self.get_rowList()),"]")
            if(type(self.get_rowList()[0]) == list) :
                for i in range(len(self.get_rowList())) :
                    if(len(str(self.get_rowList()[i])) > 100) :
                        print("   Row ["+str(i) + "]     : ",self.get_rowList()[i][0:100]) 
                    else :
                        print("   Row ["+str(i) + "]     : ",self.get_rowList()[i])
            else :
                print(self.get_rowList())
                
        if(self.get_widthList() == None) :
            print(" Width      : None")
        else :
            print(" Widths      : ",self.get_widthList())

        if(self.get_alignList() == None) :
            print(" Aligns     : None")
        else :
            print(" Aligns      : ",self.get_alignList())
        
        if(self.get_refList() == None) :
            print(" Refs        :  None")
        else :
            print(" Refs        : [",len(self.get_refList()),"]")
            if(type(self.get_refList()[0]) == list) :
                for i in range(len(self.get_refList())) :
                    print("   Ref ["+str(i) + "]     : ",self.get_refList()[i])
            else :
                print("   Ref ["+str(i) + "]     : ",self.get_refList())
        
        if(self.get_hhrefList() == None) :
            print("  hhrefs      :  None")
        else :
            print("  hhrefs      : ",self.get_hhrefList())

        if(self.get_color() == True) :
            print(" Colors      : [",len(self.get_colorList()),"]")
            for i in range(len(self.get_colorList())) :
                print("   Color ["+str(i) + "] : ",self.get_colorList()[i])
   
        if(self.get_searchable()) :
            print("\n searchable  : ",self.get_searchable())
            searchParms = self.get_searchParms()
            search_keys =   list(searchParms.keys())
            for i in range(len(search_keys)) :
                print("  ",search_keys[i],str(searchParms.get(search_keys[i]))) 
            print("\n")
            
        else :
            print("\n searchable  : ",self.get_searchable())
            
        if(self.get_tabletype() == ROW_MAJOR) :
            print("\nROW_MAJOR Parms :")
            print(" rowspertable       :     ",self.get_rowspertable())
            print(" lastrowdisplayed   :     ",self.get_lastrowdisplayed(),"\n")
        elif(self.get_tabletype() == COLUMN_MAJOR) :
            print("\nCOLUMN_MAJOR Parms :")
            print(" colsperrow         :     ",self.get_colsperrow())
            print(" lastcoldisplayed   :     ",self.get_lastcoldisplayed())
            print(" maxcolumns         :     ",self.get_maxcolumns())
            print(" scrollcallback     :     ",self.get_colscrollcallback(),"\n")
        elif(self.get_tabletype() == ROW_COL_MAJOR) :
            print("\nROW_COL_MAJOR Parms  :")
            print(" rowspertable       :     ",self.get_rowspertable())
            print(" lastrowdisplayed   :     ",self.get_lastrowdisplayed())
            print(" colsperrow         :     ",self.get_colsperrow())
            print(" lastcoldisplayed   :     ",self.get_lastcoldisplayed(),"\n")

        if(self.get_small()) :
            print("\n smallwidth     : ",self.get_smallwidth())
            print(" smallmargin    : ",self.get_smallmargin())

        if(self.get_shortrow()) :
            print(" shortrow       : ",self.get_shortrow())
            
        print(" border         : ",self.get_border())
        print(" checkLength    : ",self.get_checkLength())
        print(" textlength     : ",self.get_textLength())

        if(not(self.get_note() == "")) :
            print("\n note           : ",self.get_note())





    """
    * -------------------------------------------------------------------------- 
    * ------------------------ table build utilities---------------------------- 
    * --------------------------------------------------------------------------
    """


    def get_table_container_start(self,tableDisplay=True) :
        """
        * -------------------------------------------------------------------------- 
        * function : get table start container wrapper
        * 
        * parms :
        *   tableDisplay    -   display table flag 
        *
        * returns : 
        *  N/A
        * --------------------------------------------------------
        """

        tableHTML = ""

        if(self.get_small()) :
            tableHTML = (tableHTML + new_line + '<div class="container dc-table-container" ')
            tableHTML = (tableHTML + addattribute("id",self.get_tableid() + "container"))
            tableHTML = (tableHTML + ' style="width:' + str(self.get_smallwidth()) + '%;' + 
                                 ' margin-left:' + str(self.get_smallmargin()) + 'px;">' + new_line)
        #tableHTML = (tableHTML  + '    <div class="row">' + new_line)
            if(self.get_border()) :
                tableHTML = (tableHTML  + '    <div class="panel panel-primary" style="border:0px;"' + ">")
            else :
                tableHTML = (tableHTML  + '    <div class="panel panel-primary" style="border:0px;"' + ">")
        else :
            if(tableDisplay) :
                tableHTML = (tableHTML + table_container_start)
                tableHTML = (tableHTML + addattribute("id",self.get_tableid()+"container")  + " style='width:100%;'" + ">")
        
            tableHTML = (tableHTML + table_container_middle + " style=border:0px;>")
    
        return(tableHTML)
        

    def get_search_table_header(self,fulltable) : 
        """
        * -------------------------------------------------------------------------- 
        * function : get search table header
        * 
        * parms :
        *   tableDisplay    -   display table flag 
        *
        * returns : 
        *  N/A
        * --------------------------------------------------------
        """
        
        tableHTML = ""

        if(fulltable) :
            tableHTML = (tableHTML + table_form_start)
            tableHTML = (tableHTML + addattribute("id",self.get_tableid()+"form") + ">")
    
        if(self.get_hiddensList() != None) :
            tableHTML = (tableHTML + self.get_hiddens(self.get_tableid(),self.get_hiddensList()))
        
        tableHTML = (tableHTML + self.get_table_container_start())
        
        scrolllist   =   [0,0,0,0]
    
        if(not (self.get_searchParms() == None) ) :
            searchParms = self.get_searchParms()
            
            if(searchParms.get("SCROLL_UP") == True)    :  scrolllist[0]    =   1
            if(searchParms.get("SCROLL_DOWN") == True)  :  scrolllist[1]    =   1
            if(searchParms.get("SCROLL_RIGHT") == True) :  scrolllist[2]    =   1
            if(searchParms.get("SCROLL_LEFT") == True)  :  scrolllist[3]    =   1
            
        
    
        tableHTML = (tableHTML + self.get_scroll_table_title_row(False,scrolllist,True))

        return(tableHTML)



    def get_non_search_table_header(self,scrolllist,fulltable) : 
        """
        * -------------------------------------------------------------------------- 
        * function : get non search table header
        * 
        * parms :
        *   more            -   more flag
        *   prev            -   previous flag
        *   tableDisplay    -   display table flag 
        *
        * returns : 
        *  N/A
        * --------------------------------------------------------
        """

        tableHTML = ""

        if(fulltable) :
            tableHTML = (tableHTML + table_form_start)
            tableHTML = (tableHTML + addattribute("id",self.get_tableid()+"form") + ">")
    
        if(self.get_hiddensList() != None) :
            tableHTML = (tableHTML + get_hiddens(self.get_tableid(),self.get_hiddensList()))
        
        tableHTML = (tableHTML + self.get_table_container_start())

        if(not(self.get_title() is None)) :
        
            scrollFlag  =   False
            for i in range(len(scrolllist)) :
                if(scrolllist[i] == 1) : scrollFlag  =   True

            if(scrollFlag) :
                if(self.get_small()) :
                    tableHTML = (tableHTML + self.get_scroll_table_title_row(True,scrolllist))
                else :
                    tableHTML = (tableHTML + self.get_scroll_table_title_row(False,scrolllist))
            else :
                if(self.get_small()) :
                    tableHTML = (tableHTML + self.get_table_title_row(True))
                else :
                    tableHTML = (tableHTML + self.get_table_title_row(False))
                    
        return(tableHTML)

        
    def add_callback_to_item(self,headerrow,rowflag,value,func,parm=None) :
        """
        * -------------------------------------------------------------------------- 
        * function : add callback function to table item
        * 
        * parms :
        *   direction       -   direction to scroll in 
        *   displayTable    -   display the html flag  
        *
        * returns : 
        *  N/A
        * --------------------------------------------------------
        """
    
        item_html = ""

        if(type(value) == list) :
            rowvalue = value[1]
            rowindex = str(value[0])
        else :
            rowvalue = value
            rowindex = str(value)
        
        if(parm == None) :
            cparm = ""
        else :
            parmIsstring = False
            try :
                int(parm)
            except :
                parmIsstring = True
        
            if(parmIsstring) :
                cparm = "," + "'" + str(parm) + "'" 
            else :
                cparm = "," + str(parm)
            
        valueIsstring = False 
    
        try :
            int(rowvalue)
            valueIsstring = False
        except :
            valueIsstring = True
 
        strvalue = str(rowvalue) 

        if(len(strvalue) > maxRowElement) :
        
            # check for length of element
            newstrvalue = strvalue.replace("<b>","")
            newstrvalue = newstrvalue.replace("</b>","")
            if(self.get_checkLength() == True) :
                newstrvalue = newstrvalue.replace("&nbsp;","")
        
            if(len(newstrvalue) > maxRowElement) :
            
                if(valueIsstring):
                    if(headerrow) :
                        item_html = (item_html + '<a href="#" class="dc-table-link" style="text-decoration:none;" onclick="' + func + "(" + 
                                     "'" + strip_leading_blanks(strvalue) + "'" +  cparm + ')"' + 
                                     ' data-toggle="tooltip" data-placement="top" title="' + 
                                     strip_leading_blanks(strvalue) + '">' + self.shorten_element(newstrvalue,rowflag) + "</a>")
                    
                    else : 
                        item_html = (item_html + '<a href="#" class="dc-table-row-link" style="text-decoration:none;" onclick="' + func + "(" + 
                                     "'" + strip_leading_blanks(strvalue) + "'" +  cparm + ')"' + 
                                     ' data-toggle="tooltip" data-placement="top" title="' + 
                                     strip_leading_blanks(strvalue) + '">' + self.shorten_element(newstrvalue,rowflag) + "</a>")
                
                else :
                    item_html = (item_html + '<a href="#" class="dc-table-link" style="text-decoration:none;" onclick="' + func + "(" + 
                                 strip_leading_blanks(strvalue) + cparm + ')"' + 
                                 ' data-toggle="tooltip" data-placement="top" title="' +
                                 strip_leading_blanks(strvalue) + '">' + self.shorten_element(newstrvalue,rowflag) + "</a>")
                
            else : 
                if(valueIsstring):
                    item_html = (item_html + '<a href="#" class="dc-table-link" style="text-decoration:none;" onclick="' + func + "(" + 
                                 "'" + strip_leading_blanks(strvalue) + "'" +  cparm + ')">' + strvalue + "</a>")
                else :
                    item_html = (item_html + '<a href="#"style="text-decoration:none;" onclick="' + func + "(" + 
                                 strip_leading_blanks(strvalue) + cparm + ')">' + strvalue + "</a>")
            
        else :  

            if(valueIsstring):
                if(headerrow) :
                    item_html = (item_html + '<a href="#" class="dc-table-link" style="text-decoration:none;" onclick="' + func + "(" + 
                                 "'" + rowindex + "'" +  cparm + ')">' + strvalue + "</a>")
                else :
                    item_html = (item_html + '<a href="#" class="dc-table-row-link" style="text-decoration:none;" onclick="' + func + "(" + 
                                 "'" + rowindex + "'" +  cparm + ')">' + strvalue + "</a>")
            else :
                item_html = (item_html + '<a href="#" class="dc-table-row-link" style="text-decoration:none;" onclick="' + func + "(" + 
                             rowindex + cparm + ')">' + strvalue + "</a>")
        
        return(item_html)
        

    def add_table_head_column(self,coltext,width,align,href=None) :
        """
        * -------------------------------------------------------------------------- 
        * function : add table header column
        * 
        * parms :
        *   coltext         -   text to display in column header 
        *   width           -   width in pixels  
        *   align           -   text alignment ("left" : default "center") 
        *   href            -   call hrefon click
        *
        * returns : 
        *  N/A
        * --------------------------------------------------------
        """

        colHTML = ""
        colHTML = (colHTML + "                      <th" + 
                   addattribute("style",addstyleattribute("width", str(width)+"%")) )

        if( align == "left") :
            colHTML = (colHTML + addattribute("class"," dccolhead dccolleft")) 
        else :
            colHTML = (colHTML + addattribute("class"," dccolhead")) 
    
        if(href == None) :
        
            coltext_sep     =   coltext.split(" ")
            too_long        =   False
        
            for i in range(len(coltext_sep)) :
                if(len(coltext_sep[i]) > maxRowElement) :
                    too_long    =   True
                    break
                
            if(too_long) :
                colHTML = (colHTML + '<a href="#" class="dc-table-link" style="text-decoration:none;"'  +  
                                     ' data-toggle="tooltip" data-placement="top" title="' +
                                     strip_leading_blanks(coltext) + '">' + self.shorten_element(coltext,False) + "</a></th>")
            
            else :
                colHTML = (colHTML + ">" + coltext + "</th>")
            
        else :
            if(len(coltext) > 0) :
                colHTML = (colHTML + ">" + self.add_callback_to_item(True,False,coltext,href) + "</th>")

        return(colHTML)


    def shorten_element(table,element,row=True) :
        """
        * -------------------------------------------------------------------------- 
        * function : table item shorten and put pop up around
        * 
        * parms :
        *   element         -   text to check on 
        *   row             -   row flag or headerflag 
        *
        * returns : 
        *  N/A
        * --------------------------------------------------------
        """
    
        if(not table.get_checkLength()) :
            return(element)
        
        if(row) :
            if(not table.get_shortrow()) :
                return(element)
            
        if(len(element) > table.get_textLength()) :
            halflength = int(table.get_textLength()/2) - 2
            shortelement = element[0:halflength] + "...." + element[(len(element)-halflength) : (len(element))]
        else :
            shortelement = element
        
        return(shortelement)


    def get_row_element(self,rowElement) :
        """
        * -------------------------------------------------------------------------- 
        * function : get individual row element
        * 
        * parms :
        *   rowElement      -   row element (column) 
        *
        * returns : 
        *  N/A
        * --------------------------------------------------------
        """
    
        rowHtml = ""
    
        if(type(rowElement) == str) :
            
            if( (rowElement.find("<div") < 0)  and (rowElement.find("<table") < 0) ):
        
                # check for length of element
                newrowElement = rowElement.replace("<b>","")
                newrowElement = newrowElement.replace("</b>","")
                newrowElement = newrowElement.replace("&nbsp;","")

                if(not self.get_checkLength()) :
                    rowHtml = rowElement
                else :
                    if(len(newrowElement) > self.get_textLength()) :
                        if(newrowElement.find(",") > -1) :
                            rowHtml = rowElement 
                        else :
                            rowHtml = ('<a href="#" data-toggle="tooltip" data-placement="top" title="' +  
                                       newrowElement + '">' + self.shorten_element(newrowElement) + '</a>')
                    else :
                        rowHtml = rowElement
            else :
                rowHtml = rowElement
                
        else :
            rowHtml = rowElement

        return(rowHtml)


    def add_table_body_row(self,index,rowElement,href) :
        """
        * -------------------------------------------------------------------------- 
        * function : add table body row
        * 
        * parms :
        *   index           -   row index 
        *   rowElement      -   row element (column) 
        *   href            -   anchor 
        *
        * returns : 
        *  N/A
        * --------------------------------------------------------
        """
    
        rowHTML = ""
    
        not_all_hrefs   =   False
    
        if(not href == None) :
            for i in range(len(rowElement)) : 
                if(href[i] == None) :
                    not_all_hrefs   =   True
                    break
        
        if(not_all_hrefs) :
            rowHTML = (rowHTML + table_body_row_start)
        else :
            rowHTML = (rowHTML + table_body_row_href_start)

        if(self.get_color()) :
            tablecolorlist = self.get_colorList()[index]

        for i in range(len(rowElement)) : 
        
            if(self.get_color()) :

                if(tablecolorlist[i] == None) :
                    rowHTML = (rowHTML + "                        <td" + 
                               addattribute("style",addstyleattribute("width", str(self.get_widthList()[i])+"%")))
                else :
                    rowHTML = (rowHTML + "                        <td" + 
                               addattribute("bgcolor",tablecolorlist[i]) + 
                               addattribute("style",addstyleattribute("width", str(self.get_widthList()[i])+"%")))
            else :
                rowHTML = (rowHTML + "                        <td" + 
                           addattribute("style",addstyleattribute("width", str(self.get_widthList()[i])+"%")))
        
            if( self.get_alignList()[i] == "left") : 
                rowHTML = (rowHTML + addattribute("class","dccolleft dccolwrap"))
            else :
                rowHTML = (rowHTML + addattribute("class","dccolwrap"))

            if(href == None) :
                if("_cb" in str(rowElement[i])) :
                    rowHTML = (rowHTML + ">" + new_line)
                    rowHTML = (rowHTML + col_cb_div_start + new_line)
                    rowHTML = (rowHTML + col_cb_input_start)
                    rowHTML = (rowHTML + addattribute("id",str(rowElement[i])))
                    rowHTML = (rowHTML + col_cb_input_end)
                    rowHTML = (rowHTML + col_cb_div_end + new_line)
                    rowHTML = (rowHTML +  col_cb_td_end)
                else :
                    rowHTML = (rowHTML + ">" + str(self.get_row_element(rowElement[i])) + "</td>")
                
            elif(href[i] == None) :
                rowHTML = (rowHTML + ">" + str(self.get_row_element(rowElement[i])) + "</td>")
            else :
                if(self.get_buttonList() == None) :
                    if(self.get_refIndex() == -1) :
                
                        if(len(str(rowElement[i])) > 0) :
                            rowHTML = (rowHTML + ">" + self.add_callback_to_item(False,True,
                                                                                 rowElement[i],
                                                                                 href[i],
                                                                                 self.get_refParm()) + "</td>")
                        else :
                            rowHTML = (rowHTML + ">"  + "</td>")
                            
                    else :
                        rowHTML = (rowHTML + ">" + self.add_callback_to_item(False,True,
                                                                             [(self.get_refIndex()+index),
                                                                              rowElement[i]],
                                                                              href[i],
                                                                              self.get_refParm()) + "</td>")
                    
                else :
                    if(not (self.get_buttonList()[index][i] == None)) :
                        rowHTML = (rowHTML + ">")
                        rowHTML = (rowHTML + table_button_div_start)
                        rowHTML = (rowHTML + table_button_start)
                        rowHTML = (rowHTML + addattribute("id",self.get_tableid()+str(rowElement[i]) + "button"))
                        rowHTML = (rowHTML + addattribute("OnClick",href[i]+"('"+ str(i) +"')") )
                        rowHTML = (rowHTML + ">" + str(rowElement[i]))
                        rowHTML = (rowHTML + table_button_end)
                        rowHTML = (rowHTML + table_button_div_end)

            if(i != (len(rowElement) - 1)) :
                rowHTML = (rowHTML + new_line)    
        
        rowHTML = (rowHTML + table_body_row_end)

        return(rowHTML)


    def get_table_scrolls(self) :
        """
        * -------------------------------------------------------------------------- 
        * function : determine if table needs scroll buttons defined and included
        * 
        * parms :
        *
        * returns : 
        *  N/A
        * --------------------------------------------------------
        """
    
        if(self.get_tabletype() == ROW_MAJOR) :
            if(len(self.get_rowList()) > self.get_rowspertable() ) :
                return([1,1,0,0]) 
            else :
                return([0,0,0,0])
    
        elif(self.get_tabletype() == COLUMN_MAJOR) :
            return([0,0,1,1])        
            
        else :
            return([0,0,0,0])        
        

    def get_table_title_row(self,smallflag) :
        """
        * -------------------------------------------------------------------------- 
        * function : get header row for non scrolling table
        * 
        * parms :
        *   smallflag       -   small table flag 
        *
        * returns : 
        *  N/A
        * --------------------------------------------------------
        """

        table_id        =   self.get_tableid()
        table_title     =   self.get_title()
    
        header_html     =   plain_title_row[0:]
        
        
        
    
        header_html     =   header_html.replace("XXXXHeaderTable",table_id+"HeaderTable")
        header_html     =   header_html.replace("XXXXTitle",table_title)
        header_html     =   header_html.replace("XXXXTableTitle",table_id+"TableTitle")
    
        if(smallflag) :
            height    =   "25px"
            font_size =   "13px"
        else :
            height    =   "40px"
            font_size =   "16px"
        
        header_html     =   header_html.replace("XXXXheight",height)
        header_html     =   header_html.replace("XXXXfont-size",font_size)

        return(header_html)


    def is_scrolling_required(self,searchParms) :
        
        if(not(searchParms is None)) :
            if( (searchParms.get("SCROLL_UP_callback") == None) and 
                (searchParms.get("SCROLL_DOWN_callback") == None) and
                (searchParms.get("SCROLL_RIGHT_callback") == None) and
                (searchParms.get("SCROLL_LEFT_callback") == None) ) :

                return(False)
            else :
                return(True)
        else :
            return(False)
        
        
    def get_scroll_table_title_row(self,smallflag,scrolllist,addSearch=False) :
        """
        * -------------------------------------------------------------------------- 
        * function : get header row for scrolling table
        * 
        * parms :
        *   smallflag       -   small table flag 
        *
        * returns : 
        *  N/A
        * --------------------------------------------------------
        """

        table_id        =   self.get_tableid()
        table_title     =   self.get_title()
    
        header_html     =   scroll_title_row[0:]
    
        header_html     =   header_html.replace("XXXXHeaderTable",table_id+"HeaderTable")
        
        import dfcleanser.common.cfg as cfg
        if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
            if(addSearch) :
                titlewidth  =   "20"
            else :
                scrollcount     =   0
                for i in range(len(scrolllist)) :
                    if(scrolllist[i] == 1) :
                        scrollcount     =   scrollcount + 1
                if(scrollcount > 2) :
                    titlewidth  =   "35"
                else :
                    titlewidth  =   "45"
        else :
            if(addSearch) :
                titlewidth  =   "10"
            else :
                titlewidth  =   "55"
            
        header_html     =   header_html.replace("xxxxTitleWidth", titlewidth)
        header_html     =   header_html.replace("XXXXTitle",table_title)
        header_html     =   header_html.replace("XXXXTableTitle",table_id+"TableTitle")
    
        if(smallflag) :
            arrowsize   =   "15px"
            height      =   "25px"
            font_size   =   "13px"
        
        else :
            arrowsize   =   "20px"
            height      =   "40px"
            font_size   =   "16px"
    
        header_html     =   header_html.replace("XXXXheight",height)
        header_html     =   header_html.replace("XXXXfont-size",font_size)
    
        scrollFlag  =   False
        for i in range(len(scrolllist)) :
            if(scrolllist[i] == 1) :     scrollFlag=True
        
        if(addSearch) :
            
            searchParms     =   self.get_searchParms()
            search_html     =   search_col[0:]
            
            if(cfg.get_dfc_mode() == cfg.INLINE_MODE) :
                inputwidth  =   "15"
                if(self.is_scrolling_required(searchParms)) :
                    iconwidth   =   "10"
                else :
                    iconwidth   =   "60"
            else :
                inputwidth  =   "30"
                iconwidth   =   "5"
                
            search_html     =   search_html.replace("xxxxInputWidth",inputwidth)
            search_html     =   search_html.replace("xxxxIconWidth",iconwidth)
            
            if(not(searchParms is None)) :
                
                onclick         =   searchParms.get("searchcallback")
                searchid        =   searchParms.get("searchinputId")
                searchtext      =   searchParms.get("searchinputtext")
                upcallback      =   searchParms.get("SCROLL_UP_callback")
                downcallback    =   searchParms.get("SCROLL_DOWN_callback")
                rightcallback   =   searchParms.get("SCROLL_RIGHT_callback")
                leftcallback    =   searchParms.get("SCROLL_LEFT_callback")
                
                search_html     =   search_html.replace("XXXXonclick",onclick)
                search_html     =   search_html.replace("XXXXsid",searchid)
                search_html     =   search_html.replace("XXXXtextid",searchtext)
                
            else :
                
                upcallback      =   ""
                downcallback    =   ""
                rightcallback   =   ""
                leftcallback    =   ""
                
            header_html    =   (header_html + search_html)

        if(scrollFlag) : 
        
            header_html    =   (header_html + scroll_col_start)
        
            for i in range(len(scrolllist)) :
                arrow_html     =   scroll_button[0:]
        
                if(scrolllist[i] == 1) :
                    if(i==0)    :  
                        image       =   "downarrow"
                        direction   =   "0"
                        if(addSearch) : callback    =   upcallback
                        else :          callback    =   "scrollTable('" + table_id + "'," + direction + ")"         
                    
                    elif(i==1)  :  
                        image       =   "uparrow"
                        direction   =   "1"
                        if(addSearch) : callback    =   downcallback
                        else :          callback    =   "scrollTable('" + table_id + "'," + direction + ")"         
                    
                    elif(i==2)  :  
                        image       =   "rightarrow"
                        direction   =   "2"
                        if(addSearch) : callback    =   rightcallback
                        else :          callback    =   "scrollTable('" + table_id + "'," + direction + ")"         

                    else        :  
                        image       =   "leftarrow"
                        direction   =   "3"
                        if(addSearch) : callback    =   leftcallback
                        else :          callback    =   "scrollTable('" + table_id + "'," + direction + ")"         
            
                    arrow_html     =   arrow_html.replace("XXXXimageId",table_id + image + "Id")
                    arrow_html     =   arrow_html.replace("XXXXimage",image)
                    arrow_html     =   arrow_html.replace("XXXXScrollCallback",callback)
                    arrow_html     =   arrow_html.replace("XXXXArrowSize",arrowsize)

                    header_html    =   (header_html + arrow_html)
                
            header_html    =   (header_html + scroll_col_end)
        
        header_html    =   (header_html + scroll_title_row_end)
    
        return(header_html)


    def get_row_indices(self) :
        """
        * -------------------------------------------------------------------------- 
        * function : get the start and end indices for scrollable tables
        * 
        * parms :
        *
        * returns : 
        *  N/A
        * --------------------------------------------------------
        """

        startrowIndex   =   0
        rowcount        =   0
    
        if(self.get_tabletype() == ROW_MAJOR) :
        
            if( (len(self.get_rowList()) >= (self.get_lastrowdisplayed() + self.get_rowspertable())) ) :
                if(self.get_lastrowdisplayed() == -1) :
                    if(len(self.get_rowList()) > self.get_rowspertable()) :
                        rowcount = self.get_rowspertable() 
                    else :
                        rowcount = len(self.get_rowList())
                else : 
                    rowcount = self.get_rowspertable()
            else :
                if(len(self.get_rowList()) == 1) :
                    rowcount = 1
                elif(len(self.get_rowList()) <= self.get_rowspertable()) :
                    rowcount = len(self.get_rowList())
                else :
                    rowcount = (len(self.get_rowList()) - (self.get_lastrowdisplayed() ))
        
            if(self.get_lastrowdisplayed() == -1) :
                startrowIndex = 0
            else :
                startrowIndex = self.get_lastrowdisplayed()
    
        elif(self.get_tabletype() == COLUMN_MAJOR) :
            startrowIndex = 0 
            rowcount = rowcount = len(self.get_rowList())#1

        else :
        
            if(len(self.get_rowList()) < self.get_rowspertable()) :
                rowcount = len(self.get_rowList())
            else :
                rowcount = self.get_rowspertable()
        
        return(startrowIndex, rowcount)


"""
*
* -----------------------------------------------------------------------*
* Common table build helper functions 
* -----------------------------------------------------------------------*
*
"""

def get_hiddens(fid,hiddensList) :
    """
    * -------------------------------------------------------------------------- 
    * function : get hiddens associated with a table
    * 
    * parms :
    *   fid             -   form id - table
    *   hiddensList     -   list of hidden elements 
    *
    * returns : 
    *  N/A
    * --------------------------------------------------------
    """
    
    newHTML = ""
 
    newHTML = (newHTML + new_line + "<div ")
    newHTML = (newHTML + addattribute("id",fid + "hiddens") + ">" )#+ new_line)
       
    for i in range(len(hiddensList)) :
        newHTML = (newHTML + new_line +'    <input type="hidden" ' + 
                     addattribute("id",hiddensList[i][0]) + 
                     addattribute("value",str(hiddensList[i][1])) + 
                     "></input>" + new_line)
           
    newHTML = (newHTML + "</div> ")
    
    return(newHTML)




"""
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
* Dataframe Describe Table components 
* -----------------------------------------------------------------------*
* -----------------------------------------------------------------------*
"""

"""
* -----------------------------------------------------------------------*
* Dataframe Describe Table html 
* -----------------------------------------------------------------------*
"""
mini_table_start = """
                            <div container dc-tbl-container" style='border:0px; """
mini_table_end = """                            </div>
"""

mini_panel_start = """                                <div class="panels panel-primary" style="border:0px;">"""
mini_panel_end   = """                                </div>
"""

mini_panel_heading_start = """
                                    <div class="panel-heading clearfix dc-describe-table-panel-heading" style="background-color: rgb(61, 126, 216);">
                                        <div class="input-group-btn">"""
mini_panel_heading_end = """                                        </div>
                                    </div>"""

mini_panel_title_start = """
                                            <p class="panel-title dc-describe-table-panel-title pull-left">"""

mini_data_table_start = """
                                    <div>
                                        <table class="table">"""
mini_data_table_end = """
                                        </table>
                                    </div>
"""

mini_table_head_start = """
                                            <thead>
                                                <tr class="dc-describe-table-head">
"""
describe_df_table_head_start = """
                                            <thead>
                                                <tr class="dc-describe-table-head">
"""
mini_table_head_end = """                                                </tr>
                                            </thead>"""
                                            
mini_table_head_col_start = """                                                    <th class=" dccolhead dc-describe-table-head-col">"""
describe_df_table_head_col_start = """                                                    <th class=" dccolhead dc-describe-table-head-col">"""

mini_data_table_body_start = """
                                            <tbody>"""
mini_data_table_body_end = """
                                            </tbody>"""

mini_data_table_body_row_start = """
                                                <tr class='dc-describe-table-body-row'>"""
describe_df_table_body_row_start = """
                                                <tr class='dc-describe-table-body-row'>"""
mini_data_table_body_row_end = """
                                                </tr>"""

describe_df_table_body_first_col = """
                                                    <td class="dctablecol dccolwrap dc-describe-table-body-first-col">"""
describe_df_table_body_col = """
                                                    <td class="dctablecol dccolwrap">"""
mini_data_table_body_col = """
                                                    <td class="dctablecol dccolwrap">"""

"""
* -----------------------------------------------------------------------*
* Dataframe Describe Table methods 
* -----------------------------------------------------------------------*
"""
def get_stats_table(title,colnames,colvalues,width=0) : 
    
    stats_HTML  =   ""
    
    if(width==0) :
        stats_HTML  =   (stats_HTML + mini_table_start + "'>" + new_line)
    else :
        stats_HTML  =   (stats_HTML + mini_table_start + addstyleattribute("width",str(width) + "px") + "'>" + new_line)

    stats_HTML  =   (stats_HTML + mini_panel_start)

    stats_HTML  =   (stats_HTML + mini_panel_heading_start)
    stats_HTML  =   (stats_HTML + mini_panel_title_start)
    stats_HTML  =   (stats_HTML + title + "</p>" + new_line)
    stats_HTML  =   (stats_HTML + mini_panel_heading_end)

    stats_HTML  =   (stats_HTML + mini_data_table_start)

    # table head
    stats_HTML  =   (stats_HTML + mini_table_head_start)
    for i in range(len(colnames)) :
        stats_HTML  =   (stats_HTML + mini_table_head_col_start + str(colnames[i]) + "</th>" + new_line)
    stats_HTML  =   (stats_HTML + mini_table_head_end)

    # table body
    stats_HTML  =   (stats_HTML + mini_data_table_body_start)
    stats_HTML  =   (stats_HTML + mini_data_table_body_row_start)   
    for i in range(len(colvalues)) :
        stats_HTML  =   (stats_HTML + mini_data_table_body_col + str(colvalues[i]) + "</td>")   
    stats_HTML  =   (stats_HTML + mini_data_table_body_row_end)

    stats_HTML  =   (stats_HTML + mini_data_table_body_end)
    
    stats_HTML  =   (stats_HTML + mini_data_table_end)
    
    stats_HTML  =   (stats_HTML + mini_panel_end)
    stats_HTML  =   (stats_HTML + mini_table_end)

    return(stats_HTML)
    
"""
* -----------------------------------------------------------------------*
* Dataframe Describe Table methods 
* -----------------------------------------------------------------------*
"""
def get_df_describe_table(df_title,df,rowids,colids,width=0,centered=False) : 

    df_describe_HTML  =   ""
    
    if(width==0) :
        if(centered) :
            df_describe_HTML  =   (df_describe_HTML + mini_table_start + "' align='center' >" + new_line)
        else :
            df_describe_HTML  =   (df_describe_HTML + mini_table_start + "'>" + new_line)
    else :
        if(centered) :
            df_describe_HTML  =   (df_describe_HTML + mini_table_start + addstyleattribute("width",str(width) + "px") + "' align='center' >" + new_line)
        else :
            df_describe_HTML  =   (df_describe_HTML + mini_table_start + addstyleattribute("width",str(width) + "px") + "'>" + new_line)
        
    df_describe_HTML  =   (df_describe_HTML + mini_panel_start)

    df_describe_HTML  =   (df_describe_HTML + mini_panel_heading_start)
    df_describe_HTML  =   (df_describe_HTML + mini_panel_title_start)
    df_describe_HTML  =   (df_describe_HTML + df_title + " dataframe : " +  str(len(df)) + " Rows x " + str(len(df.columns)) + " Columns" + "</p>" + new_line)
    df_describe_HTML  =   (df_describe_HTML + mini_panel_heading_end)

    df_describe_HTML  =   (df_describe_HTML + mini_data_table_start)
    
    # table head
    df_describe_HTML  =   (df_describe_HTML + describe_df_table_head_start)
    
    colnames          =   list(df.columns)
    
    for i in range(len(colids)) :
        if(colids[i] == None) :
            df_describe_HTML  =   (df_describe_HTML + describe_df_table_head_col_start + "........" + "</th>" + new_line) 
        else :
            if(colids[i] == -1) :
                df_describe_HTML  =   (df_describe_HTML + describe_df_table_head_col_start + "row index" + "</th>" + new_line)
            else :
                df_describe_HTML  =   (df_describe_HTML + describe_df_table_head_col_start + str(colnames[colids[i]]) + "</th>" + new_line)
                               
    df_describe_HTML  =   (df_describe_HTML + table_head_end)

    # table body
    df_describe_HTML  =   (df_describe_HTML + mini_data_table_body_start)
    
    for i in range(len(rowids)) :
        df_describe_HTML  =   (df_describe_HTML + describe_df_table_body_row_start)   
        
        for j in range(len(colids)) :
        
            if(j == 0) :
                
                if(rowids[i] == None) :
                    df_describe_HTML  =   (df_describe_HTML + describe_df_table_body_first_col + "........" + "</td>") 
                else :
                    df_describe_HTML  =   (df_describe_HTML + describe_df_table_body_first_col + str(rowids[i]) + "</td>")    
            
            else :
                if(rowids[i] == None) :
                    df_describe_HTML  =   (df_describe_HTML + describe_df_table_body_col + "........" + "</td>")
                else :
                
                    if(colids[j] == None) :
                        df_describe_HTML  =   (df_describe_HTML + describe_df_table_body_col + "........" + "</td>") 
                    else :
                        df_describe_HTML  =   (df_describe_HTML + describe_df_table_body_col + str(df.iloc[rowids[i],colids[j]]) + "</td>")   
            
        df_describe_HTML  =   (df_describe_HTML + mini_data_table_body_row_end)
        
    df_describe_HTML  =   (df_describe_HTML + mini_data_table_body_end)

    
    df_describe_HTML  =   (df_describe_HTML + mini_data_table_end)

    df_describe_HTML  =   (df_describe_HTML + mini_panel_end)
    df_describe_HTML  =   (df_describe_HTML + mini_table_end)

    if(0) :
        print(df_describe_HTML)
        
    return(df_describe_HTML)




