from database_connection import get_database_connection

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, user):
        """
        Create a new user into the users table.
        """

        user_sql = (user.get_username(), user.get_password())
        print(user.get_username(), user.get_password())

        sql = ''' INSERT INTO users(username, password)
                  VALUES(?,?) '''

        cursor = self._connection.cursor()
        cursor.execute(sql, user_sql)
        self._connection.commit()

    def delete(self, username):
        user_sql = (username,)
        sql = """DELETE FROM users WHERE username = ? """
        cursor = self._connection.cursor()
        cursor.execute(sql, user_sql)
        self._connection.commit()

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM users')
        row = cursor.fetchall()
        return row

    def find_by_username(self, username):
        username_sql = (username,)
        cursor = self._connection.cursor()
        cursor.execute("""SELECT * FROM users WHERE username = ? """, username_sql)
        row = cursor.fetchall()
        return row

user_repository = UserRepository(get_database_connection())