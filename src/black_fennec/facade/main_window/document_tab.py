import os
import logging

from src.black_fennec.document_system.document_factory import DocumentFactory
from src.black_fennec.navigation.navigation_service import NavigationService
from src.black_fennec.type_system.presenter_registry import PresenterRegistry

logger = logging.getLogger(__name__)


class DocumentTab():
    def __init__(
            self,
            presenter_registry: PresenterRegistry,
            document_factory: DocumentFactory,
            navigation_service: NavigationService,
            uri: str):
        self._presenter_registry = presenter_registry
        self._document_factory = document_factory
        self._navigation_service = navigation_service
        self.uri = uri

        self.presenter = None
        self.presenter_view = None
        self.document = None

    def create_presenter(self):
        presenter_factory = self._presenter_registry.presenters[0]
        self.presenter_view = presenter_factory.create(self._navigation_service)
        self.presenter = self.presenter_view.view_model
        self._navigation_service.set_presenter(self.presenter)
        return self.presenter_view

    def load_document(self):
        assert self.presenter, 'document loaded before presenter was set'
        self.document = self._document_factory.create(
            self.uri,
            location=os.path.dirname(self.uri)
        )
        self.presenter.set_structure(self.document.content)
