from django import forms
from django.urls import reverse_lazy
from .models import *

class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
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