# Generated by Django 4.1.7 on 2023-03-12 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libri', '0013_categorie_libricategorie_categorie_libro_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorie',
            name='libro',
        ),
    ]