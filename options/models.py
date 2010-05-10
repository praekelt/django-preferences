from django.db import models

import options
from options.managers import SingletonManager

class Options(models.Model):
    singleton = SingletonManager()

def options_class_prepared(sender, *args, **kwargs):
    cls = sender
   
    if issubclass(cls, Options):
        cls.add_to_class('singleton', SingletonManager())
        #setattr(options, cls._meta.object_name, cls.singleton.get())

models.signals.class_prepared.connect(options_class_prepared)
