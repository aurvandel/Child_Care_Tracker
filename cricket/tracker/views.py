from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
#from bootstrap_modal_forms.generic import BSModalUpdateView

from .models import *
from .forms import TodoModelForm

# Create your views here.


class index(generic.ListView):
    model = Todo
    context_object_name = "todos"
    queryset = Todo.objects.all()
    template_name = 'tracker/index.html'

def todoUpdateModalView(request, pk):
    todos = Todo.objects.all()
    context = {}
    context['todos'] = todos
    obj = get_object_or_404(Todo, pk=pk)
    if request.method=='POST':
        obj.updateTodo
        obj.save()
        return render(request, 'tracker/index.html', context)
    context['obj'] = obj
    return render(request, "tracker/confirm_update.html", context)

class supplies(generic.ListView):
    model = Supply
    context_object_name = "supplies"
    queryset = Supply.objects.all()
    template_name = "tracker/supplies.html"

def suppliesUpdateModalView(request, pk):
    supplies = Supply.objects.all()
    context = {}
    context['supplies'] = supplies
    obj = get_object_or_404(Supply, pk=pk)
    if request.method=='POST':
        obj.updateSupplyDate
        obj.save()
        return render(request, 'tracker/supplies.html', context)
    context['obj'] = obj
    return render(request, "tracker/confirm_update_supply.html", context)