# Generated by Django 3.2.6 on 2021-08-31 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AbonneNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courriel', models.EmailField(max_length=254, unique=True)),
                ('confirme_abonne', models.BooleanField(default=False)),
                ('traiter', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DemandeAdhesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_Mise_a_Jour', models.DateTimeField(auto_now=True)),
                ('nom', models.CharField(max_length=150)),
                ('prenoms', models.CharField(max_length=255)),
                ('profession', models.CharField(max_length=250)),
                ('entreprise', models.CharField(max_length=250)),
                ('telephone', models.CharField(max_length=20)),
                ('courriel', models.EmailField(max_length=255, unique=True)),
                ('traiter', models.BooleanField(default=False)),
                ('confirme_adhesion', models.BooleanField(default=False)),
                ('est_associe', models.BooleanField(blank=True, default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_Mise_a_Jour', models.DateTimeField(auto_now=True)),
                ('titre', models.CharField(max_length=255)),
                ('lieu', models.CharField(max_length=255)),
                ('description_lieu', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('image_evenement', models.ImageField(upload_to='uploads/img/events/')),
                ('date_debut', models.DateTimeField(blank=True, null=True)),
                ('date_fin', models.DateTimeField(blank=True, null=True)),
                ('es_publier', models.BooleanField(blank=True, default=True)),
                ('nombre_place', models.IntegerField(blank=True, null=True)),
                ('createur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_Mise_a_Jour', models.DateTimeField(auto_now=True)),
                ('sujet', models.CharField(max_length=150)),
                ('contenu', models.FileField(upload_to='uploads/file/newsletters/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TypeEvenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('demande', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='aup_ci.demandeadhesion')),
                ('role', models.CharField(choices=[('PR', 'Président'), ('VP', 'Vice-Président'), ('SG', 'Sécrétaire Générale'), ('TR', 'Trésorière Générale'), ('VT', 'Vice-Trésorière'), ('C1', 'Premier Commissaire aux comptes'), ('C2', 'Second Commissaire aux comptes'), ('Mb', 'Membre actif')], default='Mb', max_length=2)),
                ('date_adhesion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('prenoms', models.CharField(max_length=255)),
                ('profession', models.CharField(max_length=250)),
                ('telephone', models.CharField(max_length=20)),
                ('courriel', models.CharField(max_length=255, unique=True)),
                ('evenements', models.ManyToManyField(related_name='participants', to='aup_ci.Evenement')),
            ],
        ),
        migrations.AddField(
            model_name='evenement',
            name='type_evenement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aup_ci.typeevenement'),
        ),
    ]