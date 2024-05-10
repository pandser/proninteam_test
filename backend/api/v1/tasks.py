from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email(theme, body, recipient):
    send_mail(theme, body, None, recipient)
