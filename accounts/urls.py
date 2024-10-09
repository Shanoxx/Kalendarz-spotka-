"""Definiuje wzorce adresow URL dla aplikacji accounts."""

from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    #Dolaczenie domyslnych adresow URL uwierzytelniania
    path('', include('django.contrib.auth.urls')),
    #Strona rejestracji
    path('registration/', views.register, name='register')
]