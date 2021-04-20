from database_connection import get_database_connection

class CubeRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, cube):
        """
        Create a new cube into the cubes table.
        """

        cube_sql = (cube.get_name(), cube.get_users_print(), cube.get_seticon());

        sql = ''' INSERT INTO cubes(name, users, seticon, users)
              VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, cube_sql)
        conn.commit()

    def delete(self, cube):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM cubes') # Fix this
        self._connection.commit()

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM cubes')
        rows = cursor.fetchall()

cube_repository = CubeRepository(get_database_connection())
