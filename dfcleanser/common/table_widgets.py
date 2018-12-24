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
    
    #print("addattribute",name,value)
    attribute = ""
    attribute = attribute + " " + name + "=" + '"' + str(value) + '"'
    return(attribute)

def addstyleattribute(name,value) :
    
    styleattribute = ""
    styleattribute = styleattribute + " " + name + ":" + value + "; "
    return(styleattribute)

def strip_leading_blanks(instr) :
    
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
SCROLL_NEXT         =   0
SCROLL_PREVIOUS     =   1

ROW_MAJOR           =   0
COLUMN_MAJOR        =   1
MULTIPLE            =   2



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
<div class='container dc-tbl-container'"""

table_container_middle = """
    <div class="row">
        <div class="panel panel-primary" """
        
table_container_end = """
        </div>
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
            <div class="panel-heading clearfix dc-small-table-panel-heading" height="30px" style=" margin-bottom:0px;" """
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

table_title_start = """                      <p class="dc-table-title pull-left" """
table_title_end = """</p>
"""

table_more_div_start = """                    <div class="input-group-btn dc-table-input-group-btn dc-scroll-div">
"""
table_short_more_div_start = """                    <div class="input-group-btn dc-table-title" style="padding-right:0px; padding-left:2%;" >
"""

table_more_div_end = """                    </div>
"""

table_next_start = """                        <button class="btn btn-primary moreNext" id="moreNext" """
search_table_next_start = """                        <button class="btn btn-primary search-moreNext" id="moreNext" """
table_next_end   = """>Next</button>
"""

table_prev_start = """                        <button class="btn btn-primary morePrev" id="morePrev" """
search_table_prev_start = """                        <button class="btn btn-primary search-morePrev" id="morePrev" """
table_prev_end   = """>Previous</button>
"""

table_short_next_start = """                        <button class="btn btn-primary" """
table_short_next_end   = """>+</button>
"""

table_short_prev_start        = """                        <button class="btn btn-primary" """
table_short_prev_end          = """>-</button>
"""

table_short_button_end = """                        </button>
"""

table_note_start = """<div class="table-note">
    <p class="search-table-note" """
table_note_end   = """</div>
"""                     
                
table_start = """
             <table class="table dc-table" """
table_start13 = """
             <table class="table dc-table13" """
             
table_end = """
             </table>
            </div>"""

table_head_start = """                <thead>
"""
table_head_end = """
                </thead>"""

table_head_row_start = """                    <tr style='background-color:#95C0FB; color:#262729;'>
"""
table_color_head_row_start = """                    <tr style='background-color:#95C0FB'>
"""

table_head_row_end = """                    </tr>"""

table_body_start = """
                <tbody>
"""
table_body_end = """                </tbody>"""

table_body_row_start = """                    <tr class="dc-table-row" >
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
*    basic dcTable variants 
* -----------------------------------------------------------------------*
"""

"""
* -----------------------------------------------------------------------*
*  A mult_table is a set of tables stacked like sheets with only one
*  displayed at a time
* -----------------------------------------------------------------------*
*   
*   table           -   dcTable object
*   direction       -   direction to scroll in 
*   displayTable    -   display the html flag  
* -----------------------------------------------------------------------*
"""
def get_mult_table(table,direction,displayTable=True) :

    if(direction == SCROLL_NEXT) :
        table.set_lasttabledisplayed(table.get_lasttabledisplayed()+1)    
    elif(direction == SCROLL_PREVIOUS) :
        table.set_lasttabledisplayed(table.get_lasttabledisplayed()-1)    

    temp_table = dcTable(table.get_title(),"tempmulttable",
                         table.get_owner(),
                         table.get_headerList()[table.get_lasttabledisplayed()],
                         table.get_rowList()[table.get_lasttabledisplayed()],
                         table.get_widthList()[table.get_lasttabledisplayed()],
                         table.get_alignList()[table.get_lasttabledisplayed()])
    
    temp_table.set_tableid(table.get_tableid())
    temp_table.set_tabletype(table.get_tabletype())
    if( ( not (table.get_refList() == None)) and (len(table.get_refList())>0) ) :
        temp_table.set_refList(table.get_refList()[table.get_lasttabledisplayed()])
    temp_table.set_hhrefList(table.get_hhrefList()[table.get_lasttabledisplayed()])
    temp_table.set_refParm(table.get_refParm())
    
    # MULTIPLE specific 
    temp_table.set_numtables(table.get_numtables())
    temp_table.set_lasttabledisplayed(table.get_lasttabledisplayed())
    temp_table.set_rowspertable(table.get_rowspertable())
    temp_table.set_note(table.get_note())
    
    if(not(displayTable)) :
        table_HTML = temp_table.get_html(False)
        drop_table_value("tempmulttable")
        return(table_HTML)
    else :
        temp_table.display_table() 
        drop_table_value("tempmulttable")
        
"""
* -----------------------------------------------------------------------*
*  A row_major_table is a single table that displays a subset of rows 
*  at a time
* -----------------------------------------------------------------------*
*   table           -   dcTable object
*   direction       -   direction to scroll in 
*   displayTable    -   display the html flag  
* -----------------------------------------------------------------------*
"""
def get_row_major_table(table,direction,displayTable=True) :

    if(not(displayTable)) :
        
        if(direction == SCROLL_PREVIOUS) :
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
*  A col_major_table is a single table that displays a subset of cols 
*  at a time
* -----------------------------------------------------------------------*
*   table           -   dcTable object
*   direction       -   direction to scroll in 
*   displayTable    -   display the html flag  
* -----------------------------------------------------------------------*
"""
def get_col_major_table(table,direction,displayTable=True) :

    if(not(displayTable)) :
        
        if(direction == SCROLL_PREVIOUS) :
            numinlasttable = table.get_lastcoldisplayed() % table.get_colsperrow()
            if(numinlasttable > 0) :
                colstart = table.get_lastcoldisplayed() - (numinlasttable+table.get_colsperrow())
            else :
                colstart = table.get_lastcoldisplayed() - (2*table.get_colsperrow())
                
            if(colstart < 0) :
                colstart = -1
            
            table.set_lastcoldisplayed(colstart)
            
        else :
            if( table.get_lastcoldisplayed() == len(table.get_rowList()) ) :
                table.set_lastcoldisplayed(-1)
            else :
                table.set_lastcoldisplayed(table.get_lastcoldisplayed() + table.get_colsperrow()) 
        
        from dfcleanser.common.cfg import get_dfc_dataframe 
        from dfcleanser.common.display_utils import get_df_schema_table
        if(table.get_tableid() == "dfschemaTable") :
            get_df_schema_table(get_dfc_dataframe(),table,direction)    
            
        table_HTML = table.get_html(False)
        
        return(table_HTML)
        
    else :
        table.display_table() 

        
