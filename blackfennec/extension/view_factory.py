# -*- coding: utf-8 -*-
from typing import Iterator

from .view_factory_registry import ViewFactoryRegistry


class ViewFactory:
    def __init__(self, view_factory_registry: ViewFactoryRegistry):
        self._view_factory_registry = view_factory_registry

    def create(self, interpretation) -> Iterator['Gtk.Widget']:
        for type in interpretation.types:
            factory = self._view_factory_registry.get_factory(
                type,
                interpretation.specification
            )
            if factory:
                yield factory.create(interpretation)
