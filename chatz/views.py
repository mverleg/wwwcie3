from datetime import timedelta
from django.shortcuts import render

# Create your views here.
from django.utils.timezone import now


def show_chat(request):
	messages = [
		{
			'who': 'Henk',
			'when': now() - timedelta(seconds = 3),
			'text': 'Onze chatz is supercool!',
			'topic': 'wis1',
		},
		{
			'who': 'Henk',
			'when': now(),
			'text': 'Niewaar!',
			'topic': 'wis1',
		}
	]
	return render(request, 'show_chat.html', {
		'messages': messages,
	})

