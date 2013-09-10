from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('magic.api',
     url(r'^api/events/?','events', name='api_events'),
)

