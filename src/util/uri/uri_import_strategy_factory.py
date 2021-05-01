import json
import logging


logger = logging.getLogger(__name__)


class UriImportStrategyFactory:
    JSON_MIME_TYPE = 'application/json'

    @staticmethod
    def create(mime_type):
        if mime_type == UriImportStrategyFactory.JSON_MIME_TYPE:
            return json.load
        else:
            message = f'Mime_type({mime_type}) ' \
                      'has no strategy to import'
            logger.error(message)
            raise NotImplementedError(message)
