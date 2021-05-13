import unittest
from repositories.card_repository import card_repository
from entities.card import Card
from entities.card_creature import Creature
from entities.card_instant import Instant

class TestCardRepository(unittest.TestCase):
    def setUp(self):
        card_repository.delete_all()
        self.card1 = Card('Teemu Kerppu')
        self.card2 = Creature('Kana')
        self.card3 = Instant('Kortti')
        self.card4 = Creature('Kana2')

        self.card1.set_cubes(["id1"])
        self.card2.set_cubes(["id1"])
        self.card3.set_cubes(["id2"])
        self.card4.set_cubes(["id1"])

    def test_create(self):
        card_repository.create(self.card1)
        cards = card_repository.find_all()

        self.assertEqual(len(cards), 1)
        self.assertEqual(cards[0][1], self.card1.get_name())

    def test_save_create(self):
        card_repository.save(self.card1)
        cards = card_repository.find_all()

        self.assertEqual(len(cards), 1)
        self.assertEqual(cards[0][1], self.card1.get_name())

    def test_save_update(self):
        card_repository.create(self.card1)
        self.card1.set_name("Korppu")
        card_repository.save(self.card1)
        cards = card_repository.find_all()

        self.assertEqual(len(cards), 1)
        self.assertEqual(cards[0][1], "Korppu")

    def test_delete(self):
        card_repository.create(self.card1)
        cards = card_repository.find_all()
        self.assertEqual(len(cards), 1)
        self.assertEqual(cards[0][1], "Teemu Kerppu")
        
        card_repository.delete(self.card1.get_id())
        cards = card_repository.find_all()
        self.assertEqual(len(cards), 0)

    def test_delete_all(self):
        card_repository.create(self.card1)
        card_repository.create(self.card2)
        card_repository.create(self.card3)
        cards = card_repository.find_all()
        self.assertEqual(len(cards), 3)
        
        card_repository.delete_all()
        cards = card_repository.find_all()
        self.assertEqual(len(cards), 0)

    def test_find_all(self):
        card_repository.create(self.card1)
        card_repository.create(self.card2)
        cards = card_repository.find_all()

        self.assertEqual(len(cards), 2)
        self.assertEqual(cards[0][1], self.card1.get_name())
        self.assertEqual(cards[1][1], self.card2.get_name())

    def test_find_by_cube(self):
        card_repository.create(self.card1)
        card_repository.create(self.card2)
        card_repository.create(self.card3)
        cards = card_repository.find_by_cube("id1")

        self.assertEqual(len(cards), 2)
        self.assertEqual(cards[0][1], self.card1.get_name())
        self.assertEqual(cards[1][1], self.card2.get_name())

    def test_find_by_name_that_contains(self):
        card_repository.create(self.card1)
        card_repository.create(self.card2)
        card_repository.create(self.card3)
        cards = card_repository.find_by_name_that_contains("r")

        self.assertEqual(len(cards), 2)
        self.assertEqual(cards[0][1], self.card1.get_name())
        self.assertEqual(cards[1][1], self.card3.get_name())

    def test_find_cards_from_cube_that_contains(self):
        card_repository.create(self.card1)
        card_repository.create(self.card2)
        card_repository.create(self.card3)
        card_repository.create(self.card4)
        cards = card_repository.find_cards_from_cube_that_contains("id1", "",
                                                "Creature", "", ["name", "ASC"])

        self.assertEqual(len(cards), 2)
        self.assertEqual(cards[0][1], self.card2.get_name())
        self.assertEqual(cards[1][1], self.card4.get_name())

    def test_create_csv_file(self):
        card_repository.create(self.card1)
        card_repository.create(self.card2)
        card_repository.create(self.card3)
        card_repository.create(self.card4)
        cursor = card_repository.create_csv_file("id1")
        cards = cursor.fetchall()

        self.assertEqual(len(cards), 3)
        self.assertEqual(cards[0][1], self.card1.get_name())
        self.assertEqual(cards[1][1], self.card2.get_name())
        self.assertEqual(cards[2][1], self.card4.get_name())
