from django.db import models
from preferences.models import Preferences


class MyPreferences(Preferences):
    __module__ = 'preferences.models'
    portal_contact_email = models.EmailField()
