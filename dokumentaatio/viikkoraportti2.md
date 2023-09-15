# Viikko 2
Aloitin pelin luomisen luomalla pelin toimivaksi ensin tekstikäyttöliittymällä ja sitten lisäsin graafisen käyttöliittymän. Peli on nyt pelattava kahden ihmispelaajan välillä ja tullistaa kaikki voitot ja tasapelin.

Loin testit unittestin avulla ConnectFour ja Tiedot luokille. Lisäsin koodiin docstring-dokumentoinnin.

Loin invoke komennot, joiden avulla pelin voi aloittaa (poetry run invoke start), testata (poetry run invoke test) ja luoda testikattavuusraportin (poetry run invoke coverage-report).

Otin käyttöön pylintin, joka tarkistaa koodin laatua, pylint-tarkistuksen voi suorittaa komennolla "poetry run invoke lint".

Ensi viikolla luon peliin komennon, jolla pelin saa aloitettua uudelleen ja alan kehittämään tekoälyä, jota vastaan pelataan.

Työaika: 10h

Onko graafisesta käyttöliittymästä vastaava luokka myös testattava automaattisilla testeillä?

