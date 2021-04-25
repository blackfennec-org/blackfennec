# -*- coding: utf-8 -*-
import logging

from uri import URI

from src.structure.info import Info
from src.structure.root import Root
from src.util.file.json.json_pointer import JsonPointer, JsonPointerType, is_relative_json_pointer
from src.util.file.json.uri_type import UriType

logger = logging.getLogger(__name__)


class JsonReferenceResolvingService:

    def __init__(self, file_loading_service):
        self._cached_structure = dict()
        self._file_import_service = file_loading_service

    def resolve(self, reference: str, source: Info = None):
        if reference in self._cached_structure:
            return self._cached_structure[reference]
        uri = URI(reference)
        uri_type = UriType.from_uri(uri)
        json_pointer = None
        relative_json_pointer = False
        if uri.fragment:
            json_pointer = JsonPointer(
                uri.fragment,
                JsonPointerType.ABSOLUTE_JSON_POINTER
            )
        elif not uri.host and is_relative_json_pointer(reference):
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
            structure = self._load_file(uri, source)

        if json_pointer:
            structure = json_pointer.resolve_from(structure)
        self._cached_structure[reference] = structure
        return structure

    def _load_file(
            self,
            uri: URI,
            source: Info = None
    ) -> (Info, str):
        root: Root = source.root
        current_path = root.uri
        structure = self._file_import_service.load(str(uri), current_path)
        return structure
