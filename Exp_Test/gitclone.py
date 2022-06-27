import encodings
import json
from pickle import TRUE
from subprocess import PIPE
import subprocess
import os 
import asyncio
import time

def initProjet():
    comp_process = subprocess.run("npm install" ,shell=True)
    print(comp_process.stdout)


def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print("Le balayage ce lancera dans :" + min_sec_format, end='\r')
        time.sleep(1)
        num_of_secs -= 1
        
    print('Debut du balayage')  
    
async def main():
    print("############### Debut du téléchargement de package ####################")
    initProjet()
    print("############### fin du téléchargement de package ######################")
    print("############### Debut du lancement du projet ##########################")
    subprocess.call('start  npm start', shell=True)
    print("############### Debut de la pause #####################################")
    countdown(timingPause)
    print("############### fin de la pause #######################################")
    subprocess.call("cd .. & start owasp.sh" ,shell=True)


timingPause = 300
#On se dirige dans le dossier que nous avions clonnée pour pouvoir compiler le projet
os.chdir("cwa-website")


asyncio.run(main())

