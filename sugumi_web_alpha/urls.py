# hello_django/urls.py
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


# ↓ New basic view returning "Hello, Fly!" ↓
def hello(request):
    return HttpResponse("Hello, Fly!")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", hello, name="hello"),  # ← Added!
]

