# -*- coding: utf-8 -*-
import logging
import re
from typing import Type
from urllib.parse import urlparse

from src.black_fennec.document_system.mime_type.json.json_pointer_serializer import JsonPointerSerializer
from src.black_fennec.structure.reference_navigation.navigator import Navigator
from src.black_fennec.structure.reference_navigation.uri_navigator import UriNavigator

logger = logging.getLogger(__name__)


class JsonReferenceSerializer:
    """Parses Json References"""

    REFERENCE_KEY = '$ref'
    ABSOLUTE_POINTER_PATTERN = \
        re.compile('^(/?(([^/~])|(~[01]))*)+$')
    RELATIVE_POINTER_PATTERN = \
        re.compile('^([0-9]+([+][0-9]+|[-][0-9]+)?)(/(([^/~])|(~[01]))*)*$')

    def __init__(self, document_factory, pointer_serializer: Type[JsonPointerSerializer]):
        self._document_factory = document_factory
        self._pointer_serializer = pointer_serializer

    def serialize(self, navigator_list: list[Navigator]) -> dict:
        """Serializes a list of navigators into a json reference string

        Arguments:
            navigator_list (list[Navigator]): A list of navigators
        Returns:
            str: A json reference string
        """
        if navigator_list is None or len(navigator_list) == 0:
            return {self.REFERENCE_KEY: None}
        first_element = navigator_list[0]
        if isinstance(first_element, UriNavigator):
            return {self.REFERENCE_KEY: first_element.uri}

        return {self.REFERENCE_KEY: '#/' + self._pointer_serializer.serialize(navigator_list)}

    def deserialize(self, raw: dict) -> list[Navigator]:
        reference = raw[self.REFERENCE_KEY]
        parsed_uri = urlparse(reference)
        result_navigator_list: list[Navigator] = []
        if parsed_uri.netloc:
            result_navigator_list.append(UriNavigator(self._document_factory, reference))
        elif parsed_uri.path:
            result_navigator_list.append(UriNavigator(self._document_factory, reference))
        if parsed_uri.fragment:
            if not len(result_navigator_list) and self._pointer_serializer.is_relative_json_pointer(
                    parsed_uri.fragment):
                result_navigator_list += self._pointer_serializer.deserialize_relative_pointer(parsed_uri.fragment)
            elif self._pointer_serializer.is_absolute_json_pointer(parsed_uri.fragment):
                result_navigator_list += self._pointer_serializer.deserialize_absolute_pointer(parsed_uri.fragment)

        return result_navigator_list

    @classmethod
    def is_reference(cls, raw: dict):
        if cls.REFERENCE_KEY in raw.keys() and len(raw.keys()) == 1:
            return True
        else:
            return False
