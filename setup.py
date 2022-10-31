# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='blackfennec',
    version='0.8.1',
    description='Extensible Semi-structured Data Editing Environment',
    long_description='Black Fennec',
    long_description_content_type='text/markdown',
    license='GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007',
    url='https://gitlab.ost.ch/blackfennec/blackfennec.git',
    packages=find_packages(exclude=('tests', 'doubles', 'docs')),
    package_data={'blackfennec': [ '*.ui' ]},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'blackfennec = blackfennec.__main__:main',
        ],
    }
)

