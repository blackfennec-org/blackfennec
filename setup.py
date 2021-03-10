# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name="black-fennec",
    version="0.1.1",
    description="Black Fennec",
    long_description="Black Fennec",
    long_description_content_type="text/markdown",
    license="GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007",
    url="https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec.git",
    packages=find_packages(exclude=("tests", "docs"))
)
