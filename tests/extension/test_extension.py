# -*- coding: utf-8 -*-
import unittest

from doubles.double_dummy import Dummy
from doubles.extension.double_extension_loading_service import ExtensionLoadingServiceMock
from doubles.extension.double_extensions.create_failing_extension.double_create_failing_extension import \
    CreateFailingExtensionMock
from doubles.extension.double_extensions.destroy_failing_extension.double_destroy_failing_extension import \
    DestroyFailingExtensionMock
from doubles.structure.double_boolean import BooleanMock
from doubles.structure.double_map import MapMock
from doubles.structure.double_string import StringMock
from src.extension.extension import Extension
from src.extension.extension_status import ExtensionStatus


class ExtensionTestSuite(unittest.TestCase):
    def test_can_construct(self):
        extension = Extension(
            Dummy('ExtensionLoadingService'),
            Dummy('ExtensionSource')
        )

    def test_can_construct_with_map(self):
        data = dict()
        data[Extension.NAME_KEY] = StringMock('name')
        data[Extension.LOCATION_KEY] = StringMock('location')
        data[Extension.ENABLED_KEY] = BooleanMock(True)

        data_map = MapMock(data)
        Extension(
            Dummy('ExtensionLoadingService'),
            Dummy('ExtensionSource'),
            data_map
        )

    def test_can_construct_with_empty_map(self):
        data = dict()
        data_map = MapMock(data)
        Extension(
            Dummy('ExtensionLoadingService'),
            Dummy('ExtensionSource'),
            data_map
        )
        self.assertIn(Extension.NAME_KEY, data)
        self.assertIn(Extension.LOCATION_KEY, data)
        self.assertIn(Extension.ENABLED_KEY, data)

    def test_name_getter(self):
        data = dict()
        data[Extension.NAME_KEY] = StringMock('name')

        data_map = MapMock(data)
        extension = Extension(
            Dummy('ExtensionLoadingService'),
            Dummy('ExtensionSource'),
            data_map
        )

        self.assertEqual(extension.name, data[Extension.NAME_KEY].value)

    def test_name_setter(self):
        name = StringMock('name')
        extension = Extension(
            Dummy('ExtensionLoadingService'),
            Dummy('ExtensionSource')
        )
        extension.name = name
        name.parent = extension
        self.assertEqual(extension.name, name)

    def test_location_getter(self):
        data = dict()
        data[Extension.LOCATION_KEY] = StringMock('location')

        data_map = MapMock(data)
        extension = Extension(
            Dummy('ExtensionLoadingService'),
            Dummy('ExtensionSource'),
            data_map
        )
        self.assertEqual(extension.location, data[Extension.LOCATION_KEY].value)

    def test_location_setter(self):
        location = StringMock('location')
        extension = Extension(
            Dummy('ExtensionLoadingService'),
            Dummy('ExtensionSource')
        )
        extension.location = location
        location.parent = extension
        self.assertEqual(extension.location, location)

    def test_enabled_getter(self):
        data = dict()
        data[Extension.ENABLED_KEY] = BooleanMock(True)

        data_map = MapMock(data)
        extension = Extension(
            Dummy('ExtensionLoadingService'),
            Dummy('ExtensionSource'),
            data_map
        )

        self.assertEqual(extension.enabled, data[Extension.ENABLED_KEY].value)

    def test_enabled_setter(self):
        extension = Extension(
            Dummy('ExtensionLoadingService'),
            Dummy('ExtensionSource')
        )
        extension.enabled = True
        self.assertTrue(extension.enabled)

    def test_source_getter(self):
        source = Dummy('ExtensionSource')
        extension = Extension(
            Dummy('ExtensionLoadingService'),
            source
        )

        self.assertEqual(extension.source, source)

    def test_source_setter(self):
        extension = Extension(
            Dummy('ExtensionLoadingService'),
            Dummy('ExtensionSource')
        )
        source = Dummy('new ExtensionSource')
        extension.source = source
        self.assertEqual(extension.source, source)

    def test_status_getter(self):
        extension = Extension(
            Dummy('ExtensionLoadingService'),
            Dummy('ExtensionSource')
        )

        self.assertEqual(extension.status[0], ExtensionStatus.NOT_LOADED)

    def test_status_setter(self):
        extension = Extension(
            Dummy('ExtensionLoadingService'),
            Dummy('ExtensionSource')
        )
        status = (ExtensionStatus.LOAD_FAILED, None)
        extension.status = status
        self.assertEqual(extension.status, status)

    def test_underlay_getter(self):
        data = dict()
        data[Extension.NAME_KEY] = StringMock('name')
        data[Extension.LOCATION_KEY] = StringMock('location')
        data[Extension.ENABLED_KEY] = BooleanMock(True)

        data_map = MapMock(data)
        extension = Extension(
            Dummy('ExtensionLoadingService'),
            Dummy('ExtensionSource'),
            data_map
        )
        self.assertEqual(extension.underlay, data_map)

    def test_load_extension(self):
        extension_api = Dummy('ExtensionApi')
        extension_loading_service = ExtensionLoadingServiceMock()
        extension = Extension(
            extension_loading_service,
            Dummy('ExtensionSource'),
            name='test-extension',
            location=['src.doubles.extension.extensions.valid_extension'],
            enabled=True
        )
        extension.load(extension_api)
        self.assertEqual(extension.status[0], ExtensionStatus.LOADED)

    def test_load_failing_extension(self):
        extension_api = Dummy('ExtensionApi')
        extension_loading_service = ExtensionLoadingServiceMock(fail_loading=True)
        extension = Extension(
            extension_loading_service,
            Dummy('ExtensionSource'),
            name='test-extension',
            location=['src.doubles.extension.extensions.valid_extension'],
            enabled=True
        )
        with self.assertRaises(ValueError):
            extension.load(extension_api)
        self.assertEqual(extension.status[0], ExtensionStatus.LOAD_FAILED)

    def test_load_create_failing_extension(self):
        extension_api = Dummy('ExtensionApi')
        extension_loading_service = ExtensionLoadingServiceMock(load_extension=CreateFailingExtensionMock())
        extension = Extension(
            extension_loading_service,
            Dummy('ExtensionSource'),
            name='test-extension',
            location=['src.doubles.extension.extensions.valid_extension'],
            enabled=True
        )
        with self.assertRaises(ValueError):
            extension.load(extension_api)
        self.assertEqual(extension.status[0], ExtensionStatus.CREATE_FAILED)

    def test_unload_extension(self):
        extension_api = Dummy('ExtensionApi')
        extension_loading_service = ExtensionLoadingServiceMock()
        extension = Extension(
            extension_loading_service,
            Dummy('ExtensionSource'),
            name='test-extension',
            location=['src.doubles.extension.extensions.valid_extension'],
            enabled=True
        )
        extension.load(extension_api)
        extension.unload(extension_api)
        self.assertEqual(extension.status[0], ExtensionStatus.NOT_LOADED)

    def test_unload_destroy_failing_extension(self):
        extension_api = Dummy('ExtensionApi')
        extension_loading_service = ExtensionLoadingServiceMock(load_extension=DestroyFailingExtensionMock())
        extension = Extension(
            extension_loading_service,
            Dummy('ExtensionSource'),
            name='test-extension',
            location=['src.doubles.extension.extensions.valid_extension'],
            enabled=True
        )
        extension.load(extension_api)
        with self.assertRaises(ValueError):
            extension.unload(extension_api)
        self.assertEqual(extension.status[0], ExtensionStatus.UNLOAD_FAILED)