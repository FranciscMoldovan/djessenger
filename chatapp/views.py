from django.shortcuts import render
from .models import GroupChat, TypedMessage, ChatUser
# Create your views here.
# some restrictions on logged in users
from django.contrib.auth import authenticate

from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    user = request.user
    data = TypedMessage.objects.all()
    return render(request, 'index.html', {"data":data, "user":user})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect("login")
