# -*- coding: utf-8 -*-
import json
import logging
import mimetypes
import os
import urllib.request as req

from uri import URI

from src.structure.info import Info
from src.structure.root import Root
from src.util.file.structure_parsing_service import StructureParsingService
from src.util.file.json.uri_type import UriType

logger = logging.getLogger(__name__)


class FileImportService(object):
    JSON_MIME_TYPE = 'application/json'

    def __init__(
            self,
            structure_parser = StructureParsingService,
            loaded_files: dict = None,
            file_import_strategies: dict = None
    ):
        self._loaded_files = loaded_files if loaded_files else dict()
        self._file_import_strategies = \
            file_import_strategies if file_import_strategies else dict()
        self._set_default_import_strategies()
        self._parser = structure_parser

    def _set_default_import_strategies(self):
        if FileImportService.JSON_MIME_TYPE not in self._file_import_strategies:
            self._file_import_strategies[FileImportService.JSON_MIME_TYPE] = json.load

    def load(self, uri_str: str, current_path: str = None, mime_type: str = None):
        uri = URI(uri_str)
        uri_type: UriType = UriType.from_uri(uri)
        if not mime_type:
            mime_type, _ = mimetypes.guess_type(str(uri.path))
            if not mime_type:
                if uri_type.HOST_URI:
                    with req.urlopen(str(uri)) as response:
                        info = response.info()
                        mime_type = info.get_content_type()
        if not mime_type:
            message = 'Please provide mime_type as parameter ' \
                      'as mime_type could not have been deduced ' \
                      'automatically of uri({})'.format(str(uri))
            logger.error(message)
            raise ValueError(message)

        file_id = self._file_identification(uri, mime_type)
        if file_id in self._loaded_files:
            return self._loaded_files[file_id]

        path = None
        if uri_type == UriType.HOST_URI:
            path, response = req.urlretrieve(str(uri))
            content_type = response.get_content_type()
            if mime_type != content_type:
                message = 'Mime_type({}) does not correspond with ' \
                          'content type({}) of uri({})'\
                    .format(
                        mime_type,
                        content_type,
                        str(uri)
                    )
                logger.info(message)
        elif uri_type == UriType.RELATIVE_PATH:
            path = os.path.join(os.path.dirname(current_path), str(uri.path))
        elif uri_type == UriType.ABSOLUTE_PATH:
            path = str(uri.path)
        elif uri_type == UriType.CURRENT_LOCATION:
            path = current_path
        else:
            message = 'Unknown URI-type of uri({})'.format(str(uri))
            logger.error(message)
            raise ValueError(message)

        raw = None
        with open(path, 'r') as file:
            raw = self._file_import_strategies[mime_type](file)
        structure: Info = self._parser.from_json(raw)
        self._loaded_files[file_id] = structure
        file_id_only, _ = file_id
        structure.parent = Root(structure, file_id_only, mime_type)
        return structure

    @staticmethod
    def _file_identification(uri: URI, mime_type: str) -> (str, str):
        type = UriType.from_uri(uri)
        if type == UriType.HOST_URI:
            return str(uri.host) + str(uri.path), mime_type
        return str(uri.path), mime_type

