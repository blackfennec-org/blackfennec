# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import gi

gi.require_version('AppStream', '1.0')

from gi.repository import AppStream

from blackfennec.util.meta_info import BlackFennecMetaInfo

meta_info = BlackFennecMetaInfo()

setup(
    name=meta_info.component.get_name(),
    version=meta_info.get_current_release().get_version(),
    description=meta_info.component.get_summary(),
    long_description=meta_info.get_plain_description(),
    long_description_content_type='text/markdown',
    license=meta_info.component.get_project_license(),
    url=meta_info.component.get_url(AppStream.UrlKind.HOMEPAGE),
    packages=find_packages(exclude=('tests', 'doubles', 'docs')),
    entry_points={
        "console_scripts": [
            "blackfennec = blackfennec:main"
        ],
    }
)
