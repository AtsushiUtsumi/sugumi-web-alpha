# hello_django/urls.py
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from sugumi_web_alpha import views


# ↓ New basic view returning "Hello, Fly!" ↓
def hello(request):
    import django
    return HttpResponse(django.get_version())

from django.shortcuts import render

def menu(request):
    return render(request,'menu/index.html')

urlpatterns = [
    path("admin/", admin.site.urls),
    #path("", hello, name="hello"),
    path("menu/", menu, name="menu"),
    path('', views.index, name='index'),
]

