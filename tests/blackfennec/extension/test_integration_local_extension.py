# -*- coding: utf-8 -*-
import unittest
import pytest
import blackfennec_doubles.extension.double_extensions
import blackfennec_doubles.extension.double_extensions.valid_extension
from blackfennec.extension.extension_api import ExtensionApi
from blackfennec.extension.extension_source import ExtensionSource
from blackfennec.extension.extension_status import ExtensionStatus
from blackfennec.extension.local_extension_service import LocalExtensionService
from blackfennec.interpretation.auction.auctioneer import Auctioneer
from blackfennec.interpretation.interpretation_service import InterpretationService
from blackfennec.extension.presenter_registry import PresenterRegistry
from blackfennec.structure.list import List
from blackfennec.structure.map import Map
from blackfennec.structure.string import String
from blackfennec.type_system.type_registry import TypeRegistry

pytestmark = pytest.mark.integration

class ExtensionSourceTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.source_identification = blackfennec_doubles.extension.double_extensions.__name__
        self.source_location = blackfennec_doubles.extension.double_extensions.__path__
        self.extension_source_map = Map({
            ExtensionSource.SOURCE_IDENTIFICATION: String(self.source_identification),
            ExtensionSource.SOURCE_LOCATION: List([
                String(self.source_location[0])
            ]),
        })
        self.extension_loading_service = LocalExtensionService()
        self.extension_source = ExtensionSource(
            self.extension_loading_service,
            self.extension_source_map
        )
        self.extension_source.refresh_extensions()

        type_registry = TypeRegistry()
        view_factory = None
        view_factory_registry = None
        type_loader = None
        action_registry = None
        self.extension_api = ExtensionApi(
            PresenterRegistry(),
            type_registry,
            InterpretationService(type_registry),
            view_factory,
            view_factory_registry,
            type_loader,
            action_registry
        )

    def test_can_load_extension(self):
        for extension in self.extension_source.extensions:
            if extension.name == blackfennec_doubles.extension.double_extensions.valid_extension.__name__:
                extension.enabled = True
        self.extension_source.load_extensions(self.extension_api)
        for extension in self.extension_source.extensions:
            if extension.name == blackfennec_doubles.extension.double_extensions.valid_extension.__name__:
                self.assertEqual(extension.status[0], ExtensionStatus.LOADED)
            else:
                self.assertEqual(extension.status[0], ExtensionStatus.NOT_LOADED)

    def test_can_unload_loaded_extension(self):
        self.test_can_load_extension()
        self.extension_source.unload_extensions(self.extension_api)
        for extension in self.extension_source.extensions:
            self.assertEqual(extension.status[0], ExtensionStatus.NOT_LOADED)
