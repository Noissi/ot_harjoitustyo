import unittest
from repositories.card_repository import card_repository
from entities.card import Card

class TestCardRepository(Unittest.TestCase):
    def setUp(self):
    	self.card = Card('Teemu Kerppu')
    	###
    	
    def test_create(self):
        ###
