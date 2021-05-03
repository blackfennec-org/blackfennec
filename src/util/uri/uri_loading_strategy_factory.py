import logging
import os

from uri import URI
import urllib.request as req

from src.util.uri.uri_type import UriType

logger = logging.getLogger(__name__)


class UriLoadingStrategyFactory:
    @staticmethod
    def create(uri: URI):
        uri_type: UriType = UriType.from_uri(uri)

        if uri_type == UriType.HOST_URI:
            return UriLoadingStrategyFactory._load_host_uri
        elif uri_type == UriType.RELATIVE_PATH:
            return UriLoadingStrategyFactory._load_relative_uri
        elif uri_type == UriType.ABSOLUTE_PATH:
            return UriLoadingStrategyFactory._load_absolute_uri
        else:
            message = f'UriType({uri_type.name}) ' \
                      'has no strategy to load'
            logger.error(message)
            raise NotImplementedError(message)

    @staticmethod
    def _load_host_uri(uri, current_path, mime_type):  # pylint: disable=unused-argument
        path, response = req.urlretrieve(str(uri))
        content_type = response.get_content_type()
        if mime_type != content_type:
            message = f'Mime_type({mime_type}) does not correspond with ' \
                      f'content type({content_type}) of uri({str(uri)})'
            logger.info(message)
        file = open(path, 'r')
        return file

    @staticmethod
    def _load_relative_uri(uri, current_path, mime_type=None):  # pylint: disable=unused-argument
        path = os.path.join(os.path.dirname(current_path), str(uri.path))
        file = open(path, 'r')
        return file

    @staticmethod
    def _load_absolute_uri(uri, current_path=None, mime_type=None):  # pylint: disable=unused-argument
        path = str(uri.path)
        file = open(path, 'r')
        return file
