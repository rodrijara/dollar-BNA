import sqlite3
from sqlite3 import Error

def create_connection(path):
    """
    Stablish a connection to a SQLite DB
    
    Args:
        path: string indicating where the DB is (or will be) located
            path must be a whole path and not a relative path
        
    Returns:
        a connection object, which can be used to execute queries on the specified DB
    """
    connection = None
    try:
        connection = sqlite3.connect(path)
        print('... Connection to SQLite DB successful')
    except Error as e:
        print(f'... The error "{e}" occurred')

    return connection

def execute_query(connection, query, *args):
    """
    Execute a query 'query' on 'connection' SQLite DB
    
    Args:
        connection: a connection object created with sqlite3.connect() function
        query: string indicating what to execute on connection
        
    Returns:
        does not return a value, only executes a query an exits. 
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, (args))
        connection.commit()
        print('... Query executed successfully')
    except Error as e:
        print(f'... The error "{e}" occurred')