# Generated by Django 4.1.7 on 2023-04-15 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_voyage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voyage',
            name='Number_of_attendees',
            field=models.IntegerField(choices=[('1', '1 person'), ('2', '2 person'), ('3', '3 person'), ('4', '4 person'), ('5', '5 person'), ('6', '6 person'), ('7', '7 person'), ('8', '8 person'), ('9', '9 person'), ('10+', '+10 person'), ('20+', '+20 person'), ('30+', '+30 person')]),
        ),
    ]