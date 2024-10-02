"""Definiuje wzorce adresow URL dla app rezerwacja spotkan"""
from django.urls import path
from . import views
app_name = 'rezerwacja_spotkan'
urlpatterns = [
    #Strona główna.
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    #Strona szczegolowa dotyczaca pojedynczego tematu.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #Strona przeznaczona do dodawania nowego tematu.
    path('new_topic/', views.new_topic, name='new_topic'),
]