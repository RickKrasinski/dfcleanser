"""
# Database Utilities 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:29:22 2017

@author: Rick
"""

import dfcleanser.common.cfg as cfg
from dfcleanser.common.common_utils import (opStatus)

from dfcleanser.common.cfg import (add_error_to_log, print_to_string)

from dfcleanser.Qt.system.SystemModel import is_debug_on
from dfcleanser.common.cfg import DBUtils_ID

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                    SQL Connector help urls                    -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

PYMYSQL_CONNECTOR_URL           =   "http://pymysql.readthedocs.io/en/latest/user/index.html"
PYMYSQL_CONNECTOR_SQLA_URL      =   "http://docs.sqlalchemy.org/en/latest/dialects/mysql.html#module-sqlalchemy.dialects.mysql.pymysql"
MYSQL_CONNECTOR_URL             =   "https://dev.mysql.com/doc/connector-python/en/"
MYSQL_CONNECTOR_SQLA_URL        =   "http://docs.sqlalchemy.org/en/latest/dialects/mysql.html#module-sqlalchemy.dialects.mysql.mysqlconnector"
PYODBC_CONNECTOR_URL            =   "https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/python-sql-driver-pyodbc"
PYODBC_CONNECTOR_SQLA_URL       =   "http://docs.sqlalchemy.org/en/latest/dialects/mssql.html#module-sqlalchemy.dialects.mssql.pyodbc"
PYMSSQL_CONNECTOR_URL           =   "https://docs.microsoft.com/en-us/sql/connect/python/pymssql/python-sql-driver-pymssql"
PYMSSQL_CONNECTOR_SQLA_URL      =   "http://docs.sqlalchemy.org/en/latest/dialects/mssql.html#module-sqlalchemy.dialects.mssql.pymssql"
SQLITE_CONNECTOR_URL            =   "https://docs.python.org/2/library/sqlite3.html"
SQLITE_CONNECTOR_SQLA_URL       =   "http://docs.sqlalchemy.org/en/latest/dialects/sqlite.html"
POSTGRESQL_CONNECTOR_URL        =   "http://initd.org/psycopg/docs/"
POSTGRESQL_CONNECTOR_SQLA_URL   =   "http://docs.sqlalchemy.org/en/latest/dialects/postgresql.html#module-sqlalchemy.dialects.postgresql.psycopg2"
ORACLE_CONNECTOR_URL            =   "https://oracle.github.io/python-cx_Oracle/"
ORACLE_CONNECTOR_SQLA_URL       =   "http://docs.sqlalchemy.org/en/latest/dialects/oracle.html#module-sqlalchemy.dialects.oracle.cx_oracle"
CUSTOM_CONNECTOR_URL            =   "http://docs.sqlalchemy.org/en/20/dialects/index.html"

 
from dfcleanser.common.html_widgets import displayHeading
from dfcleanser.common.common_utils import (get_parms_for_input, RunningClock)
from dfcleanser.sw_utilities.DisplayUtils import (get_exception_html, get_status_msg_html)
from dfcleanser.common.help_utils import IMPORT_CUSTOM_ID


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   database identifiers
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
MySql           =   0                         
MS_SQL_Server   =   1                   
SQLite          =   2        
Postgresql      =   3
Oracle          =   4
Custom          =   5   

"""
#--------------------------------------------------------------------------
#   db connector types
#--------------------------------------------------------------------------
"""
NATIVE          =   0
SQLALCHEMY      =   1

SQL_IMPORT      =   0
SQL_QUERY       =   1
SQL_EXPORT      =   2

"""
#--------------------------------------------------------------------------
#   database connectors libraries
#--------------------------------------------------------------------------
"""
pymysql_library             =    "pymysql"
mysql_connector_library     =    "mysql.connector"

pyodbc_library              =    "pyodbc"
pymssql_library             =    "pymssql"

sqlite_library              =    "sqlite"
sqlite3_library             =    "sqlite3"

psycopg2_library            =    "psycopg2"

cx_oracle_library           =    "cx_Oracle"


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   simple utilities
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def get_db_connector_idList(dbid) :
    """
    #------------------------------------------------------------------
    #   get an idlist for a dbid
    #
    #    dbid           -   database id 
    #
    #------------------------------------------------------------------
    """ 
    
    if(dbid == MySql)               : return(mysql_connector_idList[:6]) 
    elif(dbid == MS_SQL_Server)     : return(mssql_connector_idList[:6]) 
    elif(dbid == SQLite)            : return(sqlite_connector_idList[:3]) 
    elif(dbid == Postgresql)        : return(Postgresql_connector_idList[:6]) 
    elif(dbid == Oracle)            : return(oracle_connector_idList[:5]) 
    elif(dbid == Custom)            : return(custom_connector_idList[:2]) 


def get_db_id_title(dbid) :
    """
    #------------------------------------------------------------------
    #   get a text desc of a dbid
    #
    #    dbid           -   database id 
    #
    #------------------------------------------------------------------
    """ 
    
    if(dbid == MySql)           :   return("MySql")
    elif(dbid == MS_SQL_Server) :   return("MS SQL Server")
    elif(dbid == SQLite)        :   return("SQLite3")
    elif(dbid == Postgresql)    :   return("Postgresql")
    elif(dbid == Oracle)        :   return("Oracle")
    elif(dbid == Custom)        :   return("Custom") 
    else : return("  ")


def get_db_id_from_dbid_title(dbid_title) :
    """
    #------------------------------------------------------------------
    #   get a text desc of a dbid
    #
    #    dbid           -   database id 
    #
    #------------------------------------------------------------------
    """ 
    
    if(dbid_title == "MySql")           :   return(MySql)
    elif(dbid_title == "MS SQL Server") :   return(MS_SQL_Server)
    elif(dbid_title == "SQLite3")       :   return(SQLite)
    elif(dbid_title == "Postgresql")    :   return(Postgresql)
    elif(dbid_title == "Oracle")        :   return(Oracle)
    elif(dbid_title == "Custom")        :   return(Custom) 
    else : return(MySql)


def get_dbid_from_lib(dblib) :
    """
    #------------------------------------------------------------------
    #   get the dbid from the db;ibrary entry in the con dict
    #
    #    dblib  -   bd library
    #
    #------------------------------------------------------------------
    """    

    dbid = None
    
    if( (dblib == pymysql_library) or (dblib == mysql_connector_library) )  :    dbid = MySql
    elif( (dblib == pyodbc_library) or (dblib == pymssql_library) )         :    dbid = MS_SQL_Server
    elif( (dblib == sqlite_library) or (dblib == sqlite3_library) )         :    dbid = SQLite
    elif(dblib == psycopg2_library)                                         :    dbid = Postgresql
    elif(dblib == cx_oracle_library)                                        :    dbid = Oracle
    else                                                                    :    dbid = Custom

    return(dbid)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   SQL Connector Forms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

"""
#--------------------------------------------------------------------------
#   mysql db connector parms
#--------------------------------------------------------------------------
"""

mysql_connector_title               =   "MySql DB Connector Parameters"
mysql_connector_id                  =   "MySQLdbconnector"

mysql_connector_idList              =    ["sqlservertype",
                                          "sqldbcondblibid",
                                          "sqlconservername",
                                          "sqlcondbname",
                                          "sqlconusername",
                                          "sqlconpassword",
                                          None,None,None,None]

mysql_connector_labelList           =   ["servertype",
                                         "dblibrary",
                                         "hostname",
                                         "database",
                                         "username",
                                         "password",
                                         "Test</br>Connector",
                                         "Save</br>Connector",
                                         "Return",
                                         "Help"]

mysql_connector_jsList              =   [None,None,None,None,None,None,
                                         "dfcleanser_test_con_callback(0,0)",
                                         "maintain_dbconnectors(4,0,XXXXID,'MySQLdbconnector')",
                                         "maintain_dbconnectors(6,0,XXXXSQLID)",
                                         "display_help_url('"+str(PYMYSQL_CONNECTOR_URL)+"')"]

mysql_connector_typeList            =   ["select","select","text","text","text","text",
                                         "button","button","button","button"]

mysql_connector_placeholderList     =   ["enter SQL Server type",
                                         "enter the database connector library",
                                         "enter host name",
                                         "enter database",
                                         "enter user name",
                                         "enter passsword",
                                          None,None,None,None]

mysql_connector_reqList             =   [0,1,2,3,4,5]

mysql_connector_pymysql_help_url    =   "display_help_url('"+str(PYMYSQL_CONNECTOR_URL)+"')"
mysql_connector_mysql_help_url      =   "display_help_url('"+str(MYSQL_CONNECTOR_URL)+"')"

mysql_connector_export_jsList       =   [None,None,None,None,None,None,
                                         "dfcleanser_test_con_callback(0,0)",
                                         "maintain_dbconnectors(4,1,XXXXID,'MySQLdbconnector')",
                                         "maintain_dbconnectors(6,1,XXXXSQLID)",
                                         "display_help_url('"+str(PYMYSQL_CONNECTOR_URL)+"')"]


mysql_connector_import_test_con     =   "dfcleanser_test_con_callback(0,0)" 
mysql_connector_query_test_con      =   "dfcleanser_test_con_callback(1,0)" 
mysql_connector_export_test_con     =   "dfcleanser_test_con_callback(2,0)" 


"""
#--------------------------------------------------------------------------
#   MS SQL Server db connector parms
#--------------------------------------------------------------------------
"""

mssql_connector_title               =    "MS SQL Server DB Connector Parameters"
mssql_connector_id                  =    "MSSQLServerdbconnector"

mssql_connector_idList              =    ["sqlservertype",
                                          "sqldbcondblibid",
                                          "sqlconservername",
                                          "sqlcondbname",
                                          "sqlconusername",
                                          "sqlconpassword",
                                           None,None,None,None]

mssql_connector_typeList            =   ["select","select","text","text","text","text",
                                         "button","button","button","button"]

mssql_connector_placeholderList     = ["enter the sql server type",
                                       "enter the database connector library",
                                       "enter server name",
                                       "enter database name",
                                       "enter user name",
                                       "enter password",
                                       None,None,None,None]

mssql_connector_reqList             =   [0,1,2,3,4,5]

mssql_connector_labelList           =   ["servertype",
                                         "dblibrary",
                                         "msserver",
                                         "msdatabase",
                                         "msusername",
                                         "mspassword",
                                         "Test</br>Connector",
                                         "Save</br>Connector",
                                         "Return",
                                         "Help"]

mssql_connector_jsList              =  [None,None,None,None,None,None,
                                        "dfcleanser_test_con_callback(0,1)",
                                        "maintain_dbconnectors(4,0,XXXXID,'MSSQLServerdbconnector')",
                                        "maintain_dbconnectors(6,0,XXXXSQLID)",
                                        "display_help_url('"+str(PYODBC_CONNECTOR_URL)+"')"]

mssql_connector_pymssql_help_url    =   "display_help_url('"+str(PYMSSQL_CONNECTOR_URL)+"')"
mssql_connector_pyodbc_help_url     =   "display_help_url('"+str(PYODBC_CONNECTOR_URL)+"')"

