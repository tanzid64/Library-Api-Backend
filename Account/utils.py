from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_registration_email(subject, confirm_link, template, email_address):
    body = render_to_string(template,{'confirm_link': confirm_link})
    send_email = EmailMultiAlternatives(subject, '', to=[email_address])
    send_email.attach_alternative(body, 'text/html')
    send_email.send()