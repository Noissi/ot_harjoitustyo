import unittest
from repositories.cube_repository import cube_repository
from entities.cube import Cube

class TestCubeRepository(unittest.TestCase):
    def setUp(self):
        cube_repository.delete_all()
        self.cube1 = Cube('Kube1')
        self.cube2 = Cube('Kube2')
        self.cube3 = Cube('Kube3')

        self.cube1.set_users(['matti'])
        self.cube2.set_users(['ei matti'])
        self.cube3.set_users(['matti'])

    def test_create(self):
        cube_repository.create(self.cube1)
        cubes = cube_repository.find_all()

        self.assertEqual(len(cubes), 1)
        self.assertEqual(cubes[0][1], self.cube1.get_name())

    def test_save_create(self):
        cube_repository.save(self.cube1)
        cubes = cube_repository.find_all()

        self.assertEqual(len(cubes), 1)
        self.assertEqual(cubes[0][1], self.cube1.get_name())

    def test_save_update(self):
        cube_repository.create(self.cube1)
        self.cube1.set_name("Kupe")
        cube_repository.save(self.cube1)
        cubes = cube_repository.find_all()

        self.assertEqual(len(cubes), 1)
        self.assertEqual(cubes[0][1], "Kupe")

    def test_delete(self):
        cube_repository.create(self.cube1)
        cubes = cube_repository.find_all()
        self.assertEqual(len(cubes), 1)
        self.assertEqual(cubes[0][1], "Kube1")
        
        cube_repository.delete(self.cube1.get_id())
        cubes = cube_repository.find_all()
        self.assertEqual(len(cubes), 0)

    def test_delete_all(self):
        cube_repository.create(self.cube1)
        cube_repository.create(self.cube2)
        cube_repository.create(self.cube3)
        cubes = cube_repository.find_all()
        self.assertEqual(len(cubes), 3)
        
        cube_repository.delete_all()
        cubes = cube_repository.find_all()
        self.assertEqual(len(cubes), 0)

    def test_find_all(self):
        cube_repository.create(self.cube1)
        cube_repository.create(self.cube2)
        cubes = cube_repository.find_all()

        self.assertEqual(len(cubes), 2)
        self.assertEqual(cubes[0][1], self.cube1.get_name())
        self.assertEqual(cubes[1][1], self.cube2.get_name())

    def test_find_by_user(self):
        cube_repository.create(self.cube1)
        cube_repository.create(self.cube2)
        cube_repository.create(self.cube3)
        cubes = cube_repository.find_by_user("matti")

        self.assertEqual(len(cubes), 2)
        self.assertEqual(cubes[0][1], self.cube1.get_name())
        self.assertEqual(cubes[1][1], self.cube3.get_name())