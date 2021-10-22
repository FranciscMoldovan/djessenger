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
from django.http import HttpResponseRedirect
from django.http import JsonResponse


@login_required()
def index(request):
    user = request.user
    current_chat = GroupChat.objects.first().id
    data = TypedMessage.objects.filter(chat=current_chat)

    return render(request, 'index.html', {"data":data, "user":user, "current_chat":current_chat})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request, 'login.html')

@login_required()
def chat_data(request):
    """
    JSON chat data for js
    """
    user = request.user
    current_chat = GroupChat.objects.first().id
    data = TypedMessage.objects.filter(chat=current_chat).values()

    return JsonResponse({"data":list(data)})


def add_message(request):
    if request.method == 'POST':
        user = request.user  # message sender
        message = request.POST.get("message")
        print(f">>>>>{message}, user={user}")
        ####
        chat_user = ChatUser.objects.filter(username=user).first()

        new_message = TypedMessage()
        new_message.contents = message
        new_message.owner = chat_user
        new_message.chat = GroupChat.objects.first()

        print(f"CHAT USER:{chat_user}")

        new_message.save()
        ####
        return HttpResponseRedirect("/index/")


def logout_user(request):
    logout(request)
    return redirect("login")
