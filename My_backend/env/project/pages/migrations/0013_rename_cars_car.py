# Generated by Django 4.1.7 on 2023-05-01 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_cars_alter_guide_identity_pic_alter_guide_sexe'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cars',
            new_name='Car',
        ),
    ]
