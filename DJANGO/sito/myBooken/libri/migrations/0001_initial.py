# Generated by Django 4.1.7 on 2023-04-20 16:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCategoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Libri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=50)),
                ('autore', models.CharField(max_length=50)),
                ('isbn', models.CharField(max_length=13, validators=[django.core.validators.MinLengthValidator(13)])),
                ('descrizione', models.CharField(max_length=255)),
                ('citta', models.CharField(max_length=50)),
                ('longitudine', models.FloatField(max_length=50)),
                ('latitudine', models.FloatField(max_length=50)),
                ('immagine', models.ImageField(blank=True, null=True, upload_to='images/libri/')),
                ('data', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LibriCategorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libri.categorie')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libri.libri')),
            ],
        ),
        migrations.AddField(
            model_name='libri',
            name='categoria',
            field=models.ManyToManyField(through='libri.LibriCategorie', to='libri.categorie'),
        ),
        migrations.AddField(
            model_name='libri',
            name='idUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
