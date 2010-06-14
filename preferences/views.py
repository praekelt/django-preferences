from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

def singleton_redirect(request, model_name):
    cls = ContentType.objects.get(app_label="preferences", model=model_name).model_class()
    obj = cls.singleton.get()
    url = reverse('admin:preferences_%s_change' % model_name, args=(obj.id,))
    return redirect(url)
