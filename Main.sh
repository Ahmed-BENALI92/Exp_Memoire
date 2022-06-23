#!/bin/bash
# La fonction va utiliser l'api github et mettre tous les resultats dans le fichier Resultat_git.json
function initSearchGit()
{
    curl "https://api.github.com/search/repositories?q=src+in:app+language:js">Resultat_git.json
}




initSearchGit

# Clonner le dossier github via notre code python 

python gitclone.py
exit