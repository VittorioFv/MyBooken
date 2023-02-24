from django.db import models
from django.core.validators import MinLengthValidator

class Libri(models.Model):
  titolo = models.CharField(max_length=50)  # VARCHAR
  autore = models.CharField(max_length=50)  # VARCHAR
  
  isbn = models.CharField(max_length=13, validators=[MinLengthValidator(13)])    # CHAR

  descrizione = models.CharField(max_length=255) # VARCHAR
  