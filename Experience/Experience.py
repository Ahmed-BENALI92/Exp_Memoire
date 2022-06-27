import encodings
import json
from pickle import TRUE
from subprocess import PIPE
import subprocess
import os 
import asyncio
import time


# On veux récuperer nos resultat et les inserer dans un dictionnaire 
def openFichier():
    with open('Resultat_git.json',encoding="utf8") as json_data:
        data_dict = json.load(json_data)
    return data_dict

def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print("Le balayage ce lancera dans :" + min_sec_format, end='\r')
        time.sleep(1)
        num_of_secs -= 1
        
    print('Debut du balayage')  


def initProjet():
    comp_process = subprocess.run("npm install" ,shell=True)
    print(comp_process.stdout)

async def main():
    # Lancer la commande gitclone via python
    print("############### Debut du Clonnage ######################")
    subprocess.run("git clone "+urlclone ,shell=True)
    print("###############fin du Clonnage ######################")
    os.chdir(name)
    print("############### Debut du téléchargement de package ######################")
    initProjet()

    print("############### Debut du start serveur ######################")
    subprocess.call('start  npm start', shell=True)
    countdown(timingPause)
    print("############### Debut du blayage owasp ######################")
    subprocess.call("cd .. & start owasp.sh" ,shell=True)    

#j'ouvre le fichier
data_dict = openFichier()
timingPause = 600
projetNumber = 0
#Maintenant qu'on posséde nos donnée dans une varible
#Nous devons injecter l'url de notre repositories dans une autre variable
urlclone = data_dict["items"][projetNumber]["clone_url"]
name= data_dict["items"][projetNumber]["name"]


    

asyncio.run(main())

