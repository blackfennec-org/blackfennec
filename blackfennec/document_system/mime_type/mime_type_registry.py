# -*- coding: utf-8 -*-
from blackfennec.document_system.mime_type.mime_type import MimeType


class MimeTypeRegistry:
    """MimeType Registry Class

    Is a register of all registered mime_types.

    Attributes:
        _mime_types: stores internal mime_types
    """

    def __init__(self):
        """mime_type registry constructor.

        Initializes the _mime_types attribute with empty list
        """
        self._mime_types: dict = {}

    @property
    def mime_types(self):
        """mime_types getter

            Returns:
                dict: of mime_type
        """
        return dict(self._mime_types)

    def register_mime_type(self, mime_type_id: str, mime_type: MimeType):
        """Function to register a new mime_type

            Args:
                mime_type_id (str): Key at which the MimeType is to be inserted
                mime_type (MimeType): future element of the mime_type registry
        """
        assert mime_type_id not in self._mime_types
        self._mime_types[mime_type_id] = mime_type

    def deregister_mime_type(self, mime_type_id):
        """Function to deregister a mime_type from the registry if its class
            matches the passed type

        Args:
            mime_type_id (str): key in the mime_type dict

        """
        del self._mime_types[mime_type_id]
