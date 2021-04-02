import logging


logger = logging.getLogger(__name__)

class BlackFennecViewModel:
    def __init__(self, presenter):
        logger.info("BlackFennecViewModel __init__")
        self._presenter = presenter

    @property
    def presenter(self):
        return self._presenter

    def new(self):
        logger.warning('new() not yet implemented')

    def open(self):
        logger.warning('open() not yet implemented')

    def quit(self):
        logger.warning('quit() not yet implemented')

    def save(self):
        logger.warning('save() not yet implemented')

    def save_as(self):
        logger.warning('save_as() not yet implemented')

    def go_to_store(self):
        logger.warning('go_to_store() not yet implemented')

    def about_and_help(self):
        logger.warning('about_and_help() not yet implemented')
