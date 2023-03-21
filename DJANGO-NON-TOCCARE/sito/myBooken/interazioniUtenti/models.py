from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinLengthValidator

from libri.models import Libri

class Chat(models.Model):
  utente1 = models.ForeignKey(User, related_name='utente1', on_delete=models.CASCADE)
  utente2 = models.ForeignKey(User, related_name='utente2', on_delete=models.CASCADE)

  class Meta:
    unique_together = ('utente1', 'utente2')


class Scambi(models.Model):
  libro = models.ForeignKey(Libri, on_delete=models.CASCADE)
  chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
  codice = models.CharField(max_length=6, unique=True, validators=[MinLengthValidator(6)], null=True, blank=True)


  class Meta:
    unique_together = ('libro', 'chat')
