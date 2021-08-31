from django.core.mail import send_mail
from config.settings.dev import EMAIL_HOST_USER
#from config.settings.production import EMAIL_HOST_USER

def send_process_mail(sujet, html_contents, email):
    print(f"ENVOIE A {sujet} to {email}")
    return send_mail(sujet, html_contents, EMAIL_HOST_USER, [email], fail_silently=False)
           
def setting_send(queryset, data=dict()):
    if len(data) ==0:
        for q in queryset:
            q.send()
    else:
        for q in queryset:
            q.send(sujet=data["sujet"], status=data["status"])
