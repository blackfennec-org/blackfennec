# -*- coding: utf-8 -*-
import unittest
import doubles.extension.double_extensions
import doubles.extension.double_extensions.valid_extension
from src.extension.extension_api import ExtensionApi
from src.extension.extension_source import ExtensionSource
from src.extension.extension_status import ExtensionStatus
from src.extension.local_extension_service import LocalExtensionService
from src.interpretation.auction.auctioneer import Auctioneer
from src.interpretation.interpretation_service import InterpretationService
from src.navigation.navigation_service import NavigationService
from src.presentation.presenter_registry import PresenterRegistry
from src.structure.list import List
from src.structure.map import Map
from src.structure.string import String
from src.type_system.type_registry import TypeRegistry


class ExtensionSourceTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.source_identification = doubles.extension.double_extensions.__name__
        self.source_location = doubles.extension.double_extensions.__path__
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
        self.extension_api = ExtensionApi(
            PresenterRegistry(),
            type_registry,
            NavigationService(),
            InterpretationService(Auctioneer(type_registry))
        )

    def tearDown(self) -> None:
        self.source_identification = None
        self.source_location = None
        self.extension_source_map = None
        self.extension_loading_service = None

    def test_can_load_extension(self):
        for extension in self.extension_source.extensions:
            if extension.name == doubles.extension.double_extensions.valid_extension.__name__:
                extension.enabled = True
        self.extension_source.load_extensions(self.extension_api)
        for extension in self.extension_source.extensions:
            if extension.name == doubles.extension.double_extensions.valid_extension.__name__:
                self.assertEqual(extension.status[0], ExtensionStatus.LOADED)
            else:
                self.assertEqual(extension.status[0], ExtensionStatus.NOT_LOADED)

    def test_can_unload_loaded_extension(self):
        self.test_can_load_extension()
        self.extension_source.unload_extensions(self.extension_api)
        for extension in self.extension_source.extensions:
            self.assertEqual(extension.status[0], ExtensionStatus.NOT_LOADED)
