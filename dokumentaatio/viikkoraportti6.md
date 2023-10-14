# Viikkoraportti 6
Korjasin koodista bugin, joka antoi pelaajan laittaa nappulan täydelle riville, jolloin tekoäly sai ylimääräisen vuoron. 
Paransin pisteytys funktiota kokeilemalla erilaisia arvoja eri tilanteille. Nyt toimii aika hyvin. Poistin kokonaan pisteytyksistä kohdan, jossa on 2 omaa ja 2 tyhjää kun sen pisteyttäminen eri tilanteissa tuntui vääristävän laudan lopullista pisteytystä. Muutin mahdolliset_sarakkeet() funktiota niin, että nyt sarakkeet lisätään sen palauttamaan listaan niin, että sisemmät sarakkeet lisätään ensin. 

Kirjoitin lisää testejä ja korjasin vanhoja testejä.

Paransin koodin laatua lint ohjeiden avulla parhaani mukaan. 

Seuraavaksi koitan vielä saada tekoälyä pelaamaan vieläkin paremmin. Nyt se "luovuttaa" lopussa jos ei ole mahdollista voittaa, vaikka sen pitäisi tähdätä tasapeliin.

työaika: 10h