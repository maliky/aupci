from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.contrib import messages

def home(request):
    return render(request, "aup_ci/index.html")

def about(request):
    return render(request, "aup_ci/about.html")

def event(request):
    return render(request, "aup_ci/event.html")

def contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # add flashmessages
            messages.add_message(request, messages.SUCCESS, "Préoccupation enrégistrée avec succès")
            # redirect to a new URL:
            return HttpResponseRedirect('/contact')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    return render(request, "aup_ci/contact.html", {'form': form})

def adhesion(request):
    return render(request, "aup_ci/adhesion.html")

