from django import forms
from .models import Topic, Opis

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = {'text'}
        labels = {'text':''}
class EntryForm(forms.ModelForm):
    class Meta:
        model = Opis
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
