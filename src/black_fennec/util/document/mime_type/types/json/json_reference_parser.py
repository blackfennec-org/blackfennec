# -*- coding: utf-8 -*-
import logging
import re
from os import path
from urllib.parse import urlparse

from src.black_fennec.util.document.mime_type.types.json.json_pointer_parser import JsonPointerParser
from src.black_fennec.structure.reference_navigation.navigator import Navigator
from src.black_fennec.structure.reference_navigation.uri_navigator import UriNavigator

logger = logging.getLogger(__name__)


class JsonReferenceParser:
    """Parses Json References"""

    JSON_REFERENCE_KEY = '$ref'
    ABSOLUTE_POINTER_PATTERN = \
        re.compile('^(/?(([^/~])|(~[01]))*)+$')
    RELATIVE_POINTER_PATTERN = \
        re.compile('^([0-9]+([+][0-9]+|[-][0-9]+)?)(/(([^/~])|(~[01]))*)*$')

    def __init__(self, document_factory):
        self._document_factory = document_factory

    def parse(self, raw: dict) -> list[Navigator]:
        reference = raw[self.JSON_REFERENCE_KEY]
        parsed_uri = urlparse(reference)
        result_navigator_list: list[Navigator] = []
        if parsed_uri.netloc:
            result_navigator_list.append(UriNavigator(self._document_factory, reference))
        elif parsed_uri.path:
            result_navigator_list.append(UriNavigator(self._document_factory, reference))
        if parsed_uri.fragment:
            if not len(result_navigator_list) and JsonPointerParser.is_relative_json_pointer(parsed_uri.fragment):
                result_navigator_list += JsonPointerParser.parse_relative_pointer(parsed_uri.fragment)
            elif JsonPointerParser.is_absolute_json_pointer(parsed_uri.fragment):
                result_navigator_list += JsonPointerParser.parse_absolute_pointer(parsed_uri.fragment)

        return result_navigator_list

    @classmethod
    def is_json_reference(cls, raw: dict):
        if cls.JSON_REFERENCE_KEY in raw.keys():
            return True
        else:
            return False