"""
* -----------------------------------------------------------------------*
* class for defining dataframe cleanser html based tables 
* -----------------------------------------------------------------------*
"""
"""
*
*   ATTRIBUTES
*
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
*   tabletype           -   table type (ROW_MAJOR, COLUMN_MAJOR, MULTIPLE) 
*   colsperrow          -   number of columns per row
*   rowspertable        -   number of rows per table
*   maxtables           -   max tables in MULTIPLE table
*   lastrowdisplayed    -   last row displayed in ROW_MAJOR table
*   numtables           -   number of MULTIPLE tables generated 
*   lasttabledisplayed  -   last MULTIPLE table displayed
*   searchable          -   flag to make table searchable
*   searchtext          -   text for search box
*   searchcallback      -   search callback function
*   color               -   flag to make table colored
*   colorList           -   list of colors for each column 
*   border              -   flag to draw border
*   small               -   flag to make table small
*   smallwidth          -   small table width in percent
*   smallmargin         -   small table lefty margin
*   smallfsize          -   small table font size
*   shorthead           -   list of colors for each column 
*   shortrow            -   flag to draw border
*   note                -   note below table
*   checkLength         -   flag to check <th> and <tr> lengths and use popover
*   firstcolpadding     -   list of left padding for first column in rows
*
"""

