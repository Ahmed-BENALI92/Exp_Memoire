import encodings
import json
from subprocess import PIPE
import subprocess


# On veux récuperer nos resultat et les inserer dans un dictionnaire 
with open('Resultat_git.json',encoding="utf8") as json_data:
    data_dict = json.load(json_data)

#Maintenant qu'on posséde nos donnée dans une varible
#Nous devons injecter l'url de notre repositories dans une autre variable
Urlclone = data_dict["items"][2]["clone_url"]

# Lancer la commande gitclone via python
comp_process = subprocess.run("git clone "+Urlclone ,stdout=PIPE, stderr=PIPE)
print(comp_process.stdout)


