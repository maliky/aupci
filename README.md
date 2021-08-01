
# Table des matières

1.  [Gestion de Python](#orge9b19a3)
    1.  [Installer pyenv](#orga6cd023)
    2.  [Installer python 3.8.2](#org6c0dc58)
2.  [Installation du site web](#org28adba1)
    1.  [Créer un environnement virtuel](#orge1a3fd0)
    2.  [Télécharger le code du site web](#org37e780b)
    3.  [Installer les librairies pour le développement du site web](#orgca1e7b0)
    4.  [Lancer le site web](#org8dc1ba1)
3.  [Répartition du travail](#orgc37a0fc)
    1.  [Page "admin"](#orgdb5e150)
    2.  [Prise en main de django](#org27e890a)
    3.  [Exploration flask @Adelph](#orgd082049)
4.  [Organisation du travail](#org70aaa9f)

Instructions pour recréer le site web en local.


<a id="orge9b19a3"></a>

# Gestion de Python

Afin d'éviter des conflits avec les applications python utilisé par l'OS il est bien d'installer `=pyenv=` qui permet de gérer en parallèle différentes version de python.
Par exemple, Ce website est créer avec python 3.8.2 et vous devriez travailler avec la même version.


<a id="orga6cd023"></a>

## Installer pyenv

Il y a de légère différence entre le pyenv des linux et le pyenv de windows.  Avec celui de windows il faut gérer ses environnements virtuels séparément avec virtualenv.     Avec le pyenv de linux virtualenv est inclus dans pyenv et s'utilise en faisant

    # active l'environnement virtuel appelé web
    pyenv activate web
    
    # Crée un nouvel environnement virtuel appelé web2
    pyenv virtualenv web2

1.  Sur linux (famille debian)

    Suivre les instruction du [projet sur github](https://github.com/pyenv/pyenv).  En gros
    
    1.  S'assurer d'avoir les dépendances pour compiler différentes version de python
    
            sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
            libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
            libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
    
    2.  Télécharger et exécuter l'installateur automatique
    
            curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
    
    3.  Vérifier ses fichiers de config du bash
    
        1.  dans .bashrc avoir
        
                eval "$(pyenv init -)"
        
        2.  dans .profil avoir
        
                export PYENV_ROOT="$HOME/.pyenv"
                export PATH="$PYENV_ROOT/bin:$PATH"
                if command -v pyenv 1>/dev/null 2>&1; then
                    eval "$(pyenv init --path)"
                fi
    
    4.  Redémarrer
    
        pour mettre à jour pour recharger ses fichiers de config

2.  Pour windows

    Suivre les instructions de <https://github.com/pyenv-win/pyenv-win>


<a id="org6c0dc58"></a>

## Installer python 3.8.2

    pyenv install 3.8.2
    # créer un répertoire pour le dev web
    mkdir webdev; cd webdev
    # choisir la version python 3.8.2 pour ce dossier (et sous dossier)
    pyenv local 3.8.2


<a id="org28adba1"></a>

# Installation du site web


<a id="orge1a3fd0"></a>

## Créer un environnement virtuel

    # avec linux
    pyenv virtualenv webdev
    
    # avec windows
    python -m pip install virtualenv
    virtualenv .


<a id="org37e780b"></a>

## Télécharger le code du site web

    git clone git@github.com:maliky/aupci.git

Cela va créer un répertoire avec le suivi git.

1.  Faciliter les mises à jour git

    Ajouter votre clef publique dans votre profil git (voir section sécurité)
    
    -   **rappel:** pour générer la pair de clefs utiliser `=ssh-keygen=`


<a id="orgca1e7b0"></a>

## Installer les librairies pour le développement du site web

    cd aupci
    python -m pip install -r requirements.txt

Le fichier requirements.txt liste simplement les paquets python utilisés par notre projet.


<a id="org8dc1ba1"></a>

## Lancer le site web

    python manage.py runserver

Si vous avez un avertissement concernant la base de donnée (qui n'est pas partagée) utiliser

    python manage.py migrate

Cela recrée un base de donnée vierge.

L'idée c'est dans un premier temps de ne pas partager la base de données (sqlite) mais d'en utiliser une vierge sur chacune de nos machines.

Normalement le site web doit être accessible à l'adresse <http://localhost:8000>


<a id="orgc37a0fc"></a>

# Répartition du travail

Vous verrez que la page de garde est très simple.  Je (@malik) me charge de reproduire celle du site contenu dans le dossier \`maquette<sub>website</sub>\`


<a id="orgdb5e150"></a>

## Page "admin"

localhost:8000/admin   -> point vers un portail d'administration installé par défaut mais dont nous n'avons pas besoin à moins de gérer divers profils d'utilisateurs


<a id="org27e890a"></a>

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


<a id="orgd082049"></a>

## Exploration flask @Adelph

Je propose que l'un d'entre nous regarde la possibilité de faire un site pour pycon par exemple avec flask.  On pourrait voir comment reproduire la page d'accueil de aupci avec flask.  C'est peut être plus simple et rapide à maîtriser.


<a id="org70aaa9f"></a>

# Organisation du travail

C'est évidemment un travail collaboratif, mais pour une efficacité accrue il faut que nous nous mettions tous à peu près au même niveau.  Je propose de faire un point physique jeudi prochain à 10h au LARIT pour dénouer les gros blocages.  D'ici là chacun devrait se documenter sur django et prendre pour exemple le code de ce dossier simple et fonctionnel.

