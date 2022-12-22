# -*- coding: utf-8 -*-
from enum import Enum
from typing import Optional

import logging

from blackfennec.extension_system.extension_api import ExtensionApi


logger = logging.getLogger(__name__)


class Extension:
    class State(Enum):
        INACTIVE = 'inactive'
        ACTIVE = 'active'
        FAILED = 'failed'
        DEPENDENCY_MISSING = 'dependency_missing'

    def __init__(
            self,
            name: str,
            api: ExtensionApi,
            dependencies: Optional[set[str]] = None,
    ):
        assert name is not None
        self._name = name
        self._api = api
        self._state = Extension.State.INACTIVE
        self._dependencies = dependencies or set()

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_active(self) -> bool:
        return self.state == Extension.State.ACTIVE

    @property
    def state(self) -> 'Extension.State':
        return self._state

    @state.setter
    def state(self, state: 'Extension.State') -> None:
        self._state = state

    @property
    def dependencies(self) -> set[str]:
        return self._dependencies

    def activate(self) -> None:
        assert not self.is_active
        logger.info(f'activating extension {self.name}')
        self.register_types()
        self.register_actions()
        self.register_view_factories()
        self.register_presenters()
        self.state = Extension.State.ACTIVE

    def deactivate(self) -> None:
        assert self.is_active
        logger.info(f'deactivating extension {self.name}')
        self.deregister_presenters()
        self.deregister_view_factories()
        self.deregister_actions()
        self.deregister_types()
        self.state = Extension.State.INACTIVE

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