class dcTable :

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

        # attributes for multiple table type tables    
        self.numtables            =   0
        self.lasttabledisplayed   =   -1
        
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
        self.smallwidth      =   92
        self.smallmargin     =   40
        self.smallfsize      =   12
        self.smallheader     =   True
        
        self.shorthead       =   True
        self.shortrow        =   True

        self.note            =   ""
        
        self.checkLength     =   True
        self.textLength      =   maxRowElement

        # add the table to internal dict for later retrieval    
        if(get_table_value(self.tableid)==None) :
            set_table_value(self.tableid,self)
        else :
            drop_table_value(self.tableid)
            set_table_value(self.tableid,self)
        
    # class setters
    def set_title(self,titleParm) :
        self.title = titleParm
    def set_tableid(self,tableidParm) :
        self.tableid = tableidParm
    def set_owner(self,ownerParm) :
        self.owner = ownerParm

    
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
       
    # attributes for multiple table type tables    
    def set_numtables(self,numtablesParm) :
        self.numtables                  =   numtablesParm
    def set_lasttabledisplayed(self,lasttabledisplayedParm) :
        self.lasttabledisplayed         =   lasttabledisplayedParm
    
    # attributes for row major table 
    def set_lastcoldisplayed(self,lastcoldisplayedParm) :
        self.lastcoldisplayed         =   lastcoldisplayedParm
    def set_maxcolumns(self,maxcolumnsParm) :
        self.maxcolumns         =   maxcolumnsParm
    def set_colscrollcallback(self,callbackparm) :
        self.colscrollcallback        =   callbackparm 
        
    # attributes for search table     
    def set_searchable(self,searchableParm) :
        self.searchable = searchableParm
    def set_searchParms(self,searchParms) :
        self.searchParms = searchParms
    def set_searchRow(self,rowParm) :
        self.searchRow = rowParm
    def set_searchCol(self,colParm) :
        self.searchCol = colParm

    # attributes for color table     
    def set_color(self,colorParm) :
        self.color           =   colorParm
    def set_colorList(self,colorListParm) :
        self.colorList       =   colorListParm
    
    def set_border(self,borderParm) :
        self.border          =   borderParm
        
    # attributes for small table
    def set_small(self,smallParm) :
        self.small           =   smallParm
    def set_smallwidth(self,smallwidthParm) :
        self.smallwidth       =   smallwidthParm
    def set_smallmargin(self,smallmarginParm) :
        self.smallmargin       =   smallmarginParm
    def set_smallfsize(self,smallfsizeParm) :
        self.smallfsize       =   smallfsizeParm
    def set_smallheader(self,smallheaderParm) :
        self.smallheader       =   smallheaderParm

    def set_shorthead(self,shortheadParm) :
        self.shorthead       =   shortheadParm
    def set_shortrow(self,shortrowParm) :
        self.shortrow        =   shortrowParm
     
    def set_note(self,noteParm) :
        self.note           =   noteParm

    def set_checkLength(self,checkLengthParm) :
        self.checkLength    =   checkLengthParm
    def set_textLength(self,textLengthParm) :
        self.textLength    =   textLengthParm
        
    def set_html_only(self,html_onlyParm) :    
        self.html_only       =   html_onlyParm
    
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
        
    def get_numtables(self) :
        return(self.numtables)
    def get_lasttabledisplayed(self) :
        return(self.lasttabledisplayed)
    
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
    def get_smallfsize(self) :
        return(self.smallfsize)
    def get_smallheader(self) :
        return(self.smallheader)
    
    def get_shorthead(self) :
        return(self.shorthead)
    def get_shortrow(self) :
        return(self.shortrow) 
        
    def get_note(self) :
        return(self.note)
    
    def get_checkLength(self) :
        return(self.checkLength)
    def get_textLength(self) :
        return(self.textLength)
    
    def get_firstcolpadding(self) :
        return(self.firstcolpadding)
    def set_firstcolpadding(self,setParm) :
        self.firstcolpadding = setParm

    def get_html(self,fulltable=True) :
        
        more = False
        prev = False
    
        more, prev = get_table_scrolls(self)
    
        tableHTML = ""
    
        if(self.get_searchable()) :
            tableHTML = (tableHTML + get_search_table_header(self,fulltable))
        else :
            tableHTML = (tableHTML + get_non_search_table_header(self,more,prev,fulltable))

        if(self.get_small()) :
            if(self.get_smallfsize() == 13) :
                tableHTML = (tableHTML + table_start13)
            else :
                tableHTML = (tableHTML + table_start)
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
                tableHTML = (tableHTML + table_color_head_row_start)
            else :
                tableHTML = (tableHTML + table_head_row_start)
    
            try :

                for i in range(len(self.get_headerList())) :
                    if(self.get_hhrefList() == None) :

                        tableHTML = (tableHTML + add_table_head_column(self,
                                                                       self.get_headerList()[i],
                                                                       self.get_widthList()[i],
                                                                       self.get_alignList()[i]))
            
                    elif( (self.get_hhrefList()[i] == None) or (len(self.get_headerList()[i]) == 0) ) :

                        tableHTML = (tableHTML + add_table_head_column(self,
                                                                       self.get_headerList()[i],
                                                                       self.get_widthList()[i],
                                                                       self.get_alignList()[i]))
                    
                    else : 

                        tableHTML = (tableHTML + add_table_head_column(self,
                                                                       self.get_headerList()[i],
                                                                       self.get_widthList()[i],
                                                                       self.get_alignList()[i],
                                                                       self.get_hhrefList()[i]) )
                    
                    if(i != (len(self.get_headerList())) - 1) : #table.get_colsperrow()-1)):#len(table.get_headerList()) - 1) ) :
                        tableHTML = (tableHTML + new_line)
            except :
                print("Header Error i = ",i)
                print(self.get_headerList())
                print(self.get_widthList())
                print(self.get_alignList())
                print(self.get_hhrefList())
            
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
    
        startrowIndex, rowcount = get_row_indices(self)
    
        for i in range(startrowIndex, (startrowIndex + rowcount)) :
        
            if(self.get_refList() == None) :
                tableHTML = (tableHTML + add_table_body_row(self,i,
                                                            self.get_rowList()[i],
                                                            self.get_refList()))
            else :
                if(type(self.get_refList()[0]) == list) :
                    tableHTML = (tableHTML + add_table_body_row(self,i,
                                                                self.get_rowList()[i],
                                                                self.get_refList()[i])) 
                else :
                    tableHTML = (tableHTML + add_table_body_row(self,i,
                                                                self.get_rowList()[i],
                                                                self.get_refList()))

        tableHTML = (tableHTML + table_body_end)
        tableHTML = (tableHTML + table_end)
    
        if(fulltable) :
            tableHTML = (tableHTML + table_container_end)
        
            if(len(self.get_note()) > 0 ) :
                tableHTML = (tableHTML + table_note_start)
                tableHTML = (tableHTML + addattribute("id",self.get_tableid()+"note") + ">" + new_line)
                tableHTML = (tableHTML + self.get_note() + "</p>" + new_line)
                tableHTML = (tableHTML + table_note_end)
            
            tableHTML = (tableHTML + table_container_end1)
        
        else :
            tableHTML = (tableHTML + table_nd_container_end)
        
            if(len(self.get_note()) > 0 ) :
                tableHTML = (tableHTML + table_note_start)
                tableHTML = (tableHTML + self.get_note() + "</p>" + new_line)
                tableHTML = (tableHTML + table_note_end)
            
            tableHTML = (tableHTML + table_nd_container_end1)
    
        if(fulltable) :
            tableHTML = (tableHTML + table_form_end)
        else :
            tableHTML = (tableHTML + table_form_end)

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
        if(self.get_title() != None)  :  
            if( (self.get_title() == "@Geocoders") or ("#Geocoder Parms" in self.get_title()) ) :   
               print(tableHTML)
               
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
                    if(len(str(self.get_rowList()[i])) > 50) :
                        print("   Row ["+str(i) + "] : ",len(self.get_rowList()[i])) 
                    else :
                        print("   Row ["+str(i) + "] : ",self.get_rowList()[i])
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
                    print("   Ref ["+str(i) + "] : ",self.get_refList()[i])
            else :
                print("   Ref ["+str(i) + "] : ",self.get_refList())
        
        if(self.get_hhrefList() == None) :
            print(" hhrefs      :  None")
        else :
            print(" hhrefs      : ",self.get_hhrefList())

        if(self.get_color() == True) :
            print(" Colors      : [",len(self.get_colorList()),"]")
            for i in range(len(self.get_colorList())) :
                print("   Color ["+str(i) + "] : ",self.get_colorList()[i])
   
        if(self.get_searchable()) :
            print("\n searchable  : ",self.get_searchable())
            print(" searchParms  : \n",self.get_searchParms())
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
        elif(self.get_tabletype() == MULTIPLE) :
            print("\nMULTIPLE Parms :")
            print("\n numtables         : ",self.get_numtables())
            print(" lasttabledisplayed : ",self.get_lasttabledisplayed(),"\n")

        if(self.get_small()) :
            print("\n smallwidth     : ",self.get_smallwidth())
            print(" smallmargin    : ",self.get_smallmargin())
            print(" smallfsize     : ",self.get_smallfsize())

        if(self.get_shorthead()) :
            print(" shorthead      : ",self.get_shorthead())
        if(self.get_shortrow()) :
            print(" shortrow       : ",self.get_shortrow())

        if(not(self.get_note() == "")) :
            print("\nnote           : ",self.get_note())
            
        print(" textlength     : ",self.get_textLength())



"""
*
* -----------------------------------------------------------------------*
* Common table build helper functions 
* -----------------------------------------------------------------------*
*
"""

