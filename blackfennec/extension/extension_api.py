# -*- coding: utf-8 -*-
from blackfennec.interpretation.interpretation_service import InterpretationService
from blackfennec.extension.presenter_registry import PresenterRegistry
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
    ):
        self._presenter_registry = presenter_registry
        self._type_registry = type_registry
        self._interpretation_service = interpretation_service
        self._view_factory = view_factory
        self._view_factory_registry = view_factory_registry
        self._type_loader = type_loader

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
