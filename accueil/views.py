from django.shortcuts import render
from django.views import View

# Create your views here.
class Accueil(View):
    def get(self, request):
        # contexte pour les pages
        return render(request, "accueil/home.html")

def error_404_view(request, exception):
    return render(request, "accueil/error_404.html")

