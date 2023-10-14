
class ConnectFour:
    """Luokka, jossa on pelin oleelliste funktiot.

    Attributes:
            tiedot: Pelin tiedot
    """

    def __init__(self, tiedot):
        """Luokan konstruktori, joka luo uuden pelin.

        Args:
            tiedot: Pelin tiedot
            pelilauta: Käytettävä pelilauta
            pelaaja= Vuorossa oleva pelaaja
        """
        self.tiedot = tiedot
        #self.tiedot.matriisi = self.tiedot.matriisi
        self.pelaaja = self.tiedot.pelaaja

    def vuoro(self, sarake):
        """Kokeilee onko haluttu siirto mahdollinen, jos on niin asettaa nappulan alimmalle mahdolliselle riville ja kertoo voittiko pelaaja siirrolla tai tuliko tasapeli.

        Args:
            sarake: Sarake, jolle pelaaja haluaa asettaa nappulan

        Returns:
            Kertoo onnistuiko siirto, epäonnistuiko siirto, tuliko tasapeli tai voittiko pelaaja siirrolla
        """
        sarake_taynna = self.sarake_taynna(sarake)
        if sarake_taynna:
            return "siirto epaonnistui"

        for i in range(0, 6):
            if self.tiedot.matriisi[i][sarake] == 0:
                self.tiedot.matriisi[i][sarake] = self.tiedot.pelaaja
                break
        if self.voittava_siirto():
            return "voittava siirto"
        if self.lauta_taynna():
            return "lauta taynna"
        return "siirto onnistui"

    def sarake_taynna(self, sarake):
        """Tarkistaako onko annettu sarake täynnä.

        Args:
            sarake: Tarkistettava sarake

        Returns:
            True: sarake on täynnä
            False: sarake ei ole täynnä
        """
        if self.tiedot.matriisi[5][sarake] != 0:
            return True
        return False

    def voittava_siirto(self):
        """Tarkistaa onko pelilaudalla voittavaa suoraa.

        Returns:
            True: voittava suora löytyi
            False: ei voittavaa suoraa
        """
        # pystyssä
        for i in range(3):
            for j in range(7):
                if self.tiedot.matriisi[i][j] == self.tiedot.matriisi[i+1][j] == self.tiedot.matriisi[i+2][j] == self.tiedot.matriisi[i+3][j] != 0:
                    return True
        # vaakatasossa
        for i in range(6):
            for j in range(4):
                if self.tiedot.matriisi[i][j] == self.tiedot.matriisi[i][j+1] == self.tiedot.matriisi[i][j+2] == self.tiedot.matriisi[i][j+3] != 0:
                    return True

        # vinossa alas
        for i in range(3):
            for j in range(4):
                if self.tiedot.matriisi[i][j] == self.tiedot.matriisi[i+1][j+1] == self.tiedot.matriisi[i+2][j+2] == self.tiedot.matriisi[i+3][j+3] != 0:
                    return True

        # vinossa ylös
        for i in range(3, 6):
            for j in range(0, 4):
                if self.tiedot.matriisi[i][j] == self.tiedot.matriisi[i-1][j+1] == self.tiedot.matriisi[i-2][j+2] == self.tiedot.matriisi[i-3][j+3] != 0:
                    return True
        return False

    def lauta_taynna(self):
        """Tarkistaa onko pelilauta täynnä.

        Returns:
            True: lauta on täynnä
            False: lauta ei ole täynnä
        """
        for i in self.tiedot.matriisi:
            for j in i:
                if j == 0:
                    return False
        return True
