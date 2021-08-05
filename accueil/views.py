from django.shortcuts import render
from django.views import View

# Create your views here.
class Accueil(View):
    def get(self, request):
        # Créer un context pour la team
        team_raw = (
            (
                "Président",
                "Dr. Malik KONÉ",
                "Spécialiste en traitement de donnée langagière et des interfaces homme machine",
                "mkone.png",
            ),
            (
                "Secrétaire Général",
                "Dr. Wielfrid MORIÉ",
                "Spécialiste des jeux sérieux (serious games) et des interfaces homme machine",
                "wmorie.png",
            ),
            (
                "Vice-Président",
                "Ferdinand AMANVO",
                "Spécialiste réseau et optimisation",
                "famanvo.png",
            ),
            (
                "Trésorière",
                "Fatou TOKPA",
                "Spécialiste fake news et construction de la confiance sur les réseaux sociaux",
                "ftokpa.png",
            ),
            (
                "Trésorière adjointe",
                "Chimène MONSAN",
                "Spécialiste optimisation et calcul de haute fréquence",
                "cmonsan.png",
            ),
        )
        keys = ("fonction", "nom", "description", "image")
        team = (dict(zip(keys, team_member)) for team_member in team_raw)

        return render(request, "accueil/home.html", {"team": team})


def error_404_view(request, exception):
    return render(request, "accueil/error_404.html")
