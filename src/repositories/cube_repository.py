from database_connection import get_database_connection

class CubeRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, cube):
        """
        Create a new cube into the cubes table.
        """

        cube_sql = (cube.get_id(), cube.get_name(), cube.get_users_print(), \
                    cube.get_image(), cube.get_seticon())

        sql = ''' INSERT INTO cubes(id, name, users, image, seticon)
                  VALUES(?,?,?,?,?); '''

        cursor = self._connection.cursor()
        cursor.execute(sql, cube_sql)
        self._connection.commit()

    def update(self, cube):
        cube_sql = (cube.get_name(), cube.get_users_print(), cube.get_image(), \
                    cube.get_seticon(), cube.get_id())

        sql = ''' UPDATE cubes
                  SET name = ?,
                      users = ?,
                      image = ?,
                      seticon = ?
                   WHERE id = ?; '''

        cursor = self._connection.cursor()
        cursor.execute(sql, cube_sql)
        self._connection.commit()

    def save(self, cube):
        cube_sql = (cube.get_id(),)
        sql = """ SELECT 1 FROM cubes WHERE id = ?; """
        cursor = self._connection.cursor()
        cursor.execute(sql, cube_sql)
        if cursor.fetchone() is None:
            self.create(cube)
        else:
            self.update(cube)

    def delete(self, cube_id):
        cube_sql = (cube_id,)
        sql = """ DELETE FROM cubes WHERE cube_id = ?; """
        cursor = self._connection.cursor()
        cursor.execute(sql, cube_sql)
        self._connection.commit()

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM cubes')
        rows = cursor.fetchall()
        return rows

    def find_by_user(self, username):
        user_sql = (username,)
        sql = """ SELECT * FROM cubes WHERE users = ?; """
        cursor = self._connection.cursor()
        cursor.execute(sql, user_sql)
        rows = cursor.fetchall()
        return rows

cube_repository = CubeRepository(get_database_connection())