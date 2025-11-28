## viikko 6 

### Tehtävä 1 - Laskin ja komento-oliot
- [X] Kopioi viikko6/laskin     
- [X] Asenna riippuvuudet ja testaa laskinta   
- [X] Refaktoroi if-hässäkkä   

### Tehtävä 2 - kumoa toiminto 
- [X] Toteuta laskimeen kumoa-toiminto
- [X] Bonus: mielivaltainen määrä peräkkäisiä kumoamisia   

### Tehtävä 3 - Kyselykieli NHL-tilastoihin    
- [X] Toteuta strategy pattern   All   
- [X] Toteuta strategy pattern   HasFewerThan     
- [X] Toteuta strategy pattern   Not         



````
matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )
Owen Tippett         PHI          20 + 23 = 43
Matvei Michkov       PHI          26 + 37 = 63
Sean Couturier       PHI          15 + 30 = 45
Bobby Brink          PHI          12 + 29 = 41
Noah Cates           PHI          16 + 21 = 37
Travis Konecny       PHI          24 + 52 = 76
Travis Sanheim       PHI          8  + 22 = 30
````

````
matcher = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )

Chad Ruhwedel        NYR          0  + 1  = 1
Zac Jones            NYR          1  + 10 = 11
Brennan Othmann      NYR          0  + 2  = 2
Matthew Robertson    NYR          0  + 0  = 0
Gabe Perreault       NYR          0  + 0  = 0
Connor Mackey        NYR          0  + 0  = 0
````

````
filtered_with_all = stats.matches(All())
print(len(filtered_with_all)) 

899
````


### Tehtävä 4 - Kyselykieli NHL-tilastoihin, osa 2
- [X] Toteuta strategy pattern   Or     
- [X] Varmista, että kyselyt palauttavat oikeat pelaajat  


````
    matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )

William Nylander     TOR          45 + 39 = 84
Mitch Marner         TOR          27 + 75 = 102
Leon Draisaitl       EDM          52 + 54 = 106
Connor McDavid       EDM          26 + 74 = 100
Nikita Kucherov      TBL          37 + 84 = 121
Nathan MacKinnon     COL          32 + 84 = 116
````

````
matcher = And(
    HasAtLeast(70, "points"),
    Or(
        PlaysIn("COL"),
        PlaysIn("FLA"),
        PlaysIn("BOS")
    )
)

David Pastrnak       BOS          43 + 63 = 106
Aleksander Barkov    FLA          20 + 51 = 71
Cale Makar           COL          30 + 62 = 92
Sam Reinhart         FLA          39 + 42 = 81
Nathan MacKinnon     COL          32 + 84 = 116
````


### Tehtävä 5 - Parannettu kyselykieli, osa 1
- [X] Toteuta QueryBuilder    
- [X] Varmista, että kyselyt palauttavat oikeat pelaajat  

```` 
matcher = query.plays_in("NYR").build()
    Vincent Trocheck     NYR          26 + 33 = 59
    K'Andre Miller       NYR          7  + 20 = 27
    Brett Berard         NYR          6  + 4  = 10
    Braden Schneider     NYR          6  + 15 = 21
    Adam Fox             NYR          10 + 51 = 61
    Chad Ruhwedel        NYR          0  + 1  = 1
    Zac Jones            NYR          1  + 10 = 11
    Brennan Othmann      NYR          0  + 2  = 2
    Arthur Kaliyev       NYR          3  + 1  = 4
    Chris Kreider        NYR          22 + 8  = 30
    Matthew Robertson    NYR          0  + 0  = 0
    Alexis Lafrenière    NYR          17 + 28 = 45
    Sam Carrick          NYR          6  + 14 = 20
    Will Cuylle          NYR          20 + 25 = 45
    Adam Edstrom         NYR          5  + 4  = 9
    Artemi Panarin       NYR          37 + 52 = 89
    Jonny Brodzinski     NYR          12 + 7  = 19
    Matt Rempe           NYR          3  + 5  = 8
    Gabe Perreault       NYR          0  + 0  = 0
    Mika Zibanejad       NYR          20 + 42 = 62
    Connor Mackey        NYR          0  + 0  = 0
```` 
    
````
matcher = query.plays_in("NYR").has_at_least(10, "goals").has_fewer_than(20, "goals").build()

Adam Fox             NYR          10 + 51 = 61
Alexis Lafrenière    NYR          17 + 28 = 45
Jonny Brodzinski     NYR          12 + 7  = 19
````