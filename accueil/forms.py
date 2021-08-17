from django.forms import ModelForm
from accueil.models import Adherent

class AdherentForm(ModelForm):
    class Meta:
        model = Adherent
        fields = ['nom', 'prenom', 'numero_telephone', 'courriel', 'occupation']
