import unittest
from entities.tiedot import Tiedot
from ai import Ai
from math import inf


class TestAi(unittest.TestCase):
    def setUp(self):
        self.tiedot = Tiedot()
        self.ai = Ai(self.tiedot)

    def test_valitse_paras_siirto(self):
        self.assertEqual(self.ai.valitse_paras_siirto(), 3)

    def test_valitse_paras_siirto_mahdollisuus_voittaa(self):
        self.tiedot.matriisi = [[0, 1, 2, 2, 2, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.ai.valitse_paras_siirto(), 5)

    def test_lauta_taynna(self):
        self.assertEqual(self.ai.lauta_taynna(self.tiedot.matriisi), False)
        taysi_pelilauta = [[1, 2, 1, 2, 1, 2, 1],
                           [1, 2, 1, 2, 1, 2, 1],
                           [1, 2, 1, 2, 1, 2, 1],
                           [1, 2, 1, 2, 1, 2, 1],
                           [1, 2, 1, 2, 1, 2, 1],
                           [1, 2, 1, 2, 1, 2, 1]]
        self.assertEqual(self.ai.lauta_taynna(taysi_pelilauta), True)

    def test_mahdolliset_sarakkeet(self):
        self.assertEqual(self.ai.mahdolliset_sarakkeet(
            self.tiedot.matriisi), [3, 2, 4, 1, 5, 0, 6])

        self.tiedot.matriisi = [[0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0],
                                [0, 2, 0, 0, 0, 1, 0]]
        self.assertEqual(self.ai.mahdolliset_sarakkeet(
            self.tiedot.matriisi), [3, 2, 4, 0, 6])

    def test_voittava_siirto(self):
        pelilauta = [[1, 1, 1, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.ai.voittava_siirto(pelilauta, 1), True)
        pelilauta = [[2, 0, 0, 0, 0, 0, 0],
                     [2, 0, 0, 0, 0, 0, 0],
                     [2, 0, 0, 0, 0, 0, 0],
                     [2, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.ai.voittava_siirto(pelilauta, 2), True)
        pelilauta = [[0, 2, 1, 1, 2, 0, 0],
                     [0, 1, 1, 2, 0, 0, 0],
                     [0, 1, 2, 0, 0, 0, 0],
                     [0, 2, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.ai.voittava_siirto(pelilauta, 2), True)
        pelilauta = [[2, 1, 2, 1, 0, 0, 0],
                     [0, 2, 1, 1, 0, 0, 0],
                     [0, 0, 2, 1, 0, 0, 0],
                     [0, 0, 0, 2, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.ai.voittava_siirto(pelilauta, 2), True)
        pelilauta = [[2, 1, 2, 1, 0, 0, 0],
                     [1, 2, 2, 1, 0, 0, 0],
                     [0, 0, 1, 1, 0, 0, 0],
                     [0, 0, 0, 2, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.ai.voittava_siirto(pelilauta, 2), False)

    def test_siirto_kopio_laudalla(self):
        self.ai.siirto_kopio_laudalla(3, self.tiedot.matriisi, 1)
        self.ai.siirto_kopio_laudalla(3, self.tiedot.matriisi, 2)
        self.assertEqual(self.ai.siirto_kopio_laudalla(3, self.tiedot.matriisi, 1), [[0, 0, 0, 1, 0, 0, 0],
                                                                                     [0, 0, 0, 2,
                                                                                         0, 0, 0],
                                                                                     [0, 0, 0, 1,
                                                                                         0, 0, 0],
                                                                                     [0, 0, 0, 0,
                                                                                         0, 0, 0],
                                                                                     [0, 0, 0, 0,
                                                                                         0, 0, 0],
                                                                                     [0, 0, 0, 0, 0, 0, 0]])

    def test_siirto_kopio_laudalla_alimmalle_riville(self):
        self.assertEqual(self.ai.siirto_kopio_laudalla(3, self.tiedot.matriisi, 2), [[0, 0, 0, 2, 0, 0, 0],
                                                                                     [0, 0, 0, 0,
                                                                                         0, 0, 0],
                                                                                     [0, 0, 0, 0,
                                                                                         0, 0, 0],
                                                                                     [0, 0, 0, 0,
                                                                                         0, 0, 0],
                                                                                     [0, 0, 0, 0,
                                                                                         0, 0, 0],
                                                                                     [0, 0, 0, 0, 0, 0, 0]])

    def test_pelilaudan_pisteytys(self):
        pelilauta = [[2, 1, 1, 1, 0, 0, 0],
                     [2, 0, 0, 0, 0, 0, 0],
                     [2, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]]
        #pisteet: 50+30-15=65
        self.assertEqual(self.ai.pelilaudan_pisteytys(pelilauta), 65)
        pelilauta = [[0, 2, 2, 2, 0, 0, 0],
                     [0, 2, 1, 1, 0, 0, 0],
                     [0, 0, 2, 1, 0, 0, 0],
                     [0, 0, 0, 2, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]]
        #pisteet: 100+50+50+100+50+50+2*10=420
        self.assertEqual(self.ai.pelilaudan_pisteytys(pelilauta), 420)
        pelilauta = [[1, 1, 2, 2, 1, 2, 0],
                     [0, 2, 1, 2, 1, 2, 0],
                     [0, 0, 2, 1, 2, 1, 0],
                     [0, 0, 0, 2, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]]
        #pisteet: 3*10+100+50+50+50+50-15=315
        self.assertEqual(self.ai.pelilaudan_pisteytys(pelilauta), 315)

    def test_minimax_tunnistaa_voitot_ja_tasapelin(self):
        pelilauta = [[2, 1, 1, 1, 0, 0, 0],
                     [0, 2, 1, 2, 0, 0, 0],
                     [0, 0, 2, 1, 0, 0, 0],
                     [0, 0, 0, 2, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.ai.minimax(2, True, -1000000,
                         10000000, pelilauta), (None, inf))
        pelilauta = [[2, 2, 2, 1, 0, 0, 0],
                     [2, 1, 1, 0, 0, 0, 0],
                     [2, 1, 0, 0, 0, 0, 0],
                     [1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.ai.minimax(2, True, -1000000,
                         10000000, pelilauta), (None, -inf))
        pelilauta = [[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [1, 2, 1, 2, 1, 2, 1]]
        self.assertEqual(self.ai.minimax(
            2, True, -1000000, 10000000, pelilauta), (None, 0))

    def test_minimax_voitto_mahdollinen(self):
        pelilauta = [[1, 1, 2, 1, 2, 1, 0],
                     [0, 2, 1, 1, 1, 2, 0],
                     [0, 0, 2, 2, 1, 0, 0],
                     [0, 0, 0, 2, 2, 0, 0],
                     [0, 0, 0, 2, 1, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0]]
        palautus = self.ai.minimax(6, True, -1000000, 10000000, pelilauta)
        self.assertEqual(palautus, (2, inf))

    def test_minimax_voitto_mahdollinen_2(self):
        pelilauta = [[0, 1, 2, 2, 1, 1, 0],
                     [0, 2, 1, 1, 2, 1, 0],
                     [0, 0, 1, 2, 1, 0, 0],
                     [0, 0, 2, 2, 2, 0, 0],
                     [0, 0, 2, 2, 0, 0, 0],
                     [0, 0, 1, 1, 0, 0, 0]]
        palautus = self.ai.minimax(6, True, -1000000, 10000000, pelilauta)
        self.assertEqual(palautus, (4, inf))

    def test_minimax_voitto_mahdollinen_3(self):
        pelilauta = [[1, 1, 2, 2, 0, 0, 1],
                     [0, 1, 2, 2, 0, 0, 0],
                     [0, 0, 2, 2, 0, 0, 0],
                     [0, 0, 1, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]]
        palautus = self.ai.minimax(6, True, -1000000, 10000000, pelilauta)
        self.assertEqual(palautus, (1, inf))
