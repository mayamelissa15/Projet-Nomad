# Generated by Django 4.1.7 on 2023-05-03 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=50)),
                ('owner_email', models.EmailField(max_length=50)),
                ('nbr_persons', models.IntegerField()),
                ('status', models.CharField(choices=[('accepted', 'accepted'), ('refused', 'refused'), ('waiting', 'waiting')], default='waiting', max_length=50)),
            ],
        ),
    ]