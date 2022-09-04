# -*- coding: utf-8 -*-
import abc
import logging
from typing import IO
from uri import URI
import urllib.request as req
import mimetypes

from src.black_fennec.structure.structure import Structure
from src.black_fennec.util.document.resource_type.protocols.https_resource_type import HttpsResourceType
from src.black_fennec.util.document.resource_type.resource_type import ResourceType

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
    def export_structure(self, structure: Structure) -> IO:
        """Export the structure to raw data

        Returns:
            object: Raw data

        Raises:
            NotImplementedError: if subclass did not implement this method
        """
        raise NotImplementedError

    @staticmethod
    def try_determine_mime_type(uri: str, resource_type: str) -> str:
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
        mime_type, _ = mimetypes.guess_type(URI(uri).path)
        if mime_type:
            return mime_type
        if resource_type in ('http', 'https'):
            with req.urlopen(uri) as response:
                structure = response.info()
                mime_type = structure.get_content_type()
            if mime_type:
                return mime_type
        message = 'mime_type could not have been deduced ' \
                  f'automatically of uri({uri})'
        logger.error(message)
        raise ValueError(message)
