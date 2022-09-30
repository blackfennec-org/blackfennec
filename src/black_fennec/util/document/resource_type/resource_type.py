# -*- coding: utf-8 -*-
import abc
import contextlib
from typing import IO, List
from urllib.parse import urlparse

from uri import URI


class ResourceType(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def protocols(self) -> List[str]:
        """List of protocols supported by Resource Type

        Returns:
            List[str]: protocols supported

        Raises:
            NotImplementedError: if subclass did not implement this property
        """
        raise NotImplementedError

    @contextlib.contextmanager
    @abc.abstractmethod
    def load_resource(self, document: 'Document') -> IO:
        """Load the resource

        Arguments:
            document (Document): document to load
        Returns:
            IO: loaded resource
        Raises:
            NotImplementedError: if subclass did not implement this method
        """
        raise NotImplementedError

    @staticmethod
    def try_determine_resource_type(resource_uri: str) -> str:
        parsed_uri = urlparse(resource_uri)
        return str(parsed_uri.scheme) if parsed_uri.scheme else 'file'
