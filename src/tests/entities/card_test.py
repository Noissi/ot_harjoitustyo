import unittest
from entities.card import Card
from entities.card_creature import Creature
from entities.card_land import Land
from entities.card_instant import Instant
from entities.card_sorcery import Sorcery
from entities.card_enchantment import Enchantment
from entities.card_planeswalker import Planeswalker
from entities.card_artifact import Artifact
from entities.card_enchantment_creature import EnchantmentCreature
from entities.card_artifact_creature import ArtifactCreature

class TestCard(unittest.TestCase):
    def setUp(self):
    	self.card = Card('Graduated friend')
    	self.creature = Creature('Teemu K')
    	###
    	
    def set_card(self):    
        self.card.set_id("1234567")
        self.card.set_name("Party Tutor")
        self.card.set_image("img/partytutor")
        self.card.set_maintype("Creature")
        self.card.set_legendary(False)
        self.card.set_tribal(True)
        self.card.set_subtype("Teekkari ISO")
        self.card.set_colour("Vihreä")
        self.card.set_manacost("2U")
        self.card.set_power(3)
        self.card.set_toughness(2)
        self.card.set_feature("Haste,Trample")
        self.card.set_ruletext("Party Tutor rule")
        self.card.set_flavourtext("Party")
        self.card.set_creator("Masa")
        self.card.set_seticon("img/seticon1")
        self.card.set_rarity("Common")
    	
    def test_set_attributes(self):
        self.set_card()
        self.assertEqual(self.card.get_id(), "1234567")
        self.assertEqual(self.card.get_name(), "Party Tutor")
        self.assertEqual(self.card.get_image(), "img/partytutor")
        self.assertEqual(self.card.get_maintype(), "Creature")
        self.assertEqual(self.card.get_legendary(), False)
        self.assertEqual(self.card.get_tribal(), True)
        self.assertEqual(self.card.get_subtype(), ["Teekkari", "ISO"])
        self.assertEqual(self.card.get_colour(), ["Vihreä"])
        self.assertEqual(self.card.get_manacost(), "2U")
        self.assertEqual(self.card.get_power(), 3)
        self.assertEqual(self.card.get_toughness(), 2)
        self.assertEqual(self.card.get_feature(), ["Haste", "Trample"])
        self.assertEqual(self.card.get_ruletext(), "Party Tutor rule")
        self.assertEqual(self.card.get_flavourtext(), "Party")
        self.assertEqual(self.card.get_creator(), "Masa")
        self.assertEqual(self.card.get_seticon(), "img/seticon1")
        self.assertEqual(self.card.get_rarity(), "Common")
        
    def test_get_legendary_print(self):
        self.assertEqual(self.card.get_legendary_print(), "Ei")
        self.card.set_legendary(True)
        self.assertEqual(self.card.get_legendary_print(), "Kyllä")
        self.card.set_legendary(False)
        self.assertEqual(self.card.get_legendary_print(), "Ei")
        
    def test_get_tribal_print(self):
        self.assertEqual(self.card.get_tribal_print(), "Ei")
        self.card.set_tribal(True)
        self.assertEqual(self.card.get_tribal_print(), "Kyllä")
        self.card.set_tribal(False)
        self.assertEqual(self.card.get_tribal_print(), "Ei")
        
    def test_get_subtype_print(self):
        self.assertEqual(self.card.get_subtype_print(), "")
        self.card.set_subtype("Beast Bird")
        self.assertEqual(self.card.get_subtype_print(), "Beast Bird")
        self.card.set_subtype("Bird")
        self.assertEqual(self.card.get_subtype_print(), "Bird")
        
    def test_get_subtype_list(self):
        self.assertEqual(self.card.get_subtype_list(), [])
        self.card.set_subtype("Beast Bird")
        self.assertEqual(self.card.get_subtype_list(), ["Beast", "Bird"])
        self.card.set_subtype("Bird")
        self.assertEqual(self.card.get_subtype_list(), ["Bird"])
        
    def test_add_colour(self):
        self.card.add_colour("Punainen")
        self.assertEqual(self.card.get_colour(), ["Punainen"])
        self.card.add_colour("Valkoinen")
        self.assertEqual(self.card.get_colour(), ["Punainen", "Valkoinen"])        
        self.card.add_colour("Valkoinen")
        self.assertEqual(self.card.get_colour(), ["Punainen", "Valkoinen"])
        self.card.add_colour("Sininen")
        self.assertEqual(self.card.get_colour(), ["Punainen", "Valkoinen", "Sininen"])
        
    def test_remove_colour(self):
        self.card.add_colour("Punainen")
        self.card.add_colour("Valkoinen")
        self.card.remove_colour("Vihreä")
        self.assertEqual(self.card.get_colour(), ["Punainen", "Valkoinen"])
        self.card.remove_colour("Punainen")
        self.assertEqual(self.card.get_colour(), ["Valkoinen"])
        self.card.remove_colour("Valkoinen")
        self.assertEqual(self.card.get_colour(), [])
        self.card.remove_colour("Valkoinen")
        self.assertEqual(self.card.get_colour(), [])
        
    def test_get_card_colour(self):
        self.assertEqual(self.card.get_card_colour(), "Väritön")
        self.card.add_colour("Punainen")
        self.assertEqual(self.card.get_card_colour(), "Punainen")
        self.card.add_colour("Vihreä")
        self.assertEqual(self.card.get_card_colour(), "Kulta")
        self.card.remove_colour("Punainen")
        self.assertEqual(self.card.get_card_colour(), "Vihreä")
        self.card.remove_colour("Vihreä")
        self.assertEqual(self.card.get_card_colour(), "Väritön")
        
    def test_get_colour_print(self):
        self.assertEqual(self.card.get_colour_print(), "Väritön")
        self.card.add_colour("Punainen")
        self.assertEqual(self.card.get_colour_print(), "Punainen")
        self.card.add_colour("Vihreä")
        self.assertEqual(self.card.get_colour_print(), "Punainen, Vihreä")
        
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
        
    def test_get_power_print(self):
        self.assertEqual(self.card.get_power_print(), 0)
        self.card.set_power(4)
        self.assertEqual(self.card.get_power_print(), 4)
        self.card.set_power(2)
        self.assertEqual(self.card.get_power_print(), 2)
        
    def test_get_toughness_print(self):
        self.assertEqual(self.card.get_toughness_print(), 0)
        self.card.set_toughness(10)
        self.assertEqual(self.card.get_toughness_print(), 10)
        self.card.set_toughness(1)
        self.assertEqual(self.card.get_toughness_print(), 1)
        
    def test_add_feature(self):
        self.assertEqual(self.card.get_feature(), [])
        self.card.add_feature("Flying")
        self.assertEqual(self.card.get_feature(), ["Flying"])
        self.card.add_feature("Vigilance")
        self.assertEqual(self.card.get_feature(), ["Flying", "Vigilance"])
        self.card.add_feature("Vigilance")
        self.assertEqual(self.card.get_feature(), ["Flying", "Vigilance"])        
        self.card.add_feature("Trample")
        self.assertEqual(self.card.get_feature(), ["Flying", "Vigilance", "Trample"])
    
    def test_remove_feature(self):
        self.card.add_feature("Reach")
        self.card.add_feature("Deathtouch")
        self.card.remove_feature("Firststrike")
        self.assertEqual(self.card.get_feature(), ["Reach", "Deathtouch"])
        self.card.remove_feature("Deathtouch")
        self.assertEqual(self.card.get_feature(), ["Reach"])
        self.card.remove_feature("Reach")
        self.assertEqual(self.card.get_feature(), [])
        self.card.remove_feature("Reach")
        self.assertEqual(self.card.get_feature(), [])
        
    def test_get_feature_print(self):
        self.assertEqual(self.card.get_feature_print(), "")
        self.card.add_feature("Flying")
        self.card.add_feature("Vigilance")
        self.assertEqual(self.card.get_feature_print(), "Flying, Vigilance")
        self.card.add_feature("Trample")
        self.assertEqual(self.card.get_feature_print(), "Flying, Vigilance, Trample")
        self.card.remove_feature("Vigilance")
        self.assertEqual(self.card.get_feature_print(), "Flying, Trample")
        
    def test_get_feature_list(self):
        self.assertEqual(self.card.get_feature_list(), [])
        self.card.add_feature("Flying")
        self.card.add_feature("Vigilance")
        self.assertEqual(self.card.get_feature_list(), ["Flying", "Vigilance"])
        self.card.add_feature("Trample")
        self.assertEqual(self.card.get_feature_list(), ["Flying", "Vigilance", "Trample"])
        self.card.remove_feature("Vigilance")
        self.assertEqual(self.card.get_feature_list(), ["Flying", "Trample"])
        
    def test_get_feature2_list(self):
        self.assertEqual(self.card.get_feature2_list(), [])        
        
    def test_show_card(self):
        self.set_card()
        self.card.add_colour("Punainen")        
        #self.assertEqual(self.show_card(), )
        self.assertEqual(True, True)
        
    # Creature
    def set_creature(self):
        self.creature.set_id("891234")
        self.creature.set_name("Teemu Kerppu")
        self.creature.set_image("img/teemukerppu")
        self.creature.set_legendary(True)
        self.creature.set_subtype("DI Spirit")
        self.creature.set_manacost("2U2")
        self.creature.set_power(3)
        self.creature.set_toughness(4)
        self.creature.set_ruletext("Teemu Kerppu rule")
        self.creature.set_flavourtext("Imaginary")
        self.creature.set_creator("Peruna")
        self.creature.set_seticon("img/seticon1")
        self.creature.set_rarity("Rare")
        
    def test_set_creature(self):
        self.set_creature()        
        self.assertEqual(self.creature.get_id(), "891234")
        self.assertEqual(self.creature.get_name(), "Teemu Kerppu")
        self.assertEqual(self.creature.get_image(), "img/teemukerppu")
        self.assertEqual(self.creature.get_maintype(), "Creature")
        self.assertEqual(self.creature.get_legendary(), True)
        self.assertEqual(self.creature.get_tribal(), None)
        self.assertEqual(self.creature.get_subtype(), ["DI", "Spirit"])
        self.assertEqual(self.creature.get_manacost(), "2U2")
        self.assertEqual(self.creature.get_power(), 3)
        self.assertEqual(self.creature.get_toughness(), 4)
        self.assertEqual(self.creature.get_ruletext(), "Teemu Kerppu rule")
        self.assertEqual(self.creature.get_flavourtext(), "Imaginary")
        self.assertEqual(self.creature.get_creator(), "Peruna")
        self.assertEqual(self.creature.get_seticon(), "img/seticon1")
        self.assertEqual(self.creature.get_rarity(), "Rare")
        
    def test_copy_creature(self):
        self.set_card()
        creature = Creature(self.card.get_name())
        creature.copy(self.card)
        self.assertEqual(creature.get_id(), "1234567")
        self.assertEqual(creature.get_name(), "Party Tutor")
        self.assertEqual(creature.get_image(), "img/partytutor")
        self.assertEqual(creature.get_maintype(), "Creature")
        self.assertEqual(creature.get_legendary(), False)
        self.assertEqual(creature.get_tribal(), None)
        self.assertEqual(creature.get_subtype(), ["Teekkari", "ISO"])
        self.assertEqual(creature.get_colour(), ["Vihreä"])
        self.assertEqual(creature.get_manacost(), "2U")
        self.assertEqual(creature.get_power(), 3)
        self.assertEqual(creature.get_toughness(), 2)
        self.assertEqual(creature.get_feature(), ["Haste", "Trample"])
        self.assertEqual(creature.get_feature2(), [])
        self.assertEqual(creature.get_ruletext(), "Party Tutor rule")
        self.assertEqual(creature.get_flavourtext(), "Party")
        self.assertEqual(creature.get_creator(), "Masa")
        self.assertEqual(creature.get_seticon(), "img/seticon1")
        self.assertEqual(creature.get_rarity(), "Common")
    
    # Artifact
    def test_copy_artifact(self):
        self.set_card()
        k = Artifact(self.card.get_name())
        k.copy(self.card)
        self.assertEqual(k.get_id(), "1234567")
        self.assertEqual(k.get_name(), "Party Tutor")
        self.assertEqual(k.get_image(), "img/partytutor")
        self.assertEqual(k.get_maintype(), "Artifact")
        self.assertEqual(k.get_legendary(), False)
        self.assertEqual(k.get_tribal(), True)
        self.assertEqual(k.get_subtype(), ["Teekkari", "ISO"])
        self.assertEqual(k.get_colour(), ["Vihreä"])
        self.assertEqual(k.get_manacost(), "2U")
        self.assertEqual(k.get_power(), None)
        self.assertEqual(k.get_toughness(), None)
        self.assertEqual(k.get_feature(), [])
        self.assertEqual(k.get_feature2(), ["Hexproof", "Indestructible", "Flash"])
        self.assertEqual(k.get_ruletext(), "Party Tutor rule")
        self.assertEqual(k.get_flavourtext(), "Party")
        self.assertEqual(k.get_creator(), "Masa")
        self.assertEqual(k.get_seticon(), "img/seticon1")
        self.assertEqual(k.get_rarity(), "Common")

    def test_vehicle_artifact(self):
        self.set_card()
        k = Artifact(self.card.get_name())
        k.copy(self.card)
        k.set_subtype("Vehicle")
        self.assertEqual(k.get_id(), "1234567")
        self.assertEqual(k.get_name(), "Party Tutor")
        self.assertEqual(k.get_image(), "img/partytutor")
        self.assertEqual(k.get_maintype(), "Artifact")
        self.assertEqual(k.get_legendary(), False)
        self.assertEqual(k.get_tribal(), True)
        self.assertEqual(k.get_subtype(), ["Vehicle"])
        self.assertEqual(k.get_colour(), ["Vihreä"])
        self.assertEqual(k.get_manacost(), "2U")
        self.assertEqual(k.get_power(), 0)
        self.assertEqual(k.get_toughness(), 0)
        self.assertEqual(k.get_feature(), [])
        self.assertEqual(k.get_feature2(), ["Hexproof", "Indestructible", "Flash"])
        self.assertEqual(k.get_ruletext(), "Party Tutor rule")
        self.assertEqual(k.get_flavourtext(), "Party")
        self.assertEqual(k.get_creator(), "Masa")
        self.assertEqual(k.get_seticon(), "img/seticon1")
        self.assertEqual(k.get_rarity(), "Common")
        k.set_subtype("Vehicle Bird")
        self.assertEqual(k.get_id(), "1234567")
        self.assertEqual(k.get_name(), "Party Tutor")
        self.assertEqual(k.get_image(), "img/partytutor")
        self.assertEqual(k.get_maintype(), "Artifact")
        self.assertEqual(k.get_legendary(), False)
        self.assertEqual(k.get_tribal(), True)
        self.assertEqual(k.get_subtype(), ["Vehicle", "Bird"])
        self.assertEqual(k.get_colour(), ["Vihreä"])
        self.assertEqual(k.get_manacost(), "2U")
        self.assertEqual(k.get_power(), None)
        self.assertEqual(k.get_toughness(), None)
        self.assertEqual(k.get_feature(), [])
        self.assertEqual(k.get_feature2(), ["Hexproof", "Indestructible", "Flash"])
        self.assertEqual(k.get_ruletext(), "Party Tutor rule")
        self.assertEqual(k.get_flavourtext(), "Party")
        self.assertEqual(k.get_creator(), "Masa")
        self.assertEqual(k.get_seticon(), "img/seticon1")
        self.assertEqual(k.get_rarity(), "Common")
        
    def test_feature_artifact(self):
        self.set_card()
        k = Artifact(self.card.get_name())
        k.copy(self.card)
        k.add_feature("Trample")
        self.assertEqual(k.get_feature(), [])
        k.add_feature("Flash")
        self.assertEqual(k.get_feature(), ["Flash"])
        k.add_feature("Vigilance")
        self.assertEqual(k.get_feature(), ["Flash"])
        k.add_feature("Hexproof")
        self.assertEqual(k.get_feature(), ["Flash", "Hexproof"])        
    
    # Artifact creature
    def test_copy_artifact_creature(self):
        self.set_card()
        k = ArtifactCreature(self.card.get_name())
        k.copy(self.card)
        self.assertEqual(k.get_id(), "1234567")
        self.assertEqual(k.get_name(), "Party Tutor")
        self.assertEqual(k.get_image(), "img/partytutor")
        self.assertEqual(k.get_maintype(), "Artifact")
        self.assertEqual(k.get_legendary(), False)
        self.assertEqual(k.get_tribal(), None)
        self.assertEqual(k.get_subtype(), ["Teekkari", "ISO"])
        self.assertEqual(k.get_colour(), ["Vihreä"])
        self.assertEqual(k.get_manacost(), "2U")
        self.assertEqual(k.get_power(), 3)
        self.assertEqual(k.get_toughness(), 2)
        self.assertEqual(k.get_feature(), ["Haste", "Trample"])
        self.assertEqual(k.get_feature2(), [])
        self.assertEqual(k.get_ruletext(), "Party Tutor rule")
        self.assertEqual(k.get_flavourtext(), "Party")
        self.assertEqual(k.get_creator(), "Masa")
        self.assertEqual(k.get_seticon(), "img/seticon1")
        self.assertEqual(k.get_rarity(), "Common")
        
    # Enchantment
    def test_copy_artifact_creature(self):
        self.set_card()
        k = Enchantment(self.card.get_name())
        k.copy(self.card)
        self.assertEqual(k.get_id(), "1234567")
        self.assertEqual(k.get_name(), "Party Tutor")
        self.assertEqual(k.get_image(), "img/partytutor")
        self.assertEqual(k.get_maintype(), "Enchantment")
        self.assertEqual(k.get_legendary(), False)
        self.assertEqual(k.get_tribal(), True)
        self.assertEqual(k.get_subtype(), ["Teekkari", "ISO"])
        self.assertEqual(k.get_colour(), ["Vihreä"])
        self.assertEqual(k.get_manacost(), "2U")
        self.assertEqual(k.get_power(), None)
        self.assertEqual(k.get_toughness(), None)
        self.assertEqual(k.get_feature(), [])
        self.assertEqual(k.get_feature2(), ["Hexproof", "Indestructible", "Flash"])
        self.assertEqual(k.get_ruletext(), "Party Tutor rule")
        self.assertEqual(k.get_flavourtext(), "Party")
        self.assertEqual(k.get_creator(), "Masa")
        self.assertEqual(k.get_seticon(), "img/seticon1")
        self.assertEqual(k.get_rarity(), "Common")
        
    # Enchantment creature
    def test_copy_artifact_creature(self):
        self.set_card()
        k = EnchantmentCreature(self.card.get_name())
        k.copy(self.card)
        self.assertEqual(k.get_id(), "1234567")
        self.assertEqual(k.get_name(), "Party Tutor")
        self.assertEqual(k.get_image(), "img/partytutor")
        self.assertEqual(k.get_maintype(), "Enchantment Creature")
        self.assertEqual(k.get_legendary(), False)
        self.assertEqual(k.get_tribal(), None)
        self.assertEqual(k.get_subtype(), ["Teekkari", "ISO"])
        self.assertEqual(k.get_colour(), ["Vihreä"])
        self.assertEqual(k.get_manacost(), "2U")
        self.assertEqual(k.get_power(), 3)
        self.assertEqual(k.get_toughness(), 2)
        self.assertEqual(k.get_feature(), ["Haste", "Trample"])
        self.assertEqual(k.get_feature2(), [])
        self.assertEqual(k.get_ruletext(), "Party Tutor rule")
        self.assertEqual(k.get_flavourtext(), "Party")
        self.assertEqual(k.get_creator(), "Masa")
        self.assertEqual(k.get_seticon(), "img/seticon1")
        self.assertEqual(k.get_rarity(), "Common")
        
    # Instant
    def test_copy_artifact_creature(self):
        self.set_card()
        k = Instant(self.card.get_name())
        k.copy(self.card)
        self.assertEqual(k.get_id(), "1234567")
        self.assertEqual(k.get_name(), "Party Tutor")
        self.assertEqual(k.get_image(), "img/partytutor")
        self.assertEqual(k.get_maintype(), "Instant")
        self.assertEqual(k.get_legendary(), False)
        self.assertEqual(k.get_tribal(), True)
        self.assertEqual(k.get_subtype(), ["Teekkari", "ISO"])
        self.assertEqual(k.get_colour(), ["Vihreä"])
        self.assertEqual(k.get_manacost(), "2U")
        self.assertEqual(k.get_power(), None)
        self.assertEqual(k.get_toughness(), None)
        self.assertEqual(k.get_feature(), None)
        self.assertEqual(k.get_feature2(), [])
        self.assertEqual(k.get_ruletext(), "Party Tutor rule")
        self.assertEqual(k.get_flavourtext(), "Party")
        self.assertEqual(k.get_creator(), "Masa")
        self.assertEqual(k.get_seticon(), "img/seticon1")
        self.assertEqual(k.get_rarity(), "Common")
        
    # Land
    def test_copy_artifact_creature(self):
        self.set_card()
        k = Land(self.card.get_name())
        k.copy(self.card)
        self.assertEqual(k.get_id(), "1234567")
        self.assertEqual(k.get_name(), "Party Tutor")
        self.assertEqual(k.get_image(), "img/partytutor")
        self.assertEqual(k.get_maintype(), "Land")
        self.assertEqual(k.get_legendary(), False)
        self.assertEqual(k.get_tribal(), None)
        self.assertEqual(k.get_subtype(), ["Teekkari", "ISO"])
        self.assertEqual(k.get_colour(), ["Vihreä"])
        self.assertEqual(k.get_manacost(), None)
        self.assertEqual(k.get_power(), None)
        self.assertEqual(k.get_toughness(), None)
        self.assertEqual(k.get_feature(), [])
        self.assertEqual(k.get_feature2(), ["Hexproof", "Indestructible"])
        self.assertEqual(k.get_ruletext(), "Party Tutor rule")
        self.assertEqual(k.get_flavourtext(), "Party")
        self.assertEqual(k.get_creator(), "Masa")
        self.assertEqual(k.get_seticon(), "img/seticon1")
        self.assertEqual(k.get_rarity(), "Common")
        
    # Planeswalker
    def test_copy_artifact_creature(self):
        self.set_card()
        k = Planeswalker(self.card.get_name())
        k.copy(self.card)
        self.assertEqual(k.get_id(), "1234567")
        self.assertEqual(k.get_name(), "Party Tutor")
        self.assertEqual(k.get_image(), "img/partytutor")
        self.assertEqual(k.get_maintype(), "Planeswalker")
        self.assertEqual(k.get_legendary(), False)
        self.assertEqual(k.get_tribal(), None)
        self.assertEqual(k.get_subtype(), ["Teekkari", "ISO"])
        self.assertEqual(k.get_colour(), ["Vihreä"])
        self.assertEqual(k.get_manacost(), "2U")
        self.assertEqual(k.get_power(), 3)
        self.assertEqual(k.get_toughness(), 2)
        self.assertEqual(k.get_feature(), ["Haste", "Trample"])
        self.assertEqual(k.get_feature2(), [])
        self.assertEqual(k.get_ruletext(), "Party Tutor rule")
        self.assertEqual(k.get_flavourtext(), "Party")
        self.assertEqual(k.get_creator(), "Masa")
        self.assertEqual(k.get_seticon(), "img/seticon1")
        self.assertEqual(k.get_rarity(), "Common")
        
    # Sorcery
    def test_copy_artifact_creature(self):
        self.set_card()
        k = Sorcery(self.card.get_name())
        k.copy(self.card)
        self.assertEqual(k.get_id(), "1234567")
        self.assertEqual(k.get_name(), "Party Tutor")
        self.assertEqual(k.get_image(), "img/partytutor")
        self.assertEqual(k.get_maintype(), "Sorcery")
        self.assertEqual(k.get_legendary(), False)
        self.assertEqual(k.get_tribal(), True)
        self.assertEqual(k.get_subtype(), ["Teekkari", "ISO"])
        self.assertEqual(k.get_colour(), ["Vihreä"])
        self.assertEqual(k.get_manacost(), "2U")
        self.assertEqual(k.get_power(), None)
        self.assertEqual(k.get_toughness(), None)
        self.assertEqual(k.get_feature(), None)
        self.assertEqual(k.get_feature2(), [])
        self.assertEqual(k.get_ruletext(), "Party Tutor rule")
        self.assertEqual(k.get_flavourtext(), "Party")
        self.assertEqual(k.get_creator(), "Masa")
        self.assertEqual(k.get_seticon(), "img/seticon1")
        self.assertEqual(k.get_rarity(), "Common")
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    	
