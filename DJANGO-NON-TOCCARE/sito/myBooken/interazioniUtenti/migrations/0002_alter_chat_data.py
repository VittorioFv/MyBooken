# Generated by Django 4.1.7 on 2023-03-30 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interazioniUtenti', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='data',
            field=models.DateField(null=True),
        ),
    ]