import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
        
    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        
    def test_kortille_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(25)
        self.assertEqual(str(self.maksukortti), "saldo: 0.35")
        
    def test_kortilta_ottaminen_toimii(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")
    
    def test_kortilta_ottaminen_toimii_neg(self):
        self.maksukortti.ota_rahaa(15)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        
    def test_kortilta_ottaminen_toimii_palautus_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)
        
    def test_kortilta_ottaminen_toimii_palautus_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(15), False)
