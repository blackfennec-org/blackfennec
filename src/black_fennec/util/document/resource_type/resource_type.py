# -*- coding: utf-8 -*-
import abc
import contextlib
import logging
from typing import IO, List
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

        Returns:
            object: Raw data contained in the resource

        Raises:
            NotImplementedError: if subclass did not implement this method
        """
        raise NotImplementedError

    @staticmethod
    def try_determine_resource_type(resource_uri: str) -> str:
        uri: URI = URI(resource_uri)
        return str(uri.scheme) if uri.scheme else 'file'
