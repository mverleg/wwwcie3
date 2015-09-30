
from settings import AUTH_USER_MODEL
from django.db import models


class ChatTopic(models.Model):
    name= models.CharField(max_length=20,unique=True)


class ChatMessage(models.Model):
    user= models.ForeignKey(AUTH_USER_MODEL)
    time= models.DateTimeField(auto_now=True)
    text =models.TextField()
    topic =models.CharField(max_length=20)


