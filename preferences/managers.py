from django.conf import settings
from django.db import models
from django.contrib.sites.models import Site

class SingletonManager(models.Manager):
    def get_query_set(self):
        # get and return the first options object
        queryset = super(SingletonManager, self).get_query_set()
    
        current_site = None
        if getattr(settings, 'SITE_ID', None) != None:
            current_site = Site.objects.get_current()
        if current_site != None:
            queryset = queryset.filter(sites=settings.SITE_ID)
        try:
            queryset.get()
        except self.model.DoesNotExist:
            obj = self.model()
            obj.save()
            if current_site != None:
                obj.sites.add(current_site)
          
        return queryset