"""
* -----------------------------------------------------------------------*
* add callback function to table item 
*   
*   table           -   dcTable object
*   direction       -   direction to scroll in 
*   displayTable    -   display the html flag  
* -----------------------------------------------------------------------*
"""
def add_callback_to_item(table,rowflag,value,func,parm=None) :
    
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
        if(table.get_checkLength() == True) :
            newstrvalue = newstrvalue.replace("&nbsp;","")
        
        if(len(newstrvalue) > maxRowElement) :
            
            if(valueIsstring):
                item_html = (item_html + '<a href="#" style="text-decoration:none;" onclick="' + func + "(" + 
                             "'" + strip_leading_blanks(strvalue) + "'" +  cparm + ')"' + 
                             ' data-toggle="tooltip" data-placement="top" title="' + 
                             strip_leading_blanks(strvalue) + '">' + shorten_element(table,newstrvalue,rowflag) + "</a>")
            else :
                item_html = (item_html + '<a href="#" style="text-decoration:none;" onclick="' + func + "(" + 
                             strip_leading_blanks(strvalue) + cparm + ')"' + 
                             ' data-toggle="tooltip" data-placement="top" title="' +
                             strip_leading_blanks(strvalue) + '">' + shorten_element(table,newstrvalue,rowflag) + "</a>")
                
        else : 
            
            if(valueIsstring):
                item_html = (item_html + '<a href="#"style="text-decoration:none;" onclick="' + func + "(" + 
                             "'" + strip_leading_blanks(strvalue) + "'" +  cparm + ')">' + strvalue + "</a>")
            else :
                item_html = (item_html + '<a href="#"style="text-decoration:none;" onclick="' + func + "(" + 
                             strip_leading_blanks(strvalue) + cparm + ')">' + strvalue + "</a>")
            
    else :  

        if(valueIsstring):
            item_html = (item_html + '<a href="#"style="text-decoration:none;" onclick="' + func + "(" + 
                         "'" + rowindex + "'" +  cparm + ')">' + strvalue + "</a>")
        else :
            item_html = (item_html + '<a href="#"style="text-decoration:none;" onclick="' + func + "(" + 
                         rowindex + cparm + ')">' + strvalue + "</a>")

        
    return(item_html)

"""
* -----------------------------------------------------------------------*
* add table column header 
*
*   table           -   dcTable object
*   coltext         -   text to display in column header 
*   width           -   width in pixels  
*   align           -   text alignment ("left" : default "center") 
*   href            -   call hrefon click
* -----------------------------------------------------------------------*
"""
def add_table_head_column(table,coltext,width,align,href=None) :

    colHTML = ""
    colHTML = (colHTML + "                      <th" + 
               addattribute("style",addstyleattribute("width", str(width)+"%")) )

    if( align == "left") :
        colHTML = (colHTML + addattribute("class"," dccolhead dccolleft")) 
    else :
        colHTML = (colHTML + addattribute("class"," dccolhead")) 
    
    
    if(href == None) :
        colHTML = (colHTML + ">" + coltext + "</th>")
    else :
        if(len(coltext) > 0) :
            colHTML = (colHTML + ">" + add_callback_to_item(table,False,coltext,href) + "</th>")

    return(colHTML)

"""
* -----------------------------------------------------------------------*
* table item shorten and put pop up around 
*
*   table           -   dcTable object
*   element         -   text to check on 
*   row             -   row flag or headerflag 
* -----------------------------------------------------------------------*
"""
def shorten_element(table,element,row=True) :
    
    if(not table.get_checkLength()) :
        return(element)
        
    if(row) :
        if(not table.get_shortrow()) :
            return(element)
    else :
        if(not table.get_shorthead()) :
            return(element)  
            
    if(len(element) > table.get_textLength()) :
        halflength = int(table.get_textLength()/2)
        if(0):#element.find(",") > -1) :
            shortelement = element
        else :
            shortelement = element[0:halflength] + "...." + element[(len(element)-halflength) : (len(element))]
    else :
        shortelement = element
        
    return(shortelement)

"""
* -----------------------------------------------------------------------*
* get individual row element
*
*   table           -   dcTable object
*   rowElement      -   row element (column) 
* -----------------------------------------------------------------------*
"""
def get_row_element(table,rowElement) :
    
    rowHtml = ""
    
    if(type(rowElement) == str) :
        
        # check for length of element
        newrowElement = rowElement.replace("<b>","")
        newrowElement = newrowElement.replace("</b>","")
        newrowElement = newrowElement.replace("&nbsp;","")
        
        if(not table.get_checkLength()) :
            rowHtml = rowElement
        else :
            if(len(newrowElement) > table.get_textLength()) :
                if(newrowElement.find(",") > -1) :
                    rowHtml = rowElement 
                else :
                    rowHtml = ('<a href="#" data-toggle="tooltip" data-placement="top" title="' +  
                               newrowElement + '">' + shorten_element(table,newrowElement) + '</a>')
            else :
                rowHtml = rowElement
    else :
        rowHtml = rowElement

    return(rowHtml)

"""
* -----------------------------------------------------------------------*
* add table body row
*
*   table           -   dcTable object
*   index           -   row index 
*   rowElement      -   row element (column) 
*   href            -   anchor 
* -----------------------------------------------------------------------*
"""
def add_table_body_row(table,index,rowElement,href) :
    
    rowHTML = ""
    
    rowHTML = (rowHTML + table_body_row_start)

    if(table.get_color()) :
        tablecolorlist = table.get_colorList()[index]

    for i in range(len(rowElement)) : 
        
        if(table.get_color()) :

            if(tablecolorlist[i] == None) :
                rowHTML = (rowHTML + "                        <td" + 
                           addattribute("style",addstyleattribute("width", str(table.get_widthList()[i])+"%")))
            else :
                rowHTML = (rowHTML + "                        <td" + 
                           addattribute("bgcolor",tablecolorlist[i]) + 
                           addattribute("style",addstyleattribute("width", str(table.get_widthList()[i])+"%")))
        else :
            rowHTML = (rowHTML + "                        <td" + 
                       addattribute("style",addstyleattribute("width", str(table.get_widthList()[i])+"%")))
        
        if( table.get_alignList()[i] == "left") :    
            rowHTML = (rowHTML + addattribute("class","dccolleft dctablecol dccolwrap")) 
        else :    
            rowHTML = (rowHTML + addattribute("class","dctablecol dccolwrap")) 
 
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
                rowHTML = (rowHTML + ">" + str(get_row_element(table,rowElement[i])) + "</td>")
                
        elif(href[i] == None) :
            rowHTML = (rowHTML + ">" + str(get_row_element(table,rowElement[i])) + "</td>")
        else :
            if(table.get_buttonList() == None) :
                if(table.get_refIndex() == -1) :
                
                    if(len(str(rowElement[i])) > 0) :
                        rowHTML = (rowHTML + ">" + add_callback_to_item(table,True,
                                                                        rowElement[i],
                                                                        href[i],
                                                                        table.get_refParm()) + "</td>")
                    else :
                        rowHTML = (rowHTML + ">"  + "</td>")
                else :
                    rowHTML = (rowHTML + ">" + add_callback_to_item(table,True,
                                                                    [(table.get_refIndex()+index),
                                                                     rowElement[i]],
                                                                     href[i],
                                                                     table.get_refParm()) + "</td>")
                    
            else :
                if(not (table.get_buttonList()[index][i] == None)) :
                    rowHTML = (rowHTML + ">")
                    rowHTML = (rowHTML + table_button_div_start)
                    rowHTML = (rowHTML + table_button_start)
                    rowHTML = (rowHTML + addattribute("id",table.get_tableid()+str(rowElement[i]) + "button"))
                    rowHTML = (rowHTML + addattribute("OnClick",href[i]+"('"+ str(i) +"')") )
                    rowHTML = (rowHTML + ">" + str(rowElement[i]))
                    rowHTML = (rowHTML + table_button_end)
                    rowHTML = (rowHTML + table_button_div_end)

        if(i != (len(rowElement) - 1)) :
            rowHTML = (rowHTML + new_line)    
        
    rowHTML = (rowHTML + table_body_row_end)

    return(rowHTML)

