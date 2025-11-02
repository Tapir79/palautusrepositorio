## viikko 2 

### Tehtävä 1 
- [X] Luo kansiot              
- [X] Poetry init --python "^3.12"            
- [X] Poetry add flask@latest             
- [X] Poetry add --group dev pytest             
- [X] Poetry run pytest --version  -> 8.4.2            
- [X] Poetry add sqlalchemy              
- [X] Poetry add "sqlalchemy==1.4.54"             
- [X] Poetry remove flask          
- [X] Poetry add fastapi               

### Tehtävä 2 
- [X] Poetry add requests                
- [X] Liitä index-runko             
- [X] Luo attribuutit player luokalle JSON-datasta             
- [X] Luo tulostus pelaajille             

### Tehtävä 3
- [X] Suodata suomalaiset pelaajat        
- [X] Järjestä pisteiden mukaan           
- [X] Muotoile tulostus      

### Tehtävä 4 
- [X] Luo PlayerReader ja PlayerStats        
- [X] Toteuta PlayerReader           
- [X] Toteuta PlayerStats         
- [X] Kytke uusi logiikka pääohjelmaan                    

### Tehtävä 5
- [X] Poetry add rich      
- [X] Luo valintavalikot        
- [X] Luo tulostustaulukko richillä valitun maan ja kauden pelaajille        

![Coverage report](kuvat/vko2_harj5_rich.png)

### Tehtävä 8 
- [X] Lisää pylint ja autopep8 projektiin           
- [X] Korjaa pylint virheet 
- [X] Bonus: Lisää pre-commit projektin juureen, joka suorittaa pylint-tarkistuksen alikansiolle nhl-reader             
````
  GNU nano 6.2                                                            .git/hooks/pre-commit                                                                     
#!/bin/bash
export PATH="$HOME/.local/bin:$PATH"

echo "🔍 Running Pylint for viikko2/nhl-reader project..."

# Siirrytään oikeaan hakemistoon, jossa pyproject.toml sijaitsee
cd "$(git rev-parse --show-toplevel)/viikko2/nhl-reader" || exit 1

# Tarkistetaan, että Poetry on asennettu
if ! command -v poetry &> /dev/null; then
    echo "❌ Poetry not found in PATH. Please install Poetry."
    exit 1
fi

# Aja pylint käyttäen Poetry-ympäristöä
poetry run pylint src
RESULT=$?

if [ $RESULT -ne 0 ]; then
    echo ""
    echo "❌ Commit cancelled — Pylint found issues in viikko2/nhl-reader."
    echo "Fix the issues and try committing again."
    exit 1
fi

echo "✅ Pylint passed successfully for viikko2/nhl-reader!"
exit 0

````                

### Tehtävä 9

- [X] Luo alihakemisto viikko2/git-branch-harjoitus          
- [X] Main-haarassa cd viikko2/git-branch-harjoitus         
- [X] Luo ja committaa hakemistoon tiedosto index.py          
- [X] git checkout -b laskut       
- [X] laskut-haarassa luo tiedosto summa.py        
- [X] laskut-haarassa lisää ja committaa summa.py versionhallintaan           
- [X] git checkout main              
- [X] Main-haarassa luo tiedosto logger.py          
- [X] Main-haarassa muokkaa tiedostoa  index.py         
- [X] main-haarassa committaa muutokset        
- [X] git checkout -b laskut       
- [X] laskut-haarassa lisää ja committaa tiedosto erotus.py         
- [X] git checkout main          
- [X] Asenna gitk         
- [X] Tarkastele gitk:lla git-puuta       
![Coverage report](kuvat/gitk_week2.png)   
- [X] main-haarassa git merge laskut     
- [X] main-haarassa muuta tiedostoa index.py ja commitoi muutos    
- [X] Tarkastele gitk:lla git-puuta         
![Coverage report](kuvat/gitk_week2_main_final.png)