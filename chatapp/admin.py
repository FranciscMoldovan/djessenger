from django.contrib import admin
from .models import ChatUser, TypedMessage, GroupChat
# Register your models here.
admin.site.register(ChatUser)
admin.site.register(TypedMessage)
admin.site.register(GroupChat)