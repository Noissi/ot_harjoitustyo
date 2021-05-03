from database_connection import get_database_connection

class UserRepository:
    """ Class responsible for user database logic.

    Attributes:
        connection: A databse connection object.
    """

    def __init__(self, connection):
        """ Class constructor. Creates a new user repository.

        Args:
            connection: A databse connection object.
        """

        self._connection = connection

    def create(self, user):
        """ Creates a new user into the users table.
        Args:
            user: [User] The User entity to be saved.
        """

        user_sql = (user.get_username(), user.get_password())

        sql = ''' INSERT INTO users(username, password)
                  VALUES(?,?) '''

        cursor = self._connection.cursor()
        cursor.execute(sql, user_sql)
        self._connection.commit()

    def save(self, user):
        """ Saves the user into the users table.
        Args:
            user: [User] The User entity to be saved.
        """

        self.create(user)

    def delete(self, username):
        """ Removes the user from the users table.
        Args:
            username: [String] The username of the user to be removed from the database.
        """

        user_sql = (username,)
        sql = """DELETE FROM users WHERE username = ? """
        cursor = self._connection.cursor()
        cursor.execute(sql, user_sql)
        self._connection.commit()

    def find_all(self):
        """ Select all users from the users table.
        Return:
            rows: [List Tuple] List of tuples including the users.
        """

        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM users')
        row = cursor.fetchall()
        return row

    def find_by_username(self, username):
        """ Select user from the users table by given username.
        Args:
            username: [String] The username of a user.
        Return:
            rows: [Tuple] User attributes.
        """

        username_sql = (username,)
        cursor = self._connection.cursor()
        cursor.execute("""SELECT * FROM users WHERE username = ? """, username_sql)
        row = cursor.fetchall()
        return row

user_repository = UserRepository(get_database_connection())
