# -*- coding: utf-8 -*-
import logging

from uri import URI

from src.black_fennec.structure.structure import Structure
from src.black_fennec.util.json.json_pointer import JsonPointer, JsonPointerType, is_relative_json_pointer
from src.black_fennec.util.uri.uri_type import UriType

logger = logging.getLogger(__name__)


class JsonReferenceResolvingService:
    """Service resolves a JsonReference"""

    def __init__(self, uri_import_service):
        self._cached_structure = {}
        self._uri_import_service = uri_import_service

    def resolve(self, uri: URI, source: Structure = None) -> Structure:
        """Resolves JsonReference in the form of an URI
            to a Structure.

        Args:
            uri (URI): uri containing JsonReference
            source (Optional[Structure]): Source is required for some
                types of JsonReference to be able to navigate from.
        Returns:
            Structure: Destination of JsonReference
        """
        if str(uri) in self._cached_structure:
            return self._cached_structure[str(uri)]
        uri_type = UriType.from_uri(uri)
        json_pointer = None
        relative_json_pointer = False
        if uri.fragment:
            json_pointer = JsonPointer(
                uri.fragment,
                JsonPointerType.ABSOLUTE_JSON_POINTER
            )
        elif not uri.host and is_relative_json_pointer(str(uri)):
            relative_json_pointer = True
            json_pointer = JsonPointer(
                str(uri.path),
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
            self._cached_structure[str(uri)] = structure

        return structure

    def _load_structure_from_uri(
            self,
            uri: URI,
            source: Structure = None
    ) -> (Structure, str):
        root = source.get_root()
        current_path = root.get_uri()
        structure = self._uri_import_service.load(uri, current_path)
        return structure
