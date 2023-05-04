from django.db.models import Q
from django.shortcuts import render

from . import models
from .models import Voyage,Guide,Car

def main_part(request):
    return render(request, 'main-part.html')

def destiantion(request):
    return render(request, 'pages/destination.html')

def search_dest(request):
    if request.method == "GET":
        searched = request.GET.get('search-dest', '')  # use get() instead of indexing

        results = None

        results = models.Destination.objects.filter(
            Q(wilaya__icontains=searched) | Q(place__icontains=searched))
        print('true')

        return render(request, 'pages/search-dest.html', {'search-about': searched, 'result': results})
    else:
        return render(request, 'pages/search-dest.html')
    






def guide(request):


    if request.method == 'POST':

        date = request.POST.get('date')
        duration = request.POST.get('duration')
        unit= request.POST.get('unit')
        wilaya=request.POST.get('wilaya')
        budget=request.POST.get('budget')
        Number_of_attendees=request.POST.get('nbr_attendees')
        Guide_language=request.POST.get('language')
        Specify_your_request = request.POST.get('specify')
        accept_terms = request.POST.get('accept_terms')


    

        data=Voyage( 
                    Date_of_departure = date,
                    duration = duration ,
                    unit = unit,
                    wilaya=wilaya,
                    budget= budget,
                    Number_of_attendees=Number_of_attendees,
                    Guide_language=Guide_language,
                    Specify_your_request=Specify_your_request,
                    accept_terms=accept_terms,
            )
        



        data.save()
    return render(request, 'pages/guide.html')
        






def DevenirGuide(request):


    if request.method == 'POST':

        email = request.POST.get('email')
        phone_nbr = request.POST.get('phone_nbr')
        age = request.POST.get('age')
        sector = request.POST.get('sector')
        ln1=request.POST.get('ln1')
        ln2=request.POST.get('ln2')
        ln3=request.POST.get('ln3')
        sexe = request.POST.get('sexe')
        presentation = request.POST.get('presentation')

        profile_pic = request.FILES['profile_pic']
        identity_pic = request.FILES['identity_card']

        accept_terms = request.POST.get('accept_terms')

        data= Guide(
            email=email,
            phone_num=phone_nbr,
            age=age,
            sector=sector,
            first_language= ln1,
            second_language= ln2,
            third_language= ln3,
            sexe = sexe,
            your_presentation = presentation,
            profile_pic =  profile_pic,
            identity_pic = identity_pic,
            accept_terms = accept_terms,
        )

        data.save()


    return render(request, 'pages/DevenirGuide.html')





def covoiturage(request):



    if request.method == 'POST':



        phn_nbr= request.POST.get('phone_nbr')
        rent_from= request.POST.get('rent_from')
        rent_to=request.POST.get('rent_to')
        lisece_nbr=request.POST.get('License_nbr')
        trans=request.POST.get('transmission-select')
        fuel=request.POST.get('fuel-select')

        ident_card= request.FILES['identity_card']

        licen_pic= request.FILES['driving_license']
        
        car_pic= request.FILES['car_pic']

        notes=request.POST.get('notes')

        data=Car(

                 phone_nbr = phn_nbr,
                 rent_from=rent_from,
                 rent_to=rent_to,
                 License_nbr=lisece_nbr,
                 Transmission=trans,
                 Fuel=fuel,
                 identity_card=ident_card,
                 driving_license =licen_pic,
                 car_pic =car_pic,
                 notes=notes,
        )


        data.save()

    return render(request,'pages/form-covoiturage.html')