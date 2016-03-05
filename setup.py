#!/usr/bin/env python
#coding: utf-8
from distutils.core import setup

for cmd in ('egg_info', 'develop'):
    import sys
    if cmd in sys.argv:
        from setuptools import setup

import sys
#from imp import reload
#reload(sys).setdefaultencoding("UTF-8")

setup(
    name='django-robokassa',
    version='1.2.1.2',
    author='Mikhail Korobov',
    author_email='kmike84@gmail.com',

    packages=['robokassa', 'robokassa.migrations'],

    url='https://bitbucket.org/kmike/django-robokassa/',
    license = 'MIT license',
    description = 'Приложение для интеграции платежной системы ROBOKASSA в проекты на Django.',
    long_description = 'Ok', #open('README.rst').read() + u"\n\n" + open('CHANGES.rst').read(),

    requires=['django (>= 1.3)'],

    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ),
)
