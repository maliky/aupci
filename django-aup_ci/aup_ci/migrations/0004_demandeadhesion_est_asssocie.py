# Generated by Django 3.2.6 on 2021-08-30 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aup_ci', '0003_rename_fonction_membre_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='demandeadhesion',
            name='est_asssocie',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]