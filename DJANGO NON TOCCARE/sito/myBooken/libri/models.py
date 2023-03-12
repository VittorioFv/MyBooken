from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

class Libri(models.Model):
  titolo = models.CharField(max_length=50)  # VARCHAR
  autore = models.CharField(max_length=50)  # VARCHAR
  
  isbn = models.CharField(max_length=13, validators=[MinLengthValidator(13)])    # CHAR

  descrizione = models.CharField(max_length=255) # VARCHAR

  citta = models.CharField(max_length=50)

  longitudine = models.FloatField(max_length=50)
  latitudine = models.FloatField(max_length=50)

  immagine = models.ImageField(null = True, blank = True, upload_to="images/libri/")

  idUser = models.ForeignKey(User, on_delete=models.CASCADE)

  # per qualche motivo la variabile categorie al plurale da errore
  categoria = models.ManyToManyField('Categorie', through='LibriCategorie') 


class Categorie(models.Model):
  nomeCategoria = models.CharField(max_length=50)


class LibriCategorie(models.Model):
  libro = models.ForeignKey(Libri, on_delete=models.CASCADE)
  categoria = models.ForeignKey(Categorie, on_delete=models.CASCADE)
