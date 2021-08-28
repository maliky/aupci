from django.contrib import messages
from .forms import ContactForm, AdhesionForm, AbonneNewForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

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
            # redirect to a new URL:
            return HttpResponseRedirect(httpredirect)

    # if a GET (or any other method) we'll create a blank form
    else:
        new_form = AbonneNewForm(None)
        data_dict['newform']= new_form
    return render(request, renderpage, data_dict)
