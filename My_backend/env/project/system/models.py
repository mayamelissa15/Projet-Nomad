from django.db import models

# Create your models here.


x=[
    ('accepted','accepted'),
    ('refused','refused'),
    ('waiting','waiting'),
]

class Trip(models.Model):
    owner = models.CharField(max_length=50)
    owner_email= models.EmailField(max_length=50)
    nbr_persons = models.IntegerField()
    Specification=models.TextField(max_length=50,null=True)
    status= models.CharField(max_length=50, choices=x, default='waiting')

