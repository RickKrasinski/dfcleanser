"""
# Database Utilities 
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:29:22 2017

@author: Rick
"""

from dfcleanser.common.table_widgets import (dcTable)

import dfcleanser.common.cfg as cfg

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
 
from dfcleanser.common.html_widgets import displayHeading, InputForm
from dfcleanser.common.common_utils import (display_status, display_exception, get_parms_for_input, display_generic_grid, RunningClock, opStatus)

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


def get_db_connector_idList(dbid) :
    
    if(dbid == MySql)               : return(mysql_connector_idList) 
    elif(dbid == MS_SQL_Server)     : return(mssql_connector_idList) 
    elif(dbid == SQLite)            : return(sqlite_connector_idList) 
    elif(dbid == Postgresql)        : return(Postgresql_connector_idList) 
    elif(dbid == Oracle)            : return(oracle_connector_idList) 
    elif(dbid == Custom)            : return(custom_connector_idList) 


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   mysql db connector parms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
mysql_connector_title               =   "MySql DB Connector Parameters"
mysql_connector_id                  =   "MySQLdbconnector"

mysql_connector_idList              =    ["sqlconservername",
                                          "sqlcondbname",
                                          "sqlconusername",
                                          "sqlconpassword",
                                          "sqldbcondblibid",
                                          None,None,None,None,None,None]

mysql_connector_typeList            =   ["text","text","text","text","text",
                                         "button","button","button","button","button","button"]

mysql_connector_placeholderList     =   ["enter host name",
                                         "enter database",
                                         "enter user name",
                                         "enter passsword",
                                         "enter the database connector library",
                                         None,None,None,None,None,None]

mysql_connector_reqList             =   [0,1,2,3,4]

"""
#--------------------------------------------------------------------------
#   MySQL import sqltable db connector parms
#--------------------------------------------------------------------------
"""
mysql_connector_labelList           =   ["hostname",
                                         "database",
                                         "username",
                                         "password",
                                         "dblibrary",
                                         "Import</br>Table",
                                         "Test</br>SQL</br>Connector",
                                         "Clear","Return",
                                         "Native</br>Help","SQL</br>Alchemy</br>Help"]

"""
#   pymysql lib db connector parms
"""
mysql_connector_jsList              =   [None,None,None,None,None,
                                         "pandas_sql_import_callback(0,0)",
                                         "pandas_details_test_con_callback(0,0,0)",
                                         "pandas_details_clear_callback(5)",
                                         "pandas_details_return_callback(0)",
                                         "display_help_url('"+str(PYMYSQL_CONNECTOR_URL)+"')",
                                         "display_help_url('"+str(PYMYSQL_CONNECTOR_SQLA_URL)+"')"]

"""
#   mysql lib db connector parms
"""
mysql_connector_mysql_jsList        =   [None,None,None,None,None,
                                         "pandas_sql_import_callback(0,0)",
                                         "pandas_details_test_con_callback(0,0,0)",
                                         "pandas_details_clear_callback(5)",
                                         "pandas_details_return_callback(0)",
                                         "display_help_url('"+str(MYSQL_CONNECTOR_URL)+"')",
                                         "display_help_url('"+str(MYSQL_CONNECTOR_SQLA_URL)+"')"]





"""
#--------------------------------------------------------------------------
#   MySQL import sqlquery db connector parms
#--------------------------------------------------------------------------
"""
mysql_query_connector_labelList     =   ["hostname",
                                         "database",
                                         "username",
                                         "password",
                                         "dblibrary",
                                         "Run</br>Import</br>Query",
                                         "Test</br>SQL</br>Connector",
                                         "Clear",
                                         "Return",
                                         "Native</br>Help",
                                         "SQL</br>Alchemy</br>Help"]

"""
#   pymysql lib db connector parms
"""
mysql_query_connector_jsList        =   [None,None,None,None,None,
                                         "pandas_sql_import_callback(1,0)",
                                         "pandas_details_test_con_callback(1,0,0)",
                                         "pandas_details_clear_callback(5)",
                                         "pandas_details_return_callback(0)",
                                         "display_help_url('"+str(PYMYSQL_CONNECTOR_URL)+"')",
                                         "display_help_url('"+str(PYMYSQL_CONNECTOR_SQLA_URL)+"')"]

"""
#   mysql lib db connector parms
"""
mysql_query_connector_mysql_jsList  =   [None,None,None,None,None,
                                         "pandas_sql_import_callback(1,0)",
                                         "pandas_details_test_con_callback(1,0,0)",
                                         "pandas_details_clear_callback(5)",
                                         "pandas_details_return_callback(0)",
                                         "display_help_url('"+str(MYSQL_CONNECTOR_URL)+"')",
                                         "display_help_url('"+str(MYSQL_CONNECTOR_SQLA_URL)+"')"]



"""
#--------------------------------------------------------------------------
#   MySQL export sqltable db connector parms
#--------------------------------------------------------------------------
"""
mysql_export_connector_labelList     =   ["hostname",
                                         "database",
                                         "username",
                                         "password",
                                         "dblibrary",
                                         "Export</br>Table",
                                         "Test</br>SQL</br>Connector",
                                         "Clear",
                                         "Return",
                                         "Native</br>Help",
                                         "SQL</br>Alchemy</br>Help"]

"""
#   pymysql lib db connector parms
"""
mysql_export_connector_jsList        =   [None,None,None,None,None,
                                         "pandas_sql_export_callback(0)",
                                         "pandas_details_export_test_con_callback(0,0)",
                                         "pandas_details_clear_callback(5)",
                                         "pandas_details_return_callback(1)",
                                         "display_help_url('"+str(PYMYSQL_CONNECTOR_URL)+"')",
                                         "display_help_url('"+str(PYMYSQL_CONNECTOR_SQLA_URL)+"')"]

"""
#   mysql lib db connector parms
"""
mysql_export_connector_mysql_jsList  =   [None,None,None,None,None,
                                         "pandas_sql_export_callback(0)",
                                         "pandas_details_export_test_con_callback(0,0)",
                                         "pandas_details_clear_callback(5)",
                                         "pandas_details_return_callback(1)",
                                         "display_help_url('"+str(MYSQL_CONNECTOR_URL)+"')",
                                         "display_help_url('"+str(MYSQL_CONNECTOR_SQLA_URL)+"')"]


"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   MS SQL Server db connector parms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
mssql_connector_title               =    "MS SQL Server DB Connector Parameters"
mssql_connector_id                  =    "MSSQLServerdbconnector"

mssql_connector_idList              =    ["sqlconservername",
                                          "sqlcondbname",
                                          "sqlconusername",
                                          "sqlconpassword",
                                          "sqldbcondblibid",
                                          None,None,None,None,None,None]

mssql_connector_typeList            =   ["text","text","text","text","text",
                                         "button","button","button","button","button","button"]

