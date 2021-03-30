from database_connection import get_database_connection

class UserRepository:
    def __init__(self, connection):
        self._connection = connection
        
    def create(self, user):
        """
        Create a new user into the users table
        return: user id
        """
        user_sql = (user.get_name(), user.get_password());
            
        sql = ''' INSERT INTO users(name, password)
                  VALUES(?,?) '''
        
        cursor = self._connection.cursor()
        cursor.execute(sql, user_sql)
        self._connection.commit()
        return cursor.lastrowid
        
    def delete_all(self, user):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM users')
        self._connection.commit()
        
    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
        row = cursor.fetchone()

user_repository = UserRepository(get_database_connection())
