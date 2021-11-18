# -*- coding: utf-8 -*-
from uri import URI

from src.black_fennec.structure.structure import Structure

import logging
logger = logging.getLogger(__name__)

class Root(Structure):
    """Structure that is the Root of a structure."""

    def __init__(
            self,
            child: Structure = None,
            uri: str = '',
            mime_type: str = ''):
        super().__init__(self)
        self.uri = URI(uri)
        self.mime_type = mime_type
        self._value = child

    @property
    def uri(self) -> str:
        return str(self._uri)

    @uri.setter
    def uri(self, value: str):
        self._uri = URI(value)

    @property
    def mime_type(self):
        return self._mime_type

    @mime_type.setter
    def mime_type(self, value: str):
        self._mime_type = value

    @property
    def parent(self):
        """Readonly property for parent of Root.

        The inherited setter for this property has been overridden
            to disallow changing the parent of the root.

        Raises:
            TypeError: if the setter is called.
        """
        return self

    @parent.setter
    def parent(self, new_parent):
        message = 'cannot set readonly property `parent` on type `Root` '
        logger.error(message)
        raise TypeError(message)

    @property
    def root(self) -> 'Root':
        """Readonly property for root of structure; returns self."""
        return self

    @property
    def value(self) -> Structure:
        return self._value

    @value.setter
    def value(self, child: Structure):
        self._value = child

    def accept(self, visitor):
        return visitor.visit_root(self)
