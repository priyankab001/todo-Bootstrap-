from .models import *

from django import forms


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new Task...'}))

    class Meta:
        model = Task
        fields = '__all__'
