# -*- coding: utf-8 -*-

from .view_factory_registry import ViewFactoryRegistry

class ViewFactory:
    def __init__(self, view_factory_registry: ViewFactoryRegistry):
        self._view_factory_registry = view_factory_registry

    def create(self, interpretation):
        for type in interpretation.types:
            factory = self._view_factory_registry.get_factory(type, interpretation.specification)
            if factory:
                return factory.create(interpretation)
