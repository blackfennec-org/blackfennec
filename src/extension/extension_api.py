# -*- coding: utf-8 -*-
from src.black_fennec.interpretation.interpretation_service import InterpretationService
from src.black_fennec.type_system.presenter_registry import PresenterRegistry
from src.black_fennec.type_system.template_registry import TemplateRegistry
from src.black_fennec.type_system.type_registry import TypeRegistry


class ExtensionApi:
    """
    Enables extensions to load types, actions or presenters
    with services and registries contained within the this class.
    """

    def __init__(
            self,
            presenter_registry: PresenterRegistry,
            type_registry: TypeRegistry,
            template_registry: TemplateRegistry,
            interpretation_service: InterpretationService
    ):
        self._presenter_registry = presenter_registry
        self._type_registry = type_registry
        self._template_registry = template_registry
        self._interpretation_service = interpretation_service

    @property
    def presenter_registry(self) -> PresenterRegistry:
        return self._presenter_registry

    @property
    def type_registry(self) -> TypeRegistry:
        return self._type_registry

    @property
    def template_registry(self) -> TemplateRegistry:
        return self._template_registry

    @property
    def interpretation_service(self):
        return self._interpretation_service
