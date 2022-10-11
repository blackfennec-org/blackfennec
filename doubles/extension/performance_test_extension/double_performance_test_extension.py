# -*- coding: utf-8 -*-
from src.extension.extension_api import ExtensionApi
from src.visualisation.base.date_time.date_time import DateTime


def create_extension(extension_api: ExtensionApi):
    for i in range(1, 1000):
        extension_api.type_registry.register_type(DateTime.TYPE)


def destroy_extension(extension_api: ExtensionApi):
    extension_api.type_registry.deregister_type(DateTime.TYPE)
