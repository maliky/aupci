"""aup_ci URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

admin.site.site_header = 'AUP-CI ADMIN'                    # default: "Django Administration"
admin.site.index_title = 'BIENVENUE AU PORTAIL AUP-CI ADMIN'                 # default: "Site administration"
admin.site.site_title = 'PORTAIL AUP-CI ADMIN' # default: "Django site admin"

app_name = 'aup_ci'
urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('event/<int:page>', views.event, name="event"),
    path('event/avenir/<int:event_id>', views.show_event_Avenir, name="venir_event_show"),
    path('event/passe/<int:event_id>', views.show_event_Passer, name="passe_event_show"),
    path('event/participant/', views.show_event_Passer, name="passe_event_show"),
    path('contact', views.contact, name="contact"),
    path('adhesion', views.adhesion, name="adhesion"),
    path('admin/', admin.site.urls),
]
