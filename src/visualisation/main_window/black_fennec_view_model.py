import logging
import mimetypes

from src.structure.info import Info
from src.structure.root import Root

logger = logging.getLogger(__name__)


class BlackFennecViewModel:
    """BlackFennec MainWindow view_model.

    view_model to which views can dispatch calls
    that include business logic.

    Attributes:
        _presenter (InfoPresenter): stores injected presenter
        _navigation_service (NavigationService): stores injected
            navigation service
    """
    def __init__(self, presenter, navigation_service, file_import_service):
        """BlackFennecViewModel constructor.

        Args:
            presenter (InfoPresenter): presenter
            presenter (navigation_service): navigation service
        """
        logger.info('BlackFennecViewModel __init__')
        self._presenter = presenter
        self._navigation_service = navigation_service
        self._file_import_service = file_import_service

    @property
    def presenter(self):
        return self._presenter

    def new(self):
        """Future implementation of new()"""
        logger.warning('new() not yet implemented')

    def open(self, filename: str):
        """Opens a file
        specified by the filename

        Args:
            filename (str): Path of the file to open
        """
        structure: Info = self._file_import_service.load(filename)
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
