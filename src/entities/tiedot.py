from random import randint
class Tiedot:
    def __init__(self):
        self.matriisi=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        self.pelaaja=randint(1,2)

    def vaihda_pelaaja(self):
        if self.pelaaja==1:
            self.pelaaja=2
        else:
            self.pelaaja=1