from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'grantmcgovern.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('master.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^master/', include('master.urls')), # ADD THIS NEW TUPLE!
)
