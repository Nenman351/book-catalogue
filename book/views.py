from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render


# Create your views here.
# def playground(request):
#     send_mail('test', 'this email is send from django', '', ['nenman.willams@gmail.com'])
#     return HttpResponse('email sent')

def playground(request):
    try:
        message = EmailMessage('testing email', 'this email is send from django', 'admin@gmail.com', ['nenman.willams@gmail.com'])
        message.send()
    except BadHeaderError:
        pass
    return HttpResponse('email sent')
