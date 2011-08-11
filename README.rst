Django Preferences
==================
**Django app allowing users to set app specific preferences through the admin interface.** 

Provides singleton admin views for Preferences objects and a simple interface to preference values.
Singleton views ensure only one preference intance is available for each ``Preferences`` class.

.. contents:: Contents
    :depth: 5

Installation
------------

#. Install or add ``django-preferences`` to your Python path.

#. Add ``preferences`` to your ``INSTALLED APPS`` setting.

#. Add preferences url include to the project's ``url.py`` file BEFORE your admin urls include statement. Make sure to use ``'admin/'`` as the start of the include's path since it will override certain admin views::

    (r'^admin/', include('preferences.urls')),

Usage
-----
To create preferences for your app create a Django ORM model as usual, with the model inheriting from ``preferences.models.Preferences``. Also specify ``preferences.models`` as your models module::

    from django.db import models
    from preferences.models import Preferences

    class MyPreferences(Preferences):
        __module__ = 'preferences.models' 
        portal_contact_email = models.EmailField()

Admin classes are specified as per usual, no changes are needed. When your model is registered with admin it will show up under the *Preferences* app label in Django admin.

Preferences can be accessed in Python by importing the ``preferences`` module and traversing to your required preference in the form ``preferences.<ModelName>.<field>``, i.e.::

    from preferences import preferences

    portal_contact_email = preferences.MyPreferences.portal_contact_email


