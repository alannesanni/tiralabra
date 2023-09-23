import random
from entities.connectfour import ConnectFour
from copy import deepcopy

class Ai:
    """Tekoälystä vastaava luokka.

    Attributes:
            tiedot: Pelin tiedot
    """
    def __init__(self, tiedot):
        """Luokan konstruktori, joka alustaa käytettävät tiedot.
        """
        self.tiedot = tiedot

    def minimax(self):
        pass

    def valitse_paras_siirto(self):
        """Valitsee rivin, jolle on kannattavinta tehdä seuraava siirto. On vielä aika alussa, joten katsoo vain onko mahdollisuutta voittaa ja jos ei ole niin arpoo satunnaisen käyvän rivin. 

        Returns:
            Rivi, jolle on kannattavinta tehdä seuraava siirto. 
        """
        if self.tyhja_lauta():
            return 3
        else:
            mahdolliset_rivit = self.mahdolliset_rivit()
            for i in mahdolliset_rivit:
                if self.rivi_pisteytys(self.siirron_kokeilu_laudalla(i)) >= 100:
                    return i
            while True:
                rivi = random.randint(0, 5)
                if ConnectFour(self.tiedot).rivi_taynna(rivi) == False:
                    return rivi

    def tyhja_lauta(self):
        """Tarkistaa onko pelilauta tyhjä.

        Returns:
            True: pelilauta on tyhjä
            False: pelilauta ei ole tyhjä
        """
        for i in self.tiedot.matriisi:
            for j in i:
                if j != 0:
                    return False
        return True

    def siirron_kokeilu_laudalla(self, rivi):
        """Luo kopion pelilaudasta ja pelaa siihen syötetylle riville nappulan. 

        Args:
            rivi: Rivi, jolle nappula pelataan

        Returns:
            Kopio pelitilanteesta syötetyn rivin pelaamisen jälkeen. 
        """
        kokeilu_lauta = deepcopy(self.tiedot.matriisi)
        for i in range(0, 6):
            if kokeilu_lauta[i][rivi] == 0:
                kokeilu_lauta[i][rivi] = 2
                return kokeilu_lauta

    def rivi_pisteytys(self, lauta):
        """Laskee kuinka hyvä pelilauta on tekoälyn kannalta. Tällä hetkellä antaa laudalle pisteitä vain jos se on voittava siirto. 

        Args:
            lauta: Lauta joka pisteytetään 

        Returns:
            Laudan saamat pisteet
        """
        pisteet = 0
        # onko voittavaa siirtoa?
        # vaakasuorassa
        for i in range(6):
            for j in range(4):
                if lauta[i][j] == lauta[i][j+1] == lauta[i][j+2] == lauta[i][j+3] == 2:
                    pisteet += 100

        # vaakatasossa
        for i in range(6):
            for j in range(4):
                if lauta[i][j] == lauta[i][j+1] == lauta[i][j+2] == lauta[i][j+3] == 2:
                    pisteet += 100

        # vinossa alas
        for i in range(3):
            for j in range(4):
                if lauta[i][j] == lauta[i+1][j+1] == lauta[i+2][j+2] == lauta[i+3][j+3] == 2:
                    pisteet += 100

        # vinossa ylös
        for i in range(3, 6):
            for j in range(0, 4):
                if lauta[i][j] == lauta[i-1][j+1] == lauta[i-2][j+2] == lauta[i-3][j+3] == 2:
                    pisteet += 100

        return pisteet

    def mahdolliset_rivit(self):
        """Tarkistaa mille riveille on mahdollista pelata seuraava nappula.

        Returns:
            Listana rivit, jotka eivät ole täysiä.
        """
        rivit = []
        for i in range(7):
            if self.tiedot.matriisi[5][i] == 0:
                rivit.append(i)
        return rivit
