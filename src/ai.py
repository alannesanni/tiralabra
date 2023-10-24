from math import inf
from entities.connectfour import ConnectFour
from entities.tiedot import Tiedot
from copy import deepcopy
MIN = -inf
MAX = inf
VUOROT = 6


class Ai:
    """Tekoälystä vastaava luokka.

    Attributes:
            tiedot: Pelin tiedot
    """

    def __init__(self, tiedot):
        """Luokan konstruktori, joka alustaa käytettävät tiedot.
        """
        self.tiedot = tiedot

    def valitse_paras_siirto(self):
        """Funktio, jota kutsutaan Ui luokan loop-funktiossa.

        Returns:
            Sarake, johon on paras tehdä seuraava siirto.
        """

        for i in self.mahdolliset_sarakkeet(self.tiedot.matriisi):
            kopiopelilauta1 = deepcopy(self.tiedot.matriisi)
            self.siirto_kopio_laudalla(i, kopiopelilauta1, 2)
            if self.voittava_siirto(kopiopelilauta1, 2):
                return i

        kopiopelilauta = deepcopy(self.tiedot.matriisi)
        return self.minimax(VUOROT, True, MIN, MAX, kopiopelilauta)[0]

    def minimax(self, syvyys, maxPelaaja, alpha, beta, lauta):
        """Minimax-algoritmi alfa-beta karsinnalla.

        Args:
            syvyys: Kierrokset, kuinka pitkälle eteenpäin vuoroja lasketaan
            maxPelaaja: Kertoo kumman vuoro on, jos True niin on tekoälyn vuoro, jos False niin ihmispelaajan vuoro
            alpha: Laudan pisteytyksen suurin löydetty arvo
            beta: Laudan pisteytyksen pienin löydetty arvo
            lauta: pelilauta

        Returns:
            Sarake (johon on paras laittaa seuraava nappula), pisteet (laudan saamat pisteet jos laitetaan nappula parhaaseen sarakkeeseen)
        """
        mahd_sarakkeet = self.mahdolliset_sarakkeet(lauta)
        if self.voittava_siirto(lauta, 2):
            return None, MAX
        elif self.voittava_siirto(lauta, 1):
            return None, MIN
        elif self.lauta_taynna(lauta):
            return None, 0
        elif syvyys == 0:
            return None, self.pelilaudan_pisteytys(lauta)

        if maxPelaaja:
            paras = MIN
            sarake = self.mahdolliset_sarakkeet(lauta)[0]
            for i in mahd_sarakkeet:
                kopio_lauta = deepcopy(lauta)
                kopio_lauta = self.siirto_kopio_laudalla(i, kopio_lauta, 2)
                arvo = self.minimax(syvyys - 1, False,
                                    alpha, beta, kopio_lauta)[1]
                if arvo > paras:
                    paras = arvo
                    sarake = i
                alpha = max(alpha, paras)
                if beta <= alpha:
                    break
            return sarake, paras
        else:
            paras = MAX
            sarake = self.mahdolliset_sarakkeet(lauta)[0]
            for i in mahd_sarakkeet:
                kopio_lauta = deepcopy(lauta)
                kopio_lauta = self.siirto_kopio_laudalla(i, kopio_lauta, 1)
                arvo = self.minimax(syvyys - 1, True, alpha,
                                    beta, kopio_lauta)[1]
                if arvo < paras:
                    paras = arvo
                    sarake = i
                beta = min(beta, paras)

                if beta <= alpha:
                    break
            return sarake, paras

    def lauta_taynna(self, lauta):
        """Tarkistaa onko pelilauta täynnä.

        Args:
            lauta: pelilauta, joka tarkistetaan

        Returns:
            True: pelilauta on täynnä
            False: pelilauta ei ole täynnä
        """
        for i in lauta[5]:
            if i == 0:
                return False
        return True

    def voittava_siirto(self, lauta, pelaaja):
        """Tarkistaa onko annettu pelaaja voittanut annetulla pelilaudalla.

        Args:
            lauta: pelilauta
            pelaaja: pelaaja, jonka voitto tarkastetaan

        Returns:
            True: pelaajalla on 4 suora
            False: pelaajalla ei ole 4 suoraa
        """
        # pystysuorassa
        for i in range(3):
            for j in range(7):
                if lauta[i][j] == lauta[i+1][j] == lauta[i+2][j] == lauta[i+3][j] == pelaaja:
                    return True

        # vaakatasossa
        for i in range(6):
            for j in range(4):
                if lauta[i][j] == lauta[i][j+1] == lauta[i][j+2] == lauta[i][j+3] == pelaaja:
                    return True

        # vinossa alas
        for i in range(3):
            for j in range(4):
                if lauta[i][j] == lauta[i+1][j+1] == lauta[i+2][j+2] == lauta[i+3][j+3] == pelaaja:
                    return True

        # vinossa ylös
        for i in range(3, 6):
            for j in range(0, 4):
                if lauta[i][j] == lauta[i-1][j+1] == lauta[i-2][j+2] == lauta[i-3][j+3] == pelaaja:
                    return True
        return False

    def siirto_kopio_laudalla(self, sarake, lauta, pelaaja):
        """Pelaa annetulla laudalla (joka on kopio alkuperäisestä laudasta) annettuun sarakkeeseen annetun pelaajan nappulan. 

        Args:
            sarake: Sarake, johon nappula pelataan

        Returns:
            Pelilaudan tilanne annetun siirron jälkeen
        """
        for rivi in range(6):
            if lauta[rivi][sarake] == 0:
                lauta[rivi][sarake] = pelaaja
                return lauta

    def pelilaudan_pisteytys(self, lauta):
        """Laskee kuinka hyvä pelilauta on tekoälyn kannalta.

        Args:
            lauta: Pelilauta joka pisteytetään 

        Returns:
            Pelilaudan saamat pisteet
        """
        pisteet = 0
        # pisteet keskeltä
        nappulat = []
        for rivi in lauta:
            nappulat.append(rivi[3])
        kerroin = nappulat.count(2)
        pisteet += 10*kerroin
       
        # 3 omaa ja sivuilla 2 tyhjää
        # vaakatasossa
        for i in range(6):
            for j in range(1, 4):
                if lauta[i][j] == lauta[i][j+1] == lauta[i][j+2]  == 2:
                    if lauta[i][j-1] == lauta[i][j+3] == 0:
                        pisteet += 100
        # vinossa alas
        for i in range(1, 3):
            for j in range(1, 4):
                nappulat = [lauta[i][j], lauta[i+1][j+1], lauta[i+2][j+2]]
                if nappulat.count(2) == 3:
                    if lauta[i-1][j-1] == lauta[i+3][j+3] == 0:
                        pisteet += 100
        # vinossa ylös
        for i in range(3, 5):
            for j in range(1, 4):
                nappulat = [lauta[i][j], lauta[i-1][j+1], lauta[i-2][j+2]]
                if nappulat.count(2) == 3:
                    if lauta[i+1][j-1] == lauta[i-3][j+3] == 0:
                        pisteet += 100
        
        # 3 omaa ja 1 tyhjä
        # pystysuorassa
        for i in range(3):
            for j in range(7):
                nappulat = [lauta[i][j], lauta[i+1][j], lauta[i+2][j]]
                if nappulat.count(2) == 3 and lauta[i+3][j] == 0:
                    pisteet += 50

        # vaakatasossa
        for i in range(6):
            for j in range(4):
                nappulat = [lauta[i][j], lauta[i][j+1],
                            lauta[i][j+2], lauta[i][j+3]]
                if nappulat.count(2) == 3 and nappulat.count(1) == 0:
                    pisteet += 50

        # vinossa alas
        for i in range(3):
            for j in range(4):
                nappulat = [lauta[i][j], lauta[i+1][j+1],
                            lauta[i+2][j+2], lauta[i+3][j+3]]
                if nappulat.count(2) == 3 and nappulat.count(1) == 0:
                    pisteet += 50

        # vinossa ylös
        for i in range(3, 6):
            for j in range(4):
                nappulat = [lauta[i][j], lauta[i-1][j+1],
                            lauta[i-2][j+2], lauta[i-3][j+3]]
                if nappulat.count(2) == 3 and nappulat.count(1) == 0:
                    pisteet += 50
        
        # 3 vastustajan ja 0 tai 1 oma
        for i in range(3):
            for j in range(7):
                nappulat = [lauta[i][j], lauta[i+1][j], lauta[i+2][j]]
                if nappulat.count(1) == 3 and lauta[i+3][j] == 0:
                    pisteet -= 15
                elif nappulat.count(1) == 3 and lauta[i+3][j] == 2:
                    pisteet += 30
        # vaakatasossa
        for i in range(6):
            for j in range(4):
                nappulat = [lauta[i][j], lauta[i][j+1],
                            lauta[i][j+2], lauta[i][j+3]]
                if nappulat.count(1) == 3 and nappulat.count(2) == 0:
                    pisteet -= 15
                elif nappulat.count(1) == 3 and nappulat.count(2) == 1:
                    pisteet += 30

        # vinossa alas
        for i in range(3):
            for j in range(4):
                nappulat = [lauta[i][j], lauta[i+1][j+1],
                            lauta[i+2][j+2], lauta[i+3][j+3]]
                if nappulat.count(1) == 3 and nappulat.count(2) == 0:
                    pisteet -= 15
                elif nappulat.count(1) == 3 and nappulat.count(2) == 1:
                    pisteet += 30

        # vinossa ylös
        for i in range(3, 6):
            for j in range(0, 4):
                nappulat = [lauta[i][j], lauta[i-1][j+1],
                            lauta[i-2][j+2], lauta[i-3][j+3]]
                if nappulat.count(1) == 3 and nappulat.count(2) == 0:
                    pisteet -= 15
                elif nappulat.count(1) == 3 and nappulat.count(2) == 1:
                    pisteet += 30
       
        return pisteet

    def mahdolliset_sarakkeet(self, lauta):
        """Tarkistaa mille sarakkeille on mahdollista pelata seuraava nappula.

        Returns:
            Listana sarakkeet, jotka eivät ole täysiä.
        """
        sarakkeet = []
        for i in [3, 2, 4, 1, 5, 0, 6]:
            if lauta[5][i] == 0:
                sarakkeet.append(i)
        return sarakkeet
