from django.urls import path
from tracker.views import *
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('supplies/', supplies.as_view(), name='supplies'),
    path('admin/', admin.site.urls),
    path('supplies/admin/', admin.site.urls),
    path('task_complete/<str:pk>/', todoUpdateModalView, name="task_complete"),
    path('supply_complete/<str:pk>/', suppliesUpdateModalView, name="supply_complete"),
    path('add/', TodoCreateView.as_view(), name='todo-add'),
    path('todo/<int:pk>/', TodoUpdateView.as_view(), name='todo-update'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo-delete'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    ]