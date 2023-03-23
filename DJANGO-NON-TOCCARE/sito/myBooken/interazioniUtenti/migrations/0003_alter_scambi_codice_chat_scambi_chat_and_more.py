# Generated by Django 4.1.7 on 2023-03-21 11:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libri', '0016_libricategorie_libri_categoria'),
        ('interazioniUtenti', '0002_scambi_libro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scambi',
            name='codice',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utente1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utente1', to=settings.AUTH_USER_MODEL)),
                ('utente2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utente2', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('utente1', 'utente2')},
            },
        ),
        migrations.AddField(
            model_name='scambi',
            name='chat',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='interazioniUtenti.chat'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='scambi',
            unique_together={('libro', 'chat')},
        ),
        migrations.RemoveField(
            model_name='scambi',
            name='mittente',
        ),
        migrations.RemoveField(
            model_name='scambi',
            name='ricevente',
        ),
    ]
