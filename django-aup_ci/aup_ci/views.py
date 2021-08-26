from django.shortcuts import render
from .forms import ContactForm, AdhesionForm, AbonneNewForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone
from django.db import models
from django.db.models import F, Q
from .models import Evenement

def home(request):
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
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        new_form = AbonneNewForm(None)
    return render(request, "aup_ci/index.html", {'newform': new_form})

def about(request):
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
            # redirect to a new URL:
            return  HttpResponseRedirect('/about')

    # if a GET (or any other method) we'll create a blank form
    else:
        new_form = AbonneNewForm(None)
    return render(request, "aup_ci/about.html", {'newform': new_form})

def event(request):
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
            # redirect to a new URL:
            return HttpResponseRedirect('/event')

    # if a GET (or any other method) we'll create a blank form
    else:
        # Gérer l'affichage des événements ici
        # Une section pour l'affichage des événèments à venir, et une section pour les évènements passés
        now = timezone.now()
        evenements=(Evenement.objects.annotate(
            relevance=models.Case(
                models.When(date_debut__gte=now, then=1),
                models.When(date_debut__lt=now, then=2),
                output_field=models.IntegerField(),
            )).annotate(
            timediff=models.Case(
                models.When(date_debut__gte=now, then=F('date_creation') - now),
                models.When(date_debut__lt=now, then=now - F('date_creation')),
                output_field=models.DurationField(),
            )).order_by('relevance', 'timediff'))#.filter(relevance=1)
        aVenir = []
        passer = []
        for evenement in evenements:
            if evenement.date_debut >= now:
                aVenir.append(evenement)
            else:
                passer.append(evenement)
        print(aVenir)
        print(passer)
        new_form = AbonneNewForm(None)
    return render(request, "aup_ci/event.html", {'newform': new_form, 'event_aVenir': aVenir, 'event_passer': passer})


def show_event(request, event_id=0):
    if event_id == 0:
        return HttpResponseRedirect('/event')
    else:
        print("ID_EVENT={} de Type".format(event_id, type(event_id)))
        new_form = AbonneNewForm(None)
        return  render(request, "aup_ci/eventDetail.html", {'newform': new_form})



def contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if "contact" in request.POST:
            # create a form instance and populate it with data from the request:
            contact_form = ContactForm(request.POST)
            # check whether it's valid:
            if contact_form.is_valid():
                # process the data in form.cleaned_data as required
                # Save in the data base
                contact_form.save()
                # add flashmessages
                messages.add_message(request, messages.SUCCESS,
                                     "Votre demande d'abonnement à notre newsletter a été enregistrée et sera traitée")
                # redirect to a new URL:
                return HttpResponseRedirect('/contact')
        elif "abonne" in request.POST:
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
                # redirect to a new URL:
                return HttpResponseRedirect('/contact')

    # if a GET (or any other method) we'll create a blank form
    else:
        contact_form = ContactForm(None)
        new_form = AbonneNewForm(None)
    return render(request, "aup_ci/contact.html", {'contactform': contact_form, 'newform': new_form})


def adhesion(request):
    # if this is a POST request we need to process the form data
    #adhere_form = AdhesionForm(None)
    #new_form  = AbonneNewForm(None)
    if request.method == 'POST':
        if "adhere" in request.POST:
            # create a form instance and populate it with data from the request:
            adhere_form = AdhesionForm(request.POST)
            # check whether it's valid:
            if adhere_form.is_valid():
                # process the data in form.cleaned_data as required
                # Save in the data base
                adhere_form.save()
                # add flashmessages
                messages.add_message(request, messages.SUCCESS,
                                     "Votre demande d'adhesion a été enregistrée et sera traitée")
                # redirect to a new URL:
                return HttpResponseRedirect('/adhesion')
        elif "abonne" in request.POST:
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
                # redirect to a new URL:
                return HttpResponseRedirect('/adhesion')

    # if a GET (or any other method) we'll create a blank form
    else:
        adhere_form = AdhesionForm(None)
        new_form = AbonneNewForm(None)
    return render(request, "aup_ci/adhesion.html", {'adhereform': adhere_form, 'newform': new_form})

