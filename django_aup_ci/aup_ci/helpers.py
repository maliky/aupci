from django.contrib import messages
from .forms import  AbonneNewForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from config.settings import base
#from .models import *
from .util import send_process_mail

def base_navigue_view(request, renderpage="aup_ci/index.html", httpredirect="/", data_dict=dict()):
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        new_form = AbonneNewForm(request.POST)
        # check whether it's valid:
        if new_form.is_valid():
            # process the data in form.cleaned_data as required
            # Save in the data base
            new_form.save()
            # add flashmessages
            messages.add_message(request, messages.SUCCESS,
                                     "Votre demande d'abonnement à notre newsletter a été enregistrée et sera traitée")
            # Envoie de mail à l'administrateur
            alerte_admin(new_form)
            # redirect to a new URL:
            return HttpResponseRedirect(httpredirect)

    # if a GET (or any other method) we'll create a blank form
    else:
        new_form = AbonneNewForm(None)
        data_dict['newform']= new_form
    return render(request, renderpage, data_dict)

def alerte_admin(new_form):
    # Envoie de mail à l'administrateur
    sujet = "NOUVELLE DEMANDE_NEWSLETTER_AUPCI DE {}, ".format(new_form.cleaned_data["courriel"])
    html_contents = " Une nouvelle demande d'abonnement est enregistrée"
    email = "aup.ci@gmail.com"
    send_process_mail(sujet, html_contents, email)

