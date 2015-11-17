
from django.conf.urls import patterns, url
from chatz.views import chat_post, chat_show


urlpatterns = patterns('',
	url(r'^POST/$', chat_post, name = 'chat_post'),
	url(r'^wis1/$', chat_show, name = 'chat_show'),
)


