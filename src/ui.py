import sys
import pygame
from entities.tiedot import Tiedot
from entities.connectfour import ConnectFour
from ai import Ai

MUSTA = (0, 0, 0)
SININEN = (0, 0, 255)
PUNAINEN = (255, 0, 0)
KELTAINEN = (255, 255, 0)


class Kayttoliittyma:
    """Luokka, joka vastaa pelin käyttöliittymästä ja pelilogiikasta.

        Attributes:
            tiedot: Pelin tiedot
    """

    def __init__(self, tiedot):
        """Luokan konstruktori, joka luo pelin pohjan.

        """
        pygame.init()
        self.tiedot = tiedot
        self.leveys = 700
        self.korkeus = 700
        self.pelilauta = tiedot.matriisi
        self.peli = ConnectFour(self.tiedot)
        self.naytto = pygame.display.set_mode((self.leveys, self.korkeus))
        self.pelaaja = tiedot.pelaaja
        self.pelin_tila = "normaali"
        self.palautus = ""
        pygame.display.set_caption("ConnectFour")

    def loop(self):
        """Pelilogiikasta vastaava funktio, joka kutsuu eri funktioita riippuen pelin tilasta. Jos tila on normaali, tarkistaa kumman pelaajan vuoro on. Jos on ihmispelaajan vuoro, niin kutsuu tapahtumat funktiota ja jos on tietokoneen vuoro niin kutsuu Ai luokkaa ja sen parhaan rivin etsivää funktiota.
        """
        kello = pygame.time.Clock()
        while True:
            if self.pelin_tila == "normaali":
                self.piirra_naytto()
                if self.tiedot.pelaaja == 1:
                    self.tapahtumat()
                else:
                    rivi = Ai(self.tiedot).valitse_paras_siirto()
                    self.palautus = self.peli.vuoro(rivi)
                    self.paivita_pelin_tila()
                    if self.pelin_tila == "normaali":
                        self.tiedot.vaihda_pelaaja()
            if self.pelin_tila == "gameover":
                self.piirra_naytto()
                self.tasapeli()
                self.tapahtumat()
            if self.pelin_tila == "voitto":
                self.piirra_naytto()
                self.voitto()
                self.tapahtumat()
            pygame.display.flip()

            kello.tick(30)

    def tapahtumat(self):
        """Tarkistaa käyttäjältä tulevat syötteet ja toimii niiden mukaan. Jos halutaan asettaa uusi nappula funktio kutsuu ConnectFour-luokan vuoro-funktiota, jolloin pelilaudan tila päivittyy. Jos siirto onnistuu vaihdetaan lopussa vuoro toiselle pelaajalle.
        """
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                sys.exit()

            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_RETURN:
                    self.tiedot.matriisi = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
                        0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
                    self.pelin_tila = "normaali"

            if tapahtuma.type == pygame.MOUSEBUTTONDOWN and self.pelin_tila == "normaali":
                hiiri = pygame.mouse.get_pos()
                rivi = (hiiri[0]//100)
                self.palautus = self.peli.vuoro(rivi)
                self.paivita_pelin_tila()
                if self.pelin_tila == "normaali":
                    self.tiedot.vaihda_pelaaja()

    def paivita_pelin_tila(self):
        """Muuttaa pelin tilaa, riippuen mitä on saatu palautuksena ConnectFour luokan vuoro-funktiolta.
        """
        if self.palautus == "lauta taynna":
            self.pelin_tila = "gameover"
        elif self.palautus == "voittava siirto":
            self.pelin_tila = "voitto"

    def seuraava_nappula(self):
        """Piirtää yläriville seuraavan asetettavan nappulan, väri riippuu siitä kumman pelaajan vuoro on.
        """
        hiiri = pygame.mouse.get_pos()
        nappulan_x_koordinaatti = (hiiri[0]//100)*100+50
        if self.tiedot.pelaaja == 1:
            pygame.draw.circle(self.naytto, PUNAINEN,
                               (nappulan_x_koordinaatti, 50), 49)
        if self.tiedot.pelaaja == 2:
            pygame.draw.circle(self.naytto, KELTAINEN,
                               (nappulan_x_koordinaatti, 50), 49)

    def piirra_naytto(self):
        """Piirtää peliruudun, siihen jo asetetut nappulat ja seuraavan asetettavan nappulan.
        """
        sarake = 0
        self.naytto.fill(SININEN)
        for i in range(50, 750, 100):
            rivi = 0
            for j in range(650, 50, -100):
                if self.tiedot.matriisi[rivi][sarake] == 0:
                    vari = MUSTA
                if self.tiedot.matriisi[rivi][sarake] == 1:
                    vari = PUNAINEN
                if self.tiedot.matriisi[rivi][sarake] == 2:
                    vari = KELTAINEN
                pygame.draw.circle(self.naytto, vari, (i, j), 49)
                rivi += 1
            sarake += 1
        self.seuraava_nappula()

    def voitto(self):
        """Piirtää näytölle voitto-tekstin.
        """
        fontti = pygame.font.SysFont("arial", 40)
        if self.tiedot.pelaaja == 1:
            vari = "PUNAINEN"
        else:
            vari = "KELTAINEN"
        voitto = fontti.render(
            f"{vari} PELAAJA VOITTI!", 0, MUSTA)
        voitto_leveys = voitto.get_width()
        self.naytto.blit(voitto, (((self.leveys//2)-voitto_leveys//2), 20))

    def tasapeli(self):
        """Piirtää näytölle tasapeli-tekstin.
        """
        fontti = pygame.font.SysFont("arial", 60)
        tasapeli = fontti.render("TASAPELI!", 0, MUSTA)
        tasapeli_leveys = tasapeli.get_width()
        self.naytto.blit(tasapeli, (((self.leveys//2)-tasapeli_leveys//2), 20))