mssql_connector_placeholderList     = ["enter server name",
                                       "enter database name",
                                       "enter user name",
                                       "enter password",
                                       "enter the database connector library",
                                       None,None,None,None,None,None]

mssql_connector_reqList             =   [0,1,2,3,4]


"""
#--------------------------------------------------------------------------
#   MS SQL Server import sqltable db connector parms
#--------------------------------------------------------------------------
"""
mssql_connector_labelList           =   ["msserver",
                                         "msdatabase",
                                         "msusername",
                                         "mspassword",
                                         "dblibrary",
                                         "Import</br>Table",
                                         "Test</br>SQL</br>Connector",
                                         "Clear",
                                         "Return",
                                         "Native</br>Help",
                                         "SQL</br>Alchemy</br>Help"]

"""
#   pyodbc lib db connector parms
"""
mssql_connector_jsList              =  [None,None,None,None,None,
                                        "pandas_sql_import_callback(0,1)",
                                        "pandas_details_test_con_callback(0,1,0)",
                                        "pandas_details_clear_callback(5)",
                                        "pandas_details_return_callback(0)",
                                        "display_help_url('"+str(PYODBC_CONNECTOR_URL)+"')",
                                        "display_help_url('"+str(PYODBC_CONNECTOR_SQLA_URL)+"')"]

"""
#   pymssql lib db connector parms
"""
mssql_connector_pymssql_jsList      =  [None,None,None,None,None,
                                        "pandas_sql_import_callback(0,1)",
                                        "pandas_details_test_con_callback(0,1,0)",
                                        "pandas_details_clear_callback(5)",
                                        "pandas_details_return_callback(0)",
                                        "display_help_url('"+str(PYMSSQL_CONNECTOR_URL)+"')",
                                        "display_help_url('"+str(PYMSSQL_CONNECTOR_SQLA_URL)+"')"]

"""
#--------------------------------------------------------------------------
#   MS SQL Server import sqlquery db connector parms
#--------------------------------------------------------------------------
"""
mssql_query_connector_labelList     =   ["msserver",
                                         "msdatabase",
                                         "msusername",
                                         "mspassword",
                                         "dblibrary",
                                         "Run</br>Import</br>Query",
                                         "Test</br>SQL</br>Connector",
                                         "Clear",
                                         "Return",
                                         "Native</br>Help",
                                         "SQL</br>Alchemy</br>Help"]

"""
#   pyodbc lib db connector parms
"""
mssql_query_connector_jsList        =  [None,None,None,None,None,
                                        "pandas_sql_import_callback(1,1)",
                                        "pandas_details_test_con_callback(1,1,0)",
                                        "pandas_details_clear_callback(5)",
                                        "pandas_details_return_callback(0)",
                                        "display_help_url('"+str(PYODBC_CONNECTOR_URL)+"')",
                                        "display_help_url('"+str(PYODBC_CONNECTOR_SQLA_URL)+"')"]

"""
#   pymssql lib db connector parms
"""
mssql_query_connector_pymssql_jsList =  [None,None,None,None,None,
                                        "pandas_sql_import_callback(1,1)",
                                        "pandas_details_test_con_callback(1,1,0)",
                                        "pandas_details_clear_callback(5)",
                                        "pandas_details_return_callback(0)",
                                        "display_help_url('"+str(PYMSSQL_CONNECTOR_URL)+"')",
                                        "display_help_url('"+str(PYMSSQL_CONNECTOR_SQLA_URL)+"')"]

"""
#--------------------------------------------------------------------------
#   MS SQL Server export sqltable db connector parms
#--------------------------------------------------------------------------
"""
mssql_export_connector_labelList     =   ["msserver",
                                         "msdatabase",
                                         "msusername",
                                         "mspassword",
                                         "dblibrary",
                                         "Export</br>Dataframe",
                                         "Test</br>SQL</br>Connector",
                                         "Clear",
                                         "Return",
                                         "Native</br>Help",
                                         "SQL</br>Alchemy</br>Help"]

"""
#   pyodbc lib db connector parms
"""
mssql_export_connector_jsList        =  [None,None,None,None,None,
                                        "pandas_sql_export_callback(1)",
                                        "pandas_details_export_test_con_callback(1,0)",
                                        "pandas_details_clear_callback(5)",
                                        "pandas_details_return_callback(1)",
                                        "display_help_url('"+str(PYODBC_CONNECTOR_URL)+"')",
                                        "display_help_url('"+str(PYODBC_CONNECTOR_SQLA_URL)+"')"]

"""
#   pymssql lib db connector parms
"""
mssql_export_connector_pymssql_jsList =  [None,None,None,None,None,
                                        "pandas_sql_export_callback(1)",
                                        "pandas_details_export_test_con_callback(1,0)",
                                        "pandas_details_clear_callback(5)",
                                        "pandas_details_return_callback(1)",
                                        "display_help_url('"+str(PYMSSQL_CONNECTOR_URL)+"')",
                                        "display_help_url('"+str(PYMSSQL_CONNECTOR_SQLA_URL)+"')"]

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   Postgresql db connector parms
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
Postgresql_connector_title          =   "Postgresql DB Connector Parameters"
Postgresql_connector_id             =   "Postgresqldbconnector"

Postgresql_connector_idList         =    ["sqlconservername",
                                          "sqlcondbname",
                                          "sqlconusername",
                                          "sqlconpassword",
                                          "sqldbcondblibid",
                                          None,None,None,None,None,None]

Postgresql_connector_typeList       =   ["text","text","text","text","text",
                                         "button","button","button","button","button","button"]

Postgresql_connector_placeholderList = ["enter server name",
                                        "enter database name",
                                        "enter user name",
                                        "enter password",
                                        "enter the database connector library",
                                        None,None,None,None,None,None]

Postgresql_connector_reqList        =   [0,1,2,3,4]

"""
#--------------------------------------------------------------------------
#   Postgres import sqltable db connector parms
#--------------------------------------------------------------------------
"""
Postgresql_connector_labelList      =   ["pghost",
                                         "pgdbname",
                                         "pguser",
                                         "pgpassword",
                                         "dblibrary",
                                         "Import</br>Table",
                                         "Test</br>SQL</br>Connector",
                                         "Clear",
                                         "Return",
                                         "Native</br>Help",
                                         "SQL</br>Alchemy</br>Help"]

Postgresql_connector_jsList         =   [None,None,None,None,None,
                                         "pandas_sql_import_callback(0,3)",
                                         "pandas_details_test_con_callback(0,3,0)",
                                         "pandas_details_clear_callback(5)",
                                         "pandas_details_return_callback(0)",
                                         "display_help_url('"+str(POSTGRESQL_CONNECTOR_URL)+"')",
                                         "display_help_url('"+str(POSTGRESQL_CONNECTOR_SQLA_URL)+"')"]


