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
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),  # HTML5 date picker
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', 'step': 1}),  # HTML5 time picker
        }
    
    # def save(self, commit=True, user=None):
    #     task = super().save(commit=False)
    #     if user is not None:
    #         task.user = user  # Set the user field on the task
    #     if commit:
    #         task.save()
    #     return task