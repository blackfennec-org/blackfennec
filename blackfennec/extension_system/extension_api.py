# -*- coding: utf-8 -*-
from blackfennec.action_system.action_registry import ActionRegistry
from blackfennec.document_system.document_factory import DocumentFactory
from blackfennec.document_system.document_registry import DocumentRegistry
from blackfennec.document_system.mime_type.mime_type_registry import \
    MimeTypeRegistry
from blackfennec.document_system.resource_type.resource_type_registry import \
    ResourceTypeRegistry
from blackfennec.presentation_system.presenter_registry import PresenterRegistry
from blackfennec.presentation_system.ui_service.ui_service import UiService
from blackfennec.type_system.interpretation.interpretation_service import \
    InterpretationService
from blackfennec.type_system.type_registry import TypeRegistry


class ExtensionApi:
    """
    Enables extensions to load types, actions or presenters
    with services and registries contained within the this class.
    """

    def __init__(
            self,
            presenter_registry: PresenterRegistry,
            type_registry: TypeRegistry,
            interpretation_service: InterpretationService,
            view_factory,
            view_factory_registry,
            type_loader,
            action_registry: ActionRegistry,
            document_registry: DocumentRegistry,
            document_factory: DocumentFactory,
            ui_service: UiService,
            mime_type_registry: MimeTypeRegistry,
            resource_type_registry: ResourceTypeRegistry,
    ):
        self._presenter_registry = presenter_registry
        self._type_registry = type_registry
        self._interpretation_service = interpretation_service
        self._view_factory = view_factory
        self._view_factory_registry = view_factory_registry
        self._type_loader = type_loader
        self._action_registry = action_registry
        self._document_registry = document_registry
        self._document_factory = document_factory
        self._ui_service = ui_service
        self._mime_type_registry = mime_type_registry
        self._resource_type_registry = resource_type_registry

    @property
    def presenter_registry(self) -> PresenterRegistry:
        return self._presenter_registry

    @property
    def type_registry(self) -> TypeRegistry:
        return self._type_registry

    @property
    def interpretation_service(self):
        return self._interpretation_service

    @property
    def view_factory(self):
        return self._view_factory

    @property
    def view_factory_registry(self):
        return self._view_factory_registry

    @property
    def type_loader(self):
        return self._type_loader

    @property
    def action_registry(self) -> ActionRegistry:
        return self._action_registry

    @property
    def document_registry(self) -> DocumentRegistry:
        return self._document_registry

    @property
    def document_factory(self) -> DocumentFactory:
        return self._document_factory

    @property
    def ui_service(self) -> UiService:
        return self._ui_service

    @property
    def mime_type_registry(self) -> MimeTypeRegistry:
        return self._mime_type_registry

    @property
    def resource_type_registry(self) -> ResourceTypeRegistry:
        return self._resource_type_registry
