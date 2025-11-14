## viikko 5 

### Tehtävä 1 - Git: vahingossa tuhotun tiedoston palautus [versionhallinta]

- [X]  Tee tiedosto nimeltään important.txt, lisää ja committaa se Gitiin        
- [X] Poista tiedosto ja committaa     
- [X] Tee jotain muutoksia tähän tiedostoon ja committaa
- [X] git checkout f7b71e3ed1a48093f84d75b5c1d3e7b1fc6df09c -- viikko5/important.txt
```` 
 git status
On branch main
Your branch is ahead of 'origin/main' by 3 commits.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   viikko5/important.txt
````
- [X] commit changes   

### Tehtävä 2 - Git: commitin muutosten kumoaminen [versionhallinta]       
- [X] git revert HEAD --no-edit       
- [X] Varmista, että edellisen commitin tekemä muutos (eli tiedoston important.txt lisääminen) kumoutuu     

### Tehtävä 3 

- [X] echo "main 1" >> file.txt    
- [X] git add .    
- [X] git commit -m "Main commit"    
- [X] git checkout -b haara    
- [X] echo "branch work" >> branchfile.txt    
- [X] git add .    
- [X] git commit -m "Commit on haara"    
- [X] git checkout main    
- [X] echo "main 2" >> file2.txt    
- [X] git add .    
- [X] git commit -m "Main2 commit"    
- [X] git checkout haara    
- [X] git rebase main    
- [X] git checkout main    
- [X] git merge haara    
- [X] git reset --hard <old-hash>       
- [X] git branch -D haara       