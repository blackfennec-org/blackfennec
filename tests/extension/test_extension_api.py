# -*- coding: utf-8 -*-
import unittest

from doubles.double_dummy import Dummy
from src.extension.extension_api import ExtensionApi


class ExtensionApiTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.presenter_registry = Dummy('PresenterRegistry')
        self.type_registry = Dummy('TypeRegistry')
        self.navigation_service = Dummy('NavigationService')
        self.interpretation_service = Dummy('InterpretationService')

        self.extension_api = ExtensionApi(
            self.presenter_registry,
            self.type_registry,
            self.navigation_service,
            self.interpretation_service
        )
        
    def tearDown(self) -> None:
        self.presenter_registry = None
        self.type_registry = None
        self.navigation_service = None
        self.interpretation_service = None

    def test_can_construct(self):
        pass
    
    def test_presenter_registry_getter(self):
        self.assertEqual(self.extension_api.presenter_registry, self.presenter_registry)
        
    def test_type_registry_getter(self):
        self.assertEqual(self.extension_api.type_registry, self.type_registry)
        
    def test_navigation_service_getter(self):
        self.assertEqual(self.extension_api.navigation_service, self.navigation_service)
        
    def test_interpretation_service_getter(self):
        self.assertEqual(self.extension_api.interpretation_service, self.interpretation_service)