mssql_connector_export_jsList       =  [None,None,None,None,None,None,
                                        "dfcleanser_test_con_callback(0,1)",
                                        "maintain_dbconnectors(4,1,XXXXID,'MSSQLServerdbconnector')",
                                        "maintain_dbconnectors(6,1,XXXXSQLID)",
                                        "display_help_url('"+str(PYODBC_CONNECTOR_URL)+"')"]


mssql_connector_import_test_con     =   "dfcleanser_test_con_callback(0,1)" 
mssql_connector_query_test_con      =   "dfcleanser_test_con_callback(1,1)" 
mssql_connector_export_test_con     =   "dfcleanser_test_con_callback(2,1)" 


"""
#--------------------------------------------------------------------------
#   Postgresql db connector parms
#--------------------------------------------------------------------------
"""

Postgresql_connector_title          =   "Postgresql DB Connector Parameters"
Postgresql_connector_id             =   "Postgresqldbconnector"

Postgresql_connector_idList         =    ["sqlservertype",
                                          "sqldbcondblibid",
                                          "sqlconservername",
                                          "sqlcondbname",
                                          "sqlconusername",
                                          "sqlconpassword",
                                          None,None,None,None]

Postgresql_connector_typeList       =   ["select","select","text","text","text","text",
                                         "button","button","button","button"]

Postgresql_connector_placeholderList = ["select the sql server type",
                                        "enter the database connector library",
                                        "enter server name",
                                        "enter database name",
                                        "enter user name",
                                        "enter password",
                                        None,None,None,None]

Postgresql_connector_reqList        =   [0,1,2,3,4,5]

Postgresql_connector_labelList      =   ["servertype",
                                         "dblibrary",
                                         "pghost",
                                         "pgdbname",
                                         "pguser",
                                         "pgpassword",
                                         "Test</br>Connector",
                                         "Save</br>Connector",
                                         "Return",
                                        "Help"]

Postgresql_connector_jsList         =   [None,None,None,None,None,None,
                                         "dfcleanser_test_con_callback(0,3)",
                                         "maintain_dbconnectors(4,0,XXXXID,'Postgresqldbconnector')",
                                         "maintain_dbconnectors(6,0,XXXXSQLID)",
                                         "display_help_url('"+str(POSTGRESQL_CONNECTOR_URL)+"')"]

Postgresql_connector_export_jsList  =   [None,None,None,None,None,None,
                                         "dfcleanser_test_con_callback(0,3)",
                                         "maintain_dbconnectors(4,1,XXXXID,'Postgresqldbconnector')",
                                         "maintain_dbconnectors(6,1,XXXXSQLID)",
                                         "display_help_url('"+str(POSTGRESQL_CONNECTOR_URL)+"')"]

Postgresql_connector_import_test_con    =   "dfcleanser_test_con_callback(0,3)" 
Postgresql_connector_query_test_con     =   "dfcleanser_test_con_callback(1,3)" 
Postgresql_connector_export_test_con    =   "dfcleanser_test_con_callback(2,3)" 


"""
#--------------------------------------------------------------------------
#   SQLite db connector input form components
#--------------------------------------------------------------------------
"""

sqlite_connector_title              =   "SQLite DB Connector Parameters"
sqlite_connector_id                 =   "SQLitedbconnector"

sqlite_connector_idList             =    ["sqlservertype",
                                          "sqldbcondblibid",
                                          "SQLitedbfileName",
                                          None,None,None,None]

sqlite_connector_typeList           =   ["select","select","text",
                                         "button","button","button","button"]

sqlite_connector_placeholderList    =   ["select the sql server type",
                                         "enter the database connector library",
                                         "enter the db file name",
                                         None,None,None,None]

sqlite_connector_reqList            =   [0,1,2]

sqlite_connector_labelList          =   ["servertype",
                                         "dblibrary",
                                         "db_file",
                                         "Test</br>Connector",
                                         "Save</br>Connector",
                                         "Return",
                                         "Help"]

sqlite_connector_jsList             =   [None,None,None,
                                         "dfcleanser_test_con_callback(0,2)",
                                         "maintain_dbconnectors(4,0,XXXXID,'SQLitedbconnector')",
                                         "maintain_dbconnectors(6,0,XXXXSQLID)",
                                         "display_help_url('"+str(SQLITE_CONNECTOR_URL)+"')"]

sqlite_connector_export_jsList      =   [None,None,None,
                                         "dfcleanser_test_con_callback(0,2)",
                                         "maintain_dbconnectors(4,1,XXXXID,'SQLitedbconnector')",
                                         "maintain_dbconnectors(6,1,XXXXSQLID)",
                                         "display_help_url('"+str(SQLITE_CONNECTOR_URL)+"')"]

sqlite_connector_import_test_con    =   "dfcleanser_test_con_callback(0,2)" 
sqlite_connector_query_test_con     =   "dfcleanser_test_con_callback(1,2)" 
sqlite_connector_export_test_con    =   "dfcleanser_test_con_callback(2,2)" 


"""
#--------------------------------------------------------------------------
#   Oracle db connector parms
#--------------------------------------------------------------------------
"""


oracle_connector_title              =   "Oracle DB Connector Parameters"
oracle_connector_id                 =   "Oracledbconnector"

oracle_connector_idList             =    ["sqlservertype",
                                          "sqldbcondblibid",
                                          "sqlconservername",
                                          "sqlconusername",
                                          "sqlconpassword",
                                          None,None,None,None]

oracle_connector_typeList           =   ["select","select","text","text","text",
                                        "button","button","button","button"]

oracle_connector_placeholderList    =   ["select the sql server type",
                                         "enter the database connector library",
                                         "enter server name",
                                         "enter database name",
                                         "enter password",
                                         None,None,None,None]

oracle_connector_reqList            =   [0,1,2,3,4]

oracle_connector_labelList          =   ["servertype",
                                         "dblibrary",
                                         "tdshost",
                                         "user",
                                         "password",
                                         "Test</br>Connector",
                                         "Save</br>Connector",
                                         "Return",
                                         "Help"]

oracle_connector_jsList             =   [None,None,None,None,None,
                                         "dfcleanser_test_con_callback(0,4)",
                                         "maintain_dbconnectors(4,0,XXXXID,'Oracledbconnector')",
                                         "maintain_dbconnectors(6,0,XXXXSQLID)",
                                         "display_help_url('"+str(ORACLE_CONNECTOR_URL)+"')"]

oracle_connector_export_jsList      =   [None,None,None,None,None,
                                         "dfcleanser_test_con_callback(0,4)",
                                         "maintain_dbconnectors(4,1,XXXXID,'Oracledbconnector')",
                                         "maintain_dbconnectors(6,1,XXXXSQLID)",
                                         "display_help_url('"+str(ORACLE_CONNECTOR_URL)+"')"]

oracle_connector_import_test_con    =   "dfcleanser_test_con_callback(0,4)" 
oracle_connector_query_test_con     =   "dfcleanser_test_con_callback(1,4)" 
oracle_connector_export_test_con    =   "dfcleanser_test_con_callback(2,4)" 


"""
#--------------------------------------------------------------------------
#   custom db connector parms
#--------------------------------------------------------------------------
"""

custom_connector_title              =   "Custom DB Connector Parameters"
custom_connector_id                 =   "customdbconnector"

custom_connector_idList             =    ["dbconnectorstring",
                                          None,None,None,None]

custom_connector_labelList          =   ["customdbconnectorstring",
                                         "Test</br>Connector",
                                         "Save</br>Connector",
                                         "Return",
                                         "Help"]


custom_connector_typeList           =   ["text",
                                         "button","button","button","button"]

custom_connector_placeholderList    =   ["enter connector string",
                                         None,None,None,None]

custom_connector_jsList             =   [None,
                                         "dfcleanser_test_con_callback(0,5)",
                                         "maintain_dbconnectors(4,0,XXXXID,'customdbconnector')",
                                         "maintain_dbconnectors(6,0,XXXXSQLID)",
                                         "display_help_url('"+str(CUSTOM_CONNECTOR_URL)+"')"]

custom_connector_export_jsList      =   [None,
                                         "dfcleanser_test_con_callback(0,5)",
                                         "maintain_dbconnectors(4,1,XXXXID,'customdbconnector')",
                                         "maintain_dbconnectors(6,1,XXXXSQLID)",
                                         "display_help_url('"+str(CUSTOM_CONNECTOR_URL)+"')"]

custom_connector_reqList            =   [0]

custom_connector_import_test_con    =   "dfcleanser_test_con_callback(0,5)" 
custom_connector_query_test_con     =   "dfcleanser_test_con_callback(1,5)" 
custom_connector_export_test_con    =   "dfcleanser_test_con_callback(2,5)" 



