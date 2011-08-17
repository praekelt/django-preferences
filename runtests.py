import sys

from django.conf import settings

if not settings.configured:
    settings.configure(
        DATABASE_ENGINE='sqlite3',
        INSTALLED_APPS=[
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sites',
            'preferences',
            'preferences.tests',

        ],
        TEMPLATE_CONTEXT_PROCESSORS=(
            'preferences.context_processors.preferences_cp',
        ),
        ROOT_URLCONF='preferences.tests.urls',
    )
 
from django.test.simple import run_tests
 
def runtests():
    failures = run_tests(('preferences',), verbosity=1, interactive=True)
    sys.exit(failures)
 
if __name__ == '__main__':
    runtests()
