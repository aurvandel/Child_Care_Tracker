from django import forms
from .models import Todo

class TodoModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['todoTime', 'task', 'lastDone', 'recurring', 'completed']
