# -*- coding: utf-8 -*-
from src.black_fennec.document_system.resource_type.resource_type import ResourceType


class ResourceTypeRegistry:
    """ResourceType Registry Class

    Is a register of all registered resource_types.

    Attributes:
        _resource_types: stores internal resource_types
    """

    def __init__(self):
        """resource_type registry constructor.

        Initializes the _resource_types attribute with empty list
        """
        self._resource_types: dict = {}

    @property
    def resource_types(self):
        """resource_types getter

            Returns:
                dict: of resource_type
        """
        return dict(self._resource_types)

    def register_resource_type(self, resource_type_id: str, resource_type: ResourceType):
        """Function to register a new resource_type

            Args:
                resource_type_id (str): Key at which the ResourceType is to be inserted
                resource_type (ResourceType): future element of the resource_type registry
        """
        assert resource_type_id not in self._resource_types
        self._resource_types[resource_type_id] = resource_type

    def deregister_resource_type(self, resource_type_id):
        """Function to deregister a resource_type from the registry if its class
            matches the passed type

        Args:
            resource_type_id (str): key in the resource_type dict

        """
        del self._resource_types[resource_type_id]
