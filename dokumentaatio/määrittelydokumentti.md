## Määrittelydokumentti
Ohjelmointikieli: python

Muut osatut ohjelmointikielet: ei ole

Dokumentaatiokieli: suomi

Opinto-ohjelma: tietojenkäsittelytieteen kandidaatti

Teen connect four-pelin jota pelataan tekoälyä vastaan. Peliä pelataan 7x6 ruudukolla ja kumpikin pelaaja laittaa vuorollaan oman värisensä nappulan laudalle. Voittaja on se, joka saa ensin nejän nappulan suoran joko pystysuorassa, vaakasuorassa tai vinottain. Teen pelin graafisen käyttöliittymän pygamen avulla. Ohjelma saa pelaajalta hiiren avulla syötteen siitä, mihin seuraava nappula sijoitetaan. 

Toteutan tekoälyn minimax-algoritmin avulla, jota on tehosteetu alpha-beta-karsinnalla. Minimaxin avulla tekoäly valitsee parhaan mahdollisen siirron. Valitsin minimaxin, koska se sopii parhaiten valitsemaan parhaan siirron laudalta. Minimaxin aikavaativuus on O(b^m) ja tilavaatimus O(bm), missä b on mahdollisten siirtojen määrä ja m on puun suurin syvyys.


