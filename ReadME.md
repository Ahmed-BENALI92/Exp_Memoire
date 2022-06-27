# Automatisation de test de vulnérabiliter avec owasp zap


Le but de ce projet est d'automatiser le déploiement d'un projet web github en javascript et de lancer le balayage de test de l'owasp zap. 


## Pour commencer

Notre projet est composé de deux mini projets.
Un projet [Exp_Test](/Exp_Test/) qui va juste tester l'automatisation d'installation d'une application web, appeler cwa-website et du lancement du balayage de l'owasp zap.
Ensuite nous avons [Experience](/Experience/) qui va clonée un projet quelconque l'installer puis lancer les tests de vulnérabilité. 

Notre programme va utiliser l'Api de github pour récupérer le lien de plusieurs projets d'application web puis le résultat sera injecté sur le fichier [Resultat_git.json](/Experience/Resultat_git.json).Puis il va cloner le premier projet de la liste retournée. Ensuite il va installer toutes les dépendances du projet puis il va start le projet.

En attendant que le projet ce lance, il y'aura un compte à rebours de 10 min. Un fois les 10 minutes écoulée le balayage de l'owasp se lancera automatiquement. Vous pouvez changer la valeur du compte à rebours en changeant la variable ``` timingPause = 600 ```, qui sera en seconde, dans le fichier [gitclone.py](/Exp_Test/gitclone.py) ou [Experience.py](/Experience/Experience.py). 
Si le projet n'est pas compatible vous pouvez le changer en modifiant la variable ``` projetNumber = 0```.

### Pré-requis


- installer [OwaspZAP](https://www.zaproxy.org/download/)
- installer [npm et node](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
- installer [python3](https://www.python.org/downloads/)


### Installation

_WARNING_ **Telecharger le fichier du projet sur votre bureau**: Car aprés le balayage, owasp zap va créer un fichier json dans dans le fichier [Rapport.json](/Experience/Rapport.json) ou il va stocker le rapport de l'annalyse. 


## Démarrage


Placer vous sur la racine du dossier que vous voulez utiliser

Executez la commande ``./Main.sh`` 




## Auteurs
* **Ahmed BENALI** _alias_ [@Ahmed-BENALI92](https://github.com/Ahmed-BENALI92)



