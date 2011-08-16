from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

def singleton_redirect(request, model_name):
    if Site.objects.all().count() > 1:
        url = 'foo'
    else:
        cls = ContentType.objects.get(app_label="preferences", model=model_name).model_class()
        obj = cls.singleton.get()
        url = reverse('admin:preferences_%s_change' % model_name, args=(obj.id,))
    return redirect(url)

def listing_singleton_redirect(request, model_name):
    cls = ContentType.objects.get(app_label="preferences", model=model_name).model_class()
    if cls.objects.all().count() > 1:
        from django.contrib import admin
        return admin.site._registry[cls].changelist_view(request)
    else:
        obj = cls.singleton.get()
        url = reverse('admin:preferences_%s_change' % model_name, args=(obj.id,))
    return redirect(url)
