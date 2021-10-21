from django.shortcuts import render
from .models import GroupChat, TypedMessage, ChatUser
# Create your views here.
# some restrictions on logged in users
from django.contrib.auth import authenticate

from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this

def email_check(user):
    return user.email.endswith('@djangular.com')

def index(request):
    user = request.user
    data = TypedMessage.objects.all()
    return render(request, 'index.html', {"data":data, "user":user})
