from django import forms
from django.urls import reverse_lazy
from .models import *

class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['todoDate', 'todoTime', 'task', 'lastDone', 'recurring', 'completed']
        success_url = reverse_lazy('index')

class SuppliesCreateForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = '__all__'
        success_url = reverse_lazy('supply')

class SupplierCreateForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
        success_url = reverse_lazy('supply')

class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        success_url = reverse_lazy('contact')

class ApptCreateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        success_url = reverse_lazy('calendar')