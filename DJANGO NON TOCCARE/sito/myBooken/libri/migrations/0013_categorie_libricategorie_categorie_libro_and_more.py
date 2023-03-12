# Generated by Django 4.1.7 on 2023-03-12 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libri', '0012_alter_libri_immagine'),
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
            name='LibriCategorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libri.categorie')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libri.libri')),
            ],
        ),
        migrations.AddField(
            model_name='categorie',
            name='libro',
            field=models.ManyToManyField(through='libri.LibriCategorie', to='libri.libri'),
        ),
        migrations.AddField(
            model_name='libri',
            name='categoria',
            field=models.ManyToManyField(through='libri.LibriCategorie', to='libri.categorie'),
        ),
    ]
