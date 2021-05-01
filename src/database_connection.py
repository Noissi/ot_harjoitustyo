import sqlite3
from sqlite3 import Error
from config import DATABASE_FILE_PATH

connection = None
print(DATABASE_FILE_PATH)
try:
    connection = sqlite3.connect(DATABASE_FILE_PATH)
except Error as error:
    print(error)

def get_database_connection():
    """ Create a database connection to the SQLite database specified by DATABASE_FILE_PATH file.
    Returns: 
        Connection object or None
    """
    return connection
