from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Opis
from .forms import TopicForm, EntryForm


def index(request):
    """Strona główna dla aplikacji rezerwacja_spotkan"""
    return render(request, 'rezerwacja_spotkan/index.html')

@login_required
def topics(request,):
    """Wyswietlanie wszytkich tematow"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'rezerwacja_spotkan/topics.html', context)

@login_required
def topic(request, topic_id):
    """Wyswietla pojedynczy temat i wszystkie powiazane z nim wpisy"""
    topic = Topic.objects.get(id=topic_id)
    #Upewniamy sie ze temat nalezy do biezacego uzytkownika
    if topic.owner != request.user:
        raise Http404
    
    opisy = topic.opis_set.order_by('-date_added')
    context = {'topic': topic, 'opisy': opisy}
    return render(request, 'rezerwacja_spotkan/topic.html', context)

@login_required
def new_topic(request):
    """Dodaj nowy temat"""
    if request.method != 'POST':
        #Nie przekazano zadnych danych nalezy utworzyc pusty formularz
        form = TopicForm()
    else:
        #Przekazano dane za pomoca zadania POST nalezy je przetworzyc
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('rezerwacja_spotkan:topics')
#Wyswietlanie pustego formularza
    context = {'form': form}
    return render(request, 'rezerwacja_spotkan/new_topic.html', context)

@login_required
def new_opis(request, topic_id):
    """Dodanie nowego wpisu dla okreslonego tematu"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #Nie przekazano zadnych danych nalezy utorzyc pusty formularz
        form = EntryForm()
    else:
        #Przekazano dane za pomoca zadania POST, nalezy je przetworzyc
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_opis = form.save(commit=False)
            new_opis.topic = topic
            new_opis.save()
            return redirect('rezerwacja_spotkan:topic', topic_id=topic_id)
        
    #Wyswietlenie pustego formularza
    context = {'topic': topic, 'form': form}
    return render(request, 'rezerwacja_spotkan/new_opis.html', context)

@login_required
def edit_opis(request, opis_id):
    """Edycja istniejacego wpisu"""
    opis = Opis.objects.get(id=opis_id)
    topic = opis.topic
    if opis.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #Zadanie poczatkowe wypelnienie formularza aktualna trescia wpisu
        form = EntryForm(instance=opis)
    else:
        #Przekazano dane za pomoca zadania POST, nalezy je przetworzyc
        form = EntryForm(instance=opis, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('rezerwacja_spotkan:topic', topic_id=topic.id)
    context = {'opis': opis, 'topic': topic, 'form': form}
    return render(request, 'rezerwacja_spotkan/edit_opis.html', context)
