from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'preferences.views',
    url(r'^preferences/(?P<model_name>[\w-]+)/$', 'singleton_redirect', name='preferences_singelton_redirect'),
    url(r'^preferences/(?P<model_name>[\w-]+)/add/$', 'singleton_redirect', name='preferences_singelton_redirect'),
)
