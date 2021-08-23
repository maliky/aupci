from django.shortcuts import render
from .forms import ContactForm, AdhesionForm, AbonneNewForm
from django.http import HttpResponseRedirect
from django.contrib import messages

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
        new_form = AbonneNewForm(None)
    return render(request, "aup_ci/event.html", {'newform': new_form})

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

