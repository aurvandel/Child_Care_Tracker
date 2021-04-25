"""cricket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from tracker import views
from django.conf.urls import url
from tracker.task import notify_users
from background_task.models import Task
from django.contrib import admin

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    url(r'^tracker/', include('tracker.urls')),
    path('admin/', admin.site.urls),


]

if not Task.objects.filter(verbose_name="notify_users").exists():
    notify_users(repeat=1, verbose_name="notify_users")

# notify_users()
