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

    def test_lauta_taynna(self):
        self.assertEqual(self.ai.lauta_taynna(self.tiedot.matriisi), False)
        taysi_pelilauta = [[1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1], [
            1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1]]
        self.assertEqual(self.ai.lauta_taynna(taysi_pelilauta), True)

    def test_mahdolliset_sarakkeet(self):
        self.assertEqual(self.ai.mahdolliset_sarakkeet(
            self.tiedot.matriisi), [0, 1, 2, 3, 4, 5, 6])
        self.tiedot.matriisi = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 1, 0]]
        self.assertEqual(self.ai.mahdolliset_sarakkeet(
            self.tiedot.matriisi), [0, 2, 3, 4, 6])
        
    def test_voittava_siirto(self):
        pelilauta=[[1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.ai.voittava_siirto(pelilauta, 1), True)
        pelilauta=[[2, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0], [
            2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.ai.voittava_siirto(pelilauta, 2), True)
        
    def test_siirto_kopio_laudalla(self):
        self.assertEqual(self.ai.siirto_kopio_laudalla(3, self.tiedot.matriisi, 1), [[0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

    def test_pelilaudan_pisteytys(self):
        pelilauta = [[2, 1, 1, 1, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.ai.pelilaudan_pisteytys(pelilauta), -8850)
        pelilauta = [[0, 2, 2, 2, 2, 0, 0], [0, 2, 0, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0, 0], [
            0, 0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.ai.pelilaudan_pisteytys(pelilauta), 10720)

    def test_minimax(self):
        pelilauta = [[2, 0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0, 0], [
            0, 0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.ai.minimax(2, True, -1000000, 10000000, pelilauta), (None, inf ))
        pelilauta = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [
            1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.ai.minimax(2, True, -1000000, 10000000, pelilauta), (None, -inf ))
        pelilauta = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 2, 1, 2,1, 2, 1]]
        self.assertEqual(self.ai.minimax(2, True, -1000000, 10000000, pelilauta), (None, 0 ))


