from django.urls import path
from . import views

urlpatterns = [
    path('', views.libri, name='libri'),
    path('dettagli_libro/<int:id>', views.dettagliLibro, name='dettagli_libro')
]