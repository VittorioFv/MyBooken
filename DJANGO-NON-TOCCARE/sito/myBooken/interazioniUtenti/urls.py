from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatMain, name='chat_main'),
    path('codice/<int:codiceScambio>', views.controllaCodiceScambio, name='controlla_codice'),
    path('scambia_libro/<str:username>', views.scegliLibro, name='scambia_libro'),
    path('scambia_libro/genera_codice/<int:id>', views.generaCodice, name='genera_codice')
]