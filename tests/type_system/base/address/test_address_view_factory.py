import unittest

from doubles.interpretation.interpretation import InterpretationMock
from doubles.structure.map import MapMock
from src.type_system.base.address.address_view import AddressView
from src.type_system.base.address.address_view_factory import AddressViewFactory


class AddressViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        AddressViewFactory()

    def test_can_create_map_view(self):
        factory = AddressViewFactory()
        view = factory.create(InterpretationMock(MapMock()))
        self.assertIsInstance(view, AddressView)
