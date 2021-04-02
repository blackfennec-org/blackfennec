import logging
import json
from src.core.json_parser import JsonParser

logger = logging.getLogger(__name__)

class BlackFennecViewModel:
    def __init__(self, presenter, navigation_service):
        logger.info("BlackFennecViewModel __init__")
        self._presenter = presenter
        self._navigation_service = navigation_service

    @property
    def presenter(self):
        return self._presenter

    def new(self):
        """Future implementation of new()"""
        logger.warning('new() not yet implemented')

    def open(self, filename):
        """Future implementation of open()"""

        with open(filename, 'r') as file:
            raw = json.load(file)
        structure = JsonParser.from_json(raw)
        self._navigation_service.navigate(None, structure)

    def quit(self):
        """Future implementation of quit()"""
        logger.warning('quit() not yet implemented')

    def save(self):
        """Future implementation of save()"""
        logger.warning('save() not yet implemented')

    def save_as(self):
        """Future implementation of save_as()"""
        logger.warning('save_as() not yet implemented')

    def go_to_store(self):
        """Future implementation of go_to_store()"""
        logger.warning('go_to_store() not yet implemented')

    def about_and_help(self):
        """Future implementation of about_and_help()"""
        logger.warning('about_and_help() not yet implemented')
