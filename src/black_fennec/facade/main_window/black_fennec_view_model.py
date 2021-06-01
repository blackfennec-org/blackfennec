import logging

from uri import URI

from src.black_fennec.facade.extension_store.extension_store_view_model import ExtensionStoreViewModel
from src.black_fennec.navigation.navigation_service import NavigationService
from src.black_fennec.util.observable import Observable
from src.black_fennec.structure.structure import Structure
from src.black_fennec.util.uri.structure_encoding_service import StructureEncodingService
from src.black_fennec.facade.main_window.tab import Tab
from src.extension.extension_api import ExtensionApi
from src.extension.extension_source_registry import ExtensionSourceRegistry

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
            presenter_factory,
            interpretation_service,
            uri_import_service,
            extension_api: ExtensionApi,
            extension_source_registry: ExtensionSourceRegistry
    ):
        """BlackFennecViewModel constructor.

        Args:
            presenter_factory (StructurePresenterFactory): presenter
            interpretation_service (InterpretationService): interpretation service
        """
        logger.info('BlackFennecViewModel __init__')
        super().__init__()
        self._presenter_factory = presenter_factory
        self._interpretation_service = interpretation_service
        self._uri_import_service = uri_import_service
        self._extension_api = extension_api
        self._extension_source_registry = extension_source_registry
        self.tabs = set()

    def new(self):
        """Future implementation of new()"""
        logger.warning('new() not yet implemented')

    def open(self, uri: URI):
        """Opens a file
        specified by the filename

        Args:
            uri (URI): URI of the file to open
        """
        structure: Structure = self._uri_import_service.load(uri)
        navigation_service = NavigationService()
        presenter_view = self._presenter_factory.create(navigation_service)
        presenter = presenter_view._view_model
        navigation_service.set_presenter(presenter)
        tab = Tab(presenter_view, uri, structure)
        self.tabs.add(tab)
        presenter.set_structure(structure)
        self._notify(self.tabs, 'tabs')

    def close_tab(self, filename):
        for tab in self.tabs:
            if tab.uri == filename:
                element = tab
                self.tabs.remove(element)
                break

        self._notify(self.tabs, 'tabs')

    def quit(self):
        """Future implementation of quit()"""
        logger.warning('quit() not yet implemented')

    def save(self):
        """Future implementation of save()"""
        encoding_service = StructureEncodingService(indent=2)

        for tab in self.tabs:
            raw = encoding_service.encode(tab.structure)
            with open(tab.uri.path, 'w') as file:
                file.write(raw)

    def save_as(self):
        """Future implementation of save_as()"""
        logger.warning('save_as() not yet implemented')

    def create_extension_store(self) -> ExtensionStoreViewModel:
        return ExtensionStoreViewModel(
            self._extension_source_registry,
            self._extension_api
        )

    def about_and_help(self):
        """Future implementation of about_and_help()"""
        logger.warning('about_and_help() not yet implemented')
