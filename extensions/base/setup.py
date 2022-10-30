# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="blackfennec_extensions_base",
    version="0.0.1",
    description="Base extension for BlackFennec",
    long_description="Base extension for BlackFennec",
    long_description_content_type='text/markdown',
    license="GPL-3.0",
    packages=find_packages(exclude=('tests', 'doubles', 'docs')),
    include_package_data=True,
    package_data={'': [ '*.ui', '*.json' ]},
    entry_points={
        "blackfennec.extension": [
            "base = base"
        ]
    }
)
