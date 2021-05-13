import unittest
from entities.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
    	self.user = User('Peruna', 'salasana')
    	
    def set_user(self):
        self.user.set_username("Toinen")
        self.user.set_password("12345")
    	
    def test_set_attributes(self):
        self.set_user()
        self.assertEqual(self.user.get_username(), "Toinen")
        self.assertEqual(self.user.get_password(), "12345")