"""
* -----------------------------------------------------------------------*
* get table start container wrapper
*
*   table           -   dcTable object
*   tableDisplay    -   display table flag 
* -----------------------------------------------------------------------*
"""
def get_table_container_start(table,tableDisplay=True) :

    tableHTML = ""

    if(table.get_small()) :
        tableHTML = (tableHTML + new_line + '<div class="container dc-table-container" ')
        tableHTML = (tableHTML + addattribute("id",table.get_tableid() + "Container"))
        tableHTML = (tableHTML + ' style="width:' + str(table.get_smallwidth()) + '%;' + 
                                 ' margin-left:' + str(table.get_smallmargin()) + 'px;">' + new_line)
        tableHTML = (tableHTML  + '    <div class="row">' + new_line)
        if(table.get_border()) :
            tableHTML = (tableHTML  + '        <div class="panel panel-primary" ' + ">")
        else :
            tableHTML = (tableHTML  + '        <div class="panel panel-primary" style="border:0px;"' + ">")
    else :
        if(tableDisplay) :
            tableHTML = (tableHTML + table_container_start)
            tableHTML = (tableHTML + addattribute("id",table.get_tableid()+"container")  + ">")
        
        tableHTML = (tableHTML + table_container_middle + ">")
    
    return(tableHTML)



"""
*
* -----------------------------------------------------------------------*
* common searching table helper functions
* -----------------------------------------------------------------------*
*
"""

"""
* -----------------------------------------------------------------------*
* Search Table html 
* -----------------------------------------------------------------------*
"""
search_table_header_start = """
            <div class="panel-heading clearfix dc-table-panel-heading">
"""
search_table_input_start             = """                        <input type="text" class='form-control dc-form-search-more-input'"""
search_table_button_div_start        = """                    <div class="input-group-btn" style='margin-left:2%; '>
"""

search_table_title_start             = """                        <p class="panel-title dc-search-panel-title pull-left" style="padding-right:20px">"""
search_table_title_end               = """</p>
"""

search_table_search_button_start     = """                        <button class='btn btn-primary dc-btn-primary' """
search_table_button_glyph            = """                          <i class='glyphicon glyphicon-search'"""
search_table_button_glyph_end        = """></i>
"""
search_table_search_button_end       = """                        </button>
                      </div>
"""

search_dir_table_input_div_start = """                    <div class="input-group-btn">
"""
search_dir_table_input_div_end   = """                    </div>
"""

search_dir_table_button_div_start = """                      <div class="input-group-btn" style="padding-right:0px; padding-left:0px">
"""
search_dir_table_button_div_start1= """                      <div class="input-group-btn" align="right" style="margin-right:1%;">
"""
search_dir_table_button_div_end   = """                      </div>
"""
search_table_button_start         = """                        <button class='btn btn-primary'"""
search_table_button_img_start     = """                          <img src='"""
search_table_button_end           = """                        </button>
"""

"""
* -----------------------------------------------------------------------*
* Search Table helper functions
* -----------------------------------------------------------------------*
"""
"""
* -----------------------------------------------------------------------*
* get searchable table buttons
*
*   table           -   dcTable object
*   searchParms     -   search parameters
*   direction       -   button direction 
* -----------------------------------------------------------------------*
"""                                                                                                                                                
def get_search_table_button(table,searchParms,direction) : 
    
    if(direction == 0) : 
        imgname     =   "https://rickkrasinski.github.io/dfcleanser/graphics/uparrow.png"
        imgid       =   "uparrowimg"
        callback    =   table.get_searchParms().get("upcallback")
        
    elif(direction == 1) : 
        imgname     =   "https://rickkrasinski.github.io/dfcleanser/graphics/downarrow.png"
        imgid       =   "downarrowimg"
        callback    =   table.get_searchParms().get("downcallback")
        
    elif(direction == 2) : 
        imgname     =   "https://rickkrasinski.github.io/dfcleanser/graphics/leftarrow.png"
        imgid       =   "leftarrowimg"
        callback    =   table.get_searchParms().get("morecallback")
        
    elif(direction == 3) : 
        imgname     =   "https://rickkrasinski.github.io/dfcleanser/graphics/rightarrow.png"
        imgid       =   "rightarrowimg"
        callback    =   table.get_searchParms().get("prevcallback")
    
    button_html = ""
    button_html = (button_html + search_table_button_start + ' OnClick="' + callback + '">' + new_line) 
    button_html = (button_html + search_table_button_img_start)
    button_html = (button_html + imgname + "'")
    button_html = (button_html + addattribute("height","20px"))
    button_html = (button_html + addattribute("width","20px"))
    button_html = (button_html + addattribute("id",(table.get_tableid() + imgid)) + "></img>" + new_line)
    button_html = (button_html + search_table_button_end) 
    
    return(button_html)

