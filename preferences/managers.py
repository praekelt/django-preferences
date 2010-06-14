from django.db import models
from django.db.utils import DatabaseError

class SingletonManager(models.Manager):
    def get_query_set(self):
        # get and return the first options object
        queryset = super(SingletonManager, self).get_query_set()
        try:
            queryset.get()
        except self.model.DoesNotExist:
            obj = self.model()
            obj.save()
           
        return queryset
