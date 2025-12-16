# Raportti

## Päätyikö agentti toimivaan ratkaisuun?
Syötin agentille promptin: 

```
Build a web UI for my application. This is a poetry project. Do not touch my current code unless it is absolutely necessary. Reuse existing code as much as possible.
When you are done, start the UI.
```
Ensimmäinen iteraatio copilotin kanssa onnistui hyvin. Käyttöliitymä toimi odotetulla tavalla. Se olisi voinut olla yksinkertaisempi ja kauniimpi, mutta käytettävyys oli lopulta melko intuitiivista.  

## Kuinka paljon jouduit antamaan agentille komentoja matkan varrella?
Agentin käyttö ei ole täysin automaattista, jotta voisi vain tehdä jotain muuta järkevää sillä aikaa, kun se generoi koodia. Agetti pyysi noin 2 minuutin välein sallimaan uuden koodin suorittamista, koska muutokset ovat potentiaalisesti vaarallisia tai voivat rikkoa asioita. 2 minuutissa ei oikein ehdi aloittamaan mitään järkevää, joten katselin kissavideoita ja join kahvia. Käyttöliittymän generoimiseen kului omalla koti-Windowsillani noin 15 minuuttia, koska välillä unohduin katsomaan erityisen vangitsevaa kissavideota ja copilot oli jäänyt odottamaan hyväksyntääni. 
Edellämainitut komennot olivat muotoa hyväksy tai jatka. 

Seuraavaksi pyysin agenttia tekemään sovellukselle automatisoidut testit. Yksikkötestejä generointiin runsaat määrät. 4 ei kuitenkaan mennyt ensimmäisellä yrittämällä läpi. Toisella yrityksellä korjailun jälkeen 43 testiä meni läpi. Seuraavaksi pyysin agenttia muuttamaan sovellusta (ja testejä) siten, että jokaista peliä pelataan niin kauan kunnes toinen osapuoli on saavuttanut viisi voittoa. Muutosten jälkeen testit menivät taas rikki. Tälläkin kertaa testejä rikkoutui 4 kpl. Copilotilla oli erityisen paljon hankaluuksia AI-pelaajan testien kirjoittamisessa. Korjausten jälkeen Copilot törmäsi jaettuun tilaan, jossa yhden testin muutokset vaikuttivat toisen testin toimintaan. Molemmat toimivat yksittäin ajettuina, mutta yhdessä ne hajosivat. Tarvittiin 6 iteraatiota korjailua ja agentin ihan suoraa neuvomista, miten ratkoa ongelma, ennen kuin testit alkoivat toimimaan. Aikaa oli kulunut tähän mennessä jo reilut 2 tuntia. 


## Kuinka hyvät agentit tekemät testit olivat?
Tehdyt testit olivat hyviä ja kattavuuskin melko korkea. Se loi erityisesti yksikkötestejä ja jonkin verran integraatiotestejä. Robot-testien kaltaisia E2E-testejä se ei tehnyt. Testit mittasivat esim. logiikkaa, AI:n toimintaa (esim. muistia), pelin luomista, pelivuoroja, pisteiden laskentaa, pelin lopettamista ja pelin loppumista 5. vuorolla. Ne olivat siis hyvin kattavia, selkeästi nimettyjä ja siististi tehty.  

## Onko agentin tekemä koodi ymmärrettävää?
Koodi oli ymmärrettävää, mutta harmillisen toisteista. Lisäksi kaikki koodi on samassa tiedostossa, mikä teki sen lukemisesta melko kivuliasta. Esim. index.html sisälsi kaiken UI:n päivittämisestä tilanhallintaan, API-kutsuihin ja pelilogiikkaan ja koodi olisi kannattanut selkeyden vuoksi jakaa ainakin 4 eri osaan (konfiguraatio, api-kutsut, UI ja pelilogiikka). Vastaavasti web_app.py sisälsi mm. pelimoottorilogiikkaa, API:n, in-memmory-tallennuksen, JSON-viestin rakentamisen ja kutsujen validoinnin. Tämäkin koodi olisi kannattanut ainakin pilkkoa osiin ja vähentää toisteista koodia. Lisäksi koodissa oli paljon kovakoodattua ja ns. taikanumeroita. Kovakoodatut numerot tekivät testeistä hankalia muuttaa. Esim. muuttaessani pelin lopetuksen 5 voitosta 3 voittoon, jouduin muuttamaan numerot moneen paikkaan ja ajamaan testit useampaan kertaan, ennen kuin sain korjattua ne kaikki. 

## Miten agentti on muuttanut edellisessä tehtävässä tekemääsi koodia?
Agentti ei pyynnöstäni muuttanut alkuperäistä koodia vaan se rakensi web_app.py-tiedostoon logiikkaa, joka toimi rajapintana vanhan koodin ja käyttöliittymän välillä. 

## Mitä uutta opit?
Opin, että agentti pystyy tuottamaan toimivan UI:n hämmentävän hyvin. Opin myös, että agentille kannattaa antaa hyvin lyhyitä komentoja ja toimeksiantoja ja speksata hyvin tarkasti mitä haluaa sen tekevän. On hyvä pysyä tehdyistä muutoksista kärryillä, koska AI:n tuottaman koodin lukeminen on työlästä. Se periaatteessa ymmärtää ohjelmointipatterneja, mutta ei automaattisesti tuota sellaista koodia. Ohjelmointipatternit siltä pitää osata pyytää ja speksata tarkasti ja joskus iteroida useampaankin kertaan ennen hyvää lopputulosta. Siltikin se saattaa tehdä virheitä tai ymmärtää pyynnön väärin. Myös testejä AI korjaili siten, että testi meni läpi, mutta ei lopulta testannut sitä mitä olisin toivonut sen tekevän. Testien kirjoittaminenkin piti tarkkaan ohjeistaa Copilotille. Jos minun pitäisi jatkuvasti katselmoida AI:n generoimaa koodia ilman, että sitä siistittäisiin ensin, pelkään, että koodin heikon luettavuuden vuoksi saattaisin vahingossa päästää läpi bugeja ja logiikkavirheitä. 