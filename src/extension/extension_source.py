# -*- coding: utf-8 -*-
import logging

from src.extension.extension import Extension
from src.extension.extension_status import ExtensionStatus
from src.structure.list import List
from src.structure.map import Map
from src.structure.string import String

logger = logging.getLogger(__name__)


class ExtensionSource:
    SOURCE_LOCATION = 'location_path'
    SOURCE_IDENTIFICATION = 'location_id'
    EXTENSION_LIST_KEY = 'extensions'

    def __init__(
            self,
            extension_loading_service,
            source_map: Map = None,
            identification=None,
            location=None
    ):
        self._extension_loading_service = extension_loading_service
        self._extensions = dict()
        self._data = source_map if source_map else Map()

        if self.SOURCE_IDENTIFICATION not in self._data:
            self._data[self.SOURCE_IDENTIFICATION] = String()
        if self.SOURCE_LOCATION not in self._data:
            self._data[self.SOURCE_LOCATION] = List()

        self.identification = identification if identification \
            else self.identification
        self.location = location if location else self.location

        if self.EXTENSION_LIST_KEY not in self._data:
            self._data[self.EXTENSION_LIST_KEY] = List()
            self.refresh_extensions()

    @property
    def identification(self):
        return self._data[self.SOURCE_IDENTIFICATION].value

    @identification.setter
    def identification(self, value):
        self._data[self.SOURCE_IDENTIFICATION].value = value

    @property
    def location(self):
        return [
            uri.value
            for uri in self._data[self.SOURCE_LOCATION].children
        ]

    @location.setter
    def location(self, value):
        self._data[self.SOURCE_LOCATION].value = [
            String(uri)
            for uri in value
        ]

    @property
    def underlay(self):
        return self._data

    @property
    def extensions(self):
        source_extension_list = self._data[self.EXTENSION_LIST_KEY].children
        result = dict()
        if source_extension_list:
            for extension in source_extension_list:
                extension_name = extension[Extension.NAME_KEY].value
                result[extension_name] = Extension(
                    self._extension_loading_service,
                    self,
                    extension
                )
                if extension_name in self._extensions:
                    result[extension_name].status = \
                        self._extensions[extension_name].status
            self._extensions = result
        return list(result.values())

    @extensions.setter
    def extensions(self, value: [Extension]):
        self._data[self.EXTENSION_LIST_KEY].value = [
            extension.underlay
            for extension in value
        ]

    def refresh_extensions(self):
        installed_extensions = self._extension_loading_service.installed(
            self, self.identification, self.location
        )

        for key in installed_extensions:
            if key in self._extensions:
                installed_extensions[key].status = self._extensions[key].status
        self.extensions = installed_extensions.values()

    def load_extensions(self, extension_api):
        for extension in self.extensions:
            if extension.status[0] != ExtensionStatus.LOADED \
                    and extension.enabled:
                extension.load(extension_api)
            else:
                message = f'Extension({extension}) already loaded'
                logger.info(message)

    def unload_extensions(self, extension_api):
        for extension in self.extensions:
            if extension.status[0] == ExtensionStatus.LOADED:
                extension.unload(extension_api)
            else:
                message = f'Extension({extension}) already not loaded'
                logger.info(message)