"""
#--------------------------------------------------------------------------
#   db connector parms lists
#--------------------------------------------------------------------------
"""
MYSQL_DBCON_PARMS                    =   mysql_connector_id + "Parms"
MSSQL_DBCON_PARMS                    =   mssql_connector_id + "Parms"
SQLITE_DBCON_PARMS                   =   sqlite_connector_id + "Parms"
POSTGRESQL_DBCON_PARMS               =   Postgresql_connector_id + "Parms"
ORACLE_DBCON_PARMS                   =   oracle_connector_id + "Parms"
CUSTOM_DBCON_PARMS                   =   custom_connector_id + "Parms"


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   database connectors dictionary (dbcondict) utilities
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
def get_current_dbcondict(importexportflag):#,dbid):#,formparmsList) :
    """
    #------------------------------------------------------------------
    #   get a db connector dict from input form or default
    #
    #    dbid           -   database id 
    #    formparmsList  -   input form parms
    #
    #------------------------------------------------------------------
    """ 

    if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS")) :
        cfg.add_debug_to_log("get_current_dbcondict"," : importexportflag : " + str(importexportflag))

    dbconn      =   dfc_dbconnectors_table.get_current_dbconnector(importexportflag)
    dbcondict   =   {}
    
    if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS")) :
        cfg.add_debug_to_log("get_current_dbcondict"," : dbconn : " + str(dbconn))

    if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
        add_debug_to_log("DataImportGui",print_to_string("[get_current_dbcondict] : current_dbconnector "))
        dbconn.dump()

    current_dbid    =   int(dbconn.get_db_id())

    if(current_dbid == MySql)                   :   
    
        labellist =  mysql_connector_labelList

        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
            cfg.add_debug_to_log("get_current_dbcondict"," : labellist " + str(labellist))

        dbcondict.update({labellist[0]:str(dbconn.get_db_id())})
        dbcondict.update({labellist[1]:dbconn.get_db_library()})
        dbcondict.update({labellist[2]:dbconn.get_server()})
        dbcondict.update({labellist[3]:dbconn.get_database()})
        dbcondict.update({labellist[4]:dbconn.get_user()})
        dbcondict.update({labellist[5]:dbconn.get_password()})
    
        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
            cfg.add_debug_to_log("get_current_dbcondict"," : db_id " + str(dbconn.get_db_id()))
            cfg.add_debug_to_log("get_current_dbcondict"," : db_library " + str(dbconn.get_db_library())) 
            cfg.add_debug_to_log("get_current_dbcondict"," : server " + str(dbconn.get_server()))
            cfg.add_debug_to_log("get_current_dbcondict"," : database " + str(dbconn.get_database())) 

    elif(current_dbid == MS_SQL_Server)     :   
        
        labellist =  mssql_connector_labelList
        dbcondict.update({labellist[0]:str(dbconn.get_db_id())})
        dbcondict.update({labellist[1]:dbconn.get_db_library()})
        dbcondict.update({labellist[2]:dbconn.get_server()})
        dbcondict.update({labellist[3]:dbconn.get_database()})
        dbcondict.update({labellist[4]:dbconn.get_user()})
        dbcondict.update({labellist[5]:dbconn.get_password()})

    elif(current_dbid == SQLite)           :   
        
        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
            cfg.add_debug_to_log("get_current_dbcondict"," : SQLite dbcondict")
        
        labellist =  sqlite_connector_labelList
        dbcondict.update({labellist[0]:str(dbconn.get_db_id())})
        dbcondict.update({labellist[1]:dbconn.get_db_library()})
        dbcondict.update({labellist[2]:dbconn.get_server()})

        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
            cfg.add_debug_to_log("get_current_dbcondict"," : db_id " + str(dbconn.get_db_id()))
            cfg.add_debug_to_log("get_current_dbcondict"," : db_library " + str(dbconn.get_db_library())) 
            cfg.add_debug_to_log("get_current_dbcondict"," : server " + str(dbconn.get_server()))
            cfg.add_debug_to_log("get_current_dbcondict"," : database " + str(dbconn.get_database())) 


    elif(current_dbid == Postgresql)        :   
        
        labellist =  Postgresql_connector_labelList
        dbcondict.update({labellist[0]:str(dbconn.get_db_id())})
        dbcondict.update({labellist[1]:dbconn.get_db_library()})
        dbcondict.update({labellist[2]:dbconn.get_server()})
        dbcondict.update({labellist[3]:dbconn.get_database()})
        dbcondict.update({labellist[4]:dbconn.get_user()})
        dbcondict.update({labellist[5]:dbconn.get_password()})

    elif(current_dbid == Oracle)            :   
        
        labellist =  oracle_connector_labelList
        dbcondict.update({labellist[0]:str(dbconn.get_db_id())})
        dbcondict.update({labellist[1]:dbconn.get_db_library()})
        dbcondict.update({labellist[2]:dbconn.get_server()})
        dbcondict.update({labellist[3]:dbconn.get_user()})
        dbcondict.update({labellist[4]:dbconn.get_password()})

    elif(current_dbid == Custom)            :   
        
        labellist =  custom_connector_labelList
        dbcondict.update({labellist[0]:str(dbconn.get_db_id())})
        dbcondict.update({labellist[1]:dbconn.get_db_library()})
    
    if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
        cfg.add_debug_to_log("get_current_dbcondict"," : db_id " + str(dbconn.get_db_id()))
        cfg.add_debug_to_log("get_current_dbcondict"," : db_library " + str(dbconn.get_db_library())) 
        cfg.add_debug_to_log("get_current_dbcondict"," : server " + str(dbconn.get_server()))
        cfg.add_debug_to_log("get_current_dbcondict"," : database " + str(dbconn.get_database())) 
    
    return(dbcondict)


CON_DICT_SERVER         =   0
CON_DICT_DATABASE       =   1
CON_DICT_USERNAME       =   2
CON_DICT_PASSWORD       =   3
CON_DICT_DBLIBRARY      =   4

def get_dbcondict_value(dbid,dbcondict,valueId) :
    """
    #------------------------------------------------------------------
    #   get a db connector dict from input form or default
    #
    #    dbcondict      -   db connector dict 
    #    valueId        -   value id
    #
    #------------------------------------------------------------------
    """ 
    if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS") ) :
        cfg.add_debug_to_log("get_dbcondict_value"," : dbid valueId" + str(dbid) + str(valueId))

    if(dbid == MySql)                   :   
        if(valueId == CON_DICT_SERVER)          :   return(dbcondict.get("hostname"))        
        elif(valueId == CON_DICT_DATABASE)      :   return(dbcondict.get("database")) 
        elif(valueId == CON_DICT_USERNAME)      :   return(dbcondict.get("username"))        
        elif(valueId == CON_DICT_PASSWORD)      :   return(dbcondict.get("password")) 
        elif(valueId == CON_DICT_DBLIBRARY)     :   return(dbcondict.get("ddblibrary")) 
        else                                    :   return("")
    elif( (dbid == MS_SQL_Server) )     :   
        if(valueId == CON_DICT_SERVER)          :   return(dbcondict.get("msserver"))        
        elif(valueId == CON_DICT_DATABASE)      :   return(dbcondict.get("msdatabase")) 
        elif(valueId == CON_DICT_USERNAME)      :   return(dbcondict.get("msusername"))        
        elif(valueId == CON_DICT_PASSWORD)      :   return(dbcondict.get("mspassword")) 
        elif(valueId == CON_DICT_DBLIBRARY)     :   return(dbcondict.get("ddblibrary")) 
        else                                    :   return("")
    elif( (dbid == SQLite) )            :           
        if(valueId == CON_DICT_SERVER)          :   return(dbcondict.get("db_file"))        
        elif(valueId == CON_DICT_DBLIBRARY)     :   return(dbcondict.get("ddblibrary")) 
        else                                    :   return("")
    elif( (dbid == Postgresql) )         :   
        if(valueId == CON_DICT_SERVER)          :   return(dbcondict.get("pghost"))        
        elif(valueId == CON_DICT_DATABASE)      :   return(dbcondict.get("pgdbname")) 
        elif(valueId == CON_DICT_USERNAME)      :   return(dbcondict.get("pguser"))        
        elif(valueId == CON_DICT_PASSWORD)      :   return(dbcondict.get("pguser")) 
        elif(valueId == CON_DICT_DBLIBRARY)     :   return(dbcondict.get("ddblibrary")) 
        else                                    :   return("")
    elif( (dbid == Oracle) )            :   
        if(valueId == CON_DICT_SERVER)          :   return(dbcondict.get("tdshost"))        
        elif(valueId == CON_DICT_USERNAME)      :   return(dbcondict.get("user"))        
        elif(valueId == CON_DICT_PASSWORD)      :   return(dbcondict.get("password")) 
        elif(valueId == CON_DICT_DBLIBRARY)     :   return(dbcondict.get("ddblibrary")) 
        else                                    :   return("")
    elif( (dbid == Custom) )            :   
        if(valueId == CON_DICT_SERVER)          :   return(dbcondict.get("SQLAlchemy db connector string"))        
        else                                    :   return("")
    else                                :
        return("")

