
# II. Spécifications fonctionnelles
En réponse aux besoins exprimés dans l’énoncé, l’application web **Échange de Compétences** comporte les fonctionnalités suivantes :

----------
## 1. Pour tous les utilisateurs (Visiteur & Utilisateur connecté)
**UC1 – Voir les créneaux anonymes des autres utilisateurs** (`TASK1`)
-   **Visiteur** : affiche uniquement les créneaux de façon **anonyme**, sans révéler l’identité des utilisateurs.
-   **Utilisateur connecté** : affiche les créneaux où d’autres utilisateurs recherchent de l’aide, **avec prénom, nom et email**, mais uniquement pour les compétences que l’utilisateur connecté possède.

**UC2 – Afficher la liste des compétences disponibles** (`TASK2`)
-   Affiche toutes les compétences proposées par l’application.
-   Accessible par : Visiteur, Utilisateur connecté
----------
## 2. Pour les utilisateurs non connectés (Visiteur)
**UC3 – S’inscrire / se connecter**
-   Permet de créer un compte utilisateur (email + mot de passe) ou de se connecter.
-   Après connexion, le visiteur devient Utilisateur connecté.
----------
## 3. Pour les utilisateurs connectés (Utilisateur connecté)
### Gestion des compétences
**UC4 – Afficher mes compétences** (`TASK3`)
-   Permet de visualiser toutes les compétences que l’utilisateur a ajoutées à son profil.

**UC5 – Supprimer mes compétences** (`TASK4`)
-   Permet de retirer une compétence précédemment ajoutée.
-   Inclus dans UC4.

**UC6 – Sélectionner compétences à offrir** (`TASK5`)
-   Permet de choisir parmi les compétences disponibles celles que l’utilisateur souhaite proposer pour aider les autres.
-   Dépend de UC2, mais n’est pas accessible aux visiteurs.

### Gestion des créneaux (optionnel)
**UC7 – Définir mes créneaux disponibles pour aider d’autres utilisateurs** (`TASK6_OPT`)
-   Permet de définir les journées où l’utilisateur est disponible pour aider d’autres personnes.

### Gestion des demandes d’aide
**UC8 – Créer mes demandes d’aide** (`TASK7`)
-   Permet de créer une demande d’aide pour une activité spécifique, en sélectionnant la compétence correspondante.

**UC9 – Consulter les demandes d’aide des autres** (`TASK8`)
-   Affiche les demandes d’aide existantes pour lesquelles l’utilisateur possède la compétence correspondante.
-   Montre **prénom, nom et email** de la personne à aider.

**UC10 – Accepter ou refuser une demande d’aide** (`TASK9`)
-   Permet à l’utilisateur de se rendre volontaire pour aider une autre personne sur un créneau spécifique.
-   Une fois accepté, le créneau n’apparaît plus dans les autres affichages pour ce créneau précis.

### Affichages optionnels

**UC11 – Afficher les propositions de disponibilité des autres utilisateurs** (`TASK10_OPT`)
-   Affiche les créneaux où d’autres utilisateurs se rendent disponibles pour aider dans des activités que l’utilisateur n’a pas demandées.

----------

## Règles et contraintes métier

1.  Chaque utilisateur peut posséder plusieurs compétences et proposer plusieurs créneaux pour aider.
2.  Une compétence ne peut être ajoutée qu’une seule fois au profil d’un utilisateur.
3.  Une demande d’aide doit toujours être associée à une compétence existante dans le système.
4.  Un créneau accepté par un utilisateur n’est plus visible dans les autres affichages pour ce créneau précis.
5.  **Les informations visibles sur un autre utilisateur connecté sont limitées au prénom, nom et email.**
6.  Le système fonctionne avec une journée entière comme unité de créneau pour simplifier la planification.
7.  Les compétences et utilisateurs autorisés sont gérés via le site d’administration Django.
    
----------

## Contraintes techniques

-   Utiliser **Django 5.2.12** avec la base SQLite par défaut.
-   Application web sécurisée avec authentification utilisateur.
-   Application prête pour futur ajout de fonctionnalités (météo, recherche de proximité, créneaux horaires précis).
-   Respecter les bonnes pratiques : environnement virtuel, POO, typage statique optionnel, exceptions, docstrings, anglais dans le code, lisibilité.