from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Rejestracja nowego uzytkownika"""
    if request.method != 'POST':
        #Wyswietlenie pustego formularza rejestracji uzytkownikow
        form = UserCreationForm()
    else:
        #Przetworzenie wypelnionego formularza
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #Zalogowanie uzytkownika a nastepnie przekierowanie go na strone glowna
            login(request, new_user)
            return redirect('rezerwacja_spotkan:index')
    
    #Wyswietlenie pustego formularza
    context = {'form': form}
    return render(request, 'registration/register.html', context)
