# -*- coding: utf-8 -*-
import unittest

from blackfennec_doubles.double_dummy import Dummy
from blackfennec.extension.extension_api import ExtensionApi


class ExtensionApiTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.presenter_registry = Dummy('PresenterRegistry')
        self.type_registry = Dummy('TypeRegistry')
        self.interpretation_service = Dummy('InterpretationService')
        self.view_factory = Dummy('ViewFactory')
        self.view_factory_registry = Dummy('ViewFactoryRegistry')
        type_loader = Dummy('TypeLoader')

        self.extension_api = ExtensionApi(
            self.presenter_registry,
            self.type_registry,
            self.interpretation_service,
            self.view_factory,
            self.view_factory_registry,
            type_loader
        )

    def test_can_construct(self):
        self.assertIsNotNone(self.extension_api)
    
    def test_presenter_registry_getter(self):
        self.assertEqual(self.extension_api.presenter_registry, self.presenter_registry)
        
    def test_type_registry_getter(self):
        self.assertEqual(self.extension_api.type_registry, self.type_registry)

    def test_interpretation_service_getter(self):
        self.assertEqual(self.extension_api.interpretation_service, self.interpretation_service)