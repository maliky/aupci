from django.contrib import  admin
from .models import  DemandeAdhesion, Membre, Evenement, AbonneNew, Newsletter, TypeEvenement, Participant

def send_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        newsletter.send(request)

send_newsletter.short_description = "Send selected Newsletters to all subscribers"


class NewsletterAdmin(admin.ModelAdmin):
    actions = [send_newsletter]



admin.site.register(DemandeAdhesion)
admin.site.register(Membre)
admin.site.register(Evenement)
admin.site.register(TypeEvenement)
admin.site.register(Participant)
admin.site.register(AbonneNew)
admin.site.register(Newsletter, NewsletterAdmin)