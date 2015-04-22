#!/usr/bin/env python

import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'
parent = os.path.dirname(os.path.dirname(os.path.dirname(
                         os.path.abspath(__file__))))

sys.path.insert(0, parent)

from django.test.simple import DjangoTestSuiteRunner


def runtests():
    DjangoTestSuiteRunner(failfast=False).run_tests([
        'preferences.AdminTestCase',
        'preferences.ModelsTestCase',
        'preferences.ContextProcessorsTestCase',
        'preferences.SingletonManagerTestCase',
        ], verbosity=1, interactive=True)

if __name__ == '__main__':
    runtests()
