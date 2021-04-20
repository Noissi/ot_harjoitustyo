import sqlite3
from sqlite3 import Error
from config import DATABASE_FILE_PATH

""" Create a database connection to the SQLite database
    specified by DATABASE_FILE_PATH file.
return: Connection object or None
"""

connection = None
print(DATABASE_FILE_PATH)
try:
    connection = sqlite3.connect(DATABASE_FILE_PATH)
except Error as e:
    print(e)

def get_database_connection():
    return connection
