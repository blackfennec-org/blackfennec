# -*- coding: utf-8 -*-


class ResourceTypeRegistryMock:

    def __init__(self, resource_types=None):
        if resource_types is None:
            resource_types = dict()
        self._resource_types = resource_types
        self.resource_types_getter_count = 0

        self.register_resource_type_count = 0
        self.register_resource_type_last_resource_type = None
        self.register_resource_type_last_resource_type_key = None

        self.deregister_resource_type_count = 0
        self.deregister_resource_type_last_resource_type_key = None

    @property
    def resource_types(self):
        self.resource_types_getter_count += 1
        return self._resource_types

    def register_resource_type(self, resource_key, resource_type):
        self.register_resource_type_last_resource_type = resource_type
        self.register_resource_type_last_resource_type_key = resource_key
        self.register_resource_type_count += 1

    def deregister_resource_type(self, resource_type_key):
        self.deregister_resource_type_last_resource_type_key = resource_type_key
        self.deregister_resource_type_count += 1
