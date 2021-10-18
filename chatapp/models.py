from django.db import models
from django.conf import settings
from django.db import models


class ChatUser(models.Model):
    username = models.CharField(null=False, unique=True, max_length=200)
    email_address = models.CharField(null=False, max_length=200)
    django_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class GroupChat(models.Model):
    title = models.CharField(max_length=100)


class TypedMessage(models.Model):
    contents = models.CharField(max_length=1000)
    owner = models.ForeignKey(ChatUser, related_name="mymessage", on_delete=models.CASCADE)
    chat = models.ForeignKey(GroupChat, related_name="chat_from", on_delete=models.CASCADE)
