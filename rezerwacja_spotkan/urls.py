"""Definiuje wzorce adresow URL dla app rezerwacja spotkan"""
from django.urls import path
from . import views
app_name = 'rezerwacja_spotkan'
urlpatterns = [
    #Strona główna.
    path('', views.index, name='index'),
]