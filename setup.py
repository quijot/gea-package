#!/usr/bin/python
# -*- coding: UTF-8 -*-

from setuptools import setup

setup(
    name='gea',
    version='0.0.4',
    description='Gestión de Expedientes de Agrimensores para Django.',
    author='Santiago Pestarini',
    author_email='santiago@pestarini.com.ar',
    url='http://pypi.python.org/pypi/gea/',
    packages=['gea'],
    package_data={
        'gea': ['templates/*.html'],
    },
    license='LICENSE',
    long_description=open('README.rst', 'r').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Utilities'
    ],
)

