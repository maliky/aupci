from django import forms
from django.forms import ModelForm
from accueil.models import DemandeAdhesion


class ContactForm(forms.Form):
    lastname = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Nom*", "class": "check-form"}),
    )
    firstname = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Prenom(s)*", "class": "check-form"}
        ),
    )
    email = forms.CharField(
        label="",
        widget=forms.EmailInput(attrs={"placeholder": "Email*", "class": "check-form"}),
    )
    phone = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Téléphone*", "class": "check-form"}
        ),
    )
    message = forms.CharField(
        label="", widget=forms.Textarea(attrs={"placeholder": "Préoccupation*"})
    )


class AdherentForm(ModelForm):
    class Meta:
        model = DemandeAdhesion
        fields = ["nom", "prenoms", "telephone", "courriel", "profession", "entreprise"]
