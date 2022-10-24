# -*- coding: utf-8 -*-
import logging

from blackfennec.structure.structure import Structure
from blackfennec.document_system.document import Document
from blackfennec.document_system.document_factory import DocumentFactory
from blackfennec.structure.reference_navigation.navigator import Navigator

logger = logging.getLogger(__name__)


class UriNavigator(Navigator):
    def __init__(self, document_factory: DocumentFactory, uri: str):
        super().__init__()
        self._document_factory = document_factory
        self.uri = uri

    def navigate(self, current: Structure) -> Structure:
        """navigates current structure and returns destination

        Returns:
            Structure: Uri content
        """
        current_structure_root = current.get_root()
        current_structure_document: Document = current_structure_root.get_document()
        document: Document = self._document_factory.create(self.uri, location=current_structure_document.location)
        return document.content

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return self.uri

    def __eq__(self, other):
        if isinstance(other, UriNavigator):
            return self.uri == other.uri

    def __hash__(self):
        return hash(self.uri)
