# Katselmointi 

## Mitä huomioita Copilot teki koodistasi
Copilot huomasi koodissani yhden virheellisen tyyppipalautuksen ja korjasi sen. Se myös lisäsi puuttuvia tyyppimäärittelyjä muihin kohtiin.
Lisäksi Copilot esitti korjausehdotuksen enumeraation käytöstä: sen mukaan testini olisi voinut rikkoutua, koska käytin `Enum.ARVO` suoraan stringin sijaan `Enum.ARVO.value`. Copilotin mukaan vertailu olisi tällöin ollut muotoa:

```` 
olio == string
```` 

mikä ei voi koskaan olla totta.

Omassa testissäni vertailu ei kuitenkaan hajonnut, koska testit käyttivät suoraan string-arvoja ja logiikka sattui toimimaan niissä tapauksissa. Silti huomio enum.value:n käytöstä oli hyvä, koska se ehkäisee tällaiset vertailuongelmat.

## Olivatko ehdotetut muutokset hyviä
Erityisesti enumeraation arvon löydös oli hyvä. Muut muutokset olisi voinut löytää esim. pylintin ja/tai mypyn avulla. 

## Kuinka hyödylliseksi koit Copilotin tekemän katselmoinnin

Katselmointi oli kätevä, koska se tapahtui automaattisesti. Varsinaisia refaktorointeja copilot ei antanut jo reafktoroituun koodiini. 