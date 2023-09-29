import unittest
from entities.tiedot import Tiedot
from ai import Ai


class TestAi(unittest.TestCase):
    def setUp(self):
        self.tiedot = Tiedot()
        self.ai = Ai(self.tiedot)

    def test_valitse_paras_siirto(self):
        self.assertEqual(self.ai.valitse_paras_siirto(), 0)

    def test_lauta_taynna(self):
        self.assertEqual(self.ai.lauta_taynna(self.tiedot.matriisi), False)
        taysi_pelilauta=[[1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1]]
        self.assertEqual(self.ai.lauta_taynna(taysi_pelilauta), True)

    def test_mahdolliset_sarakkeet(self):
         self.assertEqual(self.ai.mahdolliset_sarakkeet(self.tiedot.matriisi), [0,1, 2, 3, 4, 5, 6])
         self.tiedot.matriisi=[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 1, 0]]
         self.assertEqual(self.ai.mahdolliset_sarakkeet(self.tiedot.matriisi), [0, 2, 3, 4, 6])

    def test_siirto_kopio_laudalla(self):
        self.assertEqual(self.ai.siirto_kopio_laudalla(3,self.tiedot.matriisi,1), [[0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])
        
    def test_pelilaudan_pisteytys(self):
        pelilauta=[[2, 1, 1, 1, 1, 0, 0], [2, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0], [
            2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.ai.pelilaudan_pisteytys(pelilauta), -50)

