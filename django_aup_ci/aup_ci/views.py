from django.shortcuts import render
from django.views import View
from .forms import ContactForm, AdherentForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail


def about(request):
    return render(request, "aup_ci/about.html")


def event(request):
    return render(request, "aup_ci/event.html")


def contact(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # add flashmessages
            messages.add_message(
                request, messages.SUCCESS, "Préoccupation enrégistrée avec succès"
            )
            # redirect to a new URL:
            return HttpResponseRedirect("/contact")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    return render(request, "aup_ci/contact.html", {"form": form})


class Home(View):
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

        return render(request, "aup_ci/home.html", {"team": team})


class Adhesion(View):
    def get(self, request):
        form = AdherentForm()
        context = {"formulaire_adherent": form, "Titre": "Page d'adéhsion"}
        return render(request, "aup_ci/adhesion.html", context)

    def post(self, request):
        # juste un exemple d'action
        send_mail(
            "Subject here",
            "Here is the message.",
            "malikykone@gmail.com",
            ["malikykone@gmail.com"],
            fail_silently=False,
        )
        return request


def error_404_view(request, exception):
    return render(request, "aup_ci/error_404.html")
