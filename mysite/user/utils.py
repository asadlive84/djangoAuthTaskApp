from django.core.mail import send_mail
from mysite.settings import EMAIL_HOST_USER
from .models import CustomUser

def welcome_email(email):
    subject = 'Test mail: Thanks for sigup'
    message = f'Hi {email}, thank you for registering in django app- Asaduzzaman Sohel. this is test mail'
    email_from = EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail(subject, message, email_from, recipient_list)


def email_check(email):
    mailExist  = []
    mailExist = CustomUser.objects.filter(email=email)
    if len(mailExist)>0:
        return True
    return False
    