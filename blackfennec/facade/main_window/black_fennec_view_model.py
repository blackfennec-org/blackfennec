import logging
from typing import Optional

from blackfennec.document_system.document_factory import DocumentFactory
from blackfennec.facade.about_window.about_window_view_model import AboutWindowViewModel
from blackfennec.facade.extension_store.extension_store_view_model import ExtensionStoreViewModel

from blackfennec.facade.main_window.document_tab import DocumentTab
from blackfennec.interpretation.interpretation_service import InterpretationService
from blackfennec.navigation.navigation_service import NavigationService
from blackfennec.extension.presenter_registry import PresenterRegistry
from blackfennec.util.observable import Observable
from blackfennec.extension.extension_api import ExtensionApi
from blackfennec.extension.extension_source_registry import ExtensionSourceRegistry

logger = logging.getLogger(__name__)


class BlackFennecViewModel(Observable):
    """BlackFennec MainWindow view_model.

    view_model to which views can dispatch calls
    that include business logic.

    Attributes:
        _presenter (StructurePresenter): stores injected presenter
        _navigation_service (NavigationService): stores injected
            navigation service
    """

    def __init__(
            self,
            presenter_registry: PresenterRegistry,
            interpretation_service: InterpretationService,
            document_factory: DocumentFactory,
            extension_api: ExtensionApi,
            extension_source_registry: ExtensionSourceRegistry,
    ):
        """BlackFennecViewModel constructor.

        Args:
            presenter_registry (PresenterRegistry): presenter registry
            interpretation_service (InterpretationService): interpretation
                service
            document_factory (DocumentFactory): document factory
            extension_api (ExtensionApi): Extension API
            extension_source_registry (ExtensionSourceRegistry): extension-source registry
        """
        logger.info('BlackFennecViewModel __init__')
        super().__init__()
        self._presenter_registry = presenter_registry
        self._interpretation_service = interpretation_service
        self._document_factory = document_factory
        self._extension_api = extension_api
        self._extension_source_registry = extension_source_registry
        self.tabs = set()
        self._current_directory: Optional[str] = None

    @property
    def current_directory(self):
        return self._current_directory

    @current_directory.setter
    def current_directory(self, directory: str):
        self._current_directory = directory
        self._notify('open_directory', self._current_directory)

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

    def create_extension_store(self) -> ExtensionStoreViewModel:
        """Creates an extension store view model"""
        return ExtensionStoreViewModel(
            self._extension_source_registry,
            self._extension_api
        )

    def get_about_window_view_model(self):
        return AboutWindowViewModel()

    def copy(self) -> 'BlackFennecViewModel':
        return BlackFennecViewModel(
            self._presenter_registry,
            self._interpretation_service,
            self._document_factory,
            self._extension_api,
            self._extension_source_registry
        )

    def attach_tab(self, tab: DocumentTab):
        if tab not in self.tabs:
            self.tabs.add(tab)

    def detach_tab(self, tab: DocumentTab):
        if tab in self.tabs:
            self.tabs.remove(tab)
