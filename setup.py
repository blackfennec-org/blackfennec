# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='Black Fennec',
    version='0.8.0',
    description='Extensible Semi-structured Data Editing Environment',
    long_description='Black Fennec',
    long_description_content_type='text/markdown',
    license='GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007',
    url='https://gitlab.ost.ch/blackfennec/blackfennec.git',
    packages=find_packages(exclude=('tests', 'doubles', 'docs'))
)
