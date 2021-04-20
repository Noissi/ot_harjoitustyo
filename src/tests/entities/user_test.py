import unittest
from entities.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
    	self.user = User('Peruna', 'salasana')
    	
    def set_user(self):
        self.user.set_username("Toinen")
        self.user.set_password("12345")
        self.user.set_cubes(["1234", "2345"])
        self.user.set_shared_cubes(["5432", "9876"])
    	
    def test_set_attributes(self):
        self.set_user()
        self.assertEqual(self.user.get_username(), "Toinen")
        self.assertEqual(self.user.get_password(), "12345")
        self.assertEqual(self.user.get_cubes(), ["1234", "2345"])
        self.assertEqual(self.user.get_shared_cubes(), ["5432", "9876"])
        self.user.set_cubes("12,34,56")        
        self.assertEqual(self.user.get_cubes(), ["12", "34", "56"])
        self.user.set_cubes("2,4,5")        
        self.assertEqual(self.user.get_cubes(), ["2", "4", "5"])
        
    def test_get_cubes_print(self):
        self.assertEqual(self.user.get_cubes_print(), "")
        self.user.set_cubes(["1234", "2345"])
        self.assertEqual(self.user.get_cubes_print(), "1234, 2345")
        self.user.set_cubes("9876")
        self.assertEqual(self.user.get_cubes_print(), "9876")
        
    def test_get_shared_cubes_print(self):
        self.assertEqual(self.user.get_shared_cubes_print(), "")
        self.user.set_shared_cubes(["34", "45", "12"])
        self.assertEqual(self.user.get_shared_cubes_print(), "34, 45, 12")
        self.user.set_shared_cubes("98,76")
        self.assertEqual(self.user.get_shared_cubes_print(), "98, 76")
        
    def test_add_cube(self):
        self.assertEqual(self.user.get_cubes(), [])
        self.user.add_cube("999")
        self.assertEqual(self.user.get_cubes(), ["999"])
        self.user.add_cube("777")
        self.assertEqual(self.user.get_cubes(), ["999", "777"])
        self.user.add_cube("999")
        self.assertEqual(self.user.get_cubes(), ["999", "777"])
        self.user.add_cube("111")
        self.assertEqual(self.user.get_cubes(), ["999", "777", "111"])
        
    def test_add_shared_cube(self):
        self.assertEqual(self.user.get_shared_cubes(), [])
        self.user.add_shared_cube("222")
        self.assertEqual(self.user.get_shared_cubes(), ["222"])
        self.user.add_shared_cube("222")
        self.assertEqual(self.user.get_shared_cubes(), ["222"])
        self.user.add_shared_cube("999")
        self.assertEqual(self.user.get_shared_cubes(), ["222", "999"])
    
    def test_remove_cube(self):
        self.user.remove_cube("123")
        self.assertEqual(self.user.get_cubes(), [])
        self.user.add_cube("123")
        self.user.add_cube("4321")
        self.user.remove_cube("1234")
        self.assertEqual(self.user.get_cubes(), ["123", "4321"])
        self.user.remove_cube("123")
        self.assertEqual(self.user.get_cubes(), ["4321"])
        self.user.remove_cube("1")
        self.assertEqual(self.user.get_cubes(), ["4321"])
        self.user.remove_cube("4321")
        self.assertEqual(self.user.get_cubes(), [])
        self.user.remove_cube("4321")
        self.assertEqual(self.user.get_cubes(), [])
        
    def test_remove_shared_cube(self):
        self.user.remove_shared_cube("3")
        self.assertEqual(self.user.get_shared_cubes(), [])
        self.user.add_shared_cube("23")
        self.user.add_shared_cube("21")
        self.user.remove_shared_cube("1234")
        self.assertEqual(self.user.get_shared_cubes(), ["23", "21"])
        self.user.remove_shared_cube("239")
        self.assertEqual(self.user.get_shared_cubes(), ["23", "21"])
        self.user.remove_shared_cube("21")
        self.assertEqual(self.user.get_shared_cubes(), ["23"])
        self.user.remove_shared_cube("4321")
        self.assertEqual(self.user.get_shared_cubes(), ["23"])
        self.user.remove_shared_cube("23")
        self.assertEqual(self.user.get_shared_cubes(), [])