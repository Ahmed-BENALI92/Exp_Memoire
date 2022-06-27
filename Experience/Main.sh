#!/bin/bash
# La fonction va utiliser l'api github et mettre tous les resultats dans le fichier Resultat_git.json
function initSearchGit()
{
    curl "https://api.github.com/search/repositories?l=JavaScript&q=npm+install+startin:readme&q=app+web&type=Repositories">Resultat_git.json
}




initSearchGit

# Clonner le dossier github via notre code python 
python Experience.py


exit