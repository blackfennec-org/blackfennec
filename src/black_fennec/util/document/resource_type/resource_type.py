# -*- coding: utf-8 -*-
import abc
import contextlib
import logging
from typing import IO
from uri import URI


class ResourceType(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_resource') and
                callable(subclass.load_resource) and
                hasattr(subclass, 'is_resource_type') and
                callable(subclass.is_resource_type) or
                NotImplemented)

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
