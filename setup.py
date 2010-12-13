#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='cached_cookie',
    version='0.1.1',
    author='Hint Intermedia',
    author_email='it@hint.pl',
    url='http://github.com/hint',
    description = 'Store complex data safely in cookie using a CACHE_BACKEND'
                  'as a storage',
    packages=find_packages(),
    provides=['cached_cookie',],
    include_package_data=False,
    install_requires = []
)