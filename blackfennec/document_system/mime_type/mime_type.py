# -*- coding: utf-8 -*-
import abc
import logging
import mimetypes
from typing import IO
from urllib.parse import urlparse
from blackfennec.document_system.resource_type.resource_type import ResourceType

from blackfennec.structure.structure import Structure

logger = logging.getLogger(__name__)


class MimeType(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def mime_type_id(self) -> str:
        """Identification of mime type via ID

        Returns:
            str: mime type ID

        Raises:
            NotImplementedError: if subclass did not implement this property
        """
        raise NotImplementedError

    @abc.abstractmethod
    def import_structure(self, data: IO) -> Structure:
        """Import the structure from IO data

        Returns:
            Structure: Structure contained in raw data

        Raises:
            NotImplementedError: if subclass did not implement this method
        """
        raise NotImplementedError

    @abc.abstractmethod
    def export_structure(self, output: IO, structure: Structure):
        """Export the structure to output IO

        Raises:
            NotImplementedError: if subclass did not implement this method
        """
        raise NotImplementedError

    @staticmethod
    def try_determine_mime_type(uri: str, resource_type: ResourceType) -> str:
        """Get mime_type through different approaches.

        Tries guessing the mime_type from the URI ending, then by retrieving
        the content-type of the URI if the UriType is HOST_URI.

        Args:
            uri (str): of which the mime_type should be searched
            resource_type (ResourceType): type of the passed uri
        Returns:
            str: mime_type
        Raises:
            ValueError: if no mime_type could have been guessed automatically.
        """
        parsed_uri = urlparse(uri)
        mime_type, _ = mimetypes.guess_type(parsed_uri.path)
        if mime_type:
            return mime_type
        mime_type = resource_type.guess_mime_type(uri)
        if mime_type:
            return mime_type

        message = 'mime_type could not have been deduced ' \
                  f'automatically of uri({uri})'
        logger.error(message)
        raise ValueError(message)
