import json
import logging


logger = logging.getLogger(__name__)


class UriImportStrategyFactory:
    """Factory for a import strategy"""
    JSON_MIME_TYPE = 'application/json'

    @staticmethod
    def create(mime_type: str):
        """Creates Strategy based on mime_type

        Args:
            mime_type (str): mime_type which can be imported with strategy

        Returns:
            Any: strategy that takes a FilePointer and returns
            imported raw json data

        Raises:
            NotImplementedError: if no fitting strategy is found for
                passed mime_type
        """
        if mime_type == UriImportStrategyFactory.JSON_MIME_TYPE:
            return json.load
        else:
            message = f'Mime_type({mime_type}) ' \
                      'has no strategy to import'
            logger.error(message)
            raise NotImplementedError(message)
