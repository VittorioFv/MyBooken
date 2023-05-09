from django.urls import path
from . import views

urlpatterns = [
    path('attiva/<uidb64>/<token>', views.attivaUtente, name='attiva'),
    path('recupera_password/<uidb64>/<token>', views.recuperaPassword, name='cambia_password'),

    path('recupera_password', views.passwordDimenticata, name='recupera'),
    path('login/', views.loginUtente, name='login'),
    path('logout_utente/', views.logoutUtente, name='logout'),
    path('registrazione/', views.registrazioneUtente, name='registrazione'),
]