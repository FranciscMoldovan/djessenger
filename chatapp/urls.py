from django.conf.urls import url, include
from django.contrib import admin
from .views import index
urlpatterns = [
    url(r'', index)
]