#!/usr/bin/env python3

from distutils.core import setup

setup(
    name='LoadStone',
    version='0.1',
    description='Interface for FFXIV Lodestone',
    author='Sami Elahmadie',
    author_email='s.elahmadie@gmail.com',
    url='https://github.com/Demotivated/loadstone/',
    packages=['api'],
    install_requires=[
        'flask==0.10.1',
        'flask_sqlalchemy==2.0',
        'lxml==3.4.4',
        'psycopg2==2.6.1',
        'requests==2.7.0',
    ]
)
