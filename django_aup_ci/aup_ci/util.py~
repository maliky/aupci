
def send_process_mail(sujet, html_contents, email):
    print("ENVOIE A PARAMETRER")
    # sg = SendGridAPIClient(base.SENDGRID_API_KEY)
        #message = Mail( from_email=settings.FROM_EMAIL,
        #        to_emails=email,
        #        subject=sujet,
        #        html_content=contents)
        #    sg.send(message)
def setting_send(queryset, data=dict()):
    if len(data) ==0:
        for q in queryset:
            q.send()
    else:
        for q in queryset:
            q.send(sujet=data["sujet"], status=data["status"])