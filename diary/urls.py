from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'magic.views.home', name='home'),
    url(r'^magic/', include('magic.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
