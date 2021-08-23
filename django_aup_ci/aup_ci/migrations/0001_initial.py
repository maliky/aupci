# Generated by Django 3.2.6 on 2021-08-22 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemandeAdhesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_creation', models.DateTimeField(auto_now_add=True)),
                ('Date_Mise_a_Jour', models.DateTimeField(auto_now=True)),
                ('nom', models.CharField(max_length=150)),
                ('prenoms', models.CharField(max_length=255)),
                ('profession', models.CharField(max_length=250)),
                ('entreprise', models.CharField(max_length=250)),
                ('telephone', models.CharField(max_length=20)),
                ('courriel', models.EmailField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('demande', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='aup_ci.demandeadhesion')),
                ('fonction', models.CharField(choices=[('PR', 'Président'), ('VP', 'Vice-Président'), ('SG', 'Sécrétaire Générale'), ('TR', 'Trésorière Générale'), ('VT', 'Vice-Trésorière'), ('C1', 'Premier Commissaire aux comptes'), ('C2', 'Second Commissaire aux comptes'), ('Mb', 'Membre actif')], default='Mb', max_length=2)),
                ('date_adhesion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('Date_creation', models.DateTimeField(auto_now_add=True)),
                ('Date_Mise_a_Jour', models.DateTimeField(auto_now=True)),
                ('createur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('titre', models.CharField(max_length=255)),
                ('lieu', models.CharField(max_length=255)),
                ('type_evenement', models.CharField(choices=[('HN', 'Hackaton'), ('PN', 'PyCon'), ('MP', 'Meetup'), ('AR', 'Atelier'), ('AG', 'Assemblé Générale')], default='MP', max_length=2)),
                ('description', models.TextField()),
                ('date_adhesion', models.DateTimeField()),
                ('image_evenement', models.ImageField(upload_to='uploads/')),
                ('membres', models.ManyToManyField(related_name='evenements', to='aup_ci.Membre')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
