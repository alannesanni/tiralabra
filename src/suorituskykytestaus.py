from entities.tiedot import Tiedot
from ai import Ai
from time import time
def suorituskyky(syvyys, lauta):
    tiedot=Tiedot()
    ai=Ai(tiedot)
    tiedot.matriisi=lauta
    alku=time()
    palautus=ai.valitse_paras_siirto()
    loppu=time()
    return loppu-alku

if __name__=="__main__":
    print("Vapaita sarakkeita 7:", suorituskyky(6, [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]))
    print("Vapaita sarakkeita 6:", suorituskyky(6, [[1, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [
            1, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0]]))
    print("Vapaita sarakkeita 5:", suorituskyky(6, [[1, 2, 0, 0, 0, 0, 0], [2, 1, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0], [
            1, 2, 0, 0, 0, 0, 0], [2, 1, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0]]))
    print("Vapaita sarakkeita 4:", suorituskyky(6, [[1, 2, 1, 0, 0, 0, 0], [2, 1, 2, 0, 0, 0, 0], [1, 2, 1, 0, 0, 0, 0], [
            1, 2, 1, 0, 0, 0, 0], [2, 1, 2, 0, 0, 0, 0], [1, 2, 1, 0, 0, 0, 0]]))
    print("Vapaita sarakkeita 3:", suorituskyky(6, [[1, 2, 1, 2, 0, 0, 0], [2, 1, 2, 1, 0, 0, 0], [1, 2, 1, 2, 0, 0, 0], [
            1, 2, 1, 2, 0, 0, 0], [2, 1, 2, 1, 0, 0, 0], [2, 1, 2, 1, 0, 0, 0]]))
    print("Vapaita sarakkeita 2:", suorituskyky(6, [[1, 2, 1, 2, 2, 0, 0], [2, 1, 2, 1, 1, 0, 0], [1, 2, 1, 2, 1, 0, 0], [
            1, 2, 1, 2, 1, 0, 0], [2, 1, 2, 1, 2, 0, 0], [2, 1, 2, 1, 1, 0, 0]]))
    print("Vapaita sarakkeita 1:", suorituskyky(6, [[1, 2, 1, 2, 2, 1, 0], [2, 1, 2, 1, 1, 2, 0], [1, 2, 1, 2, 1, 2, 0], [
            1, 2, 1, 2, 2, 1, 0], [2, 1, 2, 1, 2, 1, 0], [2, 1, 2, 1, 1, 2, 0]]))


