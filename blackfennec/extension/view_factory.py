# -*- coding: utf-8 -*-

class ViewFactory:
    def __init__(self, view_factory_registry):
        self._view_factory_registry = view_factory_registry

    def create(self, interpretation):
        type = interpretation.types[0]
        factory = self._view_factory_registry.get_factory(type, interpretation.specification)
        return factory.create(interpretation)
