
from django.conf.urls import patterns, url
from chatz.views import show_chat


urlpatterns = patterns('',
   url(r'^wis1/$', show_chat),
)
