from django.contrib import admin
from .models import Libri, Categorie, LibriCategorie

# Register your models here.
class LibriAdmin(admin.ModelAdmin):
  list_display = ("titolo", "id",)

class CategorieAdmin(admin.ModelAdmin):
  list_display = ("nomeCategoria", "id",)

class LibriCategorieAdmin(admin.ModelAdmin):
  list_display = ("libro", "categoria", "id",)

admin.site.register(Libri, LibriAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(LibriCategorie, LibriCategorieAdmin)