"""
* -----------------------------------------------------------------------*
* get search table header 
*
*   table           -   dcTable object
*   tableDisplay    -   display table flag 
* -----------------------------------------------------------------------*
"""
def get_search_table_header(table,fulltable) : 

    tableHTML = ""
    
    if(fulltable) :
        tableHTML = (tableHTML + table_form_start)
        tableHTML = (tableHTML + addattribute("id",table.get_tableid()+"form") + ">")
    else :
        tableHTML = (tableHTML + "<div>" + new_line)
    
    if(table.get_hiddensList() != None) :
        tableHTML = (tableHTML + get_hiddens(table.get_tableid(),table.get_hiddensList()))
    
    tableHTML = (tableHTML + get_table_container_start(table))

    tableHTML = (tableHTML + search_table_header_start)
    tableHTML = (tableHTML + table_input_group_start)
    
    if(table.get_title() != None) :
        
        tableHTML = (tableHTML + search_dir_table_input_div_start)
        tableHTML = (tableHTML + "  " + search_dir_table_input_div_start)
        tableHTML = (tableHTML + search_table_title_start + table.get_title() + table_title_end)
        tableHTML = (tableHTML + "  " + search_dir_table_input_div_end)
        

        if(not (table.get_searchParms() == None) ) :
            
            searchParms = table.get_searchParms()
            
            tableHTML = (tableHTML + "  " + search_dir_table_input_div_start)
            tableHTML = (tableHTML + search_table_input_start)
            tableHTML = (tableHTML + addattribute("size",str(searchParms.get("searchsize")))) 
            tableHTML = (tableHTML + "style='" + addstyleattribute("height",
                                                                   (str(searchParms.get("searchheight")) +"px")) )
            tableHTML = (tableHTML +             addstyleattribute("width",
                                                                   (str(searchParms.get("searchwidth")) + "px")) + "' ")
            tableHTML = (tableHTML + addattribute("id",table.get_tableid()+"InputId"))
            tableHTML = (tableHTML + addattribute("placeholder",searchParms.get("searchtext")) + "</input>" + new_line)
            tableHTML = (tableHTML + "  " + search_dir_table_input_div_end)
            
            tableHTML = (tableHTML + search_dir_table_button_div_start)
            tableHTML = (tableHTML + search_table_search_button_start)
            tableHTML = (tableHTML + addattribute("OnClick",str(searchParms.get("searchcallback"))) + ">" + new_line) 
            tableHTML = (tableHTML + search_table_button_glyph)
            tableHTML = (tableHTML + addattribute("id",(table.get_tableid()+"searchglyph")) )
            tableHTML = (tableHTML + search_table_button_glyph_end)
            tableHTML = (tableHTML + " " + search_table_search_button_end)
            tableHTML = (tableHTML + " " + search_dir_table_input_div_end)
            

            if( (searchParms.get("upflag")) or (searchParms.get("downflag")) or 
                (searchParms.get("moreflag")) or (searchParms.get("prevflag")) ) :
                
                tableHTML = (tableHTML + search_dir_table_button_div_start1)
                
                if( searchParms.get("upflag")) :
                    tableHTML = (tableHTML + get_search_table_button(table,searchParms,0))
                
                if( searchParms.get("downflag")) :
                    tableHTML = (tableHTML + get_search_table_button(table,searchParms,1))

                if( searchParms.get("moreflag")) :
                    tableHTML = (tableHTML + get_search_table_button(table,searchParms,2))

                if( searchParms.get("prevflag")) :
                    tableHTML = (tableHTML + get_search_table_button(table,searchParms,3))
                    
                tableHTML = (tableHTML + search_dir_table_button_div_end)
                    
        
    tableHTML = (tableHTML + table_input_group_end)
    tableHTML = (tableHTML + table_header_end) 
    
    return(tableHTML)

"""
* -----------------------------------------------------------------------*
* get non search table header 
*
*   table           -   dcTable object
*   more            -   more flag
*   prev            -   previous flag
*   tableDisplay    -   display table flag 
* -----------------------------------------------------------------------*
"""
def get_non_search_table_header(table,more,prev,fulltable) : 

    tableHTML = ""

    if(fulltable) :
        tableHTML = (tableHTML + table_form_start)
        tableHTML = (tableHTML + addattribute("id",table.get_tableid()+"form") + ">")
    
    if(table.get_hiddensList() != None) :
        tableHTML = (tableHTML + get_hiddens(table.get_tableid(),table.get_hiddensList()))
        
    tableHTML = (tableHTML + get_table_container_start(table))
        
    if(table.get_small()) :
        if(table.get_smallheader()) :
            tableHTML = (tableHTML + small_table_header_start + addattribute("id",table.get_tableid()+"PanelHeading") + ">" + new_line) 
        else :
            tableHTML = (tableHTML + small_table_no_header_start + addattribute("id",table.get_tableid()+"PanelHeading") + ">" + new_line)
    else :
        tableHTML = (tableHTML + table_header_start)

    tableHTML = (tableHTML + table_input_group_start)
    
    if(table.get_title() != None) :
        if(table.get_small()) :
            tableHTML = (tableHTML + table_title_short_div_start)
            tableHTML = (tableHTML + table_title_start + addattribute("id",table.get_tableid()+"Title") + ">" + table.get_title() + table_title_end)
            tableHTML = (tableHTML + table_title_div_end)
        else :
            tableHTML = (tableHTML + table_title_start + addattribute("id",table.get_tableid()+"Title") + ">" +table.get_title() + table_title_end)

    if( (more) or (prev) ) :  

        if(table.get_small()) :
            # for small tables auto both buttons
            tableHTML = (tableHTML + table_short_more_div_start)
            
            # add more button image
            tableHTML = (tableHTML + table_short_next_start)
            tableHTML = (tableHTML + addattribute("OnClick",("scrollTable("+ "'"+table.get_tableid()+"',0" + ")")))
            tableHTML = (tableHTML + ">" + new_line)
            tableHTML = (tableHTML + search_table_button_img_start + "https://rickkrasinski.github.io/dfcleanser/graphics/downarrow.png'")
            tableHTML = (tableHTML + addattribute("id","downarrowId"))
            tableHTML = (tableHTML + addattribute("height","15px") + addattribute("width","15px") + "></img>" + new_line)
            tableHTML = (tableHTML + table_short_button_end)
            
            # add more button image
            tableHTML = (tableHTML + table_short_prev_start)
            tableHTML = (tableHTML + addattribute("OnClick",("scrollTable("+ "'"+table.get_tableid()+"',1" + ")")))
            tableHTML = (tableHTML + ">" + new_line)
            tableHTML = (tableHTML + search_table_button_img_start + "https://rickkrasinski.github.io/dfcleanser/graphics/uparrow.png'")
            tableHTML = (tableHTML + addattribute("id","uparrowId"))
            tableHTML = (tableHTML + addattribute("height","15px") + addattribute("width","15px") + "></img>" + new_line)
            tableHTML = (tableHTML + table_short_button_end)
            
            
        else :
            tableHTML = (tableHTML + table_more_div_start)
            
            if(more) :
                tableHTML = (tableHTML + table_next_start)
                tableHTML = (tableHTML + addattribute("OnClick",("scrollTable("+ "'"+table.get_tableid()+"',0" + ")")))
                tableHTML = (tableHTML + table_next_end)
        
            if(prev) :
                tableHTML = (tableHTML + table_prev_start)
                tableHTML = (tableHTML + addattribute("OnClick",("scrollTable("+ "'"+table.get_tableid()+"',1" + ")")))
                tableHTML = (tableHTML + table_prev_end)
        
        tableHTML = (tableHTML + table_more_div_end)
    
    #if(table.get_small()) :
        #tableHTML = (tableHTML + table_input_group_end) 
        
    tableHTML = (tableHTML + table_input_group_end)
    tableHTML = (tableHTML + table_header_end) 

    return(tableHTML)


