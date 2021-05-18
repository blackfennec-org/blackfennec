# -*- coding: utf-8 -*-
import logging
import unittest

from doubles.double_dummy import Dummy
from doubles.extension.double_extension import ExtensionMock
from doubles.extension.double_extension_loading_service import ExtensionLoadingServiceMock
from doubles.structure.double_boolean import BooleanMock
from doubles.structure.double_list import ListMock
from doubles.structure.double_map import MapMock
from doubles.structure.double_string import StringMock
from src.extension.extension import Extension
from src.extension.extension_source import ExtensionSource
from src.extension.extension_status import ExtensionStatus
from src.structure.map import Map


class ExtensionSourceTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.extension_name = 'name'
        self.extension_location = 'location'
        self.enabled = True
        self.extension_map = MapMock({
            Extension.NAME_KEY: StringMock(self.extension_name),
            Extension.LOCATION_KEY: StringMock(self.extension_location),
            Extension.ENABLED_KEY: BooleanMock(self.enabled)
        })

        self.source_identification = 'identification'
        self.source_location = 'location'
        self.extension_source_map = MapMock({
            ExtensionSource.SOURCE_IDENTIFICATION: StringMock(self.source_identification),
            ExtensionSource.SOURCE_LOCATION: ListMock(children=[
                StringMock(self.source_location)
            ]),
            ExtensionSource.EXTENSION_LIST_KEY: ListMock(children=[
                self.extension_map
            ])
        })
        self.extension_loading_service = ExtensionLoadingServiceMock()

    def tearDown(self) -> None:
        self.extension_name = None
        self.extension_location = None
        self.enabled = None
        self.source_identification = None
        self.source_location = None
        self.extension_map = None
        self.extension_source_map = None
        self.extension_loading_service = None

    def test_can_construct(self):
        ExtensionSource(
            self.extension_loading_service
        )

    def test_can_construct_with_map(self):
        ExtensionSource(
            self.extension_loading_service,
            self.extension_source_map
        )

    def test_can_get_identifier(self):
        extension_source = ExtensionSource(
            self.extension_loading_service,
            identification=self.source_identification
        )
        self.assertEqual(extension_source.identification, self.source_identification)

    def test_can_set_identifier(self):
        extension_source = ExtensionSource(
            self.extension_loading_service,
            self.extension_source_map
        )
        new_identification = 'new identification'
        extension_source.identification = 'new identification'
        self.assertEqual(self.extension_source_map[ExtensionSource.SOURCE_IDENTIFICATION].value, new_identification)

    def test_can_get_type(self):
        extension_source = ExtensionSource(
            self.extension_loading_service,
            identification=self.source_identification
        )
        self.assertEqual(extension_source.identification, self.source_identification)

    def test_can_set_type(self):
        extension_source = ExtensionSource(
            self.extension_loading_service,
            self.extension_source_map
        )
        new_identification = 'new source_type'
        extension_source.identification = 'new source_type'
        self.assertEqual(self.extension_source_map[ExtensionSource.SOURCE_IDENTIFICATION].value, new_identification)

    def test_can_get_location(self):
        extension_source = ExtensionSource(
            self.extension_loading_service,
            location=[self.source_location]
        )
        self.assertIn(self.source_location, extension_source.location)

    def test_can_set_location(self):
        extension_source = ExtensionSource(
            self.extension_loading_service,
            self.extension_source_map
        )
        new_location = ['new location']
        extension_source.location = new_location
        self.assertEqual(self.extension_source_map[ExtensionSource.SOURCE_LOCATION].value, new_location)

    def test_can_get_underlay(self):
        extension_source = ExtensionSource(
            self.extension_loading_service,
            self.extension_source_map
        )
        self.assertEqual(extension_source.underlay, self.extension_source_map)

    def test_can_get_underlay_empty_construction(self):
        extension_source = ExtensionSource(
            self.extension_loading_service
        )
        self.assertIsInstance(extension_source.underlay, Map)

    def test_can_get_extensions(self):
        extension_source = ExtensionSource(
            self.extension_loading_service,
            self.extension_source_map
        )
        self.assertEqual(len(extension_source.extensions), 1)

    def test_can_set_extensions(self):
        extension_source = ExtensionSource(
            self.extension_loading_service,
        )
        extension_source.extensions = [ExtensionMock(self.extension_map)]

    def test_can_refresh_extensions(self):
        extension_source = ExtensionSource(
            self.extension_loading_service,
            self.extension_source_map
        )
        extension_source.refresh_extensions()
        self.assertEqual(self.extension_loading_service.installed_count, 1)

    def test_can_load_extensions(self):
        extension_source = ExtensionSource(
            self.extension_loading_service,
        )
        extension_api = Dummy('ExtensionApi')
        extension = ExtensionMock(self.extension_map)
        extension_source.extensions = [extension]
        extension_source.load_extensions(extension_api)
        self.assertEqual(self.extension_loading_service.load_count, 1)
        self.assertEqual(extension_source.extensions[0].status[0], ExtensionStatus.LOADED)

    def test_can_load_extensions_twice(self):
        extension_source = ExtensionSource(
            self.extension_loading_service,
        )
        extension_api = Dummy('ExtensionApi')
        extension = ExtensionMock(self.extension_map)
        extension_source.extensions = [extension]
        extension_source.load_extensions(extension_api)
        self.assertLogs(None, logging.INFO)
        self.assertEqual(self.extension_loading_service.load_count, 1)
        self.assertEqual(extension_source.extensions[0].status[0], ExtensionStatus.LOADED)

    def test_loaded_extension_keeps_status_after_refresh(self):
        extension_source = ExtensionSource(
            self.extension_loading_service,
        )
        extension_api = Dummy('ExtensionApi')
        extension = ExtensionMock(self.extension_map)
        extension_source.extensions = [extension]
        extension_source.load_extensions(extension_api)
        self.extension_loading_service.installed_extensions = {self.extension_name: extension}
        extension_source.refresh_extensions()
        self.assertEqual(extension_source.extensions[0].status[0], ExtensionStatus.LOADED)

    def test_can_unload_extensions_not_loaded(self):
        extension_source = ExtensionSource(
            self.extension_loading_service,
        )
        extension_api = Dummy('ExtensionApi')
        extension = ExtensionMock(self.extension_map)
        extension_source.extensions = [extension]
        extension_source.unload_extensions(extension_api)

        self.assertLogs(None, logging.INFO)
        self.assertEqual(extension_source.extensions[0].status[0], ExtensionStatus.NOT_LOADED)