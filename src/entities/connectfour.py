
class ConnectFour:
    def __init__(self,tiedot):
        self.tiedot=tiedot
        self.pelilauta=self.tiedot.matriisi
        self.pelaaja=self.tiedot.pelaaja
        self.gameover=False

    def pelaaja_1_vuoro(self):
        rivi=int(input("pelaaja 1 syötä rivi:"))
        if self.rivi_taynna(rivi):
            rivi=int(input("pelaaja 1 syötä uusi rivi:"))
        for i in range(0,6):
            if self.pelilauta[i][rivi]==0:
                self.pelilauta[i][rivi]=1
                break

    def pelaaja_2_vuoro(self):
        rivi=int(input("pelaaja 2 syötä rivi:"))
        if self.rivi_taynna(rivi):
            rivi=int(input("pelaaja 2 syötä uusi rivi:"))
        for i in range(0,6):
            if self.pelilauta[i][rivi]==0:
                self.pelilauta[i][rivi]=2
                break

    def vuoro(self,rivi):
        rivi_taynna=self.rivi_taynna(rivi)
        if rivi_taynna:
            return "siirto epaonnistui"
        else:
            for i in range(0,6):
                if self.pelilauta[i][rivi]==0:
                    self.pelilauta[i][rivi]=self.tiedot.pelaaja
                    break
            if self.voittava_siirto():
                return "voittava siirto"
            if self.lauta_taynna():
                return "lauta taynna"
            return "siiro onnistui"
            


    def rivi_taynna(self,rivi):
        if self.pelilauta[5][rivi]!=0:
            return True
        return False
    
    def voittava_siirto(self):
        #pystyssä
        for i in range(3):
            for j in range(7):
                if self.pelilauta[i][j]==self.pelilauta[i+1][j]==self.pelilauta[i+2][j]==self.pelilauta[i+3][j]!=0:
                    return True
        #vaakatasossa
        for i in range(6):
            for j in range(4):
                if self.pelilauta[i][j]==self.pelilauta[i][j+1]==self.pelilauta[i][j+2]==self.pelilauta[i][j+3]!=0:
                    return True

        #vinossa alas
        for i in range(3):
            for j in range(4):
                if self.pelilauta[i][j]==self.pelilauta[i+1][j+1]==self.pelilauta[i+2][j+2]==self.pelilauta[i+3][j+3]!=0:
                    return True

        #vinossa ylös
        for i in range(3,6):
            for j in range(0,4):
                if self.pelilauta[i][j]==self.pelilauta[i-1][j+1]==self.pelilauta[i-2][j+2]==self.pelilauta[i-3][j+3]!=0:
                    return True
        return False
    
    def lauta_taynna(self):
        for i in self.pelilauta:
            for j in i:
                if j==0:
                    return False
        return True

    