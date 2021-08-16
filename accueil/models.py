from django.db import models

# Create your models here.
class Adherent(models.Model):
    date_demande = models.DateTimeField(auto_now_add=True)
    date_acceptance = models.DateTimeField(auto_now_add=False)

    nom = models.CharField(max_length=50, blank=True, null=True)
    prenom = models.CharField(max_length=50, blank=True, null=True)

    numero_telephone = models.CharField(max_length=20, blank=True, null=True)
    courriel = models.EmailField()
    occupation = models.CharField(max_length=50, blank=True, null=True)
