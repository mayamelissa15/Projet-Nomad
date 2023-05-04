from django.db import models

# Create your models here.
class Destination(models.Model):
    wilaya = models.CharField(max_length=50)
    place = models.CharField(max_length=50)



x=[
    ('Alger','Alger'),
    ('Oran','Oran'),
    ('Timimoune','Timimoune'),
    ('Setif','Setif'),
    ('Bejaia','Bejaia'),
    ('Constantine','Constantine'),
]

y=[
    ('1 person','1 person'),
    ('2 person','2 person'),
    ('3 person','3 person'),
    ('4 person','4 person'),
    ('5 person','5 person'),
    ('6 person','6 person'),
    ('7 person','7 person'),
    ('8 person','8 person'),
    ('9 person','9 person'),
    ('+ 10 person','+ 10 person'),
    ('+ 20 person','+ 20 person'),

]


z=[
   ('Kabyle','Kabyle'),
   ('Arabe', 'Arabe'),
   ('Arabe(Darija)','Arabe(Darija)'),
   ('Francais','Francais'),
   ('Anglais','Anglais'),
   ('Espagnol','Espagnol'),
   ('Mandarin','Mandarin'),
   ]

t=[('on','on'),
('off','off'),]




class Voyage(models.Model):
    Date_of_departure = models.DateField(null=False)
    duration = models.IntegerField(null=False)

    unit = models.CharField(max_length=50,null=False,choices=[
        ('Hour(s)','Hour(s)'),
        ('Day(s)','Day(s)'),
    ]  )

    wilaya = models.CharField(max_length=50,null=False, choices=x)

    budget = models.IntegerField(null=False)

    Number_of_attendees= models.CharField(max_length=50 ,null=False,choices=y)  

    Guide_language= models.CharField(null=False,max_length=50,choices=z)

    Specify_your_request = models.CharField(max_length=60,null=False)  

    accept_terms = models.CharField(max_length=50,null=False,default='off',choices=t)






class Guide(models.Model):

    
    email = models.EmailField(max_length=50,null = False)

    phone_num= models.CharField(max_length=50,null = False)

    age = models.IntegerField( null = False)

    sector = models.CharField(max_length=50,null = False, choices=x)

    first_language= models.CharField(max_length=50,null = False)

    second_language= models.CharField(max_length=50,null=False)

    third_language= models.CharField(max_length=50,null=True,blank=True)

    sexe = models.CharField(max_length=50,null=False, choices= [('F','femme'),('M','homme')])
    
    your_presentation = models.CharField(max_length=50,null=False)

    profile_pic = models.ImageField(upload_to='profile_pics/%y/%m/%d' , default= 'static/img/avatar.png',null=True) #recuperer l'image men imagefield et l'afficher dans templates. 

    identity_pic= models.ImageField(upload_to='identity_pics/%y/%m/%d',null=True)  

    accept_terms = models.CharField(max_length=50,null=False,default='off',choices=t)





class Car(models.Model):

    phone_nbr=models.CharField(max_length=50,null=False)

    rent_from=models.DateField(null=False)

    rent_to=models.DateField(null=False)

    License_nbr=models.CharField(max_length=50,null=False)


    Transmission=models.CharField(max_length=50,choices=[('Automatic','Automatic'), ('Manual','Manual') ])

    Fuel = models.CharField(max_length=50 , choices=[('Essence','Essence'),('Diesel','Diesel'),('Electricity','Electricity')])

    identity_card = models.ImageField(upload_to='identitypics_cars/%y/%m/%d',null=True)
    
    driving_license = models.ImageField(upload_to='driving_license/%y/%m/%d',null=True)

    car_pic = models.ImageField(upload_to='cars_pics/%y/%m/%d',null=True)

    notes= models.TextField(max_length=50,null=True,blank=True)




                                                                     


