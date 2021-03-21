import unittest
from entities.card import Card
from entities.card_creature import Creature

class TestCard(unittest.TestCase):
    def setUp(self):
    	self.card = Card('Graduated friend')
    	self.creature = Creature('Teemu Kerppu')
    	###
    	
    def set_card(self):
        self.card.set_name("Party Tutor")
        self.card.set_image("img/partytutor")
        self.card.set_maintype("Creature")
        self.card.set_legendary(False)
        self.card.set_tribal(True)
        self.card.set_subtype("Teekkari ISO")
        self.card.set_ruletext("Party Tutor rule")
        self.card.set_flavourtext("Party")
        self.card.set_creator("Masa")
        self.card.set_seticon("img/seticon1")
        self.card.set_rarity("Common")
    	
    def test_set_attributes(self):
        self.set_card()        
        self.assertEqual(self.card.name, "Party Tutor")
        self.assertEqual(self.card.image, "img/partytutor")
        self.assertEqual(self.card.maintype, "Creature")
        self.assertEqual(self.card.legendary, False)
        self.assertEqual(self.card.tribal, True)
        self.assertEqual(self.card.subtype, ["Teekkari", "ISO"])
        self.assertEqual(self.card.ruletext, "Party Tutor rule")
        self.assertEqual(self.card.flavourtext, "Party")
        self.assertEqual(self.card.creator, "Masa")
        self.assertEqual(self.card.seticon, "img/seticon1")
        self.assertEqual(self.card.rarity, "Common")
        
    def test_add_colour(self):
        self.card.add_colour("Punainen")
        self.assertEqual(self.card.colour, ["Punainen"])
        self.card.add_colour("Valkoinen")
        self.assertEqual(self.card.colour, ["Punainen", "Valkoinen"])        
        self.card.add_colour("Valkoinen")
        self.assertEqual(self.card.colour, ["Punainen", "Valkoinen"])
        self.card.add_colour("Sininen")
        self.assertEqual(self.card.colour, ["Punainen", "Valkoinen", "Sininen"])
        
    def test_get_card_colour(self):
        self.assertEqual(self.card.get_card_colour(), "Väritön")
        self.card.add_colour("Punainen")
        self.assertEqual(self.card.get_card_colour(), "Punainen")
        self.card.add_colour("Vihreä")
        self.assertEqual(self.card.get_card_colour(), "Kulta")
        
    def test_get_colour(self):
        self.assertEqual(self.card.get_colour(), "Väritön")
        self.card.add_colour("Punainen")
        self.assertEqual(self.card.get_colour(), "Punainen")
        self.card.add_colour("Vihreä")
        self.assertEqual(self.card.get_colour(), "Punainen, Vihreä")
        
    def test_remove_colour(self):
        self.card.add_colour("Punainen")
        self.card.add_colour("Valkoinen")
        self.card.remove_colour("Vihreä")
        self.assertEqual(self.card.colour, ["Punainen", "Valkoinen"])
        self.card.remove_colour("Punainen")
        self.assertEqual(self.card.colour, ["Valkoinen"])
        self.card.remove_colour("Valkoinen")
        self.assertEqual(self.card.colour, [])
        self.card.remove_colour("Valkoinen")
        self.assertEqual(self.card.colour, [])
        
    def test_check_if_multicolour(self):
        self.assertNotEqual(self.card.get_card_colour(), "Kulta")
        self.card.add_colour("Punainen")
        self.assertNotEqual(self.card.get_card_colour(), "Kulta")
        self.card.add_colour("Vihreä")
        self.assertEqual(self.card.get_card_colour(), "Kulta")
        self.card.add_colour("Musta")
        self.assertEqual(self.card.get_card_colour(), "Kulta")
        self.card.remove_colour("Punainen")
        self.card.remove_colour("Musta")
        self.assertNotEqual(self.card.get_card_colour(), "Kulta")
        
    def test_add_feature(self):
        self.card.add_feature("Flying")        
        self.assertEqual(self.card.feature, ["Flying"])
        self.card.add_feature("Vigilance")
        self.assertEqual(self.card.feature, ["Flying", "Vigilance"])
        self.card.add_feature("Vigilance")
        self.assertEqual(self.card.feature, ["Flying", "Vigilance"])        
        self.card.add_feature("Trample")
        self.assertEqual(self.card.feature, ["Flying", "Vigilance", "Trample"])
        
    def test_get_feature(self):
        self.card.add_feature("Flying")        
        self.assertEqual(self.card.get_feature(), "Flying")
        self.card.add_feature("Vigilance")
        self.assertEqual(self.card.get_feature(), "Flying, Vigilance")
        self.card.add_feature("Trample")
        self.assertEqual(self.card.get_feature(), "Flying, Vigilance, Trample")
        
    def test_remove_feature(self):
        self.card.add_feature("Reach")
        self.card.add_feature("Deathtouch")
        self.card.remove_feature("Firststrike")
        self.assertEqual(self.card.feature, ["Reach", "Deathtouch"])
        self.card.remove_feature("Deathtouch")
        self.assertEqual(self.card.feature, ["Reach"])
        self.card.remove_feature("Reach")
        self.assertEqual(self.card.feature, [])
        self.card.remove_feature("Reach")
        self.assertEqual(self.card.feature, [])
        
    def test_get_legendary(self):
        self.assertEqual(self.card.get_legendary(), "Ei")
        self.card.set_legendary(True)
        self.assertEqual(self.card.get_legendary(), "Kyllä")
        self.card.set_legendary(False)
        self.assertEqual(self.card.get_legendary(), "Ei")
        
    def test_get_tribal(self):
        self.assertEqual(self.card.get_tribal(), "Ei")
        self.card.set_tribal(True)
        self.assertEqual(self.card.get_tribal(), "Kyllä")
        self.card.set_tribal(False)
        self.assertEqual(self.card.get_tribal(), "Ei")
        
    def test_get_subtype(self):
        self.assertEqual(self.card.get_subtype(), "")
        self.card.set_subtype("Beast Bird")
        self.assertEqual(self.card.get_subtype(), "Beast Bird")
        self.card.set_subtype("Bird")
        self.assertEqual(self.card.get_subtype(), "Bird")
        
    def test_show_card(self):
        self.set_card()
        self.card.add_colour("Punainen")        
        #self.assertEqual(self.show_card(), )
        self.assertEqual(True, True)
        
    # Creature
    def set_creature(self):
        self.creature.set_image("img/teemukerppu")
        self.creature.set_legendary(True)
        self.creature.set_tribal(False)
        self.creature.set_subtype("DI Spirit")
        self.creature.set_ruletext("Teemu Kerppu rule")
        self.creature.set_flavourtext("Imaginary")
        self.creature.set_creator("Peruna")
        self.creature.set_seticon("img/seticon1")
        self.creature.set_rarity("Rare")
        self.creature.set_manacost(2)
        self.creature.set_power(3)
        self.creature.set_toughness(4)
        
    def test_set_attributes(self):
        self.set_creature()
        self.assertEqual(self.creature.name, "Teemu Kerppu")
        self.assertEqual(self.creature.image, "img/teemukerppu")
        self.assertEqual(self.creature.maintype, "Creature")
        self.assertEqual(self.creature.legendary, True)
        self.assertEqual(self.creature.tribal, False)
        self.assertEqual(self.creature.subtype, ["DI", "Spirit"])
        self.assertEqual(self.creature.ruletext, "Teemu Kerppu rule")
        self.assertEqual(self.creature.flavourtext, "Imaginary")
        self.assertEqual(self.creature.creator, "Peruna")
        self.assertEqual(self.creature.seticon, "img/seticon1")
        self.assertEqual(self.creature.rarity, "Rare")
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    	
