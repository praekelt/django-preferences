DATABASE_ENGINE = 'sqlite3'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'preferences',
    'preferences.tests',
]

TEMPLATE_CONTEXT_PROCESSORS = (
    'preferences.context_processors.preferences_cp',
)

ROOT_URLCONF='preferences.tests.urls'
