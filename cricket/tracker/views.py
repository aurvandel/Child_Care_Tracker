from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
#from bootstrap_modal_forms.generic import BSModalUpdateView

from .models import Todo
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
    #form = TodoModelForm(request.POST, instance=obj)
    short_description = obj.task
    if request.method=='POST':
        obj.updateTodo
        obj.save()
        return render(request, 'tracker/index.html', context)
    #context['form'] = form
    context['obj'] = obj
    return render(request, "tracker/confirm_update.html", context)

# class todoUpdateModalView(BSModalUpdateView):
#     template_name = 'tracker/confirm_update.html'
#     form_class = TodoModelForm
#     success_message = 'Task Completed'
#     success_url = reverse_lazy('index')
#     queryset = Todo.objects.all()
