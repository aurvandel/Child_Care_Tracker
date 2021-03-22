import datetime
import calendar
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.utils.safestring import mark_safe

from .models import *
from .forms import *
from .utils import Calendar

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
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todos"] = Todo.objects.all()
        return context

# Update a task
class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoCreateForm
    template_name = 'tracker/todo_form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todos"] = Todo.objects.all()
        context["title"] = "Task"
        return context

# Details of task
class TodoDetailView(generic.DetailView):
    model = Todo
    context_object_name = "object"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todos"] = Todo.objects.all()
        return context

# Delete task
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
class SupplyList(generic.ListView):
    model = Supply
    context_object_name = "supplies"
    queryset = Supply.objects.all()
    template_name = "tracker/supplies.html"

# Create new supply
class SupplyCreateView(CreateView):
    form_class = SuppliesCreateForm
    template_name = 'tracker/supply_form.html'
    success_url = reverse_lazy('supply')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["supplies"] = Supply.objects.all()
        return context

# Update a supply
class SupplyUpdateView(UpdateView):
    model = Supply
    form_class = SuppliesCreateForm
    template_name = 'tracker/supply_form.html'
    success_url = reverse_lazy('supply')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["supplies"] = Supply.objects.all()
        return context

# Details of supply
class SupplyDetailView(generic.DetailView):
    model = Supply
    context_object_name = "object"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["supplies"] = Supply.objects.all()
        return context

# Delete supply
class SupplyDeleteView(DeleteView):
    model = Supply
    success_url = reverse_lazy('supply')
    template_name = 'tracker/supply_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["supplies"] = Supply.objects.all()
        return context

# Adds update frequency to supply order to reset reminder to order new supplies
def supplyUpdateModalView(request, pk):
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

# Create new supplier
class SupplierCreateView(CreateView):
    form_class = SupplierCreateForm
    template_name = 'tracker/supplier_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["supplier"] = Supplier.objects.all()
        return context

#Contact Views

# Contact list
class ContactList(generic.ListView):
    model = Contact
    context_object_name = "contacts"
    queryset = Contact.objects.all()
    template_name = "tracker/contact.html"

# Create new contact
class ContactCreateView(CreateView):
    form_class = ContactCreateForm
    template_name = 'tracker/contact_form.html'
    success_url = reverse_lazy('contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contacts"] = Contact.objects.all()
        return context

# Update a contact
class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactCreateForm
    template_name = 'tracker/contact_form.html'
    success_url = reverse_lazy('contact')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact"] = Contact.objects.all()
        return context

# Details of contact
class ContactDetailView(generic.DetailView):
    model = Contact
    context_object_name = "object"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contacts"] = Contact.objects.all()
        return context

# Delete contact
class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy('contact')
    template_name = 'tracker/contact_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contacts"] = Contact.objects.all()
        return context

# Calendar Views

# Render calendar
class CalendarView(generic.ListView):
    model = Appointment
    template_name = 'tracker/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('month', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

# Helpers for calander
def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - datetime.timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + datetime.timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

# Create new appt
class ApptCreateView(CreateView):
    form_class = ApptCreateForm
    template_name = 'tracker/appt_form.html'
    success_url = reverse_lazy('calendar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # use today's date for the calendar
        d = get_date(self.request.GET.get('month', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

# Update a appointment
class ApptUpdateView(UpdateView):
    model = Appointment
    form_class = ApptCreateForm
    template_name = 'tracker/appt_form.html'
    success_url = reverse_lazy('calendar')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["calendar"] = Appointment.objects.all()
        return context

# Details of contact
class ApptDetailView(generic.DetailView):
    model = Appointment
    context_object_name = "object"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["calendar"] = Appointment.objects.all()
        return context

# Delete contact
class ApptDeleteView(DeleteView):
    model = Appointment
    success_url = reverse_lazy('calendar')
    template_name = 'tracker/appt_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["calendar"] = Appointment.objects.all()
        return context