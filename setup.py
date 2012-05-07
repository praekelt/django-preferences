from setuptools import setup, find_packages

setup(
    name='django-preferences',
    version='0.0.6',
    description='Django app allowing users to set app specific preferences through the admin interface.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    license='BSD',
    test_suite='setuptest.SetupTestSuite',
    url='http://github.com/praekelt/django-preferences',
    packages=find_packages(),
    tests_require=[
        'django-setuptest>=0.0.6',
    ],
    include_package_data=True,
    install_requires = [
        'Django',
    ],
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
