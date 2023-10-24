# Testausdokumentti
Pelin luokkia on testattu unittesteillä. Testit löytyvät kansiosta src/tests

Testit voidaan suorittaa komennolla `poetry run invoke test`

Testikattavuusraportin saa komennolla `poetry run invoke coverage-report`


Testikattavuusraportti:

![image](https://github.com/alannesanni/tiralabra/assets/128046458/bc574fa2-e6a6-440f-80e9-f5a3bf292430)

Kaikki pelilogiikan ja tekoälyn funktiot on testattu mahdollisimman tarkasti yksikkötesteillä. 

Minimax algoritmia on testattu muutamalla erilaisella pelitilanteella, joissa tekoälyn on mahdollista voittaa 6 siirrolla (3 omalla siirrolla). Olen etsinty tälläiset pelitilanteet connect four solverin avulla. 

Pisteytys funktiota on testattu antamalla funkiolle kuvitteellisia satunnaisia pelitilanteita. Olen testien yhteydessä laskenut oikeiden pisteiden määrän, jotta on helpompi varmistua tuloksen oikeellisuudesta.
