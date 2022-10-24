# -*- coding: utf-8 -*-
import os

import extensions
from blackfennec.document_system.document_factory import DocumentFactory
from blackfennec.structure.list import List
from blackfennec.extension.extension_api import ExtensionApi
from blackfennec.extension.extension_source import ExtensionSource
from blackfennec.extension.extension_source_registry import ExtensionSourceRegistry
from blackfennec.extension.local_extension_service import LocalExtensionService
from blackfennec.extension.pypi_extension_service import PyPIExtensionService


class ExtensionInitialisationService:
    def __init__(
            self,
            document_factory: DocumentFactory,
    ):
        """
        encoding_service (StructureSerializer): to convert
                structure to raw json
        """
        self._document_factory = document_factory

    def _default_initialise_extensions(self, uri: str):
        """
        Function creates default Extension sources
        and writes them to a file located at path

        Args:
            uri (str): path of file to create
        """
        extension_source = ExtensionSource(
            LocalExtensionService(),
            identification=extensions.__name__,
            location=extensions.__path__,
            source_type='local'
        )
        for extension in extension_source.extensions:
            extension.enabled = True

        source_list = List([
            extension_source.underlay
        ])

        # TODO: https://gitlab.ost.ch/blackfennec/blackfennec/-/issues/1
        config = self._document_factory.create(
            uri,
            'file',
            'application/json'
        )
        config.content = source_list
        config.save()

    def load_extensions_from_file(
            self,
            extension_source_registry: ExtensionSourceRegistry,
            extension_api: ExtensionApi,
            uri: str
    ):
        """
        Function loads extensions from configuration file.
        If it does not exists, it is created.

        Args:
            extension_source_registry (ExtensionSourceRegistry): registry
            extension_api (ExtensionApi): passed to loaded extensions
            uri (str): uri of file where extension config is located
        """
        extension_services = {
            'local': LocalExtensionService(),
            'pypi': PyPIExtensionService()
        }
        absolute_path = os.path.abspath(uri)
        if not os.path.exists(absolute_path):
            self._default_initialise_extensions(absolute_path)

        # TODO: https://gitlab.ost.ch/blackfennec/blackfennec/-/issues/1
        config = self._document_factory.create(
            uri,
            'file',
            'application/json'
        )

        for extension_source_structure in config.content.value:
            source_type = extension_source_structure.value['type'].value
            extension_source = ExtensionSource(
                extension_services[source_type],
                extension_source_structure
            )
            extension_source.load_extensions(extension_api)
            extension_source_registry.register_extension_source(
                extension_source
            )