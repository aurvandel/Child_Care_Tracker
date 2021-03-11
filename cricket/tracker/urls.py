from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('supplies/', views.supplies.as_view(), name='supplies'),
    path('admin/', admin.site.urls),
    path('supplies/admin/', admin.site.urls),
    path('task_complete/<str:pk>/', views.todoUpdateModalView, name="task_complete"),
    path('supply_complete/<str:pk>/', views.suppliesUpdateModalView, name="supply_complete"),
    
    ]