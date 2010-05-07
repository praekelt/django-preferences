from setuptools import setup, find_packages

setup(
    name='django-options',
    version='dev',
    description='Django app allowing users to set app specific settings through the admin interface.',
    author='Praekelt Consulting',
    author_email='dev@praekelt.com',
    url='http://github.com/praekelt/django-options',
    packages = find_packages(),
    include_package_data=True,
)
