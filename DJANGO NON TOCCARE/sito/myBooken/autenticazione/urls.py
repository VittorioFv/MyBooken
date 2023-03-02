from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUtente, name='login'),
    path('logoutUtente/', views.logoutUtente, name='logout'),
    path('registrazione/', views.registrazioneUtente, name='registrazione'),
]