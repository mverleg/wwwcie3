
from settings import AUTH_USER_MODEL
from django.db import models


class ChatTopic(models.Model):
    name= models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.name


class ChatMessage(models.Model):
    user= models.ForeignKey(AUTH_USER_MODEL)
    time= models.DateTimeField(auto_now=True)
    text =models.TextField()
    topic = models.ForeignKey(ChatTopic)
    def __str__(self):
        return '{0:s} @ {1:s}'.format(str(self.user), str(self.topic.name))

