Django Preferences
==================
**Django app allowing users to set app specific preferences through the admin interface.** 

Provides singleton admin views for Preferences objects and a simple interface to preference values.
Singleton views ensures only one preference intance is available for each Preferences class.

Installation
------------

#. Add **preferences** to your **INSTALLED APPS** setting.

#. Add preferences url include to the project's url.py file BEFORE your admin urls include statement. Make sure to use 'admin/' as the start of the include's path since it will override certain admin views::

    (r'^admin/', include('preferences.urls')),

Usage
-----
To create preferences for your app create a model storing your preferences as normal, with the model inheriting from **preferences.models.Preferences**. Also specify **preferences.models** as your models module::

    from django.db import models
    from preferences.models import Preferences

    class MyPreferences(Preferences):
        __module__ = 'preferences.models' 
        portal_contact_email = models.EmailField()

Admin classes are specified as per usual, no changes are needed. Your preferences will show up under the **Preferences** app label in Django admin.

Preferences can be accessed in python by importing the **preferences** module and traversing to your required preferences in the form **preferences.<ModelName>.<field>**, i.e.::

    from preferences import preferences

    portal_contact_email = preferences.MyPreferences.portal_contact_email



Change Log
----------

0.0.3
~~~~~
#. Spelling correction, thanks tiktuk.

0.0.2
~~~~~
#. Doc update to indicate importance of placing url include before admin url include.

0.0.1
~~~~~
#. First super alpha release.

