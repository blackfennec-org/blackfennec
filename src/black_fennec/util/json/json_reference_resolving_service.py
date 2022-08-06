# -*- coding: utf-8 -*-
import logging
import os.path

from uri import URI

from src.black_fennec.structure.structure import Structure
from src.black_fennec.util.document.document_factory import DocumentFactory
from src.black_fennec.util.document.mime_type.mime_type import MimeType
from src.black_fennec.util.document.resource_type.resource_type import ResourceType
from src.black_fennec.util.json.json_pointer import JsonPointer, JsonPointerType, is_relative_json_pointer
from src.black_fennec.util.uri.uri_type import UriType

logger = logging.getLogger(__name__)


class JsonReferenceResolvingService:
    """Service resolves a JsonReference"""

    def __init__(self, document_factory: DocumentFactory):
        self._cached_structure = {}
        self._document_factory: DocumentFactory = document_factory

    def resolve(self, uri: str, source: Structure = None) -> Structure:
        """Resolves JsonReference in the form of an URI
            to a Structure.

        Args:
            uri (str): uri containing JsonReference
            source (Optional[Structure]): Source is required for some
                types of JsonReference to be able to navigate from.
        Returns:
            Structure: Destination of JsonReference
        """
        if uri in self._cached_structure:
            return self._cached_structure[uri]
        parsed_uri = URI(uri)
        uri_type = UriType.from_uri(parsed_uri)
        json_pointer = None
        relative_json_pointer = False
        if parsed_uri.fragment:
            json_pointer = JsonPointer(
                parsed_uri.fragment,
                JsonPointerType.ABSOLUTE_JSON_POINTER
            )
        elif not parsed_uri.host and is_relative_json_pointer(uri):
            relative_json_pointer = True
            json_pointer = JsonPointer(
                str(parsed_uri.path),
                JsonPointerType.RELATIVE_JSON_POINTER
            )

        if (
                uri_type == UriType.CURRENT_LOCATION or
                relative_json_pointer
        ):
            structure = source
        else:
            structure = self._load_structure_from_uri(uri, source)

        if json_pointer:
            structure = json_pointer.resolve_from(structure)

        if uri_type in (UriType.HOST_URI, UriType.ABSOLUTE_PATH):
            self._cached_structure[uri] = structure

        return structure

    def _load_structure_from_uri(
            self,
            uri: str,
            source: Structure = None
    ) -> (Structure, str):
        root = source.get_root()
        document = root.get_document()
        current_path = os.path.dirname(document.uri)
        resource_type = ResourceType.try_determine_resource_type(uri)
        mime_type = MimeType.try_determine_mime_type(uri, resource_type)

        message = f'Loading structure from URI({uri}) ' \
                  f'with automatically determined ResourceType({resource_type}) ' \
                  f'and automatically determined MimeType({mime_type})'
        logger.debug(message)

        document = self._document_factory.create(
            uri,
            resource_type=resource_type, mime_type=mime_type,
            location=current_path
        )
        document.load_content()
        return document.content
