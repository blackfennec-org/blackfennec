# -*- coding: utf-8 -*-
from typing import Optional

from src.extension.extension_status import ExtensionStatus
from src.structure.boolean import Boolean
from src.structure.map import Map
from src.structure.string import String


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
            extension_loading_service,
            source,
            extension_map: Optional[Map] = None,
            name: Optional[str] = None,
            location: Optional[list] = None,
            enabled: Optional[bool] = None
    ):
        self._extension_loading_service = extension_loading_service
        self._source = source
        self._status = (ExtensionStatus.NOT_LOADED, None)
        self._module = None

        self._data = extension_map if extension_map is not None else Map()
        if self.NAME_KEY not in self._data:
            self._data[self.NAME_KEY] = String()
        if self.LOCATION_KEY not in self._data:
            self._data[self.LOCATION_KEY] = String()
        if self.ENABLED_KEY not in self._data:
            self._data[self.ENABLED_KEY] = Boolean()

        self.name: str = name if name else self.name
        self.location: list = location if location else self.location
        self.enabled: bool = enabled if enabled is not None else self.enabled

    @property
    def name(self):
        return self._data[self.NAME_KEY].value

    @name.setter
    def name(self, value: str):
        self._data[self.NAME_KEY].value = value

    @property
    def location(self):
        return self._data[self.LOCATION_KEY].value

    @location.setter
    def location(self, value: str):
        self._data[self.LOCATION_KEY].value = value

    @property
    def enabled(self):
        return self._data[self.ENABLED_KEY].value

    @enabled.setter
    def enabled(self, value: bool):
        self._data[self.ENABLED_KEY].value = value

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def underlay(self):
        return self._data

    def load(self, extension_api):
        module = self._extension_loading_service.load(self)
        try:
            module.create_extension(extension_api)
            self.status = (ExtensionStatus.LOADED, module)
        except Exception as exception:
            self.status = (ExtensionStatus.CREATE_FAILED, exception)
            raise exception

    def unload(self, extension_api):
        try:
            self.status[1].destroy_extension(extension_api)
            self.status = (ExtensionStatus.NOT_LOADED, None)
        except Exception as exception:
            self.status = (ExtensionStatus.UNLOAD_FAILED, exception)
            raise exception
