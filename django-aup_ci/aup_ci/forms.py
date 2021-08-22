from django import forms
from django.forms import  ModelForm, TextInput, EmailInput
from .models import DemandeAdhesion

class ContactForm(forms.Form):
    nom = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Nom*', 'class': 'check-form'}))
    prenoms = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Prenom(s)*', 'class': 'check-form'}))
    courriel = forms.CharField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email*', 'class': 'check-form'}))
    telephone = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Téléphone*', 'class': 'check-form'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Préoccupation*'}))



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