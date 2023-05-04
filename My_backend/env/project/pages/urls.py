from django.urls import path
from . import views

urlpatterns = [
    path('', views.destiantion, name='main_part'),
    path('Destination', views.destiantion, name='destination'),
    path('Search', views.search_dest, name='search-dest'),
    path('guide',views.guide, name='guide'),
    path('DevenirGuide',views.DevenirGuide, name='DevenirGuide'),
    path('covoiturage',views.covoiturage, name='covoiturage'),

]
