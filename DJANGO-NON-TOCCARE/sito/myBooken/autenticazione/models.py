from django.db import models
from django.db.models import IntegerField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

User._meta.get_field('email')._unique = True

class Profilo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)

    citta = models.CharField(max_length=50)

    longitudine = models.FloatField(max_length=50)
    latitudine = models.FloatField(max_length=50)

    numTopen = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

'''class Recensioni(models.Model):
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    voto = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    testo = models.CharField(max_length=1000)'''