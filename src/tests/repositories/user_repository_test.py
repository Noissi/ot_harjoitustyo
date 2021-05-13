import unittest
from repositories.user_repository import user_repository
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user1 = User('matti', 'sala')
        self.user2 = User('maija', 'sana')
        self.user3 = User('kaija', '123')

    def test_create(self):
        user_repository.create(self.user1)
        users = user_repository.find_all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0][0], self.user1.get_username())

    def test_save(self):
        user_repository.save(self.user1)
        users = user_repository.find_all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0][0], self.user1.get_username())

    def test_delete(self):
        user_repository.create(self.user1)
        users = user_repository.find_all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0][0], "matti")
        
        user_repository.delete(self.user1.get_username())
        users = user_repository.find_all()
        self.assertEqual(len(users), 0)

    def test_delete_all(self):
        user_repository.create(self.user1)
        user_repository.create(self.user2)
        user_repository.create(self.user3)
        users = user_repository.find_all()
        self.assertEqual(len(users), 3)
        
        user_repository.delete_all()
        users = user_repository.find_all()
        self.assertEqual(len(users), 0)

    def test_find_all(self):
        user_repository.create(self.user1)
        user_repository.create(self.user2)
        users = user_repository.find_all()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0][0], self.user1.get_username())
        self.assertEqual(users[1][0], self.user2.get_username())

    def test_find_by_username(self):
        user_repository.create(self.user1)
        user_repository.create(self.user2)
        user_repository.create(self.user3)
        users = user_repository.find_by_username("kaija")

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0][0], self.user3.get_username())