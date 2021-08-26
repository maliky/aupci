from django.db import models
from django.contrib.auth.models import User

class TimestampUseModel(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)
    date_Mise_a_Jour = models.DateTimeField(auto_now=True)

    class Meta:
        abstract= True

class DemandeAdhesion(TimestampUseModel):

    nom = models.CharField(max_length=150)
    prenoms = models.CharField(max_length=255)
    profession = models.CharField(max_length=250)
    entreprise= models.CharField(max_length=250)
    telephone = models.CharField(max_length=20)
    courriel = models.EmailField(unique=True, max_length=255)
    traiter = models.BooleanField(default=False)

    def __str__(self):
        return '{} {} <{}>'.format(self.prenoms, self.nom, self.courriel)


class Membre(models.Model):

    LISTE_choix = [("PR", "Président"), ("VP", "Vice-Président"), ("SG", "Sécrétaire Générale"), ("TR", "Trésorière Générale"), ("VT", "Vice-Trésorière"), ("C1", "Premier Commissaire aux comptes"), ("C2", "Second Commissaire aux comptes"), ("Mb", "Membre actif")]

    demande = models.OneToOneField(DemandeAdhesion, on_delete=models.CASCADE, primary_key=True)
    fonction = models.CharField(max_length=2, choices=LISTE_choix, default="Mb")
    date_adhesion = models.DateTimeField()

    def __str__(self):
        return '{}'.format(self.fonction)


class TypeEvenement(models.Model):
    """Type d'évènement"""
    nom = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(str(self.nom))

class Evenement(TimestampUseModel):

    #demande = models.OneToOneField(DemandeAdhesion, on_delete=models.CASCADE, primary_key=True)
    #LISTE_choix = [("HN", "Hackaton"), ("PN", "PyCon"), ("MP", "Meetup"), ("AR", "Atelier"), ("AG", "Assemblé Générale")]
    createur = models.ForeignKey(User, on_delete=models.CASCADE)
    type_evenement = models.ForeignKey(TypeEvenement, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    lieu = models.CharField(max_length=255)
    description_lieu = models.CharField(max_length=255, blank=True, null=True)
    #type_evenement = models.CharField(max_length=255)
    #type_evenement = models.CharField(max_length=2, choices=LISTE_choix, default="MP")
    description = models.TextField()
    #date_adhesion = models.DateTimeField()
    image_evenement = models.ImageField(upload_to ='uploads/img/events/')
    date_debut = models.DateTimeField(blank=True, null=True) #Date et heure de début
    date_fin = models.DateTimeField(blank=True, null=True)   # Date et heure de fin
    es_publier = models.BooleanField(blank=True, default=True)
    nombre_place = models.IntegerField(blank=True, null=True)

    def __str__(self):
        FORMAT = '%H:%M %d/%m/%Y'
        return '{} {} ; {} - {}'.format(self.titre, self.lieu, self.date_debut.strftime(FORMAT), self.date_fin.strftime(FORMAT))


class Participant(models.Model):

    nom = models.CharField(max_length=150)
    prenoms = models.CharField(max_length=255)
    profession = models.CharField(max_length=250)
    telephone = models.CharField(max_length=20)
    courriel = models.CharField(unique=True, max_length=255)
    evenements = models.ManyToManyField(Evenement, related_name="participants")

    def __str__(self):
        return '{} {} <{}>'.format(self.prenoms, self.nom, self.courriel)


class AbonneNew(models.Model):
    courriel = models.EmailField(unique=True)
    #conf_num = models.CharField(max_length=15)
    confirme_abonne = models.BooleanField(default=False)

    def __str__(self):
        return self.courriel + " (" + ("n'est pas " if not self.confirme_abonne else "est ") + "confirmé)"

#class
class Newsletter(TimestampUseModel):
    sujet = models.CharField(max_length=150)
    contenu = models.FileField(upload_to='uploads/file/newsletters/')

    def __str__(self):
        return self.sujet + " " + self.Date_creation.strftime("%B %d, %Y")

    def send(self, request):
        contents = self.contents.read().decode('utf-8')
        subscribers = AbonneNew.objects.filter(confirmed=True)
        #sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        #for sub in subscribers:
        #    message = Mail(
        #        from_email=settings.FROM_EMAIL,
        #        to_emails=sub.email,
        #        subject=self.subject,
        #        html_content=contents + (
        #            '<br><a href="{}/delete/?email={}&conf_num={}">Unsubscribe</a>.').format(
        #            request.build_absolute_uri('/delete/'),
        #            sub.email,
        #            sub.conf_num))
        #    sg.send(message)


    
