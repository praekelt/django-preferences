Django Preferences
==================
**Django app allowing users to set app specific preferences through the admin interface.** 

Provides singleton admin views for Preferences objects and a simple interface to preference values.
Singleton views ensure only one preference intance per site is available for each ``Preferences`` class.

.. note:: 

    django-preferences requires and supports `Django's "sites" framework <https://docs.djangoproject.com/en/dev/ref/contrib/sites/>`_, which means you can have multiple preferences, each associated with a particular site.

.. note::

    django-preferences version 0.0.5 and higher requires Django 1.3 and higher for correct operation. If you are getting the super vague ``Error: cannot import name receiver`` error on startup either update to Django 1.3 or use django-preferences version 0.0.4 or earlier. 

.. contents:: Contents
    :depth: 5

Installation
------------

#. Install or add ``django-preferences`` to your Python path.

#. Add ``preferences`` to your ``INSTALLED APPS`` setting.

#. Add ``django.contrib.sites`` to your ``INSTALLED APPS`` setting. django-preferences associates preferences to specific sites and thus requires `Django's "sites" framework <https://docs.djangoproject.com/en/dev/ref/contrib/sites/>`_ to be installed.

#. Optionally, add ``preferences.context_processors.preferences_cp`` to your `TEMPLATE_CONTEXT_PROCESSORS <https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATE_CONTEXT_PROCESSORS>`_ settings. This will automatically add a ``preferences`` variable to your template context if you use `RequestContext <https://docs.djangoproject.com/en/dev/ref/templates/api/#subclassing-context-requestcontext>`_ to create your context (see Usage below), i.e.::
    
    TEMPLATE_CONTEXT_PROCESSORS = (
        ...other context processors...,
        "preferences.context_processors.preferences_cp",
    )

Usage
-----
To create preferences for your app create a Django ORM model as usual, with the model inheriting from ``preferences.models.Preferences``. Also specify ``preferences.models`` as your model's module::

    from django.db import models
    from preferences.models import Preferences

    class MyPreferences(Preferences):
        __module__ = 'preferences.models' 
        portal_contact_email = models.EmailField()

Admin classes are specified as per usual, except that they have to inherit from or be registered with ``preferences.admin.PreferencesAdmin``, i.e.::

    from django.contrib import admin

    from preferences.admin import PreferencesAdmin
    from <my_app>.models import MyPreferences

    admin.site.register(MyPreferences, PreferencesAdmin)

When your model is registered with admin it will show up under the *Preferences* app label in Django admin.

Preferences can be accessed in Python by importing the ``preferences`` module and traversing to your required preference in the form ``preferences.<ModelName>.<field>``, i.e.::

    from preferences import preferences

    portal_contact_email = preferences.MyPreferences.portal_contact_email

If you've specified the ``preferences.context_processors.preferences_cp`` as a `TEMPLATE_CONTEXT_PROCESSORS <https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATE_CONTEXT_PROCESSORS>`_ you can similarly access your preferences within templates through the ``preferences`` variable, i.e.::

    {{ preferences.MyPreferences.portal_contact_email }}