def check_current_dbcondict(importexportflag,dbid,conparms) :
    """
    * -------------------------------------------------------------------------- 
    * function : check db connector is complete
    * 
    * parms :
    *  dbid            -    Database Id
    *  dbconparms      -    db connector parms                      
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS")) :
        cfg.add_debug_to_log("check_current_dbcondict"," importexportflag : " + str(importexportflag) + " dbid : " + str(dbid) + "conparms : \n  " + str(conparms))
    
    dbcondict = get_current_dbcondict(importexportflag)#,dbid)#,dbid,conparms)

    if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS")) :
        cfg.add_debug_to_log("check_current_dbcondict"," dbcondict : \n  " + str(dbcondict)) 

    dbdict_keys     =   list(dbcondict.keys())
    
    for i in range(len(dbdict_keys)) :
        dbcon_val   =  dbcondict.get(dbdict_keys[i])
        if(type(dbcon_val) == str) :
            if(len(dbcon_val) == 0) :
                return(False)
    
    return(True)

def set_dbcon_dict(dbid,parmslist) :
    """
    #------------------------------------------------------------------
    #   buil db connector dict
    #
    #    dbid           -   database type identifier 
    #    parmslist      -   list of dcon parms 
    #
    #------------------------------------------------------------------
    """ 

    if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS")) :
       cfg.add_debug_to_log("set_dbcon_dict"," dbid parmslist custom_connector_labelList "+str(dbid) + str(parmslist)))  
          
    dbcondict = {}

    dbconlabels =   [mysql_connector_labelList,mssql_connector_labelList,sqlite_connector_labelList,
                     Postgresql_connector_labelList,oracle_connector_labelList,custom_connector_labelList]    
    dbconlens   =   [6,6,2,6,5,1] 
    
    dbcondict.update({"dbid":dbid})
    
    for i in range(dbconlens[dbid]) :
        dbcondict.update({dbconlabels[dbid][i]:parmslist[i]})    
    
    return(dbcondict)


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   database connectors utilities
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

def parse_connector_parms(connectparms,dbid,dbparms) :
    """
    #------------------------------------------------------------------
    #   parse the sql parms
    #
    #    sqlinputparms      -   input parm list 
    #    dbparms            -   parms dict 
    #
    #------------------------------------------------------------------
    """    
    
    if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_TEST_CONNECTOR")) :
        cfg.add_debug_to_log("parse_connector_parms"," dbid : " + type(dbid) + str(dbid) + "\n     connectparms : \n      " + str(connectparms) + "\n     dbparms : \n      " + str(dbparms))

    if(not (dbid == Custom)) :
        dbparms.update({"dbid":dbid})
    
    if(dbid == MySql)           : 
        idlist      =   mysql_connector_idList
        labellist   =   mysql_connector_labelList
    elif(dbid == MS_SQL_Server) : 
        idlist      =   mssql_connector_idList
        labellist   =  mssql_connector_labelList
    elif(dbid == SQLite)        : 
        idlist      =   sqlite_connector_idList
        labellist   =   sqlite_connector_labelList
    elif(dbid == Postgresql)    : 
        idlist      =   Postgresql_connector_idList
        labellist   =   Postgresql_connector_labelList
    elif(dbid == Oracle)        : 
        idlist      =   oracle_connector_idList
        labellist   =   oracle_connector_labelList
    elif(dbid == Custom)        : 
        idlist      =   custom_connector_idList
        labellist   =   custom_connector_labelList
    
    if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_TEST_CONNECTOR")) :
        cfg.add_debug_to_log("parse_connector_parms"," idlist : \n    " + str(idlist) + "\n     labellist : \n      " + str(labellist))
    
    if(dbid == Custom) :
        sqllist     =   connectparms[1]
    else :
        sqllist     =   get_parms_for_input(connectparms,idlist)
    
    if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_TEST_CONNECTOR")) :
        cfg.add_debug_to_log("parse_connector_parms"," dbid : " + str(dbid) + "\n     sqllist : \n      " + str(sqllist) + "\n     dbparms : \n      " + str(dbparms))
    
    for i in range(len(sqllist)) :
        dbparms.update({labellist[i]:sqllist[i]})    
    
    if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_TEST_CONNECTOR")) :
        add_debug_to_log("parse_connector_parms",print_to_string(" dbid : ",dbid,"\n     sqllist : \n      ",sqllist,"\n     dbparms : \n      ",dbparms))

    return(sqllist)




# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -          DBConnector classes and utilities                    -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

def get_stored_con_Parms(dbid) :
    """
    #------------------------------------------------------------------
    #   get connection parms stored in the cfg database
    #
    #    dbid           -   database id
    #
    #------------------------------------------------------------------
    """    
    
    conparms = None
    
    if(dbid == MySql)               : conparms = cfg.get_config_value(MYSQL_DBCON_PARMS)
    elif(dbid == MS_SQL_Server)     : conparms = cfg.get_config_value(MSSQL_DBCON_PARMS)
    elif(dbid == SQLite)            : conparms = cfg.get_config_value(SQLITE_DBCON_PARMS)
    elif(dbid == Postgresql)        : conparms = cfg.get_config_value(POSTGRESQL_DBCON_PARMS)
    elif(dbid == Oracle)            : conparms = cfg.get_config_value(ORACLE_DBCON_PARMS)
    elif(dbid == Custom)            : conparms = cfg.get_config_value(CUSTOM_DBCON_PARMS)

    return(conparms)    


def grab_connection_parms(parmsdict) :
    """
    #------------------------------------------------------------------
    #   grab the sql db connector parms
    #
    #    parmsdict     -   sql parms dict
    #
    #------------------------------------------------------------------
    """    
    
    dbid = get_dbid_from_lib(parmsdict.get("dblibrary")) 

    if(dbid is None) :
        dbid    =   Custom
    
    dbcondict       =   {}
    
    if(dbid != None) :

        if(not (dbid  == Custom)) :
            dbcondict.update({"dbid": dbid})    
    
        if(dbid == MySql) :
      
            if(not (parmsdict.get("dblibrary") == None) )   : dbcondict.update({"dblibrary":parmsdict.get("dblibrary")})
            if(not (parmsdict.get("hostname") == None) )    : dbcondict.update({"server":parmsdict.get("hostname")})
            if(not (parmsdict.get("username") == None) )    : dbcondict.update({"user":parmsdict.get("username")})
            if(not (parmsdict.get("password") == None) )    : dbcondict.update({"password":parmsdict.get("password")})
            if(not (parmsdict.get("database") == None) )    : dbcondict.update({"database":parmsdict.get("database")})
            if(not (parmsdict.get("schema") == None) )      : dbcondict.update({"schema":parmsdict.get("schema")})
        
        if(dbid == MS_SQL_Server) :
      
            if(not (parmsdict.get("dblibrary") == None) )   : dbcondict.update({"dblibrary":parmsdict.get("dblibrary")})
            if(not (parmsdict.get("msserver") == None) )    : dbcondict.update({"server":parmsdict.get("msserver")})
            if(not (parmsdict.get("msusername") == None) )  : dbcondict.update({"user":parmsdict.get("msusername")})
            if(not (parmsdict.get("mspassword") == None) )  : dbcondict.update({"password":parmsdict.get("mspassword")})
            if(not (parmsdict.get("msdatabase") == None) )  : dbcondict.update({"database":parmsdict.get("msdatabase")})
            if(not (parmsdict.get("schema") == None) )      : dbcondict.update({"schema":parmsdict.get("schema")})
        
        if(dbid == Postgresql) :
      
            if(not (parmsdict.get("dblibrary") == None) )   : dbcondict.update({"dblibrary":parmsdict.get("dblibrary")})
            if(not (parmsdict.get("pghost") == None) )      : dbcondict.update({"server":parmsdict.get("pghost")})
            if(not (parmsdict.get("pguser") == None) )      : dbcondict.update({"user":parmsdict.get("pguser")})
            if(not (parmsdict.get("pgpassword") == None) )  : dbcondict.update({"password":parmsdict.get("pgpassword")})
            if(not (parmsdict.get("pgdbname") == None) )    : dbcondict.update({"database":parmsdict.get("pgdbname")})
            if(not (parmsdict.get("schema") == None) )      : dbcondict.update({"schema":parmsdict.get("schema")})
        
        elif(dbid == SQLite) :
      
            if(not (parmsdict.get("dblibrary") == None) )   : dbcondict.update({"dblibrary":parmsdict.get("dblibrary")})
            if(not (parmsdict.get("db_file") == None) )     : dbcondict.update({"filename":parmsdict.get("db_file")})
        
        elif(dbid == Oracle) :
      
            if(not (parmsdict.get("dblibrary") == None) )   : dbcondict.update({"dblibrary":parmsdict.get("dblibrary")})
            if(not (parmsdict.get("tdshost") == None) )     : dbcondict.update({"server":parmsdict.get("tdshost")})
            if(not (parmsdict.get("user") == None) )        : dbcondict.update({"user":parmsdict.get("user")})
            if(not (parmsdict.get("password") == None) )    : dbcondict.update({"password":parmsdict.get("password")})
        
        elif(dbid == Custom) :
      
            if(not (parmsdict.get("customdbconnectorstring") == None) )   : dbcondict.update({"customdbconnectorstring":parmsdict.get("customdbconnectorstring")})
    
        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
            add_debug_to_log("grab_connection_parms",print_to_string(" : parmsdict :\n    ",parmsdict))
            add_debug_to_log("grab_connection_parms",print_to_string(" dbcondict :\n    ",dbcondict))
        
        return(dbcondict)
    
    else :
        return(None)
        
def validate_connection_parms(parmsdict) :
    """
    #------------------------------------------------------------------
    #   validate the sql db connector parms
    #
    #    parmsdict          -   connect parms dict 
    #
    #------------------------------------------------------------------
    """ 
       
    if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
        add_debug_to_log("validate_connection_parms",print_to_string(" parmsdict : \n     ",parmsdict))

    current_dbid        =   int(parmsdict.get("servertype"))

    dbconlabels =   [mysql_connector_labelList,mssql_connector_labelList,sqlite_connector_labelList,
                     Postgresql_connector_labelList,oracle_connector_labelList,custom_connector_labelList]    
    dbconlens   =   [6,6,3,6,5,1] 
    
    if(current_dbid is None) :
        if(not (len(parmsdict) == 1)) :
            return("No servertype") 
    else :

        for i in range(dbconlens[current_dbid]) :
            parm = parmsdict.get(dbconlabels[current_dbid][i])
             
            if(type(parm) == str) :
                if(parm is None) :
                    return("Invalid '" + dbconlabels[current_dbid][i] + "' parameter")
                else :
                    if(len(parm) == 0) :
                        return("Invalid '" + dbconlabels[current_dbid][i] + "' parameter")
            else :
                return("Invalid '" + dbconlabels[current_dbid][i] + "' parameter")    

    return(None)   


"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#    DB Connector Testing functions
#------------------------------------------------------------------
#------------------------------------------------------------------
"""

def test_db_connector(dbid,drivertype,sqlinputparms,sqlid,opstat,display=True) :
    """
    #------------------------------------------------------------------
    #   test the db onnector
    #
    #    dbid           -   database id
    #    drivertype     -   NATIVE or SLQALCHEMY
    #    sqlinputparms  -   sql parms
    #    sqlid          -   sql id
    #
    #------------------------------------------------------------------
    """    

    if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS")) :
        add_debug_to_log("test_db_connector",print_to_string(" dbid : ",dbid," drivertype : ",drivertype," sqlid : ",sqlid))
    
    connectParms    =   {}
    parmslist       =   parse_connector_parms(sqlinputparms,dbid,connectParms)
    errormsg        =   validate_connection_parms(connectParms)
    
    if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
        add_debug_to_log("test_db_connector",print_to_string(": \n    parmslist : \n    ",parmslist,"\n    connectParms : \n    ",connectParms))
    
    if(errormsg is None) :

        if(display) :
    
            if(drivertype == NATIVE) :
                if(dbid != Custom) :
                    displayHeading("Testing Native DB Connector",3,300)
            else :
                displayHeading("Testing SQLAlchemy DB Connector",3,300)
                
            clock = RunningClock()
            clock.start()
    
        if( not ((drivertype == NATIVE) and (dbid == Custom))) :
            dbcon = dbConnector()
            dbcon.connect_to_db(drivertype,opstat,connectParms)

        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
            add_debug_to_log("test_db_connector",print_to_string(" opstat :  ",opstat.get_status(),"\n    connectParms : \n    ",connectParms))

        if(opstat.get_status()) :

            if(display) :
                if(drivertype == NATIVE) :
                    if(dbid != Custom) :
                        get_status_msg_html("'Native DB Connector' connected Successfully : " + str(connectParms.get("dblibrary")),440,150,None,True)
                else :
                    get_status_msg_html("'SQLAlchemy DB Connector' connected Successfully : " + str(connectParms.get("dblibrary")),440,150,None,True)
            
            if( not ((drivertype == NATIVE) and (dbid == Custom))) :
                dbcon.close_dbConnection(opstat)

            if(opstat.get_status()) :

                if(display) :
                    if(drivertype == NATIVE) :
                        get_status_msg_html("'Native DB Connector' closed Successfully",440,150,None,True)
                    else :
                        get_status_msg_html("'SQLAlchemy DB Connector' closed Successfully",440,150,None,True)

                dbid = connectParms.get("dbid") 
                
                if(dbid   == MySql)             : cfg.set_config_value(MYSQL_DBCON_PARMS,parmslist)
                elif(dbid == MS_SQL_Server)     : cfg.set_config_value(MSSQL_DBCON_PARMS,parmslist)
                elif(dbid == SQLite)            : cfg.set_config_value(SQLITE_DBCON_PARMS,parmslist)
                elif(dbid == Postgresql)        : cfg.set_config_value(POSTGRESQL_DBCON_PARMS,parmslist)
                elif(dbid == Oracle)            : cfg.set_config_value(ORACLE_DBCON_PARMS,parmslist)
                elif(dbid == Custom)            : cfg.set_config_value(CUSTOM_DBCON_PARMS,parmslist)
            
            else :
                if(display) :
                    get_exception_html(opstat,width=90,left=40,display=True)
                #dbcon.close_dbConnection(opstat)

        else :
            if(display) :
                get_exception_html(opstat,width=90,left=40,display=True)
            #dbcon.close_dbConnection(opstat)
        
        if(display) :
            clock.stop()
        
    else :
        
        opstat.set_status(False)
        opstat.set_errorMsg(errormsg)  
         
    if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS")) :
        add_debug_to_log("test_db_connector",print_to_string("[end] : opstat :  ",opstat.get_status()))
        
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                    SQLAlchemy Utilitie                        -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

def get_SQLAlchemy_engine(dblibid) : 
    
    if(dblibid == pymysql_library)                  :   return(dbConnector.SQLAlchemy_MySQL_pymysql_engine)
    elif(dblibid == mysql_connector_library)        :   return(dbConnector.SQLAlchemy_MySQL_mysqlconnector_engine)
    elif(dblibid == pyodbc_library)                 :   return(dbConnector.SQLAlchemy_MSSQL_pyodbc_engine)
    elif(dblibid == pymssql_library)                :   return(dbConnector.SQLAlchemy_MSSQL_pymssql_engine)
    elif(dblibid == sqlite_library)                 :   return(dbConnector.SQLAlchemy_SQLITE_sqlite_engine )
    elif(dblibid == sqlite3_library)                :   return(dbConnector.SQLAlchemy_SQLITE_sqlite3_engine)
    elif(dblibid == psycopg2_library)               :   return(dbConnector.SQLAlchemy_POSTGRESQL_psycopg2_engine)
    elif(dblibid == cx_oracle_library)              :   return(dbConnector.SQLAlchemy_ORACLE_cx_oracle_engine)
    elif(dblibid == Custom)                         :   return(dbConnector.SQLAlchemy_CUSTOM_engine)
    
    return(None)

