from django.urls import path
from . import views

urlpatterns = [
 
    path('MyAccount', views.accept, name='MyAccount'),
    

]