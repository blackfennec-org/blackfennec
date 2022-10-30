# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from src.black_fennec.util.meta_info import BlackFennecMetaInfo

meta_info = BlackFennecMetaInfo()

setup(
    name=meta_info.get_name(),
    version=meta_info.get_version(),
    description=meta_info.get_summary(),
    long_description=meta_info.get_description(),
    long_description_content_type='text/markdown',
    license=meta_info.get_license(),
    url=meta_info.get_home_page(),
    packages=find_packages(exclude=('tests', 'doubles', 'docs')),
)

