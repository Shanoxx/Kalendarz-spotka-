from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm

def index(request):
    """Strona główna dla aplikacji rezerwacja_spotkan"""
    return render(request, 'rezerwacja_spotkan/index.html')

def topics(request,):
    """Wyswietlanie wszytkich tematow"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'rezerwacja_spotkan/topics.html', context)

def topic(request, topic_id):
    """Wyswietla pojedynczy temat i wszystkie powiazane z nim wpisy"""
    topic = Topic.objects.get(id=topic_id)
    opisy = topic.opis_set.order_by('-date_added')
    context = {'topic': topic, 'opisy': opisy}
    return render(request, 'rezerwacja_spotkan/topic.html', context)

def new_topic(request):
    """Dodaj nowy temat"""
    if request.method != 'POST':
        #Nie przekazano zadnych danych nalezy utworzyc pusty formularz
        form = TopicForm()
    else:
        #Przekazano dane za pomoca zadania POST nalezy je przetworzyc
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('rezerwacja_spotkan:topics')
#Wyswietlanie pustego formularza
    context = {'form': form}
    return render(request, 'rezerwacja_spotkan/new_topic.html', context)