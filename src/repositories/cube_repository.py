from database_connection import get_database_connection

class CubeRepository:
    """ Class responsible for cube database logic.

    Attributes:
        connection: A databse connection object.
    """

    def __init__(self, connection):
        """ Class constructor. Creates a new cube repository.

        Args:
            connection: A databse connection object.
        """

        self._connection = connection

    def create(self, cube):
        """ Creates a new cube into the cubes table.
        Args:
            cube: [Cube] The Cube entity to be saved.
        """

        cube_sql = (cube.get_id(), cube.get_name(), cube.get_users_print(), \
                    cube.get_image(), cube.get_seticon())

        sql = ''' INSERT INTO cubes(id, name, users, image, seticon)
                  VALUES(?,?,?,?,?); '''

        cursor = self._connection.cursor()
        cursor.execute(sql, cube_sql)
        self._connection.commit()

    def update(self, cube):
        """ Updates an existing cube in the cubes table.
        Args:
            cube: [Cube] The Cube entity to be updated.
        """

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
        """ Saves the cube into the cubes table.
        Args:
            cube: [Cube] The Cube entity to be saved.
        """

        cube_sql = (cube.get_id(),)
        print(cube.get_image())
        sql = """ SELECT 1 FROM cubes WHERE id = ?; """
        cursor = self._connection.cursor()
        cursor.execute(sql, cube_sql)
        if cursor.fetchone() is None:
            self.create(cube)
        else:
            self.update(cube)

    def delete(self, cube_id):
        """ Removes the cube from the cubes table.
        Args:
            cube_id: [String] The id of the cube to be removed from the database.
        """

        cube_sql = (cube_id,)
        sql = """ DELETE FROM cubes WHERE cube_id = ?; """
        cursor = self._connection.cursor()
        cursor.execute(sql, cube_sql)
        self._connection.commit()

    def find_all(self):
        """ Select all cubes from the cubes table.
        Return:
            rows: [List Tuple] List of tuples including the cubes.
        """

        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM cubes')
        rows = cursor.fetchall()
        return rows

    def find_by_user(self, username):
        """ Select cubes from the cubes table that belong to the given username.
        Args:
            username: [String] The username of a user.
        Return:
            rows: [List Tuple] List of tuples including the cubes.
        """

        user_sql = (username,)
        sql = """ SELECT * FROM cubes WHERE users = ?; """
        cursor = self._connection.cursor()
        cursor.execute(sql, user_sql)
        rows = cursor.fetchall()
        return rows

cube_repository = CubeRepository(get_database_connection())