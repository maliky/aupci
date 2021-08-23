from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import handler404

app_name = "aup_ci"
urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("adhesion", views.Adhesion.as_view(), name="adhesion"),
    path("about", views.about, name="about"),
    path("event", views.event, name="event"),
    path("contact", views.contact, name="contact"),
    path("admin/", admin.site.urls),
]

handler404 = "accueil.views.error_404_view"
