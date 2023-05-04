# Generated by Django 4.1.7 on 2023-04-15 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voyage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_of_departure', models.DateField()),
                ('duration', models.IntegerField()),
                ('unit', models.CharField(choices=[('hour(s)', 'hour(s)'), ('day(s)', 'day(s)')], max_length=50)),
                ('wilaya', models.CharField(choices=[('Alger', 'Alger'), ('Oran', 'Oran'), ('Timimoune', 'Timimoune'), ('Setif', 'Setif'), ('Bejaia', 'Bejaia'), ('Constantine', 'Constantine')], max_length=50)),
                ('budget', models.IntegerField()),
                ('Number_of_attendees', models.IntegerField(choices=[('1 person', '1 person'), ('2 person', '2 person'), ('3 person', '3 person'), ('4 person', '4 person'), ('5 person', '5 person'), ('6 person', '6 person'), ('7 person', '7 person'), ('8 person', '8 person'), ('9 person', '9 person'), ('+10 person', '+10 person'), ('+20 person', '+20 person'), ('+30 person', '+30 person')])),
                ('Guide_language', models.CharField(choices=[('Kabyle', 'Kabyle'), ('Arabe', 'Arabe'), ('Arabe(Darija)', 'Arabe(Darija)'), ('Français', 'Français'), ('Anglais', 'Anglais'), ('Espagnol', 'Espagnol'), ('Mandarin', 'Mandarin')], max_length=50)),
                ('Specify_your_request', models.CharField(max_length=60)),
            ],
        ),
    ]