import os
import logging

from blackfennec.document_system.document_factory import DocumentFactory
from blackfennec.navigation.navigation_service import NavigationService
from blackfennec.structure.visitors.deep_copy import DeepCopy
from blackfennec.extension.presenter_registry import PresenterRegistry
from blackfennec.util.observable import Observable

logger = logging.getLogger(__name__)


class DocumentTab(Observable):
    def __init__(
            self,
            presenter_registry: PresenterRegistry,
            document_factory: DocumentFactory,
            navigation_service: NavigationService,
            uri: str,
            icon: str = 'emblem-documents-symbolic',
    ):
        super().__init__()
        self._presenter_registry = presenter_registry
        self._document_factory = document_factory
        self._navigation_service = navigation_service
        self.uri = uri
        self.icon = icon
        self.presenter = None
        self.presenter_view = None
        self.document = None

    @property
    def uri(self):
        return self._uri

    @uri.setter
    def uri(self, uri: str):
        self._uri = uri
        self.title = os.path.basename(uri)
        self._notify(self.title, 'title')
        self._notify(self.uri, 'uri')

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, icon: str):
        self._icon = icon
        self._notify(self.icon, 'icon')

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
        return self.document.content

    def save_document(self):
        self.document.save()

    def save_document_as(self, uri: str):
        old_document = self.document
        new_document = self._document_factory.create(
            uri,
            old_document.resource_type.protocols[0],
            old_document.mime_type.mime_type_id
        )
        new_document.content = DeepCopy.copy(old_document.content.structure)
        self.document = new_document
        self.save_document()
        self.uri = uri