"""
#--------------------------------------------------------------------------
#   Postgres import sqlquery db connector parms
#--------------------------------------------------------------------------
"""
Postgresql_query_connector_labelList=   ["pghost",
                                         "pgdbname",
                                         "pguser",
                                         "pgpassword",
                                         "dblibrary",
                                         "Run</br>Import</br>Query",
                                         "Test</br>SQL</br>Connector",
                                         "Clear",
                                         "Return",
                                         "Native</br>Help",
                                         "SQL</br>Alchemy</br>Help"]

Postgresql_query_connector_jsList   =   [None,None,None,None,None,
                                         "pandas_sql_import_callback(1,3)",
                                         "pandas_details_test_con_callback(1,3,0)",
                                         "pandas_details_clear_callback(5)",
                                         "pandas_details_return_callback(0)",
                                         "display_help_url('"+str(POSTGRESQL_CONNECTOR_URL)+"')",
                                         "display_help_url('"+str(POSTGRESQL_CONNECTOR_SQLA_URL)+"')"]

"""
#--------------------------------------------------------------------------
#   Postgres export sqltable db connector parms
#--------------------------------------------------------------------------
"""
Postgresql_export_connector_labelList=   ["pghost",
                                         "pgdbname",
                                         "pguser",
                                         "pgpassword",
                                         "dblibrary",
                                         "Export</br>Dataframe",
                                         "Test</br>SQL</br>Connector",
                                         "Clear",
                                         "Return",
                                         "Native</br>Help",
                                         "SQL</br>Alchemy</br>Help"]

Postgresql_export_connector_jsList   =   [None,None,None,None,None,
                                         "pandas_sql_export_callback(3)",
                                         "pandas_details_export_test_con_callback(3,0)",
                                         "pandas_details_clear_callback(5)",
                                         "pandas_details_return_callback(1)",
                                         "display_help_url('"+str(POSTGRESQL_CONNECTOR_URL)+"')",
                                         "display_help_url('"+str(POSTGRESQL_CONNECTOR_SQLA_URL)+"')"]



"""
#--------------------------------------------------------------------------
#   sqlite db connector input form components
#--------------------------------------------------------------------------
"""
sqlite_connector_title              =   "SQLite DB Connector Parameters"
sqlite_connector_id                 =   "SQLitedbconnector"

sqlite_connector_idList             =    ["SQLitedbfileName",
                                          "SQLitedblibid",
                                          None,None,None,None,None,None]

sqlite_connector_typeList           =   ["text","text",
                                         "button","button","button","button","button","button"]

sqlite_connector_placeholderList    =   ["enter the db file name",
                                         "enter the database connector library",
                                         None,None,None,None,None,None]

sqlite_connector_reqList            =   [0,1,2,3,4]

"""
#--------------------------------------------------------------------------
#   sqlite import sqltable db connector parms
#--------------------------------------------------------------------------
"""
sqlite_connector_labelList          =   ["db_file",
                                         "dblibrary",
                                         "Import</br>Table",
                                         "Test</br>SQL</br>Connector",
                                         "Clear","Return",
                                         "Native</br>Help",
                                         "SQL</br>Alchemy</br>Help"]

sqlite_connector_jsList             =   [None,None,
                                         "pandas_sql_import_callback(0,2)",
                                         "pandas_details_test_con_callback(0,2,0)",
                                         "pandas_details_test_con_callback(0,2,1)",
                                         "pandas_details_clear_callback(5)",
                                         "pandas_details_return_callback(0)",
                                         "display_help_url('"+str(SQLITE_CONNECTOR_URL)+"')",
                                         "display_help_url('"+str(SQLITE_CONNECTOR_SQLA_URL)+"')"]

"""
#--------------------------------------------------------------------------
#   sqlite import sqlquery db connector parms
#--------------------------------------------------------------------------
"""
sqlite_query_connector_labelList    =   ["db_file",
                                         "dblibrary",
                                         "Run</br>Import</br>Query",
                                         "Test</br>SQL</br>Connector",
                                         "Clear","Return",
                                         "Native</br>Help",
                                         "SQL</br>Alchemy</br>Help"]

sqlite_query_connector_jsList       =   [None,None,
                                         "pandas_sql_import_callback(1,2)",
                                         "pandas_details_test_con_callback(1,2,0)",
                                         "pandas_details_test_con_callback(1,2,1)",
                                         "pandas_details_clear_callback(5)",
                                         "pandas_details_return_callback(0)",
                                         "display_help_url('"+str(SQLITE_CONNECTOR_URL)+"')",
                                         "display_help_url('"+str(SQLITE_CONNECTOR_SQLA_URL)+"')"]

"""
#--------------------------------------------------------------------------
#   sqlite export sqltable db connector parms
#--------------------------------------------------------------------------
"""
sqlite_export_connector_labelList    =   ["db_file",
                                         "dblibrary",
                                         "Export</br>Dataframe",
                                         "Test</br>SQL</br>Connector",
                                         "Clear","Return",
                                         "Native</br>Help",
                                         "SQL</br>Alchemy</br>Help"]

sqlite_export_connector_jsList       =   [None,None,
                                         "pandas_sql_export_callback(2)",
                                         "pandas_details_export_test_con_callback(2,0)",
                                         "pandas_details_export_test_con_callback(2,1)",
                                         "pandas_details_clear_callback(5)",
                                         "pandas_details_return_callback(1)",
                                         "display_help_url('"+str(SQLITE_CONNECTOR_URL)+"')",
                                         "display_help_url('"+str(SQLITE_CONNECTOR_SQLA_URL)+"')"]

"""
#--------------------------------------------------------------------------
#   Oracle db connector parms
#--------------------------------------------------------------------------
"""
oracle_connector_title              =   "Oracle DB Connector Parameters"
oracle_connector_id                 =   "Oracledbconnector"

oracle_connector_idList             =    ["sqlconservername",
                                          "sqlconusername",
                                          "sqlconpassword",
                                          "sqldbcondblibid",
                                          None,None,None,None,None,None]

oracle_connector_typeList           =   ["text","text","text","text",
                                         "button","button","button","button","button","button"]

oracle_connector_placeholderList    =   ["enter server name",
                                         "enter database name",
                                         "enter password",
                                         "enter the database connector library",
                                         None,None,None,None,None,None]

oracle_connector_reqList            =   [0,1,2,3]


"""
#--------------------------------------------------------------------------
#   oracle import sqltable db connector parms
#--------------------------------------------------------------------------
"""
oracle_connector_labelList          =   ["tdshost",
                                         "user",
                                         "password",
                                         "dblibrary",
                                         "Import</br>Table",
                                         "Test</br>SQL</br>Connector",
                                         "Clear","Return",
                                         "Native</br>Help",
                                         "SQL</br>Alchemy</br>Help"]

