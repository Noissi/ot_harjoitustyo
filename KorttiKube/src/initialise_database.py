from database_connection import get_database_connection
from sqlite3 import Error

def drop_tables(conn):
    c = conn.cursor()
    c.execute(''' drop table if exists users; ''')
    conn.commit()

def create_table(conn, create_table_sql):
    """ Create a table from the create_table_sql statement
    param conn: Connection object
    param create_table_sql: a CREATE TABLE statement
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)
        
def create_tables(conn):
    sql_create_cards_table = """ CREATE TABLE IF NOT EXISTS cards (
                                        id text PRIMARY KEY,
                                        name text NOT NULL,
                                        colour text,
                                        image text,
                                        maintype text,
                                        legendary text,
                                        tribal text,
                                        subtype text,
                                        power integer,
                                        toughness integer,
                                        manacost text,
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

    # Create tables
    if conn is not None:
        # create cards table
        create_table(conn, sql_create_cards_table)
        # create cubes table
        create_table(conn, sql_create_cubes_table)
    else:
        print("Error! Cannot create the database connection.")

def initialise_database():    
    # create a database connection
    print("creating database connection")
    connection = get_database_connection()
    
    # Create tables
    create_tables(connection)

    '''
    # Create items
    with conn:
        # create a new card
        #project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30');
        card_id = create_card(conn, card)

        # create a new cube
        #task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
        cube1 = ('OtaKube', 'testuser', card_id);
        
        # create tasks
        create_task(conn, cube1)
    '''
if __name__ == '__main__':
    initialise_database()
