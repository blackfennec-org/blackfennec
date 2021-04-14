import unittest

from doubles.core import MapMock
from doubles.core.interpretation import InterpretationMock
from src.base.types.address.address_view import AddressView
from src.base.types.address.address_view_factory import AddressViewFactory


class AddressViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        AddressViewFactory()

    def test_can_create_map_view(self):
        factory = AddressViewFactory()
        view = factory.create(InterpretationMock(MapMock()))
        self.assertIsInstance(view, AddressView)
