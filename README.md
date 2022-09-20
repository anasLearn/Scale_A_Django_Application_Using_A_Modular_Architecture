## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


## Déploiement
Dans ce projet le deploiement de l'application sur Heroku est automatisé avec un pipeline CI/CD sur CircleCI.<br>
Les détails de la configuration du pipeline sont disponibles dans le fichier config.yml du dossier .circleci

### Fonctionnement du déploiement :

- Lors d'un **git push** depuis la branche master du projet, le pipeline déclenche le linting et les tests.<br>Si le linting et les tests sont réussis, il déclenche la conteneurisation et envoie l'image sur DockerHub.<br>
Si la conteneurisation et l'envoi de l'image sont réussis, il exécute le déploiement de l'application sur Heroku.

- Seules les modifications apportées à la branche master dans Github déclenchent la conteneurisation et le deploiement du site vers Heroku.

- Les modifications apportées aux autres branches du projet déclencheront uniquement le linting et les tests.

![alt tag](https://user-images.githubusercontent.com/83015257/191265011-9c8ea0ae-fe32-485b-96c6-dec8045c2511.png)

- Lien vers le Pipeline du projet sur CircleCI :<br> <https://dl.circleci.com/status-badge/redirect/gh/SelHel/Scale_A_Django_Application_Using_A_Modular_Architecture/tree/master>

### Prérequis

- Un compte [Github](https://github.com)
- Un compte [DockerHub](https://hub.docker.com/)
- Un compte [CircleCI](https://circleci.com/signup/)
- Un compte [Heroku](https://signup.heroku.com/)
- Installer [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up

### Configuration du déploiement
#### CircleCI
- Vous devez créer un nouveau projet sur CircleCI et le lier à votre repository GitHub.
- Sélectionnez la branche master comme source pour le fichier .circleci/config.yml


- Créer un projet DockerHub.
- Créer un projet Heroku.
- Obtenir un token d'authentification Heroku. ([Documentation](https://devcenter.heroku.com/articles/authentication))
- Renseigner les variables d'environnement.

- Après le déploiement le site est accessible à l'adresse suivante: [https://oc-lettings-17.herokuapp.com](https://oc-lettings-17.herokuapp.com)

## Surveillance de l'application et suivi des erreurs via Sentry

Sentry est une application de suivi d'exceptions non gérées.

### Prérequis

- Un compte [Sentry](https://sentry.io/signup/)

### Utilisation

- Créer un projet Sentry
- Ajouter l'adresse obtenue aux variables d'environnement.

## Variables d'environnement

Les variables d'environnement sont des données sensibles à dissimuler du public, elle sont à placer à plusieurs endroits:
- Dans un fichier nommé **.env** à la racine du projet
- Dans la configuration du projet dans CircleCI

| Clé  | Valeur          | Lieu |
| :--------------: |:---------------:|:---------:|
| SECRET_KEY  |   Clé secrète DJANGO  | Fichier/CircleCI |
| DEBUG  | True / False  | Fichier/CircleCI |
| ALLOWED_HOSTS  | localhost,0.0.0.0,127.0.0.1,<your-app>.herokuapp.com  | Fichier/CircleCI |
| DOCKERHUB_USER  | Utilisateur DockerHub  | CircleCI |
| DOCKERHUB_TOKEN  | Token de connexion DockerHub  | CircleCI |
| HEROKU_TOKEN  | Tocken de connexion Heroku  | CircleCI |
| SENTRY  | Adresse Sentry  | Fichier/CircleCI |

