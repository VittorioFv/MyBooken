from django.urls import path
from . import views

urlpatterns = [
    path('libri/', views.libri, name='libri'),
    path('libri/dettagli_libro/<int:id>', views.dettagliLibro, name='dettagli_libro')
]