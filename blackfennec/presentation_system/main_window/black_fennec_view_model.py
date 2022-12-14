import logging
import os
from typing import Optional

from blackfennec.document_system.mime_type.mime_type import MimeType
from blackfennec.document_system.resource_type.resource_type import ResourceType
from blackfennec.presentation_system.about_window.about_window_view_model \
    import AboutWindowViewModel
from blackfennec.presentation_system.main_window.document_tab import DocumentTab
from blackfennec.presentation_system.navigation_service.navigation_service \
    import NavigationService
from blackfennec.util.observable import Observable
from blackfennec.util.service_locator import ServiceLocator

logger = logging.getLogger(__name__)


class BlackFennecViewModel(Observable):

    def __init__(
            self,
            services: ServiceLocator,
    ):
        super().__init__()
        self._services = services
        self._presenter_registry = services.presenter_registry
        self._interpretation_service = services.interpretation_service
        self._document_factory = services.document_factory
        self._ui_service = services.ui_service

        self.tabs = set()
        self._current_directory: Optional[str] = None

    @property
    def current_directory(self):
        return self._current_directory

    @current_directory.setter
    def current_directory(self, directory: str):
        self._current_directory = directory
        self._notify('open_directory', self._current_directory)

    def can_handle_uri(self, uri: str) -> bool:
        try:
            resource_type_identifier = ResourceType.try_determine_resource_type(
                uri
            )
            resource_type = \
                self._services.resource_type_registry.resource_types[
                    resource_type_identifier
                ]

            mime_type_identifier = MimeType.try_determine_mime_type(
                uri, resource_type)
            return mime_type_identifier in \
                   self._services.mime_type_registry.mime_types
        except Exception as e:
            logger.debug(e)
            return False

    def open(self, uri: str):
        if os.path.isdir(uri):
            self.current_directory = uri
        else:
            self.open_file(uri)

    def open_file(self, uri: str):
        """Opens a file
        specified by the filename

        Args:
            uri (str): URI of the file to open
        """
        navigation_service = NavigationService()
        tab = DocumentTab(
            self._presenter_registry,
            self._document_factory,
            navigation_service,
            uri
        )
        self.tabs.add(tab)
        self._notify('open_file', tab)

    def close_file(self, tab: DocumentTab):
        """Closes a file

        Args:
            tab (DocumentTab): tab to close
        """
        self.tabs.remove(tab)
        self._notify('close_file', tab)

    def save(self, tab: DocumentTab):
        """Saves the passed file"""
        tab.save_document()

    def save_as(self, tab: DocumentTab, uri: str):
        """Saves the passed tab under new path"""
        tab.save_document_as(uri)

    def save_all(self):
        """Saves all open files"""
        for tab in self.tabs:
            self.save(tab)

    def get_about_window_view_model(self):
        return AboutWindowViewModel()

    def undo(self, tab: DocumentTab):
        if tab.history.can_undo():
            tab.history.undo()
        else:
            raise ValueError('Cannot undo')

    def redo(self, tab: DocumentTab):
        if tab.history.can_redo():
            tab.history.redo()
        else:
            raise ValueError('Cannot redo')

    def copy(self) -> 'BlackFennecViewModel':
        return BlackFennecViewModel(self._services)

    def attach_tab(self, tab: DocumentTab):
        if tab not in self.tabs:
            self.tabs.add(tab)
        else:
            raise AssertionError('Tab already attached')

    def detach_tab(self, tab: DocumentTab):
        if tab in self.tabs:
            self.tabs.remove(tab)
        else:
            raise AssertionError('Tab not attached')
