from random import randint


class Tiedot:
    """Luokka, jonka avulla ylläpidetään käynnissä olevan pelin tietoja.
    """

    def __init__(self):
        """Luokan konstruktori, joka luo uuden pelin ja alustaa sen tiedot.

        Args:
            matriisi: pelilauta
            pelaaja: vuorossa oleva pelaaja
        """
        self.matriisi = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.pelaaja = randint(1, 2)

    def vaihda_pelaaja(self):
        """Vaihtaa pelaajan.
        """
        if self.pelaaja == 1:
            self.pelaaja = 2
        else:
            self.pelaaja = 1
