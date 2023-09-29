import unittest
from entities.connectfour import ConnectFour
from entities.tiedot import Tiedot


class TestConnectFour(unittest.TestCase):
    def setUp(self):
        self.tiedot = Tiedot()
        self.connectfour = ConnectFour(self.tiedot)

    def test_vuoro_sarake_taynna(self):
        self.tiedot.matriisi = [[0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1]]
        self.connectfour_sarake_taynna = ConnectFour(self.tiedot)
        self.assertEqual(self.connectfour_sarake_taynna.vuoro(6),
                         "siirto epaonnistui")

    def test_vuoro_voittava_siirto(self):
        self.tiedot = Tiedot()
        self.tiedot.matriisi = [[2, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [
            1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0]]
        self.connectfour_voittava_lauta = ConnectFour(self.tiedot)
        self.assertEqual(
            self.connectfour_voittava_lauta.vuoro(3), "voittava siirto")

    def test_vuoro_lauta_taynna(self):
        self.tiedot.matriisi = [[1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1], [
            2, 1, 2, 1, 2, 1, 2], [2, 1, 2, 1, 2, 1, 2], [2, 1, 2, 1, 2, 1, 0]]
        self.connectfour_lauta_taynna = ConnectFour(self.tiedot)
        self.assertEqual(
            self.connectfour_lauta_taynna.vuoro(6), "lauta taynna")

    def test_vuoro_siirto_onnistui(self):
        self.assertEqual(self.connectfour.vuoro(0), "siirto onnistui")

    def test_sarake_taynna_false(self):
        self.assertEqual(self.connectfour.sarake_taynna(0), False)

    def test_sarake_taynna_true(self):
        self.tiedot.matriisi = [[0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1]]
        self.connectfour_sarake_taynna = ConnectFour(self.tiedot)
        self.assertEqual(self.connectfour_sarake_taynna.sarake_taynna(6), True)

    def test_lauta_taynna_false(self):
        self.assertEqual(self.connectfour.lauta_taynna(), False)

    def test_lauta_taynna_true(self):
        self.tiedot.matriisi = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 1, 1], [
            1, 1, 1, 1, 2, 1, 1], [2, 2, 2, 2, 2, 2, 1], [1, 1, 1, 1, 1, 1, 1]]
        self.connectfour_lauta_taynna = ConnectFour(self.tiedot)
        self.assertEqual(self.connectfour_lauta_taynna.lauta_taynna(), True)

    def test_voittava_siirto_pystyssa(self):
        self.tiedot.matriisi = [[1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [
            1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.connectfour_voittava_siirto = ConnectFour(self.tiedot)
        self.assertEqual(
            self.connectfour_voittava_siirto.voittava_siirto(), True)

    def test_voittava_siirto_vaaka(self):
        self.tiedot.matriisi = [[1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.connectfour_voittava_siirto = ConnectFour(self.tiedot)
        self.assertEqual(
            self.connectfour_voittava_siirto.voittava_siirto(), True)

    def test_voittava_siirto_vino_ylos(self):
        self.tiedot.matriisi = [[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [
            0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.connectfour_voittava_siirto = ConnectFour(self.tiedot)
        self.assertEqual(
            self.connectfour_voittava_siirto.voittava_siirto(), True)

    def test_voittava_siirto_vino_alas(self):
        self.tiedot.matriisi = [[0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0, 0], [
            0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.connectfour_voittava_siirto = ConnectFour(self.tiedot)
        self.assertEqual(
            self.connectfour_voittava_siirto.voittava_siirto(), True)

    def test_tiedot_vaihda_pelaajaa_1(self):
        self.tiedot.pelaaja = 2
        self.tiedot.vaihda_pelaaja()
        self.assertEqual(self.tiedot.pelaaja, 1)

    def test_tiedot_vaihda_pelaajaa_2(self):
        self.tiedot.pelaaja = 1
        self.tiedot.vaihda_pelaaja()
        self.assertEqual(self.tiedot.pelaaja, 2)
