import logging
import os
from typing import Optional

from blackfennec.document_system.document_factory import DocumentFactory
from blackfennec.facade.about_window.about_window_view_model import AboutWindowViewModel
from blackfennec.facade.main_window.document_tab import DocumentTab
from blackfennec.facade.ui_service.message import Message
from blackfennec.facade.ui_service.ui_service import UiService
from blackfennec.interpretation.interpretation_service import InterpretationService
from blackfennec.navigation.navigation_service import NavigationService
from blackfennec.extension.presenter_registry import PresenterRegistry
from blackfennec.util.observable import Observable
from blackfennec.extension.extension_api import ExtensionApi

logger = logging.getLogger(__name__)


class BlackFennecViewModel(Observable):

    def __init__(
            self,
            extension_api: ExtensionApi,
    ):
        logger.info('BlackFennecViewModel __init__')
        super().__init__()
        self._presenter_registry = extension_api.presenter_registry
        self._interpretation_service = extension_api.interpretation_service
        self._document_factory = extension_api.document_factory
        self._extension_api = extension_api
        self._ui_service_registry = extension_api.ui_service_registry
        self._ui_service = None

        self.tabs = set()
        self._current_directory: Optional[str] = None

    @property
    def current_directory(self):
        return self._current_directory

    @current_directory.setter
    def current_directory(self, directory: str):
        self._current_directory = directory
        self._notify('open_directory', self._current_directory)
        self._ui_service.show_message(
            Message('Opened directory: ' + os.path.basename(directory))
        )

    def get_ui_service(self, key) -> UiService:
        return self._ui_service_registry.services[key]

    def set_ui_service(self, key, ui_service):
        if self._ui_service is not None:
            raise AssertionError('UI service already set')
        self._ui_service = ui_service
        self._ui_service_registry.register(key, ui_service)

    def open(self, uri: str):
        if os.path.isdir(uri):
            self.current_directory = uri
        else:
            self.open_file(uri)

    def open_file(self, uri: str):
        '''Opens a file
        specified by the filename

        Args:
            uri (str): URI of the file to open
        '''
        navigation_service = NavigationService()
        tab = DocumentTab(
            self._presenter_registry,
            self._document_factory,
            navigation_service,
            uri
        )
        self.tabs.add(tab)
        self._notify('open_file', tab)
        self._ui_service.show_message(
            Message('Opened file: { + os.path.basename(uri)}'))

    def close_file(self, tab: DocumentTab):
        '''Closes a file

        Args:
            tab (DocumentTab): tab to close
        '''
        self.tabs.remove(tab)
        self._notify('close_file', tab)
        self._ui_service.show_message(
            Message('Closed document'))

    def save(self, tab: DocumentTab):
        '''Saves the passed file'''
        tab.save_document()
        self._ui_service.show_message(
            Message('Saved document')
        )

    def save_as(self, tab: DocumentTab, uri: str):
        '''Saves the passed tab under new path'''
        tab.save_document_as(uri)
        self._ui_service.show_message(
            Message(f'Saved document under: {os.path.basename(uri)}'))

    def save_all(self):
        '''Saves all open files'''
        for tab in self.tabs:
            self.save(tab)
        self._ui_service.show_message(Message('Saved all opened files'))

    def get_about_window_view_model(self):
        return AboutWindowViewModel()

    def undo(self, tab: DocumentTab):
        if tab.history.can_undo():
            tab.history.undo()
            self._ui_service.show_message(
                Message(
                    'Undone last change',
                    action_name='Redo',
                    action_target='main.redo',
                )
            )
        else:
            self._ui_service.show_message(Message('Cannot undo'))

    def redo(self, tab: DocumentTab):
        if tab.history.can_redo():
            tab.history.redo()
            self._ui_service.show_message(
                Message(
                    'Redone last change',
                    action_name='Undo',
                    action_target='main.undo',
                )
            )
        else:
            self._ui_service.show_message(Message('Cannot redo'))

    def copy(self) -> 'BlackFennecViewModel':
        return BlackFennecViewModel(self._extension_api)

    def attach_tab(self, tab: DocumentTab):
        if tab not in self.tabs:
            self.tabs.add(tab)
            self._ui_service.show_message(Message('Tab attached'))
        else:
            raise AssertionError('Tab already attached')

    def detach_tab(self, tab: DocumentTab):
        if tab in self.tabs:
            self.tabs.remove(tab)
            self._ui_service.show_message(Message('Tab detached'))
        else:
            raise AssertionError('Tab not attached')

    def _dispatch_message(self, sender, ui_message):
        self._notify('message', ui_message, sender)