"""
*
* -----------------------------------------------------------------------*
* common table scrolling helper functions
* -----------------------------------------------------------------------*
*
"""

"""
* -----------------------------------------------------------------------*
* determine if table needs scroll buttons defined and included
* -----------------------------------------------------------------------*
*   table           -   table object
* -----------------------------------------------------------------------*
"""
def get_table_scrolls(table) :
    
    more = False
    prev = False
    
    if( (table.get_tabletype() == MULTIPLE) and (table.get_numtables() > 1) ):

        if( table.get_lasttabledisplayed() == (table.get_numtables()-1) ) :
            more = False
            prev = True
        else :
            if( table.get_lasttabledisplayed() < (table.get_numtables()-1) ) : 
                more = True
                if( not (table.get_lasttabledisplayed() == 0) ) :
                    prev=True
                    
    elif(table.get_tabletype() == ROW_MAJOR) :

        if( not (len(table.get_rowList()) == table.get_rowspertable())) : 
            if(len(table.get_rowList()) >  (table.get_lastrowdisplayed() + table.get_rowspertable())) : 
                more = True
            if(((table.get_lastrowdisplayed()+1) >= table.get_rowspertable())) : 
                prev = True
            
    else :
        if((table.get_lastcoldisplayed()+1) < table.get_maxcolumns()) : 
            more = True
        if((table.get_lastcoldisplayed()+1) > table.get_colsperrow()) : 
            prev = True

    return(more, prev)

"""
* -----------------------------------------------------------------------*
* get the start and end indices for scrollable tables
* -----------------------------------------------------------------------*
*   table           -   table object
* -----------------------------------------------------------------------*
"""
def get_row_indices(table) :

    startrowIndex   =   0
    rowcount        =   0
    
    if(table.get_tabletype() == MULTIPLE) :
        rowcount = len(table.get_rowList())
        
    elif(table.get_tabletype() == ROW_MAJOR) :
        
        if( (len(table.get_rowList()) >= (table.get_lastrowdisplayed() + table.get_rowspertable())) ) :
            if(table.get_lastrowdisplayed() == -1) :
                if(len(table.get_rowList()) > table.get_rowspertable()) :
                    rowcount = table.get_rowspertable() 
                else :
                    rowcount = len(table.get_rowList())
            else : 
                rowcount = table.get_rowspertable()
        else :
            if(len(table.get_rowList()) == 1) :
                rowcount = 1
            elif(len(table.get_rowList()) <= table.get_rowspertable()) :
                rowcount = len(table.get_rowList())
            else :
                rowcount = (len(table.get_rowList()) - (table.get_lastrowdisplayed() ))
        
        if(table.get_lastrowdisplayed() == -1) :
            startrowIndex = 0
        else :
            startrowIndex = table.get_lastrowdisplayed()
    
    elif(table.get_tabletype() == COLUMN_MAJOR) :
        startrowIndex = 0 
        rowcount = 1

    else :
        
        if(len(table.get_rowList()) < table.get_rowspertable()) :
            rowcount = len(table.get_rowList())
        else :
            rowcount = table.get_rowspertable()
        
    return(startrowIndex, rowcount)


"""
* -----------------------------------------------------------------------*
* get hiddens associated with a table
*
*   fid             -   form id - table
*   hiddensList     -   list of hidden elements 
* -----------------------------------------------------------------------*
"""
def get_hiddens(fid,hiddensList) :
    
    newHTML = ""
 
    newHTML = (newHTML + new_line + "<div ")
    newHTML = (newHTML + addattribute("id",fid + "hiddens") + ">" )#+ new_line)
       
    for i in range(len(hiddensList)) :
        newHTML = (newHTML + '  <input type="hidden" ' + 
                     addattribute("id",hiddensList[i][0]) + 
                     addattribute("value",str(hiddensList[i][1])) + 
                     "></input>" )#+ new_line)
           
    newHTML = (newHTML + "</div> ")
    
    return(newHTML)



        
"""
* -----------------------------------------------------------------------*
* Dataframe Schema Table html 
* -----------------------------------------------------------------------*
"""
schema_col_table_start = """
                            <div class="dc-schema-col-container">
                                <table class="table table-bordered">"""
schema_col_table_end = """                                </table>
                            </div>
"""

schema_col_dlist_start = """
                                    <tr>
                                        <div class="input-group mb-3 dc-schema-dlist">"""
schema_col_dlist_end = """
                                        </div>
                                    </tr>"""

schema_col_dlist_div_start = """
                                            <div class="input-group-prepend dc-schema-dlist-div">"""
schema_col_dlist_div_end = """                                            </div>"""

schema_col_dlist_label_start = """
                                                <label class="input-group-text dc-schema-dlist-label" """
schema_col_dlist_label_end = """>datatype</label>"""
schema_col_dlist_select_start = """
                                                <select class="custom-select" """
schema_col_dlist_select_end = """                                               </select>
"""

schema_col_radio_start = """
                                    <tr>
                                        <div class='btn-grp' """
schema_col_radio_end = """                                        </div>
                                    </tr>
                                    <br>"""

schema_col_radio_label_start = """                                            <div class="form-check dc-schema-radio-div">
                                                <label class="radio dc-schema-radio-label" style='text-align:left; margin-left:30%'>
                                                    <input type='radio' """
