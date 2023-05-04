# Generated by Django 4.1.7 on 2023-04-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_voyage_accept_terms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('phone_num', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=50)),
                ('sector', models.CharField(choices=[('Alger', 'Alger'), ('Oran', 'Oran'), ('Timimoune', 'Timimoune'), ('Setif', 'Setif'), ('Bejaia', 'Bejaia'), ('Constantine', 'Constantine')], max_length=50)),
                ('first_language', models.CharField(max_length=50)),
                ('second_language', models.CharField(max_length=50)),
                ('third_language', models.CharField(blank=True, max_length=50, null=True)),
                ('sexe', models.CharField(choices=[('Women', 'Woman'), ('Men', 'Men')], max_length=50)),
                ('your_presentation', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(default='static/img/avatar.png', null=True, upload_to='profile_pics/%y/%m/%d')),
                ('accept_terms', models.CharField(choices=[('on', 'on'), ('off', 'off')], default='off', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='voyage',
            name='Guide_language',
            field=models.CharField(choices=[('Kabyle', 'Kabyle'), ('Arabe', 'Arabe'), ('Arabe(Darija)', 'Arabe(Darija)'), ('Francais', 'Francais'), ('Anglais', 'Anglais'), ('Espagnol', 'Espagnol'), ('Mandarin', 'Mandarin')], max_length=50),
        ),
        migrations.AlterField(
            model_name='voyage',
            name='unit',
            field=models.CharField(choices=[('Hour(s)', 'Hour(s)'), ('Day(s)', 'Day(s)')], max_length=50),
        ),
    ]