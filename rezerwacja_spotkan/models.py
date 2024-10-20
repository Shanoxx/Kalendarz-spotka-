from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """Miejsce spotkan"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Zwraca reprezentacje miejsca w postaci tekstu"""
        return self.text
    
class Opis(models.Model):
    """Informacje na temat spotkan"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) 
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'opisy'

    def __str__(self):
        """Zwraca reprezenracje modelu w postaci ciagu tekstiowego"""
        return f"{self.text[:50]}..." if len(self.text) > 50 else self.text