# Generated by Django 3.2.6 on 2021-08-28 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aup_ci', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='abonnenew',
            name='traiter',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='demandeadhesion',
            name='confirme_adhesion',
            field=models.BooleanField(default=False),
        ),
    ]
