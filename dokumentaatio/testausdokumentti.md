# Testausdokumentti
Pelin luokkia on testattu unittesteillä. Testit löytyvät kansiosta src/tests

Testit voidaan suorittaa komennolla `poetry run invoke test`

Testikattavuusraportin saa komennolla `poetry run invoke coverage-report`


Testikattavuusraportti:

![image](https://github.com/alannesanni/tiralabra/assets/128046458/45b6b43f-3411-41f8-a2bc-9deb96462a74)


Kaikki pelilogiikan ja tekoälyn funktiot on testattu mahdollisimman tarkasti yksikkötesteillä. 

Minimax algoritmia on testattu muutamalla erilaisella pelitilanteella, joissa tekoälyn on mahdollista voittaa 6 siirrolla (3 omalla siirrolla). Olen etsinty tälläiset pelitilanteet connect four solverin avulla. 

Pisteytys funktiota on testattu antamalla funkiolle kuvitteellisia satunnaisia pelitilanteita. Olen testien yhteydessä laskenut oikeiden pisteiden määrän, jotta voidaan varmistua tuloksen oikeellisuudesta.
