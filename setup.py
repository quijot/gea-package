#!/usr/bin/python
# -*- coding: UTF-8 -*-

from setuptools import setup

setup(
    name='gea',
    version='0.2.2',
    description='Gestión de Expedientes de Agrimensores para Django.',
    author='Santiago Pestarini',
    author_email='santiago@pestarini.com.ar',
    url='http://pypi.python.org/pypi/gea/',
    packages=['gea'],
    package_data={
        'gea': ['templates/*.html', 'templatetags/*', 'static/*/*'],
    },
    license='LICENSE',
    long_description=open('README.rst', 'r').read(),
    install_requires=[
        'Django == 1.9.6',
        'django-grappelli == 2.8.1',
        'django-nested-admin == 3.0.2',
    ],   
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Utilities'
    ],
)

