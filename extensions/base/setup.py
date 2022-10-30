# -*- coding: utf-8 -*-

from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
    name="BlackFennec Base Extension",
    version="0.0.1",
    description="Base extension for BlackFennec",
    long_description="Base extension for BlackFennec",
    long_description_content_type='text/markdown',
    license="GPL-3.0",
    packages=find_packages(exclude=('tests', 'doubles', 'docs')),
    entry_points={
        "blackfennec.extension": [
            "base = base"
        ]
    }
)
