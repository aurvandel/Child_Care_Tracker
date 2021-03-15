from django.urls import path
from tracker.views import *
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('admin/', admin.site.urls),   
    path('task_complete/<str:pk>/', todoUpdateModalView, name="task_complete"),
    path('add/', TodoCreateView.as_view(), name='todo-add'),
    path('todo/<int:pk>/', TodoUpdateView.as_view(), name='todo-update'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo-delete'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    
    path('supply/', supply.as_view(), name='supply'),
    path('supply/admin/', admin.site.urls),
    path('supply_complete/<str:pk>/', supplyUpdateModalView, name="supply_complete"),
    path('supply/add', SupplyCreateView.as_view(), name='supply-add'),
    path('supply/<int:pk>/', SupplyUpdateView.as_view(), name='supply-update'),
    path('supply/<int:pk>/delete/', SupplyDeleteView.as_view(), name='supply-delete'),
    path('supply/<int:pk>/', SupplyDetailView.as_view(), name='supply-detail'),

    path('supplier/add', SupplierCreateView.as_view(), name='supplier-add'),
    ]