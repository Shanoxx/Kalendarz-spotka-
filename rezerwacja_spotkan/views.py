from django.shortcuts import render

def index(request):
    """Strona główna dla aplikacji rezerwacja_spotkan"""
    return render(request, 'rezerwacja_spotkan/index.html')
