from entities.tiedot import Tiedot
from ui import Kayttoliittyma


def main():
    tiedot = Tiedot()
    ui = Kayttoliittyma(tiedot)
    ui.loop()


if __name__ == "__main__":
    main()
