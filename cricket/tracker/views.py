from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
#from bootstrap_modal_forms.generic import BSModalUpdateView

from .models import *
from .forms import *

# Create your views here.

# Task views

# Index starts at todo list for now
class index(generic.ListView):
    model = Todo
    context_object_name = "todos"
    queryset = Todo.objects.all()
    template_name = 'tracker/index.html'

# Create new task
class TodoCreateView(CreateView):
    form_class = TodoCreateForm
    template_name = 'tracker/todo_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todos"] = Todo.objects.all()
        return context

class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoCreateForm
    template_name = 'tracker/todo_form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todos"] = Todo.objects.all()
        return context

class TodoDetailView(generic.DetailView):
    model = Todo
    context_object_name = "object"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todos"] = Todo.objects.all()
        return context

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('index')
    template_name = 'tracker/todo_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todos"] = Todo.objects.all()
        return context

# Adds 1 day to the task once user says it's completed
def todoUpdateModalView(request, pk):
    todos = Todo.objects.all()
    context = {}
    context['todos'] = todos
    obj = get_object_or_404(Todo, pk=pk)
    if request.method=='POST':
        if obj.recurring:
            obj.updateTodo
        else:
            obj.completed = True
        obj.save()
        return render(request, 'tracker/index.html', context)
    context['obj'] = obj
    return render(request, "tracker/confirm_update.html", context)


#Supply Views

# Supplies list
class supplies(generic.ListView):
    model = Supply
    context_object_name = "supplies"
    queryset = Supply.objects.all()
    template_name = "tracker/supplies.html"

# Adds update frequency to supply order to reset reminder to order new supplies
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

