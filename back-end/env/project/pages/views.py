from django.db.models import Q
from django.shortcuts import render
from . import models

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

        return render(request, 'pages/dest-search.html', {'searchabout': searched, 'result': results})
    else:
        return render(request, 'pages/dest-search.html')

