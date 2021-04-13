from database_connection import get_database_connection
from sqlite3 import Error

def create_table(conn, create_table_sql):
    """ Create a table from the create_table_sql statement
    Args:
        conn: Connection object
    	create_table_sql: a CREATE TABLE statement
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)

def create_tables(conn):
    """ Create tables.
    Args:
        conn: Connection object
    """
    
    sql_create_cards_table = """ CREATE TABLE IF NOT EXISTS cards (
                                        id text PRIMARY KEY,
                                        name text NOT NULL,
                                        cubes text,
                                        image text,
                                        maintype text,
                                        legendary boolean,
                                        tribal boolean,
                                        subtype text,
                                        colour text,
                                        manacost text,
                                        power integer,
                                        toughness integer,
                                        feature text,
                                        ruletext text,
                                        flavourtext text,
                                        creator text,
                                        seticon text,
                                        rarity text
                                    ); """

    sql_create_cubes_table = """CREATE TABLE IF NOT EXISTS cubes (
                                    id text PRIMARY KEY,
                                    name text NOT NULL,
                                    users text NOT NULL,
                                    card_id text NOT NULL,
                                    FOREIGN KEY (card_id) REFERENCES cards (id)
                                );"""
                              
    sql_create_users_table = """CREATE TABLE IF NOT EXISTS users (
                                    id text PRIMARY KEY,
                                    username text NOT NULL,
                                    password text NOT NULL,
                                    cube_id text,
                                    FOREIGN KEY (cube_id) REFERENCES cubes (id)
                                );"""
    
    # Create tables
    if conn is not None:
        # Create cards table
        create_table(conn, sql_create_cards_table)
        # Create cubes table
        create_table(conn, sql_create_cubes_table)
        # Create users table
        create_table(conn, sql_create_users_table)
    else:
        print("Error! Cannot create the database connection.")

def initialise_database():    
    # Create a database connection
    print("Creating database connection")
    connection = get_database_connection()
    
    # Create tables
    create_tables(connection)

if __name__ == '__main__':
    initialise_database()
