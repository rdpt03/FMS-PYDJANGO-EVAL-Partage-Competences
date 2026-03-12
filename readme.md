
# FMS-PYDJANGO-EVAL-Partage-Competences  
  
## Description  
Ce projet est une application web développée dans le cadre de l'évaluation Python-Java P1 2026 à l'Académie CDA.   
Le but est de créer un système permettant aux utilisateurs d'échanger des compétences (ex. : jardinage, administration informatique) et d'accomplir des activités avec d'autres personnes.  
  
Cette version prototype ne prend pas en compte la recherche de proximité ou la météo, et considère que chaque créneau correspond à une journée entière.  
  
---  
  
## Fonctionnalités  
  
### Pour les visiteurs  
- Voir la liste des compétences disponibles  
- Voir les prochains créneaux proposés anonymement  
  
### Pour les utilisateurs connectés  
- **Login / Logout** ✔  
- **Inscription** ✔  
- Ajouter des compétences à son profil ✔ (liste existante)  
- Demander de l'aide pour une activité ✔  
- Accepter des demandes d'aide ✔  
- Voir les prochains créneaux acceptés ✔  
- Administration des compétences via Django Admin ✔  
  
> Note : Les catégories de compétences et l'option d'offrir de l'aide directement ne sont pas implémentées.  
  
---  
  
## Architecture & Modèles  
  
- **App principale :** `core`  
- **Modèles principaux :**  
 - `Person` : informations personnelles  
 - `Skill` : compétences  
 - `Task` : activité, avec type `REQUEST` ou `PROPOSAL`  
 - `User` : Django User étendu par `Person`  
  
Relations principales :  
- Une personne peut posséder plusieurs compétences  
- Une personne peut demander ou aider dans plusieurs tâches  
- Chaque tâche est liée à au moins une compétence  
  
---  
  
## Technologies utilisées  
- Python 3  
- Django 5.2  
- SQLite (base de données par défaut)  
- HTML, CSS, Bootstrap  
  
---  
  
## Installation  
  
1. Cloner le projet  
```bash  
git clone https://github.com/rdpt03/FMS-PYDJANGO-EVAL-Partage-Competences.git  
cd FMS-PYDJANGO-EVAL-Partage-Competences
```
2.  Créer un environnement virtuel
```
python -m venv venv  
source venv/bin/activate # Linux / Mac  
venv\Scripts\activate # Windows
```
3.  Installer les dépendances
```
pip install -r requirements.txt
```
4.  Mettre à jour la base de données
```
python manage.py makemigrations  
python manage.py migrate
```
5.  Lancer le serveur
```
python manage.py runserver
```
----------

## Spécifications fonctionnelles & maquettes

-   Diagrammes UML ✔
-   Maquettes / Wireframes ✔ : [lien]   
-   Spécifications fonctionnelles ✔
    

----------

## Utilisation
-   Créer un compte ou se connecter
-   Ajouter les compétences que vous possédez
-   Créer une demande d'aide pour une activité
-   Voir les créneaux disponibles et accepter ceux correspondant à vos compétences
-   Admin : gérer les compétences et les utilisateurs
