from django.shortcuts import render
from .models import Trip
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.


def accept(request):

    trips = Trip.objects.all()
    z = {'aw': trips}

    if request.method == 'POST':
        trip_id = request.POST.get('trip_id')
        trip=Trip.objects.get(id=trip_id)

        if 'accept' in request.POST:
            # send acceptance email

                email_msg = EmailMessage(
                    'Trip accepted',
                    'Hi there! Your trip has been accepted.',
                    settings.EMAIL_HOST_USER,
                    [trip.owner_email],
                )

                email_msg.fail_silently = True
                email_msg.send() 
                trip.status='accepted'
                trip.save()
                

            



        elif 'refuse' in request.POST:
                # send refusal email

                email_msg = EmailMessage(
                    'Trip refused',
                    'Hi there! Your trip has been refused.',
                    settings.EMAIL_HOST_USER,
                    [trip.owner_email],
                )

                email_msg.fail_silently = True
                email_msg.send()
                trip.status='refused'
                trip.save()





    return render(request, 'system/MyAccount.html',z) 
