Django Options
==============
**Django app allowing users to set app specific options through the admin interface.** 

Provides singleton admin views for Options objects and a simple programming interface to option values.
Singleton views ensures only one option intance is available for each Options class.

Installation
------------

#. Add *options* to your *INSTALLED APPS* setting.

#. Add option url include to the project's url.py file. Make sure to use 'admin/' as the start of the include's path since it will override certain admin views::

    (r'^admin/', include('options.urls')),

Usage
-----
To create options for your app create a model storing your options as normal, with the model inheriting from *options.models.Options*. Also specify 'options.models' as your models module::

    from django.db import models
    from options.model import Options

    class MyOptions(Options):
        __module__ = 'options.models' 
        portal_contact_email = models.EmailField()

Admin options are specified as per usual, no changes are needed. Your options will show up under the *Options* app label in Django admin.

Options can be accessed in python by importing the *options* module and traversing to your required option in the form *options.<ModelName>.field*, i.e.::

    import options

    portal_contact_email = options.MyOptions.portal_contact_email
