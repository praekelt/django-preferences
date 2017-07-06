from setuptools import setup, find_packages

setup(
    name="django-preferences",
    version="0.2",
    description="Django app allowing users to set app specific preferences through the admin interface.",
    long_description=open("README.rst", "r").read() + open("AUTHORS.rst", "r").read() + open("CHANGELOG.rst", "r").read(),
    author="Praekelt Consulting",
    author_email="dev@praekelt.com",
    license="BSD",
    test_suite="setuptest.setuptest.SetupTestSuite",
    url="http://github.com/praekelt/django-preferences",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django"
    ],
    tests_require=[
        "tox"
    ],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
