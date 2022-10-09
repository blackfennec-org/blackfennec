# -*- coding: utf-8 -*-
import os

import src.visualisation
import src.presentation

from src.black_fennec.structure.list import List
from src.black_fennec.document_system.document_factory import DocumentFactory
from src.extension.extension_api import ExtensionApi
from src.extension.extension_source import ExtensionSource
from src.extension.extension_source_registry import ExtensionSourceRegistry
from src.extension.local_extension_service import LocalExtensionService
from src.extension.pypi_extension_service import PyPIExtensionService
from src.black_fennec.structure.structure_serializer import StructureSerializer


class ExtensionInitialisationService:
    def __init__(
            self,
            encoding_service: StructureSerializer
    ):
        """
        encoding_service (StructureSerializer): to convert
                structure to raw json
        """
        self._encoding_service = encoding_service

    def _default_initialise_extensions(self, path):
        """
        Function creates default Extension sources
        and writes them to a file located at path

        Args:
            path (str): path of file to create
        """
        visualisation = src.visualisation
        type_system_source = ExtensionSource(
            LocalExtensionService(),
            identification=visualisation.__name__,
            location=visualisation.__path__,
            source_type='local'
        )
        for extension in type_system_source.extensions:
            extension.enabled = True

        presentation = src.presentation
        presentation_source = ExtensionSource(
            LocalExtensionService(),
            identification=presentation.__name__,
            location=presentation.__path__,
            source_type='local'
        )
        for extension in presentation_source.extensions:
            extension.enabled = True

        source_list = List([
            type_system_source.underlay,
            presentation_source.underlay
        ])

        raw = self._encoding_service.serialize(source_list)
        with open(path, 'w') as file:
            file.write(raw)

    def load_extensions_from_file(
            self,
            extension_source_registry: ExtensionSourceRegistry,
            document_factory: DocumentFactory,
            extension_api: ExtensionApi,
            uri: str
    ):
        """
        Function loads extensions from configuration file.
        If it does not exists, it is created.

        Args:
            extension_source_registry (ExtensionSourceRegistry):
            document_factory (DocumentFactory): used to import the config file
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
        config = document_factory.create(
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
