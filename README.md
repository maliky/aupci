# Installation

Installation des packages réquis avec la commande ci-dessous:

 ```pip install -r requirements/dev.txt```
 
 N.B: Assurez-vous que vous avez installé python et un paquet permettant de créer un environnement. Puis créez un environnement virtuel avant d'exécuter la commande
# Execution du projet
## En mode développement

Via la commande ci-dessous:

```python manage.py runserver --settings=config.settings.dev```

## En mode production

Via la commande ci-dessous:

```python manage.py runserver --settings=config.settings.production```