from django.contrib import  admin
from .models import  DemandeAdhesion, Membre, Evenement, AbonneNew, Newsletter, TypeEvenement, Participant
from django import forms
from .util import setting_send
from django.db.models.functions import Lower

#admin.site.site_header = "AUP-CI ADMIN"

class NewsletterAdmin(admin.ModelAdmin):
    model = Newsletter
    actions = ["send_newsletter"]
    list_display = ("sujet", "date_creation")

    def get_ordering(self, request):
        return ['date_creation']  # sort case insensitive

    def send_newsletter(self, request, queryset):
        setting_send(queryset)

    send_newsletter.short_description = "Envoyer les newsletters selections aux abonnées"

class DemandeAdhesionAdmin(admin.ModelAdmin):
    model = DemandeAdhesion
    actions = ["accepter_demande", "refuser_demande"]
    list_display = ("nom", "prenoms", "courriel", "traiter", "confirme_adhesion")
    #list_display = ("nom", "prenoms", "courriel", "traiter", "is_confirmed")
    readonly_fields = ("traiter", "confirme_adhesion")

    def get_ordering(self, request):
        return ['traiter']

    #@admin.display(boolean=True)
    #def is_confirmed(self, obj):
        #return obj.confirme_adhesion

    #is_confirmed.boolean = True
    #is_confirmed.admin_order_field = 'confirme_adhesion'
    #is_confirmed.short_description = 'Adhesion confirmée?'

    def accepter_demande(self, request, queryset):
        queryset.update(traiter=True)
        queryset.update(confirme_adhesion=True)
        data = {"sujet": "Acceptation de la demande d'adhésion", "status": "accepter"}
        setting_send(queryset, data)

    def refuser_demande(self, request, queryset):
        queryset.update(traiter=True)
        queryset.update(confirme_adhesion=False)
        data = {"sujet": "Refus de la demande d'adhésion", "status": "accepter"}
        setting_send(queryset, data)


    refuser_demande.short_description = "Refuser demande(s)"
    accepter_demande.short_description = "Accepter demande(s)"


class AbonneNewAdmin(admin.ModelAdmin):
    model = AbonneNew
    actions = ["accepter_demande", "refuser_demande"]
    list_display = ("courriel", "traiter", "confirme_abonne")
    readonly_fields = ("traiter", "confirme_abonne")

    def get_ordering(self, request):
        return ['traiter']



    def accepter_demande(self, request, queryset):
        queryset.update(traiter=True)
        queryset.update(confirme_abonne=True)
        data = {"sujet": "Acceptation de la demande d'abonnement", "status": "accepter"}
        setting_send(queryset, data)

    def refuser_demande(self, request, queryset):
        queryset.update(traiter=True)
        queryset.update(confirme_abonne=False)
        #print("QUERYSET", queryset)
        data = {"sujet": "Refus de la demande d'abonnement", "status": "refuser"}
        setting_send(queryset, data)

    refuser_demande.short_description = "Refuser demande(s)"
    accepter_demande.short_description = "Accepter demande(s)"


class MembreAdmin(admin.ModelAdmin):
    model = Membre
    list_display = ("nom","prenoms", "courriel", "role", "profession")

    def nom(self, obj):
        adherant = obj.demande
        return adherant.nom

    def prenoms(self, obj):
        adherant = obj.demande
        return adherant.prenoms

    def courriel(self, obj):
        adherant = obj.demande
        return adherant.courriel

    def profession(self, obj):
        adherant = obj.demande
        return adherant.profession


    nom.short_description = 'nom'
    prenoms.short_description = 'prenoms'
    courriel.short_description = "courriel"
    profession.short_description = "profession"

    nom.admin_order_field = 'nom'

    #def get_ordering(self, request):
        #return ['demande', 'role']



    def formfield_for_dbfield(self, db_field, request, **kwargs):
        #user = kwargs['request'].user
        #print("DB_FIELD", db_field)
        if db_field.name == "demande":
            #kwargs['initial'] = user.default_company
            qs = DemandeAdhesion.objects.filter(confirme_adhesion=True)
            print("qs", qs)
            return forms.ModelChoiceField(queryset=qs, **kwargs)
        return super(MembreAdmin, self).formfield_for_dbfield(db_field, request, **kwargs)


class EvenementAdmin(admin.ModelAdmin):
    model = Evenement
    list_display = ("titre", "date_debut", "date_fin")
    def get_ordering(self, request):
        return ['-date_debut']

class TypeEvenementAdmin(admin.ModelAdmin):
    model = TypeEvenement
    list_display = ("nom",)
    def get_ordering(self, request):
        return ['nom']



admin.site.register(DemandeAdhesion, DemandeAdhesionAdmin)
admin.site.register(Membre, MembreAdmin)
admin.site.register(Evenement, EvenementAdmin)
admin.site.register(TypeEvenement, TypeEvenementAdmin)
#admin.site.register(Participant)
admin.site.register(AbonneNew, AbonneNewAdmin)
admin.site.register(Newsletter, NewsletterAdmin)