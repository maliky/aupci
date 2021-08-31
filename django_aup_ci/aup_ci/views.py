from django.shortcuts import render, get_object_or_404
#from django.shortcuts import get_object_or_404
from .forms import ContactForm, AdhesionForm, AbonneNewForm, ParticiperForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone
from django.db import models
from django.db.models import F, Q
from .models import Evenement, Membre
from .helpers import base_navigue_view, alerte_admin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .util import send_process_mail

def home(request):
   render_page = "aup_ci/index.html"
   http_redirect = "/"
   now = timezone.now()
   plus_proche = Evenement.objects.filter(date_debut__gte=now).order_by('date_debut').first()
   membres = Membre.objects.all()
   nombre_membre = 0
   if len(list(membres)) > 0:
       nombre_membre = len(list(membres))
   #print(evenement_avenir)

  #   plus_proche = list(evenement_avenir)[0]    if len(evenement_avenir)!=0 else []

   #print(plus_proche)
   data = {'evenement': plus_proche, 'nombre_membre': nombre_membre}
   http_response = base_navigue_view(request, render_page, http_redirect, data)
   return http_response

def about(request):
    render_page = "aup_ci/about.html"
    http_redirect = "/about"
    membres = Membre.objects.all()
    nombre_membre = 0
    if len(list(membres)) > 0:
        nombre_membre = len(list(membres))
    data = {'nombre_membre': nombre_membre}
    http_response= base_navigue_view(request, render_page, http_redirect, data)
    return  http_response

def event(request, page=1):
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
            return HttpResponseRedirect('/event/'+str(page))

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
        #print(aVenir)
        #print(passer)
        #page_number = request.GET.get('page')
        page_number = page
        print("PAGE NUMBER", page_number)
        paginator = Paginator(passer, 1)  # Show 25 contacts per page.
        try:
            past_events = paginator.get_page(page_number)
        except PageNotAnInteger:
            past_events = paginator.get_page(1)
        except EmptyPage:
            past_events = paginator.get_page(paginator.num_pages)
        print("PastEvent", past_events )
        new_form = AbonneNewForm(None)
    return render(request, "aup_ci/event.html", {'newform': new_form, 'event_aVenir': aVenir, 'event_passer': past_events})


def show_event_Passer(request, event_id=0):
    if event_id == 0:
        return HttpResponseRedirect('/event')
    else:
        #print("ID_EVENT={} de Type".format(event_id, type(event_id)))
        evenement = get_object_or_404(Evenement, pk=event_id)
        now = timezone.now()
        es_a_venir = 1
        if evenement.date_debut < now:
            es_a_venir = 0
            #new_form = AbonneNewForm(None)
            render_page = "aup_ci/eventDetail.html"
            http_redirect = '/event/passe/'+str(event_id)
            data = {'evenement': evenement, 'es_a_venir': es_a_venir}
            httpresponse = base_navigue_view(request, render_page, http_redirect, data)
            return httpresponse
        else:
            return HttpResponseRedirect('/event/avenir/'+str(event_id))

        #return  render(request, "aup_ci/eventDetail.html", {'newform': new_form})


def show_event_Avenir(request, event_id=0):
    if event_id == 0:
        return HttpResponseRedirect('/event')
    else:
        #print("ID_EVENT={} de Type".format(event_id, type(event_id)))
        evenement = get_object_or_404(Evenement, pk=event_id)
        now = timezone.now()
        es_a_venir = 0
        if evenement.date_debut > now:
            es_a_venir = 1
            if request.method == 'POST':
                if "detail_event" in request.POST:
                    # create a form instance and populate it with data from the request:
                    other_form = ParticiperForm(request.POST)
                    # check whether it's valid:
                    if other_form.is_valid():
                        # process the data in form.cleaned_data as required
                        # Envoyer un email à l'administrateur
                        sujet = "PARTICIPATION_AUPCI A '{}' DE {} MOTIF{}".format(evenement.titre, other_form.cleaned_data["courriel"],
                                                                  other_form.cleaned_data["motif"])
                        html_contents = other_form.cleaned_data["message"]
                        email = "aup_ci@gmail.com"
                        # print(sujet, html_contents, email)
                        send_process_mail(sujet, html_contents, email)
                        # add flashmessages
                        messages.add_message(request, messages.SUCCESS,
                                             "Votre demande de participation a été enregistrée et sera traitée")
                        # redirect to a new URL:
                        return HttpResponseRedirect('/event/avenir/'+str(event_id))
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
                        # Envoie de mail à l'administrateur
                        alerte_admin(new_form)
                        # redirect to a new URL:
                        return HttpResponseRedirect('/event/avenir/'+str(event_id))
            else:
                render_page = "aup_ci/eventDetail.html"
                http_redirect = '/event/avenir/'+str(event_id)
                form_event = ParticiperForm(None)
                data = {'evenement': evenement, 'es_a_venir': es_a_venir, 'event_form': form_event}
                httpresponse = base_navigue_view(request, render_page, http_redirect, data)
                return httpresponse
        else:
            return HttpResponseRedirect('/event/passe/'+str(event_id))

        #new_form = AbonneNewForm(None)
        #return  render(request, "aup_ci/eventDetail.html", {'newform': new_form})



def contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if "contact" in request.POST:
            # create a form instance and populate it with data from the request:
            contact_form = ContactForm(request.POST)
            # check whether it's valid:
            if contact_form.is_valid():
                # process the data in form.cleaned_data as required
                #Envoyer un mail
                sujet = "CONTACT_AUPCI DE {} {}".format(contact_form.cleaned_data["nom"], contact_form.cleaned_data["prenoms"])
                html_contents = contact_form.cleaned_data["message"]
                email = "contact@aup.ci"
                #print(sujet, html_contents, email)
                send_process_mail(sujet, html_contents, email)
                #exit(0)
                # add flashmessages
                messages.add_message(request, messages.SUCCESS,
                                     "Votre préoccupation a été enregistrée et sera traitée rapidement")
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

                # Envoie de mail à l'administrateur
                alerte_admin(new_form)
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
                # Message de signalement de nouvel adhérent
                sujet = "NOUVELLE DEMANDE_ADHESION_AUPCI DE {} {} {}, ".format(adhere_form.cleaned_data["nom"],
                                                          adhere_form.cleaned_data["prenoms"], adhere_form.cleaned_data["courriel"])
                html_contents = " Une nouvelle demande d'adhesion est enregistrée"
                email = "aup.ci@gmail.com"
                send_process_mail(sujet, html_contents, email)
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
                # Envoie de mail à l'administrateur
                alerte_admin(new_form)
                # redirect to a new URL:
                return HttpResponseRedirect('/adhesion')

    # if a GET (or any other method) we'll create a blank form
    else:
        adhere_form = AdhesionForm(None)
        new_form = AbonneNewForm(None)
    return render(request, "aup_ci/adhesion.html", {'adhereform': adhere_form, 'newform': new_form})



