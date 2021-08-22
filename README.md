#Prééquis
1. Cloner notre branche

2. Installer un moteur de base de données [postgresql](https://www.postgresql.org/download/) tout en installant pgadmin lors de l'installation de postgresql

3. Selon la section "DATABASE" dans le fichier (config/settings/base.py), il faut maintenant ouvrir pgadmin puis créer la base de données 'aupci_DB'

4. Dans ce même fichier configuration changer le mot de passe "Ferdi" par le mot de passe que vous avez utilisé lors de l'installation de postgresql.

# Installation

1. Installation des packages réquis avec la commande ci-dessous:

 ```pip install -r requirements/dev.txt```
 
 N.B: Assurez-vous que vous avez installé python et un paquet permettant de créer un environnement. Puis créez un environnement virtuel avant d'exécuter la commande

2. Créer les migrations comme suit:

```python manage.py makemigrations --settings=config.settings.dev```

3. Appliquez les migrations à la base de données

```python manage.py migrate --settings=config.settings.dev```

N.B: Supprimer le dossier migration existant avant d'appliquer les deux commandes ci-dessus.

4. Créer un super utilisateur 

```python manage.py createsuperuser --settings=config.settings.dev```


# Execution du projet
## En mode développement

Via la commande ci-dessous:

```python manage.py runserver --settings=config.settings.dev```

## En mode production

Via la commande ci-dessous:

```python manage.py runserver --settings=config.settings.production```

N.B: Toute appel à une commande necessitant manage.py doit utiliser l'une des valeurs ci-dessous pour l'option --settings
