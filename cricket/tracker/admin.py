from django.contrib import admin
from .models import Todo, Appointment, Supplier, Supply

# Register your models here.
models = [Todo, Appointment, Supplier, Supply]
for model in models:
    admin.site.register(model)
