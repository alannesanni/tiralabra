# Käyttöohjeet

1. Lataa githubista viimeisin release

2. Asenna riippuvuudet komennolla `poetry install`

3. Käynnistä peli komennolla `poetry run invoke start`


- Siirrä hiiren avulla nappula haluamasi sarakkeen kohdalle ja aseta nappula sarakkeelle painamalla hiiren vasenta painiketta

- Voittaja on se joka saa ensin nejän nappulan suoran joko pystysuorassa, vaakasuorassa tai vinottain

- Uuden pelin voi aloittaa painamalla enter


Testit voidaan suorittaa komennolla `poetry run invoke test`

Testikattavuusraportin saa komennolla `poetry run invoke coverage-report`

Koodin laatutarkastuksen voi tehdä komennolla `poetry run invoke lint`