import logging
from typing import Optional

from src.black_fennec.document_system.document_factory import DocumentFactory
from src.black_fennec.facade.about_window.about_window_view_model import AboutWindowViewModel
from src.black_fennec.facade.extension_store.extension_store_view_model import ExtensionStoreViewModel

from src.black_fennec.facade.main_window.document_tab import DocumentTab
from src.black_fennec.interpretation.interpretation_service import InterpretationService
from src.black_fennec.navigation.navigation_service import NavigationService
from src.black_fennec.type_system.presenter_registry import PresenterRegistry
from src.black_fennec.util.observable import Observable
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
        self.project: Optional[str] = None

    def set_project(self, project_location: str):
        """Sets the project location

        Args:
            project_location (str): project location
        """
        self.project = project_location
        self._notify(self.project, 'project')

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
        self._notify(tab, 'open_file')

    def close_file(self, tab: DocumentTab):
        """Closes a file

        Args:
            tab (DocumentTab): tab to close
        """
        self.tabs.remove(tab)
        self._notify(tab, 'close_file')

    def save(self):
        """Saves all open files"""
        for tab in self.tabs:
            root = tab.structure.get_root()
            document = root.get_document()
            document.save()

    def save_as(self):
        """Future implementation of save_as()"""
        logger.warning('save_as() not yet implemented')

    def create_extension_store(self) -> ExtensionStoreViewModel:
        """Creates an extension store view model"""
        return ExtensionStoreViewModel(
            self._extension_source_registry,
            self._extension_api
        )

    def get_about_window_view_model(self):
        return AboutWindowViewModel()
