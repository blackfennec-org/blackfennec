# -*- coding: utf-8 -*-
from src.interpretation.interpretation_service import InterpretationService
from src.navigation.navigation_service import NavigationService
from src.presentation.presenter_registry import PresenterRegistry
from src.type_system.type_registry import TypeRegistry


class ExtensionApi:
    """
    Enables extensions to load types, actions or presenters
    with services and registries contained within the this class.
    """
    def __init__(
            self,
            presenter_registry: PresenterRegistry,
            type_registry: TypeRegistry,
            navigation_service: NavigationService,
            interpretation_service: InterpretationService
    ):
        self._presenter_registry = presenter_registry
        self._type_registry = type_registry
        self._navigation_service = navigation_service
        self._interpretation_service = interpretation_service

    @property
    def type_registry(self) -> TypeRegistry:
        return self._type_registry

    @property
    def presenter_registry(self) -> PresenterRegistry:
        return self._presenter_registry

    @property
    def navigation_service(self) -> NavigationService:
        return self._navigation_service

    @property
    def interpretation_service(self):
        return self._interpretation_service
