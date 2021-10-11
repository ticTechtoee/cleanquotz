from django.shortcuts import render
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings


def index(request):

    # create a variable to keep track of the form
    messageSent = False

    # check if form has been submitted
    if request.method == 'POST':

        form = EmailForm(request.POST)

        # check if data from the form is clean
        if form.is_valid():
            cd = form.cleaned_data
            subject = "Email from Cleanquotz"
            greetings = "Hello "
            fName = cd['first_name']
            
            message = "We have Received your Query and we will contact you as soon as possible"
            
            # send the email to the recipent
            send_mail(subject, greetings + "Mr " + fName +" "+ message,
                      settings.DEFAULT_FROM_EMAIL, [cd['recipient']])


            cd = form.cleaned_data
            subject = "Email from "
            fName = cd['first_name']
            
            message = cd['message']
            recipient = cd['recipient']
            # send the email to the recipent
            send_mail(subject + fName + " ", message + "\nReply back at " + recipient,
                      settings.DEFAULT_FROM_EMAIL, ['cleanquotz@gmail.com'])

            # set the variable initially created to True
            messageSent = True

    else:
        form = EmailForm()

    return render(request, 'contact/index.html', {

        'form': form,
        'messageSent': messageSent,

    })