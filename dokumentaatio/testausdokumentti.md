# Testausdokumentti
Pelin luokkia on testattu unittesteillä. Testit löytyvät kansiosta src/tests

Testit voidaan suorittaa komennolla `poetry run invoke test`

Testikattavuusraportin saa komennolla `poetry run invoke coverage-report`


Testikattavuusraportti:

![image](https://github.com/alannesanni/tiralabra/assets/128046458/bc574fa2-e6a6-440f-80e9-f5a3bf292430)






### Suorituskyky
Suorituskyky-funktio mittaa, kuinka kauan minimaxin suoritus kestää riippuen siitä kuinka moneen sarakkeeseen voidaan laittaa nappula. 

![image](https://github.com/alannesanni/tiralabra/assets/128046458/7875ae8a-ce9e-4b1b-a79f-fbc83ba14792)
![image](https://github.com/alannesanni/tiralabra/assets/128046458/2dbc647c-5909-4f43-a57d-98883d07dbcd)

Tulosten avulla muodostetusta kaaviosta nähdään, että aika suurenee lähes eksponenttiaalisesti, kun vapaiden sarakkeiden määrä lisääntyy. 

