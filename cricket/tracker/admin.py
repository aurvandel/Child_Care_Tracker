from django.contrib import admin
from .models import *

# Register your models here.
models = [Todo, Appointment, Supplier, Supply, Contact]
for model in models:
    admin.site.register(model)
