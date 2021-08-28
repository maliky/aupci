from django import forms
from django.forms import  ModelForm, TextInput, EmailInput
from .models import DemandeAdhesion, AbonneNew

class ContactForm(forms.Form):
    nom = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Nom*', 'class': 'check-form'}))
    prenoms = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Prenom(s)*', 'class': 'check-form'}))
    courriel = forms.CharField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email*', 'class': 'check-form'}))
    telephone = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Téléphone*', 'class': 'check-form'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Préoccupation*'}))


class ParticiperForm(forms.Form):
    choix = [("sp", "Simple participant"), ("pt", "Présentateur"), ("cr", "Compétiteur à Hackathon"), ("pe", "Partenaire, sponsor"), ("ar", "Annonceur")]
    motif = forms.ChoiceField(label="Participer en qualité de* :", choices=choix, required=True)

    #forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Nom*', 'class': 'check-form'}))
    courriel = forms.CharField(label='Email* :', widget=forms.EmailInput(attrs={'placeholder': 'ex: toto@gmail.com', 'class': 'check-form'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': "Laissez-nous plus de précisions, vous recevrez plus d'informations*"}))



class AdhesionForm(ModelForm):

    class Meta:
        # specify model to be used
        model = DemandeAdhesion
        # specify that form must use all fields of the model
        #fields = ["nom", "prenoms", "profession", "telephone", "entreprise", "courriel"]
        #fields = "__all__"
        exclude = ['traiter']
        labels = {'nom': '', 'prenoms':'', 'profession' : '', 'telephone' : '', 'entreprise' : '', 'courriel' : ''}
        widgets ={
            "nom": TextInput(attrs={'placeholder': 'Nom* :', 'class': 'check-form'}),
            "prenoms": TextInput(attrs={'placeholder': 'Prénoms* :', 'class': 'check-form'}),
            "profession": TextInput(attrs={'placeholder': 'Profession* :', 'class': 'check-form'}),
            "telephone": TextInput(attrs={'placeholder': 'Telephone* :', 'class': 'check-form'}),
            "entreprise": TextInput(attrs={'placeholder': 'Entreprise* :', 'class': 'check-form'}),
            "courriel": EmailInput(attrs={'placeholder': 'Email* :', 'class': 'check-form'}),
        }


class AbonneNewForm(ModelForm):

    class Meta:
        model = AbonneNew
        exclude = ["confirme_abonne"]
        labels = {"courriel": "",}
        widgets = {
            "courriel": EmailInput(attrs={'placeholder': 'Courriel (ex: xxxxxx@gmail.com)'}),
        }