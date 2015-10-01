
from django import template
from chatz.models import ChatTopic
from chatz.views import generate_chat_html


register = template.Library()


@register.simple_tag(takes_context = True)
def display_chat(context, topic):
	request = context.get('request', None)
	if not request:
		return 'Need RequestContext to display chat.'
	if not isinstance(topic, ChatTopic):
		try:
			topic = ChatTopic.objects.get(name = topic)
		except ChatTopic.DoesNotExist:
			return 'We do not have a discussion about "{0:s}" yet.'.format(topic)
	return generate_chat_html(request, topic)


