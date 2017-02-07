#!/usr/bin/python
# -*- coding: UTF-8 -*-

from setuptools import setup

setup(
    name='gea',
    version='0.2.11',
    description='Gestión de Expedientes de Agrimensores para Django.',
    author='Santiago Pestarini',
    author_email='santiago@pestarini.com.ar',
    url='http://pypi.python.org/pypi/gea/',
    packages=['gea'],
    package_data={
        'gea': [
            'migrations/*',
            'static/*/*',
            'templates/*',
            'templates/*/*',
            'templatetags/*',
        ],
    },
    license='LICENSE',
    long_description=open('README.rst', 'r').read(),
    install_requires=[
        'Django == 1.8.9',
        'django-grappelli == 2.7.3',
        'django-filebrowser == 3.6.4',
        'django-nested-admin == 2.1.8',
        'django-extensions == 1.7.6',
    ],   
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ],
)