schema_col_radio_label_end = """
                                                </label>
                                            </div>
"""

schema_col_input_start = """
                                    <tr>
                                        <div class="form-group dc-schema-input-div">"""
schema_col_input_end = """
                                        </div>
                                    </tr>"""
schema_col_input_label_start = """
                                            <label """
schema_col_input_label_end = """>Nan Fill Value:</label>
"""
schema_col_input_form_start = """                                               <input type="text" class="form-control dc-schema-input-form"  style='font-size: 12px; height: 25px; margin-left:10%; width:80%;'"""
schema_col_input_form_end = """>"""

schema_col_button_start = """
                                    <tr>
                                        <div class="dc-schema-input-div">"""
schema_col_button_end = """
                                        </div>
                                    </tr>
""" 
schema_col_button_chdt_start = """
                                            <button type="button" class="btn btn-grp dc-schema-button" style='font-size: 12px; height: 30px; color:white; background-color: #67a1f3;'"""
schema_col_button_chdt_end = """ >Change Schema</button>"""

num_dtypes      =   19

def get_df_schema_table_col(col_name,datatypeId,nancount) : 

    df_schema_HTML  =   ""
    df_schema_HTML  =   (df_schema_HTML + schema_col_table_start)
    
    # df schema dropdown list     
    df_schema_HTML  =   (df_schema_HTML + schema_col_dlist_start)
    df_schema_HTML  =   (df_schema_HTML + schema_col_dlist_div_start)
    df_schema_HTML  =   (df_schema_HTML + schema_col_dlist_label_start)
    df_schema_HTML  =   (df_schema_HTML + addattribute("for","dfschsel"+col_name))
    df_schema_HTML  =   (df_schema_HTML + schema_col_dlist_label_end)
    df_schema_HTML  =   (df_schema_HTML + schema_col_dlist_select_start)
    df_schema_HTML  =   (df_schema_HTML + addattribute("id","dfschsel"+col_name) + ">" + new_line)

    for i in range(num_dtypes) :
        df_schema_HTML  =   (df_schema_HTML + "                                                    <option ")
        if(i == datatypeId) :
            df_schema_HTML  =   (df_schema_HTML + "selected ") 
        df_schema_HTML  =   (df_schema_HTML + addattribute("value",str(i))+">")
        from dfcleanser.common.common_utils import get_datatype_str
        df_schema_HTML  =   (df_schema_HTML + get_datatype_str(i) + "</option>" + new_line)
    
    df_schema_HTML  =   (df_schema_HTML + schema_col_dlist_select_end)    
    df_schema_HTML  =   (df_schema_HTML + schema_col_dlist_div_end)
    df_schema_HTML  =   (df_schema_HTML + schema_col_dlist_end)
    
    # df schema radio buttons     
    df_schema_HTML  =   (df_schema_HTML + schema_col_radio_start)
    df_schema_HTML  =   (df_schema_HTML + addattribute("id","rf"+col_name) + ">" + new_line)
    df_schema_HTML  =   (df_schema_HTML + schema_col_radio_label_start)
    df_schema_HTML  =   (df_schema_HTML + addattribute("name","fdna"+col_name))
    df_schema_HTML  =   (df_schema_HTML + addattribute("id","fillna"+col_name))
    if(nancount > 0) :
        df_schema_HTML  =   (df_schema_HTML + addattribute("onClick","dfsch_fillnaselect('"+ "dfschinput"+col_name+"')"))
        df_schema_HTML  =   (df_schema_HTML + addattribute("value","fillna") + " checked>fillna</input>" + new_line)
    else :
        df_schema_HTML  =   (df_schema_HTML + addattribute("disabled","true"))
        df_schema_HTML  =   (df_schema_HTML + addattribute("value","fillna") + ">fillna</input>")
    df_schema_HTML  =   (df_schema_HTML + schema_col_radio_label_end)
    
    df_schema_HTML  =   (df_schema_HTML + schema_col_radio_label_start)
    df_schema_HTML  =   (df_schema_HTML + addattribute("name","fdna"+col_name))
    df_schema_HTML  =   (df_schema_HTML + addattribute("id","dropna"+col_name)) 
    if(nancount < 1) :
        df_schema_HTML  =   (df_schema_HTML + addattribute("disabled","true"))
    else :
        df_schema_HTML  =   (df_schema_HTML + addattribute("onClick","dfsch_dropnaselect('"+ "dfschinput"+col_name+"')"))
    df_schema_HTML  =   (df_schema_HTML + addattribute("value","dropna") + ">dropna</input>")
    df_schema_HTML  =   (df_schema_HTML + schema_col_radio_label_end)
    df_schema_HTML  =   (df_schema_HTML + schema_col_radio_end)

    # df schema dropdown list
    df_schema_HTML  =   (df_schema_HTML + schema_col_input_start)
    df_schema_HTML  =   (df_schema_HTML + schema_col_input_label_start)
    df_schema_HTML  =   (df_schema_HTML + addattribute("for","dfschinput"+col_name))
    df_schema_HTML  =   (df_schema_HTML + schema_col_input_label_end)
    df_schema_HTML  =   (df_schema_HTML + schema_col_input_form_start)    
    df_schema_HTML  =   (df_schema_HTML + addattribute("id","dfschinput"+col_name))
    if(nancount < 1) :
        df_schema_HTML  =   (df_schema_HTML +"disabled ")
    df_schema_HTML  =   (df_schema_HTML + schema_col_input_form_end)    
    df_schema_HTML  =   (df_schema_HTML + schema_col_input_end)    
    
    # df schema buttons
    df_schema_HTML  =   (df_schema_HTML + schema_col_button_start)
    df_schema_HTML  =   (df_schema_HTML + schema_col_button_chdt_start)
    df_schema_HTML  =   (df_schema_HTML + addattribute("onClick","dfsch_changedt('" + col_name + "')"))
    df_schema_HTML  =   (df_schema_HTML + schema_col_button_chdt_end)
    df_schema_HTML  =   (df_schema_HTML + schema_col_button_end)
   
    df_schema_HTML  =   (df_schema_HTML + schema_col_table_end)

    if(0) :
        print(df_schema_HTML)
        
    return(df_schema_HTML)

