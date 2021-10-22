from django.conf.urls import url, include
from django.contrib import admin
from .views import index, login_view, logout_user
from django.urls import include, path


urlpatterns = [
    url(r'index', index, name='index'),
    url(r'login', login_view, name='login'),
    url(r'logout', logout_user, name='logout')
]