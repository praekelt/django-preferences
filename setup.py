from setuptools import setup, find_packages
from setuptools.command.test import test

def run_tests(self):
    from setuptest.runtests import runtests
    return runtests(self)
test.run_tests = run_tests

setup(
    name='django-preferences',
    version='0.0.5',
    description='Django app allowing users to set app specific preferences through the admin interface.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    license='BSD',
    test_suite = 'preferences.tests',
    url='http://github.com/praekelt/django-preferences',
    packages=find_packages(),
    tests_require=[
        'django-setuptest',
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
