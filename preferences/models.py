from django.db import models

import preferences
from preferences.managers import SingletonManager

class Preferences(models.Model):
    singleton = SingletonManager()

def preferences_class_prepared(sender, *args, **kwargs):
    cls = sender
   
    if issubclass(cls, Preferences):
        # add singleton manager to subclasses
        cls.add_to_class('singleton', SingletonManager())
        # add property for preferences object to preferences.preferences
        setattr(preferences.Preferences, cls._meta.object_name, property(lambda x: cls.singleton.get()))

models.signals.class_prepared.connect(preferences_class_prepared)