oracle_connector_jsList             =   [None,None,None,None,
                                         "pandas_sql_import_callback(0,4)",
                                         "pandas_details_test_con_callback(0,4,0)",
                                         "pandas_details_clear_callback(5)",
                                         "pandas_details_return_callback(0)",
                                         "display_help_url('"+str(ORACLE_CONNECTOR_URL)+"')",
                                         "display_help_url('"+str(ORACLE_CONNECTOR_SQLA_URL)+"')"]

"""
#--------------------------------------------------------------------------
#   oracle import sqlquery db connector parms
#--------------------------------------------------------------------------
"""
oracle_query_connector_labelList    =   ["tdshost",
                                         "user",
                                         "password",
                                         "dblibrary",
                                         "Run</br>Import</br>Query",
                                         "Test</br>SQL</br>Connector",
                                         "Clear","Return",
                                         "Native</br>Help","SQL</br>Alchemy</br>Help"]

oracle_query_connector_jsList       =   [None,None,None,None,
                                         "pandas_sql_import_callback(1,4)",
                                         "pandas_details_test_con_callback(1,4,0)",
                                         "pandas_details_clear_callback(5)",
                                         "pandas_details_return_callback(0)",
                                         "display_help_url('"+str(ORACLE_CONNECTOR_URL)+"')",
                                         "display_help_url('"+str(ORACLE_CONNECTOR_SQLA_URL)+"')"]

"""
#--------------------------------------------------------------------------
#   oracle export sqltable db connector parms
#--------------------------------------------------------------------------
"""
oracle_export_connector_labelList    =   ["tdshost",
                                         "user",
                                         "password",
                                         "dblibrary",
                                         "Export</br>Dataframe",
                                         "Test</br>SQL</br>Connector",
                                         "Clear","Return",
                                         "Native</br>Help","SQL</br>Alchemy</br>Help"]

oracle_export_connector_jsList       =   [None,None,None,None,
                                         "pandas_sql_export_callback(4)",
                                         "pandas_details_export_test_con_callback(4,0)",
                                         "pandas_details_clear_callback(5)",
                                         "pandas_details_return_callback(1)",
                                         "display_help_url('"+str(ORACLE_CONNECTOR_URL)+"')",
                                         "display_help_url('"+str(ORACLE_CONNECTOR_SQLA_URL)+"')"]

"""
#--------------------------------------------------------------------------
#   custom db connector parms
#--------------------------------------------------------------------------
"""
custom_connector_title              =   "Custom DB Connector Parameters"
custom_connector_id                 =   "customdbconnector"

custom_connector_idList             =    ["dbconnectorstring",
                                          None,None,None,None,None]

custom_connector_labelList          =   ["SQLAlchemy db connector string",
                                         "Import</br>Table",
                                         "Test</br>SQLAlchemy</br>Connector",
                                         "Clear","Return","Help"]

custom_query_connector_labelList    =   ["SQLAlchemy db connector string",
                                         "Run</br>Import</br>Query",
                                         "Test</br>SQLAlchemy</br>Connector",
                                         "Clear","Return","Help"]

custom_export_connector_labelList    =   ["SQLAlchemy db connector string",
                                         "Export</br>Dataframe",
                                         "Test</br>SQLAlchemy</br>Connector",
                                         "Clear","Return","Help"]

custom_connector_typeList           =   ["text",
                                         "button","button","button","button","button"]

custom_connector_placeholderList    =   ["enter connector string",
                                         None,None,None,None,None]

custom_connector_jsList             =   [None,
                                         "pandas_sql_import_callback(0,5)",
                                         "pandas_details_test_con_callback(0,5,1)",
                                         "pandas_details_clear_callback()",
                                         "pandas_details_return_callback(0)",
                                         "displayhelp(('" + str(IMPORT_CUSTOM_ID) + "')"]

custom_query_connector_jsList       =   [None,
                                         "pandas_details_test_con_callback(1,5)",
                                         "pandas_details_test_con_callback(1,5,1)",
                                         "pandas_details_clear_callback()",
                                         "pandas_details_return_callback(0)",
                                         "displayhelp(('" + str(IMPORT_CUSTOM_ID) + "')"]

custom_export_connector_jsList       =   [None,
                                         "pandas_sql_export_callback(5)",
                                         "pandas_details_export_test_con_callback(5,1)",
                                         "pandas_details_clear_callback()",
                                         "pandas_details_return_callback(0)",
                                         "displayhelp(('" + str(IMPORT_CUSTOM_ID) + "')"]

custom_connector_reqList            =   [0]


MYSQL_DBCON_PARMS                    =   mysql_connector_id + "Parms"
MSSQL_DBCON_PARMS                    =   mssql_connector_id + "Parms"
SQLITE_DBCON_PARMS                   =   sqlite_connector_id + "Parms"
POSTGRESQL_DBCON_PARMS               =   Postgresql_connector_id + "Parms"
ORACLE_DBCON_PARMS                   =   oracle_connector_id + "Parms"
CUSTOM_DBCON_PARMS                   =   custom_connector_id + "Parms"

def get_db_id_title(dbid) :
    
    if(dbid == MySql)           :   return("MySql")
    elif(dbid == MS_SQL_Server) :   return("MS SQL Server")
    elif(dbid == SQLite)        :   return("SQLite3")
    elif(dbid == Postgresql)    :   return("Postgresql")
    elif(dbid == Oracle)        :   return("Oracle")
    else : return("  ")

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   connector types
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
NATIVE          =   0
SQLALCHEMY      =   1

