# -*- coding: utf-8 -*-
import logging
import mimetypes
import urllib.request as req

from uri import URI

from src.black_fennec.structure.info import Info
from src.black_fennec.structure.root import Root
from src.black_fennec.util.uri.structure_parsing_service import StructureParsingService
from src.black_fennec.util.uri.uri_type import UriType
from src.black_fennec.util.uri.uri_import_strategy_factory import UriImportStrategyFactory
from src.black_fennec.util.uri.uri_loading_strategy_factory import UriLoadingStrategyFactory

logger = logging.getLogger(__name__)


class UriImportService:
    """Service to Import Uri into Info composition"""

    def __init__(
            self,
            structure_parser: StructureParsingService,
            uri_loading_strategy_factory: UriLoadingStrategyFactory,
            uri_import_strategy_factory: UriImportStrategyFactory,
            uri_cache: dict = None,
    ):
        """UriImportService Constructor

        Args:
            structure_parser (StructureParsingService): Service to
                parse raw json structure to Info composition.
            uri_loading_strategy_factory (UriLoadingStrategyFactory):
                Service to load uri and return FilePointer of loaded URI.
            uri_import_strategy_factory (UriImportStrategyFactory):
                Service to import FilePointer into raw json structure.
            uri_cache (dict):
                Cache of already resolved URI's containing complete
                    Info compositions to directly return.
        """
        self._parser = structure_parser
        self._loading_strategy_factory = uri_loading_strategy_factory
        self._import_strategy_factory = uri_import_strategy_factory
        self._uri_cache = uri_cache if uri_cache else dict()

    def load(
            self,
            uri: URI,
            current_path: str = None,
            mime_type: str = None
    ):
        """Loads data from URI into Info composition
            with the help of strategies provided to
            UriImportService.

        Args:
            uri (URI): containing the location of the data
                to load into the application.
            current_path (str): Path from which the URI should be
                resolved. Required if an absolute path is contained
                in the uri.
            mime_type (str): provided if known, can also be guessed
                during load if unknown, might be required if guessing
                the mime_type was not possible.

        Returns:
            Info: composition of Infos that were retrieved from uri.
        """
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
            structure.parent = Root(
                structure,
                uri_id_without_mime_type,
                mime_type
            )
            return structure

    @staticmethod
    def _uri_identification(
            uri: URI,
            uri_type: UriType,
            mime_type: str
    ) -> (str, str):
        """Creates identifier for uri together with mime_type

        Args:
            uri (URI): to create identifier from
            uri_type (UriType): type of passed uri
            mime_type (str): mime_type of uri
        Returns:
            (str, str): tuple containing a identification of the uri
                based on the mime_type and the uri
        """
        if uri_type == UriType.HOST_URI:
            return str(uri.host) + str(uri.path), mime_type
        return str(uri.path), mime_type

    @staticmethod
    def _get_mime_type(uri: URI, uri_type: UriType, mime_type):
        """Helper function to get mime_type through different approaches.

        Tries guessing the mime_type from the URI ending, then by retrieving
            the content-type of the URI if the UriType is HOST_URI.
        Args:
            uri (URI): of which the mime_type should be searched
            uri_type (UriType): type of the passed uri
            mime_type (str): if already set, then immediately is returned.

        Returns:
            str: mime_type

        Raises:
            ValueError: if no mime_type could have been guessed automatically.
        """
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