def set_SQLAlchemy_engine(dblibid,engine) : 
    
    if(dblibid == pymysql_library)                  :   dbConnector.SQLAlchemy_MySQL_pymysql_engine = engine
    elif(dblibid == mysql_connector_library)        :   dbConnector.SQLAlchemy_MySQL_mysqlconnector_engine = engine
    elif(dblibid == pyodbc_library)                 :   dbConnector.SQLAlchemy_MSSQL_pyodbc_engine = engine
    elif(dblibid == pymssql_library)                :   dbConnector.SQLAlchemy_MSSQL_pymssql_engine = engine
    elif(dblibid == sqlite_library)                 :   dbConnector.SQLAlchemy_SQLITE_sqlite_engine = engine
    elif(dblibid == sqlite3_library)                :   dbConnector.SQLAlchemy_SQLITE_sqlite3_engine = engine 
    elif(dblibid == psycopg2_library)               :   dbConnector.SQLAlchemy_POSTGRESQL_psycopg2_engine = engine
    elif(dblibid == cx_oracle_library)              :   dbConnector.SQLAlchemy_ORACLE_cx_oracle_engine = engine
    elif(dblibid == Custom)                         :   dbConnector.SQLAlchemy_CUSTOM_engine = engine



def get_SQLAlchemy_connector_string(parmsdict) :
    """
    #------------------------------------------------------------------
    #   get sql alchemy connector string
    #
    #    parmsdict    -   sql parms dict 
    #
    #------------------------------------------------------------------
    """    
    
    dbConnectString = ""
    
    dblibid = parmsdict.get("dblibrary")
    
    if(dblibid == None) :
        dblibid = Custom
        
    if(dblibid == pymysql_library) :
        dbConnectString = ('mysql+pymysql://' + parmsdict.get("user") + ':' + 
                            parmsdict.get("password") + '@' + parmsdict.get("server") +
                            "/" + parmsdict.get("database"))
        
    elif(dblibid == mysql_connector_library) :
        dbConnectString = ('mysql+mysqlconnector://' + parmsdict.get("user") + ':' + 
                            parmsdict.get("password") + '@' + parmsdict.get("server")+
                            "/" + parmsdict.get("database"))

    elif(dblibid == pyodbc_library) :  
        import urllib
        connecturl = urllib.parse.quote_plus('DRIVER={SQL Server};' + 
                                             'SERVER=' + parmsdict.get("server") + ';' +
                                             'DATABASE=' + parmsdict.get("database") + ';' +
                                             'UID=' + parmsdict.get("user") + ';' +
                                             'PWD=' + parmsdict.get("password") )
        
        dbConnectString = ("mssql+pyodbc:///?odbc_connect="+connecturl)                

    elif(dblibid == pymssql_library) :             
        dbConnectString = ('mssql+pymssql://' + parmsdict.get("user") + ':' + 
                            parmsdict.get("password") + '@' + parmsdict.get("server") + '/' + 
                            parmsdict.get("database") + "?charset=utf8")
            
    elif(dblibid == sqlite3_library) :             
        dbConnectString = ('sqlite:///' + parmsdict.get("filename"))
            
    elif(dblibid == psycopg2_library) :             
        dbConnectString = ('postgresql+psycopg2://' + parmsdict.get("user") + ':' + 
                            parmsdict.get("password") + '@' + parmsdict.get("server") + '/' + 
                            parmsdict.get("database") )
        
    elif(dblibid == cx_oracle_library) :             
        dbConnectString = ('oracle+cx_oracle://' + parmsdict.get("user") + ':' + 
                            parmsdict.get("password") + '@' + parmsdict.get("server") )
        
    elif(dblibid == Custom) : 
        dbConnectString =   parmsdict.get("customdbconnectorstring") 

    if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
        add_debug_to_log("get_SQLAlchemy_connector_string",print_to_string(" parmsdict : \n     ",parmsdict))
        add_debug_to_log("get_SQLAlchemy_connector_string",print_to_string(" dbConnectString : \n     ",dbConnectString))
    

    return(dbConnectString)




# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                    DBConnector class                          -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class dbConnector :
    
    # static class SQLAlchemy engines
    SQLAlchemy_MySQL_pymysql_engine             =       None
    SQLAlchemy_MySQL_mysqlconnector_engine      =       None
    SQLAlchemy_MSSQL_pyodbc_engine              =       None
    SQLAlchemy_MSSQL_pymssql_engine             =       None
    SQLAlchemy_SQLITE_sqlite_engine             =       None
    SQLAlchemy_SQLITE_sqlite3_engine            =       None
    SQLAlchemy_POSTGRESQL_psycopg2_engine       =       None
    SQLAlchemy_ORACLE_cx_oracle_engine          =       None
    SQLAlchemy_CUSTOM_engine                    =       None

    # full constructor
    def __init__(self,
                 dbConn = None) :

        self.dbConn             =     None
        self.dbconnectParms     =     {}
        self.connectortype      =     None
        
    def get_dbConnection(self) :
        return(self.dbConn)
    def get_ConnectionParms(self) :
        return(self.dbconnectParms)
    def set_ConnectionParms(self,connectparms) :
        self.dbconnectParms = connectparms
    
    def connect_to_db(self,connectortype,opstat,inparms=None) :

        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS")) : 
            add_debug_to_log("connect_to_db",print_to_string(" connectortype : ",connectortype,"\n     inparms : \n     ",inparms))
    
        if((inparms != None)) :

            self.dbconnectParms   =   {}
            
            errormsg = validate_connection_parms(inparms)
            
            if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_TEST_CONNECTOR")) :
                add_debug_to_log("connect_to_db",print_to_string(" validate_connection_parms : errors  ",errormsg))
            
            if( errormsg == None) :
                dbcondict = grab_connection_parms(inparms)

                if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_TEST_CONNECTOR")) :
                    add_debug_to_log("connect_to_db",print_to_string("grab parms  \n",dbcondict))

                if(len(dbcondict) == 0) :

                    opstat.set_status(False)
                    opstat.set_errorMsg("Unable to build connect parms dict")
                    return(None)

                else :
                    self.set_ConnectionParms(dbcondict)

                if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_TEST_CONNECTOR")) :
                    add_debug_to_log("connect_to_db",print_to_string(" dbcondict \n  ",dbcondict))

            else :

                opstat.set_status(False)
                opstat.set_errorMsg(errormsg)
                return(None)
            
        else :
            
            if( (self.dbconnectParms == None) or (len(self.dbconnectParms) == 0) ) :
                opstat.set_status(False)
                opstat.set_errorMsg("No connector parms for connect")
                return(None)
             
        self.dbconnectParms.update({"contype":connectortype})

        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_TEST_CONNECTOR")) :
            add_debug_to_log("connect_to_db",print_to_string(" self.connectortype : ",self.dbconnectParms.get("contype"),"\n    dbconnectParms \n   ",self.dbconnectParms))
        
        if( self.dbconnectParms.get("contype") == NATIVE) :
            
            try :
                
                opstat.set_status(True)
                
                if(self.dbconnectParms.get("dblibrary") == pymysql_library) :
                    import pymysql
                    self.dbConn = pymysql.connect(host = self.dbconnectParms.get("server"), 
                                                  user = self.dbconnectParms.get("user"), 
                                                  passwd = self.dbconnectParms.get("password"),
                                                  db = self.dbconnectParms.get("database"))
                
                elif(self.dbconnectParms.get("dblibrary") == mysql_connector_library) :
                    import mysql.connector
                    self.dbConn = mysql.connector.connect(host = self.dbconnectParms.get("server"), 
                                                          user = self.dbconnectParms.get("user"), 
                                                          passwd = self.dbconnectParms.get("password"),
                                                          db = self.dbconnectParms.get("database"))
                
                elif(self.dbconnectParms.get("dblibrary") == pyodbc_library) :
                    import pyodbc
                    self.dbConn = pyodbc.connect("DRIVER={ODBC Driver 13 for SQL Server};SERVER=" + self.dbconnectParms.get("server") + ";" + 
                                                 "DATABASE=" + self.dbconnectParms.get("database") + ";" +
                                                 "UID=" + self.dbconnectParms.get("user") +";" + 
                                                 "PWD=" + self.dbconnectParms.get("password"))
                
                elif(self.dbconnectParms.get("dblibrary") == pymssql_library) :
                    import pymssql
                    self.dbConn = pymssql.connect(self.dbconnectParms.get("server") + ',' + 
                                                  self.dbconnectParms.get("user") + ',' +
                                                  self.dbconnectParms.get("password") +',' + 
                                                  self.dbconnectParms.get("database"))
                    
                elif(self.dbconnectParms.get("dblibrary") == sqlite_library) :
                    import sqlite
                    self.dbConn = sqlite.connect(self.dbconnectParms.get("filename"))
                    
                elif(self.dbconnectParms.get("dblibrary") == sqlite3_library) :
                    import sqlite3
                    self.dbConn = sqlite3.connect(self.dbconnectParms.get("filename"))
                    
                elif(self.dbconnectParms.get("dblibrary") == psycopg2_library) :
                    import psycopg2
                    self.dbConn = psycopg2.connect(dbname = self.dbconnectParms.get("database"),
                                                   user = self.dbconnectParms.get("user"),
                                                   password = self.dbconnectParms.get("password"))
                    
                elif(self.dbconnectParms.get("dblibrary") == cx_oracle_library) :
                    import cx_Oracle
                    self.dbConn = cx_Oracle.connect(dsn = self.dbconnectParms.get("server"),
                                                    user = self.dbconnectParms.get("user"),
                                                    password = self.dbconnectParms.get("password"))

                else :
                    opstat.set_status(False)
                    opstat.set_errorMsg("Invalid *dblibrary connect parm : " + self.dbconnectParms.get("dblibrary"))

            except Exception as e:
                opstat.store_exception("Unable to connect to database ",e)
                self.dbConn = None
                cfg.add_error_to_log("Unable to connect to database : " + opstat.get_exception_details_text(),1)

            
            return(self.dbConn)
        
        else : # SQLAlchemy connector

            if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_TEST_CONNECTOR")) :
                add_debug_to_log("connect_to_db",print_to_string("Testing SQLAlchemy : dblibrary : ",self.dbconnectParms.get("dblibrary")))
            
            try :
                
                from sqlalchemy import create_engine
                connectString = ""
                
                if(1):#get_SQLAlchemy_engine(self.dbconnectParms.get("dblibrary")) == None) :

                    if(self.dbconnectParms.get("dblibrary") == pymysql_library) :
                    
                        import pymysql
                        connectString = get_SQLAlchemy_connector_string(self.dbconnectParms)

                        if(not (self.dbconnectParms.get("schema") == None) ) :
                            connectString = (connectString + '/' + self.dbconnectParms.get("schema"))
                            
                    elif(self.dbconnectParms.get("dblibrary") == mysql_connector_library) :

                        import mysql.connector
                        connectString = get_SQLAlchemy_connector_string(self.dbconnectParms)

                        if(not (self.dbconnectParms.get("schema") == None) ) :
                            connectString = (connectString + '/' + self.dbconnectParms.get("schema"))

                    elif(self.dbconnectParms.get("dblibrary") == pyodbc_library) :
                    
                        import pyodbc
                        connectString = get_SQLAlchemy_connector_string(self.dbconnectParms)

                    elif(self.dbconnectParms.get("dblibrary") == pymssql_library) :

                        import pymssql
                        connectString = get_SQLAlchemy_connector_string(self.dbconnectParms)

                    elif(self.dbconnectParms.get("dblibrary") == sqlite3_library) :
                    
                        import sqlite3
                        connectString = get_SQLAlchemy_connector_string(self.dbconnectParms)

                    elif(self.dbconnectParms.get("dblibrary") == psycopg2_library) :
                    
                        import psycopg2
                        connectString = get_SQLAlchemy_connector_string(self.dbconnectParms)

                    elif(self.dbconnectParms.get("dblibrary") == cx_oracle_library) :
                    
                        import cx_Oracle
                        connectString = get_SQLAlchemy_connector_string(self.dbconnectParms)
                        
                    else :
                    
                        connectString = get_SQLAlchemy_connector_string(self.dbconnectParms)

                    if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_TEST_CONNECTOR")) :
                        add_debug_to_log("connect_to_db",print_to_string("SQLAlchemy connectString ",connectString,"\n",self.dbconnectParms))
                    
                    new_engine = create_engine(connectString, echo=False)
                    if(self.dbconnectParms.get("dblibrary") != None) :
                        set_SQLAlchemy_engine(self.dbconnectParms.get("dblibrary"),new_engine)
                    else :
                        set_SQLAlchemy_engine(Custom,new_engine)

                if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_TEST_CONNECTOR")) :
                    add_debug_to_log(" connect_to_db",print_to_string("SQLAlchemy connectString : ",connectString,"\n",self.dbconnectParms))

                # go ahead and get a connecton to the engine 
                if(self.dbconnectParms.get("dblibrary") != None) :   
                    self.dbConn = get_SQLAlchemy_engine(self.dbconnectParms.get("dblibrary")).connect() 
                else :
                    self.dbConn = get_SQLAlchemy_engine(Custom).connect() 
                        
                opstat.set_status(True)
            
            except Exception as e:
                opstat.store_exception("Unable to connect to database ",e)
                cfg.add_error_to_log("Unable to connect to database : " + opstat.get_exception_details_text(),1)

                self.dbConn = None
            
            return(self.dbConn)
            

    def close_dbConnection(self,opstat) :
        
        try :
            self.dbConn.close()
            self.dbConn = None

            if(self.dbconnectParms.get("dbid") == MySql) :   
                if(self.dbconnectParms.get("dblibrary") == pymysql_library) :   SQLAlchemy_MySQL_pymysql_engine  =  None
                else :    SQLAlchemy_MSSQL_pyodbc_engine                        =       None   
            elif(self.dbconnectParms.get("dbid") == MS_SQL_Server) :   
                if(self.dbconnectParms.get("dblibrary") == pyodbc_library) :   SQLAlchemy_MSSQL_pyodbc_engine  =  None
                else :    SQLAlchemy_MSSQL_pymssql_engine                       =       None   
            elif(self.dbconnectParms.get("dbid") == SQLite) :   
                if(self.dbconnectParms.get("dblibrary") == sqlite_library) :   SQLAlchemy_SQLITE_sqlite_engine  =  None
                else :    SQLAlchemy_SQLITE_sqlite3_engine                      =       None   
            elif(self.dbconnectParms.get("dbid") == Postgresql) :    SQLAlchemy_POSTGRESQL_psycopg2_engine  =  None
            elif(self.dbconnectParms.get("dbid") == Oracle)     :    SQLAlchemy_ORACLE_cx_oracle_engine  =  None
            else                                                :    SQLAlchemy_CUSTOM_engine  =  None

            opstat.set_status(True)
            
        except Exception as e:
            opstat.store_exception("Unable to close connection ",e)
            cfg.add_error_to_log("Unable to close connection : " + opstat.get_exception_details_text(),1)



