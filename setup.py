# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='black_fennec',
    version='0.8.0',
    description='Black Fennec',
    long_description='Black Fennec',
    long_description_content_type='text/markdown',
    license='GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007',
    url='https://git.yodabyte.ch/black-fennec/black-fennec.git',
    packages=find_packages(exclude=('tests', 'doubles', 'docs'))
)
