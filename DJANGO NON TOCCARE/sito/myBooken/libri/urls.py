from django.urls import path
from . import views

urlpatterns = [
    path('', views.libri, name='libri'),
    path('dettagli_libro/<int:id>', views.dettagliLibro, name='dettagli_libro'),
    path('aggiungi_libro', views.aggiungiLibro, name='aggiungi_libro'),
    path('i_miei_libri', views.mieiLibri, name='i_miei_libri'),
]