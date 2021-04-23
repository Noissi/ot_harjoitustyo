import unittest
from entities.cube import Cube

class TestCube(unittest.TestCase):
    def setUp(self):
    	self.cube = Cube('Otakube')

    def set_cube(self):
        self.cube.set_id("11")
        self.cube.set_name("Testikube")
        self.cube.set_users(["1234", "2345"])
        self.cube.set_seticon("kuva")

    def test_set_attributes(self):
        self.set_cube()
        self.assertEqual(self.cube.get_id(), "11")
        self.assertEqual(self.cube.get_name(), "Testikube")
        self.assertEqual(self.cube.get_users(), ["1234", "2345"])
        self.assertEqual(self.cube.get_seticon(), "kuva")
        self.cube.set_users("12,34,56")        
        self.assertEqual(self.cube.get_users(), ["12", "34", "56"])

    def test_get_users_print(self):
        self.assertEqual(self.cube.get_users_print(), "Ei käyttäjiä")
        self.cube.set_users(["1234", "2345"])
        self.assertEqual(self.cube.get_users_print(), "1234, 2345")
        self.cube.set_users("9876")
        self.assertEqual(self.cube.get_users_print(), "9876")

    def test_add_user(self):
        self.assertEqual(self.cube.get_users(), [])
        self.cube.add_user("999")
        self.assertEqual(self.cube.get_users(), ["999"])
        self.cube.add_user("777")
        self.assertEqual(self.cube.get_users(), ["999", "777"])
        self.cube.add_user("999")
        self.assertEqual(self.cube.get_users(), ["999", "777"])
        self.cube.add_user("111")
        self.assertEqual(self.cube.get_users(), ["999", "777", "111"])
    
    def test_remove_user(self):
        self.cube.remove_user("123")
        self.assertEqual(self.cube.get_users(), [])
        self.cube.add_user("123")
        self.cube.add_user("4321")
        self.cube.remove_user("1234")
        self.assertEqual(self.cube.get_users(), ["123", "4321"])
        self.cube.remove_user(None)
        self.assertEqual(self.cube.get_users(), ["123", "4321"])
        self.cube.remove_user("123")
        self.assertEqual(self.cube.get_users(), ["4321"])
        self.cube.remove_user("1")
        self.assertEqual(self.cube.get_users(), ["4321"])
        self.cube.remove_user("4321")
        self.assertEqual(self.cube.get_users(), [])
        self.cube.remove_user("4321")
        self.assertEqual(self.cube.get_users(), [])
