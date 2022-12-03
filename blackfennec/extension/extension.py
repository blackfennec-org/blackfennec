# -*- coding: utf-8 -*-
from typing import Optional

import logging

from blackfennec.extension.extension_api import ExtensionApi


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Extension:
    """
    Class representing Extension

    Wrapper for underlay, able to load and unload
    the extension saved in an underlay
    """
    NAME_KEY = 'identification'
    LOCATION_KEY = 'location'
    ENABLED_KEY = 'enabled'

    def __init__(
            self,
            name: str,
            api: ExtensionApi,
            dependencies: Optional[set[str]] = None,
    ):
        assert name is not None
        self._name = name
        self._api = api
        self._is_active = False
        self._dependencies = dependencies or set()

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_active(self) -> bool:
        return self._is_active

    @property
    def dependencies(self) -> set[str]:
        return self._dependencies

    def activate(self) -> None:
        assert not self.is_active
        logger.debug(f"activating extension {self.name}")
        self.register_types()
        self.register_actions()
        self.register_view_factories()
        self.register_presenters()
        self._is_active = True

    def deactivate(self) -> None:
        assert self.is_active
        logger.debug(f"deactivating extension {self.name}")
        self.deregister_presenters()
        self.deregister_view_factories()
        self.deregister_actions()
        self.deregister_types()
        self._is_active = False

    def register_types(self):
        ...

    def deregister_types(self):
        ...

    def register_actions(self):
        ...

    def deregister_actions(self):
        ...

    def register_view_factories(self):
        ...

    def deregister_view_factories(self):
        ...

    def register_presenters(self):
        ...

    def deregister_presenters(self):
        ...