SQL_IMPORT      =   0
SQL_QUERY       =   1
SQL_EXPORT      =   2

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   database connectors
#--------------------------------------------------------------------------
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
#------------------------------------------------------------------
#   get a db connector dict from input form or default
#
#    dbid           -   database id 
#    formparmsList  -   input form parms
#
#------------------------------------------------------------------
""" 
def get_dbcondict(dbid,formparmsList) :
    
    dbconpList = []
    dbcondict  = {}
    
    if(formparmsList == None) :
        
        dbconpList = get_stored_con_Parms(dbid)
        #dbconpList = get_config_value(cfgname)
    
    else :
        dbconpList = formparmsList

    if(dbid == MySql)                   :   labellist =  mysql_connector_labelList
    elif( (dbid == MS_SQL_Server) )     :   labellist =  mssql_connector_labelList
    elif( (dbid == SQLite) )            :   labellist =  sqlite_query_connector_labelList
    elif( (dbid == Postgresql) )        :   labellist =  Postgresql_connector_labelList
    elif( (dbid == Oracle) )            :   labellist =  oracle_connector_labelList
    elif( (dbid == Custom) )            :   labellist =  custom_connector_labelList
    
    for i in range(len(dbconpList)) :
        dbcondict.update({labellist[i]:dbconpList[i]})
    
    return(dbcondict)


"""
#------------------------------------------------------------------
#   parse the sql parms
#
#    sqlinputparms      -   input parm list 
#    dbparms            -   parms dict 
#
#------------------------------------------------------------------
"""    
def parse_connector_parms(sqlinputparms,dbid,dbparms) :


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
  
    sqllist = get_parms_for_input(sqlinputparms,idlist)
    
    for i in range(len(sqllist)) :
        dbparms.update({labellist[i]:sqllist[i]})    

    return(sqllist)
    
"""
#------------------------------------------------------------------
#   get a table for the dbconnector options
#
#------------------------------------------------------------------
""" 
def get_db_connector_table(forExport=False) :
    
    dblibslistHeader        =   [""]
    dblibslistRows          =   []
    dblibslistWidths        =   [100]
    dblibslistAligns        =   ["left"]
    dblibslistHrefs         =   []

    dblibstexts     =   ["MySql",
                         "&nbsp;&nbsp;&nbsp;&nbsp;"+pymysql_library,
                         "&nbsp;&nbsp;&nbsp;&nbsp;"+mysql_connector_library,
                         "MS SQL Server",
                         "&nbsp;&nbsp;&nbsp;&nbsp;"+pyodbc_library,
                         "&nbsp;&nbsp;&nbsp;&nbsp;"+pymssql_library,
                         "SQLite",
                         "&nbsp;&nbsp;&nbsp;&nbsp;"+sqlite3_library,
                         "PostGresql",
                         "&nbsp;&nbsp;&nbsp;&nbsp;"+psycopg2_library,
                         "Oracle",
                         "&nbsp;&nbsp;&nbsp;&nbsp;"+cx_oracle_library,
                         "Custom"]
    
    if(forExport) :
        dblibshrefs    =    [None,"select_export_db","select_export_db",None,
                             "select_export_db","select_export_db",None,
                             "select_export_db",None,"select_export_db",None,
                             "select_export_db","select_custom"]
    else :
        dblibshrefs    =    [None,"select_db","select_db",None,"select_db","select_db",
                             None,"select_db",None,"select_db",None,"select_db",
                             "select_custom"]
    
    for i in range(len(dblibstexts)) :
        dblibslistRows.append([dblibstexts[i]])    
        dblibslistHrefs.append([dblibshrefs[i]])
        
    dblibs_names_table = dcTable("DB Connectors","dbconnectorsTable",
                                 cfg.DataImport_ID,
                                 dblibslistHeader,dblibslistRows,
                                 dblibslistWidths,dblibslistAligns)

    dblibs_names_table.set_refList(dblibslistHrefs)
        
    dblibs_names_table.set_rowspertable(len(dblibstexts))
    dblibs_names_table.set_small(True)
    dblibs_names_table.set_smallwidth(98)
    dblibs_names_table.set_smallmargin(10)

    dblibs_names_table.set_border(True)
    dblibs_names_table.set_checkLength(False)

    listHtml = dblibs_names_table.get_html()
    
    return(listHtml)
    
    
"""
#------------------------------------------------------------------
#   display db connector inputs form
#
#------------------------------------------------------------------
"""     
def display_db_connector_inputs(dbid,dbconparms,sqlid,owner=None) :
    
    #print("display_db_connector_inputs",dbid,sqlid)
    print("\n")
    
    if(sqlid == SQL_EXPORT) :
        listHtml = get_db_connector_table(True)
    else :
        listHtml = get_db_connector_table(False) 

    db_con_input_form = None
    
    if(dbid == None) :
        
        cfg.set_config_value(cfg.CURRENT_DB_ID_KEY,MySql)
        dbid = MySql
        dblib = pymysql_library
        
    if(dbid == MySql) :
        
        dblib = dbconparms[4]
        
        if(sqlid == SQL_IMPORT) :
            
            if(dblib == pymysql_library) :
                db_con_jslist = mysql_connector_jsList
            else :
                db_con_jslist = mysql_connector_mysql_jsList
                
            db_con_input_form   =   InputForm(mysql_connector_id,
                                              mysql_connector_idList,
                                              mysql_connector_labelList,
                                              mysql_connector_typeList,
                                              mysql_connector_placeholderList,
                                              db_con_jslist,
                                              mysql_connector_reqList)
            
        elif(sqlid == SQL_QUERY) :
            
            db_con_labelist  =   mysql_query_connector_labelList    
            
            if(dblib == pymysql_library) :
                db_con_jslist = mysql_query_connector_jsList
            else :
                db_con_jslist = mysql_query_connector_mysql_jsList

            db_con_input_form   =   InputForm(mysql_connector_id,
                                              mysql_connector_idList,
                                              db_con_labelist,
                                              mysql_connector_typeList,
                                              mysql_connector_placeholderList,
                                              db_con_jslist,
                                              mysql_connector_reqList)
            
        else : #sqlid == SQL_EXPORT
            
            db_con_labelist     =   mysql_export_connector_labelList
            
            if(dblib == pymysql_library) :
                db_con_jslist       =   mysql_export_connector_jsList
            else :
                db_con_jslist       =   mysql_export_connector_mysql_jsList

            db_con_input_form   =   InputForm(mysql_connector_id,
                                              mysql_connector_idList,
                                              db_con_labelist,
                                              mysql_connector_typeList,
                                              mysql_connector_placeholderList,
                                              db_con_jslist,
                                              mysql_connector_reqList)
            
    elif(dbid == MS_SQL_Server) :
        
        dblib = dblib = dbconparms[4]
        
        if(sqlid == SQL_IMPORT) :
            
            if(dblib == pyodbc_library) :
                db_con_jslist = mssql_connector_jsList
            else :
                db_con_jslist = mssql_connector_pymssql_jsList
             
            db_con_input_form   =   InputForm(mssql_connector_id,
                                              mssql_connector_idList,
                                              mssql_connector_labelList,
                                              mssql_connector_typeList,
                                              mssql_connector_placeholderList,
                                              db_con_jslist,
                                              mssql_connector_reqList)
            
        elif(sqlid == SQL_QUERY) :
            
            if(dblib == pyodbc_library) :
                db_con_jslist = mssql_query_connector_jsList
            else :
                db_con_jslist = mssql_query_connector_pymssql_jsList
                
            db_con_input_form   =   InputForm(mssql_connector_id,
                                              mssql_connector_idList,
                                              mssql_query_connector_labelList,
                                              mssql_connector_typeList,
                                              mssql_connector_placeholderList,
                                              db_con_jslist,
                                              mssql_connector_reqList)
            
        else : #sqlid == SQL_EXPORT
            
            if(dblib == pyodbc_library) :
                db_con_jslist = mssql_export_connector_jsList
            else :
                db_con_jslist = mssql_export_connector_pymssql_jsList
            
            db_con_input_form   =   InputForm(mssql_connector_id,
                                              mssql_connector_idList,
                                              mssql_export_connector_labelList,
                                              mssql_connector_typeList,
                                              mssql_connector_placeholderList,
                                              db_con_jslist,
                                              mssql_connector_reqList)          
        
    elif(dbid == SQLite) :
        
        dblib = dblib = dbconparms[1]
        
        if(sqlid == SQL_IMPORT) :
            db_con_input_form   =   InputForm(sqlite_connector_id,
                                              sqlite_connector_idList,
                                              sqlite_connector_labelList,
                                              sqlite_connector_typeList,
                                              sqlite_connector_placeholderList,
                                              sqlite_connector_jsList,
                                              sqlite_connector_reqList)
        elif(sqlid == SQL_QUERY) :
            db_con_input_form   =   InputForm(sqlite_connector_id,
                                              sqlite_connector_idList,
                                              sqlite_query_connector_labelList,
                                              sqlite_connector_typeList,
                                              sqlite_connector_placeholderList,
                                              sqlite_query_connector_jsList,
                                              sqlite_connector_reqList)
        else : #sqlid == SQL_EXPORT
            db_con_input_form   =   InputForm(sqlite_connector_id,
                                              sqlite_connector_idList,
                                              sqlite_export_connector_labelList,
                                              sqlite_connector_typeList,
                                              sqlite_connector_placeholderList,
                                              sqlite_export_connector_jsList,
                                              sqlite_connector_reqList)           
        
    elif(dbid == Postgresql) :
        
        dblib = dblib = dbconparms[4]
        
        if(sqlid == SQL_IMPORT) :
            db_con_input_form   =   InputForm(Postgresql_connector_id,
                                              Postgresql_connector_idList,
                                              Postgresql_connector_labelList,
                                              Postgresql_connector_typeList,
                                              Postgresql_connector_placeholderList,
                                              Postgresql_connector_jsList,
                                              Postgresql_connector_reqList)

        elif(sqlid == SQL_QUERY) :
            db_con_input_form   =   InputForm(Postgresql_connector_id,
                                              Postgresql_connector_idList,
                                              Postgresql_query_connector_labelList,
                                              Postgresql_connector_typeList,
                                              Postgresql_connector_placeholderList,
                                              Postgresql_query_connector_jsList,
                                              Postgresql_connector_reqList)
        else : #sqlid == SQL_EXPORT
            db_con_input_form   =   InputForm(Postgresql_connector_id,
                                              Postgresql_connector_idList,
                                              Postgresql_export_connector_labelList,
                                              Postgresql_connector_typeList,
                                              Postgresql_connector_placeholderList,
                                              Postgresql_export_connector_jsList,
                                              Postgresql_connector_reqList)           

    elif(dbid == Oracle) :
        
        dblib = dblib = dbconparms[3]

        if(sqlid == SQL_IMPORT) :
            db_con_input_form   =   InputForm(oracle_connector_id,
                                              oracle_connector_idList,
                                              oracle_connector_labelList,
                                              oracle_connector_typeList,
                                              oracle_connector_placeholderList,
                                              oracle_connector_jsList,
                                              oracle_connector_reqList)
        elif(sqlid == SQL_QUERY) :
            db_con_input_form   =   InputForm(oracle_connector_id,
                                              oracle_connector_idList,
                                              oracle_query_connector_labelList,
                                              oracle_connector_typeList,
                                              oracle_connector_placeholderList,
                                              oracle_query_connector_jsList,
                                              oracle_connector_reqList)
        else : #sqlid == SQL_EXPORT
            db_con_input_form   =   InputForm(oracle_connector_id,
                                              oracle_connector_idList,
                                              oracle_export_connector_labelList,
                                              oracle_connector_typeList,
                                              oracle_connector_placeholderList,
                                              oracle_export_connector_jsList,
                                              oracle_connector_reqList)           
        
    elif(dbid == Custom) :
        
        if(sqlid == SQL_IMPORT) :
            db_con_input_form   =   InputForm(custom_connector_id,
                                              custom_connector_idList,
                                              custom_connector_labelList,
                                              custom_connector_typeList,
                                              custom_connector_placeholderList,
                                              custom_connector_jsList,
                                              custom_connector_reqList)
        elif(sqlid == SQL_QUERY) :
            db_con_input_form   =   InputForm(custom_connector_id,
                                              custom_connector_idList,
                                              custom_query_connector_labelList,
                                              custom_connector_typeList,
                                              custom_connector_placeholderList,
                                              custom_query_connector_jsList,
                                              custom_connector_reqList)
        else :
            db_con_input_form   =   InputForm(custom_connector_id,
                                              custom_connector_idList,
                                              custom_export_connector_labelList,
                                              custom_connector_typeList,
                                              custom_connector_placeholderList,
                                              custom_export_connector_jsList,
                                              custom_connector_reqList)          
        

    if( (dbid == None) or (dbid == MySql) )     :   cfgname =  MYSQL_DBCON_PARMS
    elif( (dbid == MS_SQL_Server) )             :   cfgname =  MSSQL_DBCON_PARMS
    elif( (dbid == SQLite) )                    :   cfgname =  SQLITE_DBCON_PARMS
    elif( (dbid == Postgresql) )                :   cfgname =  POSTGRESQL_DBCON_PARMS
    elif( (dbid == Oracle) )                    :   cfgname =  ORACLE_DBCON_PARMS
    elif( (dbid == Custom) )                    :   cfgname =  CUSTOM_DBCON_PARMS
    
    if(cfg.get_config_value(cfgname) == None) :
        cfg.set_config_value(cfgname,dbconparms)
    else :
        dbparms = cfg.get_config_value(cfgname)
        if(dbconparms != None) :     
            for i in range(len(dbconparms)) :
                if(dbconparms[i] != "") : dbparms[i] = dbconparms[i]
        
        cfg.set_config_value(cfgname,dbparms,False)
    
    dbtitle = ""    
    if( (dbid == None) )            :   dbtitle = ""
    elif( (dbid == MySql) )         :   dbtitle = "MySql : " + dblib
    elif( (dbid == MS_SQL_Server) ) :   dbtitle = "MS SQL Server : " + dblib
    elif( (dbid == SQLite) )        :   dbtitle = "SQLite : " + dblib
    elif( (dbid == Postgresql) )    :   dbtitle = "Postgresql : " + dblib
    elif( (dbid == Oracle) )        :   dbtitle = "Oracle : " + dblib
    elif( (dbid == Custom) )        :   dbtitle = "Custom"
    
    sql_db_connector_heading_html =   "<div>Connection Parms - " + dbtitle + "</div><br></br>"

    db_con_input_form.set_gridwidth(640)

    db_con_input_html = ""
    db_con_input_html = db_con_input_form.get_html() 
    
    gridclasses     =   ["dfcleanser-common-grid-header","dfc-left","dfc-right"]
    gridhtmls       =   [sql_db_connector_heading_html,listHtml,db_con_input_html]
    
    display_generic_grid("sql-connector-wrapper",gridclasses,gridhtmls)
   

def get_stored_con_Parms(dbid) :
    
    conparms = None
    
    import dfcleanser.common.db_utils as dbu
    
    if(dbid == dbu.MySql)               : conparms = cfg.get_config_value(MYSQL_DBCON_PARMS,cfg.GLOBAL)
    elif(dbid == dbu.MS_SQL_Server)     : conparms = cfg.get_config_value(MSSQL_DBCON_PARMS,cfg.GLOBAL)
    elif(dbid == dbu.SQLite)            : conparms = cfg.get_config_value(SQLITE_DBCON_PARMS,cfg.GLOBAL)
    elif(dbid == dbu.Postgresql)        : conparms = cfg.get_config_value(POSTGRESQL_DBCON_PARMS,cfg.GLOBAL)
    elif(dbid == dbu.Oracle)            : conparms = cfg.get_config_value(ORACLE_DBCON_PARMS,cfg.GLOBAL)
    elif(dbid == dbu.Custom)            : conparms = cfg.get_config_value(CUSTOM_DBCON_PARMS)

    return(conparms)    

def get_db_connector_list(dbid,dbcondict) :

    dbconlistHeader    =   [""]
    dbconlistRows      =   []
    dbconlistWidths    =   [100]
    dbconlistAligns    =   ["left"]
    dbconlistHrefs     =   []

    if(dbid != Custom) :
        rowText = ["","&nbsp;&nbsp;DB Id :","&nbsp;&nbsp;&nbsp;&nbsp;" + get_db_id_title(dbid),
                   "&nbsp;&nbsp;DB Library :","&nbsp;&nbsp;&nbsp;&nbsp;" + dbcondict.get("dblibrary"),
                   "","&nbsp;&nbsp;Parms :"]
    else :
        rowText = ["","&nbsp;&nbsp;DB Id :","&nbsp;&nbsp;&nbsp;&nbsp;" + "Custom",
                   "&nbsp;&nbsp;DB Library :","&nbsp;&nbsp;&nbsp;&nbsp;" + "Custom",
                   "","&nbsp;&nbsp;Parms :"]
        
    
    if(dbid == MySql) :
        rowText.append("&nbsp;&nbsp;&nbsp;&nbsp;" + dbcondict.get("hostname"))
        rowText.append("&nbsp;&nbsp;&nbsp;&nbsp;" + dbcondict.get("username"))
        rowText.append("&nbsp;&nbsp;&nbsp;&nbsp;" + dbcondict.get("password"))
        rowText.append("&nbsp;&nbsp;&nbsp;&nbsp;" + dbcondict.get("database"))
        
    if(dbid == MS_SQL_Server) :
        rowText.append("&nbsp;&nbsp;&nbsp;&nbsp;" + dbcondict.get("msserver"))
        rowText.append("&nbsp;&nbsp;&nbsp;&nbsp;" + dbcondict.get("msusername"))
        rowText.append("&nbsp;&nbsp;&nbsp;&nbsp;" + dbcondict.get("mspassword"))
        rowText.append("&nbsp;&nbsp;&nbsp;&nbsp;" + dbcondict.get("msdatabase"))
        
    if(dbid == Postgresql) :
        rowText.append("&nbsp;&nbsp;&nbsp;&nbsp;" + dbcondict.get("pghost"))
        rowText.append("&nbsp;&nbsp;&nbsp;&nbsp;" + dbcondict.get("pguser"))
        rowText.append("&nbsp;&nbsp;&nbsp;&nbsp;" + dbcondict.get("pgpassword"))
        rowText.append("&nbsp;&nbsp;&nbsp;&nbsp;" + dbcondict.get("pgdbname"))
     
        
    elif( (dbid == SQLite) ) :
        rowText.append("&nbsp;&nbsp;&nbsp;&nbsp;" + dbcondict.get("db_file"))
        
    elif( (dbid == Oracle) ) :
        rowText.append("&nbsp;&nbsp;&nbsp;&nbsp;" + dbcondict.get("tdshost"))
        rowText.append("&nbsp;&nbsp;&nbsp;&nbsp;" + dbcondict.get("user"))
        rowText.append("&nbsp;&nbsp;&nbsp;&nbsp;" + dbcondict.get("password"))
        
    elif( (dbid == Custom) ) :
        rowText.append("&nbsp;&nbsp;&nbsp;&nbsp;" + "Custom")

    for i in range(len(rowText)) :
        dbconlistrow = [rowText[i]]
        dbconlistRows.append(dbconlistrow)
        dbconlistHrefs.append([None])
        
    dbcon_parms_table = dcTable("DB Connector","dbconnectorParmssTable",
                                cfg.DataImport_ID,
                                dbconlistHeader,dbconlistRows,
                                dbconlistWidths,dbconlistAligns)
    
    dbcon_parms_table.set_refList(dbconlistHrefs)
    
    dbcon_parms_table.set_rowspertable(len(rowText))
    dbcon_parms_table.set_small(True)
    dbcon_parms_table.set_smallwidth(98)
    dbcon_parms_table.set_smallmargin(10)

    dbcon_parms_table.set_border(True)
    dbcon_parms_table.set_checkLength(False)
    
    dbcon_parms_table.set_html_only(True) 
    
    listHtml = dbcon_parms_table.get_html()
    
    return(listHtml)

"""
#------------------------------------------------------------------
#   test the db connector
#
#    importtype         -   pandas import identifier 
#    sqlinputparms      -   connection string 
#
#------------------------------------------------------------------
"""    
def test_db_connector(dbid,driverid,sqlinputparms,sqlid) :
    
    connectParms  =   {}
    parmslist = parse_connector_parms(sqlinputparms,dbid,connectParms)
    
    errormsg = validate_connection_parms(connectParms)
    
    if(errormsg == None) :
    
        if(driverid == NATIVE) :
            display_db_connector_inputs(dbid,parmslist,sqlid)
        
        if(driverid == NATIVE) :
            displayHeading("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Testing Native DB Connector",4)
        else :
            displayHeading("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Testing SQLAlchemy DB Connector",4)
                
        clock = RunningClock()
        clock.start()
        
        opstat = opStatus()

        dbcon = dbConnector()
        dbcon.connect_to_db(driverid,opstat,connectParms)

        if(opstat.get_status()) :
            if(driverid == NATIVE) :
                display_status("'DB Native Connector' connected Successfully : " + str(connectParms.get("dblibrary")))
            else :
                display_status("'DB SQLAlchemy Connector' connected Successfully : " + str(connectParms.get("dblibrary")))
            
            dbcon.close_dbConnection(opstat)
            if(opstat.get_status()) :
                display_status("'DB Connector' closed Successfully")

                dbid = connectParms.get("dbid") 
                
                if(dbid   == MySql)             : cfg.set_config_value(MYSQL_DBCON_PARMS,parmslist,cfg.GLOBAL)
                elif(dbid == MS_SQL_Server)     : cfg.set_config_value(MSSQL_DBCON_PARMS,parmslist,cfg.GLOBAL)
                elif(dbid == SQLite)            : cfg.set_config_value(SQLITE_DBCON_PARMS,parmslist,cfg.GLOBAL)
                elif(dbid == Postgresql)        : cfg.set_config_value(POSTGRESQL_DBCON_PARMS,parmslist,cfg.GLOBAL)
                elif(dbid == Oracle)            : cfg.set_config_value(ORACLE_DBCON_PARMS,parmslist,cfg.GLOBAL)
                elif(dbid == Custom)            : cfg.set_config_value(CUSTOM_DBCON_PARMS,parmslist,cfg.GLOBAL)
            
            else :
                display_exception(opstat)                
        else :
            display_exception(opstat)
        
        clock.stop()
        
    else :
        
        display_db_connector_inputs(dbid,parmslist,sqlid)  
        display_status(errormsg)


"""
#------------------------------------------------------------------
#   get the dbid from the db;ibrary entry in the con dict
#
#    dbcondict      -   dbconnector dict 
#
#------------------------------------------------------------------
"""     
def get_dbid_from_lib(dbcondict) :

    dbid = None
    
    dblib = dbcondict.get("dblibrary")
    
    if( (dblib == pymysql_library) or (dblib == mysql_connector_library) )  :    dbid = MySql
    elif( (dblib == pyodbc_library) or (dblib == pymssql_library) )         :    dbid = MS_SQL_Server
    elif( (dblib == sqlite_library) or (dblib == sqlite3_library) )         :    dbid = SQLite
    elif(dblib == psycopg2_library)                                         :    dbid = Postgresql
    elif(dblib == cx_oracle_library)                                        :    dbid = Oracle
    else                                                                    :    dbid = Custom

    return(dbid)

"""
#------------------------------------------------------------------
#   grab the sql db connector parms
#
#    dbid               -   database type identifier 
#    sqlinputparms      -   connection string 
#
#------------------------------------------------------------------
""" 
def grab_connection_parms(parmsdict) :
    
    dbid = get_dbid_from_lib(parmsdict) 
    
    dbcondict       =   {}
    
    if(dbid != None) :
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
      
            if(not (parmsdict.get("dblibrary") == None) )       : dbcondict.update({"dblibrary":parmsdict.get("dblibrary")})
            if(not (parmsdict.get("connectstring") == None) )   : dbcondict.update({"connectstring":parmsdict.get("connectstring")})
        
        return(dbcondict)
        
"""
#------------------------------------------------------------------
#   validate the sql db connector parms
#
#    dbid               -   database type identifier 
#    sqlinputparms      -   connection string 
#
#------------------------------------------------------------------
"""    
def validate_connection_parms(parmsdict) :

    dbid = get_dbid_from_lib(parmsdict)
    
    dbconlabels =   [mysql_connector_labelList,mssql_connector_labelList,sqlite_connector_labelList,
                     Postgresql_connector_labelList,oracle_connector_labelList,custom_connector_labelList]    
    dbconlens   =   [5,5,2,5,4,1] 
    
    if(dbid == None) :
        return("No db id") 
    else :

        for i in range(dbconlens[dbid]) :
            parm = parmsdict.get(dbconlabels[dbid][i])
            if(parm == None) :
                return("Invalid " + dbconlabels[dbid][i] + " parameter")
    
    return(None)    


"""
#------------------------------------------------------------------
#   test the sql db connector
#
#    dbid               -   database type identifier 
#    sqlinputparms      -   connection string 
#
#------------------------------------------------------------------
"""    
def get_SQLAlchemy_connector_string(parmsdict) :

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
        cparms          =   cfg.get_config_value(custom_connector_id + "Parms")    
        dbConnectString =   cparms[0] 

    return(dbConnectString)

"""
#------------------------------------------------------------------
#   buil db connector dict
#
#    dbid           -   database type identifier 
#    parmslist      -   list of dcon parms 
#
#------------------------------------------------------------------
""" 
def set_dbcon_dict(dbid,parmslist) :

    #print("set_dbcon_dict",dbid,parmslist,custom_connector_labelList)    
    dbcondict = {}

    dbconlabels =   [mysql_connector_labelList,mssql_connector_labelList,sqlite_connector_labelList,
                     Postgresql_connector_labelList,oracle_connector_labelList,custom_connector_labelList]    
    dbconlens   =   [5,5,2,5,4,1] 
    
    dbcondict.update({"dbid":dbid})
    
    for i in range(dbconlens[dbid]) :
        dbcondict.update({dbconlabels[dbid][i]:parmslist[i]})    
    
    return(dbcondict)

"""
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#   database connector
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
"""
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
    
        if((inparms != None)) :
            self.dbconnectParms   =   {}
            
            errormsg = validate_connection_parms(inparms)
            if( errormsg == None) :
                dbcondict = grab_connection_parms(inparms)
                self.set_ConnectionParms(dbcondict)

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
                    opstat.set_errorMsg("Invalid DB Library" + self.dbconnectParms.get("dblibrary"))

            except Exception as e:
                opstat.store_exception("Unable to connect to database ",e)
                self.dbConn = None
            
            return(self.dbConn)
        
        else :
            
            try :
                
                from sqlalchemy import create_engine
                connectString = ""
                
                if(get_SQLAlchemy_engine(self.dbconnectParms.get("dblibrary")) == None) :

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
                    
                    new_engine = create_engine(connectString, echo=False)
                    if(self.dbconnectParms.get("dblibrary") != None) :
                        set_SQLAlchemy_engine(self.dbconnectParms.get("dblibrary"),new_engine)
                    else :
                        set_SQLAlchemy_engine(Custom,new_engine)


                # go ahead and get a connecton to the engine 
                if(self.dbconnectParms.get("dblibrary") != None) :   
                    self.dbConn = get_SQLAlchemy_engine(self.dbconnectParms.get("dblibrary")).connect() 
                else :
                    self.dbConn = get_SQLAlchemy_engine(Custom).connect() 
                        
                opstat.set_status(True)
            
            except Exception as e:
                opstat.store_exception("Unable to connect to database ",e)
                self.dbConn = None
            
            return(self.dbConn)
            

    def close_dbConnection(self,opstat) :
        
        try :
            self.dbConn.close()
            self.dbConn = None

            opstat.set_status(True)
            
        except Exception as e:
            opstat.store_exception("Unable to close connection ",e)

  
    