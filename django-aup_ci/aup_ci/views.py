from django.shortcuts import render

def home(request):
    return render(request, "aup_ci/index.html")

def about(request):
    return render(request, "aup_ci/about.html")

def event(request):
    return render(request, "aup_ci/event.html")

def contact(request):
    return render(request, "aup_ci/contact.html")

def adhesion(request):
    return render(request, "aup_ci/adhesion.html")