"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Dataframe Cleanser db connector and history classes
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""

IMPORT_FLAG     =   0
EXPORT_FLAG     =   1

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                     DBConnector Parms class                   -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class DataframeCleanserDBConnectorParms :

    # instance variables
    
    db_id           =   None
    db_library      =   None
    server          =   None
    database        =   None
    user            =   None
    password        =   None
    
    
    # full constructor
    def __init__(self,db_id,db_library,server,database,user,password) :
        
        self.db_id          =   db_id
        self.db_library     =   db_library
        self.server         =   server
        self.database       =   database
        self.user           =   user
        self.password       =   password
        
        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :   
            add_debug_to_log("DataframeCleanserDBConnectorParms",print_to_string(" self",self.db_id ,self.db_library,self.server,self.database,self.user,self.password))     
        
    def get_db_id(self) :
        return(self.db_id)
    
    def get_db_library(self) :
        return(self.db_library)

    def get_server(self) :
        return(self.server)

    def get_database(self) :
        return(self.database)

    def get_user(self) :
        return(self.user)
    
    def get_password(self) :
        return(self.password)
    
    def does_match(self,dbconnector) :

        if( (dbconnector.get_db_id() == self.db_id) and 
            (dbconnector.get_db_library() == self.db_library) and
            (dbconnector.get_server() == self.server) and 
            (dbconnector.get_database() == self.database) and 
            (dbconnector.get_user() == self.user) and 
            (dbconnector.get_password() == self.password)) :
            
            return(True)
        
        else :

            return(False)
    
    def dump(self) :
        add_debug_to_log("db_utils",print_to_string("db_id       : ",type(self.db_id),self.db_id))
        add_debug_to_log("db_utils",print_to_string("db_library  : ",type(self.db_library),self.db_library))
        add_debug_to_log("db_utils",print_to_string("server      : ",type(self.server),self.server))
        add_debug_to_log("db_utils",print_to_string("database    : ",type(self.database),self.database))
        add_debug_to_log("db_utils",print_to_string("user        : ",type(self.user),self.user))
        add_debug_to_log("db_utils",print_to_string("password    : ",type(self.password),self.password))






# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                   DBConnectors Table class                    -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

