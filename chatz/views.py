from datetime import timedelta
from django.shortcuts import render

# Create your views here.
from django.utils.timezone import now
from chatz.models import ChatMessage, ChatTopic


def show_chat(request):
	topic = ChatTopic.objects.get(name='wiskunde1')
	messages = ChatMessage.objects.filter(topic=topic)
	return render(request, 'show_chat.html', {
		'messages': messages,
	})

