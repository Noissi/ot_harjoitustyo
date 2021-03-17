import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(200)

    def test_kassassa_oikea_maara_rahaa(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        
    def test_kassassa_oikea_maara_myytyja_lounaita(self):
        myydyt = self.kassa.edulliset + self.kassa.maukkaat
        self.assertEqual(myydyt, 0)
        
    def test_osta_kateisella_edullinen_kasvu(self):
        self.kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        
    def test_osta_kateisella_edullinen_vaihtoraha(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(250), 10)
        
    def test_osta_kateisella_edullinen_myydyt_lisaantyy(self):
        self.kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassa.edulliset, 1)
        
    def test_osta_kateisella_edullinen_kasvu_ei_tarpeeksi_rahaa(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        
    def test_osta_kateisella_edullinen_vaihtoraha_ei_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(200), 200)
        
    def test_osta_kateisella_edullinen_myydyt_lisaantyy_ei_tarpeeksi_rahaa(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.edulliset, 0)
        
    def test_osta_kateisella_maukas_kasvu(self):
        self.kassa.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        
    def test_osta_kateisella_maukas_vaihtoraha(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(450), 50)
        
    def test_osta_kateisella_maukas_myydyt_lisaantyy(self):
        self.kassa.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassa.maukkaat, 1)
        
    def test_osta_kateisella_maukas_kasvu_ei_tarpeeksi_rahaa(self):
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        
    def test_osta_kateisella_maukas_vaihtoraha_ei_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(200), 200)
        
    def test_osta_kateisella_maukas_myydyt_lisaantyy_ei_tarpeeksi_rahaa(self):
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.maukkaat, 0)
        
    def test_osta_kortilla_edullisesti_tarpeeksi_rahaa(self):
        self.kortti.lataa_rahaa(200)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)
        
    def test_osta_kortilla_edullisesti_tarpeeksi_rahaa_veloitus(self):
        self.kortti.lataa_rahaa(200)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 1.6")
        
    def test_osta_kortilla_edullisesti_tarpeeksi_rahaa_myydyt(self):
        self.kortti.lataa_rahaa(200)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 1)
        
    def test_osta_kortilla_edullisesti_ei_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), False)
        
    def test_osta_kortilla_edullisesti_ei_tarpeeksi_rahaa_veloitus(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 2.0")
        
    def test_osta_kortilla_edullisesti_ei_tarpeeksi_rahaa_myydyt(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_osta_kortilla_maukkaasti_tarpeeksi_rahaa(self):
        self.kortti.lataa_rahaa(200)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), True)
        
    def test_osta_kortilla_maukkaasti_tarpeeksi_rahaa_veloitus(self):
        self.kortti.lataa_rahaa(200)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 0.0")
        
    def test_osta_kortilla_maukkaasti_tarpeeksi_rahaa_myydyt(self):
        self.kortti.lataa_rahaa(200)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 1)
        
    def test_osta_kortilla_maukkaasti_ei_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), False)
        
    def test_osta_kortilla_maukkaasti_ei_tarpeeksi_rahaa_veloitus(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 2.0")
        
    def test_osta_kortilla_maukkaasti_ei_tarpeeksi_rahaa_myydyt(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 0)
        
    def test_rahaa_ladatessa_kassaan_tulee_rahaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 210)
        self.assertEqual(self.kassa.kassassa_rahaa, 1210)
        
    def test_rahaa_ladatessa_kassaan_tulee_rahaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 210)
        self.assertEqual(str(self.kortti), "saldo: 4.1")
        
    def test_rahaa_ladataan_negatiivinen_maara(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -210)
        self.assertEqual(str(self.kortti), "saldo: 2.0")
    
