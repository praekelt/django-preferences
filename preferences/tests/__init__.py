from unittest import TestCase
        
from django import template
from django.template import RequestContext, Template

from preferences import context_processors
from preferences.tests.models import MyPreferences

class ContextProcessorsTestCase(TestCase):

    def test_preferences_cp(self):
        
        class MockRequest(object):
            pass

        context = context_processors.preferences_cp(MockRequest())

        # context should have preferences.
        preferences = context['preferences']

        # preferences should have test MyPreferences object member.
        my_preferences = preferences.MyPreferences
        self.failUnless(isinstance(my_preferences, MyPreferences), "%s should be instance of MyPreferences." % my_preferences) 
        
        # With preferences_cp is loaded as a TEMPLATE_CONTEXT_PROCESSORS templates should have access to preferences object.
        context_instance = RequestContext(MockRequest())
        context = template.Context({
            'request': MockRequest,
        })
        t = Template("{% if preferences %}{{ preferences }}{% endif %}")
        self.failUnless(t.render(context_instance), "preferences should ba available in template context.")

        t = Template("{% if preferences.MyPreferences %}{{ preferences.MyPreferences }}{% endif %}")
        self.failUnless(t.render(context_instance), "MyPreferences should ba available as part of preferences var in template context.")
