# -*- coding: utf-8 -*-
import logging

from src.extension.extension import Extension
from src.extension.extension_status import ExtensionStatus
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String

logger = logging.getLogger(__name__)


class ExtensionSource:
    """
    Source of multiple extensions

    Identifies one location in which extensions can be found.
    """
    SOURCE_LOCATION = 'location_path'
    SOURCE_IDENTIFICATION = 'location_id'
    SOURCE_TYPE = 'type'
    EXTENSION_LIST_KEY = 'extensions'

    def __init__(
            self,
            extension_loading_service,
            source_map: Map = None,
            identification=None,
            location=None,
            source_type=None
    ):
        self._extension_loading_service = extension_loading_service
        self._extensions = dict()
        self._data = source_map if source_map else Map()

        if self.SOURCE_IDENTIFICATION not in self._data:
            self._data[self.SOURCE_IDENTIFICATION] = String()
        if self.SOURCE_LOCATION not in self._data:
            self._data[self.SOURCE_LOCATION] = List()
        if self.SOURCE_TYPE not in self._data:
            self._data[self.SOURCE_TYPE] = String()

        self.identification = identification if identification \
            else self.identification
        self.location = location if location else self.location
        self.type = source_type if source_type else self.type

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
    def type(self):
        return self._data[self.SOURCE_TYPE].value

    @type.setter
    def type(self, value):
        self._data[self.SOURCE_TYPE].value = value

    @property
    def location(self):
        return [
            uri.value
            for uri in self._data[self.SOURCE_LOCATION].value
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
    def extensions(self) -> [Extension]:
        """
        Reloads extensions from underlay, but keeps
            status of already loaded extensions.

        Returns:
             [Extension]: list of extensions in source
        """
        source_extension_list = self._data[self.EXTENSION_LIST_KEY].value
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
                message = f'Extension({extension}) disabled or already loaded'
                logger.warning(message)

    def unload_extensions(self, extension_api):
        for extension in self.extensions:
            if extension.status[0] == ExtensionStatus.LOADED:
                extension.unload(extension_api)
            else:
                message = f'Extension({extension}) not loaded'
                logger.warning(message)
