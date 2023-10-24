# Toteutusdokumentti

Ohjelman kulku sekvenssikaaviona:

```mermaid
sequenceDiagram
  participant main
  participant Tiedot
  participant Käyttöliittymä
  actor Pelaaja
  participant Connectfour
  participant Ai
  
  main ->>Tiedot:  
  Tiedot -->>main:   
  main ->>Käyttöliittymä: loop(Tiedot)
  Käyttöliittymä ->>Pelaaja: kysy sarake
  Pelaaja -->>Käyttöliittymä: valittu sarake
  Käyttöliittymä ->>Connectfour: vuoro(sarake)
  Connectfour ->>Tiedot: muokkaa pelilautaa
  Tiedot -->>Connectfour:   
  Connectfour ->>Käyttöliittymä:   
  Käyttöliittymä ->>Ai: valitse_paras_siirto()
  Ai -->>Käyttöliittymä: paras sarake
  Käyttöliittymä ->>Connectfour: vuoro(sarake)
  Connectfour ->>Tiedot: muokkaa pelilautaa
  Tiedot -->>Connectfour:    
  Connectfour ->>Käyttöliittymä:  
  Käyttöliittymä -->>main:  
```
Kaaviossa mallinnettu tilanne, jossa pelaajan vuoro on ensin. 




**Lähteet:**

https://en.wikipedia.org/wiki/Minimax 

https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/ 


Ei käytetty laajoja kielimalleja.
