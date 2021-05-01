# -*- coding: utf-8 -*-
import logging
import mimetypes
import urllib.request as req

from uri import URI

from src.structure.info import Info
from src.structure.root import Root
from src.util.uri.structure_parsing_service import StructureParsingService
from src.util.uri.uri_type import UriType
from src.util.uri.uri_import_strategy_factory import UriImportStrategyFactory
from src.util.uri.uri_loading_strategy_factory import UriLoadingStrategyFactory

logger = logging.getLogger(__name__)


class UriImportService:

    def __init__(
            self,
            structure_parser: StructureParsingService,
            uri_loading_strategy_factory: UriLoadingStrategyFactory,
            uri_import_strategy_factory: UriImportStrategyFactory,
            uri_cache: dict = None,
    ):
        self._parser = structure_parser
        self._loading_strategy_factory = uri_loading_strategy_factory
        self._import_strategy_factory = uri_import_strategy_factory
        self._uri_cache = uri_cache if uri_cache else dict()

    def load(self, uri_str: str, current_path: str = None, mime_type: str = None):
        uri = URI(uri_str)
        uri_type: UriType = UriType.from_uri(uri)
        mime_type = self._get_mime_type(uri, uri_type, mime_type)

        uri_id = self._uri_identification(uri, uri_type, mime_type)
        if uri_id in self._uri_cache:
            return self._uri_cache[uri_id]

        loading_function = self._loading_strategy_factory.create(uri)
        with loading_function(uri, current_path, mime_type) as file:
            import_function = self._import_strategy_factory.create(mime_type)
            raw = import_function(file)

            structure: Info = self._parser.from_json(raw)
            self._uri_cache[uri_id] = structure
            uri_id_without_mime_type, _ = uri_id
            structure.parent = Root(structure, uri_id_without_mime_type, mime_type)
            return structure

    @staticmethod
    def _uri_identification(uri: URI, uri_type: UriType, mime_type: str) -> (str, str):
        if uri_type == UriType.HOST_URI:
            return str(uri.host) + str(uri.path), mime_type
        return str(uri.path), mime_type

    @staticmethod
    def _get_mime_type(uri: URI, uri_type: UriType, mime_type):
        if mime_type:
            return mime_type
        mime_type, _ = mimetypes.guess_type(str(uri.path))
        if mime_type:
            return mime_type
        if uri_type.HOST_URI:
            with req.urlopen(str(uri)) as response:
                info = response.info()
                mime_type = info.get_content_type()
            if mime_type:
                return mime_type
        message = 'Please provide mime_type as parameter ' \
                  'as mime_type could not have been deduced ' \
                  f'automatically of uri({str(uri)})'
        logger.error(message)
        raise ValueError(message)