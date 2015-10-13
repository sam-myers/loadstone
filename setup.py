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
        'flask',
        'flask_sqlalchemy',
        'lxml',
        'psycopg2',
        'pytest',
        'pytest-flask',
        'requests',
        'sphinx',
        'sphinx-rtd-theme',
    ]
)
