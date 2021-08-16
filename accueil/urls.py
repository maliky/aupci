from django.urls import path
from . import views
from django.conf.urls import handler404

app_name = 'accueil'

urlpatterns = [
    path('', views.Accueil.as_view(), name='accueil'),
    path('accueil', views.Accueil.as_view(), name='accueil'),
]

handler404 = 'accueil.views.error_404_view'