class DataframeCleanserDBConnectors :
    
    # instance variables
    
    # notebook specific import history data
    connectors_file_loaded          =   False
    connectors_table                =   {}
    current_dbconnector             =   None
    current_export_dbconnector      =   None 
    
    # -----------------------------------------------------------------#
    # -  Dataframe Cleanser dbconnector table initialization methods  -#
    # -----------------------------------------------------------------#   

    # full constructor
    def __init__(self) :
        
        self.connectors_file_loaded             =   False
        self.connectors_table                   =   {}
        
        self.current_import_dbconnector_key     =   None
        self.current_export_dbconnector_key     =   None
        
        self.current_import_dbconnector         =   0
        self.current_export_dbconnector         =   0

        self.load_dbconnector_file()       


    # -----------------------------------------------------------------#
    # -    Dataframe Cleanser dbconnector table maintenance methods   -#
    # -----------------------------------------------------------------#   

    def get_dbconnector_dir_name(self) :
        
        import os
        
        from dfcleanser.common.cfg import DataframeCleansercfg
        dfcdir   =   DataframeCleansercfg.get_dfc_cfg_dir_name()
        return(dfcdir)
   
    def get_dbconnector_file_name(self) :

        import os
        
        dfcdir  =   self.get_dbconnector_dir_name()
         
        if(dfcdir is None) :
            return(None)
        else :
            return(os.path.join(dfcdir,"dfcleanserCommon_dbconnectors.json")) 

    def load_dbconnector_file(self) :
        
        import json
        import sys
        
        dbconnector_data        =   []
        dbconnector_dir_name    =   self.get_dbconnector_dir_name()
        dbconnector_file_name   =   self.get_dbconnector_file_name()
        
        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
            add_debug_to_log("db_utils",print_to_string("[load_dbconnector_file] : dbconnector_file_name : \n",dbconnector_file_name))
        
        if(not (dbconnector_dir_name is None)) :
            
            from dfcleanser.common.common_utils import does_dir_exist, make_dir
            if(not (does_dir_exist(dbconnector_dir_name))) :
                make_dir(dbconnector_dir_name)
            
            from dfcleanser.common.common_utils import does_file_exist
            if(not (does_file_exist(dbconnector_file_name))) :
                
                if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
                    add_debug_to_log("db_utils",print_to_string("[load_dbconnector_file] - file not found\n",dbconnector_file_name))
 
                self.connectors_file_loaded     =   False    
                self.connectors_table           =   {}
                
            # import history file does exist
            else :
                
                if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
                    add_debug_to_log("db_utils",print_to_string("load_dbconnector_file - file found\n",dbconnector_file_name))
                
                try :

                    with open(dbconnector_file_name,'r') as  dbconnector_file :
                            
                        dbconnector_data = json.load(dbconnector_file)
                        dbconnector_file.close()

                    if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
                        add_debug_to_log("db_utils",print_to_string("load_dbconnector_file - file loaded : ",type(dbconnector_data)))
                   
                    self._parse_dbconnector_file_to_dict(dbconnector_data)
                    self.history_file_loaded            =   True
                    self.current_dbconnector            =   dbconnector_data[0][0] 
                    self.current_export_dbconnector     =   dbconnector_data[0][0]
                        
                except :
                        
                    from dfcleanser.common.cfg import add_error_to_log, SEVERE_ERROR
                    add_error_to_log("[Load dbconnector file Error - for json decode error] "  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)
                    return()
                    
        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
            add_debug_to_log("db_utils",print_to_string("[load_dbconnector_file] - complete\n\n"))


    def save_dbconnector_file(self) :
        
        import json
        import sys
        
        dbconnector_data        =   []
        dbconnector_dir_name    =   self.get_dbconnector_dir_name()
        dbconnector_file_name   =   self.get_dbconnector_file_name()
            
        from dfcleanser.common.common_utils import does_dir_exist, make_dir
        if(not (does_dir_exist(dbconnector_dir_name))) :
            make_dir(dbconnector_dir_name)
            
        dbconnector_data        =   self._parse_dbconnector_dict_to_list()  
            
        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
            add_debug_to_log("db_utils",print_to_string("[save_dbconnector_file] : dbconnector_data\n"))
            for i in range(len(dbconnector_data)) :
                add_debug_to_log("db_utils",print_to_string("history",dbconnector_data[i]))
            
        try :
                    
            with open(dbconnector_file_name, 'w') as  dbconnector_file :
                json.dump(dbconnector_data,dbconnector_file)
                dbconnector_file.close()
                    
            if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
                add_debug_to_log("db_utils",print_to_string("[save_dbconnector_file] : dbconnector file saved ok"))

            self.load_dbconnector_file()
                            
        except :

            from dfcleanser.common.cfg import add_error_to_log, SEVERE_ERROR
            add_error_to_log("[save_dbconnector_file] : Error - see error log"  + str(sys.exc_info()[0].__name__),SEVERE_ERROR)
            
    def _parse_dbconnector_file_to_dict(self,dbconnector_file) :
        """
        * -------------------------------------------------------- 
        * function : convert the import history file into a dict
        * 
        * parms :
        *  history_file     -   history_file to convert                     
        *
        * returns : N/A
        * --------------------------------------------------------
        """
        
        total_entries    =   len(dbconnector_file)
        
        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
            add_debug_to_log("db_utils",print_to_string("_parse_dbconnector_file_to_dict  ",type(dbconnector_file),total_entries,"\n"))
            for i in range(total_entries) :
                add_debug_to_log("db_utils",print_to_string("[",i,"] ",dbconnector_file[i]))
        
        for i in range(total_entries) :
            
            dbcon_uuid          =   dbconnector_file[i][0]
            db_id               =   dbconnector_file[i][1]
            library             =   dbconnector_file[i][2]
            server              =   dbconnector_file[i][3]
            database            =   dbconnector_file[i][4]
            user                =   dbconnector_file[i][5]
            password            =   dbconnector_file[i][6]
                
            dbconnector_entry       =   DataframeCleanserDBConnectorParms(db_id,library,server,database,user,password)
            self.connectors_table.update({str(dbcon_uuid) : dbconnector_entry})

    
    def _add_entry_to_dbconnector_dict(self,dbcon_uuid,dbconnector_entry) :
        """
        * -------------------------------------------------------- 
        * function : add a dbconnector entry to the dict
        * 
        * parms :
        *  dbconnector_entry  -   dbconnector entry                     
        *
        * returns : N/A
        * --------------------------------------------------------
        """
        
        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
            add_debug_to_log("db_utils",print_to_string("[_add_entry_to_dbconnector_dict] : total dbcons : ",self.get_total_dbconnectors()))

        import uuid
        
        opstat  =   opStatus()
        
        try :
 
            connectors_keys     =   list(self.connectors_table.keys())
            match_key           =   None

            for i in range(len(connectors_keys)) :
                self.connectors_table.update({dbcon_uuid : dbconnector_entry})
        
        except Exception as e:
            opstat.store_exception("_add_entry_to_dbconnector_dict\n ",e)
            cfg.add_error_to_log("_add_entry_to_dbconnector_dict : " + opstat.get_exception_details_text(),1)


        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
            add_debug_to_log("db_utils",print_to_string("[_add_entry_to_dbconnector_dict] : total dbcons : ",self.get_total_dbconnectors()))


    def _parse_dbconnector_dict_to_list(self) :
        """
        * -------------------------------------------------------- 
        * function : convert the import history dict to a list 
        * 
        * parms :
        *
        * returns : N/A
        * --------------------------------------------------------
        """
        
        opstat  =   opStatus()
        
        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
            add_debug_to_log("db_utils",print_to_string("[_parse_dbconnector_dict_to_list]"))
        
        try :
        
            dbconnector_list    =   []

            dbconnector_keys    =   list(self.connectors_table.keys())

            for i in range(len(dbconnector_keys)) :

                current_dbconnector         =  self.connectors_table.get(dbconnector_keys[i])
                current_dconnnector_parms   =   [] 
                current_dconnnector_parms.append(str(dbconnector_keys[i]))
                current_dconnnector_parms.append(str(current_dbconnector.get_db_id()))
                current_dconnnector_parms.append(str(current_dbconnector.get_db_library()))
                current_dconnnector_parms.append(str(current_dbconnector.get_server()))
                current_dconnnector_parms.append(str(current_dbconnector.get_database()))
                current_dconnnector_parms.append(str(current_dbconnector.get_user()))
                current_dconnnector_parms.append(str(current_dbconnector.get_password()))

                dbconnector_list.append(current_dconnnector_parms)
         
            if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
                add_debug_to_log("db_utils",print_to_string("[_parse_dbconnector_dict_to_list] : dbconnector_list\n",dbconnector_list,"\n"))
                
            return(dbconnector_list)
    
        except Exception as e:
            opstat.store_exception("[_parse_dbconnector_dict_to_list]\n ",e)
            cfg.add_error_to_log("_parse_dbconnector_dict_to_list : " + opstat.get_exception_details_text(),1)

            return([])
    
    # -----------------------------------------------------------------#
    # -    Dataframe Cleanser dbconnector table getters - setters     -#
    # -----------------------------------------------------------------#   

    def get_dbconnectors_entries_list(self) :

        dbconnectors_list   =   self._parse_dbconnector_dict_to_list()  

        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
            add_debug_to_log("db_utils",print_to_string("[get_dbconnectors_entries_list] : dbconnector_list\n",dbconnectors_list,"\n"))
 
        return(dbconnectors_list)   

    def get_total_dbconnectors(self) :

        return(len(self.connectors_table))    
    
    def set_current_dbconnector(self,keytype,conindex) :

        if(keytype == IMPORT_FLAG) :
            self.current_import_dbconnector     =   conindex
        else :
            self.current_export_dbconnector     =   conindex  
 
    def set_current_dbconnector_key(self,keytype,dbconkey) :

        if(self.is_dbconnector_key_valid(dbconkey)) : 
            if(keytype == IMPORT_FLAG) :
                self.current_import_dbconnector_key     =   dbconkey
            else :
                self.current_export_dbconnector_key     =   dbconkey  
    
    def get_current_dbconnector_key(self,keytype) :

        if(keytype == IMPORT_FLAG) :
            return(self.current_import_dbconnector_key)
        else :
            return(self.current_export_dbconnector_key)  

    def get_current_dbconnector(self,keytype) :

        if(keytype == IMPORT_FLAG) :

            if(self.current_import_dbconnector_key is None) :
                return(None)
            else :           
                return(self.connectors_table.get(self.current_import_dbconnector_key))
            
        else :

            if(self.current_export_dbconnector_key is None) :
                return(None)
            else :
                return(self.connectors_table.get(self.current_export_dbconnector_key))            
    
    def add_dbconnector(self,connectparms) :

        import uuid
        dbconn_key  =   str(uuid.uuid4())

        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS")) :
            add_debug_to_log("db_utils",print_to_string("[add_dbconnector] : type : ",type(connectparms)))
            add_debug_to_log("db_utils",print_to_string("[add_dbconnector] : connectparms : \n  ",connectparms))


        if(not (type(connectparms) == list)) :
            
            if(connectparms.find("MySql") > -1) :           sqlservertype   =   get_db_id_from_dbid_title("MySql")
            elif(connectparms.find("MS SQL Server") > -1) : sqlservertype   =   get_db_id_from_dbid_title("MS SQL Server")
            elif(connectparms.find("SQLite") > -1) :        sqlservertype   =   get_db_id_from_dbid_title("SQLite")
            elif(connectparms.find("Postgresql") > -1) :    sqlservertype   =   get_db_id_from_dbid_title("Postgresql")
            elif(connectparms.find("Oracle") > -1) :        sqlservertype   =   get_db_id_from_dbid_title("Oracle")
            elif(connectparms.find("Custom") > -1) :        sqlservertype   =   get_db_id_from_dbid_title("Custom")
            else :                                          sqlservertype   =   None 
        
        else :

            cparms  =   []
            sqlservertype   =   int(connectparms[0])

        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS")) :
            add_debug_to_log("db_utils",print_to_string("[add_dbconnector] : connectparms : \n  ",connectparms))

        if(sqlservertype == MySql) :
            if(type(connectparms) == list) :
                new_dbconn  =   DataframeCleanserDBConnectorParms(connectparms[0],connectparms[1],connectparms[2],connectparms[3],connectparms[4],connectparms[5])  
            else :  
                cparms      =   get_parms_for_input(connectparms,mysql_connector_idList)
                new_dbconn  =   DataframeCleanserDBConnectorParms(sqlservertype,cparms[1],cparms[2],cparms[3],cparms[4],cparms[5])
        elif(sqlservertype == MS_SQL_Server) :
            if(type(connectparms) == list) :
                new_dbconn  =   DataframeCleanserDBConnectorParms(connectparms[0],connectparms[1],connectparms[2],connectparms[3],connectparms[4],connectparms[5])  
            else :  
                cparms      =   get_parms_for_input(connectparms,mssql_connector_idList)
                new_dbconn  =   DataframeCleanserDBConnectorParms(sqlservertype,cparms[1],cparms[2],cparms[3],cparms[4],cparms[5])
        elif(sqlservertype == SQLite) :
            if(type(connectparms) == list) :
                new_dbconn  =   DataframeCleanserDBConnectorParms(connectparms[0],connectparms[1],connectparms[2],"","","")  
            else :  
                cparms      =   get_parms_for_input(connectparms,sqlite_connector_idList)
                new_dbconn  =   DataframeCleanserDBConnectorParms(sqlservertype,cparms[1],cparms[2],"","","")
        elif(sqlservertype == Postgresql) :
            if(type(connectparms) == list) :
                new_dbconn  =   DataframeCleanserDBConnectorParms(connectparms[0],connectparms[1],connectparms[2],connectparms[3],connectparms[4],connectparms[5])  
            else :  
                cparms      =   get_parms_for_input(connectparms,Postgresql_connector_idList)
                new_dbconn  =   DataframeCleanserDBConnectorParms(sqlservertype,cparms[1],cparms[2],cparms[3],cparms[4],cparms[5])
        elif(sqlservertype == Oracle) :
            if(type(connectparms) == list) :
                new_dbconn  =   DataframeCleanserDBConnectorParms(connectparms[0],connectparms[1],connectparms[2],"",connectparms[3],connectparms[4])  
            else :  
                cparms      =   get_parms_for_input(connectparms,oracle_connector_idList)
                new_dbconn  =   DataframeCleanserDBConnectorParms(sqlservertype,cparms[1],cparms[2],"",cparms[3],cparms[4])
        elif(sqlservertype == Custom ) :
            if(type(connectparms) == list) :
                new_dbconn  =   DataframeCleanserDBConnectorParms(connectparms[0],connectparms[1],"","","","")  
            else :  
                cparms      =   get_parms_for_input(connectparms,custom_connector_idList)
                new_dbconn  =   DataframeCleanserDBConnectorParms(sqlservertype,cparms[1],"","","","")
        else :
            new_dbconn  =   None

        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS")) :
            add_debug_to_log("db_utils",print_to_string("[add_dbconnector] : cparms : \n",cparms))
            add_debug_to_log("db_utils",print_to_string("[add_dbconnector] : new_dbconn : \n",new_dbconn))

        if(not (new_dbconn is None)) :

            self.connectors_table.update({dbconn_key : new_dbconn})
            self.save_dbconnector_file()

        else :

            from dfcleanser.common.cfg import add_error_to_log, SEVERE_ERROR
            add_error_to_log("[Invalid dbconnector key to add] : ["  + ' '.join(parm_vals) + "]",SEVERE_ERROR)


    def delete_dbconnector(self,dbconkey) :

        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS")) :
            add_debug_to_log("db_utils",print_to_string("[delete_dbconnector] : dbconkey : ",dbconkey))

        if(self.is_dbconnector_key_valid(dbconkey)) :
            
            if(self.current_import_dbconnector_key == dbconkey) :
                self.current_import_dbconnector_key =   None
            if(self.current_export_dbconnector_key == dbconkey) :
                self.current_export_dbconnector_key =   None

            self.connectors_table.pop(dbconkey)
            self.save_dbconnector_file()
        
        else :

            from dfcleanser.common.cfg import add_error_to_log, SEVERE_ERROR
            add_error_to_log("[Invalid dbconnector key to delete] : ["  + dbconkey + "]",SEVERE_ERROR)

    
    def update_dbconnector(self,dbconn_key,connectparms) :
            
        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS")) :
            add_debug_to_log("db_utils",print_to_string("[update_dbconnector] : dbconn_key : ",dbconn_key,"\n  connectparms : \n  ",connectparms))
            add_debug_to_log("db_utils",print_to_string("[update_dbconnector] : total_dbconnectors ",self.get_total_dbconnectors(self)))

        self.connectors_table.update({dbconn_key : connectparms})
        
        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS_DBCONNECTORS")) :
            add_debug_to_log("db_utils",print_to_string("[update_dbconnector] : dbconnectors\n  ",self.get_dbconnectors_entries_list(),"\n"))

        self.save_dbconnector_file()
        
        if(is_debug_on(DBUtils_ID,"DEBUG_DBUTILS")) :
            add_debug_to_log("db_utils",print_to_string("[update_dbconnector] : end : total_dbconnectors ",self.get_total_dbconnectors(self)))


    def is_dbconnector_key_valid(self,dbconkey) :

        if( (not (dbconkey is None)) and (type(dbconkey) is str) and (len(dbconkey) > 0)) :

            dbconnector_keys    =   list(self.connectors_table.keys())

            for i in range(len(dbconnector_keys)) :
                if(dbconnector_keys[i] == dbconkey) :
                    return(True)
        
        from dfcleanser.common.cfg import add_error_to_log, SEVERE_ERROR
        add_error_to_log("[Invalid dbconnector key ] : ["  + str(dbconkey) + "]",SEVERE_ERROR)

        return(False)   


