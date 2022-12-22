# -*- coding: utf-8 -*-
from typing import Iterator

from .type_view import TypeView
from .type_view_factory import TypeViewFactory
from .type_view_factory_registry import TypeViewFactoryRegistry
from blackfennec.type_system.interpretation.interpretation import Interpretation


class StructureViewFactory:
    def __init__(self, type_view_factory_registry: TypeViewFactoryRegistry):
        self._type_view_factory_registry = type_view_factory_registry

    def create(self, interpretation: Interpretation) -> Iterator[TypeView]:
        for type in interpretation.types:
            type_factory: TypeViewFactory = self._type_view_factory_registry\
                .get_factory(
                    type,
                    interpretation.specification
                )
            if type_factory:
                yield type_factory.create(interpretation)
