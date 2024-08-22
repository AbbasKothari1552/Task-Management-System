from django import forms
from .models import Tag, Task

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name',]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'tag', 'priority', 'date', 'time', 'repeat']