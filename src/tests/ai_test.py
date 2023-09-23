import unittest
from entities.tiedot import Tiedot
from ai import Ai


class TestConnectFour(unittest.TestCase):
    def setUp(self):
        self.tiedot = Tiedot()
        self.ai = Ai(self.tiedot)

    def test_mahdolliset_rivit(self):
         self.assertEqual(self.ai.mahdolliset_rivit(), [0,1, 2, 3, 4, 5, 6])
         self.tiedot.matriisi=[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 1, 0]]
         self.assertEqual(self.ai.mahdolliset_rivit(), [0, 2, 3, 4, 6])

    def test_siirron_kokeilu_laudalla(self):
        self.assertEqual(self.ai.siirron_kokeilu_laudalla(3), [[0, 0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

    def test_tyhja_lauta(self):
        self.assertEqual(self.ai.tyhja_lauta(), True)
        self.tiedot.matriisi=[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 1, 0]]
        self.assertEqual(self.ai.tyhja_lauta(), False)