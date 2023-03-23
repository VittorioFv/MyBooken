# Generated by Django 4.1.7 on 2023-03-23 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libri', '0016_libricategorie_libri_categoria'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interazioniUtenti', '0003_alter_scambi_codice_chat_scambi_chat_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='scambi',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='chat',
            name='numeroScambi',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='scambi',
            name='idRichiedente',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='scambi',
            unique_together={('libro', 'idRichiedente')},
        ),
        migrations.RemoveField(
            model_name='scambi',
            name='chat',
        ),
    ]