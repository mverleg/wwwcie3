
from django.conf.urls import patterns, include, url
from django.contrib import admin
import chatz.urls


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'leochat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^chat/', include(chatz.urls)),
)
