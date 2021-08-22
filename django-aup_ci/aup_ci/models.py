from django.db import models
from django.contrib.auth.models import User

class TimestampUseModel(models.Model):
    Date_creation = models.DateTimeField(auto_now_add=True)
    Date_Mise_a_Jour = models.DateTimeField(auto_now=True)

    class Meta:
        abstract= True

class DemandeAdhesion(TimestampUseModel):

    nom = models.CharField(max_length=150)
    prenoms = models.CharField(max_length=255)
    profession = models.CharField(max_length=250)
    entreprise= models.CharField(max_length=250)
    telephone = models.CharField(max_length=20)
    courriel = models.EmailField()

    def __str__(self):
        return '{} {} <{}>'.format(self.prenoms, self.nom, self.courriel)


class Membre(models.Model):

    LISTE_choix = [("PR", "Président"), ("VP", "Vice-Président"), ("SG", "Sécrétaire Générale"), ("TR", "Trésorière Générale"), ("VT", "Vice-Trésorière"), ("C1", "Premier Commissaire aux comptes"), ("C2", "Second Commissaire aux comptes"), ("Mb", "Membre actif")]

    demande = models.OneToOneField(DemandeAdhesion, on_delete=models.CASCADE, primary_key=True)
    fonction = models.CharField(max_length=2, choices=LISTE_choix, default="Mb")
    date_adhesion = models.DateTimeField()

    def __str__(self):
        return '{}'.format(self.fonction)


class Evenement(TimestampUseModel):

    #demande = models.OneToOneField(DemandeAdhesion, on_delete=models.CASCADE, primary_key=True)
    LISTE_choix = [("HN", "Hackaton"), ("PN", "PyCon"), ("MP", "Meetup"), ("AR", "Atelier"), ("AG", "Assemblé Générale")]
    createur = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    titre = models.CharField(max_length=255)
    lieu = models.CharField(max_length=255)
    #type_evenement = models.CharField(max_length=255)
    type_evenement = models.CharField(max_length=2, choices=LISTE_choix, default="MP")
    description = models.TextField()
    date_adhesion = models.DateTimeField()
    image_evenement = models.ImageField(upload_to ='uploads/')
    membres = models.ManyToManyField(Membre, related_name="evenements")

    def __str__(self):
        return '{} {}'.format(self.titre, self.lieu)


    
