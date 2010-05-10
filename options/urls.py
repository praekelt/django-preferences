from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'options.views',
    url(r'^options/(?P<model_name>[\w-]+)/$', 'singleton_redirect', name='options_singelton_redirect'),
    url(r'^options/(?P<model_name>[\w-]+)/add/$', 'singleton_redirect', name='options_singelton_redirect'),
)
