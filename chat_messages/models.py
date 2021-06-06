from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    pass


class UserMessage(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='messages_sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='messages_receiver', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    is_new = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['creation_date']
