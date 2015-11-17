
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render
import chatz.urls


def playground(request):
	return render(request, 'base.html')


urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'leochat.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^$', playground),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^chat/', include(chatz.urls)),
)
