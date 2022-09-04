# -*- coding: utf-8 -*-
from typing import Type, Optional
from uri import URI

from src.black_fennec.structure.root_factory import RootFactory
from src.black_fennec.structure.structure import Structure
from src.black_fennec.util.document.mime_type.mime_type import MimeType
from src.black_fennec.util.document.resource_type.resource_type import ResourceType


class Document:
    def __init__(
            self,
            mime_type: MimeType,
            resource_type: ResourceType,
            root_factory: Type[RootFactory] = RootFactory,
            uri: str = '',
            location: str = ''
    ):
        self.uri: URI = URI(uri)
        self.location: URI = URI(location)
        self.mime_type: MimeType = mime_type
        self._root_factory: Type[RootFactory] = root_factory
        self.resource_type: ResourceType = resource_type
        self.content: Optional[Structure] = None

    @property
    def mime_type(self) -> MimeType:
        return self._mime_type

    @mime_type.setter
    def mime_type(self, value: MimeType):
        self._mime_type = value

    @property
    def resource_type(self) -> ResourceType:
        return self._resource_type

    @resource_type.setter
    def resource_type(self, value: ResourceType):
        self._resource_type = value

    @property
    def uri(self) -> str:
        return str(self._uri)

    @uri.setter
    def uri(self, value: str):
        self._uri = URI(value)

    @property
    def location(self) -> str:
        return str(self._location)

    @location.setter
    def location(self, value: str):
        self._location = URI(value)

    @property
    def content(self) -> Structure:
        if self._content is None:
            self._load_content()
        return self._content

    @content.setter
    def content(self, content: Structure):
        self._root_factory.make_root(content, document=self)
        self._content = content

    def _load_content(self):
        with self.resource_type.load_resource(self) as raw:
            structure = self.mime_type.import_structure(raw)
        self.content = structure
