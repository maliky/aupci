# Generated by Django 3.2.6 on 2021-08-30 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aup_ci', '0004_demandeadhesion_est_asssocie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demandeadhesion',
            old_name='est_asssocie',
            new_name='est_associe',
        ),
    ]