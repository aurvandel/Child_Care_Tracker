from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('tracker/<int:pk>', views.TodoUpdate, name='todo-update'),
    # path("task_complete/<str:pk>/", views.todoUpdateModal, name='task_complete')

]