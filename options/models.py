from django.db import models

import options
from options.managers import SingletonManager

class Options(models.Model):
    singleton = SingletonManager()

def options_class_prepared(sender, *args, **kwargs):
    cls = sender
   
    if issubclass(cls, Options):
        # add singleton manager to subclasses
        cls.add_to_class('singleton', SingletonManager())
        # add property for options object to to options.options
        setattr(options.Options, cls._meta.object_name, property(lambda x: cls.singleton.get()))

models.signals.class_prepared.connect(options_class_prepared)
