# -*- coding: utf-8 -*-
from blackfennec.structure.structure import Structure
from blackfennec.document_system.mime_type.mime_type import MimeType
from blackfennec.document_system.resource_type.resource_type import ResourceType


class Document:
    """A document can contain a structure which is lazy loaded from a given URI via it's resource and mime type"""

    def __init__(
            self,
            document_registry,
            mime_type: MimeType,
            resource_type: ResourceType,
            uri: str = '',
            location: str = ''
    ):
        """ Create a new document
            Content is lazy loaded on access to the content property

        Args:
            mime_type (MimeType): The mime type of the document
            resource_type (ResourceType): The resource type of the document
            root_factory (Type[RootFactory]): The root factory to use for the document
            uri (str): The uri of the document
            location (str): The location of the document
        """
        self.uri: str = uri
        self.location: str = location
        self.mime_type: MimeType = mime_type
        self._document_registry = document_registry
        self.resource_type: ResourceType = resource_type
        self._content = None

    @property
    def mime_type(self) -> MimeType:
        """Get the mime type of the document"""
        return self._mime_type

    @mime_type.setter
    def mime_type(self, value: MimeType):
        """Set the mime type of the document"""
        self._mime_type = value

    @property
    def resource_type(self) -> ResourceType:
        """Get the resource type of the document"""
        return self._resource_type

    @resource_type.setter
    def resource_type(self, value: ResourceType):
        """Set the resource type of the document"""
        self._resource_type = value

    @property
    def uri(self) -> str:
        """Get the uri of the document"""
        return self._uri

    @uri.setter
    def uri(self, value: str):
        """Set the uri of the document"""
        self._uri = value

    @property
    def location(self) -> str:
        """Get the location of the document"""
        return self._location

    @location.setter
    def location(self, value: str):
        """Set the location of the document"""
        self._location = value

    @property
    def content(self) -> Structure:
        """Get the content of the document"""
        if self._content is None:
            self._load_content()
        return self._content

    @content.setter
    def content(self, content: Structure):
        """Set the content of the document"""
        self._content = content
        self._document_registry.register_document(self)

    def _load_content(self):
        """Load the content of the document"""
        with self.resource_type.load_resource(self, "r") as raw:
            structure = self.mime_type.import_structure(raw)
        self.content = structure

    def save(self):
        """Save the document"""
        with self.resource_type.load_resource(self, "w") as raw:
            self.mime_type.export_structure(raw, self.content)
