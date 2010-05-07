from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

def singleton_redirect(request, model_name):
    try:
        cls = ContentType.objects.get(app_label="options", model=model_name).model_class()
        obj = cls.objects.get()
        url = reverse('admin:options_galleryoptions_change', args=(obj.id,))
    except cls.DoesNotExist:
        url = reverse('admin:options_galleryoptions_add',)

    return redirect(url)
