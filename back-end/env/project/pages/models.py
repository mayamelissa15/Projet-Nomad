from django.db import models

# Create your models here.
class Destination(models.Model):
    wilaya = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
