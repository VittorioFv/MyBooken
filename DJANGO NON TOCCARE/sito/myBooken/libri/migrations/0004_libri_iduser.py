# Generated by Django 4.1.7 on 2023-03-09 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libri', '0003_libri_autore_libri_descrizione_alter_libri_titolo'),
    ]

    operations = [
        migrations.AddField(
            model_name='libri',
            name='idUser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