dfc_dbconnectors_table  =   DataframeCleanserDBConnectors()

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -                  DBConnectors Table class end                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# -             common database retrieval methods                 -#
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#


def fetch_rows(SQL_Server_Type_Id,dbcon,queryString,opstat,colid=0) :
    """
    * --------------------------------------------------------
    * function : fetch rows into a list
    * 
    * parms :
    *  SQL_Server_Type_Id   -   database id
    *  dbcon                -   database connector
    *  queryString          -   sql query to run
    *  opstat               -   op status container
    *  colid                -   column id
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    if(is_debug_on(DBUtils_ID,"DEBUG_SQL_DBUTILS")):
        add_debug_to_log("db_utils",print_to_string("[Qt_db_utils][fetch_rows] : SQL_Server_Type_Id : colid : ",SQL_Server_Type_Id,colid,"\n     querystring : \n      ",queryString))
    
    try :

        cursor          =   dbcon.get_dbConnection().cursor()
        crows           =   []
        number_of_rows  =   0
            
        if(SQL_Server_Type_Id == MySql) :

            if(dbcon.get_ConnectionParms().get("dblibrary") == pymysql_library) :
                number_of_rows = cursor.execute(queryString)
                crows = cursor.fetchall()
            else :
                cursor.execute(queryString)
                crows = cursor.fetchall()
                number_of_rows = len(crows)

        elif(SQL_Server_Type_Id == MS_SQL_Server) :
            
            cursor.execute(queryString)
            
            row = cursor.fetchone()
            while row:
                crows.append(row)
                number_of_rows = number_of_rows + 1
                row = cursor.fetchone()
            
        elif(SQL_Server_Type_Id == SQLite) :
                
            cursor.execute(queryString)    
            crows = cursor.fetchall()
            number_of_rows = len(crows)
                    
        elif(SQL_Server_Type_Id == Postgresql) :

            cursor.execute(queryString)    
            crows = cursor.fetchall()
            number_of_rows = len(crows)
            
        elif(SQL_Server_Type_Id == Oracle) :

            cursor.execute(queryString)
            for row in cursor.fetchall():
                number_of_rows = number_of_rows + 1    
                crows.append(row)
                
            cursor.close()
                
        else :

            number_of_rows = cursor.execute(queryString)
            crows = cursor.fetchall()
    
        if(is_debug_on(DBUtils_ID,"DEBUG_SQL_DBUTILS")):
            add_debug_to_log("db_utils",print_to_string("[Qt_db_utils][fetch_rows] : number_of_rows : ",number_of_rows))
            
        resultList = []
        for i in range(number_of_rows) :
            resultList.append(crows[i][colid])

        if(is_debug_on(DBUtils_ID,"DEBUG_SQL_DBUTILS")):
            add_debug_to_log("db_utils",print_to_string("[Qt_db_utils][fetch_rows] : len(results) :  ",len(resultList)))

    except Exception as e:
        opstat.store_exception("Unable to get rows ",e)
        cfg.add_error_to_log("Unable to get rows : " + opstat.get_exception_details_text(),1)

    if(opstat.get_status() ) :
        return(resultList) 
    else :
        return(None)


def get_table_names(dbcondict,opstat) :
    """
    * -------------------------------------------------------
    * function : get table names from a db
    * 
    * parms :
    *  dbid    -   database id
    *  opstat  -   op status container
    *
    * returns : N/A
    * --------------------------------------------------------
    """

    if(is_debug_on(DBUtils_ID,"DEBUG_SQL_DBUTILS")):
        add_debug_to_log("db_utils",print_to_string("[get_table_names] : dbcondict : \n  ",dbcondict))
    
    dbcon = dbConnector()
    dbcon.connect_to_db(NATIVE,opstat,dbcondict)
    
    if(not(opstat.get_status())) :

        from dfcleanser.sw_utilities.dfc_qt_model import get_exception_details_text

        details_msg     =   get_exception_details_text(opstat)
        details_msg     =   details_msg.replace("\n","<br>") 

        title       =   "dfcleanser exception"
        status_msg  =   "[get_table_names] db tables error " + details_msg
        from dfcleanser.sw_utilities.dfc_qt_model import display_exception
        display_exception(title,status_msg,opstat.get_exception())

        tableList   =   None
    
    else :

        current_dbid    =   int(dbcondict.get("servertype"))

        try :

            if(current_dbid == MySql) :
                gettablesquery = ("SELECT table_name FROM information_schema.tables WHERE table_schema = '" + 
                                   dbcondict.get("database") + "'")
            
            elif(current_dbid == MS_SQL_Server) :
                gettablesquery =  "SELECT Distinct TABLE_NAME FROM information_schema.TABLES where TABLE_TYPE = 'BASE TABLE'"
            
            elif(current_dbid == SQLite) : 
                gettablesquery = ("SELECT name FROM sqlite_master WHERE type='table'")
            
            elif(current_dbid == Postgresql) : 
                gettablesquery = ("SELECT tablename FROM pg_tables WHERE schemaname = 'public'")
            
            elif(current_dbid == Oracle) : 
                gettablesquery = ("SELECT table_name FROM user_tables")

            else :
                return(None)
       
            tableList = []
            tableList = fetch_rows(current_dbid,dbcon,gettablesquery,opstat) 
        
            if(opstat.get_status()) :
                if(current_dbid == SQLite) :
                    sqlitelist = []
                    for i in range(len(tableList)) :
                        if(tableList[i].find("sqlite") == -1) :
                            sqlitelist.append(tableList[i])

                    tableList = sqlitelist
            else :

                title       =   "dfcleanser exception"
                status_msg  =   "[get_table_names] db tables error "
                from dfcleanser.sw_utilities.dfc_qt_model import display_exception
                display_exception(title,status_msg,opstat.get_exception())

                tableList = None
            
            dbcon.close_dbConnection(opstat)
        
        except Exception as e:

            title       =   "dfcleanser exception"
            status_msg  =   "[get_table_names] fetch error "
            from dfcleanser.sw_utilities.dfc_qt_model import display_exception
            display_exception(title,status_msg,e)

            opstat.set_errorMsg("Unable to retrieve tables")
            tableList   =   None
    
        
    if(is_debug_on(DBUtils_ID,"DEBUG_SQL_DBUTILS")):
        add_debug_to_log("db_utils",print_to_string("[get_table_names] : tablelist : \n    ",tableList))

    return(tableList)  

    
def get_column_names(tablename, dbcondict, opstat) :
    """
    * --------------------------------------------------------
    * 
    * parms :
    *  dbid         -   database id
    *  tablename    -   table name
    *  opstat       -   op status container
    *
    * returns : N/A
    * --------------------------------------------------------
    """
    
    if(is_debug_on(DBUtils_ID,"DEBUG_SQL_DBUTILS")):
        add_debug_to_log("db_utils",print_to_string("[get_column_names] tablename : ",tablename))
    
    columnList = [] 
    
    if( len(tablename) == 0 ) :
        return(columnList)
    
    dbcon = dbConnector()
    dbcon.connect_to_db(NATIVE,opstat,dbcondict)

    SQL_Server_Type     =  dbcondict.get("servertype") 
    SQL_Server_Type_Id  =  int(SQL_Server_Type)
    

    if( (opstat.get_status()) and (len(tablename) > 0) ) :

        try :

            if(SQL_Server_Type_Id == MySql) :
        
                getcolumnsquery = ("SELECT column_name FROM information_schema.columns "  + 
                                    "where table_schema='" + dbcondict.get("database") + "'" + 
                                    " AND table_name = '" + tablename + "'")
            
            elif(SQL_Server_Type_Id == MS_SQL_Server) :
            
                getcolumnsquery = ("SELECT column_name FROM information_schema.columns " +  
                                    "WHERE table_name='" + tablename + "'")

            elif(SQL_Server_Type_Id == SQLite) : 
            
                getcolumnsquery = ("PRAGMA table_info(" + tablename + ")")

            elif(SQL_Server_Type_Id == Postgresql) : 
            
                getcolumnsquery = ("SELECT column_name FROM information_schema.columns " + 
                                    "WHERE table_schema = 'public' " + 
                                    "AND table_name = '" + tablename + "'")
            
            elif(SQL_Server_Type_Id == Oracle) : 
            
                getcolumnsquery = ("SELECT COLUMN_NAME from ALL_TAB_COLUMNS where TABLE_NAME='" + tablename + "'")
            
            else :

                opstat.set_errorMsg("Invalid DB ID for get columns")
                return(None)
    
            if(SQL_Server_Type_Id == SQLite) :
                columnList = fetch_rows(SQL_Server_Type_Id,dbcon,getcolumnsquery,opstat,1)
            else :
                columnList = fetch_rows(SQL_Server_Type_Id,dbcon,getcolumnsquery,opstat) 

        except :

            opstat.set_errorMsg("Unable to retrieUnable to retrieve columnsve columns")
            cfg.add_error_to_log("Unable to get rows : " ,1)
        
        
        if(not (opstat.get_status())) :
            columnList = None

        dbcon.close_dbConnection(opstat)
        
    else : 
        if(len(tablename) < 1) :
            opstat.set_errorMsg("Invalid Table Name")
         
    if(is_debug_on(DBUtils_ID,"DEBUG_SQL_DBUTILS")):
        add_debug_to_log("db_utils",print_to_string("[get_column_names]: columnList :  \n    ",columnList))
    
    return(columnList)  

































"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Dataframe Cleanser db connector widgets
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""






"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#    DB Connector Display functions
#------------------------------------------------------------------
#------------------------------------------------------------------
"""






