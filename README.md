# P9_LITReview

## Présentation

Ce programme est une version beta d'un site internet permettant aux utilisateurs de pouvoirs poster et obtenir des avis sur des livres.

Les objectifs de ce programme sont les suivants:

 * Connection et inscritpion - le site ne doit pas être accessible à un utilisateur non connecté.
 * Afficher un flux contenant les derniers tickets et avis des utilisateurs qu'ils suivent, classés par heure, les plus récents en premier.
 * Créer de nouveaux tickets pour demander une critique sur un livre/article.
 * Créer des avis en réponse aux tickets.
 * Créer des avis non en réponse à un ticket. Dans le cadre d'un processus en une étape, l'utilisateur créera un ticket, puis un avis répondant à son propre ticket.
 * Pouvoir afficher, modifier et supprimer ses propres tickets et avis,
 * Suivez d'autres utilisateurs en saisissant leur nom d'utilisateur,
 * Voir qui ils suivent et ne plus suivre qui ils veulent.

## Pour commencer

Les instructions ci dessous vous aiderons à exécuter correctement ce programme.

## Pré-requis

* Python 3 installé [Télécharger Python](https://www.python.org/downloads/)
* Savoir naviguer dans les dossiers & fichiers à partir d'un terminal.

## Installation

Pour un bon fonctionnement, il est préférable d'exécuter le programme dans un environnement virtuel. Pour cela, ci dessous les étapes à suivre:

1. **Téléchargement du projet.**

    1. Depuis votre terminal, placez vous à l'endroit souhaité:
    
    ```cd [chemin d'accès]```  
    
    2. Creer un nouveau dossier:
    
    ```mkdir [nom de votre dossier]```
    
    3. Copier le programme source:
    
    ```git clone https://github.com/JM-Duval/P9_LITReview.git```
    

Vous devez voir (depuis votre explorateur) les dossiers suivants: 

 * accounts/
 * litreview_project/
 * posts/
 * review/
 * subscription/
 * ticket/

Et les fichiers suivants:

 * .gitignore
 * README.md

2. **Creer un environnement virtuel.**

Depuis windows/mac/linux: ```python3 -m venv env```

3. **Activer l'environnement.**

Depuis windows: ```env\Scripts\activate.bat```

Depuis mac/linux: ```source env/bin/activate```

Si vous rencontrez des difficultés ou si vous souhaitez plus de détails sur l'installation d'un environnement virtuel, vous pouvez vous reporter à la documentation Python:
[Documentation Python](https://www.python.org/doc/)

4. **Installer les paquets.**

```pip install -r requirements.txt```

En executant la commande: pip freeze, vous devez voir apparaitre cette liste: 
- asgiref==3.4.1
- astroid==2.8.0
- colorama==0.4.4
- Django==3.2.6
- django-crispy-forms==1.12.0
- django-debug-toolbar==3.2.2
- flake8==3.9.2
- isort==5.9.3
- lazy-object-proxy==1.6.0
- mccabe==0.6.1
- Pillow==8.3.2
- platformdirs==2.4.0
- psycopg2==2.9.1
- pycodestyle==2.7.0
- pyflakes==2.3.1
- pylint==2.11.1
- pytz==2021.1
- sqlparse==0.4.1
- toml==0.10.2
- typing-extensions==3.10.0.2
- wrapt==1.12.1


5. **Lancement du programme.**

A l'endroit ou se situe votre dossier, exécuter la commande suivante:

```./manage.py runserver```

Losque vous allez lancer le programme depuis le terminal, vous allez voir apparaitre le texte ci dessous:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 06, 2021 - 17:47:35
Django version 3.2.6, using settings 'litreview_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK. 
```

Copiez l'adresse ```http://127.0.0.1:8000/``` dans la barre de votre navigateur web. Vous devez accèder directement sur le site internet concerné.


## Fabriqué avec
[PyCharm Community Edition 2020.2.3 x64](https://pycharm-community-edition.fr.softonic.com/) - Editeur de textes


## Auteurs

* **JM Duval** 

