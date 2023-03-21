from django.contrib import admin
from .models import Libri

# Register your models here.
class LibriAdmin(admin.ModelAdmin):
  list_display = ("titolo", "autore",)

admin.site.register(Libri, LibriAdmin)