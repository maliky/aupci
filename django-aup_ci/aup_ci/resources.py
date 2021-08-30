from import_export import resources
from .models import Membre, DemandeAdhesion
class MembreResource(resources.ModelResource):
    class Meta:
        model = Membre
        fields = ('demande__nom', 'demande__prenoms', 'demande__courriel', 'role', 'demande__profession', 'date_adhesion')
        export_order= ('demande__nom', 'demande__prenoms', 'role', 'date_adhesion', 'demande__profession', 'demande__courriel')
        widgets = {
            'date_adhesion': {'format': '%d.%m.%Y'},
        }