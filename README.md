#Prééquis
1. Cloner notre branche

2. Installer un moteur de base de données [postgresql](https://www.postgresql.org/download/) tout en installant pgadmin lors de l'installation de postgresql

<<<<<<< HEAD
1.  [Gestion de Python](#org4ece436)
    1.  [Installer `pyenv`](#orgd1d6a93)
    2.  [Installer python 3.8.2](#orga834c3c)
2.  [Installation du site web](#orge92d117)
    1.  [Créer un environnement virtuel](#org12fece4)
    2.  [Télécharger le code du site web](#orgb2c700f)
    3.  [Installer les librairies pour le développement du site web](#org618053f)
    4.  [Lancer le site web](#org4cf5647)
3.  [Répartition du travail](#org748e4b9)
    1.  [Page "admin"](#org8b88d74)
    2.  [Prise en main de django](#org2afb079)
    3.  [Exploration flask @Adelph](#org4b4a976)
4.  [Organisation du travail](#orgaa583d4)
=======
3. Selon la section "DATABASE" dans le fichier (config/settings/base.py), il faut maintenant ouvrir pgadmin puis créer la base de données 'aupci_DB'
>>>>>>> master

4. Dans ce même fichier configuration changer le mot de passe "Ferdi" par le mot de passe que vous avez utilisé lors de l'installation de postgresql.

# Installation

<<<<<<< HEAD
<a id="org4ece436"></a>
=======
1. Installation des packages réquis avec la commande ci-dessous:
>>>>>>> master

 ```pip install -r requirements/dev.txt```
 
 N.B: Assurez-vous que vous avez installé python et un paquet permettant de créer un environnement. Puis créez un environnement virtuel avant d'exécuter la commande

<<<<<<< HEAD
Afin d'éviter des conflits avec les applications python utilisé par l'OS il est bien d'installer `pyenv` qui permet de gérer en parallèle différentes version de python.
Par exemple, Ce website est créé avec `python 3.8.2` et vous devriez travailler avec la même version.
=======
2. Créer les migrations comme suit:
>>>>>>> master

```python manage.py makemigrations --settings=config.settings.dev```

<<<<<<< HEAD
<a id="orgd1d6a93"></a>
=======
3. Appliquez les migrations à la base de données
>>>>>>> master

```python manage.py migrate --settings=config.settings.dev```

<<<<<<< HEAD
Il y a de légère différence entre le `pyenv` des linux et le `pyenv` de windows.  Avec celui de windows il faut gérer ses environnements virtuels séparément avec `virtualenv`.     Avec le `pyenv` de linux `virtualenv` est inclus dans `pyenv` et s'utilise en faisant `pyenv virtualenv`.
=======
N.B: Supprimer le dossier migration existant avant d'appliquer les deux commandes ci-dessus.
>>>>>>> master

4. Créer un super utilisateur 

<<<<<<< HEAD
    Suivre les instruction du [projet sur github](https://github.com/pyenv/pyenv).  En gros
    
    1.  S'assurer d'avoir les dépendances pour compiler différentes version de python
    
            sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
            libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
            libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
    
    2.  Télécharger et exécuter l'installateur automatique
    
            curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
    
    3.  Vérifier les fichiers de config de son shell (bash)
    
        1.  dans .bashrc avoir
        
                eval "$(pyenv init -)"
        
        2.  dans .profil (ou .bash\_profil) avoir
        
                export PYENV_ROOT="$HOME/.pyenv"
                export PATH="$PYENV_ROOT/bin:$PATH"
                if command -v pyenv 1>/dev/null 2>&1; then
                    eval "$(pyenv init --path)"
                fi
    
    4.  Redémarrer
    
        pour mettre à jour et recharger la config
=======
```python manage.py createsuperuser --settings=config.settings.dev```
>>>>>>> master


# Execution du projet
## En mode développement

Via la commande ci-dessous:

<<<<<<< HEAD
<a id="orga834c3c"></a>
=======
```python manage.py runserver --settings=config.settings.dev```
>>>>>>> master

## En mode production

Via la commande ci-dessous:

```python manage.py runserver --settings=config.settings.production```

<<<<<<< HEAD
<a id="orge92d117"></a>

# Installation du site web


<a id="org12fece4"></a>

## Créer un environnement virtuel

    # avec linux
    pyenv virtualenv webdev
    
    # avec windows
    python -m pip install virtualenv
    virtualenv .


<a id="orgb2c700f"></a>

## Télécharger le code du site web

    git clone https://github.com/maliky/aupci.git

Cela va créer un répertoire avec le suivi git.

1.  Faciliter les mises à jour git

    Ajouter votre clef publique dans votre profil git (voir section sécurité)
    
    -   **rappel:** pour générer la pair de clefs utiliser `ssh-keygen`


<a id="org618053f"></a>

## Installer les librairies pour le développement du site web

    cd aupci
    python -m pip install -r requirements.txt

Le fichier requirements.txt liste simplement les paquets python utilisés par notre projet.


<a id="org4cf5647"></a>

## Lancer le site web

1.  Créer la base de donnée

        python manage.py migrate

2.  Lancer le serveur en local

        python manage.py runserver
    
    L'idée c'est dans un premier temps de ne pas partager la base de données (sqlite) mais d'en utiliser une vierge sur chacune de nos machines.
    
    Normalement le site web doit être accessible à l'adresse <http://localhost:8000>
    
    Il faut le rendre sembable à la maquette.


<a id="org748e4b9"></a>

# Répartition du travail

Vous verrez que la page de garde est très simple.  Je (@malik) me charge de reproduire celle du site contenu dans le dossier \`maquette\_website\`


<a id="org8b88d74"></a>

## Page "admin"

localhost:8000/admin   -> point vers un portail d'administration installé par défaut mais dont nous n'avons pas besoin à moins de gérer divers profils d'utilisateurs


<a id="org2afb079"></a>

## Prise en main de django

Pour la prise en main de django je propose de vous attribuer chacun la responsabilité d'un page web:

1.  Les pages

    1.  Page "Évènement" @Morié
    
        Accessible à aup.ci/evenement
    
    2.  Page "Qui Sommes-nous" @Atta
    
        Accessible à aup.ci/qui-somme-nous    
    
    3.  Page "Contact" @Gnimanssoun
    
        Accessible à aup.ci/contact    
    
    4.  Page "Adhésion" @Kopoin
    
        Accessible à aup.ci/contact    

2.  Comment les éditer ?

    Les fichiers à modifier sont principalement :
    
    1.  accueil/urls.py
    
        fait le lien entre l'url et le classe (View) qui contient la logique pour générer la page
    
    2.  accueil/views.py
    
        gère la logique de la requête.  En gros récupère l'objet HTTPRequest associé à POST, GET, PUT ect. effectue en traitement et appelle un template pour représenter les data
    
    3.  accueil/templates/accueil/
    
        C'est le dossier qui contient les templates appelé par les views.  On parle de templates, car il y a un mini langage pour par exemple faire un tableau html à partir d'un objet python list.  Et puis on peut réutiliser du code comme le fichier base.html (avec les headers)


<a id="org4b4a976"></a>

## Exploration flask @Adelph

Je propose que l'un d'entre nous regarde la possibilité de faire un site pour pycon par exemple avec flask.  On pourrait voir comment reproduire la page d'accueil de aupci avec flask.  C'est peut être plus simple et rapide à maîtriser.


<a id="orgaa583d4"></a>

# Organisation du travail

C'est évidemment un travail collaboratif, mais pour une efficacité accrue il faut que nous nous mettions tous à peu près au même niveau.  Je propose de faire un point physique jeudi prochain à 10h au LARIT pour dénouer les gros blocages.  D'ici là chacun devrait se documenter sur django et prendre pour exemple le code de ce dossier simple et fonctionnel.

Le <span class="underline">projet</span> django s'appel **aupci** et <span class="underline">l'application</span>  **accueil**.

=======
N.B: Toute appel à une commande necessitant manage.py doit utiliser l'une des valeurs ci-dessous pour l'option --settings
>>>>>>> master
