from database_connection import get_database_connection

class CubeRepository:
    def __init__(self, connection):
        self._connection = connection
        
    def create(self, cube):
        """
        Create a new cube into the cubes table
        return: cube id
        """
        
        cube_sql = (cube.get_name(), cube.get_users_print(), cube.get_seticon());
                    
        sql = ''' INSERT INTO cubes(name, users, seticon)
              VALUES(?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, cube_sql)
        conn.commit()
        return cur.lastrowid
        
    def delete_all(self, cube):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM cubes')
        self._connection.commit()
        
    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM cubes WHERE name = ?', (name,))
        row = cursor.fetchone()

cube_repository = CubeRepository(get_database_connection())