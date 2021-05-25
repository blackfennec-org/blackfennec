# -*- coding: utf-8 -*-
from src.extension.extension_api import ExtensionApi
from src.visualisation.base.address.address_bidder import AddressBidder


def create_extension(extension_api: ExtensionApi):
    for i in range(1, 1000):
        extension_api.type_registry.register_type(AddressBidder())


def destroy_extension(extension_api: ExtensionApi):
    extension_api.type_registry.deregister_type(AddressBidder)
