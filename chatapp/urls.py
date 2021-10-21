from django.conf.urls import url, include
from django.contrib import admin
from .views import index
from django.urls import include, path


urlpatterns = [
    url(r'app', index)
]