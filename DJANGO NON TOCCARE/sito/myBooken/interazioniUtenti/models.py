from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinLengthValidator

from libri.models import Libri


# Create your models here.
class Scambi(models.Model):
  ricevente = models.ForeignKey(User, related_name='ricevente', on_delete=models.CASCADE)
  mittente = models.ForeignKey(User, related_name='mittente',on_delete=models.CASCADE)
  libro = models.ForeignKey(Libri, on_delete=models.CASCADE)

  codice = models.CharField(max_length=6, unique=True, validators=[MinLengthValidator(6)])