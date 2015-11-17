
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from chatz.models import ChatMessage, ChatTopic


def generate_chat_html(request, topic):
	messages = ChatMessage.objects.filter(topic = topic)
	return render_to_string('render_chat.html', RequestContext(request, {
		'messages': messages,
		'topic': topic,
	}))


def chat_show(request, topic_name = 'wiskunde1'):
	try:
		topic = ChatTopic.objects.get(name = topic_name)
	except ChatTopic.DoesNotExist:
		return HttpResponse('We do not have a discussion about "{0:s}" yet. {1:s}'.format(topic_name, 'You can create it in the admin panel.' if request.user.is_staff else ''))
	return render(request, 'show_chat.html', {
		'topic': topic,
	})


@login_required
@require_POST
def chat_post(request):
	topic_name = request.POST.get('topic', '')
	try:
		topic = ChatTopic.objects.get(name = topic_name)
	except ChatTopic.DoesNotExist:
		return HttpResponse('We do not have a discussion about "{0:s}" yet. {1:s}'.format(topic_name, 'You can create it in the admin panel.' if request.user.is_staff else ''))
	return HttpResponse('ja oke je hoort nog van ons doeeei! {0}'.format(', '.join('{0:s}: {1:}'.format(k, v) for k, v in request.POST.items())))


