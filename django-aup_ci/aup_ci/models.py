from django.db import models
from django.contrib.auth.models import User
from .util import send_process_mail

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
    confirme_adhesion = models.BooleanField(default=False)
    est_associe = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return '{} {} <{}>'.format(self.prenoms, self.nom, self.courriel)

    def send(self, **kwargs):
        sujet = kwargs["sujet"]
        status = kwargs["status"]
        contents = "Bonjour !, votre demande d'adhésion a été acceptée. Bienvenue dans la grande famille des utilisateurs Python de Côte d'Ivoire. Veuillez visiter regulièrement notre site pour ne rien rater!!!<br> Cordialement."
        if status == "refuser":
            contents = "Bonjour !, votre demande d'adhésion à l'AUP ne peut être acceptée. Vous pouvez nous contacter sur notre site web pour plus d'informations sur les raisons de notre refus. <br> Cordialement."
        print("Envoie de mail satut adhésion effectué")
        html_content = contents
        send_process_mail(sujet, html_content, self.courriel)



class Membre(models.Model):

    LISTE_choix = [("PR", "Président"), ("VP", "Vice-Président"), ("SG", "Sécrétaire Générale"), ("TR", "Trésorière Générale"), ("VT", "Vice-Trésorière"), ("C1", "Premier Commissaire aux comptes"), ("C2", "Second Commissaire aux comptes"), ("Mb", "Membre actif")]

    demande = models.OneToOneField(DemandeAdhesion, on_delete=models.CASCADE, primary_key=True)
    role = models.CharField(max_length=2, choices=LISTE_choix, default="Mb")
    date_adhesion = models.DateTimeField()

    def __str__(self):
        return '{} {}; courriel={}; role= {}'.format(self.demande.nom, self.demande.prenoms, self.demande.courriel, self.role)


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
    traiter = models.BooleanField(default=False)

    def __str__(self):
        return self.courriel + " (" + ("n'est pas " if not self.confirme_abonne else "est ") + "confirmé)"

    def send(self, **kwargs):
        sujet  = kwargs["sujet"]
        status = kwargs["status"]
        contents = "Bonjour !, votre demande d'abonnement a été acceptée. <br> A très bientôt pour des news!!!<br> Cordialement."
        if status == "refuser":
            contents = "Bonjour !, votre demande d'abonnement n'a pas été acceptée. Vous pouvez nous contacter sur notre site web pour plus d'informations sur les raisons de notre refus. <br> Cordialement."
        print("Envoie de mail satut abonnement effectué")
        html_content = contents
        print("JUSTE AVANT ENVOIE")
        #exit(0)
        send_process_mail(sujet, html_content, self.courriel)

#class
class Newsletter(TimestampUseModel):
    sujet = models.CharField(max_length=150)
    contenu = models.FileField(upload_to='uploads/file/newsletters/')

    def __str__(self):
        return self.sujet + " " + self.date_creation.strftime("%B %d, %Y")

    def send(self):
        contents = ""
        try:
            contents = self.contenu.read().decode("utf-8")
        except:
            contents = self.contenu.read().decode("latin-1")

        abonnes = AbonneNew.objects.filter(confirme_abonne=True)
        print("Liste des abonnées", abonnes)
        print("Envoie de la newsletter effectué")
        #sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        for abonne in abonnes:
            pass
            #    html_content = contents + (
            #            '<br><a href="{}/delete/?courriel={}">Désabonnez</a>.').format(
            #            request.build_absolute_uri('/delete/'),
            #            abonne.courriel,)
            # send_process_mail(self.sujet, html_content, self.courriel)



    
